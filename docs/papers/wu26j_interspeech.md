# AuscuTSLM: Patient-Level Multimodal Question Answering from Multi-Site Auscultation Recordings

- 论文编号：2037
- 报告人：Fan Wu
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26j_interspeech.pdf

## 问题
听诊主观性强；通用 ALM 不擅生理声学细微异常。既有方法多为孤立分类或短窗切分，难做多部位、患者级问答式综合评估。

## 方法
AuscuTSLM：用门控交叉注意力将多部位听诊录音对齐冻结 LLM 嵌入空间；比较轻量自训编码器（Raw/Mel）与 Wav2Vec2/Whisper/CLAP；支持更长上下文（至约 30s）与多部位聚合。在 CaReSound 上做患者级 QA（是否题 + 开放生成）。

## 实验与结果
1.4B 模型：Yes/No Acc 93.50%、F1-macro 0.865、Contains-Match 42.60%、ROUGE-L 0.673、METEOR 0.643、BERTScore 0.952，优于零样本 ALM 与微调 CaReAQA（F1 0.846）。Raw 编码器与大预训练前端相当或更好；上下文从 30s 缩到 10s 性能明显下降，多部位聚合可部分补偿截断。

## 结论
域专用轻量前端 + LLM 对齐可 rival 大规模 ALM；多部位空间冗余有助于患者级听诊 QA。

## 点评
把听诊从分类推向可问询的患者级理解，更贴近临床交互。生成指标提升大于二分类，说明对齐主要改善文本 grounding。依赖 CaReSound 与冻结 LLM 世界知识，罕见病理与噪声设备外推仍待验证。
