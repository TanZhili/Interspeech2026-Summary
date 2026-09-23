# SE Architectures, Adaptation and Audio Front-Ends

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：6
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场语音增强（SE）与前端覆盖双编码器融合、可调重建–抑噪损失、增强与响度联合、复合退化条件注入、脉冲神经网络、并行时–频混洗前端、无字典离散注意力、音素敏感 TF 加权损失，以及真实远场分布对齐与无监督去混响。目标从“干净波形”扩展到 ASR 友好、会议响度达标与低功耗神经形态实现。

关键设计议题包括：条件应注入各层而非仅输入层；前后端模块联合优化（SE+AGC）；前端要并行高效并对 ASR 伪影可控；真实远场需轻量潜空间对齐弥合仿真–真实鸿沟。

## 技术内容

### 编码器融合、损失与联合流水线

**Dual-Encoder Fusion with Explicit and Implicit Injection for the Interspeech 2026 Audio Encoder Capability Challenge**（论文 463；Ming Li）以 Whisper 与 Dasheng 互补，比较隐式（融合前参数高效适应）与显式（残差分解+辅助正则隔离非冗余信息）注入。显式注入任务互补更强、更多单任务最优；并提出 token 级 softmax 门控残差融合加轻量 STFT 残差支路的稳定骨干。

**Balancing Speech Reconstruction and Noise Suppression Using Dual-Asymmetric Loss**（论文 794；Merlin Carson）提出可调参数损失平衡原语音重建与抑噪。多架构上相对基线可按目标抬高质量或抑噪；13 个参数取值下与语音/噪声指标相关达 0.95 / −0.96。

**SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios**（论文 1023；Eng Siong Chng）端到端联合 SE 与自动增益，利用 SE 保留轻声以利 AGC。提出 SE-AGC-DataGen 与 LUFS/St LUFS/LRA 响度指标。摘要称持续达标响度并提升语音质量与 ASR。

### 条件注入、神经形态与 ASR 前端

**SLICE: Speech Enhancement via Layer-wise Injection of Conditioning Embeddings**（论文 1715；Seokhoon Moon）从预训练多任务头得到噪声类型/混响/失真条件，注入 timestep 嵌入以贯穿残差块。对照实验中输入级条件在复合退化上劣于无编码器，而层向注入最优并泛化到真实录音。

**Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks**（论文 1797；Wenbin Jiang）GSU-DBNet 双支路同时建模幅度与复谱并预测相应掩码，双路径 GSU 挖掘时频信息。基准上 PESQ 3.04、仅 394K 参数，优于既有 SNN 方法，参数量为代表性 ANN 的约 4.5%–10.6%。

**Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends**（论文 1972；Xingyu Shen）Parallel Time-Band Mixer 消除块内循环展开，统一并行做带内时间混合与帧级跨带注意力，并以学习 Observation-Adding 抑制 ASR 敏感伪影。DNS/CHiME-4 上冻结 Whisper 后端相对循环带分基线降 WER；前端约 0.96M 参数、0.58 GMAC/s。

### 注意力、音素加权与真实/无监督适配

**Dictionary-Free Discrete Key-Value Attention for Improving Speech Enhancement**（论文 2881；Zihao Cui）提出 DFDA：受有限标量量化启发数据驱动离散化注意力 key/value，无需手工谐波字典。与 Harmonic Attention 适配到 TFGridNet 后，摘要称更好恢复浊/清音谱结构并抑噪。

**Time–Frequency Weighted Losses for Phoneme Reconstruction in DNN-Based Speech Enhancement**（论文 3416；Nasser-Eddine Monir）按局部语音存在、SIR 与谱通量调制 SDR，强调高竞争 TF 仓与辅音爆发等瞬态。摘要称提升频率加权增强指标与音素识别（尤其辅音），中频结构在较不利 SIR 下重建更好。

**Bridging the Distribution Gap in Real-World Far-Field Speech Enhancement via Lightweight Latent Representation Alignment**（论文 3478；Biao Liu）引入高质量真实数据与两阶段轻量框架：预训练去噪后，分布映射模块将特征对齐到干净近场潜空间再解码。真实测试集 P.835 OVRL 2.94、P.808 3.35，约 0.8 GMAC/s。

**ARTT: Augmented Reverberant-Target Training for Unsupervised Monaural Speech Dereverberation**（论文 1857；Wei-Qiang Zhang）先进一步混响观测混合再判别式恢复该混响混合（RTT），发现可有效去混响；再以 mean-teacher 在线自蒸馏增强。摘要称无监督去混响显著优于先前基线。

## 本场要点

- 双编码器显式/隐式注入为 LALM 模块化融合提供可操作经验。
- 可调双不对称损失与 TF 加权损失把增强目标与听感/音素可懂度对齐。
- SE+AGC 联合优化面向会议响度波动。
- 层向条件注入与学习 Observation-Adding 分别改善复合退化与 ASR 前端。
- 脉冲双支路以极少参数逼近 ANN 增强质量。
- 真实远场潜对齐与 ARTT 无监督去混响应对仿真–真实与无干净参考难题。

## 覆盖核对

| id | title |
|---|---|
| 463 | Dual-Encoder Fusion with Explicit and Implicit Injection for the Interspeech 2026 Audio Encoder Capability Challenge |
| 794 | Balancing Speech Reconstruction and Noise Suppression Using Dual-Asymmetric Loss |
| 1023 | SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios |
| 1715 | SLICE: Speech Enhancement via Layer-wise Injection of Conditioning Embeddings |
| 1797 | Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks |
| 1972 | Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends |
| 2881 | Dictionary-Free Discrete Key-Value Attention for Improving Speech Enhancement |
| 3416 | Time–Frequency Weighted Losses for Phoneme Reconstruction in DNN-Based Speech Enhancement |
| 3478 | Bridging the Distribution Gap in Real-World Far-Field Speech Enhancement via Lightweight Latent Representation Alignment |
| 1857 | ARTT: Augmented Reverberant-Target Training for Unsupervised Monaural Speech Dereverberation |
