# Robust Multi-Source-Free Domain Adaptation via Posterior Adjustment and Label Agreement

- 论文编号：370
- 报告人：Hoyoung Yoon
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yoon26_interspeech.pdf

## 问题
声学场景分类跨设备部署时，隐私与传输限制导致无法共享源数据；多源无源域适应（MSFDA）又受麦克风响应造成的类别预测偏置、以及置信度不可靠困扰。仅 AdaBN 对齐特征统计仍留显著标签偏置。

## 方法
FASOLA：对 K 个冻结源模型，(1) 后验调整——用目标上的边际预测 ˆp_k 与动量估计目标先验 ˆq，校准 logits ˜z = z − τ(log ˆp − log ˆq)；(2) 标签一致性——用留一式多数一致率 s_k 作权重（softmax(γ s)），再加权聚合。先可做 AdaBN。评测 DCASE 2020 Task 1A，Leave-One-Domain-Out（目标为模拟设备 S1–S6），骨干 CP-ResNet；对比 Oracle、Uniform、DECISION、CAiDA、DATE、Bi-ATEN。

## 实验与结果
平均 Acc/F1：FASOLA 54.43/54.04，优于 Uniform 50.68/49.89 与最强基线 DECISION 约 51.88/51.16。消融（S6）：PA/LA 各自有益，完整最好。随机降采样类别时 ˆq 更贴近真先验。权重与真目标准确率相关：r=0.9365、ρ=0.9286，高于 DECISION 等。

## 结论
后验校准 + 一致性加权可在无源数据下缓解设备异质引起的偏置并选出可靠源，稳健于标签分布偏移；未来拟做在线流式、摆脱全局统计依赖。

## 点评
把“设备偏置=标签偏置”说清楚，用先验对齐替代置信度加权，切中 MSFDA 痛点。动量先验与一致性权重形成闭环；仍依赖整批目标统计，边缘实时场景需再简化。会话主题是 Spatial Audio，但内容属 ASC 域适应——按 batch 元数据写程序字段即可。
