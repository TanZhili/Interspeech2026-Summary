# Modulation of Phonetic Realizations in Cantonese Dialogue with Human and AI Interlocutors

- 论文编号：1194
- 报告人：Peggy Pik Ki Mok
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26m_interspeech.pdf

## 问题
人机语音互动中的语音调节多在语调语言、偏积极表达系统上研究；粤语等声调语言、以及面对负面/对抗性 AI 时，对话者身份（人 vs AI）如何改变精细语音实现仍不清楚。

## 方法
17 名香港粤语母语者，被试内 2×2：Interlocutor（Human vs AI）× Emotion（Neutral vs Negative）。Wizard-of-Oz 脚本对话 20 段；人类条件为同一女性母语者音视频，AI 条件为同说话人约 3000 句训练的 DurIAN 定制 TTS + Memoji，音色/内容可比。测目标词时长、六声调时正则化 F0（GAMM）、三角元音 VSA（情绪主效应因数据平衡仅在情绪上分析）。MFA 强制对齐后人工校正。

## 实验与结果
目标双音节词时长：AI 条件显著更短（β = −10.891, p = .04）；音节时长边际更短；话语语速无显著差。F0：相对人类，中性下 AI 上 Tone 1、Tone 4 升高、Tone 5 降低；负面下 Tone 4 亦升高；Tone 2 在负面情绪下相对中性升高（两种 interlocutor）。VSA 在负面下边际更大（β = 1.07, p = .057）。全文讨论后半截断，引言/结果中的主要发现已可读。

## 结论
与 AI 对话时目标词更短、部分声调 F0 呈声调特异而非整体抬高/压低；情绪效应较弱且偏局部（Tone 2、边际 VSA）。表明声调语言中 interlocutor 效应比先前报告的更细粒度。

## 点评
用同一说话人定制 TTS 控制音色/语速混淆，比直接用 Alexa 类助手更干净，也解释了为何与“对 AI 说话更慢更长”的文献相反。时长效应落在反复出现的目标词而非全局语速，设计上便于定位。截断限制了对完整讨论与局限的核对；样本量 17、脚本对话外推到自然对抗性交互仍需谨慎。
