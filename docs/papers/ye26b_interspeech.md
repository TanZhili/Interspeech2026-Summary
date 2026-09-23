# Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning

- 论文编号：2284
- 报告人：Jiangnan Ye
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ye26b_interspeech.pdf

## 问题
细粒度强调控制因标注稀缺与韵律复杂而难；规则调音高/能量常不自然，LLM-TTS 指令微调又数据饥渴。

## 方法
在 F5-TTS 上加 Emphasis Encoder（4 层 Transformer），融合 `<strong>` 等标签嵌入。三阶段：(1) 2.5 h 人工中文强调数据 SFT；(2) 用 SFT 采样 + WPT 突显度排序构造偏好对做 Flow-DPO；(3) Flow-CPS（FlowGRPO 变体）以 WPT 为奖励做组相对优势在线 RL。标签可由 DeepSeek 辅助生成。

## 实验与结果
突显度：F5 0.86 → SFT 1.22 → DPO 1.42 → GRPO 1.45（CosyVoice 1.32）；WER 约 1.62–1.63% 稳定，SIM≈0.71–0.72。主观：E-MOS 2.51 vs CosyVoice 2.16，N-MOS 3.47 vs 3.06。名词强调控制准确率 GRPO 63%（DPO 37%，CosyVoice 22%）。

## 结论
作者认为 SFT→DPO→Flow-CPS 流水线可在有限标注下显著提升强调强度与可控性，同时保持可懂度与说话人相似。

## 点评
把 LLM 对齐套路迁到 flow-matching TTS，并用 WPT 作可计算突显度奖励，缓解标注瓶颈。风险是奖励模型与人类感知不完全一致；主要评测在中文强调场景，跨语与更复杂话语焦点泛化未充分展开。
