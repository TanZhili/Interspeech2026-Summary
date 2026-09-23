# WER Are We (Really): How Well Do Top Open ASR Leaderboard Models Generalize to Nonstandard Speech?

- 论文编号：3522
- 报告人：Nihar Mahapatra
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/dhaka26_interspeech.pdf

## 问题
Open ASR Leaderboard 上主流模型在标准基准 WER 约 5–7%，但对口吃、构音障碍等非标准语音的泛化未知；既有工作多聚焦单一病况或模型族。

## 方法
在 FluencyBank、SEP-28k（口吃，CHAT 重标）与 UIUC SAP（构音障碍，多病因）上，统一 16 kHz、贪心解码，评测 Whisper-Large-v3、CrisperWhisper、Parakeet-TDT、Canary-Qwen、Granite-Speech。报告全局 WER/CER、词级 F1、BERTScore；参考与假设均去标点、去 CHAT 口吃码（因此不利逐字模型）。

## 实验与结果
相对榜单，平均 WER 约膨胀 2–5×，极端可达 24×。Whisper 整体最稳（如 FB WER 0.18、SEP 0.12）；Parakeet 在构音障碍 CER 与 CP/DS/Stroke 等条件上互补优势。Granite 幻觉/重复严重（SAP 平均 WER 可 >3，过滤后仍差）。无单一架构通吃所有构音病因与任务类型。

## 结论
作者认为榜单成绩严重高估可及性；Whisper 泛化最好，Parakeet 在部分构音条件有用，需面向可及性的专项评测与调优。

## 点评
价值在“榜单锚定 + 多架构 + 口吃/构音双轨”的黑盒体检。CHAT 规范化会抬高逐字系统 WER，作者已坦白。架构因果解释属假说；Granite 失败更像适配器–LM 先验失控案例，对“更大未必更稳健”有警示。
