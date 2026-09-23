# ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation

- 论文编号：2384
- 报告人：Khushal Yadav
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yadav26_interspeech.pdf

## 问题
端到端 S2ST 大模型（如 SeamlessM4T）参数与双语数据需求大，Indic 低资源方向易过拟合与长序列幻觉。需要更强结构先验以跨语言共享、在极少数据下稳定翻译。

## 方法
ARTIST（166M）：先用 VQAE 在源/目标发音特征上预训练共享离散发音空间（码本 K=20）；S2A 用 Conformer 编码器 + 中间层 CTC 对齐源发音单元，Convolution-Augmented Differential Transformer 自回归预测目标发音 token；VQAE 解码后经 A2Mel + HiFi-GAN 合成。在 BhashaAnuvad 11 个 Indic→英方向上训练（短句 3–20s），长句 OOD（20–50s）评测。

## 实验与结果
相对 1.2B SM4T，各资源档 BLEU/chrF/COMET 普遍更高（如 Hindi 22.14 vs 13.21 BLEU；Gujarati 仅 10h 达 16.91 BLEU）。消融：去中间 CTC 则 BLEU 崩至 1.07；印地单语相对多语从 22.14 降至 12.95；去掉解码器卷积模块亦降分。JES（BLEU/(小时×十亿参））相对基线提升约 23×–231×。

## 结论
通用发音瓶颈促进跨语言脚手架，参数与数据效率高，并改善长音频稳健性。中间 CTC 与局部卷积对稳定训练与发音连续性至关重要。

## 点评
把“生理发音空间”做成极端压缩的共享目标，比纯声学离散单元更适合 Indic 多语少数据；中间 CTC 消融的灾难性结果说明早期语音内容解耦几乎是硬前提。对比锚定在 SM4T 且评测偏长句，对 cascade/专精 S2ST 的相对位置需读者自行外推；发音特征依赖 IMS Toucan 等前置估计，错误可能沿链路放大。
