# Robust ASR: Uncertainty and Confidence

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：8
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕稳健 ASR 的训练目标、上下文偏置、不确定性与幻觉抑制。CTC/音素识别侧用课程式过渡目标缓解 blank 主导与不稳对齐；非自回归精炼引入一致性正则，并可借快速解码为半监督生成伪标签。热词/实体偏置则结合对比正则、偏置分数估计与不确定性门控的音素级解码时偏置。

另一主线是噪声与低可懂场景：干净—噪声双视角自蒸馏、智通度引导的观测融合（observation addition），以及耳语场景下的自监督不确定性学习与置信融合解码。Speech-LLM ASR 侧用因果中介剖析幻觉来源，并提出小语言模型对齐减轻文本 token 过度注意；置信估计则用基于秩距离的连续目标改进多种架构上的 CEM。

## 论文技术总结

# Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition

- 论文编号：1040
- 报告人：Izabela Krysińska
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/krysinska26_interspeech.pdf

## 问题
CTC 音素识别早期易陷入 blank 主导的“抑制期”，梯度弱、对齐难学；全程细粒度音素目标加剧该问题。

## 方法
Transitional Objective Learning（TOL）：课程式动态加权多个不同粒度 CTC 目标（粗语音特征类→细音素），权重由重要性分数经 Softmax 随 epoch 转移，总损失为加权和。在英语 TIMIT、波兰 LnNor、法语 Vibravox 等上对比标准 CTC 微调。

## 实验与结果
相对基线 PER 相对降约 9.5–14.3%（TIMIT 0.049→0.044 等），t 检验显著。验证曲线显示更快进入 peaking、更早收敛；梯度范数与方差更低。消融表明层级过渡优于仅正则化效应。

## 结论
由粗到细的目标过渡可缩短 blank 主导期、加速收敛并降低 PER，提升 CTC 音素识别稳定性。

## 点评
针对 CTC 经典 blank 病理做课程化损失调度，实现简单、跨语种证据一致。粗类如何定义、权重日程是否需按语种重调，文中依赖声学特征层级；与中间 CTC 正则等方法的直接对比仍可加强。


# Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization

- 论文编号：1471
- 报告人：Wanting Huang
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26i_interspeech.pdf

## 问题
一致性正则（CR）已提升 CTC，但在 Align-Refine 等非自回归迭代对齐精炼及半监督伪标签场景中如何系统结合仍不足。

## 方法
Align-Consistency：对 Align-Refine（CTC 初对齐 + S=2 步 Transformer 精炼）的 base 与各精炼步，在 SpecAugment 双视图上施加 CR；半监督时用非 AR 解码在线生成伪标签并继续训练。ESPnet Conformer，评 LibriSpeech LS-100/960 与 Libri-Light 无标数据。

## 实验与结果
监督：相对 CR-CTC，test WER LS-100 约 12.2/26.7→10.0/22.9，LS-960 4.3/9.9→3.3/7.4；CR 作用于 CTC 与精炼步可叠加。半监督：从 LS-100 模型用 960h 无标可至约 4.3/9.6，再加 LL-6000 至 3.8/9.1；Align-Consistency 伪标签优于纯 CTC。

## 结论
非 AR 精炼与 CR 互相增益；快速并行解码适合在线伪标签，半监督下 CR 对噪声监督仍稳健。

## 点评
把 CR 从纯 CTC 扩到对齐精炼全链路，并证明伪标签质量受益于非 AR，逻辑闭环。超参（α、λ、S）依赖验证调参；未与强 AR 自训练主流路线同协议全面对比。


# COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation

- 论文编号：1097
- 报告人：Jhih-Rong Guo
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/guo26b_interspeech.pdf

## 问题
SLM 语境偏置在大列表与多实体共现时易因上下文窗口与干扰项退化；既往判别损失在多正样本上训练易塌或需辅助 log loss。

## 方法
COALA：冻结骨干 + LoRA，用判别投影器把实体 token 隐状态映射为长度归一化匹配分；提出 Multi-Positive Discriminative Loss（MPD）与 Decoupled Point-wise Discriminative Loss（DPD）缓解多正样本梯度冲突。推理可用 Biasing Target Identification（Top-K 打分）过滤后再送 ASR 提示，并用 `<unbiased>` 阈值。

## 实验与结果
LibriSpeech：DPD 在 test-clean 上 Recall#20 达 99.09%，可独立收敛；相对 Bias-Loss/CTC-Filter 等更稳。加 BTI 后，在 N=500/1000/5000 偏置列表上 B-WER 显著优于无筛选的大列表直接偏置，可扩展到大 N 而避免 OOM。

## 结论
专用打分空间 + 多正样本稳健目标，可在复杂多实体场景提升语境偏置，兼顾列表规模与 B-WER。

