# QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement

- 论文编号：889
- 报告人：Shogo Yamauchi
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yamauchi26_interspeech.pdf

## 问题
轻量语音增强压缩参数时常损害相位建模，引入听感伪迹；需在少参数下联合保持幅度与相位。

## 方法
提出 QC-GAN：用 Hamilton 积实现四元数 FC/卷积/多头自注意，将 Conformer 式编解码改写为 Quaternion Conformer；输入为 Δlog|Y|、log|Y|、归一化相位 cos/sin 组成的四元数特征。编码器用 QG-Dilated DenseNet，瓶颈为两阶段时–频 Q-Conformer，解码双分支估计幅度 mask 与复残差；MetricGAN 判别器逼近 PESQ。损失含 RI/Mag/Time/可微 PESQ/GAN。

## 实验与结果
VoiceBank+DEMAND：Base（0.89M）PESQ 3.48，接近更大 SoTA 且参数不到一半；Tiny（35K）PESQ 3.23，优于多数同等极紧凑模型。DNS-Challenge 3 盲测用 DNSMOS/P.808 验证泛化。消融显示四元数相对全实数替换相位误差更低。

## 结论
四元数结构归纳偏置以约 1/4 参数耦合幅度–相位，结合 MetricGAN 可在紧凑模型上达到高保真增强。

## 点评
把 SE 的相位难题对准 Hamilton 积的分量耦合，比单纯通道缩减更有理论抓手。MetricGAN+可微 PESQ 强推听感分数，需防指标过拟合；Tiny 变体展示可扩展性，但极低容量下复杂噪声场景仍可能受限。
