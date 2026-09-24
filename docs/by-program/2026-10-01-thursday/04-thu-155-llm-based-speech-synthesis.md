# LLM Based Speech Synthesis

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕基于语言模型的语音合成：解码顺序、束搜索效率、稳定性幻觉、混合骨干加速、块离散扩散并行生成，以及自然语言意图驱动的通用合成。主线是在保持可懂度与表现力的同时，纠正自回归 TTS 的顺序偏见、退化与算力瓶颈，并拓宽输入接口。

解码与对齐方面，掩码扩散框架显示从左到右并非最优，反向与置信度自适应顺序更优；注意力引导与 OAS 指标抑制重复/漏读等稳定性幻觉；SaVE-Beam 拆开搜索与评估以实用化最大化解码。架构方面，MamTra 交织 Mamba 与 Transformer 并知识蒸馏；DLLM-TTS 在块内并行掩码扩散；Bagpiper-TTS 先推理用户意图得到富说明再合成，覆盖多说话人、意图到语音、角色扮演与歌声等。

## 论文技术总结

# Decoding Order Matters in Autoregressive Speech Synthesis

- 论文编号：1339
- 报告人：Minghui Zhao
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26e_interspeech.pdf

## 问题
自回归语音合成默认从左到右生成，但声学依赖含全局韵律与前后协同发音；解码顺序是否最优、如何在统一框架比较，尚缺系统研究。

## 方法
用掩码扩散（MDM）训练顺序无关模型，推理可任意置换逐帧解掩。为隔离编码器归纳偏置，对 Mel 做参数无关标量量化（Q=100）并用现成 HiFi-GAN。比较 l2r、r2l、随机、top1 置信自适应、时长引导段内随机，以及 β 控制的随机插值。

## 实验与结果
LJSpeech：r2l 多项客观指标优于 l2r；top1 MOS 3.91（系统输出最高），vocoded 参考 3.99，r2l 3.87，uro 最差 3.50。top1 局部多为右→左连续扩展（ρ_r2l≈0.9）。量化 Mel 仍可被 HiFi-GAN 较好重建。随机性增大时 MCD 降、UTMOS 降，WER 非单调。

## 结论
左到右并非最优；有效顺序常保持局部连续帧簇并偏向局部右到左，以兼顾长程依赖与局部连贯。解码顺序应作为合成质量的关键建模选择。

## 点评
用 MDM + 标量 Mel 把“顺序”从 token 学习中干净拆出，结论有说服力。单说话人朗读语料与帧级更新限制外推；是否迁移到多说话人/神经编解码 token 仍待验证。


# Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis

- 论文编号：1531
- 报告人：Chenlin Liu
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26l_interspeech.pdf

## 问题
LM-based TTS 多依赖采样解码，存在随机不稳定；beam search 虽是最大化解码，但在语音生成中易出现时间坍塌（长时间静音/噪声循环），且推理延迟过高。作者分析发现 beam search 约 98% 时间花在搜索扩展上，评估只占很小比例。

## 方法
提出 SaVE-Beam：将假设扩展与序列打分解耦。轻量 student（自蒸馏，温度 τ=2，强调高概率 token 排序）做 chunk 级 beam 树构建；原 teacher LM 做精确评估与最终选择。Chunk 长度 L，学生扩展后由教师树解码、top-K 过滤，并用类似 speculative decoding 的接受比 rt 与阈值 α 做确定性验收，按接受长度与教师对数概率选路径。搜索阶段对近期窗口 w 内已出现 token 做硬屏蔽（概率置零再归一化），避免软惩罚在最大化解码下仍坍塌。另用动态剪枝保留 top-N 节点。

## 实验与结果
在 CosyVoice 2 上实现，训练集 LibriTTS 与 WenetSpeech4TTS premium，评测 SeedTTS-Eval。相对 TRAD-BS，LM 解码加速约 3.9×–5.1×；相对采样 baseline，en/zh 的 W/CER 分别可降约 50%/33%，速度接近 baseline（如 SaVE-Beam-2h：en TPS 22.21、WER 1.83；zh TPS 23.92、CER 0.84）。RTF 从 TRAD-BS 的 4.95 降到约 1.18–1.19。消融表明硬重复约束对抑制时间坍塌关键；去掉动态剪枝可在 test-hard 上进一步改善 CER。

## 结论
通过搜索–评估解耦、chunk 扩展与硬重复约束，SaVE-Beam 可在接近采样系统实时性的前提下，使最大化 beam 解码在 LM-TTS 中实用，并显著降低生成错误。

