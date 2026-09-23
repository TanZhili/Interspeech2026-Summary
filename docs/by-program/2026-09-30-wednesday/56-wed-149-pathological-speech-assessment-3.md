# Pathological Speech Assessment 3

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：13
- 论文数：8
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场延续病理语音评估：神经退行与运动障碍（ALS、亨廷顿）、抑郁跨库检测、构音障碍严重度，以及上气道疾病相关鼻化。贯穿问题是临床标注稀缺、异质性强与跨语料/跨人群迁移难。

数据增广与参数高效适配成为主路径：流匹配大规模合成病理/健康元音，并考察合成规模定律；MOS 合成评测语料迁移到构音障碍可懂度/自然度；WavLM 上层次 LoRA-MoE 用临床监督路由做严重度专用专家。图学习则把多发音片段 SSL 嵌入聚成被试级图，服务 ALS 严重度与进展预测。

抑郁检测强调稀疏诊断线索：跨模态自适应门控按帧重加权；层间多因素自适应解缠抑制说话人/语料干扰在层级中的累积。亨廷顿篇章朗读用多语种复合时间语音指数对齐 UHDRS；上气道手术前后则用 A1-P0/A1-P1 系统分析元音鼻化。整体上，临床可用性依赖“可迁移表征 + 可解释声学指标 + 可扩展合成监督”。

## 技术内容

### ALS、合成增广与抑郁检测

**Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction**（论文 844；Behrad TaghiBeyglou）  
将多发音录音 2 秒片段的预训练 SSL 嵌入建成被试级 kNN 图，比较四种 SSL 前端与五种 GNN。SAND（339 人）上 HuBERT+GIN 验证集宏 F1 达 0.73（5 类构音严重度）与 0.69（4 类 ALSFRS-R 进展），优于基线 0.61/0.58。

**Synthetic Pathological Speech at Scale: A Flow Matching Approach for Clinical Data Augmentation**（论文 2313；Alkis Koudounas）  
流匹配框架用临床状态 token 条件合成病理与健康元音；监督分类器在 100–100,000 合成样本上训练。四语言上仅用 10 万合成训练的分类器在留出真实数据上优于真实基线（准确率 +3.9%，灵敏度 +13.3%）；合成增广亦提升多类病理零样本迁移与帕金森元音检测。

**Learning to Attend to Depression-Related Patterns: An Adaptive Cross-Modal Gating Network for Depression Detection**（论文 1075；Hangbin Yu）  
抑郁相关模式在语音中稀疏分布于特定片段。ACMG 跨模态自适应门控重分配声学与文本帧级权重。系统优于无 ACMG 基线；可视化显示自动关注低能量声学段与含负面情感的文本段。

**Layer-wise Multi-factor Adaptive Disentanglement for Cross-corpus Speech Depression Detection**（论文 465；Minggang Wang）  
跨库迁移中多源因素在网络层级累积，仅说话人或输出层约束不足。LMAD 在关键编码器层约束中间表示降低对说话人/语料依赖、保留抑郁信息，并以自适应权重调节层间/层内解缠强度。DAIC-WoZ↔Androids 双向迁移优于基线与仅说话人解缠，库内仍具竞争力。

### 构音障碍、亨廷顿与上气道鼻化

**Augmenting Dysarthric Speech Severity Assessment with MOS Supervision**（论文 1300；Zengrui Jin）  
临床构音标注稀缺，提出用 QualiSpeech 的人工 MOS 合成评测数据增强。在合成评测数据上微调一致提升可懂度与自然度预测；联合训练主要增益自然度。提示合成伪影与构音障碍共享感知共性。

**Clinically-Supervised Hierarchical LoRA-MoE: A Parameter-Efficient Framework for Severity-Aware Dysarthric Speech Assessment**（论文 3043；Jiaqi Wang）  
冻结 WavLM，浅层共享 LoRA 做通用声学建模，深层动态路由专家 LoRA 捕获严重度特异性模式，临床监督路由按话语特征激活专家。UA-Speech 2/5 类设置 F1 达 94.54%/61.55%，优于全量微调。

**A multilingual composite speech index to assess passage reading in Huntington’s disease**（论文 2654；Valentina G. Constantin）  
对英/波/西三语 89 名 HD 与 82 名对照篇章朗读，自适应阈值检测有声活动突发并估计时间特征；按语种对照标准化后平均得 CTSI。CTSI 与 UHDRS 综合、认知、运动分强相关，与符号数字模态测验相关最高。

**Vowel Nasalization in Upper Airway Diseases: An Analysis Using the CUCO Database**（论文 46；Qi Wang）  
用 CUCO 分析鼻中隔成形、内镜鼻窦手术、扁桃体切除患者与健康对照术前术后元音鼻化（A1-P0、A1-P1）。A1-P0 对病理差异更敏感，鼻化依赖元音且 /u/ 对共鸣变化最敏感；仅扁桃体切除组出现短暂早期术后变化，其他组无长期差异。

## 本场要点

- ALS 可用多发音 SSL 图学习做严重度与进展估计。
- 流匹配大规模合成可缓解病理数据稀缺并改善跨域。
- 抑郁线索稀疏，需跨模态帧级门控与层间多因素解缠做跨库。
- MOS 合成评测与层次 LoRA-MoE 降低对稀缺临床标注的依赖。
- 亨廷顿篇章朗读复合时间指数与认知/运动量表相关。
- 上气道疾病可用元音鼻化指标做术前术后语音分析。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 46 | Vowel Nasalization in Upper Airway Diseases: An Analysis Using the CUCO Database |
| 465 | Layer-wise Multi-factor Adaptive Disentanglement for Cross-corpus Speech Depression Detection |
| 844 | Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction |
| 1075 | Learning to Attend to Depression-Related Patterns: An Adaptive Cross-Modal Gating Network for Depression Detection |
| 1300 | Augmenting Dysarthric Speech Severity Assessment with MOS Supervision |
| 2313 | Synthetic Pathological Speech at Scale: A Flow Matching Approach for Clinical Data Augmentation |
| 2654 | A multilingual composite speech index to assess passage reading in Huntington’s disease |
| 3043 | Clinically-Supervised Hierarchical LoRA-MoE: A Parameter-Efficient Framework for Severity-Aware Dysarthric Speech Assessment |
