# Trajectory Variance: An Unsupervised Measure of Developmental Vocal Plasticity in Birdsong

- 论文编号：3557
- 报告人：Kanghwi Lee
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lee26z_interspeech.pdf

## 问题
鸟鸣发育中，静态声学描述只能刻画某一时刻的声音，无法回答“若在另一发育年龄发出，会差多少”。需要无需类型标签的逐发声可塑性度量，以区分学习性音节与先天叫声等发育动态。

## 方法
对每只鸟独立训练谱图 VAE（123×100→128 维 latent）。因无纵向同发声轨迹，用 minibatch OT（Hungarian）构造跨年龄训练对；6 层 AdaLN 残差 MLP 学习年龄条件位移 δ，一次前向得到反事实 latent：z_cf = z_src + f_θ(z_src, a_src, a_tgt)。对每条发声在 T=7 个均匀目标年龄生成反事实，定义 trajectory variance 为各维跨年龄方差之和。用 bout 启发式（间隙 <200 ms 且 bout≥3 标为 song）做 song/call 标签，避免与谱特征循环。

## 实验与结果
三只斑胸草雀（183K–274K 发声，40–101 dph）。duration-残差后 song/call：Cohen’s d_r=0.29–0.57，AUC=0.58–0.67；Gaussian OT、per-age k-NN、per-age OT 均不能在全部鸟上一致分离。轨迹方差与谱平坦度负相关（r=−0.48 至 −0.75），与时长正相关（r=0.70–0.80，故报告残差化指标）。解码反事实 FAD 0.01–0.06（仅作解码诊断）。

## 结论
学习到的位移模型可在无类型标签下提供发育可塑性分数，并与经典谱描述对齐；局限包括无纵向真值、时长混淆需残差化、标签启发式偏差，以及仅三只同种鸟、外推未验证。

## 点评
把单细胞 OT/反事实思路迁到鸟鸣发育，度量目标清晰：预测变化量而非分类。强在对非参数基线的系统对照；证据仍是横截面人口匹配，个体真实轨迹不可验证，且 AUC 仅中等，更适合作为可塑性探针而非部署级分类器。
