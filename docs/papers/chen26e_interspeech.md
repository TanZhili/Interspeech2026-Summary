# CAAD: Contrastive Audio-Aware Distillation for Efficient Speech Language Models

- 论文编号：645
- 报告人：Chun Wei Chen
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26e_interspeech.pdf

## 问题
Speech LM 参数大且易被语言先验压过声学证据；对比解码（正路径音频 / 负路径纯文本）可增强接地但双倍推理延迟。标准知识蒸馏会把教师的语言偏置一并拷给小模型，且逐步自回归对比目标训练难并行。

## 方法
提出 Contrastive Audio-Aware Distillation（CAAD）：Stage 1 按 DeSTA 从音频元数据（性别、情感、环境等）用 Llama3-8B-Instruct 生成 Pseudo-GT 锚序列；Stage 2 对冻结教师同步 teacher-forcing 正/负路径，目标 \(\hat{z}=(1+\alpha)z^+-\alpha z^-\)，学生对齐 KL（温度 \(\tau\)）并加 Pseudo-GT CE，总损失 \(\lambda L_{CD}+(1-\lambda)L_{GT}\)。学生为 DeSTA2 的 Llama-3.2-3B（教师 8B），仅训 Q-Former 适配器约 32M 参数；DeSTA2 指令数据，A6000 约 70 小时。评测 Dynamic-SUPERB 五维与 MCR-BENCH 情感冲突（Shift）。

## 实验与结果
3B CAAD 在 Dynamic-SUPERB ALL 54.44，高于 Std. KD 50.40、测试时 CD 学生 35.80，并在部分副语言任务超教师 greedy。MCR-BENCH：Acc_neu 45.90、Shift 79.03（Std. KD Shift=100）。\(\alpha=1.0\) ALL 最高 55.00，\(\alpha=2.0\) Shift 最低；元数据锚优于直接音频同步。

## 结论
作者认为把对比音频感知内化到单路径学生可降延迟并减语言偏置；局限是蒸馏收益受师生能力差约束，对已很强的小模型增益可能有限。

## 点评
核心是用 Pseudo-GT 解锁全序列对比蒸馏，把推理期双路径成本前移到训练。强项是偏置指标与 \(\alpha\)/锚消融完整；脆弱处在于 Pseudo-GT 质量决定目标分布，且只训适配器时表征上限仍受冻结 LLM 限制。
