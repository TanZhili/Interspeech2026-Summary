# MSR-HuBERT: Self-supervised Pre-training for Adaptation to Multiple Sampling Rates

- 论文编号：1354
- 报告人：Zikang Huang
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26g_interspeech.pdf

## 问题
HuBERT 等 SSL 固定 320× 下采样对应 16 kHz 的 20 ms 帧移；其他采样率会分辨率错配，重采样又丢高频，分率训练成本高。

## 方法
MSRHuBERT：多采样率自适应下采样 CNN（16/22.05/24/48 kHz 分支，步长使帧移统一为 20 ms）+ 每支路层归一化进共享特征空间；保留 HuBERT 掩码预测与 Transformer、单一共享码本，支持混合率预训练。

## 实验与结果
SUPERB 式 ASR 与全频带重建：相对单率/重采样 HuBERT，MSR 在多率上同时保持较低 WER（如 16 kHz 5.89）与较高重建 STOI（48 kHz 约 85.79），优于“全重采样到 48 kHz 伤 ASR、到 16 kHz 伤重建”的折中。微调不重采样时，错配基线 ASR 可崩至数十 WER，而 MSR 可原生适配。增一支路约 +3% 参数。

## 结论
用率特异下采样对齐时间网格，可在不改 SSL 范式下解决多采样率错配，兼顾低频语义与高频细节。

## 点评
把“分辨率错配”作为显式问题提出并量化，对 SSL 部署很实用。仍是多 CNN 分支而非完全共享前端；极高采样率下的码本聚类标签来源与计算开销需注意。
