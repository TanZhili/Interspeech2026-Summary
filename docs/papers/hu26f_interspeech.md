# ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids

- 论文编号：1660
- 报告人：De Hu
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/hu26f_interspeech.pdf

## 问题
开放式助听器存在外噪声经通气孔漏入耳道，损害双耳增强；传统主动 BSE+ANC 常需耳道深部误差麦，佩戴不适且难部署。

## 方法
提出 ABSE-NET：BMVDR 粗增强后，将左右参考麦与 BMVDR 输出的实虚部拼入轻量网络；编码器–特征增强（重复 L 次 F-TDL：频率/时间依赖学习，含 RMB-Conv1D 与因果 C-RMB-Conv1D）–ConvAtt（通道与频–时注意）–解码器，输出经次级路径抵消泄漏并补偿波束形成失真。损失为 −SI-SDR − λ·STOI。训练可用误差麦建模，推理部署无需耳内误差麦。

## 实验与结果
Librispeech+NOISEX-92，HRIR 来自 Hearpiece。ABSE-NET 约 0.112M 参数、0.184G FLOPs；SI-SDR 9.869 dB、PESQ 3.626、STOI 0.955，PESQ/STOI/CSIG/COVL 优于 ASE-TM 等，参数与算力远小于 DeepANC/ASE-TM；空间线索 ΔILD/ΔIPD 保持较好。相对无泄漏处理的 BMVDR 与带泄漏 BMVDR 均有明显听感与客观提升。

## 结论
模型驱动粗增强 + 轻量神经后处理可在无耳内误差麦部署下联合做开放式助听器主动双耳增强。

## 点评
把泄漏消除与失真补偿并入同一后滤波映射，避开实时耳内反馈回路，贴近可穿戴约束。F-TDL 用重参数多分支卷积换注意力，利于助听器算力。性能依赖次级路径与泄漏建模假设，真实个体耳道差异仍需现场校准验证。
