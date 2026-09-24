# Bidirectional Retention Network-based Segmentation Model for Speaker Diarization

- 论文编号：1032
- 报告人：Jian You
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/you26b_interspeech.pdf

## 问题
EEND-VC 在短窗上做局部分割再聚类，可处理重叠与任意说话人数，但局部分割后端常见 RNN/注意力/Mamba；需在长上下文复杂度与重叠建模之间找更合适的序列骨干。

## 方法
在 Pyannote/DiariZen 管线内，用 WavLM Base+（可学习层加权）前端 + 双向 Retention Network（BiRetNet）后端替换 BiLSTM。Retention 采用 chunkwise recurrent（块长 100 帧≈2s），γ=1 避免衰减；4 个 BiRetNet 块，powerset 损失（N=4, K=2）。嵌入 ResNet34-LM，VBx 聚类。训练两阶段：冻结 WavLM 再可选联合微调；可按数据集做域适应。

## 实验与结果
复合训练集约 952h。冻结 WavLM、无域适应时，BiRetNet 域内 macro DER 15.8%，优于 LSTM 17.3、Attention 17.9、Mamba 16.2。联合微调 + 域适应（S7）macro 15.0%，AISHELL-4 9.9%、VoxConverse 8.5% 达文中所列 SOTA；DIHARD III 约降 4.5 点。3 块 6.5M 后端仍优于更大 Mamba；chunk=100 整体最优。CPU 上 RTF≈1.5，内存随窗长缓增。

## 结论
BiRetNet 作为 EEND-VC 局部分割后端在多数集合上优于 LSTM/Attention/Mamba；与 WavLM 微调及域适应结合可达强综合表现。代码已公开。

## 点评
控制前端与公平对比后端是亮点；Retention 线性复杂度对长窗友好。增益幅度相对 Mamba 不大，SOTA 声明依赖域适应与 Optuna 调参。NOTSOFAR-1 仍难，说明高密度重叠场景瓶颈未必只在后端选择。
