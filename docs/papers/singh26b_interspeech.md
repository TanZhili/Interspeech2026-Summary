# CHUCKLE - When Humans Teach AI to Learn Emotions the Easy Way

- 论文编号：1591
- 报告人：Ankush Pratap Singh
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/singh26b_interspeech.pdf

## 问题

语音情感识别（SER）标签主观、噪声大，课程学习（CL）从易到难训练有吸引力，但既有难度定义多为启发式、数据驱动或模型驱动，较少对齐人类感知难度。作者认为：对主观任务，众包标注中的一致性与“意图—感知”对齐，才是更自然的难度信号。

## 方法

提出 CHUCKLE：在 CREMA-D（7442 片段、91 演员、6 情感；每段有意图标签与 8–12 名评分者感知标签）上，用两类课程构造难度排序。分数式：意图情感得票比例、标注分布熵，再按四分位分成 Easy / Borderline Easy / Borderline Tough / Tough。规则式：把样本划为 Clear Match、Clear Mismatch、Ambiguous Match、Ambiguous Mismatch，再给出三种由易到难排序（Agreement 1/2/3），分别强调一致性强度、与意图对齐、或二者折中。训练按 bin 递增加入样本；输入为未微调的 HuBERT-Xlarge 帧级表征，分类器为 2 层 BiLSTM 或 2 层 Transformer；对比非课程、随机课程与各类感知课程；评测含 subject-dependent 与 subject-independent，指标为 mean macro accuracy。

## 实验与结果

规则式 Intended-Perceived Agreement 1 在多数设定最优且常达显著：subject-dependent 上 LSTM 0.6623、Transformer 0.6827；subject-independent 上 LSTM 0.6669、Transformer 0.6857。相对非课程基线，规则课程相对准确率提升约 LSTM 0.7%–1.8%、Transformer 0.8%–3.0%；Agreement 1 约少 17% gradient updates，Agreement 2 可少近 40% updates 且准确率仍可比。随机课程往往不升反降。

## 结论

众包中的标注一致性与意图—感知对齐可作为 SER 课程的有效难度信号；规则式课程在准确率与效率上优于非课程与分数式课程，且在跨说话人设定仍有收益。方法在样本排序层工作，模型无关，前提是同时有意图与感知标签；未来拟扩展到多模态与更多数据集。

## 点评

做法抓住的是 SER 特有的“双标签”结构：不仅看 annotator 分歧，还显式建模与演员意图的匹配/错配，尤其把“一致但错配”当作最误导信号之一，比单纯熵排序更贴近主观任务的噪声机制。强项是同时报告准确率与梯度更新成本。脆弱点是依赖 CREMA-D 式 acted 数据与意图标签，真实自发语料往往没有“intended emotion”；绝对增益不大，且难度假设“对人难则对网难”未必处处成立。
