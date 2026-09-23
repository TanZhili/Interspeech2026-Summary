# SSL-based Sequence Matching for Unsupervised Audio Retrieval

- 论文编号：2369
- 报告人：Moreno La Quatra
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/laquatra26b_interspeech.pdf

## 问题
无标注音频到音频检索需稳健表示与序列匹配；不同域（哼唱 vs 口语示例）对连续对齐与离散词袋式匹配的需求不同，尚缺系统比较。

## 方法
冻结 SSL 帧嵌入（HuBERT/WavLM/w2v2/MERT/voc2vec 等）；可选 K-Means 得聚类嵌入或聚类 ID。匹配：DTW（连续/聚类嵌入）或 TF-IDF/BM25（离散 ID）。在 MIR-QBSH 哼唱检索与自建 QbE-LibriSpeech 短语检索上评 Accuracy/MRR/R@3/R@5；辅以 Soft-DTW 与 Temporal TF-IDF 分析时间敏感性。

## 实验与结果
哼唱：DTW + 原始 SSL 最优，HuBERT-LS Accuracy 0.765、MRR 0.801；文本式匹配明显更差。口语 QbE：TF-IDF on C-IDs 最优，HuBERT-LS Accuracy 0.633、MRR 0.723；DTW 反而弱。均值池化余弦全面落后。结论：音乐依赖音高轨迹轮廓，语音更依赖离散单元分布。

## 结论
作者认为无监督 SSL 检索应域依赖地选择匹配：连续 DTW 利音乐，离散 TF-IDF/BM25 利语音，且无需任务特定训练。

## 点评
贡献在“匹配范式 × 域”的系统对照与机制解释，而非新模型。QbE 集规模较小；K 与层选择影响大，实际部署需再调。
