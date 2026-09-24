# From Bilevel to Trilevel: Joint Training for Speech Recognition

- 论文编号：1738
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26b_interspeech.pdf

## 问题
ASR 常用“无监督预训练 + 监督蒸馏微调”两阶段流程，预训练损失在微调时被丢弃，易遗忘或负迁移；既有双层优化（如 BL-JUST）联合监督与无监督，但仍缺少知识蒸馏这一层。

## 方法
提出 TL-SUD：三层嵌套优化——上层监督损失 L_sup（标注数据）、中层无监督 L_unsup、下层蒸馏 L_KD（标注+无标注，蒸馏时不用真标签）。将中下两层折叠成双层子问题，用惩罚型双层梯度下降（PBGD）两次，得到共享骨干 θ 与各任务头 ϕ/η/ψ 的嵌套更新；惩罚系数 γ1、γ2 随 epoch 从 0 退火升至最大值。实现上 FastConformer 学生（115M，17 块）用 CTC 监督、对比无监督、特征级蒸馏；教师更大 FastConformer（616M）。

## 实验与结果
LibriSpeech：unlabeled=train-other-500，labeled=train-clean-100 时，TL-SUD test-clean/other 6.7/15.9，优于 PT(U)+FT(SD) 7.4/19.5、加权求和 7.4/19.1、监督基线 8.7/23.0。相对 BL-JUST（无 KD）在 100/200/360h 标注上均更低 WER（如 100h：6.7/15.9 vs 7.0/17.1）。惩罚日程敏感，最佳约 γ1 max=180、γ2 max=0.005。解码为无外部 LM 的 greedy。

## 结论
把监督、无监督与蒸馏纳入可训练的三层优化，能比两阶段与双层 JUST 更一致地利用三类信号，并在低资源标注设定下降低 WER。

## 点评
做法把“遗忘预训练语义”的管线问题改成嵌套可行集约束，KD 放最底层注入教师先验。工程关键是惩罚调度；调不好会破坏三目标平衡。评价刻意去掉 LM，突出优化本身，但绝对数字与带 LM 系统不可直接比。
