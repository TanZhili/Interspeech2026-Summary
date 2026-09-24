# Investigating ASR for Low-Intelligibility Dysarthric Speech

- 论文编号：1326
- 报告人：Jun Wang
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kwon26b_interspeech.pdf

## 问题
构音障碍 ASR 研究多用轻–中度、短时数据；重度低可懂度（本例 SIT 可懂度 20.9%）是否可学、以及重度适配能否泛化到其他患者尚不清楚。

## 方法
一名无神动性脑瘫、语速约 37 词/分的英语说话人，约一年家庭录音，本研究用 21.6h（总约 100h）。说话人相关：从零训 BLSTM-HMM；微调 Whisper tiny–medium.en。另做 Whisper-medium 数据量缩放，并在 TORGO 构音障碍说话人上测跨说话人泛化。

## 实验与结果
说话人相关：BLSTM-HMM WER 13.4%；Whisper-medium 微调后测试 WER 10.5%（微调前 63.4%）。训练从 1h→15h，测试 WER 25.40%→10.52%（相对降约 58.6%）。TORGO：重度说话人多数 WER 降 6–12pp，轻度/中度几乎不变；整体均值 45.8%→41.7%（摘要称重度约 +6.4pp 改善且不伤轻中度）。

## 结论
在充足单说话人数据下，重度构音障碍语音含可学结构规律；基于重度数据微调的 Whisper 可改善其他重度说话人而不显著损害轻中度。

## 点评
用超长单说话人重度数据直接挑战“重度太乱学不会”的假设，缩放曲线很有说服力。跨说话人增益主要落在重度，符合选择性迁移叙事。局限是单供体、Whisper 30s 切分，会话/自然对话泛化仍待证。
