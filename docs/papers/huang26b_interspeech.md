# GISNO: Neural Operator-based HRTF Personalization from 3D Meshes via Differentiable Helmholtz Rendering

- 论文编号：366
- 报告人：Liming Shi
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/huang26b_interspeech.pdf

## 问题
个性化 HRTF 测量成本高；数据驱动方法常绑死离散方向网格，且把不规则 3D 网格重采样到规则网格会抹掉耳廓细结构。需要能从 3D 头模直接到连续声场、并支持任意方向/距离/频率查询的方法。

## 方法
GISNO 将 HRTF 预测写成边界复压强场上的算子学习：GNO 编码器把网格几何特征（面积元、法向、源相对位置等）投影到球面潜网格（耳间坐标系+表面锚点邻域），SFNO 块做球谐域全局散射映射，解码回网格边界压强；再经可微 Helmholtz 积分渲染到任意场点得到 HRTF。训练最小化场点复压强 NMSE；利用声学互易，每受试者双耳各一次前向即可渲染多方向。

## 实验与结果
HUTUBS：40 训练 / 15 测试；法向高斯扰动增广至 160 网格。相对 DNN-PCA/VAE/SHT/CAE 等人体测量基线，LSD 均值 2.92 dB（对比约 4.29–5.27 dB）。零样本测试：训练在 1.2 m、1550 点、Δf=150 Hz 的 Mesh2HRTF 仿真，测试 1.5 m、7800 点、Δf=100 Hz；1 kHz 球面上归一化幅度误差均值 0.0139。

## 结论
作者认为神经算子 + Helmholtz 渲染可在保留网格形态细节的同时实现物理一致、可任意分辨率查询的 HRTF 个性化，并展现空间超分、径向外推与频谱细化的零样本能力。局限是 HUTUBS 规模小、零样本主要在仿真数据上验证。

## 点评
把“学边界算子、积分求场”写进端到端训练，比直接回归离散 HRTF 网格更有物理归纳偏置，也自然解释多维零样本。与人体测量基线的 LSD 优势明显，但未与近期 mesh 方法同协议对比；刚性声硬边界假设与仿真零样本仍可能高估真实测量场景的泛化。
