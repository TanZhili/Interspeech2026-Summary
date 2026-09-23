# USV-DETR: High-Resolution and Densely Supervised Detection of Ultrasonic Vocalizations

- 论文编号：1492
- 报告人：Yilan Wei
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wei26d_interspeech.pdf

## 问题
啮齿动物超声发声（USV）在频谱图上尺度小、窄带、稀疏，规则阈值或常规 CNN/检测器难保细节与稳定监督。

## 方法
USV-DETR 基于 RT-DETR：引入高分辨率 P2 特征层表征窄带短时信号；采用 DEIM 训练框架（密集 O2O 匹配增强 + 对低质量匹配的自适应加权监督）稳定稀疏小目标学习。损失含 MAL、L1、GIoU、Focal、分布精炼等。数据：SqueakOut（小鼠，12954 图）与自建 USVpic（大鼠，3000 图），7:2:1 划分；指标 AP、AP50、AP75、APs。

## 实验与结果
摘要称跨数据集一致取得最佳检测，时频定位更准。全文较短，细表数字在抽取中覆盖有限。

## 结论
作者认为高分辨率特征与密集监督使端到端检测器更适 USV 小目标，可作为神经行为声学分析工具。

## 点评
把通用小目标检测进展迁到生物声学，P2+DEIM 针对“又小又稀”很贴切。两数据集均为频谱图目标检测设定，对连续长录音流式部署与种系泛化仍需工程化验证。
