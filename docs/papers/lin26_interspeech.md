# Progressive Learnable Counterfactual Attention for Music Classification

- 论文编号：147
- 报告人：Yi-Xing Lin
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26_interspeech.pdf

## 问题

音乐分类中注意力常只靠分类损失弱监督，易被伪相关与数据集偏差带偏。LCA 用可学习反事实分支暴露误导性区域，但在单一表示空间中残余偏差仍可能与主注意力纠缠，难以彻底解耦。

## 方法

提出 Progressive Learnable Counterfactual Attention（P-LCA）：在 genreMERT（或 Short-chunk ResNet）的 LCA 之上做 K 阶段精炼。每阶段在当前表示上跑主分支与反事实分支，用与 LCA 相同的一组损失；阶段结束后把主分支注意力条件特征经共享的 stage-wise representation projection 投影到新潜空间，作为下一阶段输入，并用正弦 stage embedding 区分阶段、共享注意力参数。推理时丢弃反事实分支。总损失为各阶段损失加权求和。

## 实验与结果

任务：Artist20 歌手识别（SID）、GTZAN 流派（MGC）、EMOPIA 情感（MER）。SID 消融中 K=3 最佳；genreMERT(w/ P-LCA) 帧级 F1 Avg/Best 0.70/0.73、歌曲级 0.88/0.94，优于 LCA。去投影模块或仅增大 LCA 容量均无明显增益。MGC：帧/歌曲 Acc 0.91/0.94（LCA 为 0.89/0.92）。MER（Short-chunk ResNet）：4Q/Arousal/Valence Acc 0.78/0.92/0.84，高于 LCA 的 0.76/0.92/0.82。可视化显示主注意力更聚焦，反事实更弥散。

## 结论

作者认为分阶段投影能从不同表示视角反复暴露并抑制残余注意力偏差，在多种音乐分类任务上稳定优于单阶段 LCA，且增益来自结构而非单纯参数量。

## 点评

做法针对的是“偏差与任务线索在同一特征空间不可分”：用投影换视角再做一轮反事实竞争，比加深单阶段 LCA 更对症。阶段数有最优值（文中 K=3），过多可能过拟合或稀释监督；目标与超参基本沿用 LCA，跨架构适用性已在 ResNet 上验证，但训练目标组合较重，落地时调参成本不低。
