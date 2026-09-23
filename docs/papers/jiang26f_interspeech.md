# Earnings25: A Comprehensive 500-Hour Speech Benchmark for Finance

- 论文编号：2642
- 报告人：Anshul Wadhawan
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26f_interspeech.pdf

## 问题
财报电话会议含行话、数字、口音、重叠与角色切换，通用 ASR 易域偏移；现有金融语音资源或偏训练规模、或缺行业均衡与说话人角色等元数据，难做可复现细粒度评测。

## 方法
Earnings25：testset-full 498 小时 S&P 500 英语完整电话（2025 Q4）；testset-segmented 46 小时、290 段（每行业一段，5–10 分钟，自 2025 全年美股池分层抽样）。CTC 强制对齐、过滤操作员套话，提供转写与行业/说话人等元数据。基线 Whisper base/medium/large-v2 与 Parakeet-TDT-0.6B-v2，报告多种归一化 WER。

## 实验与结果
testset-full 上 Parakeet WER 0.108、WER-N-nc-np 0.061；Whisper-large-v2 约 0.140/0.080。segmented 集类似。行业级显示 Biotech/Pharma 等更高错误。支持说话人角色与行业感知分析。

## 结论
提供近期、元数据丰富、行业均衡的金融 ASR 评测基准，补全长格式与分段两种协议。

## 点评
相对 Earnings-21/22，强调行业分层与角色元数据，评测更“能诊断”。体量接近“~500h 全量测试”对计算要求高；segmented 子集更适合常规迭代。无外部 LM 的基线设定清晰可复现。
