# DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units

- 论文编号：2791
- 报告人：Maxime Poli
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/poli26_interspeech.pdf

## 问题
语言文献需发现音素清单；SSL 离散单元是否在未见、类型多样语言上对应音素仍缺统一评测。既往基准多停在连续表征 ABX，未要求限数据无监督离散化与音素映射。

## 方法
发布 DiscoPhon：6 开发语 + 6 测试语（音系跨度大），每语约 10 h 训/2 h 验测，另有 10 min/1 h 低资源划分；预训练不得见任何基准语（含英语）。两赛道：many-to-one（256 单元→最频音素）与 one-to-one（单元数=音素数+静音，线性指派）。指标 PNMI、PER、R-value、F1，可选 ABX。基线为未接触基准语的 HuBERT/SpidR，预训练于 VP-20 或 MMS-ulab-v2，可零样本或 10 h 继续预训练。

## 实验与结果
Many-to-one：SpidR VP-20 最佳；10 h 微调后测试集平均 PER 61.67、R-value 53.27、PNMI 64.38。HuBERT 更易过分割（R-value 低）。One-to-one 难得多（SpidR 零样本测试 PER≈120）。语言间差异大（如微调后 Basque PER≈41%、Mandarin≈96%）；插入主导错误；替换多发生在相近发音类之间。

## 结论
基准表明当前 SSL 离散单元已含可观音位信息但跨语不均；SpidR 优于 HuBERT；严格一对一映射仍远未解决。资源公开于 cognitive-ml.fr。

## 点评
把“发现音素清单”落成可复现的离散单元评测，对 SSL tokenizer 与濒危语言文档化都有用。金标来自强制对齐，评测映射用了金标统计，严格意义上是诊断“可映射性”而非完全无监督清单发现；one-to-one 极难也点明层次聚类等方向。
