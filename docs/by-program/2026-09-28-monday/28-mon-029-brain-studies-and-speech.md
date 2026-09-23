# Brain Studies and Speech

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster（Area 1）
- 论文数：10
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场连接神经解码、说话人身份神经表征、认知负荷下的归一化与掩蔽、双语执行功能、屏幕阅读语速能力，以及增强效果的 fMRI 神经评测与 EEG 引导说话人提取。方法光谱从迁移学习、对比对齐、fMRI/MEG/EEG 实验到心理语言学与 IRT 建模。

脑机接口侧强调少数据：MEG 感知预训练可迁移到产出与跨任务；EEG–语音时间对齐用监督对比分类；SAGE 面向试验内注意切换的软门控提取。认知神经侧显示说话人特质并非单一构念，粤语声调归一化在负荷下依赖主动控制，PMBR 或表征构音复杂度。行为与应用侧覆盖掩蔽语言熟悉度、语码转换动机与工作记忆/抑制，以及视障用户语速 IRT；NeuroPAS 则用 fMRI 解码器度量增强是否更接近 Clean 神经模式。

## 技术内容

### 神经–语音对齐与解码

**MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data**（论文 439；Xabier de Zuazo）
在单被试 50 小时倾听数据上预训练 Conformer，再对 18 人各约 5 分钟微调。任务内准确率提升约 1–4%，跨任务可达约 5–6%；产出训练模型可超随机解码被动倾听，提示共享神经过程而非纯运动伪迹。

**SCANS: Supervised Contrastive Temporal Alignment of Neural Responses and Speech Stimuli**（论文 2651；K M Naimul Hassan）
将 EEG 段与同句多个非重叠候选段匹配为分类任务，用膨胀卷积前端与跨模态注意力，交叉熵+对比损失。SParrKULee 上显著提升神经–语音对齐准确率。

**SAGE: Switch-Aware EEG-Guided Soft Gating for Target Speaker Extraction with In-Trial Switching**（论文 864；Xuefei Wang）
生成两路候选语音流，EEG 引导开关感知门控平滑融合，并含延迟补偿与不确定保守策略。报告 SI-SDR 8.67 dB、STOI 88.24%，平均切换延迟降至 2.04 s。

**fMRI Decoding of Speech Conditions Across Brain Regions of Interest for Neural Evaluation of Speech Enhancement**（论文 1947；Ching-Chih Sung）
NeuroPAS-Net 三阶段解码 25 人在 Clean/Noisy/DNN-SE/Classic-SE 下的 fMRI；12 个 ROI 上优于 SVM/CNN，右中央前回峰值准确率 79%。NeuroPAS 与可懂度相关，并将 DNN-SE 排得比 Classic-SE 更接近 Clean。

### 身份、负荷、运动与感知行为

**Is Speaker Identity a Unitary Construct? Neural Evidence for Distinct Trait Processing**（论文 1018；Kaile Zhang）
fMRI 显示性别、年龄、口音共享双侧 STG/STS 核心，但口音激活更强，且各特质招募部分特异皮层，支持“核心+扩展”模型。

**Neural Oscillatory Mechanisms of Speaker Normalization Under Cognitive Load: Evidence from Cantonese Tone Perception**（论文 1940；Kaile Zhang）
行为不受视觉负荷影响，但 EEG 显示无负荷时 alpha 去同步，负荷时顶枕 alpha 持续激活；高负荷诱发前额 delta 抑制，支持主动控制假设。

**Beta Rebound as a Neural Signature for Speech Movement: Preliminary Evidence Using Magnetoencephalography**（论文 2995；Keerthana Stanley）
5 名健康成人说不同构音复杂度短语；最复杂短语 PMBR 强于最简单，双侧可见但语言优势半球更强，提示可作构音复杂度神经指标。

**Effects of listener language experience, masker language, and cognitive load on word monitoring accuracy and response time**（论文 2950；Jessica Chin）
英语掩蔽导致最差正确率与反应时；类型学相似度证据不足。阿英双语者更慢但不更不准，也不被阿拉伯掩蔽额外伤害；数字预载认知负荷未见影响。

### 双语执行功能与可及性语速

**Not all language switching is equal: Language brokering and code-switching are associated with working memory and inhibitory control in young adults**（论文 3404；Sarah M. Wright）
总体切换频率与 EF 无关；词汇动机切换与更新/抑制正相关，频繁语言中介（brokering）与之负相关，关联取决于交际功能。

**Profiling Speech Rate Abilities of Visually Impaired Screen Reader Users by Bayesian Item Response Theory**（论文 3096；Takahiro Miura）
对 11 名日本视障用户在 150–500 WPM 用贝叶斯 IRT 分离题目难度与个体能力。难度随语速上升，能力个体差大（SD 0.91–1.10）；全盲理解更高，视障状态与听力经验独立预测理解。

## 本场要点

- 少样本 MEG 迁移与跨任务解码表明感知/产出共享神经表征。
- 监督对比与开关感知软门控分别推进 EEG–语音对齐与动态注意提取。
- 说话人身份呈“共享核心+特质特异扩展”；负荷下归一化依赖主动抑制干扰。
- PMBR 与 NeuroPAS 分别连接构音复杂度与增强的神经接近度评测。
- 掩蔽语言与双语使用形态对行为/EF 的影响不能简化为“切换频率”。
- 贝叶斯 IRT 为屏幕阅读 TTS 语速能力提供可扩展刻画。

## 覆盖核对

- 439 | MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data
- 2651 | SCANS: Supervised Contrastive Temporal Alignment of Neural Responses and Speech Stimuli
- 1018 | Is Speaker Identity a Unitary Construct? Neural Evidence for Distinct Trait Processing
- 1940 | Neural Oscillatory Mechanisms of Speaker Normalization Under Cognitive Load: Evidence from Cantonese Tone Perception
- 2995 | Beta Rebound as a Neural Signature for Speech Movement: Preliminary Evidence Using Magnetoencephalography
- 2950 | Effects of listener language experience, masker language, and cognitive load on word monitoring accuracy and response time
- 3404 | Not all language switching is equal: Language brokering and code-switching are associated with working memory and inhibitory control in young adults
- 3096 | Profiling Speech Rate Abilities of Visually Impaired Screen Reader Users by Bayesian Item Response Theory
- 1947 | fMRI Decoding of Speech Conditions Across Brain Regions of Interest for Neural Evaluation of Speech Enhancement
- 864 | SAGE: Switch-Aware EEG-Guided Soft Gating for Target Speaker Extraction with In-Trial Switching
