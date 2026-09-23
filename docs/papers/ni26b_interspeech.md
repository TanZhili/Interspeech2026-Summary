# DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration

- 论文编号：2291
- 报告人：Gongping Huang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/ni26b_interspeech.pdf

## 问题
Music source restoration（MSR）要在解混的同时逆转压缩、编解码等非线性制作效果。现有系统 FAD 尚可但 MMSNR 普遍偏低，说明语义分布贴近而波形重建不足。作者要把分布拟合与信号重建拆成两阶段。

## 方法
DTT-BSR+：第一阶段用 GAN 式 DTT-BSR 从劣化混合中生成符合干净 stem 先验的估计；第二阶段用去掉 BLSTM 的 Demucs-L，以时间域 L1 + multi-resolution STFT 回归到真值，限制感受野以免改写第一阶段分布。在 MSRBench（3250 条 10 s/48 kHz，8 类 stem）上，第一阶段按既有设定预训练，第二阶段用冻结第一阶段在训练集上的推断结果作输入，Adam 训 150 epoch；训练时 10% 概率用真值替换第一阶段输出，并做随机相位偏移增强。

## 实验与结果
相对单阶段 DTT-BSR，八类 stem 的 MMSNR 均提升，Bass 2.49→9.29 dB、Drums 2.24→8.79、Vocals 3.34→6.72；平均 MMSNR 4.35，优于 X-LANCE-MSR 的 2.28，且在 Vocals/Guitars/Synthesizers/Bass/Drums 五类上更高；八类 Zimtohrli 均为最佳。FAD-CLAP 在部分 stem 随 MMSNR 下降而改善，在 Guitars/Keyboards/Synthesizers/Orchestral 等却上升。消融显示 Demucs-L 作第二阶段整体优于 MSG；Percussions 上单阶段 MSG（2.47 dB）远好于级联（约 0.4 dB），说明第一阶段失真难被第二阶段救回。FAD 分解表明变差主要由语义均值项 Dμ 上升驱动，协方差项变化小。

## 结论
把语义拟合与波形重建分阶段，可系统抬高 MMSNR 与感知指标；但重建精度与语义分布存在 stem 相关权衡，统一架构不足以覆盖全部 stem，尤其 Percussions 需另策。

## 点评
问题诊断（FAD 好、MMSNR 差）直接导出 cascade 设计，比把 MSR 拆成分离/去混响/去噪更贴“目标冲突”。FAD 均值项分析把“听起来像但分布中心漂了”说清楚了。脆弱点在于级联误差传播（Percussions）以及第二阶段可能把生成分布往回归均值拉；后续 stem-aware 或端到端联合训是自然方向。
