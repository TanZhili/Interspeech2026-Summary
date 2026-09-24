# Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition

- 论文编号：1040
- 报告人：Izabela Krysińska
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/krysinska26_interspeech.pdf

## 问题
CTC 音素识别早期易陷入 blank 主导的“抑制期”，梯度弱、对齐难学；全程细粒度音素目标加剧该问题。

## 方法
Transitional Objective Learning（TOL）：课程式动态加权多个不同粒度 CTC 目标（粗语音特征类→细音素），权重由重要性分数经 Softmax 随 epoch 转移，总损失为加权和。在英语 TIMIT、波兰 LnNor、法语 Vibravox 等上对比标准 CTC 微调。

## 实验与结果
相对基线 PER 相对降约 9.5–14.3%（TIMIT 0.049→0.044 等），t 检验显著。验证曲线显示更快进入 peaking、更早收敛；梯度范数与方差更低。消融表明层级过渡优于仅正则化效应。

## 结论
由粗到细的目标过渡可缩短 blank 主导期、加速收敛并降低 PER，提升 CTC 音素识别稳定性。

## 点评
针对 CTC 经典 blank 病理做课程化损失调度，实现简单、跨语种证据一致。粗类如何定义、权重日程是否需按语种重调，文中依赖声学特征层级；与中间 CTC 正则等方法的直接对比仍可加强。