## 点评
把“从大列表筛相关实体”从生成分布中拆出，切中 SLM 窗口瓶颈。无偏置时基线 WER 偏高，对比需看相对增益；大 N 下仍依赖 Top-K 启发式与阈值，召回–误召平衡值得更细分析。


# UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models

- 论文编号：1577
- 报告人：Yong-Jie Hou
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hou26_interspeech.pdf

## 问题
热词语境偏置在 BPE 切分下脆弱；拼音/语音匹配可提召回，但易过偏置与同音误触发。需免训练、可栅控的解码期方案。

## 方法
UGPCB：参数无关 logit bridge 取声学后验熵作不确定性门控，仅在高熵步注入偏置；字素 BPE trie 与拼音（带调/不带调）双轨匹配，并用字素–拼音对比惩罚抑制纯拼音假阳性；配合 N-best 重打分。在 Dolphin 基座、SeACo 测集评估，并测至 1000 干扰项。

## 实验与结果
完整系统：召回 84.19%、F1 90.81%（基线 F1 80.85%）、CER 5.60%；相对文本浅融合召回 +4.68 pp。熵门控降误报；1000 干扰下仍有约 +14.26% 召回增益。精度下降约 0.78 pp 量级、与部分对比差异不显著。

## 结论
不确定性门控 + 双模态拼音匹配可在免训练解码中提升热词召回并抑制过偏置/同音幻觉，适合大模型热词应用。

## 点评
面向普通话同音与 BPE 截断的设计很具体，免训练部署友好。依赖拼音工具规范读音、未枚举多音字；门控阈值与惩罚强度需场景调参，过严会牺牲召回（消融 B3 已体现）。


# Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs

- 论文编号：2229
- 报告人：Vinayak Abrol
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bhooi26_interspeech.pdf

## 问题
Speech-LLM ASR 常更新骨干；严格仅训 adapter 时，自回归 LLM 易漂移，而扩散 LLM 的全局精炼是否更耐 adapter-only 瓶颈仍待验证。

## 方法
冻结语音编码器与 LLaDA 等扩散 LLM，仅训练深度 MLP adapter（帧堆叠 + LayerNorm/SiLU）做跨模态投影；对比同设定下的自回归 Llama 等。在 LibriSpeech 多数据量划分评 WER 与 RTFx。

## 实验与结果
960h：test-clean WER 2.807%，相对同设定 AR 约 54% 相对改进，RTFx 约 12.3×（吞吐约 +45%）。低资源多 100h 子集上 dLLM 方差更低、更稳。消融：归一化与手工帧堆叠优于可学习卷积时序；过强 SpecAugment 略伤精度。

## 结论
在严格 adapter-only 协议下，扩散 LLM 比 AR 更可扩展、更快，适合多模态 ASR 集成。

## 点评
把“只训桥”作为硬约束来对比 AR vs 扩散，结论有部署意义。SOTA 数字需放在同冻结协议下理解，未必优于全参微调大系统；adapter 设计消融扎实，但编码器/LLM 选型固定时外推有限。


# DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition

- 论文编号：3232
- 报告人：Jaeeun Baik
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/baik26_interspeech.pdf

## 问题
噪声增强微调常在干净条件掉点并过拟合特定噪声；需在提升噪声稳健的同时保住干净识别。

## 方法
DASH：双分支自蒸馏——干净教师（EMA）与噪声学生；多层编码器隐表示经投影与原型（k-means）分配，用温度 KL 对齐干净–噪声视图。两阶段：无标签蒸馏预训练（约 5k 步，~4% 微调时长）再标准 ASR 微调。骨干 Parakeet-TDT-CTC-110m；噪声视图默认 SpecAugment+加性噪声。

## 实验与结果
相对仅微调，DASH 在 test-clean/other 与多种 SNR 噪声上更优（如 clean 2.02 / other 4.25 vs 基线 2.58/5.41、仅微调 2.14/4.40），并缓解干净–噪声折中。多层蒸馏优于仅末层；EMA 更新有益。Noisy→Clean 配置显示蒸馏阶段本身可赋予噪声不变性。

## 结论
多层原型自蒸馏能以很小开销学习干净–噪声一致性，提升稳健性且不牺牲干净精度。

## 点评
把稳健性做成标签无关预训练阶段，避开与 ASR 损失联合优化的干扰，工程上干净。噪声类型仍偏仿真混合；与 VIC/CR-CTC 等一致性方法的直接头对头对比可再加强。


# Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition

- 论文编号：879
- 报告人：Gaopeng Xu
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26g_interspeech.pdf

## 问题
耳语缺少基频与谐波结构，声学不确定度高，导致常规 ASR 陷入准确率–可靠性权衡：要么对耳语识别差，要么为提高灵敏度而更容易把噪声幻听成语音。现有伪耳语数据增强存在分布差距，静态投影适配又难以随耳语变化动态调节。

