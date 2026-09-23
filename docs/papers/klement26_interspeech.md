# Analysing Adversarial Priors for Data-driven Unsupervised Speech Enhancement

- 论文编号：2511
- 报告人：Dominik Klement
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/klement26_interspeech.pdf

## 问题
监督增强依赖成对数据，存在训练–部署域差。无监督 GAN 方法用非成对先验，但单分支模型常因一致性损失过强或干净语音先验过弱出现源泄漏（噪声渗入干净估计）。

## 方法
双分支无监督 GAN：共享 DAC 风格编解码器，两条 RoFormer 分支分别估计干净语音与噪声，再用闭式标量 \(\alpha^*,\beta^*\) 线性合成重构噪声输入。三类判别器（干净、噪声、混合）用 LS-GAN 施加分布先验；生成器损失含一致性（多尺度 Mel + SI-SDR）、对抗/特征匹配、以及防止静音塌陷的能量最大化项。编解码器用预训练 DAC 初始化。

## 实验与结果
VCTK+Demand 上相对 MetricGAN-U、MOS-GAN、unSE、unSE+，双分支 PESQ 2.58、COVL 3.08 最高；单分支变体全面更弱。域内干净先验明显优于域外（OOD 干净先验导致噪声泄漏到干净支路）。对齐的噪声先验可把语音→噪声泄漏从 0.23 降到 0.02、噪声→语音从 0.10 降到 0.03（风噪混合实验），减轻过抑制。CBAK 偏低，说明背景伪影仍可能存在。

## 结论
作者认为先验对齐决定分离行为；显式建模噪声并用易采集的环境噪声先验，可减少交叉泄漏并提升感知质量，优于单分支无监督 GAN。

## 点评
把无监督增强的失败模式明确为“一致性 vs 先验”张力下的源泄漏，用噪声支路作 sink 是清晰机制解释。实践上强调环境噪声易采、可对齐，部署友好。脆弱点在干净先验域外匹配差时仍易泄漏，且 CBAK 提示抑噪与自然度之间仍有残余伪影。
