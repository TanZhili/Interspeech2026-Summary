# AURA Score: A Metric for Holistic Audio Question Answering Evaluation

- 论文编号：3185
- 报告人：Satvik Dixit
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/dixit26_interspeech.pdf

## 问题

开放式音频问答（AQA）难用准确率评；沿用 BLEU/METEOR/BERTScore 或音频描述指标忽略问题语境、推理与部分正确，长答案上与人类相关弱。需要同时看文本正确性与音频接地的专用指标。

## 方法

构建 AQEval：约 1 万条（问题、参考、多 ALM 回答）由 5 名众包标注正确性（聚合成 0/0.5/1），音频来自 ClothoAQA 与 OpenAQA。提出 AURA：LLM few-shot + CoT 对回答打分，并将问—答改写为假设后用音频蕴含（CLAP 等）检查是否被音频支持，两者加权归一得最终分。系统对比传统 NLG、FENSE/MACE 与纯 LLM-judge。

## 实验与结果

AURA 与人类相关整体最高：ClothoAQA 总体约 72.62 vs LLM 基线 62.59；OpenAQA 总体 45.44 vs 43.56；相对纯 LLM 总体可高约 9.1%。传统 n-gram 在二值/单词题与长答上明显掉相关。消融显示 few-shot、CoT 与音频接地项均贡献。

## 结论

AQA 评测必须问题条件化并接地音频；AQEval + AURA 提供更对齐人类的基准与指标，资源已释放以推动更好开放式音频理解评测。

## 点评

明确指出“字幕指标 ≠ 问答指标”，并用音频蕴含补纯文本 LLM 裁判的幻觉风险，方向正确。代价是依赖外部 LLM 与蕴含模型，成本与可复现性受版本影响；OpenAQA 绝对相关仍中等，说明长开放答评测远未解决。
