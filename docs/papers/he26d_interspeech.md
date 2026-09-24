# Disentangling Acoustic Cues in Alzheimer’s Pathology and Perception: The Roles of Language and Gender

- 论文编号：1149
- 报告人：Liu He
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/he26d_interspeech.pdf

## 问题
AD 语音生物标志与人类听感线索是否对齐，尚少跨语言、跨性别系统审计；全局 XAI 可能掩盖人群特异失败，影响临床公平部署。

## 方法
对 Mandarin（NCMMSC2021）与 Greek（ADReSS-M）看图描述各 30 条（AD/HC 各半）提取 21 维声学特征（时序流畅、韵律、发声、发音）。训练 Random Forest：病理分类（临床 AD）与感知回归（16 名普通话听者的 Perception Weighted Score）。用 SHAP 比较两任务特征重要性，并用 GLMER 验证语言/性别与声学交互；年龄与教育仅作统计协变量，不进预测模型。

## 实验与结果
全数据病理 AUC=0.70、感知 r=0.72；Mandarin 与女性病理模型显著（AUC 0.83/0.79），Greek 与男性病理未超机会（0.60/0.52），但感知模型均显著。病理–感知特征排序总体 Spearman ρ=0.55；Mandarin/女性仍显著对齐（ρ≈0.52–0.54），Greek/男性对齐消失。病理更重 pause/jitter/F1 等，感知更重语速、停顿总长与 F0。GLMER 显示停顿、F0 标准差等驱动 AD 听感，且 F0/F2 等与性别有显著交互。

## 结论
病理与感知线索仅部分对齐，且强依赖语言与性别；人群特异 XAI 审计可暴露“模型对某人口几乎无效”的失败模式，是公平临床语音 AI 的前提。

## 点评
把“XAI 是否对人类利益相关者有效”从模型内正确性推进到跨人群外部效度，问题设置很有临床意义。样本每语种仅 30 句、听者文化同质，作者亦定位为假说生成；Greek/男性病理接近机会时，其 SHAP 解读需谨慎。