## 点评
核心洞察是把昂贵的 beam 扩展交给小模型，把目标函数仍交给原 LM，并用硬结构约束补救语音 token 低信息密度带来的坍塌。与把解码完全交给蒸馏学生不同，质量门槛仍由 teacher 决定；学生引入的受控随机性在 hard 集上甚至可能帮助逃离局部最优，这是设计上的有趣副效应。脆弱点在于 chunk/窗口/α 等超参与 student 容量：太弱会频繁拒收而抵消加速，软惩罚替代硬约束则会重新坍塌。


# Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance

- 论文编号：1345
- 报告人：Shiming Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26x_interspeech.pdf

## 问题
LLM-based TTS 缺少显式 text–speech 对齐，在长文本/难文本上易出现稳定性幻觉（重复、无尽生成、漏读）。早期 cross-attention 单调约束不适配 decoder-only；硬单调注意力又伤自然度；强制对齐标签在大规模数据上难以获得。

## 方法
在 CosyVoice2（Qwen-0.5B，24 层×14 头）上分析自注意力，发现中层存在类似 cross-attention 的“alignment heads”。提出 Optimal Alignment Score（OAS）：对 speech→text 注意力子矩阵用 Viterbi 求最优对齐路径，再取路径概率占比；OAS 与 WER 相关系数约 −0.638。将第 8、9 层半数头指定为对齐头并 mask 到对齐区域，用可微 OAS 正则 LOAS 监督。进一步做 attention-guided CoT 学生训练：用教师最高 OAS 头路径作伪强制对齐；学生预测稀疏重复文本 token（非整段重复）与 progress bar 位置值（L1 + 一阶差分非负约束），且预测文本不回灌输入，减轻伪标签误差累积。

## 实验与结果
WenetSpeech4TTS 从头训 LLM；Seed-TTS-Eval 与 CV3-Eval 上评 hard/common。相对 CV2，CV2 OAS 在 hard 上 WER 分别降约 2.1%/1.6%（Seed hard 13.568%→11.472%；CV3 hard 10.239%→8.657%），SIM/UTMOS 不降。CV2 AG（sparse text + progress bar）进一步到 Seed hard WER 9.984%、CV3 hard 6.660%。稀疏文本监督的 token 准确率明显高于 full text（train 97.10% vs 90.44%）。common 场景 MOS 略升或持平。

## 结论
用 OAS 损失与注意力引导训练，可在难文本上减少 CosyVoice2 的稳定性幻觉，且不明显损害自然度与相似度，且无需真实强制对齐标签。

## 点评
做法抓住的是 decoder-only TTS 里“对齐头可学、可监督”这一结构：先度量再约束，再用伪对齐做 CoT，比硬单调推理更贴合语音连续性。稀疏重复 + progress bar 是对伪标签不准与重复句式的务实修补。潜在脆弱处是对齐头层位与头选择依赖该 backbone 的统计（文中锁定 8–9 层），换模型需重标定；伪对齐质量上限仍受教师稳定性约束。


# MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis

- 论文编号：1031
- 报告人：Tan Dat Nguyen
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26c_interspeech.pdf

## 问题
LLM-TTS 依赖自回归 Transformer，长序列下自注意力二次复杂度与 KV cache 膨胀，限制播客/有声书/边缘部署。纯 Mamba 线性高效但全局上下文与表达力不足；已有混合方案多需昂贵从头预训练且细节不公开。

## 方法
提出 MamTra：在预训练 CosyVoice 2 上按多种策略（Interleaved BlockBeg/End、Contiguous Front/Middle/Back/Sandwich、数据驱动 Importance）把部分 Transformer 换成 Mamba，比例 1:1 到 1:11。用注意力线性化与 SSM 的结构对应，把教师 Q/K/V 投影初始化到 Mamba 的 C/B/x。再用多层蒸馏恢复性能：L = LCE + Llogits（skew KL）+ Lemb（token embedding MSE）。训练只用约 0.5k 小时 LibriTTS（约为教师英语数据的 2%）。

## 实验与结果
评测 Seed-TTS-eval test-en 与 LibriTTS test-clean。MamTra 1:1（BlockBeg）相对 CosyVoice 2：VRAM 可降约 34%，每 token FLOPs 在上下文 2048 时最多省约 1.4×10^11；WER 仅绝对升约 0.25%（2.03→2.28），NMOS/UTMOS/SSIM 接近教师。更激进 1:11 时可懂度明显下降。BlockBeg 在低成本扫描中 CE/WER 更稳；高替换比时 WER 重要性选层更有效。消融显示去掉 LCE/Llogits/Lemb 都会抬高 WER；重用预训练权重收敛远快于 Xavier/Kaiming。

## 结论
通过结构化替换、权重迁移与多层蒸馏，MamTra 可在很少数据上恢复教师级质量，并显著降低推理显存与计算，适合内存受限的长上下文 TTS。

