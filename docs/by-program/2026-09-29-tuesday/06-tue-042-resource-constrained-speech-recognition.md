# Resource Constrained Speech Recognition

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
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

本场面向端侧/资源受限 ASR：超低比特量化、忆阻器模拟计算中的位置编码、Whisper PTQ 格式选型、亚 1-bit Conformer、一次性剪枝作正则，以及利用时间冗余的 KV 池化注意力。共同目标是在内存、能耗与延迟约束下保住转写质量。

量化线索强调“帧并非同等重要”与“激活位宽往往比权重量化格式更关键”：DiffAQ 按帧间变化加权 Hessian；系统 PTQ 研究覆盖 INT/FP 多种格式并给出 Pareto 指南。LittleASR 用变秩二值分解突破每参数至少 1 bit 的网格下界。剪枝工作则翻转叙事：敏感度感知一次性剪枝可无细调即改善泛化，并揭示编码器–解码器不对称。架构侧 KV-Pooling 压缩 Key/Value 以利用语音时间冗余，降低对网络深度的依赖。

硬件相关瓶颈包括 ADC 动态范围被位置编码大输出拖垮，以及 FP 乘法器相对 INT 的面积效率讨论。

## 论文技术总结

# Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR

- 论文编号：1569
- 报告人：Woori Jeon
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeon26c_interspeech.pdf

## 问题
将 GPTQ/AWQ 等 PTQ 直接用于 Whisper 在 2–3 bit 时严重退化甚至幻觉循环。语音激活在稳态与零填充区高度相关，在音素边界变化剧烈；帧均等进 Hessian 会使静态/填充主导校准，掩盖关键过渡。

## 方法
DiffAQ：用帧间激活差 ∆xt=xt−xt−1 的 L2 范数作时间密度，归一化后得权重 wt=α+(1−α)d̄t（α=0.2），缩放 Hessian 累加。仅改编码器线性层；解码器仍用标准 GPTQ。训练无关，校准 128 条 LibriSpeech train-other，评 Whisper base/small/medium、LibriSpeech 与 FLEURS。

## 实验与结果
3-bit 全配置最低或近最低 WER；2-bit 增益最大：Medium test-other 17.53%→12.93%，FLEURS 18.05%→12.07%；Small FLEURS 3-bit 11.37%→8.69%。RTN/AWQ 常 WER>100%。Base 在 2-bit 仍崩坏，属容量瓶颈。α 不敏感。

## 结论
按声学变化率加权 Hessian 可改善超低比特 ASR 的 PTQ；2-bit Medium 权重大约从 1.5 GB 压到 <200 MB。局限：噪声瞬态也可能获高权重；未验证其他编码器架构。

## 点评
抓住语音相对文本的“时间冗余/填充陷阱”，把 PTQ 校准偏到音素过渡，改动小、解释清楚。强在无需重训；弱在 Base 2-bit 仍不可救，且差分对非语音瞬态不具选择性。


# Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition

- 论文编号：683
- 报告人：Benedikt Hilmes
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hilmes26_interspeech.pdf

## 问题
忆阻器可模拟执行 VMM 以降耗，但编程与执行噪声大；相对位置编码（PE）对 ASR 尤其低精度很重要，却发现其线性变换输出幅值易被默认 ADC 裁剪，导致映射到忆阻器后相对无 PE 反而更差。

## 方法
在 SynaptogenML 上仿真 CTC-Conformer（~77M）带相对 PE；LibriSpeech 与 Loquacious 250h；权重 8/4-bit、激活 8-bit；ADC 默认 4 精度+4 量程位。分析 PE 线性层 ADC 裁剪（约 40% 时间），试验：扩大量程/精度、固定 8 bit 预算下移位给量程、仅调 PE 层 ADC、去掉 PE 线性层、学习型 PE、数字域保留 PE（oracle）。

## 实验与结果
数字基线：相对 PE 在 4-bit 权重更稳（dev-other 5.6 vs 无 PE 6.5）。默认忆阻器映射后有 PE 反而更差。将 PE ADC 量程提到 8 或固定预算 1/7（精度/量程）可把相对退化约减半，恢复约 15% 相对优于无 PE。去掉编码相关线性变换时相对退化约降 30%。oracle（PE 留数字）接近最优。

## 结论
PE 层输出动态范围与默认 ADC 不匹配是主要病灶；调 ADC 量程或去掉线性变换可恢复 PE 收益。部署需在硬件可改 ADC 与模型改造间权衡。

## 点评
把硬件量化裁剪与相对 PE 的幅值特性对上号，比笼统报“忆阻器掉点”更有指导性。强在软硬协同建议；弱在纯仿真、且评测子集较小（dev-other/dev）。


# Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR

- 论文编号：698
- 报告人：Woosuk Choi
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26_interspeech.pdf

## 问题
端侧部署 Whisper 时，INT/FP 量化格式与激活精度如何影响编码器–解码器 ASR 仍缺系统证据；LLM 上流行的 W4A16 与 NVFP4/MXFP4 是否迁移到 Whisper 不清楚。

## 方法
对 tiny.en/base.en 做 80+ 组 FakeQuant PTQ：INT8/4/3 与 FP8/FP4/NVFP4/MXFP4，扫激活精度、组大小与 SmoothQuant；LibriSpeech test-clean/other；比较面积文献中 FP vs INT 乘法器。给出 Pareto 与六条部署指南。

