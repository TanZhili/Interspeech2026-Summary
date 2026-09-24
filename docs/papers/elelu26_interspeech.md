# ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

- 论文编号：572
- 报告人：Tashfain Ahmed
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/elelu26_interspeech.pdf

## 问题
多数 MOS 预测器只给点估计、无可靠不确定性；人类评分主观且有噪声，部署时难以判断低置信或分布偏移样本。

## 方法
ConformalMOS：冻结上游（M2D2 或 wav2vec）均值池化嵌入 → 两层 MLP 序数头；将 MOS 划为等宽 bin，用高斯平滑软标签训 KL+辅助 L1；再在 10% 校准集上做 split conformal，取残差 (1−α) 分位数为半宽，输出截断到 [1,5] 的区间。

## 实验与结果
BVCC（VoiceMOS 划分）：M2D2 α=0.05 系统级 MSE 0.080、LCC 0.953、SRCC 0.943，优于 FUSE-MOS（MSE 0.086）；句级略弱于 UTMOS。经验覆盖贴近名义水平，校准误差低、区间相对窄；wav2vec 骨干覆盖不足、区间更宽。α 增大则区间变窄、覆盖下降。

## 结论
在交换性假设下可为 MOS 提供有限样本覆盖保证的区间，且不牺牲（甚至提升）系统级点估计；强骨干对校准质量关键。未测跨域，听者分歧建模留作未来工作。

## 点评
把 conformal 接到序数 MOS 头上，比启发式置信更可解释。系统级亮眼、句级仍落后顶尖点估计器；交换性在新 TTS 系统上是否成立是实际部署的硬约束。
