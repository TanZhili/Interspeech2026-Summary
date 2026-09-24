# ARTT: Augmented Reverberant-Target Training for Unsupervised Monaural Speech Dereverberation

- 论文编号：1857
- 报告人：Wei-Qiang Zhang
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/song26d_interspeech.pdf

## 问题
单通道无监督去混响缺少干净参考与空间线索，属病态逆问题；WPE 难用深度先验，USDnet 等常依赖多通道约束，生成式方法算力重；Noise2Noise 式 NyTT 因混响相关卷积而难以直接套用。

## 方法
ARTT 两阶段：(1) Reverberant-Target Training（RTT）——观测混响混合再与随机统计 RTF（指数衰减扩散尾）卷积，判别式训练 DNN 重建原观测，因卷积交换律倾向同时削弱合成与真实混响；(2) mean-teacher 自蒸馏——教师吃轻噪观测，学生吃相对 RIR 卷积 + 噪声的加重腐化输入，蒸馏损失对齐教师伪标签并辅以重建观测的 \(L_{aux}\)。骨干 TF-GridNet，损失 SI-SDR-SE + 幅度 L1。

## 实验与结果
WSJ0CAM-DEREVERB 单通道：RTT 阶段 SI-SDR 3.3 / PESQ 2.18；完整 ARTT 达 7.3 / 2.61 / eSTOI 0.832，超过 WPE、单通道 USDnet、BUDDy 及监督 DNN-WPE。消融显示 \(L_{aux}\) 与噪声注入对稳定与抑噪关键；Stage II 在低 SNR 更稳。

## 结论
用“再混响→重建观测”构造监督信号，再加非对称自蒸馏，可在无干净参考下实现强单通道去混响。

## 点评
把 NyTT 思路改成相关混响增广，物理直觉清楚；Stage II 显著抬升说明仅 RTT 不够稳。评测仍在仿真基准，真实房间泛化与作者未强调的多通道潜力留待验证。
