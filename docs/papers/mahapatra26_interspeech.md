# ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks

- 论文编号：831
- 报告人：Aurosweta Mahapatra
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/mahapatra26_interspeech.pdf

## 问题

深度伪造检测在标准基准上表现好，但对富情感/表达性合成攻击常失效。许多系统在假样本占优数据上只做分类微调，易学数据集特有伪影，而非自然语音的可迁移结构。人类更像先内化真实韵律变异，再把伪造当偏离。作者希望把说话人条件韵律结构显式写入 SSL 表征。

## 方法

ProSDD 两阶段。(I) 仅真实语音（LibriSpeech clean）：对 XLS-R 做监督掩码预测，目标为 ECAPA 说话人嵌入拼接帧级韵律（F0、voice activity、energy，256 维），用 InfoNCE 区分正样本与同说话人不同韵律 / 不同说话人同韵律负样本。(II) 在 ASVspoof 2019 或 2024 上联合加权 CE 分类与同一掩码预测辅助损失；每步 masked/unmasked 双前向；分类头仅线性+Dropout+ReLU，避免复杂池化抢功。推理只用骨干与分类头。

## 实验与结果

2019 训练：ProSDD 在 ASV19/21/24 EER 为 0.42/3.87/16.14，EmoFake 3.70、EmoSpoof 9.54，相对 XLSR-SLS 的 25.43/8.84/18.92 等明显改善（摘要称情感集约 50% 相对降幅）。2024 训练：ASV24 从 39.62% 降至 7.38%，EmoSpoof 11.96、EmoFake 25.06，并优于 RawNet2/AASIST。消融去掉掩码预测与 Stage I 全面变差；仅 Stage II 保留掩码仍不如完整两阶段稳定。

## 结论

先从真实语音学习说话人条件韵律结构，再以辅助任务保持该结构做伪造判别，可在保持传统基准竞争力的同时显著提升对情感/表达性攻击的泛化。代码与资源已公开。

## 点评

训练哲学从“盯假样本伪影”转向“先建模真语音韵律规范再找偏离”，与人类直觉和表达性 TTS 弱点对齐。轻量分类头有助于把增益归因到表征而非架构。脆弱点是韵律目标依赖外部编码器质量、Stage I 仅英语朗读、跨攻击（TTS 训 / VC 测）上 EmoFake 仍偏高，且双阶段训练成本更高。
