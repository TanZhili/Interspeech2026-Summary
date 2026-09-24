# How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR

- 论文编号：920
- 报告人：Simon Gonzalez
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26c_interspeech.pdf

## 问题
多语 ASR 替换错误对语义保持的影响难以用 WER 刻画；先前多用 WALS 等语言层类型学代理，不清楚从 ASR 输出直接量测的音系/形态/句法/词汇特征如何交互、是否因架构而异。

## 方法
在 FLEURS 42 语、>154 小时上跑 Whisper 与 Seamless；仅分析对齐后的替换错误。因变量为句级语义相似度 SENT（paraphrase-multilingual-MiniLM）；自变量为词级 PHN（phonemizer+Levenshtein）、MOR/SYN（Stanza POS/依存差）、SEM（fastText）。用 glmmTMB 混合效应 beta 回归，分阶段加入维度交互、ASR 三阶交互与语言效应。

## 实验与结果
主效应均显著：PHN 负向最强（β=-0.31），SEM 正向最强（β=0.84）。交互模型显著改进拟合；最强为 MOR:SYN（χ²=165 量级改进中 χ²=113）。Seamless 基线更好（Whisper β=-0.20）；Whisper 对 PHN/SEM/SYN 退化更敏感，但更会利用形态保持。语言随机效应差异大（如越南语维度强但句级一般，捷克语音系差但句级可补偿，乌尔都语句级最差）。

## 结论
句级语义保持来自跨维度系统交互而非孤立错误；Whisper 与 Seamless 以不同机制整合语言学信息；类型学差异导致不同错误剖面，多维框架比聚合准确率更有信息量。

## 点评
把评价从 WER 拉到“意义是否保住”，并对架构做交互建模，对多语部署诊断有价值。仅替换错误、依赖 Stanza/phonemizer/嵌入工具链，插入删除与工具误差会偏置结论；属分析研究，未给出可直接落地的纠错或训练改法。
