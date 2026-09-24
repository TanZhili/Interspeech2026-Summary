# An Acoustic Landmark Database of the English Lexicon via Articulatory Synthesis

- 论文编号：1374
- 报告人：Mateo Cámara
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/camara26_interspeech.pdf

## 问题
声学 landmark 标注语料稀缺，人工标注贵且有分歧；连续语音中协同发音又使“应有”事件模糊。自动标注（如 Auto-Landmark on TIMIT）尚缺独立校验，难作可靠 ground truth。

## 方法
用 Pink Trombone 物理声道合成器，从 CMUDict→IPA 词表生成整部英语词表：为每个音素手工映射静态构音目标，词内线性插值做有限协同发音，固定音长与 f0，分别合成成人男/女两套解剖参数。按规则在闭塞、爆破、摩擦启停、鼻音闭开、元音/滑音中点等物理时刻算法放置八类 landmark（V、G、Sc、Sr、Fc、Fr、Nc、Nr）。产出 ALLIE-PT：波形 + 关键帧 JSON + landmark 时间戳。

## 实验与结果
单性别统计：115,487 词、1,100,803 个 landmark；辅音类 676,646、元音/滑音类 424,157，辅音/元音 landmark 比约 1.595。频次最高为 V（279,980），其次 Sc/Sr（各 153,181）、G（144,177）等。语料 >200,000 合成词、双配置、48 kHz/16-bit；可懂度用 STOI（正文抽取段未给出具体分数）。音位结构分析在 4.3 节开头截断。

## 结论
作者认为由构音命令“生成”而非从声学事后推断 landmark，可提供无人工标注误差的沙盒，用于验证 landmark 理论并训练/评测自动检测器；词级、非韵律、有限协同发音是刻意简化边界。

## 点评
把标注问题倒转为可控合成，适合做检测器基准与词典级统计。常音长、常 f0、弱协同发音远离自然连续语音，迁移到真实数据时需额外适配；全文抽取未含 STOI 数值与后续音位模式细节。
