# Robust and Efficient ASR

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场 Long Oral 同时追求 ASR 精度与效率/可控性。解码端 MDM-ASR 用 Masked Diffusion 非自回归框架，配合 Iterative Self-Correction Training 与位置偏置熵界置信采样，缩小 NAR 与 AR 差距并保留并行解码。幻觉治理上，从 Whisper 编码器激活与 Sparse AutoEncoder 潜空间做线性可分检测，并以激活/SAE 转向把非语音幻觉率大幅压低。

数据与标注政策成为另一轴：嵌入多视角（说话人、音素、语义）从十万小时野外数据中为领域专家模型精选约 5% 子集即可相对全量降低 WER；把 verbatim vs intended 转写风格视为可控潜变量，用 decoder task token 与平行文本激活，并改进不流畅语音的词级时间戳。流式 ITN 则把预训练 text-to-text 模型配上 Read-Tag-Write 策略做成端到端流式规范化。测试时适应方面，严格推导自回归熵最小化目标，统一先前启发式。瓶颈包括 NAR 质量缺口、幻觉、异构标注噪声、域数据过载与流式格式化。

## 论文技术总结

# MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding

- 论文编号：488
- 报告人：Sabato Marco Siniscalchi
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yen26_interspeech.pdf

## 问题
Seq2seq Transformer ASR 中 AR 精度高但逐 token 慢；NAR（含近期扩散/流匹配 ASR）可并行但相对强 AR 仍有明显差距。训练只见 oracle mask、推理却对自生成错误去噪，加剧训练–推理失配。

## 方法
MDM-ASR：预训练语音编码器 + Transformer **离散掩码扩散（MDM）解码器**；非因果自注意力，每步并行预测掩码位置，交叉注意条件于声学。
- **ISCT（Iterative Self-Correction Training）**：先对真值 mask 重建，再对模型自输出再 mask 并二次监督，暴露中间错误；
- **Position-Biased Entropy-Bounded Confidence sampler**：结合熵界与位置偏置的推理采样，权衡步数与质量。
架构其余与常规 encoder–decoder 一致，仅解码策略改为扩散迭代。

## 实验与结果
摘要称在多基准上相对既有 NAR 持续提升，并与强 AR 基线可比，同时保留并行解码效率；文中还计划消融缩放、ISCT 与采样器。
（PDF 抽取在采样器小节截断，具体 WER 表未进入可读全文。）

## 结论
用音频条件 MDM 替换左到右 AR，配合 ISCT 与置信采样，可在保持 NAR 吞吐的同时显著缩小与 AR 的精度鸿沟。

## 点评
把文本 MDM 的双向精炼迁到 ASR，并用自纠训练对症“自生成噪声”，路线清晰。强在与既有流匹配中间分布手搓不同、更数据驱动；**实验数字因抽取截断不可用**，加速比与绝对 WER 需回 PDF。


# Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders

- 论文编号：1989
- 报告人：Georgii Aparin
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aparin26_interspeech.pdf

## 问题
Whisper 常对非语音输入生成流畅但与声学无关的转写（幻觉）。既有缓解依赖前/后处理或微调特定神经元；是否可仅靠编码器内部表示检测并在推理时纠正，且少伤正常语音 WER，仍待验证。

## 方法
提取 Whisper 音频编码器激活，在两空间分析幻觉可分性：原始激活与 **AudioSAE** 稀疏潜变量（扩展×8，Top-k=50）。线性分类器显示判别力集中于稀疏特征子集、并随层加深增强。提出免微调干预：
1. **激活空间 steering**：沿分类方向加减扰动；
2. **SAE latent steering**：对 top-k 幻觉相关潜维做加性/乘性缩放，再经 SAE 解码注入残差流。
在 Whisper small / large-v3 上评测；非语音训测严格划分（MUSAN、WHAM!、FSD50k、UrbanSound8K 等）；语音侧用 LibriSpeech、FLEURS、AISHELL-1 监控 WER/CER。

