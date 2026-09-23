# Resource Constrained Speech Recognition
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 9）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场面向端侧/资源受限 ASR：超低比特量化、忆阻器模拟计算中的位置编码、Whisper PTQ 格式选型、亚 1-bit Conformer、一次性剪枝作正则，以及利用时间冗余的 KV 池化注意力。共同目标是在内存、能耗与延迟约束下保住转写质量。

量化线索强调“帧并非同等重要”与“激活位宽往往比权重量化格式更关键”：DiffAQ 按帧间变化加权 Hessian；系统 PTQ 研究覆盖 INT/FP 多种格式并给出 Pareto 指南。LittleASR 用变秩二值分解突破每参数至少 1 bit 的网格下界。剪枝工作则翻转叙事：敏感度感知一次性剪枝可无细调即改善泛化，并揭示编码器–解码器不对称。架构侧 KV-Pooling 压缩 Key/Value 以利用语音时间冗余，降低对网络深度的依赖。

硬件相关瓶颈包括 ADC 动态范围被位置编码大输出拖垮，以及 FP 乘法器相对 INT 的面积效率讨论。

## 技术内容

### 量化、模拟计算与亚比特压缩

**Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR**（论文 1569；presenter：Woori Jeon）
超低比特 PTQ 直接套 GPTQ/AWQ 会严重劣化 ASR。DiffAQ 用帧间激活差衡量声学变化率并按比例分配 Hessian 重要性，把精度集中在音素关键帧。作为对 GPTQ 的免训练修改，摘要称跨 Whisper 体量与基准降低 WER，2-bit 时收益最大。

**Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition**（论文 683；presenter：Benedikt Hilmes）
忆阻器模拟计算中，变换后位置编码的大输出值严重劣化 ADC。通过调整特定层 ADC 的权重量与精度比特比例，摘要称执行劣化相对下降约一半且估计能耗稳定；若 ADC 不可改，去掉编码相关线性变换也可相对减劣化约三成。

**Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR**（论文 698；presenter：Woosuk Choi）
系统评估 Whisper tiny.en/base.en 八十余种 PTQ 配置。主要发现：激活位宽远比权重格式重要；多类 4-bit 中 NVFP4 W4A16 接近全精度，MXFP4 在标准 PTQ 下失败。摘要给出内存预算 Pareto 与六条实用选型指南。

**Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition**（论文 2063；presenter：Jinsu Yeo）
整数量化受离散网格约束、每参数下限 1 bit。LittleASR 基于变秩二值分解与梯度感知敏感度，把非关键层压到亚 1-bit，在极端压缩与识别准确率间权衡。

### 剪枝正则与高效注意力

**Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR**（论文 3411；presenter：Julian Irigoyen）
对 Whisper-small 编码器–解码器，一次性幅值剪枝可作隐式正则、无需细调。敏感度诊断显示解码器 FFN 脆弱，解码器自注意力与靠后编码器层有可去冗余。摘要报告特定 50% 剪枝设置下的 WER 改善及跨语料保持，并在高稀疏度下相对全局幅值剪枝保住近基线精度。

**Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR**（论文 2124；presenter：Yi Wu）
KV-Pooling 对 Key/Value 平均池化压缩，保留 Query 分辨率；并按层抽象预设差分池化步长集成到 Zipformer。相对原生 Zipformer，摘要报告 AISHELL-1 CER 与 LibriSpeech WER 绝对下降，以及指定 CPU 上 RTF 改善。

## 本场要点
- 超低比特 ASR 量化需突出音素过渡帧，避免稳态帧主导校准。
- 端侧 Whisper 选型中激活位宽往往主导精度。
- 亚 1-bit 与敏感度剪枝分别突破量化下界与“剪枝必细调”习惯。
- 忆阻器路径上位置编码与 ADC 动态范围是关键硬件–算法接口。
- 利用语音时间冗余压缩 KV，可同时改善精度与 RTF。
- 编码器/解码器不同子层对压缩的脆弱性不对称。

## 覆盖核对
`1569 | Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR`
`683 | Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition`
`698 | Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR`
`2063 | Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition`
`3411 | Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR`
`2124 | Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR`
