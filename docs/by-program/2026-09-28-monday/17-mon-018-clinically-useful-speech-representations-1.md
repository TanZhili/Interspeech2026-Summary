# Clinically Useful Speech Representations 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：13
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦临床可用的语音表征：抑郁与认知下降解耦、认知障碍筛查可解释性、ALS 言语障碍预测、痴呆检测基准可靠性，以及自然会话作为早期生物标志。共同张力是：声学/语言模型很强，但临床需要可解释、可对照并发评估、且经得起小样本陷阱检验的证据。

多篇强调“并发临床评分”与任务设计：在 MCI 老年人群中控制认知后再看抑郁相关声学；在 ALS 中比较跨说话人与个性化建模及不同言语任务；在 Cookie Theft 上从 CIU 空间分布扩展到时间图。另有工作把电话通话与受试者口头交流并入结构化临床数据融合，报告显著 AUC 提升。

可解释与试验设计是另一轴：SHAP+语言学特征+大模型叙事把黑盒筛查翻译成临床维度；时间到事件与风险率分析论证言语生物标志可加速 ALS 试验。与之对照，对 ADReSS/ADReSSo 的声学变异性审计显示：极简特征、标签置换仍可获竞争性测试表现，警示基准伪相关。层级认知评分研究则提示任务约束如何塑造“专才/通才”表征。

方向上，临床语音分析正从刷分转向：解耦共病、可解释落地、端点敏感度与基准可信度并重。

## 论文技术总结

# Disentangling Depression from Cognitive Decline in Elderly Speech Using Concurrent Clinical Assessments

- 论文编号：1247
- 报告人：Woori Jeon
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/jeon26_interspeech.pdf

## 问题
老年 MCI 中抑郁与认知下降的声学效应重叠；缺少同步临床评分时，分类器可能学到认知而非抑郁特异模式。常用 F0 特征未必在控制认知后仍有效。

## 方法
韩国老年 MCI 朗读语料：89 人三年纵向 209 次观测，每次同步 SGDS（抑郁）与 MMSE（认知）。提取 eGeMAPS 七组；对各组 PC1 做 LMM（含 SGDS+MMSE）与偏相关（控 MMSE 等）。再用组内全特征 SVM（LOSO）做抑郁二分类，并对比 Whisper CER/WER 与 SSL 嵌入。

## 实验与结果
七组中仅 formant 在控认知后与抑郁显著相关（LMM \(\beta=-0.095\)，偏相关 \(r=-0.196\)）；F0 无信号。Formant 18 维 UAR 0.747；F1+F2 子集 12 维 UAR 0.760，优于全 eGeMAPS 与多种 SSL。F0 组 UAR≈0.512 近随机。

## 结论
作者认为同步临床评估可分离抑郁特异声学标记；在该 MCI 朗读任务中，共振峰（尤其 F1/F2）比常用 F0 更关键。

## 点评
方法学贡献在于“先统计去混杂、再分类验证”，避免事后挑特征。样本仍偏小、任务为朗读“秋天”段落，外推到自发语与其他语言需谨慎。


# From Black-Box to Clinical Insight: A Multi-Stage Explainable Framework for Speech-Based Cognitive Impairment Detection

- 论文编号：1252
- 报告人：Maryam Zolnoori
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/haghbin26_interspeech.pdf

## 问题
基于 transformer 的认知障碍筛查性能提升，但黑盒难临床落地；现有 SHAP/LIME 多停在 token 重要性，缺少与认知–语言机制及可读叙述的衔接。

## 方法
在 SpeechCARE-AGF（mGTE 语言 + mHuBERT 声学 + 年龄门控融合，NIA PREPARE F1=72.11%）上建四级可解释管线：子词 SHAP 聚合到词；词汇丰富度/句法/不流畅/语义连贯等理论特征；LLaMA-3.1-70B-Instruct 四阶段推理，把归因与特征译成结构化临床叙述。数据 PREPARE（英/西/普，2,058 人）。

## 实验与结果
医生在 70 例分层英语样本上评估，解释与患者级认知画像对齐良好；系统可用性 SUS 82/100，提示工作流集成潜力。筛查模型本身为 PREPARE 挑战获奖架构。

## 结论
作者认为多阶段 XAI 可将黑盒预测转为临床可理解叙事，有助于筛查模型的可解释部署。

## 点评
重点不在抬分类分数，而在临床可沟通性；LLM 叙事层是差异化。局限：医生评测规模有限且偏英语；解释质量依赖 ASR 转写与 LLM 忠实度，幻觉风险需临床把关。