## 方法
在 Qwen2-Audio 上增加轻量 Uncertainty Perception Module（UPM）与 Confidence-Fused Decoding。UPM 用两个自监督任务感知信号质量：F0 轮廓预测（MSE，由预测误差得到帧级置信度）与掩码频谱重建（时间平均得到全局不确定性向量）。解码时，全局向量经 MLP 变成 instruction embedding 作为系统提示；帧级置信度作为可学习标量加权的加性偏置调制 LLM 对声学帧的注意力。训练分三阶段：仅训 UPM 自监督 → 编码器/适配器/UPM/接口联合、LLM 冻结 → 端到端（ASR + 辅助损失，LLM 用 LoRA）。

## 实验与结果
基座为 Qwen2-Audio（Qwen-7B）。UPM 预训练混合 WenetSpeech/GigaSpeech 子集、AISHELL-1、LibriSpeech、wTIMIT、AISHELL6-Whisper 与噪声；微调用上述数据子集。AISHELL6-Whisper 耳语 CER 1.31%（相对此前最佳 Seed-ASR 的 1.58% 降约 17%），正常语音 CER 0.63%。英文 wTIMIT 多口音正常/耳语条件均优于对比系统。AISHELL-1 CER 1.34%、LibriSpeech-clean WER 1.91%。自建 Noise Hallucination Set 上幻觉率 4.5%（强基线多在 25% 以上）。消融：仅注意力调制 3.45%、仅全局指令 1.84%、完整模型 1.31%（基线微调 3.98%）。

## 结论
通过自监督感知信号不确定性并用置信度融合解码，模型在耳语 ASR 上达到文中报告的 SOTA，同时显著降低噪声幻觉，且不明显牺牲通用 ASR 能力。

## 点评
核心不是“把耳语学得更像正常语音”，而是先量化声学证据可靠度再约束生成，直接打在耳语场景的准确率–幻觉权衡上。全局指令对 CER 与幻觉率贡献更大，帧级注意力起补充作用；依赖 F0/频谱自监督与三阶段训练是否在其他 Audio-LLM 上同样稳定，正文未充分展开。


# Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models

- 论文编号：1278
- 报告人：Bi-Cheng Yan
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yan26c_interspeech.pdf

## 问题
Speech-augmented Language Models（SLM）做 ASR 时仍易幻觉：生成与语音不对齐的额外内容。文中将幻觉词定义为对齐后的一类特殊插入错误。相对视觉–语言与纯文本场景，SLM 的幻觉机制与缓解仍不足。

## 方法
先用因果中介（对 MHA/MLP 做零消融）与注意力行为分析定位幻觉来源。再提出 AudioSLM：在 connector 上建 CTC 模块得到对齐 logits，经 CTC-Gated（深度卷积 + SwiGLU 门控） refinement 音频 token；在 Transformer 块的 MHA 与 MLP 之间插入 cross-attention（query 来自 MHA，key/value 为音频 token），训练时主要更新该层。骨干为 SmolLM2，音频编码器取自 Whisper-large-v2，connector 为 3 层 CNN（下采样 4），LLM 侧用 LoRA。

## 实验与结果
LibriSpeech train-clean-100，评估 clean/other。Dev-clean 上 Vanilla-SLM 的 HER 52.01%、INS 3.69%，AudioSLM 降至 HER 8.69%、INS 0.74%；去掉 CA 或 CTC-Gate 后 HER 升至 11.96%/14.67%。WER：AudioSLM（135M）test-clean/other 为 7.11/11.92，优于 Vanilla-SLM 与 CTC/RNN-T/CTC-Atten，并在 other 上优于 LLM-Guided Decoder（LLaMA-7B）；放大到 1.7B 后 test-clean/other 为 4.71/10.21，但 Dev-clean HER 随规模从 8.69 升到 10.64、12.76。分析显示幻觉词注意力几乎全偏文本 token。

## 结论
幻觉主要来自过度偏向文本先验的自注意力；CTC 对齐门控与跨模态交叉注意力可显著降低 HER，并保持有竞争力的 WER。作者计划后续研究无训练的解码抑制策略。

## 点评
把幻觉形式化为对齐后的插入并做组件级因果分析，使缓解方向有据可依。训练数据仅 clean-100、骨干偏小，规模越大 HER 反升，提示“更强语言先验”与幻觉风险同向；方法强在对齐与跨模态约束，对极嘈杂或开放域场景的外推仍待验证。


# Rank-Distance Based Confidence Estimation for ASR

- 论文编号：1355
- 报告人：Nagarathna Ravi
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ravi26_interspeech.pdf

