# Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR

- 论文编号：2309
- 报告人：Seunghee Ma
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ma26d_interspeech.pdf

## 问题
大规模预训练 ASR（如 Whisper）顺序域适应时会发生灾难性遗忘；严格 rehearsal-free 设定下仅有上一模型参数可用。标准 LwF 对所有 token 等权蒸馏，不确定教师输出会污染保留方向，且监督梯度与蒸馏梯度冲突时会损害保留。

## 方法
以冻结上一模型作教师：用教师分布熵构造 token 级权重 λ_t，抬高低熵（自信）token、压低高熵 token，得到熵引导蒸馏损失。将蒸馏梯度视为 retention direction；当 cos(g_CE, g_distill)<0 时，用系数 η 投影掉监督梯度中与蒸馏方向冲突的分量。基于对角 Fisher 分析冻结 encoder、只微调 decoder。顺序适应 LIB→AMI→TED→SPG。

## 实验与结果
Whisper Large-v3，η=0.75。最终平均 WER 8.12%，相对 LwF decoder-only（8.75%）降 7.2%，相对 FT decoder-only 降 15.9%；BWT 从 LwF 的 −4.63 改善到 −2.82。无 replay 仍优于带 1h TED 缓冲的 GEM/ER。Common Voice 多语退化平均绝对增幅 0.95%，相对 LwF（1.96%）降 51.5%。消融显示投影主推保留与泛化，熵加权在投影下略恢复目标域适应；η 可调保留–适应折中。

## 结论
熵引导 token 蒸馏 + 保留投影 + encoder 冻结，在 rehearsal-free 连续 ASR 适应上优于 LwF，并更好保住多语能力。η 提供显式折中控制。

## 点评
把蒸馏梯度当作可投影的保留方向，比固定 λ 的 LwF 更贴近“冲突时该保什么”的优化问题。代价是投影会牺牲新域适应（AMI WER 上升），且依赖教师在当前域输入上的输出质量；Fisher 仅支撑 encoder 冻结假设，未与 LoRA 等 PEFT 路线直接对比。