# Towards Speech Impairment Prediction in German-Speaking Individuals with Amyotrophic Lateral Sclerosis

- 论文编号：1052
- 报告人：Monica Gonzalez-Machorro
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalezmachorro26_interspeech.pdf

## 问题
ALS 球麻痹致言语障碍，临床用 ALSFRS-R-speech 与 QOL-Dys 等量表；德语队列上跨说话人 vs 个体内预测、以及何种言语任务更有信息量，尚缺系统对比与采集标准化参考。

## 方法
AIMnd 2.0 中 66 名德语 pwALS、最多三访；任务含持续 /a:/、Cookie Theft、/da/-/da/、/da/-/ba/、北风与太阳朗读。特征：eGeMAPS、Whisper Large v3、Wav2vec2-de。SVM/XGB/RF 回归两量表；跨说话人分层划分与个体内时间划分；任务预测可均值融合。

## 实验与结果
跨说话人：QOL-Dys 上重复任务 /da/-/da/、/da/-/ba/ 最佳 CCC≈0.62；朗读/看图对 ALSFRS-R-speech 可达约 0.64–0.65。个体内设置可达 CCC 0.86（摘要报告）。多任务融合亦有竞争力。作者强调结果为德语 ALS 言语障碍预测的初步步骤。

## 结论
作者认为声学特征可跨人与个体内预测言语相关临床分；重复任务对 QoL 主观言语特征尤其有用，有助于标准化采集讨论。

## 点评
价值在同一队列上对照量表、任务与建模范式，服务协议标准化。样本量与访次有限；个体内高 CCC 依赖有随访的子集，监测场景外推需更大纵向数据。


# Automatic Graphical Representations of Language for Dementia Detection

- 论文编号：1233
- 报告人：Si-Ioi Ng
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/xu26n_interspeech.pdf

## 问题
Cookie Theft 图画描述中，基于 23 个 content information units（CIUs）的分析能反映描述的信息相关性与效率，但现有 CIU 分析依赖人工标注、对未见词鲁棒性差，且多关注空间分布，较少刻画 CIU 之间的时间动态（如空话、拖延过渡、反复纠缠少数 CIU）。

## 方法
流水线：录音下采样至 16 kHz → WhisperX 得到带词级时间戳的转写 → 微调 BERT-base-uncased 做 23 类多标签 CIU 识别（辅以低权重 ranking loss）→ 用 Layer-wise Relevance Propagation（LRP）定位各 CIU 对应词/跨度并取 onset 时间 → 将 CIU 序列建成有向时间图（边权为相邻 CIU 时间间隔），提取 unique nodes、归一化 walk length/cycles、degree centralization、relative edge jitter 等图特征，并与 unfilled pause rate、speech rate 对比。训练数据为 Pitt + WRAP（2,783 转写 / 1,352 说话人），测试与统计在 W-ADRC（Normal vs Clinical）。

## 实验与结果
W-ADRC 上 CIU 识别：人工转写 F1 0.879±0.086，ASR 转写 F1 0.865±0.098；LRP 定位准确率 0.910±0.067（“girl 的动作”类仅 0.741）。组间比较（校正年龄/性别/教育）：Clinical 组词数更少、停顿率更高、语速更慢；unique nodes 显著更少（Hedge’s g=0.80）；归一化 walk length、mean/std edge weight、relative edge jitter 等也显著更差；Normal 组归一化 cycle 反而更高，作者解释为有目的补充说明而非病理固着。

## 结论
自动化 CIU 识别 + 时间图特征可扩展、可解释地补充既有空间—语义 CIU 分析，支持认知—语言能力筛查。未来需改进临床语音的 WhisperX 切分与低敏感 CIU 定位，并做成临床可视化界面。

## 点评
做法把“说了哪些内容单元”与“单元间多久、是否迂回”绑在一张时间图上，比单纯计数 CIU 或静音率更贴近“空话/低效叙事”的临床描述。弱点在于依赖 ASR 与 LRP 定位质量（动作类 CIU 明显更弱），且图特征仍与话语长度强相关，归一化能否完全去掉长度混杂还需谨慎解读。


# Natural Speech Encodes Early Markers of Cognitive Decline: Evidence from Clinical Conversations

- 论文编号：1860
- 报告人：Maryam Zolnoori
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/haghbin26b_interspeech.pdf

## 问题
ADRD 早期症状在结构化 EHR 中记录稀疏，实验室短任务语料又偏晚期、生态效度不足；真实照护场景中的电话回访与护患对话是否能作为可扩展的早期认知障碍生物标志，增量价值尚不明确。

