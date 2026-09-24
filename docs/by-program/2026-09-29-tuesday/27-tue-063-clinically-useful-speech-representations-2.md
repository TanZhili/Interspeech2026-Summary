# Clinically Useful Speech Representations 2

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：13
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以“临床有用”而非“预测准确”为主轴。邀请报告梳理临床有意义语音表征需满足可解释、跨人群/任务/语言/录音条件鲁棒、对临床有意义变化敏感、纵向可靠、对照临床构念验证，并最终支持真实研究决策，例证覆盖 ALS、帕金森、精神分裂、抑郁、自闭与认知障碍等。论文工作则分别给出 ALS 临床试验中可解释复合指数以降测量噪声、任务条件多模态融合估计认知量表、hikikomori 认知行为治疗中的纵向嗓音轨迹，以及睡眠剥夺法语朗读语音的可解释节约模型。

方法论上强调心理测量学评价（ICC、MDC）、多模态任务条件融合、纵向轨迹与 SHAP/症状网络等可解释分析，并关注性别年龄偏差与碳足迹等节俭性。整体上，临床语音 AI 议程从单点分类器转向可纵向监测、可解释且可部署的表征与指标。

## 论文技术总结

# Clinically meaningful speech representations

- 论文编号：
- 报告人：Vikram Ramanarayanan
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
现代语音模型可学到强表征并取得较高预测性能，但高准确率本身尚未带来广泛临床采用。需要可解释、跨人群/任务/语言/录音条件稳健、对有临床意义的变化敏感、纵向可靠，并相对相关临床构念与结局得到验证，最终能支持真实世界研究中的决策。

## 方法
报告综述「有临床意义的语音表征」演进，并以 ALS、帕金森病、精神分裂症、抑郁、自闭症、认知障碍等相关研究为例。重点讨论如何把先进模型、综合指标与可扩展多模态评估的能力，与可解释性、心理测量严谨性与临床验证结合起来。

## 实验与结果
摘要列举了应用病种方向，但未给出具体队列规模、指标数值或对比结果。

## 结论
目标是把语音表征从「实验室里好看」推进为「真实临床场景可用」的工具；关键在于解释性、稳健性与临床验证，而非仅预测精度。

## 点评
把「临床可用性」拆成可检验属性（解释、稳健、敏感、纵向可靠、构念验证），问题定义清楚。摘要无方法细节与数字，只能作议程级理解。


# Reducing Measurement Noise in Digital Speech Biomarkers: Interpretable Composite Index Scores for Longitudinal ALS Monitoring in Clinical Trials

- 论文编号：2841
- 报告人：Vikram Ramanarayanan
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/neumann26_interspeech.pdf

## 问题
单条数字语音特征易受录音条件、疲劳等噪声影响，SEM/MDC 过大，不利于 ALS 临床试验终点；复合指数能否跨自然史→试验队列泛化尚缺系统心理计量证据。

## 方法
在 EverythingALS 自然史数据（146 人）上，用等权、逻辑回归、LDA、逐步 Youden’s J 等方法为 10 个语音特征求权重，目标为延髓受累或听者努力。将权重用于 VRG50635 试验（54 人、716 录音）。任务含朗读、DDK、看图描述。用 LME 建模纵向变化，并报告 ICC、SEM、MDC95、Bland–Altman 等。

## 实验与结果
指数 ICC>0.9，相对单特征降低 MDC，同时保持对进展敏感；与 ALSFRS-R、PP/SVC 等斜率相关强（|\(\rho\)|>0.6），与 NfL 中等相关。时长类特征（如 RPSD）与指数贡献大。权重可跨数据集迁移。

## 结论
可解释复合语音指数能降测量噪声并跟踪 ALS 纵向变化，适合作试验稳健终点候选。

## 点评
自然史训权重、试验验泛化的设定贴近监管/终点需求。Spearman–Brown 聚合逻辑清晰。局限是特征集固定、听者努力标签样本有限，且复合分数解释性仍依赖成分可懂度。


# Task-Conditioned Audio-Text-Image Fusion for Cognitive Score Estimation from Speech-Based Assessments

- 论文编号：1424
- 报告人：Justyna Krzywdziak
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/krzywdziak26_interspeech.pdf

## 问题
轻度认知障碍者在看图描述中常漏掉场景细节与空间关系；仅音频/文本难显式建模“说了什么相对图”，且需从言语任务估计 MoCA/MMSE。

## 方法
波兰多中心 88 人（69 MCI、19 HC）五任务：口头答题、忆述故事、记词、看图描述、朗读。预训练音频/文本/（PD 可选）视觉编码器 + 任务条件融合；递进实验 E0–E6（eGeMAPS→单模态→late/mid fusion→视觉→标签条件图文对齐损失→MoE）。对齐损失鼓励 HC 高图文相似、惩罚 MCI 过高相似。患者级 5 折 CV。

## 实验与结果
总体最优 E6：MoCA RMSE 2.49、MMSE 2.14。PD 上最佳约 MoCA 2.11、MMSE 1.85。PD 信息量最大，朗读最难；任务间差异 ANOVA 显著。HC 图文相关更集中对角，MCI 更弥散。

