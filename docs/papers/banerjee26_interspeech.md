# wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval

- 论文编号：141
- 报告人：Adhiraj Banerjee
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/banerjee26_interspeech.pdf

## 问题
QbE-STD 需要可变长话语间保持相似的离散语音表示；wav2tok 用 CTC 显式对齐但聚类与对比–对齐紧耦合，难扩展；BEST-STD 可扩展但对齐仅隐式依赖 DTW 正样本采样。

## 方法
wav2tok 2.0 以 BEST-STD 为骨干（谱前端 + 双向 Mamba，约 4.7M 参数，VQ 码本）。两阶段训练：Stage I 用 SimCLR 式对比损失 + commitment，经 DTW 构造帧级锚–正对；Stage II 加入无 blank 的 CTC 成对对齐（对去重 token 序列做前向后向），并提出 DTW 对齐的帧级 token 预测损失 Lpair；λCTC 自适应缩放为对比损失量级的约一半，避免 CTC 主导或数值不稳。检索沿用 BEST-STD：1s 段、bigram 倒排索引 + Jaccard 精排。

## 实验与结果
LibriSpeech train-clean-360 训练，在 train-clean-100 检索，并测未见 TIMIT。离散一致性（Table 1）：码本 256 时 unigram/bigram Jaccard 达 0.83/0.75，优于 BEST-STD 与 wav2tok。QbE-STD（Table 2）：512 码本 LibriSpeech IV MAP/MRR 0.86/0.90，OOV 0.82/0.84；TIMIT 上仍领先；相对仅 CTC 的 wav2tok，帧级预测进一步抬高 MAP/MRR 与 MTWV。

## 结论
在可扩展骨干上把显式成对对齐做成一等训练信号，可同时提升 token 稳定（尤其 bigram）与检索指标，且不牺牲效率。未来可并入 OT 码本均衡，并扩展到多语/噪声/长音频与语音 LLM。

## 点评
分段训练把“先聚好再对齐”说清楚，自适应 λCTC 是可扩展配方的关键工程点。增益主要来自检索向目标而非通用 SSL 表征；大码本上 MAP/MRR 与 MTWV 的折中仍在，说明对齐不能消去词汇量–鲁棒性张力。
