# CraftTTS: Fine-Grained Prosody Control for Text-to-Speech

- 论文编号：2018
- 报告人：Qihang Lu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yang26l_interspeech.pdf

## 问题
零样本 TTS 全局克隆强，但严格词级强度/语速控制易破坏声学先验，产生伪影、停顿或不自然情绪泄漏。

## 方法
CraftTTS 三阶段对齐 CosyVoice 2：(1) 计算驱动数据：DeepSeek-V3 打 strong/weak/fast/slow 标签，Indextts2 多轮 AR 续写 + best-of-N（音色相似/时长代理语速）构造偏好正样本，无人工标注；(2) 联合 SFT+DPO 增强局部标签敏感；(3) GRPO，奖励解耦为停顿感知 ASR CER、情绪锚定强度对比、语速方向正则，平衡局部可控与全局自然。

## 实验与结果
中文 InstructTTSEval 等评测：相对 CosyVoice 2 基线，完整 CraftTTS 提升 NMOS（3.87 vs 3.67）、STMOS/SPMOS，SMOS 略升；CER 7.01%（基线 6.36%）、Sim 略降。消融与主观表明 Stage 2/3 逐步改善细粒度表达。

## 结论
作者认为零样本偏好构造 + SFT/DPO/GRPO 对齐可使 LLM-TTS 在保持零样本能力下达到更强词级韵律可控。

## 点评
与强调控制工作同属“对齐管线迁到 TTS”，特色是无人工偏好数据与多维解耦奖励，直接针对局部控制破坏全局先验的冲突。CER/Sim 小幅回退提示可控性–保真仍有张力；依赖教师 TTS 质量与 LLM 标注可靠性。
