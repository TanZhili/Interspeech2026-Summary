# Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval

- 论文编号：907
- 报告人：Pranshu Nema
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nema26_interspeech.pdf

## 问题
端到端 ASR 对专有名词/长尾词常产出音近但词错的替换，伤下游实体理解；微调代价高，单信号后编辑又弱。

## 方法
后处理专名 grounding：GLiNER 抽实体；对预定义词表做多视图检索——G2P 音素编辑距离、Soundex 粗语音编码、上下文嵌入余弦；min-max 归一化后加权融合排序，不改 ASR 也不用声学特征。在 United-MedSyn 药物名闭集词表上评 Whisper-large-v3 与 Qwen3-ASR-1.7B。

## 实验与结果
原 ASR 实体精确匹配约 38.27%/36.27%。融合（+text-embedding-3-large）Recall@1 达 74.67%/59.82%（相对精确匹配 +36.4/+23.6 pp），R@10 最高 87.36%。单视图中 G2P 略优于 Soundex；语义视图单独较弱但在高 K 互补。近同音与语义近邻仍是残差错误主因。

## 结论
ASR 专名错误具结构化音近性，多粒度语音+语义检索可显著提升实体级 Recall@K，且 ASR 无关。可扩展到其他专名词表；未来拟做自适应权重与解码约束。

## 点评
把「纠错」改成「排序候选供下游/人工」，产品形态更务实。评估条件在 NER 对齐成功样本上，抽取失败被排除，报告的是 grounding 上限而非端到端流水线。
