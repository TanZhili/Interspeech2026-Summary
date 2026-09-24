# WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations

- 论文编号：102
- 报告人：Hui Wang
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26_interspeech.pdf

## 问题
中文老年语音多在受控环境采集，话题/自发度/信道多样性不足；野外自动管线对老年声又易出错，缺带细粒度人工标注的真实场景语料。

## 方法
WildElder：从在线视频（关键词检索 + 老年创作者频道）收集，人工切分、转写与元数据标注（年龄段、性别、口音强度轻/中/重）。质检要求抽检准确率 ≥95% 等。最终 23,701 句、33.7 小时（619 视频）；说话人级划分训/开/测 18,835/2,465/2,400 句。基线含从零 Transformer/Conformer/Branchformer/Paraformer，以及 CW（WenetSpeech）与 Whisper Tiny–Medium 零样本/微调。

## 实验与结果
从零最优约 Conformer attention rescoring CER 31.74%。CW 零样本/微调 16.43%/13.54%；Whisper-Medium 23.41%/16.14%。微调后女/男 CER 约 10.44%/16.89%；随年龄上升，85+ 明显变差（90–95 约 24.41%）。

## 结论
野外老年普通话仍难；预训练+领域微调必要。数据集可作为 ASR 与说话人画像等任务的挑战基准。

## 点评
「野外来源 + 人工细标」补上现有中文老年库的空白。人口学分解（性别/高龄）把难点落到可行动的采集与适配方向，而不只是报一个总 CER。
