# SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation

- 论文编号：3243
- 报告人：Ye-Eun Ko
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ko26b_interspeech.pdf

## 问题
部署 ASR 面临说话人流式到达、无可回顾历史数据的 rehearsal-free 持续说话人适应；O-LoRA 等任务无关正交分离可抑干扰，但会阻断声学相近说话人之间的正迁移。

## 方法
提出 SCOLoRA：每说话人学新 LoRA 分支并合并进骨干；用 ECAPA-TDNN 嵌入余弦相似度 S_{i,t}，经 sigmoid 先验与轻量 router 映射为有符号系数 λ(S)：相似时 λ<0 鼓励子空间对齐，不相似时 λ>0 强制正交。对 LoRA 基做单位 Frobenius 投影以稳定有符号重叠目标。总损失为 ASR 损失 + Σ λ(S)∥A_i^⊤ A_t∥_F²。

## 实验与结果
Whisper small + LoRA（r=4）于 TEDLIUM2/3 与 CHiME3。TEDLIUM3 上 SCOLoRA 测试平均 WER 4.11%、dev 4.41%、forgetting 0.05，优于 SeqLoRA（4.35/0.10）、O-LoRA（4.33/0.19）及 EWC/L2P/InfLoRA/GainLoRA。跨库一致改进；CHiME3 平均 WER 22.59（SeqLoRA 29.32，O-LoRA 28.09）。消融显示有符号加权与 router 优于仅正向相似度条件，对 τ∈{0.20,0.25} 不敏感。

## 结论
按说话人相似度调节对齐/分离，可在无回放持续说话人适应中同时降低 WER 与遗忘。

## 点评
把 O-LoRA 的硬正交改成相似度调制的有符号正则，切中说话人流“有的该共享、有的该隔离”。依赖说话人编码器质量与合并后单模型容量；长流上存储全部历史 A 基的开销与干扰累积正文未充分展开。