## 实验与结果
激活位宽主导：16→8 bit 约 +1–3% 绝对 WER；INT16 与 FP16 激活几乎无差别。NVFP4 W4A16 在 base.en 达 4.88%（距 FP32 0.07%、约 6.4× 压缩）；MXFP4 标准 PTQ 严重崩（tiny 可达 38–94%）。INT3 近不可用。Pareto：>约 36 MB 时量化 base 优于 tiny。

## 结论
保 16-bit 激活比抠权重更重要；NVFP4 是近无损 4-bit 首选；FP 激活路径因乘法器面积更小更适合 NPU。指南覆盖 20–80 MB 预算。

## 点评
工程向系统扫参，结论可直接指导格式选型。强在激活位宽与 NVFP4 vs MXFP4 的机制解释（E8M0 尺度过粗）；弱在仅 tiny/base、FakeQuant 非真机延迟，且未与 GPTQ/AWQ 权重敏感方法交叉。


# Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition

- 论文编号：2063
- 报告人：Jinsu Yeo
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yeo26_interspeech.pdf

## 问题
Conformer-Transducer 端侧内存受限；整数量化有 1 bit/参数硬下界。解码器对误差敏感需高精，编码器冗余多，若解码器不能再压，只能把编码器压到亚 1-bit，但标准量化做不到。

## 方法
LittleASR：用 LittleBit 式变秩二值分解 ˜W=diag(h)Ub diag(ℓ) Vb⊤ diag(g)，以秩 r 准连续控制有效 bpw。梯度敏感度 Ω(l) 引导可微预算搜索，编码器压到亚 1-bit、解码器/联合网保留更高秩，再 QAT。目标含点卷积、LSTM 投影与线性层；Conv2d 用 INT4 RTN。NeMo Conformer-Transducer Large（120M），LibriSpeech。

## 实验与结果
混合秩 1.0 bpw：dev-other WER 6.01%（AbsMean tensor 6.30%，尺寸约 18.8 MB）。可到 0.2 bpw（7.1 MB），整数基线无法进入。同尺寸下混合秩优于均匀秩（如 0.4 bpw：8.78 vs 10.82）。分配显示浅层编码器约 0.3–0.4 bpw、深层与 Value 投影更高、联合网约 2.0 bpw。

## 结论
变秩二值分解打破 1-bit 地板，敏感度分配在极端压缩下拓宽 Pareto 前沿，适合超紧内存 ASR。

## 点评
把“编码器可狠压、解码器要护”落到连续秩预算，而非死守离散比特档，问题意识准。强在亚 1-bit 可达与层内（如 Wv vs Wq）细粒度；弱在依赖 QAT、二值 GEMM 真机收益未测，且极端 0.2 bpw WER 仍明显抬升。


# Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR

- 论文编号：3411
- 报告人：Julian Irigoyen
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/irigoyen26_interspeech.pdf

## 问题
剪枝常被当作训后压缩；编码器–解码器 ASR Transformer 是否存在过参数冗余，使无微调的一次性幅度剪枝反而改善泛化，尚缺系统敏感度诊断。

## 方法
对 Whisper-small（244M）做训后梯度与对角 Fisher 敏感度诊断；按模块/层（早中晚）做无结构幅度剪枝，无微调。主评 LibriSpeech test-other（基线 WER 11.64%），掩码原样迁到 Common Voice、TED-LIUM。敏感度引导组件级稀疏度分配。

## 实验与结果
解码器整体更脆弱；全局剪枝 30–40% 崩溃。解码器自注意力 50% 剪枝：test-other 绝对降 2.38%；编码器末四层 50%：降 1.72%。解码器早层/FFN 极脆。40.8% 稀疏度下敏感度感知压缩近保基线，全局幅度剪枝则塌。跨语料增益可迁移。

## 结论
一次性幅度剪枝可作隐式正则；解码器自注意力与深层编码器冗余可剪，解码器早期与 FFN 需保护。方法模型无关但需按架构重验敏感度剖面。

## 点评
把“剪枝=压缩”翻成“剪枝=正则”，并用一/二阶诊断对齐实证，视角新鲜。强在无微调即增益与跨库迁移；弱在非结构化稀疏未加速实际推理，且相对某流水线基线报告，不宜与官方 Whisper 数字硬比。


# Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR

- 论文编号：2124
- 报告人：Yi Wu
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26k_interspeech.pdf

## 问题
自注意力 O(T²) 限制长序列 ASR；粗时间下采样伤边界精度。语音帧高度冗余，K/V 作上下文不必与 Q 同分辨率，固定步长池化又忽略层间冗余差异与相对位置错位。

## 方法
KV-Pooling Attention：对 K/V 平均池化（步长 s），Q 保持原分辨率，复杂度 O(T²/s)；中心对齐相对位置编码；因果掩码按池化窗右边界、padding 需窗内全有效。分析 Zipformer 层间帧相似与熵，浅层大步长、深层小步长，集成 KV-Pooling-Zipformer（步长配置如 4,2,1,2）。Pruned RNN-T，AISHELL-1 与 LibriSpeech。

## 实验与结果
AISHELL-1：L/M/S 测集 CER 分别 6.58→6.35、6.57→6.35、8.10→7.87；摘要称绝对约 -0.2% CER。LibriSpeech：L 上 clean/other 3.33/8.32→3.30/8.09；摘要称约 -0.3% WER。EPYC 7763 上推理 RTF 约改善 10%。注意力图更集中于对角。

## 结论
非对称分辨率注意可利用时间冗余加速并略提准确率；层差分步长与位置/掩码适配是落地关键。

## 点评
把“语音帧冗余”直接写进 K/V 池化，比整体下采样更保边界。层自适应步长有分析依据；增益幅度不大，小模型在 clean 上偶有回退，平滑可能抹掉细微音素细节。

