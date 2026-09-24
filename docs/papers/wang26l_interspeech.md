# An All-neural Distributed Filtering Algorithm for Speech Extraction in Wireless Acoustic Sensor Networks

- 论文编号：648
- 报告人：Jiawei Wang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26l_interspeech.pdf

## 问题
无线声学传感器网络（WASN）可用分布式压缩交换（如 DANSE）避免集中式聚合，但基于协方差迭代的滤波在低 SNR、非平稳噪声下脆弱；现有深度方法多只做掩码前端，核心仍依赖线性滤波与矩阵求逆。

## 方法
提出 ANDFilter：端到端神经分布式滤波，通信协议与 DANSE 一致（每节点广播一个压缩标量）。三模块：SNFM（U²-Encoder + S-TCN + Decoder + LSTM 滤波器映射）由本地多通道观测量直接合成局部复滤波器并产生压缩信号；NSM 以本地为 query、远端压缩为 key/value，余弦注意力自适应加权；MNFM 结构同 SNFM，在本地观测与精炼压缩信号上合成全局滤波器。损失为 SNFM/MNFM 的 RI–幅度混合损失加 NSM 熵正则。

## 实验与结果
Pyroomacoustics 仿真 4 节点×4 麦十字阵，LibriSpeech 干净语音 + Freesound 噪声，16 kHz。消融：完整 ANDFilter PESQ/ESTOI 2.86/0.83，优于 SNFM+MNFM（2.80/0.82）与 DANSE（1.44/0.61）。相对 C-MWF、DANSE、C/D-PEVD、TANGO，在各 SNR 段均最优，平均 PESQ/ESTOI/DNSMOS 为 2.86/0.83/2.60。

## 结论
作者认为用结构化神经模块直接合成分布式滤波器，可在有限带宽下摆脱协方差迭代，于低 SNR 与非平稳条件更稳健。

## 点评
把 DANSE 两阶段结构“神经化”且保留可解释通信形式，相对掩码+传统滤波的混合系统更彻底。证据几乎全在仿真 WASN，真实无线同步/丢包/时钟偏差未覆盖；节点数固定为 4，规模扩展性仍待检验。
