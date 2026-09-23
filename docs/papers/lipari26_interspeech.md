# Disentangling sociophonetic and physiological variation in /s/ acoustics across 12 languages

- 论文编号：2975
- 报告人：Massimo Lipari
- 程序：Tuesday 29 September 2026 / Cross-Linguistic and L2 Phonetic Studies
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lipari26_interspeech.pdf

## 问题
跨语言常见 /s/ 的性别差异，但难以区分是社会表演还是生理（如声道长度 VTL）介导。仅凭声学数据时，如何可靠拆开性别对 /s/ 峰频的直接效应与经 VTL 的间接效应？

## 方法
自建 12 语朗读语料库（GlobalPhone、NCHLT、LibriSpeech 子集；过滤后 1,386 说话人，约 129k 个 /s/ token）。由元音 F1–F3 估计 ΔF（与 VTL 成反比）；对词首元音前 /s/ 用 multitaper 谱取 >1 kHz 最高峰。用带按语言最大随机效应的线性混合模型做因果中介分析：结果模型为 peak ~ ΔF × Gender，中介模型为 ΔF ~ Gender；并做逐语言中介分析。

## 实验与结果
跨语言：ΔF 对峰频有强正向效应（更高 ΔF→更高峰）；性别直接效应边际且约为间接效应的一半；间接效应显著，总效应约 −738 Hz（男相对女）。几乎所有语言 ΔF–峰关系方向一致（阿拉伯语例外不显著）。性别直接效应跨语言差异大：英语/阿拉伯/捷克等显著，日语/波兰/俄语不显著；普通话直接与间接效应反向、近乎抵消。半数语言直接效应不显著但总效应显著——若不控制 VTL 易误判“社会表演”。

## 结论
VTL（ΔF）与 /s/ 峰频关系跨语言较稳定；性别差异中生理与社会成分的相对大小因语言而异，中介分析有助于从声学数据拆分二者。局限包括 ΔF 本身可能被操控、性别与生理性别未区分、朗读语料可能缩小社会效应，以及 16 kHz 采样与峰频索引的粗糙性。

## 点评
把社会语音学问题明确写成中介因果结构，并在 12 语大样本上检验，方法贡献突出。关键假设是“ΔF≈纯生理”，作者自己也指出喉高/唇位可表演，故直接效应仍可能混入形态而非纯表演；阿拉伯语样本小、普通话反向模式值得后续用体型或 MRI 复核。
