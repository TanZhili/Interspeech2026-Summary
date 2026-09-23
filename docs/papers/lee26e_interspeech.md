# RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

- 论文编号：646
- 报告人：Yongjoon Lee
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26e_interspeech.pdf

## 问题
GAN 声码器架构进步快，但训练目标常不足以学到可泛化表示；提升泛化往往牺牲单步效率（如扩散/大模型）。需在保持 GAN 效率下同时抬升见域保真与未见域泛化。

## 方法
RAF：用 WavLM/HuBERT 等 SSL 嵌入与频域度量定义 real–fake 的 quality gap；判别器用相对论配对（RpGAN 式）估计 discriminator gap，对抗目标使两者对齐，生成器最小化判别器差距。应用于 BigVGAN-base、HiFi-GAN、Vocos 等，对照 LSGAN/SAN/WaveFM 等。

## 实验与结果
多数据集上客观与主观一致提升；摘要称 RAF 训练的 BigVGAN-base 在感知质量上可超过 LSGAN 训练的更大 BigVGAN，且参数仅约 12%。跨源域与未见集泛化增强。

## 结论
作者认为 SSL 辅助的相对论配对对抗反馈是提升通用 GAN 声码器的有效训练框架。

## 点评
改损失不改推理图，部署友好。SSL 选择（WavLM 末卷积层、HuBERT 第 22 层）有感知/音素依据。与 MetricGAN 系需区分：RAF 强调配对相对反馈而非直接回归可微指标。未见域增益取决于 SSL 覆盖面。
