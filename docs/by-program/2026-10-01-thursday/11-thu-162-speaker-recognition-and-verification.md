# Speaker Recognition and Verification

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：4
- 论文数：12
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。其中论文 2193 程序表未提供摘要，下文不臆造结果。

## 技术趋势

本场海报覆盖说话人表示学习骨干、模型压缩、联邦学习、半监督/自监督伪标签、短时验证、低资源语料构建，以及取证场景下的词 n-gram 与编解码失配分析。主线是在保持或逼近全监督性能的同时，降低部署成本、数据共享风险与标注需求，并正视短时、噪声、话题与编解码带来的不稳定性。

表示与压缩方面，流形约束超连接扩展残差信息流；持续 2D 谱—时 Transformer 避免过早坍缩谱时格；剪枝—量化复合误差用渐进蒸馏缓解。联邦学习用双分类头或 Fisher 关键关键关键维对齐缓解异构与冗余知识。伪标签从瞬时置信度扩展到历史稳定性（HistoMatch）与预训练层聚类一致性 + DINO 式自蒸馏。

应用与取证侧，短时验证构建 VoxPhrase 并混合文本相关/无关注册做神经重打分；VieSpeaker 用不依赖人脸的元数据—LLM 推理建越南语大规模集；取证则警示话题词偏置与编解码—时长—说话人依赖的个体差异，系统级良好指标不保证人人可用。

## 技术内容

### 骨干表示、压缩与谱—时建模

**Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning**（论文 634；Zhe LI）  
将残差路径改为多流演化，经双随机矩阵混合信息，并以 Sinkhorn-Knopp 保证能量守恒、稳定梯度。在 ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net 上替换标准残差，VoxCeleb1 上一致提升。

**Mitigating Pruning-Quantization Compound Errors for Ultra-Lightweight ResNet34-Based Speaker Recognition**（论文 587；城轩 龙）  
统一通道剪枝与低比特量化：ResRep-MB 用多分支压缩器评估通道重要性；PPQD 双教师渐进剪枝—量化蒸馏缓解剪枝与 INT4 复合误差。压缩 ResNet34 约 19.2×，相对 EER 劣化约 6.8%，并保持跨语鲁棒。

**Continuous 2D Spectral—Temporal Transformer for Speaker Verification**（论文 963；Seongwook Ham）  
C2D-ST 在骨干全程保持谱—时表示并在格上做全局依赖，仅末段做纯时间建模。VoxCeleb 上约 0.507 平均 EER、6.9M 参数，兼顾性能与参数效率。

### 联邦、半监督与自监督

**A Federated Learning-Based Speaker Recognition Method with Dual Classification Heads**（论文 25；Liang He）  
引入更知情的分类头使本地模型吸收更全面全局知识。VoxCeleb2 上相对本地训练平均 EER 改善 46.5%、相对 FedAvg 7.6%；VoxCeleb 与 CN-Celeb 联合训练相对本地 68.8%、相对 FedAvg 5.4%。

**Learning Global Key Knowledge for Federated Speaker Recognition via Fisher Information**（论文 196；Liang He）  
用 Fisher 信息矩阵抽取嵌入关键维，对齐全局与本地表示，引导本地学习全局关键知识以抑制冗余知识损害。

**HistoMatch: Unified Transient-Steady Assessment for Noise-Robust Semi-Supervised Speaker Verification**（论文 244；Shenghan Gao）  
以历史预测稳定性为稳态指标，结合瞬时置信度构成 DHSE 筛选高质量无标签数据。VoxCeleb1 三测试集 EER 0.91%/1.13%/2.13%，接近全监督。

**Self-supervised Speaker Verification with High-Confidence Pseudo-Label Selection and DINO-Style Self-Distillation Based on Pre-trained Models**（论文 1965；Yishuang Li）  
从 PTM 选 top-K 说话人判别层分别聚类，对齐后保留一致样本为高置信伪标签；高置信集用标签噪声校正损失，其余用 EMA 教师软蒸馏与一致性正则。VoxCeleb 上可达当前 SOTA 可比水平。

