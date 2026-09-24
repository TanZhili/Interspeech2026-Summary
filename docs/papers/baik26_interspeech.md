# DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition

- 论文编号：3232
- 报告人：Jaeeun Baik
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/baik26_interspeech.pdf

## 问题
噪声增强微调常在干净条件掉点并过拟合特定噪声；需在提升噪声稳健的同时保住干净识别。

## 方法
DASH：双分支自蒸馏——干净教师（EMA）与噪声学生；多层编码器隐表示经投影与原型（k-means）分配，用温度 KL 对齐干净–噪声视图。两阶段：无标签蒸馏预训练（约 5k 步，~4% 微调时长）再标准 ASR 微调。骨干 Parakeet-TDT-CTC-110m；噪声视图默认 SpecAugment+加性噪声。

## 实验与结果
相对仅微调，DASH 在 test-clean/other 与多种 SNR 噪声上更优（如 clean 2.02 / other 4.25 vs 基线 2.58/5.41、仅微调 2.14/4.40），并缓解干净–噪声折中。多层蒸馏优于仅末层；EMA 更新有益。Noisy→Clean 配置显示蒸馏阶段本身可赋予噪声不变性。

## 结论
多层原型自蒸馏能以很小开销学习干净–噪声一致性，提升稳健性且不牺牲干净精度。

## 点评
把稳健性做成标签无关预训练阶段，避开与 ASR 损失联合优化的干扰，工程上干净。噪声类型仍偏仿真混合；与 VIC/CR-CTC 等一致性方法的直接头对头对比可再加强。
