# Beyond Semantic Dominance: Cognitive Affective Reasoning and Empathetic Response Alignment in Audio Language Models

- 论文编号：2400
- 报告人：Zhixian Zhao
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26h_interspeech.pdf

## 问题
ALM 常被文本语义主导，忽略与字面冲突的副语言线索（讽刺等），且情感推理停留在声学描述，缺少意图/心理层面，回复易流于模板化。

## 方法
提出 **CogAudio-LLM**：构建 **LIME-440K**（约 44 万句、497 小时）——同文多情绪的语义–声学解耦数据，含 EIPS 四步 CoT（感知、意图、心理建模、策略）与 Index-TTS2 合成语音。三阶段训练：SFT 显式 EIPS → 混合显式/仅回复数据做隐式内化 → **DR-SAPO** 双路线 RL（显式路线奖励格式与 CoT 各维逻辑，隐式路线奖励共情，共享共鸣奖励）。底座 Qwen2.5-Omni-7B + LoRA。

## 实验与结果
隐式回复共情：LLM/人工评测全面高于 Freeze-Omni、GLM-4-Voice、Kimi-Audio、Step-Audio、Qwen2.5/3-Omni、GPT-4o-Audio；冲突子集上尤为明显（如 HumDial LLM 冲突 2.91 vs 基线多 <2）。情绪准确率在冲突集从基座约 24% 升至约 46%。消融显示解耦 SFT、混合内化与 DR-SAPO 逐步抬升。

## 结论
解耦数据 + 心理 CoT + 双路线对齐可抑制语义主导并提升共情对齐；真实语音零样本较好，但 TTS 与自发微韵律仍有缝隙。

## 点评
针对“文本捷径 + 浅层情感”双瓶颈，用同文多情绪逼模型听声学，再用 EIPS 把共情做成可监督推理。风险在于训练数据大量合成、裁判（Gemini）与奖励同源偏倚，以及共情分数主观；结论对真实冲突对话的泛化仍需更多野外数据验证。
