# Physics-Informed Neural Operator for Speech Production Analysis

- 论文编号：2023
- 报告人：Kazuya Yokota
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yokota26_interspeech.pdf

## 问题
声带–声道耦合物理仿真对嗓音研究重要，但传统数值求解计算贵、逆问题需专用算法；经典 PINN 换条件需重训，难做多样声道形状的快速前向仿真。

## 方法
提出面向言语产生的 PINO（PI-DeepONet）：branch 网络输入归一化声道截面面积并输出稳态 \(f_0\)；trunk 输入时空配点。输出声带位移、声压与经硬约束耦合的体积速度（两质量模型 + 一维声道方程 + 唇辐射）。损失为声带/声道/辐射 PDE 残差加权和，无需监督仿真数据；Fourier 特征强制单周期稳态分析。

## 实验与结果
Arai 五元音 /a,i,u,e,o/ 截面，单网训练；对照 RK4-FDM。\(f_0\) 相对误差约 0.1–0.2%；声门体积流 range-normalized RMSE 约 0.36–1.23%，唇压约 1.01–5.98%（摘要称流约 0.8%、波形约 3.2%）。五元音训练约 80 小时，每元音推理均值 0.0389 s，可 GPU 并行。

## 结论
PINO 可在多种声道形状下快速输出 \(f_0\)、声门流与唇压波形。当前仅覆盖已训练形状与稳态；未来需泛化、非稳态、三维与辅音等。

## 点评
把算子学习做到耦合言语产生、用硬约束保证声门–声道耦合，避免为条件换网重训。唇压误差高于声门流，符合谱偏置对高共振峰的困难；训练成本高、仅稳态已训形状，是走向实用逆问题前的主要边界。
