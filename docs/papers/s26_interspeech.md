# Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms

- 论文编号：3047
- 报告人：Seshan S
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/s26_interspeech.pdf

## 问题
性别差距常被归因于训练数据失衡，并通过在性别可控子集上微调预训练 ASR 来检验；但预训练语料性别分布未知，微调能否真正暴露「组成→差距」关系存疑。

## 方法
三数据集（LibriSpeech clean、Indic TIMIT、Common Voice v3）× 11 种男:女比例（0–100%，步长 10%）× 四系统：微调 Wav2Vec2、SPRING Wav2Vec2、Whisper Medium，以及从零训 Kaldi TDNN-HMM（LF-MMI）；每配置训练时长上限 71.36h，固定测试集与外部 trigram LM。共 132 条件。用 Demographic Disparity Score DDS=100×(WER_f−WER_m)/WER_m。另在 LibriSpeech 极端比例训 Zipformer 验证。

## 实验与结果
Kaldi：DDS 随组成强且可预测（Indic TIMIT 从 +43.1 到 −37.2）；Zipformer 极端比例亦反转（−9.3→+39.4）。三预训练系统 DDS 波动小且无一致方向（多在约 ±12 内），50:50 近零不等于对组成敏感。微调性别配比无法消除如 LibriSpeech 上 Whisper 持续的女性劣势。

## 结论
组成效应在从零训练中真实存在；预训练表征掩盖了微调阶段的组成信号。仅平衡微调数据不足以缓解预训练 ASR 的性别差距，需表征级干预。

## 点评
用从零系统当阳性对照，方法上干净地拆开「效应是否存在」与「微调能否测到」。对依赖微调性别配比做公平性结论的工作是直接证伪；范围仍限英语与二元性别标注。
