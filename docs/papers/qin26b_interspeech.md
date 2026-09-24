# Domain-Adaptive Dual-Gating Mixture of Experts for Generalizable Speech Deepfake Detection

- 论文编号：1778
- 报告人：Zhe LI
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qin26b_interspeech.pdf

## 问题
MoE 有助 SDD 泛化，但现有门控多为通用 FFN，忽略深度伪造的声学/时序伪迹，难以把不同攻击模式路由到专长专家。

## 方法
DADG-MoE：双门控对原始波形与 XLSR SSL 特征分别用 Sinc / depthwise Sinc 滤波提取伪迹，再结合可学习域原型生成路由权重；专家为极轻量仿射（BN 的 γ/β）。Top-k 聚合后接 AASIST。在 ASVspoof2019 LA 训练，测 21DF、ITW、FoR、ADD2023。

## 实验与结果
相对 XLSR-AASIST：21DF 3.69→2.54（−31.2%）、ITW 10.46→6.35（−39.3%）、FoR 7.47→4.42（−40.8%相对）。仅增约 0.17M 参数。消融：去掉 Raw-Gating 掉点最大；原型与 SSL-Gating 对域外重要。top-k=2 较稳。

## 结论
语音特异双门控 + 域原型 + 仿射专家，能以极低参数代价提升未见攻击/条件泛化。

## 点评
门控真正“听”伪迹而不是只看高层嵌入，方向正确；仿射专家把域差异压到统计仿射上，解释与效率兼顾。与通用 MoE 基线对比仍偏少，但相对强基线增益清晰。
