# KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting

- 论文编号：1586
- 报告人：Wenbin Jiang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26y_interspeech.pdf

## 问题
用户自定义关键词检测需区分目标词与音近干扰词；全序列匹配易被整体相似淹没局部可辨音素差异。

## 方法
KFC-KWS：利用 CTC 尖峰后验选高置信音素关键帧，对齐音频、音素与文本模态；再经交叉注意力与全句表示融合，兼顾局部判别与全局语境。冻结 XLS-R 音频编码 + G2P 音素 + DistilBERT 文本；可训约 2.0M 参数；模态 dropout。

## 实验与结果
LibriPhrase：无增强时平衡 AUC 98.06%（LPH 96.54%，EER 9.13%），优于 HyperSpotter-c 等且参数更少。带模态 dropout：平衡 AUC 98.73%，LPH AUC 97.65%、EER 7.75%，强于增强版 PLCL 等。易集上 EER 略逊部分全序列模型，偏重难集可辨性。

## 结论
CTC 引导关键帧融合能有效提升音近关键词判别，在 LibriPhrase 难集与平衡指标上达到强结果且参数紧凑。

## 点评
抓住“混淆发生在少数音素位置”，用 CTC 峰定位再融合，比纯全局嵌入更对症。参数效率好。易集略牺牲、依赖 CTC 对齐质量；开放域口语噪声下峰检测是否稳仍待验。
