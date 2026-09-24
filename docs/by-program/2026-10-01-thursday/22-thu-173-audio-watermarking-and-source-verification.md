# Audio Watermarking and Source Verification

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕生成式语音时代的可追溯性：对抗神经编解码失真的水印恢复、在信息层（音节时长）而非波形层嵌入、利用流匹配初始噪声空间相关的免训练水印、大规模扰动基准、抗纯化主动防御，以及开集溯源中成对验证目标的隐藏代价。主线是信号级水印在编解码/声码器/纯化攻击下脆弱，需编解码感知恢复、生成过程内嵌或语义耦合。

方法谱从提取前自适应谱恢复，到合成时控时长、噪声—输出余弦相关，再到音素感知 Mamba 主动嵌入。评测侧 VoxWatermark 统一多注入法与多盒扰动；溯源侧则警示成对度量学习可能压缩嵌入方向分辨率，全局锚定在同等预算下更优。

## 论文技术总结

# Countering Neural Audio Codec Distortions in Watermarking with Adaptive Restoration

- 论文编号：953
- 报告人：Sungho Park
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/park26d_interspeech.pdf

## 问题
神经音频编解码器（EnCodec、DAC 等）带来结构化、非线性失真，常把水印提取准确率打到近随机；各编解码器失真模式不同，单一恢复网络难以泛化。现有深度水印对经典失真较稳，但对神经编解码仍脆弱。

## 方法
在不动 Timbre 水印嵌入/解码器的前提下，于编解码输出与提取器之间插入频谱恢复：STFT 幅度谱 → 轻量编解码器分类器 → 按类选择专用 ConvNeXt U-Net 恢复 → 送入原提取器。用 L1 重建损失对齐编解码前水印谱。VQ 失真具空间相关，故用 7×7 depthwise ConvNeXt 扩大感受野。按编解码器各训专家模型，推理时动态路由。

## 实验与结果
LJSpeech 8:1:1，评估 11 种神经编解码器。编解码器分类器测试准确率 100%。RVQ 多码本场景恢复后 bitwise accuracy 常超 98%（如 EnCodec 24 kbps：72.91%→98.75%；DAC 8 kbps：86.56%→99.58%）；单码本极低码率（WavTokenizer、StableCodec 等）提升有限、近随机。自适应优于单一共享模型。消融：无恢复 59.01%，无自适应 60.54%，Basic CNN+自适应 70.44%，完整方案 84.05%（EnCodec 6 kbps）。

## 结论
作者认为后处理恢复可显著提升对 RVQ 神经编解码的水印稳健性，且易于扩展新编解码器；单码本信息瓶颈下后验恢复能力有限，未来水印设计宜考虑量化机制本身。

## 点评
把问题定为“编解码感知的谱恢复”而非重训水印，工程上易插拔。自适应专家路由对异构失真很关键。边界清晰：单码本/极低码率几乎不可恢复；训练依赖已知编解码器配对，开放未知编解码仍待验证。


# DuraMark: Duration-Embedded Watermarking in LLM-based TTS

- 论文编号：2298
- 报告人：Zhenwei Mou
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/mou26_interspeech.pdf

## 问题
LLM-TTS 高逼真克隆带来 deepfake 风险。主流信号级水印易被神经编解码/声码器等生成式重合成抹掉；既有信息级方法（如改 pitch）又易导致韵律不自然。

## 方法
DuraMark 在信息级嵌入：基于 CosyVoice 式 LLM + flow matching 的时长可控 TTS，按音节预测时长与语音 token，并用时长提取器（文本–Mel Transformer 帧级归属）与 guide loss 强制解码器遵循指定时长。嵌入时将各音节时长奇偶编辑到目标比特（0/1）；检测时提取时长序列，映射到 [-1,1] 后与水印相关，超阈值 τ 判有水印。支持知情检测（真值文本）与盲检（ASR 转写）。

## 实验与结果
WenetSpeech 训练、AISHELL-3 评测。33–64 音节时 Info/Blind TPR@1%FPR 约 0.998/0.987。对 EnCodec/DAC/SpeechTokenizer/FACodec、多类声码器、增强、压缩与常规信号处理，DuraMark 平均 TPR 约 0.993（Info）/0.978（Blind），显著高于 AudioSeal、Timbre、WavMark（后者在多数生成攻击下崩溃）。CER/MOS 与未加水印接近。消融去掉 duration 输入或 L_guide 后 TPR 大幅下降。

## 结论
作者认为通过合成阶段编辑音节时长可实现抗生成式攻击的稳健水印，同时保持自然度；显式时长控制与引导损失是关键。

