# Do speech foundation models really learn words?

- 论文编号：2676
- 报告人：Robin Huo
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huo26_interspeech.pdf

## 问题
自监督语音基础模型在探测任务上能区分词身份，但这可能只是因为编码了音素形式（能指），而非独立于局部语音内容的词表征。需要把音系信息剥离后，检验是否仍保留“词”层面的信息。

## 方法
对英文预训练 HuBERT-base 与 wav2vec 2.0 base 的卷积末层及 12 个 Transformer 层，在 LibriSpeech dev-clean 帧级对齐音素/词标签上做线性探测。用 ridge 回归从 one-hot 音素（或左右 diphone、triphone）预测嵌入并残差化，再测词身份分类准确率；先标准化再残差。并在 HuBERT 第 9 层上做无监督词发现（边界检测 + k-means，k=13967），比较残差前后 NED/F1/R。

## 实验与结果
- 残差后音素探测准确率大幅下降（验证有效），但未完全到随机（众数音素约 11.6%）。
- 词探测：原始表示在中后层峰值超约 90%；去掉音素后整体模式仍在；去掉 triphone 后多数层大降，但 HuBERT 9–10 层、wav2vec 7–8 层对长度 3–6 词仍远高于按长度/triphone 众数基线。
- 词发现：去音素残差可改善 NED/F1/R（如相对 Malan et al. 设定 NED 0.508→0.463）；去 diphone/triphone 则损害切分。

## 结论
后期层存在一定程度上独立于局部音系内容的词身份信息；简单残差化可增强词发现中的更高层语言学可及性。局限：需要音素对齐标签；残差未完全抹净线性音素信息；排除单音素词会影响完全去除效果。

## 点评
用线性残差直接拆开“能指 vs 所指”混淆，比单纯余弦相似度更干净。结果说明模型不只是记短 n-gram，但仍不能断定编码了语义/句法；对下游的实用价值受限于对齐标签需求，更适合作为解释与诊断工具。
