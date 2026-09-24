# Multi-Talker ASR Unaffected by Speaker Change Count

- 论文编号：1582
- 报告人：Naoki Makishima
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/makishima26_interspeech.pdf

## 问题
自回归多人 ASR 用说话人切换 token 串接转写；推理时切换次数超过训练分布会漏说话人、CER/SCCA 崩坏。切段过短又损语义连续性。

## 方法
在 Transformer 解码器自注意力中用说话人切换 token mask 替代纯前瞻 mask：对 `[st]`（及 SOMSRED-SVC 中的时间/说话人 token）置 −∞，禁止其他 query 读到已出现的切换计数；训练时另以概率 r 随机 mask 文本 token，阻断从语境推断话轮数。推理只 mask 切换类 token。应用于「ASR+[st]」与联合 diarization 的 SOMSRED-SVC。

## 实验与结果
CSJ 伪多人混合/拼接；训练最多 2 次切换。3 SC 非重叠：基线 CER 13.5%/SCCA 59.5%，Ours(r=0.6) 5.9%/96.3%，接近含 3 SC 的 oracle。4–5 SC 时基线大量少报切换（CER 22–28%），Ours 多数正确。SOMSRED-SVC 上 r=0.4 时 3 SC CER/SCCA 亦明显改善，TER/EER 几乎不降。

## 结论
屏蔽切换计数语境可使自回归多人 ASR 外推到训练未见的切换次数，而无需为更长话轮重造数据。

## 点评
针对「从历史 `[st]` 计数」这一捷径做结构性封堵，比数据扩容更干净。r 过大伤训练；带时间/说话人 token 时与 oracle 差距仍大，说明被 mask 的结构信号越多越难逼近。
