# A Sparsity-Aware Robust Nonlinear Active Noise Control for Impulsive Noise Environments

- 论文编号：122
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26_interspeech.pdf

## 问题
FLN 非线性 ANC 扩展基函数冗余，抬高过量 MSE、收窄稳定步长；MOV-FsLMP 虽抗冲击并约束输出功率，仍缺乏在线特征选择。

## 方法
在 MOV-FsLMP 代价上加 RZA（对数和近似 L0）正则：Jprop = E[|e|^p]+λE[y²]+ρrza Σ log(1+ε|wi|)；更新含鲁棒 Lp 项、输出约束与逐元素零吸引。理论指出稀疏剪枝降低有效输入能量、扩大 μmax。仿真：α=1.6 SαS 冲击、非线性主路径、三角 FLN（P=3），对比 FxLMS/FsLMS/MOV-FsLMP。

## 实验与结果
最优步长下稳态 MSE 较基线约低 1–2 dB。大步长 μ=0.02 时基线边缘发散，所提方法仍收敛至约 −6.5～−3 dB。稳定性扫描显示可容忍更大 μ；摘要亦报告相同配置下更高 ANR。复杂度仍 O(L)。

## 结论
稀疏感知 MOV-FsLMP 可在冲击噪声与非线性下同时改善稳态误差与稳定域，适合实用非线性 ANC。

## 点评
把“FLN 过参数化”当作与冲击鲁棒同等重要的问题，用 RZA 做在线剪枝，设计简洁。结论主要来自合成路径仿真，真实扬声器饱和与声学二次路径的外推还需实测。
