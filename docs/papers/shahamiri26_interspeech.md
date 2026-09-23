# BetterSpeak: An Atypical Speech to Typical Speech Platform for Dysarthric Speakers

- 论文编号：3605
- 报告人：Seyed Reza Shahamiri
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shahamiri26_interspeech.pdf

## 问题
构音障碍（尤其儿童）语音变异大、数据稀缺，通用 ASR（如 Whisper）在重度病例上 WER 可很高；需要可手机部署的个性化识别并配合 TTS 辅助沟通。

## 方法
BetterSpeak 移动平台 + 两阶段个性化 Conformer：Phase1 用健康对照（UASpeech/TORGO 等）做词汇域适应；Phase2 用入职少量用户录音仅微调靠近声学输入的编码器层。识别文本可 LLM 润色后 TTS 朗读；支持隐私模式停存录音、监护人纠错反馈持续更新模型。

## 实验与结果
管线前期评估平均 WER：UASpeech 21.5%、TORGO 12.7%，优于先前 Seq2Seq。平台本身尚处伦理批准后的开放试验计划（唐氏/脑瘫等），未在本文报告新的现场儿童试验数字。

## 结论
数据高效个性化适配使构音障碍 ASR 可做成可及辅助技术；计划公开试验后对全体构音障碍用户开放。

## 点评
把已发 Conformer 适配接进儿童可用 App，闭环采集–适应–TTS。强在少样本防过拟合设计；弱在公开儿童构音库缺失、本篇以演示/平台为主，现场效度待试验。
