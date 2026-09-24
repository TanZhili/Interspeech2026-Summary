# A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration

- 论文编号：2582
- 报告人：Bunlong Lay
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lay26_interspeech.pdf

## 问题
SGMSE+ 等条件扩散用插值 SDE（iSDE）在干净语音与退化观测之间插值，无条件图像生成用的 DPM-Solver 等快速采样器不能直接套用，导致反向过程需大量 NN 评估。

## 方法
统一形式化 iSDE：均值 μ_t=(1−k(t))x_0+k(t)y，漂移 f_t=γ(t)(y−x_t)，并给出 k(t)↔γ(t) 关系及由目标方差求 g(t) 的公式；归纳 OUVE、BBED、最优传输、布朗桥等，并提出修正参数含义的 fOUVE。基于指数 Runge–Kutta，推导面向 y≠0 与 DSM/score 估计的 iSDE-pS-κ 求解器（含 κ∈[0,1] 的 PF-ODE/反向 SDE），对部分 SDE 给出权重闭式解。

## 实验与结果
在降噪、带宽扩展、去削波、MP3 解码、去混响等多恢复任务上，提出求解器约 10 次 NN 评估即可达到与自适应 RK45（>40 NFE）相近的恢复质量。

## 结论
iSDE 统一形式与专用快速求解器使条件扩散语音恢复可在少步采样下接近高阶 ODE 求解器表现，并为后续条件版 DPM 变体铺路。

## 点评
把「观测插值」从无条件高斯终点显式拆开，是把 DPM-Solver 思想迁移到 SGMSE+ 族的关键。fOUVE 修正 σ_min/σ_max 可解释性有助调参。全文实验表抽取不完整，具体客观分数以原文表格为准；算法贡献本身已较完整。