### 短时验证、低资源数据与取证

**Stabilizing Short Duration Speaker Verification through Neural Re-scoring with Hybrid Enrollment**（论文 228；Zhiqi Ai）  
构建 VoxPhrase 短时语料；分析显示 TD 注册受时长限制不稳定，TI 注册随时长更稳但有内容失配。提出混合注册神经重打分，并行交叉注意力做帧级比较，多说话人模型上一致提升。

**VieSpeaker: A Large-Scale Vietnamese Speaker Recognition Dataset Beyond Visual Dependency**（论文 3449；Viet Hoang Pham）  
不依赖人脸、用文本元数据与 LLM 从转写与上下文推断说话人；约 902 小时、4715 说话人。相对既有越南语数据提升鲁棒与泛化，展示无脸建库可行性。

**Confusion-Transport Pruning: Optimal-Transport Redundancy and CKA Geometry Distillation for Hard-Set Robust Speaker Verification**（论文 2193；presenter 未提供）  
程序表未提供摘要与作者/报告人完整信息，此处不臆造方法或实验结果。

**Function words: a topic independent approach to word n-gram selection for forensic speaker comparison**（论文 3166；Michael Carne）  
指出词 n-gram 基线（Cllr 0.60）含话题依赖项可能高估证据强度；用 156 个功能词特征集得 Cllr 0.83，ANOVA F-ratio 筛选至 k=50 后 Cllr=0.78。

**Codec-induced Mismatch, Speech Duration, and Speaker-dependent Effect in a DNN-based Forensic Speaker Recognition System**（论文 1004；Guangmou Deng）  
在 G.711 A-law、AMR-NB、Opus 与不同质疑语音时长下评估 ResNet34-MHA FASR：系统级在 >30s 时总体较好，AMR-NB 劣化最大、Opus 影响最小；个体层面存在显著说话人依赖，差说话人更易受编解码失配影响。

## 本场要点

- 残差多流与全程谱—时 Transformer 继续挖深说话人表示容量与效率。
- 剪枝—量化需专门处理复合误差；联邦双头与 Fisher 对齐应对异构。
- 半/自监督从历史稳定性与多层聚类一致性筛选伪标签逼近全监督。
- 短时验证宜混合 TD/TI 注册；无脸元数据管线可建低资源大规模说话人库。
- 取证需警惕话题词偏置与系统级指标掩盖的说话人依赖脆弱性；一篇无摘要条目不作结果推断。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 634 | Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning |
| 587 | Mitigating Pruning-Quantization Compound Errors for Ultra-Lightweight ResNet34-Based Speaker Recognition |
| 963 | Continuous 2D Spectral—Temporal Transformer for Speaker Verification |
| 25 | A Federated Learning-Based Speaker Recognition Method with Dual Classification Heads |
| 196 | Learning Global Key Knowledge for Federated Speaker Recognition via Fisher Information |
| 244 | HistoMatch: Unified Transient-Steady Assessment for Noise-Robust Semi-Supervised Speaker Verification |
| 1965 | Self-supervised Speaker Verification with High-Confidence Pseudo-Label Selection and DINO-Style Self-Distillation Based on Pre-trained Models |
| 228 | Stabilizing Short Duration Speaker Verification through Neural Re-scoring with Hybrid Enrollment |
| 3449 | VieSpeaker: A Large-Scale Vietnamese Speaker Recognition Dataset Beyond Visual Dependency |
| 2193 | Confusion-Transport Pruning: Optimal-Transport Redundancy and CKA Geometry Distillation for Hard-Set Robust Speaker Verification |
| 3166 | Function words: a topic independent approach to word n-gram selection for forensic speaker comparison |
| 1004 | Codec-induced Mismatch, Speech Duration, and Speaker-dependent Effect in a DNN-based Forensic Speaker Recognition System |
