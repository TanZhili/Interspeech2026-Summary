# Uncovering Dimension-Specific Layer Preferences in Wav2Vec2 for Fine-Grained Perceptual Assessment of Dysarthric Speech

- 论文编号：692
- 报告人：Zihan Zhong
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhong26_interspeech.pdf

## 问题
构音障碍细粒度评估需覆盖 Darley–Aronson–Brown（DAB）多维感知评分，但现有工作常默认取 Wav2Vec2 最后一层特征，可能丢掉与特定言语子系统相关的信息；公开细粒度标注也稀缺。

## 方法
两阶段：Stage-1 在 SAP 未标注数据上对 Wav2Vec2-Large 做 LoRA 无监督域适应（对比掩码预测，约 9.4M 可训参数）；Stage-2 冻结编码器，在 25 个样本≥1000 的 DAB 维上用 CORAL 序数损失做线性探针与可学习 scalar mixing。探针扫全部 25 层（含 CNN）；mixing 用 softmax 层权融合，经 Conv1d neck 后接各维 CORAL 头，比较全局共享权（c=1）与每维独立权（c=25）。自建说话人无关 Train/Dev/Test：8637/1029/1392 句。

## 实验与结果
LoRA 在 23/25 层改善平均 MAE、21/25 层改善 Spearman；最后一层几乎从不是最优。最佳单层+neck 约 MAE 0.46、ρ 0.41；scalar mix（c=1）达 MAE 0.429、ρ 0.464，c=25 平均接近且在 Pitch breaks、Audible inspiration 等事件维上更好。全局混合权峰值在层 4–9；按子系统看，发声偏早层、共鸣偏早中层、构音/整体结果偏中上层，韵律–时间维层偏好最分散。部分维（如 Pitch level、Nasal emission）相关仍很低。

## 结论
LoRA 域适应提升病理表征；25 维 DAB 的最优层因维而异，可学习多层融合优于单层选择，且学到的层偏好与临床言语子系统及 SSL 可解释性结论大致一致。

## 点评
把“用哪一层”从默认最后一层改成维度相关的软混合，对多目标临床评估很贴题。标签高度偏正常/轻度、以及均值池化对时间结构弱，解释了若干维的低相关；全文结尾在抽取中截断，但核心结果与结论段落已足够支撑上述判断。
