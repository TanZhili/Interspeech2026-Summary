# GradHarmony: A Gradient Alignment and Magnitude Normalization Strategy for Audio Deepfake Detection

- 论文编号：2216
- 报告人：Inho Kim
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kim26r_interspeech.pdf

## 问题
音频 deepfake 检测常用多增广（如 RawBoost、RIR、MUSAN）提升泛化，但同一迭代中干净样本与多种增广样本的梯度可能方向冲突（夹角>90°）或幅度失衡，导致更新相互抵消或被某一增广主导。已有对齐方法多面向单增广或成对对齐，缺少以干净梯度为统一锚点、并同时约束幅度的多增广策略。

## 方法
GradHarmony 两步处理每个 mini-batch 中按干净/各增广类型分别回传的梯度：
1. Clean-referenced Gradient Alignment (CGA)：以干净梯度 g^(C) 为锚；仅当增广梯度与其内积为负时，用 PCGrad 式投影去掉冲突分量（也可换 GradVac），干净梯度本身不变。
2. EMA-based Magnitude Normalization (EMA-MN)：对对齐后梯度的 ℓ2 范数取中位数，再经 EMA 平滑得阈值；曾与干净梯度冲突的增广用更严阈值，其余用 α 倍阈值做裁剪缩放。最终更新为干净梯度加各归一化增广梯度之和。超参固定（β=0.99、α=2、热身 N_w=100），batch 内 50% 干净、50% 均分多增广。

## 实验与结果
在 ASVspoof 2019 LA 上训练；评测 DF21（含 hidden）、ITW、DSD、FoR。模型含 AASIST、RawNet2、RawGATST、SSL-AASIST、SSL-Conformer。相对朴素多增广，GradHarmony 普遍更好且收敛更少 epoch；摘要称两套 SOTA 模型在 OOD 上平均 EER 降约 22%。例：SSL-AASIST 在 ITW 上从增广的 11.60% 到 7.04%；AASIST FoR 从 26.67% 到 21.68%。消融显示 CGA 与 EMA-MN 互补，二者齐全最优；GradVac 作对齐算子仍有效。

## 结论
联合处理方向冲突与幅度失衡可稳定多增广训练并加速收敛；作者将自适应参考方向选择、更丰富增广设定及自适应裁剪强度列为未来工作。

## 点评
把多增广当成“共享标签、不同视图”的优化问题，用干净梯度当主方向比盲目两两 PCGrad 更贴 ADD 设定。脆弱点在于假设干净目标始终是正确锚——若干净分布本身与部署域偏差大，锚定可能固化捷径；固定 α/β 未按模型调参，极端增广强度下幅度裁剪是否仍合适有待验证。
