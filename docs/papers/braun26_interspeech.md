# Mitigating Scoring Errors and Compensating for Nonverbal Subtests in Speech-Based Dementia Assessment

- 论文编号：2806
- 报告人：Franziska Braun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/braun26_interspeech.pdf

## 问题
基于语音自动化德语 Syndrom-Kurz-Test（SKT）时，病理/方言/结构化应答导致转写错误，且运动子测无法靠语音完成，限制总分与分型准确性。

## 方法
158 名临床受试者。规则基线（RB）从 Whisper 转写算子测分；deep correction 用 RB + Whisper 编码器/解码器嵌入精炼子测分；deep compensation 融合可用言语子测表示以逼近专家总分（补偿缺失运动子测）。并搜索高效子测序列以兼顾分类与效率。

## 实验与结果
RB+ENC/DEC 与专家子测分强相关，ASR 难子测相关可提升最多约 0.35。即使省略运动子测 4/5，补偿模型与专家总分仍可达很高相关（文中称近 0.9 量级）。最优言语子测序（如 1→7→8→6→2）在保持总分相关的同时提升效率。

## 结论
转写分数与 Whisper 嵌入融合可纠评分误差；用言语子测表示可补偿非言语子测缺失，支持更可及的语音化 SKT 筛查。

## 点评
把临床量表自动化中的两类硬伤（ASR 错分、运动项缺失）拆开处理，工程路径清晰。样本量中等、口罩录音与临床场景特定，外推需谨慎；补偿不等于真正测到运动域，诊断解释仍应标注缺失维度。
