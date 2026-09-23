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
