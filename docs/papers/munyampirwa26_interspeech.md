# Contextual Earnings-22: A Speech Recognition Benchmark with Custom Vocabulary in the Wild

- 论文编号：1375
- 报告人：Berkin Durmus
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/munyampirwa26_interspeech.pdf

## 问题
学术 ASR 榜 WER 近饱和，但工业场景中人名/公司/产品等自定义词错误往往决定可用性；缺标准化的、带真实语境词表与干扰项的公开评测。

## 方法
基于 Earnings-22：LLM 抽人/公司/产品词，按词切 15 s 片段，wav2vec 对齐并人工校对（约 29.5% 片段改词）。提供 local（仅本段词）与 global（整通电话词表含干扰）两种语境。评测 WER + 关键词 Precision/Recall/F。基线含 Deepgram、OpenAI Whisper API、AssemblyAI、Whisper OSS、CTC-WS、Parakeet+CTC-WS。测试 630 样本。

## 实验与结果
给语境普遍抬升关键词 F，WER 变化因系统而异（有的变差，存在幻觉/重复等伪影）。local 比 global 更容易；提示与 boosting 两路线均可显著改善自定义词，规模系统与学术 boosting 均有收益。强调关键词指标与 WER 互补。

## 结论
公开 Contextual Earnings-22 为自定义词 ASR 提供可复现基准，暴露“WER 相近但关键词差距大”的现象，并对比 prompting vs boosting。

## 点评
问题卡在“可用性 = 稀有实体”，评测设计（local/global）贴近部署。人工校对提升可信度；规模仍相对小（55 源文件），且部分商用 API 版本随时间变化需锁定。
