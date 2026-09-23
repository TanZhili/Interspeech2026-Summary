# Cross-linguistic word-medial stop lenition: A Functional PCA approach

- 论文编号：1786
- 报告人：Seung Suk Lee
- 程序：Tuesday 29 September 2026 / Cross-Linguistic and L2 Phonetic Studies
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lee26p_interspeech.pdf

## 问题
词中塞音弱化（continuity lenition）是否跨语言普遍、是否统一服务于韵律延续与切分？既往研究语言少、方法不一，难以区分真实跨语言差异与操作化差异。作者还关心鼻音 / 浊塞 / 清塞在弱化表现上是否一致。

## 方法
从 GlobalPhone（7 语）、LibriSpeech 英语子集、Seoul Corpus 韩语共 9 种语言力对齐语料中抽取约 147 万个 /VCV/ 词首/词中鼻音与口腔塞音。对强度轮廓做 Functional PCA，以 PC1 刻画强度“凹陷”大小与陡度，并建每语言的贝叶斯混合线性模型分别预测标准化 PC1 与 log 时长，检验词位效应及与塞音类型的交互；部分语言补充词重音协变量。

## 实验与结果
PC1 解释约 40.3% 强度变异，并能按鼻音 < 浊/lenis < 清/fortis 区分类型。大多数情况下词中塞音在时长、PC1 或二者上更弱；浊（或韩语 lenis）塞音在几乎所有语言中既更短又更弱化。例外包括：西班牙语鼻音无显著差异；韩语 aspirated 与瑞典语清塞词中反而更少弱化等，作者归因于音系或词典/语料伪迹。纳入重音会改变词位效应大小，但多数不消失。

## 结论
作者认为词中弱化近乎普遍，支持 continuity lenition 作为跨语言韵律切分线索；浊塞最一致，语言在“弱化主要体现在时长还是强度”上存在差异，听者需学习母语线索模式。未来拟扩展更多语言。

## 点评
统一用 FPCA 量化强度轮廓，避免了以往依赖极值、丢弃高度弱化 token 的问题，适合大规模跨语言比较。论证上把例外归因于音系与语料词典问题较有说服力，但“词”仅近似韵律域、强制对齐对高度弱化音段可能偏差，且韩语为唯一自发口语语料，风格与语言特异性仍纠缠。
