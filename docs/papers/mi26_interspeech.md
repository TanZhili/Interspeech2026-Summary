# Learning Emotion-discriminative Representations for Zero-Shot Cross-Lingual Speech Emotion Recognition

- 论文编号：1170
- 报告人：Jinyi Mi
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mi26_interspeech.pdf

## 问题
零样本跨语 SER 中，仅源语标注训练时分布失配严重；许多方法仍需目标语无标注语音或语言标签，且多减分布差而未显式对齐情感结构。

## 方法
在源语/非目标情感语音上：预训练特征提取器 + 情感分类；监督对比学习拉近同情感、推远异情感跨语样本；说话人对抗分类（GRL）抑制说话人线索。九组零样本设置（英/中/德/法互为源–目标）。指标 UAR 与 Macro-F1。

## 实验与结果
Proposed 平均 UAR/F1=82.26%/81.96%，相对 Baseline 2 提升约 9.05/9.38 点，最接近 upper bound（91.92/91.41）。去监督对比学习降约 5.40 UAR；去说话人对抗降约 2.15 UAR。表征可视化显示情感簇更跨语对齐。

## 结论
对比对齐情感结构 + 说话人对抗可在仅少量语言标注下提升零样本跨语 SER；两者均有贡献，对比项更关键。

## 点评
把“跨语”问题明确成情感条件表征对齐，消融干净。语种仍偏欧亚主流、任务为表演/实验室情感设定的典型局限；相对需目标语无标注数据的 DANN 类方法，零样本约束更强，实用价值更高。
