# Your U-Net Dereverberation Model is Secretly an RIR Encoder

- 论文编号：2707
- 报告人：Sina Khanagha
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khanagha26_interspeech.pdf

## 问题
NCSN++ U-Net 类去混响网络是否在隐式编码 RIR？若是，显式 RIR 条件化能否改善表示与收敛？

## 方法
分析：从去混响 U-Net 注意力特征提嵌入做 t-SNE，与对比学习训的 RIR 编码器（ResNet34 / Conformer）对照。训练：InfoNCE 式对比，使同 RIR 不同语句靠近。应用：将预训练 RIR 嵌入注入 SGMSE+/NCSN++ 各 BigGAN 残差块作条件。数据约 10k 真实 RIR 的 VCTK-Reverb。

## 实验与结果
t-SNE 显示判别/扩散去混响骨干深层特征按 RIR 成簇，形态接近专用 RIR 编码器。显式条件化：SGMSE+ PESQ 2.62→约 2.86–2.89（ResNet/Conformer 嵌入），并加速收敛；DNSMOS 同步改善。RIR 可分性与去混响分数相关。

## 结论
去混响 U-Net“暗中”学 RIR 编码；显式对比 RIR 条件可提升质量与训练效率，作为概念验证。

## 点评
分析性贡献强：把黑盒特征解释成退化算子编码。条件化增益中等但一致；真实未知 RIR 时需先估嵌入，级联误差是下一步。证明“秘密切 RIR”比单纯刷分更有启发。
