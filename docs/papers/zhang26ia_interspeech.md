# Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting

- 论文编号：3546
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ia_interspeech.pdf

## 问题
端侧流式 KWS 要求严格因果、零 lookahead 学生模型；从非因果教师（如 AST）做中间层蒸馏时存在 causality mismatch：教师逐步特征已含未来上下文，点式回归会与学生可实现感受野冲突，损害连续长时推理鲁棒性。

## 方法
提出 Causal Temporal Relation Distillation：用无参 Adaptive Average Pooling 将师生时序特征对齐到统一长度 L（默认 24），行内 ℓ2 归一化后构造关系矩阵；对教师关系矩阵施加下三角因果掩码，只蒸馏历史拓扑（Ours）。离线双向变体 Ours-Bi 在保留 L_rel 历史锚点基础上，额外用全矩阵 L_bi 作 privileged prior。联合目标含 CE、logits KD、L_rel 与可选 L_bi；关系匹配仅离线计算，推理仍为因果 1D-CNN。

## 实验与结果
GSC v2 上，冻结 AudioSet 预训练 AST 教师（约 85M），学生约 150K/5.2M MACs。Scratch 95.12%，Vanilla KD 95.74%，Feature KD 95.45%，Relational KD 96.08%，Ours 96.53%，Ours-Bi 96.91%。流式 FRR@1.0 FA/h：Scratch 8.52%→Ours-Bi 4.15%。消融显示仅 L_bi 不如有因果锚点的组合；L=24 优于无 pooling 或过平滑的 L=12。Raspberry Pi 逐步时延约 0.15 ms，各学生变体部署成本相同。

## 结论
用因果可实现的时序拓扑蒸馏替代点式特征回归，可缓解 causality mismatch，并在闭集准确率与连续流 FRR 上取得最佳结果，且无额外部署开销。结论限于 GSC v2、AST→1D-CNN 设定。

## 点评
把“错在绝对特征含未来”转成“只对齐可实现的相对关系，再软用全拓扑”是清晰的因果蒸馏设计。强项是关系构造与推理解耦；风险在于依赖特定教师与合成流协议，且 L 的子音素尺度是否跨域通用需再验证。