## 问题
ASR 解码器最大类概率常过自信，无法反映正确性；二值目标的辅助置信度模型（CEM）把部分正确词也标成 0；基于强制对齐的连续目标易受时间戳误差影响；真类概率型连续目标在大词表下又塌缩成近似二值，校准变差。

## 方法
提出 RanD 连续目标：对预测–参考词做编辑对齐，再对 token 对齐；用参考 token 在后验中的归一化秩分数 \(s_{rank}\) 与后验相对 one-hot 的归一化欧氏距离 \(s_{dis}\) 加权（\(\alpha=0.5\)），词级取 token 平均。再按架构从 ASR 抽取词级嵌入训 CEM（shrinkage loss）：CTC 用编码器/解码器隐藏与后验平均；RNN-T/TDT 用预测网络状态与后验；AED 用注意力上下文、解码状态与嵌入。CEM 结构因架构而异（全连接 / BiLSTM / 小 FFN）。

## 实验与结果
在 NeMo 预训练模型上评估：Hindi Conformer-CTC（KB 训练 CEM，PB 作域外）、Conformer RNN-T、Parakeet-TDT、Canary-Flash AED（LibriSpeech 训 CEM，NPTEL/Svarah 域外）。对比 MCP、熵、二值 CEM（M/T/S-CEM 等）及 TeLeS、TruCLeS。RanD 在多数 MAE/KLD/JSD/NCE/ECE/AUROC/AUPRC 上优于或持平 SOTA；例如 CTC 在 KB 上 MAE 0.0570、AUROC 0.8669；RNN-T/TDT/AED 在 LibriSpeech 与域外集上也整体更优，并显示对错配域有更好泛化。

## 结论
用秩与分布距离构造连续置信目标，可避免二值粗糙、对齐不准与真类概率塌缩等问题，在四种 ASR 架构及域内/域外数据上优于文中对比的 SOTA CEM。未来拟覆盖删除错误与低资源场景。

## 点评
RanD 用排序位置代替易塌缩的真类概率，同时用分布距离刻画不确定度，对大词表过自信问题针对性强。方法依赖编辑对齐与架构特定特征抽取，实现成本随 ASR 类型变化；域外结果整体更好，但部分指标并非全面最优，实用时仍需按指标与任务权衡。


# Training-Free Intelligibility-Guided Observation Addition for Noisy ASR

- 论文编号：1096
- 报告人：Haoyang Li
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26s_interspeech.pdf

## 问题
噪声下 ASR 差，语音增强（SE）可抑噪但常引入损害识别的伪影。Observation Addition（OA）用权重融合噪声与增强语音、无需改 SE/ASR，但 \(S'\) 若只看噪声侧信号质量，或依赖需标注 WER/CER 训练的神经预测器，则复杂且难泛化。

## 方法
提出无训练的可懂度引导 OA：理想情形用噪声与增强的 WER 反比归一化定 \(S'\)；实际用后端 ASR 置信度近似，\(S'=\mathrm{conf}(y)/(\mathrm{conf}(y)+\mathrm{conf}(\hat{x}))\)，再按 \(\bar{x}=S'y+(1-S')\hat{x}\) 融合后解码。Whisper 用段级平均 log-prob 的 token 加权几何均值；Parakeet/Wav2Vec2-CTC 用 Tsallis 熵（\(q=0.33\)）导出 token 置信度再取几何均值。另比较硬切换（选置信更高者）与基于帧级置信的 OA。

## 实验与结果
SE：Demucs 与 GR-KAN MP-SENet（VoiceBank-DEMAND 训练）；ASR：Whisper-large、parakeet-tdt-0.6b-v2、wav2vec2-large-960h。评测 VoiceBank+DEMAND 与 CHiME-4（Simu/Real，SE 域外）。对比 SNR-OA、DNSMOS-OA、Classifier-OA（2/3 类）。WER-OA 整体最低；实用的 Conf-OA 在多数设置上优于既有 OA 基线（如 MP-SENet+CHiME-4 Real 上 Whisper/Parakeet/Wav2Vec2 为 5.86/5.55/24.03）。误校准子集上 Conf-OA 明显优于硬切换；帧级 OA 相对句级反而变差（如 Wav2Vec2+MP-SENet Real：24.03→25.30）。

## 结论
用后端 ASR 置信度做句级 OA 权重，可在不改动 SE/ASR、无需额外训练的前提下改善噪声 ASR，并优于多种已有 OA；句级融合优于硬切换与帧级融合。

## 点评
把“该信噪声还是增强”直接交给识别器自身置信度，避开了信号质量与 ASR 目标不一致、以及再训预测器的开销。当噪声与增强差距极大时，融合可能略逊于单用更强支路；帧级变差说明时间一致性对后端 ASR 很敏感，句级标量更稳妥。

