# Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR

- 论文编号：2124
- 报告人：Yi Wu
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26k_interspeech.pdf

## 问题
自注意力 O(T²) 限制长序列 ASR；粗时间下采样伤边界精度。语音帧高度冗余，K/V 作上下文不必与 Q 同分辨率，固定步长池化又忽略层间冗余差异与相对位置错位。

## 方法
KV-Pooling Attention：对 K/V 平均池化（步长 s），Q 保持原分辨率，复杂度 O(T²/s)；中心对齐相对位置编码；因果掩码按池化窗右边界、padding 需窗内全有效。分析 Zipformer 层间帧相似与熵，浅层大步长、深层小步长，集成 KV-Pooling-Zipformer（步长配置如 4,2,1,2）。Pruned RNN-T，AISHELL-1 与 LibriSpeech。

## 实验与结果
AISHELL-1：L/M/S 测集 CER 分别 6.58→6.35、6.57→6.35、8.10→7.87；摘要称绝对约 -0.2% CER。LibriSpeech：L 上 clean/other 3.33/8.32→3.30/8.09；摘要称约 -0.3% WER。EPYC 7763 上推理 RTF 约改善 10%。注意力图更集中于对角。

## 结论
非对称分辨率注意可利用时间冗余加速并略提准确率；层差分步长与位置/掩码适配是落地关键。

## 点评
把“语音帧冗余”直接写进 K/V 池化，比整体下采样更保边界。层自适应步长有分析依据；增益幅度不大，小模型在 clean 上偶有回退，平滑可能抹掉细微音素细节。
