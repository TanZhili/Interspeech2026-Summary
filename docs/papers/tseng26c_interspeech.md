# VOSSA: Voiceprint Optimization for Streaming Speech Architectures

- 论文编号：2763
- 报告人：Mu-Ruei Tseng
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26c_interspeech.pdf

## 问题
流式 VC 常用冻结 ASV 嵌入，其设计刻意压制说话人内音素/韵律变化，与帧级声学生成冲突；另训说话人编码器又增复杂度。

## 方法
VOSSA 以 TVTSyn 为骨干：从冻结内容编码器的 CNN 末层与每隔一层 MHSA 特征拼接，经 ASP+MLP 得全局说话人嵌入，与 VC 目标联合训练，去掉外部说话人编码器。双路径训练：LibriTTS 自重建 + VoxCeleb 非平行转换。六数据集评测，并做 F0、F1 共振峰诊断与听感测试。

## 实验与结果
NISQA-MOS、WER 与 TVTSyn 相当；归一化目标相似度显著更高；HNR 接近 TVTSyn 且优于多数基线。自重建上 F0 MAE/PCC 与元音 F1 的 Wasserstein 距离最优。听感：相对 TVTSyn，说话人相似 46→54、可懂度 44→56、活力 48→52（百分比偏好）。

## 结论
中间层内容表征足以支撑说话人条件，可在保持流式延迟的同时改善音高动态与元音区分线索。

## 点评
把“说话人嵌入从哪来”从 ASV 惯性改到内容编码器中层，对准生成所需的音素条件可变性。声学诊断（F1/F0）比只报 SIM 更能说明表征差异。
