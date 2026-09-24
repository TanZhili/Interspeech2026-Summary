# Progressive Learning for Robust Speaker Representation

- 论文编号：2097
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/keetha26_interspeech.pdf

## 问题
说话人嵌入在噪声/混响与跨语条件下易编码语言学内容，导致同语异说话人误纳、跨语同说话人误拒。

## 方法
两阶段：Stage1 用 ArcMargin 在 TidyVoice 上微调 ReDimNet-B6，并加大 MUSAN 噪声、RIR、变速增强；Stage2 冻结骨干，训轻量卷积投影网（约 256K 参）用三元组损失拉近同说话人（含跨语正样本）、推开异说话人（含同语负样本）。曾试 GRL 语言对抗但无效故弃用。

## 实验与结果
开发集总体 EER：基线 3.07% → 无适配 ReDimB6 2.70% → Stage1 1.75% → Stage2 1.58%；最难 SS-DL vs DS-SL 由 4.42% 降至 2.52%。盲测 eval-A 9.06%→4.81%，eval-U（未见语）11.60%→7.01%。噪声与混响扰动下 EER 保持较稳；t-SNE 显示跨语同说话人簇更紧、异说话人更分。

## 结论
域内 ArcMargin 适配 + 跨语平衡三元组投影，可在噪声与语言变化下提升说话人表征鲁棒性，并在未见语盲测上显著优于挑战基线。

## 点评
渐进式“先鲁棒分类、再度量塑形”清晰，平衡四类试验对采样很关键。最易条件下有轻微回退；共享多语的说话人簇仍偏近，口音/跨语音素缠结未完全消解。
