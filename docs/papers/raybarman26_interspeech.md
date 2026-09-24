# Towards a Phonology-Informed Evaluation of Multilingual TTS

- 论文编号：3311
- 报告人：Neeraj Kumar Sharma
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/raybarman26_interspeech.pdf

## 问题
MOS 等自然度指标不检验语言特有音系对立；阿萨姆语 ATR 元音和谐由语法决定共现，TTS 可能“好听”却中和或错放和谐条件对比。

## 方法
用 14 名母语者录音（8125 元音 token）建人类基准，提取 Lobanov 归一化 F1–F3、B1、时长及高度/前后特征；Meta MMS TTS（mms-tts-asm）合成同载体句（281 token）。Task 1：LR/RF 做跨域 ATR 分类（H→H、H→TTS 等）。Faithfulness audit：比金标 ATR 与分类器预测，区分 overgeneration（−→+）与 underproduction（+→−）。Task 2：词级三分类和谐类型，用声学聚合与金标/预测 ATR 序列特征。

## 实验与结果
LR 的 H→H 与 H→TTS 准确率均约 82%，宏 F1 0.81；RF 域内更高但迁移落差大。TTS 错配率 0.16，但 underproduction:overgeneration≈7:1（人类近对称）；[+ATR] 中元音 /e/、/o/ 约 1/3 token 被判为 [−ATR]。词级上 H→TTS 时 A+B_pred（宏 F1 0.62）优于 A+B_gold（0.49），说明声学 ATR 轮廓与意图音系不一致。

## 结论
MMS 对中元音 [+ATR] 声学线索系统性 underproduce；框架可推广到其他有可测声学线索的音系对立，但本文仅单系统、单现象、TTS 样本小且类别不平衡。

## 点评
把“听感尚可”与“音系忠实”拆开，用人类训练分类器当声学探针，比 MOS 更对准语法条件对立。结论强度受 TTS token 少（尤其 AgrNoMixYes）与类不平衡约束；方向性偏置比总错配率更有诊断价值。
