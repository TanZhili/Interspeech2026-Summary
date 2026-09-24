# Cross-Modal Consistency-Aware Structured Pruning for Efficient Speech Enhancement with Air- and Bone-Conduction Microphones

- 论文编号：1548
- 报告人：Yeeun Kim
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26n_interspeech.pdf

## 问题
ACM+BCM 多模态 SE 算力大，难上可穿戴；幅度/梯度剪枝与跨模态激活对比对融合关键通道不友好，噪声与模态失配更易误剪。

## 方法
CCAP：对预训练卷积 SE 模型做结构化通道剪枝。分别零掩 ACM 或 BCM，相对多模态响应算归一化灵敏度，平均得重要性后剪低分通道并微调。在 DCCRN、MMINet、LAU-Net 上检 0–80% 剪枝比；TAPS 配对语料 + DNS 噪声（SNR −5–10 dB）。

## 实验与结果
各架构上 PESQ/STOI 优于 PP、TP、BN、MANU；80% 时相对最强基线 PESQ 约 +0.10/+0.20/+0.10。同延迟下质量更高；MMINet 相关层冗余降更多、CKA 漂移更小。MCU 上 LAU-Net 50% 剪枝：Flash/RAM 降约 48%/27%，304 ms 段推理 87 ms（RTF 0.29）。

## 结论
以模态零掩下的响应保持评估通道，可压缩 MMSE 同时保住融合信息，适合嵌入式部署。

## 点评
剪枝准则直接对准“去掉一模态后谁还活着”，比纯权重范数更贴多模态。一次性估计+微调流程实用；是否推广到非卷积融合块与更强非平稳噪声仍待看。
