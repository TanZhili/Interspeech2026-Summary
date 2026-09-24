# How Language-Independent Are Emotional Attributes? A Study on Training Data Scaling and Cross-Lingual Generalization

- 论文编号：2143
- 报告人：Dániel Halmai
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/halmai26_interspeech.pdf

## 问题
高资源语言（如英语）有大量维度情感标注，低资源语言不清楚需要多少目标语数据才能让跨语适应超过从零训练，以及 arousal/valence/dominance 的语言独立性是否不同。

## 方法
WavLM Large 骨干，在 MSP-Podcast（英语约 104h）与 BIIC-Podcast（台湾华语约 102h）上做回归预测三维度（MSE）。对比 Direct（仅华语 1/2/5/10/20/100h）与 Transfer（先英语再华语子集微调）；冻结卷积、Adam、5 随机种子，报告 Pearson 与 CCC，Mann-Whitney U 检验显著性。

## 实验与结果
测试集：Transfer 在 1–2h 对三维度均显著优于同量 Direct；arousal 上 Transfer-10h Pearson 0.624 可显著超过 Direct-100h 的 0.606；valence 约需 20h 适应才追上 Direct-100h；dominance 上多组 Transfer 即可持平或更好。纯跨语（0h）与同语 100h 差距约 0.05–0.1。

## 结论
作者认为 arousal 相对更跨语可迁移，valence 更依赖目标语数据；任务特异适应是低资源维度 SER 的有效路径。

## 点评
用配对语料与数据缩放曲线直接回答“低资源阈值”，问题清晰、结论可操作。仅英→华单向、dominance 绝对值偏低可能含标注噪声；未做类别情感，结论限于维度属性。
