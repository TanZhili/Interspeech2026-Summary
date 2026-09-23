# Content-Aware Dynamic Compression for Efficient Speech Recognition based on Large Language Model

- 论文编号：230
- 报告人：Bingqian Wang
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26_interspeech.pdf

## 问题

LLM-ASR 常用固定步长下采样压缩声学序列，忽略内容动态，易丢信息或冗余，损害准确率–效率权衡。

## 方法

用 Continuous Integrate-and-Fire（CIF）作动态前端：对冻结编码器输出预测 firing 权重，累加触发声学嵌入，训练时用 MAE 使权重和逼近转写 token 数；推理无文本时仍生成与内容匹配的变长序列，再经适配器送入 LLM。对比 Conv-MLP / Concat-MLP 固定 DS=2/4/6。

## 实验与结果

AISHELL-1（FireRed 编码器）：Dyn-MLP CER 2.67–3.53，ASEL 27，相对 WEST 固定基线相对降错约 15–33%，长度约减 61%。StepAudio2 设定下相对相近 ASEL 固定基线可相对降错约 12–26%，ASEL 常减约 60%。GigaSpeech Stage2 CER 11.20（ASEL 39）。TTFT 在较长句上降约 7–19%。回归损失 MAE/MSE/SMAE 影响很小。

## 结论

作者认为内容引导的 CIF 动态压缩可在更短 LLM 输入下保持或提升识别，改善准确率–效率权衡，并在大规模数据上可扩展。

## 点评

把“该留多少帧”绑到文本长度，比盲目加大固定下采样比更合理。推理无真值长度依赖学到的速率先验，极快/极慢语速可能偏。编码器冻结利于稳定，也限制与映射器联合再优化声学表示。
