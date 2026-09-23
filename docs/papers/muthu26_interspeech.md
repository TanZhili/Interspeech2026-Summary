# DysfluentNet: Joint Stuttering Event Detection and Dysfluency-Aware Transcription via Hierarchical Self-Supervised Learning

- 论文编号：696
- 报告人：Mohankumar Muthu
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/muthu26_interspeech.pdf

## 问题
口吃检测与转写常拆成独立系统；标准 WER 用流畅参考会惩罚忠实保留不流畅的系统；多任务耦合与困难样本课程策略在口吃场景仍不足。

## 方法
DysfluentNet：冻结 WavLM-Large，学层加权和；检测头用 attentive pooling + 六类多标签 focal loss（BLK/PRO/SR/WR/INT/FLU）；转写头为 BiLSTM + 扩展词汇的 SA-CTC，经 cross-attention gate 用检测 logits 条件化解码，并加对齐一致性项。按 SEP-28k 标注者 Fleiss’ κ 分五档课程，由易到难扩展训练集。联合损失 `L_det + β L*_CTC`。

## 实验与结果
SEP-28k 检测 macro F1 72.4（相对最佳公开基线 LLM-Dys +6.8）；FluencyBank 二分类 F1 81.5。转写 DI-WER 18.3（相对 SSDM 2.0 −4.1），标准 WER 13.8。消融：无课程 −3.3 F1；无 SA-CTC 条件/对齐损害 DI-WER；换 wav2vec 2.0 骨干亦下降。少数类 BLK/SR 提升最大。

## 结论
共享冻结 SSL、检测条件化 SA-CTC 与标注一致性课程，使检测与不流畅感知转写互相增益，并在 SEP-28k/FluencyBank 上刷新报告指标；目前仅英语。

## 点评
把检测当 soft prior 注入 CTC、并用 DI-WER 对齐“保留不流畅”目标，系统设计闭环清楚。脆弱点是对齐窗固定、编码器全冻、评测说话人规模有限，以及课程依赖众包 κ 分层质量。
