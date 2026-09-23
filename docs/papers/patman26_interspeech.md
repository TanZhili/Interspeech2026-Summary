# Assessing the effect of volitional and synthetic pitch raising in female speakers on automatic speaker recognition

- 论文编号：444
- 报告人：Kirsty McDougall
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/patman26_interspeech.pdf

## 问题
意志性抬高音高是法医常见语音伪装，男性说话人上已显示会严重损害自动说话人识别（ASR），但女性基频更高、抬高策略不同（少用 falsetto、升幅通常更小），其对 ASR 及说话人间变异尚不清楚；亦需检验合成 f0 操纵能否替代真实意志性抬高。

## 方法
(1) PASR 库 3 名女性语音学家：默认与意志性抬高朗读，VOCALISE 2021 spectral x-vector（22 维 MFCC）做非同期 D–D / D–R 同/异说话人比较，报告 EER、x-vector 分数与 zooplot。(2) 声学/听感：Praat 长时 f0、音高 excursion；听感评估喉位等策略。(3) 试点：LMS 库 16 名南方标准英式英语女性，用 Praat 将样本 2 的长时 f0 合成抬高 +1.5 至 +10.5 ST（条件 A–E），同样做 D–D 与 D–合成比较。

## 实验与结果
PASR：D–D EER = 0.0%，D–R EER = 14.4%。退化主要由 P5 驱动（抬高中位 f0 最高约 342 Hz，升幅约 9.8 ST，且音高 excursion 受限）；P8 等同/异分数仍较分离。合成试点：LMS D–D EER = 3.9%；EER 随抬高幅度升至极端 +10.5 ST 时 15.2%。Zooplot 显示中等及以上抬高后“dove”消失，部分说话人变为 chameleon；效应依赖默认 f0 在群体分布中的位置，说话人间不一致。合成无法复现意志性抬高中的多重发音策略。

## 结论
女性抬高 f0 后 ASR 表现高度说话人特异：有人仍可区分，有人变难识别；意志性场景的变异更可能来自策略差异，合成场景则与默认 f0 位置等相关。合成抬高不应视为意志性抬高的代理；需更大规模多说话人意志性数据以区分群体与个体效应，服务法医应用。

## 点评
把“整体 EER 变差”拆到个体策略与 f0 分布位置，对法医 ASR 很有用。强在同一 VOCALISE 管线下对照真实意志性与合成操纵；弱在 PASR 仅 3 人且为训练有素的语音学家，外推到外行伪装需谨慎，合成试点也不能代替真实喉部策略。
