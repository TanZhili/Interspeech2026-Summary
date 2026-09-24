# Search Methods and Inference Algorithms

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral
- Area：9
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦解码与搜索算法本身：如何在保持或提升识别质量的同时降低延迟与计算。多条线汇合于“用约束或草稿加速，而不是只堆更大模型”——阿拉伯语变音符恢复用 CTC + 字符级 diacritization lattice 硬约束做非自回归语音到文本变音；Whisper-CD 用多负例对比解码（噪声、静音、时移）抑制长音频幻觉且免训练。

投机/半自回归解码成为效率主力：SASD 在联合 CTC-attention 上对高置信 CTC token 直接采用、对难 token 用 attention 精炼；自投机方案以 CTC 编码器为草稿、LLM 一次前向校验并在失败时回退 AR。NAR-MBR 则从 NAR 输出分布采样并以期望效用最大化替代单纯最大概率，且单次前向即可多样本。

另有工作给出语音处理中自回归解码的广义形式化与纳入标准，澄清“何为 AR 搜索”以便做以搜索策略为中心的消融。整体瓶颈是长音频错误累积、NAR 不确定性与 AR 速度之间的张力；方向是约束解码、对比负例、投机草稿与风险最小化解码。

## 论文技术总结

# Constrained CTC decoding for Efficient Diacritic Restoration

- 论文编号：3220
- 报告人：Rufael Marew
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marew26_interspeech.pdf

## 问题
阿拉伯语文本常缺标音符号，纯文本复原对同形异音仍模糊；已有语音+文本多模态复原有效但计算重、跨域弱。需在保持字母骨架不变的前提下，用语音高效恢复 diacritics。

## 方法
在给定语音与无标音参考 \(u\) 时，用 CTC ASR（Wav2vec2-XLSR 微调）预测含字母与复合标音标签的序列；推理时由 \(u\) 构图字符级 diacritization lattice（字母固定、其后通配符位只允许 diacritic/blank），与 CTC 解码图组合或限制 beam，实现部分强制对齐式约束解码。无标音用 CTC blank 表示。对比 Text-only 与 Text+ASR 基线（后者可额外用 Tashkeela 文本预训练）。

## 实验与结果
数据：ClArTTS（CA，12h 训 / 0.3h 测）、ArVoice 1+3（MSA，6h / 0.9h）。匹配 ClArTTS：Ours WER/DER 11.21 / 3.53，接近 Text+ASR。跨域与联合训练：Ours 明显更稳（如 ClArTTS 训→ArVoice：DER 12.04 vs Text+ASR 19.21；联合训练 ClArTTS DER 3.80、ArVoice 8.69）。bootstrap 95% CI 显示相对 Text+ASR 的 DER 改善显著。

## 结论
约束 CTC 解码在 CA/MSA 上优于或持平多模态基线，且更精简高效，可直接作带标音 ASR 或对无标音标注语音做复原，利于阿拉伯语数据策展。

## 点评
把“字母骨架硬约束”下沉到解码图，避开额外文本编码器与融合训练，效率与跨域表现合理。依赖已有无标音参考；未覆盖方言且基线独享大规模文本预训，公平性上作者已说明。


# Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding

- 论文编号：3058
- 报告人：Hoseong Ahn
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ahn26b_interspeech.pdf

## 问题
Whisper 等长音频编解码 ASR 易产生静音幻觉、跨段重复环与内容漏识；启用上一段转写作上下文时错误会放大，beam search 也难纠正高置信幻觉。

## 方法
提出训练无关的 Whisper-CD：每步用干净音频 logits 与三种声学扰动负样本对比——高斯噪声（SNR 10 dB）、全零 silence、波形左移 \(\Delta_s=7\) s；用 log-sum-exp（\(\tau=1\)）聚合负 logits，\(\ell^{CD}=(1+\alpha\tau)\ell^{pos}-\alpha\tau\log(\frac{1}{K}\sum\exp(\ell^{neg}/\tau))\)。编码器与解码器路径批并行；保持语言识别与时间戳等能力。默认开 previous-context、greedy。