## 点评
把水印从波形细节挪到韵律时长，正好避开信号级“被重合成抹平”的弱点。依赖文本/音节对齐与中文一字一音节设定；盲检依赖 ASR，跨语种与强时间拉伸攻击下的表现正文未充分展开。


# AudioNoisePrints: Model-free audio watermarking using spatial correlation in flow matching TTS

- 论文编号：2165
- 报告人：Timothy Tin-Long Tse
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/tse26_interspeech.pdf

## 问题
Flow matching / diffusion TTS 水印若用后处理会改音质并有额外开销，且易被同款开源水印覆盖；若重训模型则成本高、可能伤质量。需要不重训、不改生成质量的水印方案。

## 方法
AudioNoisePrints 利用初始高斯噪声与生成 Mel/音频之间的空间相关：生成时使用由哈希确定的特殊初始噪声；检测用余弦相似度（或点积）相对随机噪声的经验 p-value 判定（model-free）。另训轻量 4 层 Conv2D ResNet 检测器，对指定噪声周期平铺到 Mel 帧长，并以压缩等增强提高稳健性。在 F5-TTS、MatchaTTS 及 DiffWave 声码器上验证相关性质。

## 实验与结果
相对 AudioSeal：强增强下（噪声、滤波、裁剪、变速等）整体更稳，尤其速度拉伸时 AudioSeal 几乎失败而本方法仍可用；MP3 影响很小；Echo 上本方法较弱。余弦相似度优于 L1/L2。多模型上 originated noise 与输出的相似度显著高于随机噪声（p≈0）。检测器在 AAC 等压缩上可达约 0.99 准确率。

## 结论
作者认为对 FM/diffusion TTS（及声码器）可在零生成开销、不伤音质下做可检测水印，且空间相关具一定普适性；可选外部检测器提升复杂攻击下的稳健性。

## 点评
把图像域 NoisePrints 迁到音频，抓住“噪声指纹”而非改波形，产品友好。需持有/复现初始噪声假设，适合“我自己的合成管线可追溯”；对未知模型来源或彻底重采样后的伪造场景覆盖有限，Echo 等未训增强仍是短板。


# VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations

- 论文编号：1771
- 报告人：Farnaz Sedaghati
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/sedaghati26_interspeech.pdf

## 问题
TTS 大规模部署后亟需可验证溯源，但缺少统一、面向检测器的大规模基准：现有基准覆盖水印方法少、扰动有限，且缺乏在未知嵌入方法与真实分布偏移下的通用检测基线。

## 方法
构建 VoxWatermark：在多语多源语料上统一注入 10 种水印（6 传统：LSB、QIM、Patchwork、Echo、Phase Coding、DSSS；4 神经：AudioSeal、WavMark、Timbre、Perth），约 91,090K 样本 / 126,513.89 小时。扰动分 no-box（17 类信号处理/编解码等）、black-box（HSJA、Square）、white-box（可微伪造/去除）。提出 AudioWMD：基检测器对 log-mel 打分，再对 K=8 随机查询分数聚合为 5 维稳定性特征（均值、标准差、极差、正类占比、翻转率），经逻辑回归做最终判决；对比单查询 WMD（ConvNeXt-V2）。

## 实验与结果
训练见 6 种水印、无扰动增强；OOD 含跨语（非英中 Common Voice）与跨口音（VCTK），并含未见水印（Patchwork、Echo、WavMark）。验证集上 AudioWMD AUROC 88.3% 高于 WMD 72.0%；OOD Test1/2 为 63.8%/63.2% vs 57.1%/57.9%。no-box 下两者多接近随机；white-box 上 AudioWMD 明显更稳（如 T1 AUROC 77.15 vs 48.63）；black-box 表现依赖攻击类型，HSJA-spec 上 AudioWMD 大幅掉点而 WMD 更强。

## 结论
作者认为注入方法多样性与分布偏移显著影响检测稳定性；AudioWMD 在多场景下更稳/可扩展，开源数据与代码以推动标准化评测。

## 点评
贡献重心在检测向大规模基准与三档威胁模型，暴露“干净域高分、真实扰动崩塌”的常见假象。AudioWMD 的查询稳定性建模对 white-box 有帮助，但对强自适应 black-box 并不万能——正好说明基准设计的价值。数据规模宏大，但检测器训练仅见部分水印、无扰动增强，OOD 数字仍偏低，实用部署需继续加强。


# Phoneme-Aware Mamba Watermark: An Active Defense System Against Purified Speech Deepfakes

- 论文编号：2105
- 报告人：Yanda Shao
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/shao26_interspeech.pdf

## 问题
零样本语音克隆（如 YourTTS、sv2TTS）使深度伪造语音高度逼真，被动 Audio Deepfake Detection 对未见合成模型泛化不足。扰动式主动防御（AntiFake、VoiceGuard）又易被 PhonePuRe 等扩散净化抹除。需要一种能嵌入可检索身份信息、并在净化与克隆后仍可追踪的“阴影式”水印防御。

