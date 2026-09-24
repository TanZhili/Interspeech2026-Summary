# The SSPNet Speaker Personality Corpus Version 2: Investigating the Role of Language Understanding in Automatic Personality Perception

- 论文编号：383
- 报告人：Alessandro Vinciarelli
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/alshubaily26_interspeech.pdf

## 问题
原 SSPNet SPC 是 APP 常用基准，但评测者听不懂法语，只能依赖副语言；且 9 点量表偏粗、无转写、无标准协议，妨碍多模态与“语言理解是否改变人格印象”的研究。

## 方法
发布 SPC V2：仍用原 640 条 10 秒法语新闻片段（322 说话人）。新增 ASR 转写；两组评测者各约 100 人（懂法语 vs 仅英语）用 BFI-10 的 0–100 分评 Big Five，每条 10 人平均，并可中位数二值化。提供特征、说话人独立五折协议与 6 套基线（Whisper 副语言 / Word2Vec 语言，分类与回归，中/晚融合）。

## 实验与结果
表 1：多数配置显著优于随机/均值基线。懂法语组在 Conscientiousness、Extraversion 等上准确率更高（如多模态尽责性 Acc 67.1%）；不懂法语组 Agreeableness 副语言 Acc 达 61.2%。回归 MAE 约 5.9–8.4（百分制）。

## 结论
SPC V2 使语言理解对照、回归与可复现多模态 APP 成为可能，并附带统一基准协议，意在替代原 SPC。

## 点评
核心贡献是实验设计而非新模型：同音频、异语言理解能力，直接拆开词汇与副语言对第一印象的贡献。转写来自在线 ASR，误差会抬高语言通道噪声；基线 LSTM 偏旧，但协议清晰便于后人替换更强编码器。
