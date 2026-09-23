# Data-Efficient ASR Personalization for Non-Normative Speech Using an Uncertainty-Based Phoneme Difficulty Score for Guided Sampling

- 论文编号：776
- 报告人：Niclas Pokel
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/pokel26_interspeech.pdf

## 问题
非规范/障碍语音数据少、声学变异大，个性化微调易过拟合；均匀对待样本或简单熵不确定度难以区分不可学噪声与可学发音难点。

## 方法
用 VI LoRA（或 MCD）对 Whisper 做高效认知不确定度估计；构造音素难度 PhDScore=加权(错误率+熵+(1−真值一致率))；按句内音素平均难度过采样难句做 Full FT/LoRA/VI LoRA。评测 UA-Speech（英语构音障碍）与 BF-Sprache（德语 Apert，经语义重链）；并与一年间隔两次言语治疗报告做纵向相关。

## 实验与结果
过采样降低非规范错误（如 LoRA 在极低可懂度说话人 ∆WER 约 −15 pp），但伴随规范语音遗忘；混入规范样本可缓解。效能与可懂度大致反相关。复合 PhDScore 优于纯熵；须用预训练模型不确定度（微调后信号失效）。PhDScore 与临床报告音素难点更吻合。

## 结论
作者认为 VI LoRA 不确定度驱动的音素难度过采样可数据高效地个性化障碍语音 ASR，并与临床评估对齐。

## 点评
把主动学习式“难样本优先”落到音素级临床可解释信号，且证明熵不够。个性化–遗忘权衡写清楚。依赖对齐到音素与小数据设定；德语仅单儿童病例，外推需谨慎。