## 方法
175 人多模态语料（47 认知下降 / 128 健康）：约 100 维结构化临床变量 + 护理笔记；回访电话（均约 9 min）与护患口头交流（均约 29 min）。AWS Transcribe 转写与说话人分离，GPT-4o 映射患者侧；SpeechDETECT 提六类声学特征，BERT / BioMedBERT 提语言嵌入。轻量 bottleneck 融合：各模态经 adapter/encoder 成 token，用 m=8 可学习 fusion tokens 做 cross-attention + self-attention，再经 MLP 分类。分步加入模态；缺失模态用训练集均值填补；五随机种子报告均值±标准差。

## 实验与结果
EHR  alone：AUC 0.74±0.05，CI 类 F1 58.22。加首次电话：AUC 0.76，F1 61.95；加两次护患对话：AUC 0.90，F1 78.22。最佳为 EHR + 首次电话 + 两次护患对话：AUC 0.92±0.03，F1 83.08±3.59，Macro F1 88.31。Gradient×Input：首次护患对话贡献最大（34.6%），EHR 最小（17.4%）；声学与语言贡献接近（52.6% / 47.4%），声学侧以谱/倒谱为主。完整模态子集与性别/年龄分层结果大体稳定。

## 结论
真实场景自然对话相对结构化 EHR 能显著提升早期认知障碍检出；语音可作为可扩展、非侵入的功能向标志。局限包括样本规模与语言多样性不足，尚需纵向验证是否预测进展而非短期波动。

## 点评
增量消融设计清楚：先钉死 EHR 基线，再分别量化电话与护患对话的增益，结论可操作性强。瓶颈融合与归因分析也把“哪路信号在起作用”说清楚了。需注意缺失填补、小样本分层与电话标准化话术可能抬高可迁移性预期；最佳配置依赖较长护患录音，落地成本高于纯 EHR。


# Speech-based Digital Biomarkers can Accelerate ALS Clinical Trials: Insights from Time-to-Event and Hazard Rate Analysis

- 论文编号：2847
- 报告人：Vikram Ramanarayanan
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kothare26_interspeech.pdf

## 问题
ALS 试验主终点 ALSFRS-R 对早期球麻痹变化不够敏感且可能非线性；多数语音生物标志评估用线性混合模型，对非正态、异方差与不规则随访不够稳健。需要用 time-to-event 视角检验语音/面部数字标志能否更早检出功能下降，并据此估计试验样本量与时长。

## 方法
EverythingALS 招募、Modality 平台远程纵向采集（约每 2 周；2020-11 至 2024-04）。Praat / MFA 提语音特征，MediaPipe 提面部运动，spaCy 提图画描述语言特征；聚焦九个既往敏感指标。事件定义为达到最保守（最大）MCID；ALSFRS-R 言语题下降 1 分、球麻痹亚分下降 3 分。Kaplan–Meier + log-rank；由 KM 用指数近似估 hazard rate，再按 log-rank 公式在 HR=0.5/0.8、3–24 月下估每臂样本量，或固定 n=30 估所需时长（80% power，α=0.05）。

## 实验与结果
九个数字标志的 KM 曲线均比 ALSFRS-R 更陡：20% 患者达 MCID 最短约 14 天（阅读段落最大唇宽），最长约 100 天（阅读段落时长）；对应 ALSFRS-R 球麻痹亚分约 660 天、言语题约 208 天。数字标志相对球麻痹亚分均 log-rank p<0.001。示例：HR=0.8、12 月时球麻痹亚分约需 2551/臂，而 CTA、时长、F0、唇宽等可降至数百甚至数十；n=30/臂、HR=0.5 时球麻痹需约 137 月，最大唇宽约 4 月。

## 结论
远程语音/面部数字标志可更早检出临床有意义变化，有望缩短试验、减少样本量；宜与传统量表联用。局限：患者异质性、常数 hazard 近似、删失偏倚，泛化仍待验证。

## 点评
把“更敏感”直接翻译成试验设计数字（样本量/时长表），对产业与临床读法都很有冲击力。MCID 取最保守估计降低假事件，但 KM+指数近似仍假设风险形态，且唇宽等与 ALSFRS-R 相关弱却事件极早，需警惕测量噪声与定义阈值对“加速”幅度的放大。


# Rethinking Acoustic Variability Of ADReSS and ADReSSo Datasets For Dementia Detection

- 论文编号：2862
- 报告人：Muhammad Abdullah Zafar
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zafar26_interspeech.pdf

