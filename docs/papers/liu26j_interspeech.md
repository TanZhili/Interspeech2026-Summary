# Text-Annotated Noisy Speech as Supervision: A Dual-Learning Framework for Target-Domain Clean-Free Speech Enhancement

- 论文编号：1259
- 报告人：Xueliang Zhang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26j_interspeech.pdf

## 问题
深度增强多在合成噪声–干净对上训练，难以泛化到真实场景；目标域往往没有与噪声对齐的干净参考。真实噪声+转写（ASR 语料）更易获得，需要无干净目标的目标域适配方法。

## 方法
提出 SwitchSE：在同一 GCRN 复谱映射骨干上，用可学习 switch embedding 沿时间维拼到噪声复谱前端，指示增强模式或 ASR 模式。每个 batch 只含一种数据类型并只激活对应损失：增强模式用时频 L1（对干净谱与波形）；ASR 模式用冻结 WeNet U2++（GigaSpeech）的 CTC 损失，以转写监督增强结果更利于识别。训练时在 VCTK 干净–噪声 batch 与 CHiME-3 噪声–转写 batch 间随机切换；推理时通过 switch token 偏向感知质量或 ASR 友好输出。

## 实验与结果
VCTK 合成混合（SNR −10~10 dB 训练）预训练；用 CHiME-3 真实噪声约 2.9 h（1600 句）微调。表 1：仅 VCTK 的 GCRN 在 CHiME WER 升至 63.66；仅 ASR 微调保住 WER 但 P.808 MOS 差。SwitchSE 的 \(S_{\mathrm{Enh}}\) 在 CHiME 达 P.808 MOS 3.23，\(S_{\mathrm{ASR}}\) WER 20.27，同时 VCTK 上 PESQ/STOI 仍接近原基线。去掉 \(z_s\) 表现居中；加长 switch 到 4 帧可进一步降 WER（18.09）但略损 MOS。

## 结论
作者认为少量真实噪声–转写数据即可做无干净参考的目标域微调，并在感知增强与 ASR 友好之间可控折中，同时保留源域合成集表现。

## 点评
抓住“真实域有转写、无干净参考”的数据现实，用模式开关避免多任务同 batch 互相拉扯，比单纯 ASR 微调或单纯合成预训练更可操作。边界在于 WER 绑定提供训练信号的同一 U2++，反映的是识别器特定友好性而非通用 ASR；骨干仍为 GCRN，更强增强骨干上的迁移有待验证。
