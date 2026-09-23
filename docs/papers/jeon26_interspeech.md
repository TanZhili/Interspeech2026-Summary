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
