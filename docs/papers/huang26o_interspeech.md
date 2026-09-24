# Neural Directional Coding: Joint Spatial Coding and Filtering with Configurable Directivity Patterns

- 论文编号：2234
- 报告人：Weilong Huang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26o_interspeech.pdf

## 问题
通信接收端常需可配置指向性空间处理，但传全阵列代价高；级联 SpatialCodec 重建全通道再做 UNDF 参数量大、码率高，不够高效。

## 方法
提出 Neural Directional Coding（NDC）：参考通道用 EVS（12.8 kbps）传输；阵列空间信息经 SpatialCodec 式编码器–RVQ–解码器压成低维侧信息。接收端 FiLM-JNF 估计模块结合可配置指向性向量 Λt，输出复掩码乘参考通道得到虚拟指向麦信号。两阶段训练：先用一阶 Cardioid 多样源–阵几何预训练编码，再冻结编码器/量化器、用多样 μ/θs/J 模式训解码与滤波。可选输入归一化仅保留通道间幅度/相位差。

## 实验与结果
4 麦（3 cm UCA+中心参考）、16 kHz、无回声仿真。0.25 kbps/1.4M 参数 NDC 在多种未见高阶指向性上 SDR/PESQ 优于同码率 SpatialCodec+UNDF，并多数超过 7.5 kbps/90.8M 级联基线与 oracle-DOA 参数滤波。归一化输入差距小，说明比特主要用于空间信息；无预训练变差。低混响动态场景中仍能抑制移动干扰。

## 结论
作者认为联合空间编码与可配置指向性滤波，可用极低侧信息码率与轻量模型近似虚拟指向麦，优于“全重建再滤波”管线。

## 点评
把 DirAC 思路神经化并与 UNDF 联合优化，码率–参数优势非常突出。主要在无回声、共面源设定训练，混响/移动仅为定性推广；参考通道仍占 12.8 kbps，总链路码率需一并考虑。