## 实验与结果
五集长音频：Large-v3-Turbo 上 CORAAL 38.75→14.43（最多约 24.3 pp 降幅），Earnings22 33.25→16.16 等全面下降；Large-v3 基线因重复环 WER 可 >100%，CD 后大幅收敛但仍高于 Turbo。吞吐高于 beam=5（如 Turbo CORAAL 147 vs 99 tokens/s）。消融：单扰动不如多负样本；\(\alpha\) 过大伤干净集（TED-LIUM）。

## 结论
多负样本对比解码可在无重训条件下抑制长音频幻觉与重复，相对 greedy 开销有限、显著快于 beam search，可作已部署 Whisper 的即插替换。

## 点评
把对比解码从视觉/文本迁到 ASR，用声学退化暴露模型先验，直接打在上下文传递放大错误的链路。\(\alpha\) 与模型尺度敏感，Large-v3 深重复环仍难完全拉回；decoder-only ASR 如何注入扰动路径仍开放。


# Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding

- 论文编号：1953
- 报告人：Long Wu
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/wu26g_interspeech.pdf

## 问题
端到端 ASR 中，AED 的自回归解码精度高但难以并行；NAR 虽快但语义建模与对齐常受损。现有 attention rescoring 等混合解码依赖 CTC prefix beam search 或复杂 CTC prefix score，成为吞吐瓶颈，且与 streaming chunk 解码不够契合。

## 方法
提出 Semi-Autoregressive Speculative Decoding（SASD），基于 joint CTC-attention 框架、无需重训：
1. 用 CTC greedy search 得到初假设（draft）；
2. 以 CTC 峰值概率为置信度，低于阈值 \(P_{\mathrm{thres}}\)（实验取 0.99）的位置记为低置信 token；
3. 高置信位置直接采用 CTC 结果；低置信位置用 attention decoder 做 speculative beam search，将 attention 分数与 CTC 分数插值后选 top-\(k\)；
4. 注意 decoder 只在原索引上替换 token，输出长度与 CTC 假设严格一致。
该设计避免精确 CTC prefix scoring，并兼容 chunk-based streaming。

## 实验与结果
数据：AISHELL-1、WenetSpeech（TestNet / TestMeeting）、内部约 33 小时工业测试集。在 WENET 五个预训练中文模型上评测。
- AISHELL-1（u2++ conformer）：SASD CER 4.73%（full），与 attention rescoring 4.77% 相当，优于 CTC greedy 5.18%；GPU RTF 0.0188，约为 attention rescoring（0.0535）的约 2.8 倍加速；batch=8 时 RTF 0.0098。
- WenetSpeech：与 attention rescoring 接近（如 TestNet full：9.40 vs 9.26），chunk 减小时更稳。
- 工业模型：CER 4.58 vs E2E 4.57，约 3.5× 加速。
摘要称相对 SOTA attention-rescoring 约 2.8×–3.5× 加速且 CER 可比。

## 结论
SASD 在解码阶段对“易”token 走 NAR（CTC）、对“难”token 走 AR（attention），省去 CTC prefix scoring / CTC beam search，在公开与工业数据上取得接近 rescoring 的 CER 与更高推理速度。

## 点评
做法本质是 token 级 draft-and-verify：用 CTC 峰度当置信门控，把昂贵的 attention 算力集中在少数低置信位置，因而延迟可接近 CTC greedy。强在兼容已有 AED、无需额外 draft 模型、对 streaming chunk 友好；脆弱点在于依赖 CTC 置信阈值与假设“多数 token 已足够自信”——若低置信比例升高（难声学条件），AR 修正成本会上升，加速比缩小。


# Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts

- 论文编号：2680
- 报告人：Avihu Dekel
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/saon26_interspeech.pdf

## 问题
Speech-aware LLM（SLM）ASR 精度领先，但自回归逐 token 前向限制吞吐。常规 speculative decoding 常需额外 draft 模型；联合 CTC/attention 虽可加速，但如何在不重训的前提下复用 SLM 自带 CTC 编码器做 draft，并兼顾准确率与 RTFx，仍不清晰。

