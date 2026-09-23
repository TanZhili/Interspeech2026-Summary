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
