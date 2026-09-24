# VieSpeaker: A Large-Scale Vietnamese Speaker Recognition Dataset Beyond Visual Dependency

- 论文编号：3449
- 报告人：Viet Hoang Pham
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pham26_interspeech.pdf

## 问题
越南语说话人语料规模与声学多样性不足；VoxCeleb 式管线依赖人脸，排除无画面录音且标注成本高，VoxVietnam 等仍受视觉约束。

## 方法
提出不依赖人脸的构建管线：YouTube 多域采集 → Pyannote 说话人日志 → gemini-2.5-pro 据元数据与转写证据映射身份（不确定则 Unknown）→ 名称归一化与 ECAPA 嵌入聚类合并 → IQR 清洗与时长过滤。产出 VieSpeaker：4,715 说话人、365,874 句、约 902 小时；划分 VieSpeaker-T/E/H。

## 实验与结果
WeSpeaker ECAPA-TDNN。从零训练 VieSpeaker-T 在 VoxVietnam 上最强；作预训练再微调 Vietnam-Celeb-T，E/H EER 5.45%/6.74%，优于 VoxCeleb2 预训练（5.79%/6.91%）。本基准上从零训达 2.40%/13.45%，VoxCeleb2→VieSpeaker-T 微调最佳 1.81%/9.83%。

## 结论
作者认为元数据+LLM 推理可规模化越南语说话人标注，VieSpeaker 显著扩大说话人与时长，并提升鲁棒性与跨集泛化；数据在 Hugging Face 开放。

## 点评
绕开视觉模态对播客/电台类数据尤为关键。身份质量依赖 LLM 证据约束与人工抽检；相对 VoxCeleb2 仍偏小，Hard 协议上跨会话难度仍高。