## 方法
提出 self-speculative decoding（SSD），三步、无需额外 draft 模型：
1. **CTC decode + verify**：CTC greedy 假设；若所有帧级 CTC 输出熵低于 \(\tau_{\mathrm{CTC}}\)，直接接受；
2. **LLM verify**：否则用单次 LLM 前向，按松弛准则检查各 token 似然是否均大于 \(\tau_{\mathrm{SLM}}\)；通过则接受 CTC 假设；
3. **AR fallback**：失败则从最长已验证 CTC 前缀继续自回归解码。
架构为 Conformer CTC encoder + Q-Former adapter + LLM；要求 CTC encoder 在 projector/LoRA 微调时冻结。松弛接受（“plausible”而非精确匹配）用于提高接受率。

## 实验与结果
主模型 granite-speech-4.0-1b（约 1B LLM + 440M CTC encoder），在 HuggingFace Open ASR 及 MLS、CommonVoice 等多语料评测（1×H100，batched）。
- High accuracy（\(\tau_{\mathrm{CTC}}=0.7,\tau_{\mathrm{SLM}}=0.2\)）：Open ASR 平均 WER 5.58%，优于 full AR 的 5.75%，RTFx 相当（548 vs 564）；作者称创纪录 5.58% WER。
- High RTFx（\(\tau_{\mathrm{CTC}}=3.0,\tau_{\mathrm{SLM}}=0.1\)）：Open ASR 平均 WER 6.56%、RTFx 2491，相对 AR 约 4.4× 加速，相对 WER 增约 12%。
- 消融显示双阶段验证在多数 WER–RTFx 区间 Pareto 更优；LLM 验证相对纯 AR 常进一步降 WER，作者归因于 CTC 与 SLM 错误互补。

## 结论
复用冻结 CTC 编码器作 draft、LLM 做验证与回退，可在不重训、不引入独立 draft 模型的情况下同时提升准确率与吞吐。局限：需 CTC 训练的 SLM；仅适用于 ASR；验证失败时整句从失败点 AR，低接受率语料收益有限。

## 点评
核心是“声学接地的 CTC draft + 语言模型验证”：高置信 CTC 可跳过 LLM，而 LLM 接受 CTC 又能纠偏 AR 的语言先验偏差。强在自投机、可调 \(\tau\) 覆盖准确–速度谱；脆弱在依赖 CTC 头质量与 utterance 级接受失败时的整段 AR 回退，对长句与低接受率场景不友好。


# Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition

- 论文编号：2971
- 报告人：Hiroyuki Deguchi
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/deguchi26_interspeech.pdf

## 问题
NAR ASR（如 Mask-CTC）并行解码快，但因 token 独立性与多模态路径不确定性，相对 AR beam search 仍有 WER 差距。标准 MAP 选最高概率路径不一定质量最优；MBR 用期望效用选假设可更稳健，但在 AR 设定下采样与效用计算昂贵。

## 方法
提出 NAR-MBR：在 Mask-CTC 上做无偏采样 + 期望效用（负 WER）最大化，无需额外训练。
1. **采样**：按帧独立从 CTC 分类分布采样多条对齐路径 \(|Z|\)；再按置信度 Bernoulli 采样 mask，用 CMLM 从分类分布填 mask（可用 \(N_{\mathrm{iter}}\) 迭代；\(N_{\mathrm{iter}}=0\) 仅用 CTC）；假设集与伪参考共用同一采样集。
2. **EU 最大化**：选使相对伪参考平均 WER 最小的假设；用去最长公共前后缀、去重缓存、多核并行与 Rust 实现的编辑距离加速。
相对原 Mask-CTC 的确定性 mask + greedy，改为概率采样以服务 Monte Carlo MBR。

