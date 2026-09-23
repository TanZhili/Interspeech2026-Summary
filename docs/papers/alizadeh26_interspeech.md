# The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation

- 论文编号：2454
- 报告人：Hadi Alizadeh
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/alizadeh26_interspeech.pdf

## 问题
波斯语正式/口语差异大，公开数据多正式朗读，非正式自发语音导致声学–文本错配，ASR/ST 在真实对话上严重退化。

## 方法
构建 T-PID：影视中单人片段人工转写非正式波斯语，ChatGPT-4o mini 译英并抽样质检（改写 WER≈4%），最终 36.77 h、22,443 句、性别均衡。针对性文本规范化并开源 Persian normalizer。微调 Whisper-small/medium 与 Wav2Vec2-BERT；级联 NLLB-200 做 ST。

## 实验与结果
基线 Whisper 在 T-PID 上因幻觉 WER 极高（200+/360+）；微调后 small/medium 约 37.5/36.3，Wav2Vec2-BERT 29.1，且 Common Voice/FLEURS 正式集也提升。级联 ST：微调后 T-PID BLEU 最高 25.30（Wav2Vec2-BERT+微调 NLLB）。T-PID 困惑度远高于正式集，解释困难度。

## 结论
高质量非正式波斯语可显著改善低资源 ASR/ST，并增强对正式域的泛化；数据集与规范化工具已公开。

## 点评
贡献在填补“口语对齐转录+平行英文”空白，而非新架构。音频优先、转写贴口语利于 CTC；翻译依赖 LLM 抽样质检，成语/文化表达仍可能有噪声。
