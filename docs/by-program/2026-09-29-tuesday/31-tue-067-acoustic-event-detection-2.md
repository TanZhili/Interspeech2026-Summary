# Acoustic Event Detection 2

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：5；论文数：11
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场覆盖声音事件检测、异常声检测、开放词汇 SED、跨域小样本增量分类、超声发声检测、短时/事件扰动下的声场景分类，以及谱增强与音乐分类去偏。预训练前端 + 一致性/均值教师、概率化音文对齐、统一扩散异常检测，体现“少标签、多域、重叠事件”下的共同压力。

开放词汇与语义锚点、查询增强，把 SED 从闭集类别推向任意事件描述；跨域 FCAC 与事件注入 ASC 基准则直面分布偏移与前景事件干扰。噪声鲁棒边界引导注意力与 SpecAugment—Patch Merging，分别从边界约束与训练吞吐两侧优化。

音乐分类上的渐进可学习反事实注意力提醒：事件/场景模型同样需要抑制虚假判别区域。整体趋势是：结构化一致性、不确定性建模与鲁棒评测基准并行推进。

## 技术内容

### 预训练 SED、概率对齐与异常检测

**Consistency-Regularized Dual-Branch Network with Performance-Aware Mean Teacher for Sound Event Detection**（论文 353；Lipeng Dai）以 ATST 前端与双分支后端建模浅/深层特征，用时间拓扑一致性损失对齐双分支结构相似度，并以性能感知均值教师自适应 EMA；跨阶段融合后在 DCASE 2024 Task 4 上报告优势。

**MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining**（论文 360；Yu Nakagome）把音、文表示为分布而非点嵌入，用混合音文对模拟重叠声与语义包含关系，并以多层 inclusion loss 约束；在检索基准上优于确定性基线。

**UD-ASD: A Unified Diffusion Model for Anomalous Sound Detection**（论文 482；Pengxiang Gao）用轻量模块把机器 ID 嵌入条件，引导扩散重建 log-Mel，再用 GMM 拟合重建误差；统一模型跨多机型。摘要报告相对基线 AUC/pAUC 分别提升 3.44%/2.52%（DCASE2022 Task 2）。

**A Semantic-Anchor-based Method for Open-Vocabulary Sound Event Detection**（论文 731；Yanfeng Shi）学习语义锚向量作参考 token，配合双向注意力与查询增强。AudioSet-Strong 开放词汇设定报告 34.9 PSDS；DESED 零样本 PSDS1 达 44.1。

**Cross Domain Few-Shot Class-Incremental Audio Classification Via Adversarial Contrastive Learning**（论文 1250；Yanxiong Li）针对基类与增量类域偏移，以对抗对比训练；编码器基阶段训练后冻结，分类器全程更新。六组跨域数据上平均准确率超过既有方法。

### 专用检测、场景鲁棒、效率与音乐去偏

**USV-DETR: High-Resolution and Densely Supervised Detection of Ultrasonic Vocalizations**（论文 1492；Yilan Wei）基于 RT-DETR，引入高分辨率 P2 层与 DEIM 稠密监督，面向窄带短时稀疏 USV；跨数据集报告更精确时频定位。

**Enhancing Temporal Prediction Consistency for Short-Duration Acoustic Scene Classification via Semantic Adversarial Training**（论文 1955；Yiqiang Cai）指出短窗崩溃源于时间预测不一致；SAT 用对抗目标迫使特征丢弃时长依赖语义方差。报告一致性与准确率相关，并减轻高差异样本性能跌落。

**BG-CRNN: Boundary-Guided Dynamic Attention for Sound Event Detection in Complex Scenarios**（论文 2019；Zongmu Lin）用边界预测掩码限制自注意力于事件段内，并以 BGA 门控增强活跃区域。WildDESED 上在 10 dB 至 −5 dB SNR 下优于基线；−5 dB 时 PSDS1 为 0.191。

**Towards Event-Robust Acoustic Scene Classification**（论文 2350；Bohan Hu）发布 ESAS：用 LLM 辅助把前景事件注入背景场景，评测 ASC 对未知事件偏移的鲁棒性；现有模型显著退化。

**From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer**（论文 3273；Chanwoo Kim）在 patch 级 SpecAugment 后合并掩码 patch 对以减 token。AudioSet 上 mAP 近似不变（34.07→34.08）而吞吐 43.3→49.3 samples/sec；ESC-50、Speech Commands V2 呈类似模式。

**Progressive Learnable Counterfactual Attention for Music Classification**（论文 147；Yi-Xing Lin）提出多阶段 P-LCA：每阶段后将主分支注意力特征投影到新潜空间再去偏。Artist20、GTZAN、EMOPIA 上一致改进，可视化显示更聚焦稳定的注意力。

## 本场要点

- 一致性正则、性能感知均值教师与概率音文对齐，强化弱监督/重叠事件设定。
- 统一条件扩散 ASD 与语义锚点开放词汇 SED，分别服务多机监测与新类识别。
- 跨域 FCAC、ESAS 事件偏移基准把“域/事件干扰”升格为显式评测目标。
- 边界引导注意力与短时 ASC 对抗训练聚焦噪声与时长不一致。
- SpecAugment—Patch Merging 与 P-LCA 分别从训练效率与注意力去偏两侧补充工具箱。

## 覆盖核对

| id | title |
|---|---|
| 353 | Consistency-Regularized Dual-Branch Network with Performance-Aware Mean Teacher for Sound Event Detection |
| 360 | MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining |
| 482 | UD-ASD: A Unified Diffusion Model for Anomalous Sound Detection |
| 731 | A Semantic-Anchor-based Method for Open-Vocabulary Sound Event Detection |
| 1250 | Cross Domain Few-Shot Class-Incremental Audio Classification Via Adversarial Contrastive Learning |
| 1492 | USV-DETR: High-Resolution and Densely Supervised Detection of Ultrasonic Vocalizations |
| 1955 | Enhancing Temporal Prediction Consistency for Short-Duration Acoustic Scene Classification via Semantic Adversarial Training |
| 2019 | BG-CRNN: Boundary-Guided Dynamic Attention for Sound Event Detection in Complex Scenarios |
| 2350 | Towards Event-Robust Acoustic Scene Classification |
| 3273 | From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer |
| 147 | Progressive Learnable Counterfactual Attention for Music Classification |
