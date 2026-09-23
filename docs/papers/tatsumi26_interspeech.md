# Universality of Speech Emotion Recognition in Humans and Speech Language Models

- 论文编号：3061
- 报告人：Yuka Tatsumi
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/tatsumi26_interspeech.pdf

## 问题
人类能在不熟悉语言中较好识别语音情绪（universality），但英语单语 ASR 编码器是否同样具备跨语种情绪识别、且是否与人类在情绪类别与反应偏向上一致，尚不清楚。

## 方法
人类侧：Prolific 招募英语单语听众（分析用有效样本约 101 人量级，文中 119 人录音后排除 18 人），对法语、日语、希腊语、泰语情绪语音做六选一（happy/sad/angry/fear/surprise/neutral）。模型侧：冻结 Whisper-medium.en 与 HuBERT-large-ll60k，在各层做全局平均池化后训 \(L_2\) 多项 Logistic Regression 探针；仅用英语 ESD、CREMA-D、RAVDESS 训练，非英语刺激与人类完全相同且不做适配。主分析层按英语验证集最优选取（Whisper L17、HuBERT L11）。

## 实验与结果
人类总体准确率 43.8%（机会水平按最频类 sad 为 21.4%），中性最高（80.0%），happy 最低（22.6%）。非英语上 Whisper 39.0%、HuBERT 48.3%。bootstrap：Whisper–人类差异不显著（−1.4%，CI 跨 0）；HuBERT 显著高于人类（+6.8%）。情绪准确率排序人类与模型明显不同；错误反应中人类默认 neutral（32.4%），Whisper 默认 happy（52.4%），HuBERT 默认 surprise（53.0%）。

## 结论
冻结单语 ASR 编码器也表现出跨语种情绪识别 universality，整体可达或超过人类；但类别表现与反应偏向与人类不同。局限：英语训练语料选择、Whisper 英语变体是否绝对无非英语音频、每语一种数据集、情绪标签不完全对齐。

## 点评
用相同刺激直接对比人与探针，把 universality 从“高于随机”推进到“系统差异”。强在拆开总体准确率与默认标签偏差。脆弱点是 acted 语料与探针层选择：主分析层按英语最优选取，非英语最优层可能不同，文中亦提示结果为下界。
