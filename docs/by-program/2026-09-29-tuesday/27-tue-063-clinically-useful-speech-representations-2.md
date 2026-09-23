# Clinically Useful Speech Representations 2

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：13
- 论文数：5
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场以“临床有用”而非“预测准确”为主轴。邀请报告梳理临床有意义语音表征需满足可解释、跨人群/任务/语言/录音条件鲁棒、对临床有意义变化敏感、纵向可靠、对照临床构念验证，并最终支持真实研究决策，例证覆盖 ALS、帕金森、精神分裂、抑郁、自闭与认知障碍等。论文工作则分别给出 ALS 临床试验中可解释复合指数以降测量噪声、任务条件多模态融合估计认知量表、hikikomori 认知行为治疗中的纵向嗓音轨迹，以及睡眠剥夺法语朗读语音的可解释节约模型。

方法论上强调心理测量学评价（ICC、MDC）、多模态任务条件融合、纵向轨迹与 SHAP/症状网络等可解释分析，并关注性别年龄偏差与碳足迹等节俭性。整体上，临床语音 AI 议程从单点分类器转向可纵向监测、可解释且可部署的表征与指标。

## 技术内容

### 邀请报告与 ALS 纵向复合生物标志

**Clinically meaningful speech representations**（论文 id 未提供；Vikram Ramanarayanan）邀请报告指出高预测性能尚未转化为广泛临床采用，并概述临床有意义表征应满足的可解释、鲁棒、敏感、纵向可靠与临床验证等要求，结合 ALS、帕金森、精神分裂、抑郁、自闭与认知障碍等领域研究例证进行综述。

**Reducing Measurement Noise in Digital Speech Biomarkers: Interpretable Composite Index Scores for Longitudinal ALS Monitoring in Clinical Trials**（论文 2841；Vikram Ramanarayanan）用自然病史数据估计特征权重构建复合指数，在 VRG50635 ALS 临床试验数据上系统心理测量评估；摘要称指数 ICC > 0.9，相对单特征降低 MDC，并经线性混合效应模型相对 ALSFRS-R 评估纵向变化敏感性。

### 认知评估多模态融合与治疗/睡眠纵向声学

**Task-Conditioned Audio-Text-Image Fusion for Cognitive Score Estimation from Speech-Based Assessments**（论文 1424；Justyna Krzywdziak）从语音认知任务估计 MoCA/MMSE：预训练音/文/可选视觉编码器经模态投影与任务条件融合，比较声学特征到基础模型嵌入、晚融合、中层交叉注意力融合与最终 MoE；并对看图说话样本引入标签条件图—文对齐损失，以刻画描述覆盖范围差异。

**Analyzing Longitudinal Vocal Changes During Cognitive Behavioral Therapy for Hikikomori Patients**（论文 742；Samara S. Leal）在 CBT 会话级录音上先筛选时序稳定、早期被试间变异低的 MFCC，轨迹分析区分临床改善/恶化模式，再比较 Wav2vec 2.0 与传统声学；摘要称 Wav2vec 2.0 与 MFCC、F0 融合在跨年龄性别组别上取得最高 F1。

**Acoustic Biomarkers of Sleep Deprivation on French Read Speech: Interpretable and Frugal Modeling of Sleep Deprivation and Its Symptoms**（论文 777；Vincent P. Martin）基于 SOMVOICE，用 eGeMAPS 与 Snack 等经验证简单特征及 SVM/随机森林/梯度提升，估计睡眠剥夺及其困倦、疲劳、表现下降等症状；评估性别年龄偏差，报告能耗与碳足迹，并用 SHAP 与症状网络/跨任务评价推动机制性解释。

## 本场要点

- “临床有用”要求超越准确率：可解释、鲁棒、敏感、纵向可靠与临床验证。
- ALS 复合指数可降测量噪声并保持对疾病进展的敏感性。
- 认知评分估计走向任务条件音—文—图融合与对齐损失。
- 治疗监测可用纵向 MFCC 轨迹 + 自监督嵌入融合。
- 睡眠剥夺研究强调可解释、节俭特征与偏差/碳足迹报告。
- 邀请报告与试验生物标志论文共同把议程锚定在真实临床决策支持。

## 覆盖核对

| paper_id | title |
|---|---|
| （空） | Clinically meaningful speech representations |
| 2841 | Reducing Measurement Noise in Digital Speech Biomarkers: Interpretable Composite Index Scores for Longitudinal ALS Monitoring in Clinical Trials |
| 1424 | Task-Conditioned Audio-Text-Image Fusion for Cognitive Score Estimation from Speech-Based Assessments |
| 742 | Analyzing Longitudinal Vocal Changes During Cognitive Behavioral Therapy for Hikikomori Patients |
| 777 | Acoustic Biomarkers of Sleep Deprivation on French Read Speech: Interpretable and Frugal Modeling of Sleep Deprivation and Its Symptoms |
