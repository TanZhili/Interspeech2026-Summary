# NVV-SuperBench: Beyond Words, Beyond Quality—Benchmarking Nonverbal Vocalizations in Speech Generation

- 论文编号：2513
- 报告人：Liumeng Xue
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xue26c_interspeech.pdf

## 问题
笑声、叹息、抽泣等非言语发声（NVV）对类人语音关键，但现有评测很少同时检验系统是否生成目标 NVV、位置是否正确、是否显著且不伤语音质量。

## 方法
NVV-SuperBench：统一 45 类 NVV 分类（呼吸、喉生理、笑声谱、哭声谱、情感发声、口腔杂类），英/中各 2,250 条（每类 50）。三阶段建数：从 InstructTTSEval 挖种子（Gemini 标注 + 人工多数表决）→ 按类控制生成 text / text_with_nvv / caption → 自动一致性 + 人工质检补齐。控制接口分 prompt（自然语言 caption）与 tag（如 [laugh]）。评 15 个系统（8 tag + 7 prompt）。客观：WER/CER、DNSMOS、CLAP（prompt）、NVV P/R/F1 与归一化标签距离（tag，Gemini GT 条件验证）；另有主观听测与 LLM 多评审。

## 实验与结果
摘要与导论：NVV 可控性常与整体语音质量解耦；低 SNR 口腔线索与长时情感 NVV 是持续瓶颈；不同控制接口表现差异大。正文在客观指标定义处截断，各系统具体分数未完整可读。

## 结论
该基准把 NVV 生成评测从笼统质量扩展到可控性、位置与显著性，揭示当前系统短板并支持跨接口公平比较。

## 点评
分类学覆盖远超多数 TTS 标签集，评测轴设计对“会不会笑在对的位置”很贴题。依赖 Gemini 做种子与验证存在幻觉风险，作者用约束编辑与人工审核缓解。因结果表抽取缺失，系统排名只能采信摘要定性结论。
