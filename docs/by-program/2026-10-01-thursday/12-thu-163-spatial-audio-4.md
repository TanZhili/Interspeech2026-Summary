# Spatial Audio 4

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：5
- 论文数：11
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场空间音频海报贯穿测量校准、盲 RIR/房间嵌入、生成空间音频评测与视频到 FOA、双耳自监督空间表示，以及分布式阵列上的几何约束分离、几何自标定、定位与 DOA 引导分离。共同主题是把空间几何与语义内容解耦，并在标注有限时用对比、正则或伪测量流程补足监督。

生成与评测侧，FAD（定位相关嵌入）与声学图在响应性、平滑性与对称性上更稳健；视频到 FOA 用“先 mono W、后 XYZ 空间化”解耦 what/where，并以语义增强数据缓解稀疏。表示学习把方向性、扩散性等声学先验写入软声学对比损失。盲估计则从 CTF 重建到房间嵌入不确定性分数，强调内容与劣化导致的表示漂移。

阵列侧从有限阶质心校准方向响应，到 DOA 约束的去中心化 IVA、TDoA CRLB 优化声源放置、网格到连续定位网络、指向性正则 FastMNMF，以及说话人表征引导的多移动声源定位，持续压低排列不一致与网格分辨率—复杂度权衡。

## 技术内容

### 测量校准、盲 RIR 与房间嵌入不确定性

**Addressing random spatial translations in measured microphone directional responses by maximizing finite order energy**（论文 149；Xue Wen）  
提出有限阶质心：使方向响应在有限阶空间谐波能量最大的平移，用以抵消实测中的随机空间平移扰动，得到具有下游可用保证的校准方向响应，并用简单任务演示用途。

**Blind Room Impulse Response Identification via Reverberant Speech Spectrum Reconstruction**（论文 217；Pengyu Wang）  
Rec-RIR 基于 CTF：多任务网络依次去噪去混响，再经混响谱重建估计 CTF，并以伪侵入测量将 CTF 转为 RIR。摘要称盲 RIR 识别达 SOTA。

**Quantifying the Uncertainty of Blindly Estimated Room Embeddings Using a Dispersion-Calibrated Score**（论文 1357；Yang Xiang）  
学习对语音内容变化鲁棒的房间嵌入，并用无下游监督的表示级不确定性分数；嵌入锚定结构化 RIR 潜空间，经多视图 KL 对齐与多正对比细化；轻量不确定性头按损坏诱导嵌入离散度校准。推理仅需单句即可支持选择性预测。

### 生成空间音频评测与视频到 FOA、双耳 SSL

**Sensitivity Analysis of Generative Spatial Audio Metrics : A Study on Responsiveness, Smoothness, and Symmetry**（论文 252；Purnima Kamath）  
沿连续空间轨迹分析 FOA 生成指标对方位/仰角变化的响应性、平滑性与对称性。定位相关嵌入的 FAD 与声学图表现更稳健；强度向量随场景复杂度退化。

**FoleyImmersive: Decoupling What and Where for Video-to-First-Order Ambisonics**（论文 531；Liming Liang）  
Stage1 语义优先扩散生成 mono W，Stage2 复 STFT U-Net 结合逐帧视觉与相机方向将 W 空间化为 XYZ，方向残差混合器稳定定位。配套 YT-AmbiSem 语义增强数据；摘要称语义与空间指标达 SOTA。

**Learning Self-Supervised Spatial Representations via Soft Acoustic Contrastive Alignment**（论文 641；Yotam Silverman）  
双耳 SSL 的 Soft Acoustic Contrastive 损失按方向性、扩散性等共享声学属性对齐嵌入而无需真值标签；五项下游空间参数估计任务上持续优于基线。

### 分布式阵列：分离、标定、定位与 DOA 引导

**Geometrically Constrained Decentralized Independent Vector Analysis for Distributed Microphone Arrays**（论文 1037；Changda Chen）  
GC-Dec-IVA 引入 DOA 缓解阵列间排列失配，并弱化跨阵列源模型依赖以提升噪声下鲁棒；改进分离与跨阵列排列一致性。

**Optimal Source Placement for TDoA-based Geometry Calibration of Distributed Microphone Arrays**（论文 1691；Xu Wang）  
用移动机器人作多标定源，基于含时间偏移的 TDoA CRLB 优化位置（房间约束），并给出多阶段近似以兼顾算力与时延；数值实验验证有效。

**G2C-NET: A Grid-to-Continuous Neural Network for Sound Source Localization in Distributed Microphone Arrays**（论文 1733；Zhiyuan Yue）  
GLE 自适应成对特征聚合得网格全局似然，CPE 对高置信网格加权求和得连续位置，同等网格分辨率下优于既有网格 SSL。

**Fast Multichannel Nonnegative Matrix Factorization with Directivity Regularization for DOA-Informed Speech Separation**（论文 2139；Ryosuke Ono）  
对 FastMNMF 加指向性正则，使伪分离滤波器通过目标方向、抑制其他方向并容忍 DOA 误差；闭合形式 VCD 更新分离矩阵，仿真噪声同时语音混合上提升分离。

**SpkGuideDOA: Speaker-wise Representation Guidance for Multiple Moving Speaker Localization**（论文 3131；Yongseok Choi）  
辅助引导生成器从多通道幅度提取隐式说话人表征，经池化分辨率残差调制注入空间线索估计器；联合 PIT 保持说话人一致。仿真与 LOCATA 上提升定位且保持效率。

## 本场要点

- 有限阶质心、盲 Rec-RIR 与校准不确定性分数分别服务方向响应、RIR 与房间嵌入可靠性。
- 生成空间音频需指标敏感性分析；视频到 FOA 宜解耦语义与几何。
- 双耳软声学对比可把空间先验写入无标签预训练。
- 分布式阵列工作围绕排列一致性、CRLB 最优标定声源、网格—连续定位与 DOA/说话人引导。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 149 | Addressing random spatial translations in measured microphone directional responses by maximizing finite order energy |
| 217 | Blind Room Impulse Response Identification via Reverberant Speech Spectrum Reconstruction |
| 252 | Sensitivity Analysis of Generative Spatial Audio Metrics : A Study on Responsiveness, Smoothness, and Symmetry |
| 531 | FoleyImmersive: Decoupling What and Where for Video-to-First-Order Ambisonics |
| 641 | Learning Self-Supervised Spatial Representations via Soft Acoustic Contrastive Alignment |
| 1037 | Geometrically Constrained Decentralized Independent Vector Analysis for Distributed Microphone Arrays |
| 1691 | Optimal Source Placement for TDoA-based Geometry Calibration of Distributed Microphone Arrays |
| 1733 | G2C-NET: A Grid-to-Continuous Neural Network for Sound Source Localization in Distributed Microphone Arrays |
| 2139 | Fast Multichannel Nonnegative Matrix Factorization with Directivity Regularization for DOA-Informed Speech Separation |
| 3131 | SpkGuideDOA: Speaker-wise Representation Guidance for Multiple Moving Speaker Localization |
| 1357 | Quantifying the Uncertainty of Blindly Estimated Room Embeddings Using a Dispersion-Calibrated Score |