## 结论
任务条件多模态融合与标签条件图文对齐可提升认知分数回归；看图描述最适合作视觉 grounding。

## 点评
把“描述是否贴图”做成可训对齐目标，契合 MCI 表型。样本量小、HC 少、类别不平衡，回归比分类更稳但仍需外部验证；Whisper 转写误差会传导到文本支路。


# Analyzing Longitudinal Vocal Changes During Cognitive Behavioral Therapy for Hikikomori Patients

- 论文编号：742
- 报告人：Samara S. Leal
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/leal26b_interspeech.pdf

## 问题
CBT/ICBT 疗效监测缺客观时序标记；多数抑郁语音研究做静态分类或前后差，难刻画治疗过程中的个体轨迹。

## 方法
SOLITAIRE 试验 35 名 hikikomori 患者、8 次会话、约 276.7 h 语音。会话级 MFCC 汇总，相对首会话基线校正。RQ1 用趋势/变异/早期跨被试稳定性筛稳定纵向 MFCC；RQ2 比较 Better/Worse 结局轨迹；RQ3 在 LOPO 下比较 MFCC+F0（MLP）与 wav2vec2（GRU）及融合。结局为归一化抑郁量表前后变化。

## 实验与结果
低阶 MFCC1–3 纵向趋势最强。年轻成人 Better/Worse 中后期轨迹分化更清晰，青少年更嘈杂。融合 wav2vec2 与 MFCC+F0 在各年龄/性别分层上 F1 最高，显示深度与手工特征互补。轨迹演化优于静态前后差。

## 结论
治疗相关语音变化更宜用会话轨迹刻画；深度与声学描述子融合可更好预测 ICBT 结局。

## 点评
真实纵向临床语音与 within-patient 归一化设计有价值。队列小、Better/Worse 阈值阈值依赖分位，泛化谨慎；仅分析声学特征符合伦理，但丢掉语言学线索也可能限性能。


# Acoustic Biomarkers of Sleep Deprivation on French Read Speech: Interpretable and Frugal Modeling of Sleep Deprivation and Its Symptoms

- 论文编号：777
- 报告人：Vincent P. Martin
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/martin26_interspeech.pdf

## 问题
睡眠剥夺及其后果（困倦、疲劳、表现下降）是重要公卫问题，临床需要可在自然场景下反复测量的工具。现有语音研究多聚焦主观困倦或疲劳等副作用，且近年健康语音常依赖大模型，难解释、耗能高，也少系统报告性别/年龄偏差。本文问：仅用可解释声学特征与简单分类器，能否估计睡眠剥夺及其相关症状，并同时评估偏差、能耗与分类器学到的构念特异性。

## 方法
数据为 SOMVOICE：28 名被试（16 女）随机顺序经历正常夜与全睡眠剥夺后做 MSLT；每次朗读前朗读约 150 词法语文本，共 336 段录音，经 rVAD 切成≥20 s 的 818 段。标签包括睡眠剥夺状态、MSLT 潜伏期（≤8 min）、KSS（>5）、疲劳 VAS（>50）、PVT 中位速度与 RTD。特征为 88 维 eGeMAPS、27 维 Snack，及二者早期融合。分类器为 SVC、Random Forest、HistGradientBoosting；嵌套分层分组 10×5 折，按说话人分组并平衡正负类、性别与年龄，段级训练、录音级多数投票，以 UAR 为主指标。用 McNemar 比较特征集，用 logistic 回归评估误分类相对年龄×性别的偏差，用 SHAP 解释特征贡献，用 codecarbon 估计能耗与碳足迹；并用症状网络与跨任务预测检验分类器是否学到更泛化的构念。

## 实验与结果
最佳聚合 UAR：KSS 0.628 最低，PVT-RTD 0.852 最高；睡眠剥夺 0.744、MSLT 0.706、疲劳约 0.65–0.68，PVT Speed/RTD 约 0.80–0.86。除睡眠剥夺任务上融合显著优于单特征集外，特征集间多数无显著差异。部分睡眠剥夺、KSS、疲劳系统存在年龄或年龄–性别交互偏差。SHAP 显示多任务与更低平均能量等相关，不同任务有特异描述符（如 MSLT 更高 F1 mean）。训练+解释合计约 0.450 kWh、8.55 g CO₂。跨任务上，剥夺/MSLT/KSS 较特异；两个 PVT 指标几乎可互换；疲劳与 KSS 易混淆（疲劳模型预测 KSS 的 UAR 甚至高于专训 KSS 模型）。

## 结论
作者认为可用节俭、可解释管线估计睡眠剥夺相关症状，并应同时报告偏差与学到的临床构念特异性。后续拟用贝叶斯推断联合症状网络与分类器估计做联合建模。

## 点评
工作刻意避开 foundation model，把重点放在可解释性、偏差审计与“分类器到底泛化了什么”三件事上，和健康语音里常见的刷分路线形成对照。弱点是样本量小（28 人）、朗读任务场景受限，且疲劳/KSS 混淆提示主观标签边界本身就不清，声学可分性可能部分来自相关构念而非单一症状。