## 实验与结果
- SAE steering 将完整非语音测试集幻觉率：small **72.63%→14.11%**；large-v3 **86.88%→27.33%**；
- 语音数据上 WER 仅小幅退化，接近微调类方法效果。
（抽取在数据集与 HR 表处截断，分数据集明细与 WER 表未全读到。）

## 结论
幻觉在编码器表示中线性可分；SAE 空间 steering 可不改模型参数大幅降非语音幻觉，并在多语言语音上保持可用识别质量。

## 点评
把可解释性工具（SAE + steering）接到 ASR 幻觉，避免重训整模，工程友好。强在双规模模型与非语音–语音分离评测；脆弱在依赖幻觉标签定义与 steering 强度 \(\alpha\)——过强可能伤真实语音。


# Which Data Matter? Embedding-Based Data Selection for Speech Recognition

- 论文编号：3073
- 报告人：Zakaria Aldeneh
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aldeneh26_interspeech.pdf

## 问题
大规模伪标注野外数据利于通才 ASR，但专科模型容量有限、无法消化全部异构数据。如何从约 **100k 小时** 源数据中选出贴合目标域的子集，仍缺系统答案。

## 方法
用互补嵌入刻画样本：说话人（MFA-Conformer）、语音/音素（WavLM Base+ 均值池化）、语义（SBERT）；再做 **batched greedy MMR**（相关–多样权衡 \(\lambda\)，相关预过滤、目标端 k-means 压缩）。在 Granary 英源上按目标域（LibriSpeech / CommonVoice / TED-LIUM）验证集选子集；训 CTC Conformer-Small（9M）与 Large（107M）。

## 实验与结果
- 全量 Granary 跨域优于仅在域内训练的专科数据（如 Conformer-Large：LS-clean 6.7 vs 仅 LS 的 3.2 但 CV/TED 更差；全量 Granary CV 25.4、TED 6.5）。
- 随机 5% 已接近全量；摘要称策略性选中的 **5% 子集相对全量最高约 36.8% 相对 WER 下降**。
（抽取在 Table 2 中途截断，MMR 主表数字不完全。）

## 结论
对专科 ASR，嵌入空间上兼顾相关与多样的数据选择可显著优于盲目用全量或随机子集；说话人/音素/语义轴需按目标域权衡。

## 点评
把信息检索里的 MMR 接到 ASR 数据策展，问题贴近工业“海量伪标→专科模型”。强在三轴嵌入与可扩展批选；**MMR 相对全量的完整对照表因截断不全**，36.8% 相对降幅以摘要为准。


# Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing

- 论文编号：2792
- 报告人：Laurin Wagner
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wagner26_interspeech.pdf

## 问题
现代 ASR 训练数据混杂 verbatim（含填充停顿、重复等）与 intended（流利化）标注，把转写风格当成未控隐变量，导致解码不稳、评测混淆（风格错配可占报告 WER 的约 60%）、词级时间戳不可靠。模型其实已编码两种风格，缺的是可控激活。

## 方法
1. **Coverage-aware decoder task tokens**：在并行 verbatim/intended 对上训练，用任务 token 显式切换策略；
2. **Supervised cross-attention finetuning**：选与 TIMIT 对齐相关最好的 \(k=10\) 头，对平均注意力与词区间二值目标做余弦距离；推理时能量 pause 模型 + 温度锐化 + Viterbi 得词时间戳；
3. 新任务 **verbatimize**：从 intended/异构文本生成规范 verbatim，用于语料富集。

## 实验与结果
- 仅英语训练即可零样本把德语不流畅 F1 **10%→79%**；
- 全量英-only 微调在 verbatim 精度、不流畅检测与 intended 质量上英德均超基线；
- 监督交叉注意使不流畅语音上的词时间戳优于强制对齐基线。
（抽取在方法中后部截断，完整数值表未全见。）

