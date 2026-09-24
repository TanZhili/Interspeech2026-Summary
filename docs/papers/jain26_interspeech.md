# The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders?

- 论文编号：2498
- 报告人：Rishabh Jain
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/jain26_interspeech.pdf

## 问题
VSR 在 LRS3 等基准上已很强，但高准确率未必等于类人视觉语音感知；模型可能依赖训练语言模式而非构音视觉线索。缺公开人类唇读数据时难以对齐比较。

## 方法
在 MaFI 词级唇读集上对比 Auto-AVSR（S/L）、AV-HuBERT、VSP-LLM 与人类基线；报告词/字/音素/视素指标；用仅给前若干音素的文本 n-gram 作无视觉基线；分析训练词频 vs 视觉信息量（MaFI informativeness）对错误的解释力；视素混淆与清晰度相关。

## 实验与结果
摘要与方法段：模型整体准确率更高，但成功/失败词与人类不同；文本 n-gram 可媲美人类唇读；词级错误更由训练词频解释而非视觉难度；模型在人类最难视素上增益最大，对视觉清晰度依赖远弱于人类。LRS3 上模型 WER 约 20.3–28.6%（Table 1 报告值）。具体 MaFI 表数值以可读段落定性结论为主。

## 结论
当代 VSR 主要靠语言先验，未能把视觉特征稳固绑定为有意义的词；基准高分不等于类人感知。

## 点评
把「像不像人类唇读」操作化为多粒度对齐与无视觉基线，打中过拟合语言模式的痛点。强在 MaFI 视觉信息量维度；脆弱点在词级孤立评测与连续语音训练设定的鸿沟，以及模型未为词级唇读特训。
