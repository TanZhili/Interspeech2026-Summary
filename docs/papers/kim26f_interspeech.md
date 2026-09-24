# ArtBoost: Synthetic Articulatory Data Augmentation for Acoustic-to-Articulatory Inversion

- 论文编号：664
- 报告人：Hyung Kyu Kim
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26f_interspeech.pdf

## 问题
学习式 AAI 依赖昂贵稀缺的 EMA 配对数据，规模与说话人/语音多样性不足，制约数据驱动反演的扩展性。

## 方法
ArtBoost 把大规模 speech–mesh 数据（TFHP，FLAME 网格）转为伪发音监督：ASR 切分为 utterance；在网格上跟踪 UL/LL/LI 锚点均值，取突出与开口方向构成与 EMA 兼容的 12 通道目标（不可见通道置零并重采样）；先以通道掩码 MSE 在伪轨迹上预训练，再在真实 EMA 上全通道微调。可接入既有 AAI 架构，无需改模型结构。

## 实验与结果
预训练用 TFHP；微调与评估用 HPRC、USC-TIMIT，leave-one-speaker-out。相对无增强：HPRC 上 PCC 0.678→0.698、RMSE 0.736→0.717；USC-TIMIT 上 PCC 0.351→0.510、RMSE 0.864→0.792（文中亦称基线上 PCC 约 +2.9% / +45.3%）。SSL-AAI 与 SI-AAI 两架构均稳定增益；伪监督虽仅可见锚点，多发音器通道 PCC 仍提升。

## 结论
speech–mesh 可作为可扩展的发音监督来源：伪轨迹预训练加 EMA 微调可稳定提升 PCC/RMSE，并跨架构可用。

## 点评
绕开改架构，用面部网格补 EMA 稀缺，对小数据 USC-TIMIT 增益更明显。伪标签只覆盖嘴唇/下切牙，舌等不可见通道靠表征迁移，物理保真与跨说话人网格质量仍是脆弱点。