## 方法
提出基于 Mamba 的音素感知主动水印框架。输入语音经冻结 XLS-R 300M 提取语音表征，并与 STFT 复谱并行；水印编码器在说话人身份码条件下生成谱扰动，注入 100–1000 Hz 频带后经 iSTFT 重建。Montreal Forced Aligner 得到音素边界，构造稳定区 mask，将扰动集中在音素稳态区。编码器对比 Bi-LSTM、Dual-column Bidirectional Mamba 与 Multi-Head Mamba（含音素门控）；解码器为独立 8 层 CNN，从 log-magnitude STFT 恢复水印。训练含抗净化对抗：周期引入 PhonePuRe（RevDiffWave + Refiner），联合水印检索、扰动幅度、重建、干净语音假阳性与净化后可检索损失。水印用 Hamming(6,3) 将 16 bit 扩为 36 bit，按 1 s 块重复嵌入，检测时多数表决。

## 实验与结果
在 LibriSpeech train-clean-100 训练，VCTK 11 说话人做真实威胁仿真。对抗微调后 MH-Mamba 净化前/后 bit 准确率 91.56% / 84.55%，Retain Rate 92.34%，优于 LSTM 与 BiMamba。对 YourTTS/sv2TTS 克隆语音源追踪 TPR 近 100%，延迟约 1.0–1.2 s。PESQ>3.5、SNR>34 dB。消融显示音素引导显著提升 PhonePuRe 后保留率。

## 结论
将水印与音素稳态耦合，并以对抗训练对抗 PhonePuRe，可在 TTS 克隆链路中保持可追踪、低延迟、较透明的主动防御。作者认为这为应对新兴语音深度伪造提供了实用机制。

## 点评
做法抓住的是“净化—克隆后仍可检索”而非单纯干扰合成：用音素稳态承载水印，直接针对 PhonePuRe 的音素条件去噪路径。Mamba 长程建模与对抗净化训练配套合理，但依赖 MFA 对齐与固定频带注入，对噪声、语种或非对齐语音的稳健性正文未充分展开；UFL 理论上界约 2 s，短时伪造仍可能漏检。


# The Hidden Cost of Pairwise Verification in Synthetic Speech Source Tracing

- 论文编号：120
- 报告人：Anton Firc
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/firc26_interspeech.pdf

## 问题
开集合成语音源追踪常被当作验证问题，因而借鉴生物识别中的成对度量学习。但合成器间差异细微，局部 pairwise 目标是否优于全局锚定、以及性能差距是否只由嵌入维度造成，尚不清楚。

## 方法
在匹配骨干、数据与 epoch 预算下，对比全局锚定（闭集 Softmax CE，推理用 penultimate 嵌入余弦相似度）与多种 pairwise 验证目标（随机、难负挖掘、方向性覆盖、rival mining；可选 XLS-R 微调）。骨干默认冻结 XLS-R 300M，池化用 MHFA（与 AASIST 对比后选定），pairwise 头为 FFCosine。域内用 MLAAD、域外用 STOPA，claim-based 评估（R=1，MLAAD 另报 R=5）。用 k99（解释 99% 方差所需主成分数）分析嵌入衰减，并对全局基线施加 10/13 维瓶颈消融。

## 实验与结果
全局 CE 在 MLAAD 上 EER 8.61%，优于 pairwise（约 12–15%）；rival + XLS-R 微调最好 pairwise 仍为 12.39%。R=5 时全局微调可达 5.50% EER。STOPA 上各法均大幅退化（最佳约 27.74% EER），严格低 FPR 下 TPR 仅约 1%。全局 k99≈121，pairwise≈13；全局 10 维瓶颈仍具竞争力（EER 7.05%）。细粒度错误显示 pairwise 在架构相近变体（如 Bark 系列）上混淆显著增多。

## 结论
在所测设置下，全局锚定仍是开集源追踪的强基线；pairwise 的差距不能仅用维度解释，而与目标塑造的嵌入方向及更重尾的分数分布有关。建议优先用全局锚定，仅在能证明低 FPR 收益时再考虑 pairwise。局限：结论依赖所测 pairwise 与 XLS-R/池化头；STOPA 排序仅作参考。

## 点评
论文把“生物识别里有效的 pairwise”搬到源追踪并系统证伪，诊断链（k99、分数 CDF、假接受分解、二元探针）比单纯刷 EER 更有说服力。强在指出目标塑造方向而非维度本身；脆弱处在于 OOD 上全体坍塌、且未覆盖监督对比/proxy 等更强度量损失，结论不宜过度外推到全部度量学习。

