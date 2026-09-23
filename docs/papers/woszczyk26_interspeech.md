# Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation

- 论文编号：3392
- 报告人：Dominika Woszczyk
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/woszczyk26_interspeech.pdf

## 问题
TTS 保真提升后，单一“自然度”难反映是否适合下游用途；合适性如何随域变化、与人类相似度是否一致，缺少系统证据。

## 方法
150 名英语听者，拉丁方评 5 系统（Kokoro、Gemini TTS、Kyutai-TTS、GPT-4o-mini-tts、ElevenLabs）+ 真人，覆盖朗读、演员、动画角色、助手、自发说话者等人格；刺激来自 LibriQuote、MSP-Podcast、MELD、AnimeVox 等。同时报人类相似度与“说服力/合适性”，并分析声学特征与自动指标相关。

## 实验与结果
合适性跨域独立于自然度：Kokoro 适朗读/助手但弱于对话；Kyutai 适自发对话但弱于助手/动画。人类相似度与合适性在 Actor/Spontaneous/Reader 正相关，动画近零、助手负相关（ρ≈−0.44）。动画偏好更高节奏波动，助手偏好更稳、更低 f0 范围。单一自动指标难以普适预测合适性。

## 结论
TTS 未“通吃”：优化一域可伤另一域；自然度会惩罚风格化、奖励自发性，需域感知评测。

## 点评
把自然度与合适性拆开并跨域对照，直接服务产品选型。低评者一致性（α≈0.2）说明合适性主观且期望驱动，榜单需报告域与协议。助手“略机器感更合适”的现象值得后续验证。