## 结论
把转写策略显式化为可控变量，可稳定激活 verbatim/intended，并改善词级 timing；verbatimize 支持可扩展语料建设。

## 点评
问题诊断（风格作隐变量）对临床/自发语音 ASR 很关键；任务 token + 对齐头监督是轻量可控方案。强在跨语零样本不流畅检测；脆弱在依赖并行风格对与 TIMIT 头选择，泛化到更多语言/病理语音仍待验证。


# Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy

- 论文编号：1060
- 报告人：Kiet Anh Hoang
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hoang26_interspeech.pdf

## 问题
流式 ASR 需要把口语形式即时转为书面 ITN（标点、大小写、半符号实体等）。现有流式 ITN 多为神经标注 + 手工 FST，跨域跨语难扩展；端到端 seq2seq 精度好但全局注意力不可流式。

## 方法
基于预训练文本-to-文本模型做流式端到端 ITN：
- **流式编码器**（如块注意力）+ 自回归解码器；
- **Read–Tag–Write（RTW）**：编码器边读边对 token 做 IOB 标注；标签为 O（原样）则立即写出以降延迟；遇到需归一化跨度完成后再调解码器 WRITE；
- **Prefix-based Training Augmentation**：随机截断源、目标侧加局部 `<EOS>`，让解码器在无全局 EOS 时也能结束局部跨度；
- KV cache 与推理优化；数据来自越南语新闻语料自动生成约 5M 句对（标点/大小写/半符号/语音学 OOV 等）。

## 实验与结果
摘要：越南语数据上精度可比非流式端到端基线，优于流式混合方法，并满足实时延迟要求。
（抽取主要在方法与数据构造，完整延迟/准确率表未进入可读尾部。）

## 结论
RTW 利用 ITN 多为局部、大量 token 无需改写的结构，使预训练 T2T 模型可流式化，摆脱 FST 规则依赖。

## 点评
把 SiMT 的 read/write 思想改成 ITN 友好的 Read–Tag–Write，抓住“多数 token 直通”降低延迟。强在与预训练 LM 知识结合；**定量延迟与类别 F1 因抽取不全**需回 PDF；手工 regex 造数对真实 ASR 噪声的鲁棒性仍是潜在风险。


# Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models

- 论文编号：944
- 报告人：Chee-En Yu
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26c_interspeech.pdf

## 问题
分类任务上熵最小化（EM）是成熟的测试时适应（TTA）手段，但用于自回归生成时，既有做法分裂为伪标签 teacher-forcing 与策略梯度 RL 启发式，缺统一、数学正确的 EM 梯度。

## 方法
推导自回归模型上精确 EM 目标，自然分解为：
- **token 级策略梯度项**；
- **token 级熵项**。
据此将先前方法解释为该统一目标的部分实现。在 Whisper ASR 上实施 episodic TTA（单样本适应后复位），比较 Greedy-EM、序列级与 token 级变体及 beam 扩展（如 EM-tok-b）。

## 实验与结果
- 加性噪声：源模型平均 WER 22.53%；Greedy-EM 21.91%；EM-seq 21.34%；EM-tok 20.77%；**EM-tok-b 平均 19.15%**，在十种噪声上最低。
- 口音迁移等亦有表（摘要称覆盖噪声、口音、多语等 **>20 域** 持续改进；自称首次对 Whisper 做 TTA）。

## 结论
正确 EM 为自回归 TTA 提供统一理论；完整 token 级目标（可加 beam）优于不完整启发式，提升 Whisper 在分布偏移下的稳健性。

## 点评
贡献首先是理论澄清：把“伪标签熵”与“RL 熵奖励”收束到同一分解。强在 Whisper 多域实证；脆弱在 episodic 单样本适应的算力与稳定性，以及伪标签质量差时策略梯度方差——噪声表显示完整目标更有效，但极端失配时仍可能放大错误。

