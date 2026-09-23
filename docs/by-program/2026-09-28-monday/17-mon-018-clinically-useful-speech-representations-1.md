# Clinically Useful Speech Representations 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 13）
- 论文数：8
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场聚焦临床可用的语音表征：抑郁与认知下降解耦、认知障碍筛查可解释性、ALS 言语障碍预测、痴呆检测基准可靠性，以及自然会话作为早期生物标志。共同张力是：声学/语言模型很强，但临床需要可解释、可对照并发评估、且经得起小样本陷阱检验的证据。

多篇强调“并发临床评分”与任务设计：在 MCI 老年人群中控制认知后再看抑郁相关声学；在 ALS 中比较跨说话人与个性化建模及不同言语任务；在 Cookie Theft 上从 CIU 空间分布扩展到时间图。另有工作把电话通话与受试者口头交流并入结构化临床数据融合，报告显著 AUC 提升。

可解释与试验设计是另一轴：SHAP+语言学特征+大模型叙事把黑盒筛查翻译成临床维度；时间到事件与风险率分析论证言语生物标志可加速 ALS 试验。与之对照，对 ADReSS/ADReSSo 的声学变异性审计显示：极简特征、标签置换仍可获竞争性测试表现，警示基准伪相关。层级认知评分研究则提示任务约束如何塑造“专才/通才”表征。

方向上，临床语音分析正从刷分转向：解耦共病、可解释落地、端点敏感度与基准可信度并重。

## 技术内容

### 共病解耦、可解释筛查与自然会话

**Disentangling Depression from Cognitive Decline in Elderly Speech Using Concurrent Clinical Assessments**（论文 1247；Woori Jeon）
老年 MCI 中抑郁与认知下降声学效应重叠。构建 89 名韩国老年 MCI 说话人、三年并发 SGDS 与 MMSE 语料。线性混合效应与偏相关均显示：七类特征中仅共振峰在控制认知后与抑郁相关，常用 F0 无信号；F1+F2 子集 12 维特征 UAR 0.760，优于完整 eGeMAPS 与自监督表示。

**From Black-Box to Clinical Insight: A Multi-Stage Explainable Framework for Speech-Based Cognitive Impairment Detection**（论文 1252；Maryam Zolnoori）
Transformer 认知筛查缺乏临床可解释性。框架整合 SHAP token 归因、理论驱动语言学特征与 LLaMA-3.1-70B-Instruct 四阶段推理，基于 SpeechCARE-Adaptive Gating Network（NIA PREPARE 上 F1=72.11%）。映射到词汇丰富度、句法复杂度、语义连贯等维度；70 例分层英语样本医师评估对齐良好，SUS 82/100。

**Natural Speech Encodes Early Markers of Cognitive Decline: Evidence from Clinical Conversations**（论文 1860；Maryam Zolnoori）
验证通话与受试者口头交流作为早期认知障碍生物标志。175 人注意力融合：仅结构化临床数据 AUC=0.74；加电话升至 0.76；加受试者口头交流达 0.90；最佳配置 AUC=0.92、F1=83.08。

### ALS 与试验端点

**Towards Speech Impairment Prediction in German-Speaking Individuals with Amyotrophic Lateral Sclerosis**（论文 1052；Monica Gonzalez-Machorro）
用两项临床言语相关评分预测德语 ALS 言语障碍，比较跨说话人与个性化范式并分析任务效用。66 人队列中，/da/-/da/、/da/-/ba/ 重复任务跨说话人预测 QoL 问卷 CCC=0.62；说话人内 CCC=0.86。

**Speech-based Digital Biomarkers can Accelerate ALS Clinical Trials: Insights from Time-to-Event and Hazard Rate Analysis**（论文 2847；Vikram Ramanarayanan）
用 Kaplan-Meier 与风险率比较言语衍生生物标志与传统 ALSFRS-R 子分对功能下降事件的检出。摘要称言语指标更快识别下降，并可用于估计检出疗效所需样本量与试验时长。

### 叙事图建模、基准批判与层级评分

**Automatic Graphical Representations of Language for Dementia Detection**（论文 1233；Si-Ioi Ng）
Cookie Theft 含 23 个 CIU，既往多靠人工标注且偏空间分布。框架自动识别 CIU，将 CIU 转移建模为时间图并提取图特征与可视化，以可扩展方式刻画叙事组织与时间动态。

**Rethinking Acoustic Variability Of ADReSS and ADReSSo Datasets For Dementia Detection**（论文 2862；Muhammad Abdullah Zafar）
系统审视两挑战测试集声学变异：仅两维低级声学特征可达近 SOTA；随机置换痴呆标签仍可获竞争性测试表现；Monte Carlo 重采样下特征可分性不泛化。结论警示强结果可能来自伪相关，需更谨慎解读小数据集基准。

**Beyond Binary: Speech Representations Across the Cognitive Score Hierarchy**（论文 2725；Serli Kopar）
基于 5,754 段德语神经心理评估录音，在任务/域/全局三层比较手工声学与 SSL 嵌入。SSL 在较低层通常更优，但 MCI 分类趋势反转；响应自由度高的任务随层级升高表现稀释，高度结构化任务则向高层提升，对应“专才/通才”表征。

## 本场要点

- 并发临床评分可把抑郁相关声学从认知下降中解耦，共振峰比 F0 更关键。
- 可解释框架与自然会话融合推动筛查从黑盒分数走向临床叙事与可扩展生物标志。
- ALS 工作同时覆盖德语障碍预测与试验加速的时间到事件分析。
- Cookie Theft 分析从空间 CIU 扩展到自动时间图。
- ADReSS/ADReSSo 审计提醒：小基准上的高分可能反映伪相关而非病理线索。
- 认知评分层级与任务约束共同塑造表征的专才/通才属性。

## 覆盖核对

- 1247 | Disentangling Depression from Cognitive Decline in Elderly Speech Using Concurrent Clinical Assessments
- 1252 | From Black-Box to Clinical Insight: A Multi-Stage Explainable Framework for Speech-Based Cognitive Impairment Detection
- 1052 | Towards Speech Impairment Prediction in German-Speaking Individuals with Amyotrophic Lateral Sclerosis
- 1233 | Automatic Graphical Representations of Language for Dementia Detection
- 1860 | Natural Speech Encodes Early Markers of Cognitive Decline: Evidence from Clinical Conversations
- 2847 | Speech-based Digital Biomarkers can Accelerate ALS Clinical Trials: Insights from Time-to-Event and Hazard Rate Analysis
- 2862 | Rethinking Acoustic Variability Of ADReSS and ADReSSo Datasets For Dementia Detection
- 2725 | Beyond Binary: Speech Representations Across the Cognitive Score Hierarchy
