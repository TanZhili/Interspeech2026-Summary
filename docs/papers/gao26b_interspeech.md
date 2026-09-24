# HistoMatch: Unified Transient-Steady Assessment for Noise-Robust Semi-Supervised Speaker Verification

- 论文编号：244
- 报告人：Shenghan Gao
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26b_interspeech.pdf

## 问题
半监督说话人验证的伪标签筛选多依赖瞬时置信度阈值，但随机切段与噪声增强易导致预测漂移，伪标签利用率低；*Match 范式在 SV 上增益有限。

## 方法
提出 HistoMatch：在 FixMatch 风格流程上用 AAM 替代 CE。Dual-state History-based Stability Evaluator（DHSE）联合瞬态过滤（弱增强上 max(p)≥T）与稳态过滤（近 K 个 epoch 历史预测直方图最大同类计数 S≥阈值，用于召回置信度不够但历史稳定的样本）；阈值由 EMA 自适应更新。有标与筛后无标样本均用 AAM 损失。

## 实验与结果
VoxCeleb2 训练，每说话人 4/10/20 条为有标；ECAPA-L。20 条/人时 O/E/H EER 达 0.91%/1.13%/2.13%，接近全监督（0.87%/1.12%/2.12%），并优于 FixMatch/FlexMatch/SpeakerMatch 等。ECAPA-S、10 条/人消融：仅瞬态 1.87%、仅稳态 1.22%、双态 1.08%。

## 结论
作者认为瞬态–稳态双阈值可回收因切段/噪声导致置信度失败的优质伪标签，半监督性能逼近全监督并达所报告设定下的 SOTA。

## 点评
把“历史一致性”升为与置信度并列的稳态指标，切中 SV 强增强带来的标签抖动。有标预算固定、骨干统一，对比干净；对历史队列长度 K 与早期噪声累积的敏感性正文着墨较少。
