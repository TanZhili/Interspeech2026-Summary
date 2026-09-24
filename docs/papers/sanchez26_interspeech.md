# An Evaluation Framework for Text-to-Speech Voice Reconstruction

- 论文编号：2600
- 报告人：Ariadna Sanchez
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanchez26_interspeech.pdf

## 问题
语音重建需在提升可懂度的同时保留说话人身份，却无“病前真值”；常用 MOS 自然度/相似度敏感度与可靠性不足，客观指标与听感是否对齐也未充分验证。

## 方法
主观：情境化 Best Worst Scaling，分 INTELLIGIBILITY（只评可懂度）与 RECONSTRUCTION（同时考虑可懂度与想象中的病前身份）。客观：WER/PER、WeSpeaker 余弦相似度、UTMOS，以及双参考 TTSDS2——对高可懂 LibriTTS 子集与 SAP 乱序参考分别打分，再取 TTSDSMean 刻画折中。用 17 个零样本克隆 TTS，在 SAP 193 名英语母语障碍说话人（帕金森等，高/低可懂按 WER 30% 划分）上各生成 1 句。

## 实验与结果
全体说话人：INTELLIGIBILITY 上多数 TTS 高于原录音（StyleTTS2 等领先）；RECONSTRUCTION 上多数低于录音，IndexTTS2、Qwen3-TTS、E2-TTS 领先。低可懂子集上几乎所有系统可懂度更好，但 RECONSTRUCTION 仅 IndexTTS2、Qwen3-TTS 高于录音。客观上 WER/PER/UTMOS/TTSDS|LibriTTS 与 INTELLIGIBILITY 强相关；RECONSTRUCTION 上 Spk.Sim. ρ≈0.75，TTSDSMean 更高（全体 0.81，低可懂 0.73）。

## 结论
情境化 BWS 与双参考分布度量比通用 MOS/单指标更能对齐语音重建任务；零样本系统在严重障碍上仍难同时保身份与提可懂度。

## 点评
把“听得清”和“还是本人”拆成两套听测与一套均值分布分数，直接打中重建折中。数据偏帕金森与高可懂；客观相关是系统级排序相关，不等于样本级诊断。听者想象“病前声音”本身主观，框架对更重障碍会更吃力。
