# TIMBRE: Layer-Wise Cross-Lingual Speech Emotion Recognition Across 49 Layers and 26 Corpora

- 论文编号：579
- 报告人：Anatoly Marchenko
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/marchenko26_interspeech.pdf

## 问题
跨语言语音情感识别（SER）中，情感线索在何种表征深度上能跨类型学差异泛化仍不清楚。已有工作或只看末层、或只做语料内 probing、或仅覆盖少数语料，尚未把大模型每一层与大规模跨语料迁移系统结合。

## 方法
对 wav2vec2-xls-r-1b 的 49 个提取点（48 个 Transformer 层 + CNN 特征编码器）做 mean-pool 线性探测：在 26 个情感语料（23 语、14 语系）上，标签统一为 angry/happy/sad/neutral，每类最多 500 句；对每层做 26×26 跨语料 logistic regression（C=1.0，训练语料 z-score），共 31,850 次实验。另对比 27 维手工艺声学特征（扰动、F0、MFCC、频谱、共振峰、能量）与全层 mean-pool 的同协议迁移，并对 25 个语料做特征组 leave-one-out 消融。

## 实验与结果
跨语料平均 F1 在 layer 15（约 31% 深度，作者称 CRIS）达峰值 0.392，L45 跌至 0.296（相对峰值 −24.6%）。Romance 相对优势呈 U 形，tonal 相对优势随深度上升；组内/组间迁移在 L15 统计上难区分，整体迁移更受语料表达强度与诱发方式驱动。同分类器下 mean-pool wav2vec2 平均 F1 0.355，声学特征 0.252（约 +41%），声学保留约 71% 基线质量但仅在 3/26 语料上胜出。消融中 MFCC 最重要（平均 ΔF1≈−0.097）。

## 结论
作者认为 L15（或 L12–L18 平台）是冻结 mean-pool 特征做跨语言 SER 的较优提取层；类型学影响层间迁移曲线形状，而语料表达性/诱发风格比语系归属更能解释整体可迁移性。局限包括多为表演/朗读语料、Romance/tonal 样本量小、仅探测单一 SSL 模型、线性探针可能低估层容量等。

## 点评
核心贡献是把“中层情感信息”从语料内现象扩展为大规模跨语料证据，并给出可操作的层选择建议。用固定 LogReg、不调参换可比性，结论对该协议更稳健，但对微调/更强分类器未必直接外推。类型学解释与表演语料、规模共变存在混杂，正文也承认应作探索性解读。