## 实验与结果
数据：LibriSpeech、Switchboard、AMI、Web（约 346h 训练）。AR 用 Conformer + CTC 联合解码；NAR/NAR-MBR 用 Mask-CTC（ESPNet）。
- WER：\(N_{\mathrm{iter}}\in\{1,10\}\)、\(|Z|\in\{64,256\}\) 时 NAR-MBR 相对 NAR 在多数集合显著更好（如 LS Clean \(N_{\mathrm{iter}}=1,|Z|=256\)：3.1 vs NAR 3.4；Web 7.3 接近 AR Beam 7.3）。峰值多在 \(N_{\mathrm{iter}}=1\)，增大迭代几乎不再降 WER。
- 速度（相对 AR Beam）：Web 上 \(|Z|=64,N_{\mathrm{iter}}=1\) 约 43.1×，\(|Z|=256\) 约 20.7×；仍快于 AR Greedy，但 \(N_{\mathrm{iter}}=1\) 时 GPU 显存升高（Web 上 \(|Z|=256\) 约 ×5.0）。
- \(|Z|\) 增大 WER 改善并在 ≥64 趋于饱和。

## 结论
利用 NAR 独立性可一次前向廉价采多样本，再用 MBR 缓解多模态不确定性，从而在无重训下优于原 NAR，并相对 AR beam 大幅加速；未来拟扩展到更多模型与任务。显存开销与采样规模是明确边界。

## 点评
把 MBR 的“用样本估期望质量”接到 NAR 的“一次前向可多样本”上，用决策准则补独立性假设的短板，比堆迭代 mask  refinement 更对症。强在训练零改动、\(N_{\mathrm{iter}}=1\) 即可；脆弱在二次效用与多样本带来的 CPU/显存成本，以及效用仍绑定 WER——对其他评价指标需重定义 \(u(\cdot)\)。


# A Generalized Formalism of Auto-Regressive Decoding for Speech Processing

- 论文编号：2768
- 报告人：Julia Gachot
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/gachot26_interspeech.pdf

## 问题
语音处理中序列生成高度依赖自回归搜索，但“AR / next-token / MAP beam”等概念定义分散，推测解码、NAR、随机采样等常被用不同名称复述相近机制，导致难以系统比较、消融与报告。现有分类常按任务或“确定性 vs 随机”切分，跨任务迁移结论困难。

## 方法
将生成表述为 \((M, g_{\mathrm{AR}})\)，在 SIPC（随机整数规划）视角下给出 AR 纳入准则与模块化形式：
- **模型假设**：网络估计有限字母表上的条件概率，并用解码状态/先验更新；
- **解码假设**：迭代局部搜索，且至少一次用目标函数（如 MAP）更新有限候选集。
每次迭代 \(f^t_{(M,g_{\mathrm{AR}})}(Y_t,Z_t)\) 由四步组成：**Estimation**（条件 PMF）、**Decision**（目标函数选/扩候选）、**Update of prior**（维护 \(Z_t\)）、**Termination test**。报告解码策略即报告初始条件与上述设计选择。用该框架形式化 beam search 与 temperature sampling，并讨论 speculative / “NAR” 边界案例的纳入与排除。

## 实验与结果
本文以形式化与讨论为主，未报告新的 ASR/MT 数值实验。在 2018–2025 的十篇相关工作上做归类：按解码假设排除 1 篇非 SIPC；模型假设下 speculative 与部分所谓非 AR 方法可纳入。进一步说明可用“用基线步骤替换某一步”做结构消融，以隔离 estimation / decision / prior / termination 的贡献。

## 结论
作者给出统一的 AR 搜索形式与报告清单，用以跨任务比较与设计聚焦解码的消融；主张摆脱“仅是似然最大化器”的笼统描述，转向递推关系与模块设计视角。

## 点评
贡献是元方法：把解码拆成可复用的结构组件，便于把 speculative、多样性惩罚等放到同一坐标系里比较。强在澄清报告要素与消融接口；作为纯理论/分类工作，正文没有对照实验数字，实际收益取决于社区是否采用该报告约定。技术分类虽挂在 asr-decoding，内容覆盖更广的序列生成搜索。