## 点评
价值在“转换预训练 Transformer→混合骨干”而非从零训 SSM：把二次注意力瓶颈换成局部线性状态，同时保留少量全局层。BlockBeg + 适度替换比是效率–质量甜点；过度替换（1:11）会跌破可懂度底线。脆弱点包括蒸馏对教师分布的依赖，以及 Importance/WER 选层在新域是否可迁移。


# DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis

- 论文编号：788
- 报告人：Wasim Madha
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/madha26_interspeech.pdf

## 问题
自回归 codec LM 音质与可懂度好，但需大规模数据且逐 token 解码延迟高；非自回归流匹配/扩散虽并行，常需显式时长建模或对齐弱，易漏词/重复。块离散扩散（BD3-LM）在文本上有效，尚未用于条件语音 codec 生成。

## 方法
DLLM-TTS 把 TTS 建成对 X-Codec2（单流 FSQ，|V|=6561，50 Hz）token 的条件块离散扩散。序列切成块（默认 B=32，约 0.64 s），块内掩码扩散并行预测，块间顺序生成。用 staircase attention：噪声块内双向、对前序干净块因果、干净块内因果。训练最小化掩码位置交叉熵；用 EOS 处理变长，无需显式时长。0.6B Transformer 自 Qwen2 初始化。推理：参考文本+参考 codec + 全掩码生成段；每块最多 T 步置信度采样（τ=0.6），可提前停止；默认 T=16 时 RTF=0.15。

## 实验与结果
两阶段：Emilia 采样 16K 小时 20 epoch，再 4K 小时高质量合成数据微调，合计约 20K 小时。Seed-TTS-eval（英）：WER 2.25、CER 1.05、SIM 0.750、MOS 4.25，接近或优于若干更大数据/参数系统。消融：T 从 8→32，WER 14.58%→2.25%；T=64 反而变差。B=32 优于 8/16。掩码目标被视为隐式数据增强，解释相对自回归的数据效率（相对 60K–250K 小时约 3–12× 减少）。

## 结论
块离散扩散可在无显式时长标注下兼顾局部声学一致性与跨块文本对齐，以较小数据与 RTF 0.15 实现实用、有竞争力的零样本 TTS。

## 点评
关键是把“块内并行 + 块间因果”对准语音的局部相干与全局对齐需求，staircase mask 替代了时长模型。速度–质量由 B 与 T 直接调节；T 过大变差说明过度去噪并非单调受益。相对纯 NAR，保留了顺序结构；相对纯 AR，换来并行与数据增强。脆弱处包括块边界伪影风险（文中主观 MOS 未明显受损）以及对 codec 单流设定的依赖。


# Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis

- 论文编号：873
- 报告人：Haoran Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tian26_interspeech.pdf

## 问题
传统 TTS 依赖固定槽位式输入（文本+预定义元数据），与真实用户自然语言请求不匹配；多说话人对话、角色扮演、歌声等任务又难以在单一管线中灵活统一。

## 方法
Bagpiper-TTS 以 Bagpiper-Base（Qwen3-8B-Base + 50 Hz 多流 X-Codec，8 codes/帧，600B token 预训练）为骨干，采用 Planning–Caption–Generation：先文本规划理解意图，再生成长达数百 token 的 rich caption（转写+副语言/声学蓝图），最后据此合成语音。微调数据用六步仿真：音频精选→自动 caption→WER 过滤→LLM 反推用户请求→规划过程仿真→LLM 一致性校验（均分>3.5）。覆盖 classical / multi-talker / intent-to-speech / role-play / SVS / general-purpose，共约 738k 样本。推理对文本与语音用解耦 Top-k，语音侧 CFG λ=3。

## 实验与结果
SFT 2 epoch。Seed-TTS-Eval (En) classical WER 1.7%（Qwen3-TTS 1.5%，CosyVoice 2 2.6%）。四类进阶任务：LLM-as-a-judge 均分约 4.09，人工 MOS 均约 3.69；如 Multi-Talker WER 4.2 / TF 4.23，SVS WER 7.2 / TF 4.60（相对 YuE WER 11.0）。定性显示能处理倒序计数、委婉批评等需推理的请求。系统不接受参考音频，故未测 speaker similarity。

## 结论
以自然语言与 rich caption 为统一接口，单一模型可覆盖多种合成应用，classical TTS 可懂度接近前沿专用系统，进阶任务在裁判与主观评价上整体可用。

## 点评
核心是把“槽位控制”换成“可扩写的文本蓝图”，让预训练 caption↔speech 对齐直接承接任意用户话术。数据仿真与严格校验决定上限；general-purpose 子集试图覆盖未定义场景。脆弱点包括 caption 幻觉需 WER/多模态校验兜底、相对专用模型在部分主观分上仍有差距，以及无参考音色克隆能力。

