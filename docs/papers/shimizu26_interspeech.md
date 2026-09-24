# MeanFlow-TSE: One-Step Generative Target Speaker Extraction with Mean Flow

- 论文编号：109
- 报告人：Riki Shimizu
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shimizu26_interspeech.pdf

## 问题
扩散/流匹配生成式 TSE 质量高但需多步采样，低延迟场景难用；AD-FlowTSE 虽可少步，但标准流目标并非为真正一步推理优化。

## 方法
MeanFlow-TSE：沿 AD-FlowTSE 在背景与目标间、由混合比 λ 定义的流路径，改用 mean-flow 目标训练，使从混合物（t=λ）到目标（t=1）可一步生成。在 Libri2Mix 噪声/干净集与多 NFE 设置下对比其他生成式 TSE。

## 实验与结果
干净集 PESQ 3.26、SI-SDR 18.80 dB，超过 AD-FlowTSE；噪声集亦优。NFE 分析显示 MeanFlow 在 NFE=1 时 SI-SDR/PESQ 已接近或优于多步，适合实时。

## 结论
mean-flow 引导的一步生成可在保持分离与感知质量的同时大幅降低推理步数。

## 点评
把“能一步”从启发式少步变成目标函数层面，对助听器/通话延迟约束很关键。仍依赖注册音等辅助线索设定；与强判别式骨干的绝对差距文中以生成式对照为主。
