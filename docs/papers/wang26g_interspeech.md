# MS-GNN: Multi-Scale Graph Neural Network for Detecting Local Audio-Visual Forgery Traces

- 论文编号：416
- 报告人：Ju Zhang
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26g_interspeech.pdf

## 问题
音视频伪造常只改短时窗（如替换一句口型/语音）；全局池化多模态特征会冲淡瞬时不一致（如唇同步错位）。需要显式保留局部痕迹并与全局语义交互。

## 方法
MS-GNN 将 AV 流切成窗口构图：自底向上聚合窗口到片段语义，自顶向下回传全局上下文细化局部证据；用窗口级辅助监督 + 视频级主监督训练，再聚合得全局表示。

## 实验与结果
LAV-DF：ACC 98.12%、AUC 99.81%，高于 Referee、DimoDif 等。FakeAVCeleb 与消融亦显示窗口监督与多尺度路径有益；效率表在 A800 上比较。

## 结论
作者认为多尺度图聚合配合窗口级监督更适合捕获局部伪造痕迹，提升 AV deepfake 检测。

## 点评
针对“局部篡改被全局池化淹没”的设计动机清楚，窗口辅助损失是关键。对跨数据集未见操纵的泛化正文数字相对次要；图构建与窗口长度选择可能敏感。
