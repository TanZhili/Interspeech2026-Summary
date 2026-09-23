# To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection

- 论文编号：790
- 报告人：Mark Gales
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/loweimi26_interspeech.pdf

## 问题
真实广播档案中目标可能仅闻其声、仅见其人或二者皆有；对缺失模态固定融合会注入噪声，使精度低于最佳单模态。

## 方法
在 MVSE（ECAPA-TDNN 说话人 + ResNet 人脸，零样本）上加查询自适应：用各模态 top-n 检索的组内分数与跨模态分数（一方检索集上另一方的分数）刻画模态一致性；分类器判 AoP/VoP/AVP 并设融合权重 \(\lambda\in\{1,0,0.5\}\)。语料 BBC Rewind（>12,000 视频）。

## 实验与结果
模态检测准确率约 89%。检索 P@1：自适应 94.2%，优于说话人-only 82.9%、人脸-only 93.4%、固定融合 90.0%；相对 oracle（96.6%）收回约 64% 的固定融合差距。固定融合在 VoP/AoP 上明显伤 P@1。

## 结论
作者认为先检测活跃模态再融合，比盲目多模态更好，避免缺失模态噪声。

## 点评
问题设定贴近真实档案，跨模态一致性作诊断信号直觉清晰。人脸单模态已很强，自适应主要补“该不该融”的决策；检测错误仍会落到次优 \(\lambda\)。
