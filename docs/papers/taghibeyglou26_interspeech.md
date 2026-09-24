# Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction

- 论文编号：844
- 报告人：Behrad TaghiBeyglou
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/taghibeyglou26_interspeech.pdf

## 问题
ALS 相关构音障碍线索分散在多类发声任务与时段；标签少、说话人变异大，单录音/手工特征或端到端深度模型难稳健做严重度与进展预测。

## 方法
SAND：339 人（205 ALS / 134 对照），每人最多 5 元音 + 3 DDK。重采样 16 kHz、铺成 20 s、切成 10×2 s；冻结 SSL（wav2vec 2.0 / HuBERT / data2vec / UniSpeech-SAT）均值池化得 768 维节点；按 cosine 建受试者级 kNN 图，用 GCN / ResGCN / GAT / GraphSAGE / GIN 图分类（均值池化 + MLP）。Task1：5 类构音严重度；Task2：由早期录音预测末次 ALSFRS-R（4 类）。

## 实验与结果
官方验证集最佳 HuBERT+GIN：Task1 mF1 0.73（BACC 0.72），Task2 mF1 0.69；同验证基线约 0.61 / 0.58。10-fold CV 上同配置约 0.67±0.05 / 0.67±0.10。作者提醒与挑战测试榜（服务器）不可直接比。

## 结论
多录音片段在 SSL 嵌入空间用图消息传递可提升受试者级 ALS 评估；HuBERT+GIN 双任务最稳。局限：SSL 多为英语预训练而数据为意大利语等。

## 点评
把“一人多任务多片段”显式建成图，比独立录音更合理。GIN 的 sum 聚合适合稀疏关键线索；跨语 SSL 与验证/测试划分差异使绝对数字需谨慎解读。
