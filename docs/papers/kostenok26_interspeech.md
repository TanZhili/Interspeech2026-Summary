# Calibration-Reasoning Framework for Descriptive Speech Quality Assessment

- 论文编号：2362
- 报告人：Milos Cernak
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/kostenok26_interspeech.pdf

## 问题

可解释语音质量评估需超越标量 MOS，刻画失真维度、伪影类型与时间定位。现有 Audio LLM 描述常流利但不接地，维度分数干扰 MOS，且统一奖励的 RL 难针对各感知维度。

## 方法

两阶段后训练 Audio Flamingo 3：(1) Calibration——SFT 对齐噪声、失真、连续性、可懂度、自然度、MOS 等维度评分与简短描述；(2) Reasoning——用 GRPO，按维度设计细粒度奖励（含伪影检测/时间定位），相对组内归一并加 KL 约束。在 QualiSpeech 等多维基准上对比 QualiSpeech-FT、SQ-LLM、LLM-judge 等。

## 实验与结果

Calibration-Reasoning 达平均 PCC 0.71、MOS PCC 0.76（摘要称相对约 +13% MOS 提升）。维度 PCC 与伪影描述 F1/相关优于仅 SFT 或粗粒度 RL；仅 Calibration 平均 PCC 约 0.66，说明 RL 推理阶段关键。解冻策略与奖励设计影响稳定性。

## 结论

先校准维度尺度再以维度特异 GRPO 强化推理，可使 Audio LLM 同时提升多维评分、MOS 与伪影时域诊断，成为更可靠的描述性质量工具。代码与演示已公开。

## 点评

把“会聊天的质量总结”纠偏为“可核验的诊断”，用分维度奖励对准可解释评估瓶颈。依赖较强基座与标注维度；生成描述的自动评测本身仍有噪声，长期需更多人类诊断标注闭环。
