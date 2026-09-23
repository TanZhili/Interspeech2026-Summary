# Enhancing Visual Paralinguistics: Motion-Guided Spatial Denoising for Non-Verbal Interaction Analysis

- 论文编号：868
- 报告人：Junjie Wan
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wan26_interspeech.pdf

## 问题
自然 HCI 中微动作被静态背景“幽灵关键点”淹没；重骨干隐式学时空依赖成本高且易过拟合，固定权重晚期融合又忽略不同微动作对 RGB/姿态依赖不同。

## 方法
双流：ResNet-18 RGB + 姿态热图流。MG-SRM 用一/二阶时间差分作运动先验，对空间/时间分支做仿射调制与门控聚合（零初始化残差）。CLF 为每类学姿态流权重 p_c，融合 S_rgb+(1+tanh(p_c))·S_pose，避免实例级注意力过拟合。在 MA-52 上评测。

## 实验与结果
MG-SRM+CLF：Top-1 67.02%、F1-Mean 0.6993，超复现 PCAN（66.40%）与 MMN（62.71%）。消融：基线 65.88%；+CLF 66.42%；+MG-SRM 66.43%；两者 67.02%。实例级注意力 66.72% 低于 CLF。倒放掉 1.34%；相对 Transformer 编码器变体高 0.98%。增参约 0.072M、+1.8G FLOPs。GradCAM 显示注意力更贴手–头动态。

## 结论
显式运动引导空间去噪加类别自适应融合，以极低开销提升嘈杂场景微动作识别，可作为多模态对话系统的视觉前端。

## 点评
把语音增强里的“减噪/高通”类比迁到姿态热图，对 ghost keypoint 问题切得准；CLF 用类别偏置换稳定也很务实。仅 MA-52 单一基准，与语音通道的联合情感/意图实验未做。
