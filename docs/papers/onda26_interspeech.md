# Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference

- 论文编号：1668
- 报告人：Kentaro Onda
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/onda26_interspeech.pdf

## 问题
SSL 离散 token 压缩好、训练省，但硬量化丢信息，下游相对连续特征常变差；HuBERT-Soft 等虽软化表示却失去离散压缩优势且需额外微调 SSL。

## 方法
训练下游模型时仍用 k-means 硬离散；推理时按特征到各质心距离做 softmax 后验，对 token 嵌入做期望加权求和再送入下游。温度 `τ` 可按任务调、无需重训。可与多层码本加权叠加。

## 实验与结果
HuBERT/WavLM large 第 21 层，`K∈{128,1024,4096}`。ASR（LibriSpeech-100h 训）：hard/soft 全面优于 hard/hard；ERJ 非母语上甚至可超过连续特征（如 WavLM K=4096：38.8 vs cont. 38.9）。合成（LJSpeech HiFi-GAN）：重建与 TIMIT→LJ 的 VC 多数指标改善，SpkSim 仍保持离散去说话人优势。嵌入分析显示音素类内方差下降、可分性比（inter/intra）上升。`τ` 过小近硬分配、过大近均匀，均损害 WER。

## 结论
仅在推理做软分配，可在保留训练压缩的同时提升 ASR/合成，并改善跨域与音素可分性。

## 点评
改动极轻但抓住“训练压缩 vs 推理信息量”的不对称；对域外与非母语尤其有用。脆弱在于最优 `τ` 依赖验证集搜索，训练仍是硬标签，分布偏移大时软后验质量受质心与 SSL 层选择制约。
