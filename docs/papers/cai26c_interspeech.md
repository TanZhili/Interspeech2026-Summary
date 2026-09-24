# Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts

- 论文编号：2297
- 报告人：Yunrui Cai
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cai26c_interspeech.pdf

## 问题
联合多说话人 ASR（含归因与时间戳）在说话人数未知、输出结构严格时很难；仅 SFT 对齐 Speech-LLM 在高重叠下易突发幻觉与畸形 speaker/timestamp 标签。

## 方法
两阶段生成框架：(1) CoT 增强 SFT：先推断全局说话人数再转写；(2) GRPO 约束探索，用 Multi-dimensional Constraint-Aware Reward（MCAR）直接优化置换不变准确度，并强制计数、时间与结构约束（含 burst 惩罚等）。骨干 Qwen2.5-Omni-7B + LoRA；在高重叠 1 万样本上做 GRPO。

## 实验与结果
Libri2/3Mix 与 Dynamic-Mix(2+3)：SFT+CoT+GRPO 在 3 说话人 cpWER 14.52%、WDER 1.95%；Dynamic-Mix cpWER 9.24%、WDER 1.12%、CoT-Acc 99.72%。相对 SFT+CoT，GRPO 带来约 35%/54% 相对 cpWER 降幅。零样本基线说话人计数仅约 32%。

## 结论
先计数的 CoT + 多维约束 GRPO 使 Speech-LLM 在未知人数、高重叠下联合转写与日志显著更稳，超越仅模仿式 SFT。

## 点评
把“人数未知”显式建成推理前缀，再用 RL 罚结构崩坏，对准生成式多说话人输出的主要失败模式。评测偏合成混合；真实会议噪声/重叠分布外推未充分展开。奖励设计复杂，权重敏感。
