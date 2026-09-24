# Hearing the Order: Investigating Position Bias in Large Audio-Language Models

- 论文编号：1025
- 报告人：Yu-Xiang Lin
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lin26c_interspeech.pdf

## 问题
LALM 常在 MCQ 上评测；选项顺序是否系统影响预测（位置偏差）在音频–语言模型中尚未系统验证，可能扭曲排行与可靠性。

## 方法
在 MMAU、MMAR、MMLU 及其 GPT-4o mini TTS 口语版（过滤 >180 s、固定四选项）上，将正确答案轮流固定到 A/B/C/D 并打乱其余选项。测 Gemini-2.0-Flash、Phi-4-Multimodal、Qwen2.5-Omni-3B/7B、Voxtral-Mini-3B、Voxtral-Small-24B；指标含准确率、Δ准确率、RSD、CKLD。再比有无选项标识符、与文本 LLM 对照，并用循环/全排列多数投票缓解偏差。

## 实验与结果
六模型均有位置偏差：部分约 5% 波动，Phi-4-Multimodal 最大约 24%。偏好方向因模型而异（如偏好 A 或 D）。选项字母标识常提准确率但不稳降偏。与文本基座比：Voxtral 偏差异与 Mistral 相近，Qwen 系音频微调后可偏离文本行为。全排列相对原始与循环通常更好降 RSD/CKLD 并提准确率；打乱选项会改变模型排名。

## 结论
位置偏差在 LALM 中普遍存在，常规 MCQ 评测可能不可靠；排列投票可缓解但算力更贵，需更专门的评测与消偏方法。

## 点评
把 LLM/VLM 已知问题系统迁到 LALM，并对排行敏感性给直接证据，对基准设计很有价值。口语版依赖 TTS，与真实口语分布有差距；全排列成本高，实用评测仍需更轻量折中。
