# Dual-Granularity Orthogonal Disentanglement for Generalizable Audio Deepfake Detection

- 论文编号：836
- 报告人：Zhuodong Liu
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/liu26g_interspeech.pdf

## 问题
检测器常学到说话人身份而非合成伪迹（隐式身份泄漏），跨说话人/跨域 EER 暴涨；对抗解缠复杂且训练不稳。

## 方法
共享浅层 CNN 后分内容支（卷积+MHSA→伪迹）与身份支（统计池化→说话人）。双粒度正交：样本级余弦正交 + 批级交叉协方差 Frobenius 惩罚。课程调度逐步加大解缠权重 β(t)；身份损失仅在真实样本上。总参约 2.1M。

## 实验与结果
ASVspoof 2019 LA EER 1.35%、2021 DF 7.88%、In-the-Wild 21.58%；跨数据集迁移相对梯度反转解缠绝对改进约 2.60%。以小模型达到接近更大 SSL 系统的量级表现（文中对比）。

## 结论
无需辅助网络或对抗动力学，双粒度正交 + 课程即可抑制身份泄漏并提升跨域泛化。

## 点评
把身份—伪迹独立性写成可微几何约束，比 GRL 更稳、overhead 更低。身份监督依赖训练说话人标签；ITW 仍 20%+ EER，说明真实域失配未完全消除，正交只是必要非充分。
