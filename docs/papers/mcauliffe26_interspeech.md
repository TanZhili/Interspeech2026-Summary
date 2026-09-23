# Montreal Forced Aligner and the state of speech-to-text alignment in 2026

- 论文编号：2734
- 报告人：Michael McAuliffe
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/mcauliffe26_interspeech.pdf

## 问题
MFA 自 2016 成为最常用强制对齐工具，但十年来功能、数据与神经对齐器生态剧变，尚缺对 MFA 3.0 相对经典与神经对齐器的系统跨语言评测。低资源、方言、儿童/L2 等用例也对适配、重映射与发音建模提出新需求。

## 方法
文档化 MFA 3.0 相对 1.0 的发展，核心包括：
- **更大数据预训练**：CommonVoice、MLS 等，多方言/风格；人工清洗；渐进混入噪声数据的 HMM-GMM 训练（monophone→triphone→LDA→SAT + 发音概率）；
- **词典**：WikiPron 等、跨语言谐调窄式 IPA、G2P、可选音系规则扩展变体；
- **适配与重映射**：`mfa adapt`、跨语言 phone remapping，以大模型服务训练外语言；
- **语料工具**：对齐评测（改进 Levenshtein）、SpeechBrain VAD/日记化、WhisperX 转写、中日韩泰分词等。
评测设定（摘要）：英/日/韩等，对照经典与神经对齐器；并评估适配、重映射、发音概率与音系规则贡献。

## 实验与结果
（全文抽取在 §3.4 可用性处截断，实验数字主要来自摘要。）
- MFA 3.0 在四个基准上达 SOTA 或接近 SOTA；**平均边界误差低于 15 ms**。
- 适配与跨语言重映射对训练分布外语言有效；发音概率建模与音系规则在特定条件下带来增益。

## 结论
MFA 3.0 在扩大语言/方言覆盖与工具链的同时，边界精度仍可与当代神经对齐器竞争；适配与重映射是服务分布外数据的实用路径。

## 点评
工作重心是“十年工具演进 + 系统基准”，对语言科学流水线比纯学术新架构更直接有用。强在数据清洗、渐进训练与 IPA 谐调；**PDF 抽取未含实验表**，具体语言/对齐器对照数字需回 PDF；点评不补编未出现的 ms 明细。
