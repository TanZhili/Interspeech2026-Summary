# Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset

- 论文编号：190
- 报告人：Yu Ji
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ji26_interspeech.pdf

## 问题
音乐源分离缺大规模细粒度乐器标注；网络爬取易有标签噪声与混音，人工建库成本高，常见 4-stem 粒度不足。

## 方法
定义 7 类固定 stem（Piano/Drums/Bass/Acoustic Guitar/Electric Guitar/Strings/Wind-Brass）；冻结 Dasheng 编码器上训练每类单源二分类器（3 s/16 kHz）；多语关键词爬 YouTube 得 ACMID-Uncleaned；分段检测后从 48 kHz 原音频拼接纯净段得 ACMID-Cleaned。开放爬虫与检测权重。

## 实验与结果
检测器七类平均准确率 97.14%（Dasheng 优于 Music2Latent/CNN）。用清洗数据训分离模型：相对未清洗平均 SDR 提升明显（Cleaned 平均 4.63 vs Uncleaned 2.24 dB）；与 MoisesDB+MedleyDB 合并后平均 SDR 6.05，相对原基线约 +1.16 dB。清洗后时长大幅收缩（如 Wind-Brass 2259.72→102.64 h）。

## 结论
自动单源检测可有效清洗网络乐器数据并支撑更细粒度 MSS；清洗质量比单纯堆未清洗小时数更关键。

## 点评
把“solo 爬取 + 纯度分类”做成可复现流水线，直接打标签噪声。强在检测准确率与下游 SDR 闭环；弱在依赖 YouTube 许可与版权、不含人声、阈值权衡会牺牲规模。
