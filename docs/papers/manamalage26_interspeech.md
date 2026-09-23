# FedMPA: A Novel Privacy-Performance Optimization Approach for Multimodal Speech-Based Depression Detection

- 论文编号：586
- 报告人：Dushanthi Madhushika Manamalage
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/manamalage26_interspeech.pdf

## 问题
基于语音的抑郁症检测需兼顾性能与隐私；联邦学习下多模态非 IID、成员推理泄漏与相对中心化的性能落差同时存在，且鲜有量化隐私–性能权衡的指标。

## 方法
FedMPA：在 ALiDeR 上扩展模态特异类原型（文本/音频/融合）、EMA 稳定全局原型库、原型拉取+排斥损失、原型相似度加权聚合，以及 softmax–原型混合推理（低置信时 defer 到原型分类）。提出 PPS：UAR 与基于 MIA 置信 AUC 的隐私分的调和平均。

## 实验与结果
E-DAIC 上，完整损失组合达 UAR 0.89；混合推理优于纯 softmax/纯原型。对比 FedAvg/FedProx/FedProto/FedGPD 与中心化 ALiDeR：FedMPA 获最高 PPS 0.92（UAR 0.89，MIA_conf_AUC≈0.52），中心化 UAR 更高（0.92）但隐私更差（PPS 0.88）。

## 结论
模态特异原型对齐与混合推理可在联邦抑郁检测中同时提升效用与抗成员推理能力，并用 PPS 显式度量权衡。

## 点评
把“多模态非对齐 + 隐私–性能”做成可优化目标是贡献点。评估仍限 E-DAIC 与黑盒置信 MIA，未包含差分隐私等显式防护；原型假设两类抑郁标签空间，对更细严重度回归未展开。
