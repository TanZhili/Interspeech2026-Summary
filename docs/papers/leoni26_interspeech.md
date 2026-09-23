# Indigenising Speech Technology: Building a TTS Model for te Reo Māori

- 论文编号：1443
- 报告人：Gianna Leoni
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/leoni26_interspeech.pdf

## 问题
公开 Māori TTS 缺失或质量差；主流多语系统忽视 ng/wh 等音位与双语码切换。社区需要文化上可接受、服务于语言复兴的合成声，而非“数据越多越好”的堆量路径。

## 方法
Te Hiku Media 原住民主导：经同意选用族内广播人才（先男后女），文本优先 Māori 作者、经语言专家手工校 macron/专名，幻灯片逐句录制。现约 24 小时男声（近 11h Māori + 13h+ 英语）与 8h+ 女声（3h+ Māori + 近 5h 英语）。质检听审批准/重录/改文本。训练沿用既有管线（IPA、西班牙语预训练因音系相近等）。评测靠社区语言专家主观审听；自建 90 句全音覆盖 Māori benchmark 与 100 句双语码切换 benchmark。

## 实验与结果
专家对照迭代报告审元音辅音、音高/韵律/清晰自然度；早期机器人分段感逐步改善。专名覆盖不足仍是持续难点。无公开 MOS/WER 数字；强调精心少量数据优于劣质大规模开源 Māori 数据。

## 结论
细致策展、质保与主权治理可在有限数据下做出高质量 Māori TTS，并给出可复制于其他濒危/少数语言的流程模板。

## 点评
贡献重心在伦理—数据主权—质控方法论，而非新网络结构。强在社区内人才、文本与评测闭环；弱在客观指标少、合成器部署细节多指向前作，读者需另文补全训练数字。
