# Branch-wise Complementary Attention for Acoustic Scene Classification

- 论文编号：865
- 报告人：Seung-Gyu Han
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/han26b_interspeech.pdf

## 问题
轻量 ASC 的多分支卷积虽扩大感受野，但分支常简单拼接/相加，未显式建模互补关系，也难补偿各核在时/频上的盲区。通用注意力多为单路径设计，难以按分支差异分配。

## 方法
在 Rep-Mobile 四分支（3×3、3×1、1×3、1×1）上引入 Branch-wise Complementary Attention（BCA）：从融合特征池化得到通道/时间/频率描述子，生成 wc、wt、wf 与联合 wctf，经 element-wise softmax 后分别加权对应分支（通道→3×3、时间→3×1、频率→1×3、联合→1×1）。另提出通道切分的 BCA-Lite 以降参。训练保留分支而不做推理重参数合并。

## 实验与结果
TAU 2020 / 2022 Mobile：BCA 准确率 72.03% / 63.24%，优于无注意力 Rep-Mobile（68.86% / 61.52%）及 SE/ECA/CTFA；参数与 MACs 仅小幅增加。BCA-Lite 略低准确率但更省算力。消融显示提出的注意力–分支分配最优；去掉任一注意力类型均降点；有效感受野面积比明显扩大。

## 结论
按感受野互补分配通道–时间–频率注意力可提升多尺度融合且开销小，适合移动端 ASC。

## 点评
设计原则清晰：给谱向分支补时间注意力、给时向分支补频率注意力。增益来自“互补分配”而非单纯加注意力，分配消融能支撑这一点。代价是推理无法像原版 Rep-Mobile 一样合并分支，部署形态与挑战赛原骨干不完全一致。
