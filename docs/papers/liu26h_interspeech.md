# Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA

- 论文编号：1183
- 报告人：Jie Liu
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/liu26h_interspeech.pdf

## 问题
低资源多语 ASR 联合训练中，共享 LoRA 子空间易负迁移；一致性/自训练在预测不可靠时会放大确认偏置与跨视图不稳。

## 方法
冻结 Whisper-small，用 SPF-LoRA：共享分支学跨语共性、每语私有分支建模特异分布，可学习门控 β_ℓ 融合。训练上用 MT-CR：仅对可训适配器做 EMA 教师；双增强视图上学生 CE + 教师置信度门控（c_t>τ）的 KL 一致性；两阶段先监督训 SPF，再升温 λ、收紧 τ。

## 实验与结果
Kathbath 五语（gu/hi/mr/pa/ur）。SPF-LoRA 宏平均 WER 23.93%，加 MT-CR 至 19.85%，优于 small+LoRA（30.73%）与 medium+LoRA（22.46%）；Gujarati 38.86%→25.04%。消融：可学习融合优于纯共享/纯私有/固定求和；置信度门控是 MT-CR 关键；注入范围扩至 qkvofc 最佳。相对 LoRA 五语 CER 均下降。

## 结论
共享–私有 Fusion-LoRA 加置信度门控 Mean-Teacher，可在冻结骨干的参数高效设定下缓解负迁移并提升低资源多语 ASR。

## 点评
把“容量竞争”拆到私有 LoRA、用门控过滤不可靠一致性，针对性强。实验限于印欧系五语与 Whisper-small；最差语仍明显更高，门控阈值与增强强度需调，跨语系泛化未验证。
