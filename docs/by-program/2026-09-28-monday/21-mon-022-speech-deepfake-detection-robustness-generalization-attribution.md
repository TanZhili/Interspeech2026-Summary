# Speech Deepfake Detection: Robustness, Generalization, Attribution

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 4）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场围绕音频深度伪造检测的泛化、神经编解码鲁棒性、词级伪造定位、开集溯源与表征解耦。生成模型迭代使未见攻击成为常态；神经编解码又可能抹掉伪造痕迹并扭曲 bona fide 嵌入分布。

提升泛化的策略包括：用扩散重建制造难样本并配合多层特征聚合与正则辅助对比学习；针对编解码后 bona fide 更易被判假的偏移设计辅助损失与边界小批量；以及用频谱专家混合与幅度/相位显式编码补足预训练表示对物理线索的忽视。

任务形态也在扩展：微调 Whisper 以 next-token 预测同时转写并检词级伪造；双分支门控融合做开集源追踪；正交解耦抑制说话人身份泄漏。共同方向是把“难样本/分布偏移”纳入训练目标，并把身份与伪造伪影分开。

## 技术内容

### 难样本、编解码鲁棒与词级检测

**Diffusion Reconstruction towards Generalizable Audio Deepfake Detection**（论文 158；Bo Cheng）
以难样本分类为核心，比较多种重建范式并认定扩散最适于生成难样本，再结合多层特征聚合与 Regularization-Assisted Contrastive Learning（RACL）。实验称相对基线显著降低平均 EER，泛化更优。

**Hard Positive-targeted Training for Robust Audio Deepfake Detection under Neural Codec Processing**（论文 2167；Jiwon Seo）
嵌入分析显示神经编解码主要使 bona fide 向 spoof 区偏移。训练策略对常被误判的编解码 bona fide 加辅助正则，并以边界邻近的 bona fide–spoof 对构造小批量。EER 与准确率显示在 NC 条件下鲁棒性提升且保持 spoof 检测性能。

**Deepfake Word Detection by Next-token Prediction using Fine-tuned Whisper**（论文 628；Xin Wang）
对用生成模型替换真实话语中若干词的场景，微调 Whisper 在转写同时做合成词检测；并探索以部分声码化话语作微调数据降采集成本。域内合成词与转写错误率低；域外未见生成器上与专用 ResNet 检测器相当，但整体退化提示需加强泛化。

### 开集溯源、频谱适应与身份解耦

**Dual-Branch Gated Fusion for Open-Set Audio Deepfake Source Tracing**（论文 3008；Khalid Malik）
闭环模型难拒识未见合成器。双分支融合 XLSR-53 与 66 维 CORES 描述子，输入条件门控加权，联合交叉熵、能量间隔与门控多样性损失。MLAAD 上 ID 准确率 97.6%、EERc 4.9%，相对 2025 基线 FPR95 相对降 83.5%。

**Mixture of Spectral Experts for Audio Deepfake Detection**（论文 661；Zhe Li）
频率音频编码器显式建模幅度与相位，Mixture of Spectral Experts 在 SVD 域做低秩更新并冻结奇异基，以适应生成相关频谱伪影。在 ASVspoof 2019 LA、2021 LA/DF 与 In-the-Wild 上报告有效且对未见信道与真实攻击泛化强。

**Dual-Granularity Orthogonal Disentanglement for Generalizable Audio Deepfake Detection**（论文 836；Zhuodong Liu）
针对隐式身份泄漏，在样本级余弦正交与批次级交叉协方差两粒度强制特征独立，并以课程调度逐步加强约束、无需辅助网络或对抗。ASVspoof 2019 LA / 2021 DF / In-the-Wild EER 分别为 1.35%、7.88%、21.58%，跨数据集相对梯度反转解耦绝对优 2.60%。

## 本场要点

- 未见攻击泛化依赖难样本生成（扩散重建）与对比/正则目标。
- 神经编解码主要伤害 bona fide 侧，需针对性难正例训练。
- 词级深度伪造可用微调 Whisper 的 next-token 预测兼顾转写与检测。
- 开集溯源需门控融合互补描述子并显式做 ID/OOD 分离。
- 幅度/相位与频谱专家适配补足 SSL 对低层物理线索的盲区。
- 正交解耦抑制说话人身份泄漏以提升跨说话人/跨集泛化。

## 覆盖核对

- 158 | Diffusion Reconstruction towards Generalizable Audio Deepfake Detection
- 2167 | Hard Positive-targeted Training for Robust Audio Deepfake Detection under Neural Codec Processing
- 628 | Deepfake Word Detection by Next-token Prediction using Fine-tuned Whisper
- 3008 | Dual-Branch Gated Fusion for Open-Set Audio Deepfake Source Tracing
- 661 | Mixture of Spectral Experts for Audio Deepfake Detection
- 836 | Dual-Granularity Orthogonal Disentanglement for Generalizable Audio Deepfake Detection
