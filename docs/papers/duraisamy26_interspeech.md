# Subject-Invariant Dynamic Graph Modeling for Cross-Subject EEG Imagined Speech Decoding

- 论文编号：2884
- 报告人：Saravanakumar Duraisamy
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/duraisamy26_interspeech.pdf

## 问题
EEG 想象言语跨被试泛化差：Transformer 常把电极当可交换 token，忽略拓扑与动态连接，且任务特征易与被试特异性纠缠，LOSO 下常近随机。

## 方法
在预训练 EEG Transformer（如 EEGPT）上做电极对齐池化；按短窗估计多视图动态连接先验（空间/PLV/相干/包络相关等）注入图偏置注意力；用梯度反转层做对抗被试解缠。两套公开 15 人五词想象言语数据（BCI 2020 与 overt/covert 中的 covert），严格 LOSO。

## 实验与结果
完整模型两数据集平均准确率 31.20%±3.12% 与 30.36%±4.05%，高于仅 Transformer 基线（约 20%）及多种常规基线；图先验与 GRL 消融均有贡献，动态先验优于静态；α≈0.5、收缩 ρ=0.2 较稳。

## 结论
结构化动态连接建模加被试不变训练可在严格 LOSO 下改善想象言语 EEG 解码，尽管绝对准确率仍有限。

## 点评
把“电极拓扑 + 动态连接 + 对抗去身份”对上 LOSO 失败模式，问题抓得准。强在双数据集一致增益；弱在五类准确率仍偏低、临床可用性远，且依赖预训练骨干质量。
