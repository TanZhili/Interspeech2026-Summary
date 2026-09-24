# Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming

- 论文编号：296
- 报告人：Joseph Keshet
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/weber26_interspeech.pdf

## 问题
词级强制对齐对语言研究与 ASR/合成管线关键；HMM-GMM（如 MFA）仍强，但需 G2P；希望融合多语 SSL 表征并在未见语言上可迁移。

## 方法
对齐编码器融合 UnSupSeg（无监督音素边界）与 MMS CTC 词边界置信，经 Conformer 等预测帧级边界概率（focal loss）；对齐解码器为可学习动态规划，用边界距离、编码器转移分、区间内边界惩罚、MMS 字母发射和等特征求词结束帧。编码器与解码器分阶段迭代训练。无需音素/G2P。

## 实验与结果
英：TIMIT/Buckeye 上 MWA 全面优于 MFA、MMS、WhisperX、Canary（如 TIMIT ≤10 ms 58.0% vs MFA 41.6%）。未见语：希伯来、荷兰 IFA、德 PHONDAT 上 TIMIT 训练模型更可迁移；≤50 ms 及以上常优于或持平 MFA/MMS（德 ≤50 ms 84.7% vs MFA 82.1%）。

## 结论
融合 MMS 与 UnSupSeg 再加学习 DP，可在英语上超 MFA，并有望扩展到 MMS 支持的 1100+ 语而无需再训练。

## 点评
去掉 G2P、用多语 SSL 做零样本跨语对齐，工程价值高。编码器–解码器非端到端联合优化；荷兰整体偏低、希伯来宽容差下 MMS 仍更强，说明迁移并非处处压过基线。