## 问题
ADReSS / ADReSSo 已成为语音痴呆检测事实标准，但小数据、录音条件残余不平衡可能导致模型利用通道伪相关而非病理线索；既有工作已显示静音段也可区分，整段录音上低层声学特征是否同样脆弱尚欠系统检验。

## 方法
对 openSMILE 的 eGeMAPS（88）与 ComParE（6373）做单特征筛选后再做两特征组合；一律用可解释的 logistic regression，报告 macro-F1。评价设定：(1) 官方 challenge 测试集；(2) 训练标签随机置换 100 次负对照；(3) 全数据 70/30 平衡蒙特卡洛重采样 100 次。另用 pyannote VAD 构造 silence-only / speech-only 变体，检验高分特征是否依赖语音本身。

## 实验与结果
两特征即可逼近 SOTA：ADReSS macro-F1 0.875（SOTA 0.895），ADReSSo 0.831（SOTA 0.857）；所选特征偏听觉滤波能量分位、谱质心导数、MFCC 统计等，易受通道/静音边界影响。同一特征对上 silence-only 反优于 speech-only（0.702 vs 0.643；0.631 vs 0.576）。标签置换时测试 F1 上界可分别摸到 0.875 / 0.831。蒙特卡洛下两特征均值降至 0.622 / 0.667；eGeMAPS 中极少特征对在 ≥50% 迭代复现，ComParE 无一达标，复现对最高也仅约 0.73 / 0.69。

## 结论
强测试分可能来自固定划分上的偶然相关，不宜过度解读；小样本痴呆语音评测应报告重采样离散度、标签置换负对照，并重视可解释、锚定临床标记的建模。

## 点评
用“极简两特征 + 负对照 + 重采样”拆穿乐观测试集，方法论上很干净，对后续凡报 ADReSS(o) 数字的工作都是重要刹车。它不否定病理声学信号存在，而是证明当前划分与 LLD 探针不足以支撑强泛化声称；后续若继续用这两套数据，至少应把蒙特卡洛均值/方差与静音对照一并报出。


# Beyond Binary: Speech Representations Across the Cognitive Score Hierarchy

- 论文编号：2725
- 报告人：Serli Kopar
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kopar26_interspeech.pdf

## 问题
临床语音分析常做 AD vs HC 二分类，对 MCI 细微变化不敏感；英语单任务语料多，且把各临床分数当扁平独立目标，忽视 CERAD+/MMSE 固有的任务—领域—全局层级结构。

## 方法
TREND 德语队列：MMSE + 五项 CERAD+（RW、BNT、RL、VF、PF），质控后 959 会话 / 593 人（698 HC、261 MCI）。优化 diarization 后得到 Prosody-Preserved 与 Concatenated 两路音频；提 eGeMAPS（prosody / voice-quality / all）与 wav2vec 2.0、HuBERT 全局均值池化嵌入。对每个层级目标独立训练 Ridge / SVM(R) / XGBoost，开发集 5×3 嵌套交叉验证（被试不相交），再在 hold-out 验证。层级：任务分 → 领域复合分（LAN/MEM/EXE/VIS）→ CERAD+ 总分（连续与阈值 85）及 MCI 二分类（>1.5 SD）。

## 实验与结果
Level 1：SSL（尤其 HuBERT）普遍优于手工艺声学；开放任务（VF/PF）相关更高，HuBERT 预测 PF 达 r=0.85±0.02（HO 0.80）。Level 2：HuBERT 仍最强，画图导向的 EXE/VIS 更弱。Level 3：开放任务出现“稀释”（任务级 → 全局级下降），受限任务（MMSE、RW）出现反向稀释。MCI 二分类最佳为 MMSE + eGeMAPS All（DEV 0.62±0.07，HO 0.63）；连续/二值 CERAD+ 与 LAN 等则 HuBERT 更优。SVM 权重显示 MCI 侧 F0/谱斜率不稳定等可解释声学线索。

## 结论
语音特征预测力同时取决于认知目标所处层级与任务约束：开放任务偏“专家”、受限筛查偏“通才”。局限为单一德语队列且未纳入社会人口学/生活方式协变量；未来可跨语言验证并做联合层级建模。

## 点评
把“测什么分数”和“任务开放度”绑在一起分析，比单一 MCI 准确率更能解释 SSL 与手工特征何时互换优劣。设计上被试不相交 + hold-out 较扎实。MCI 二分类绝对水平仍中等，且 EXE/VIS 靠言语任务跨域预测，泛化边界需明确；“specialist/generalist”是有用归纳，但依赖当前电池构造，不宜过度外推。

