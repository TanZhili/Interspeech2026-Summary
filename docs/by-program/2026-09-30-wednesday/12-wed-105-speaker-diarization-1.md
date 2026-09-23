# Speaker Diarization 1

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：4
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场覆盖说话人日志（diarization）的空间增强、分割骨干、角色感知域适应、目标说话人打分校准、球面变分聚类、印度多语联合基准、基于音频语言模型的分离，以及音视频主动说话人检测与大音频语言模型端到端日志识别。主线是提升重叠语音、任意说话人数与领域迁移下的可靠性。

空间 DOA 线索被注入序列到序列神经日志；Retention Network、角色感知半监督与 GMM 分数校准分别改进分割、课堂师生角色与短段验证。聚类后端出现面向超球面嵌入的 SphereVBx，简化 EEND-VC。资源与范式上，Indic DiarBench 覆盖印度 22 种法定语言；LlaSep 用离散令牌因果 LM 生成式分离；RT-ASDNet 统一实时音视频主动说话人检测；GLSC-SDR 用全局–局部说话人分类增强 LALM 端到端能力。

## 技术内容

### 空间、分割骨干与角色适应

**Spatially-Augmented Sequence-to-Sequence Neural Diarization for Meetings**（论文 3473；Li Li）  
SA-S2SND 将 SRP-DNN 估计的 DOA 注入 S2SND；两阶段训练并引入模拟 DOA 生成以减轻对匹配多通道语料依赖。AliMeeting 上摘要称离线相对 S2SND DER 降 7.4%，结合通道注意力相对改进超过 19%。

**Bidirectional Retention Network-based Segmentation Model for Speaker Diarization**（论文 1032；Jian You）  
WavLM 前端 + 双向 Retention Network（BiRetNet）分割后端，用于 EEND-VC。RetNet 具并行与递归双形式及有利序列长度扩展。摘要称在两套常用日志数据集上优于 RNN、注意力与 Mamba 变体。

**Role-Aware Semi-Supervised Domain Adaptation for Teacher-Student Speaker Diarization**（论文 155；Zhen Liao）  
基于 Mean Teacher 的角色感知半监督域适应与 TSSD 数据集，将通用声学先验对齐课堂分布。Role-Aware Union Loss 把身份区分改为角色检测；PIT-MSE 一致性损失对说话人顺序不变。摘要称可把复杂声学场景解耦为角色流。

### 打分校准、球面聚类与多语基准

**Leveraging Diarization Labels for Robust Score Calibration in Target Speaker Tagging via Gaussian Mixture Modeling**（论文 896；Hee-Soo Heo）  
对每个日志聚类内分数拟合两成分 GMM，区分正确聚类与误聚类段，用最可能成分均值做稳健聚合。在 TST-Bench 与 ICSI 上摘要称跨工作点与嵌入架构持续优于未校准与常规基线。

**SphereVBx: Spherical Variational Bayes Clustering for Simplified EEND-VC Diarization**（论文 2224；Petr Pálka）  
基于 T-PSDA 的超球面贝叶斯聚类，用 von Mises–Fisher 混合替代高斯 PLDA；无参变体 SphereVBx-PF 接近余弦打分且无需预训练后端。摘要称级联管线聚类更准，EEND-VC 中相当或更好且显著简化聚类阶段。

**Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages**（论文 2484；Deovrat Mehendale）  
约 108 小时自然多说话人音频，覆盖印度 22 种法定语言，含近场、远场与野外，人工校正时间对齐说话人转写，含语码混合、方言与重叠。开放评测商业 API 与多模态 LLM 联合 ASR+日志能力。

### 生成式分离、实时 ASD 与 LALM 联合训练

**Speaker Separation via Audio Language Modeling**（论文 2864；Luca Lanzendörfer）  
LlaSep 在离散令牌域用因果 LM 单次解码生成各说话人编解码令牌流，条件于混合令牌与预训练语音编码器语义特征；在约 15k 小时七语合成会话上监督微调。LibriCSS 与 CallHome 上摘要称分离/日志有竞争力且音质显著更高。

**RT-ASDNet: Unified, Real-Time Active Speaker Detection**（论文 448；Okan Köpüklü）  
端到端统一音视频架构：原始波形与视频帧两流融合到无锚检测头，单次前向同时定位人脸并预测说话活动；每帧推理一次，计算量与人数无关。在 AVA-ActiveSpeaker 上为联合检测与分类设定基线。

**Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition**（论文 774；Yuhang Dai）  
GLSC-SDR 将说话人分类与日志识别联合训练；全局–局部策略用聚类说话人作全局标签、簇内重编码作局部标签。在 AliMeeting、AISHELL-4、AMI-SDM 上摘要称相对仿真与多编码器方法有竞争力或更优，且不依赖大规模真实会话数据。

## 本场要点

- DOA 空间线索与通道注意力互补，显著降低会议 DER。
- BiRetNet 分割后端在 EEND-VC 上优于 RNN/注意力/Mamba。
- 角色感知半监督适配课堂师生“多对一”映射。
- 聚类内 GMM 校准提升短段目标说话人打分稳健性。
- SphereVBx 简化超球面 EEND-VC 聚类。
- Indic DiarBench、LlaSep、RT-ASDNet、GLSC-SDR 扩展多语、生成式与 LALM 路径。

## 覆盖核对

| id | title |
|---|---|
| 3473 | Spatially-Augmented Sequence-to-Sequence Neural Diarization for Meetings |
| 1032 | Bidirectional Retention Network-based Segmentation Model for Speaker Diarization |
| 155 | Role-Aware Semi-Supervised Domain Adaptation for Teacher-Student Speaker Diarization |
| 896 | Leveraging Diarization Labels for Robust Score Calibration in Target Speaker Tagging via Gaussian Mixture Modeling |
| 2224 | SphereVBx: Spherical Variational Bayes Clustering for Simplified EEND-VC Diarization |
| 2484 | Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages |
| 2864 | Speaker Separation via Audio Language Modeling |
| 448 | RT-ASDNet: Unified, Real-Time Active Speaker Detection |
| 774 | Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition |
