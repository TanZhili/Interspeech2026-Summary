# Learnable Schrödinger Bridge and Activations for Efficient Diffusion-based Speech Enhancement

- 论文编号：2465
- 报告人：Yihui Fu
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/fu26b_interspeech.pdf

## 问题
扩散/SB 语音增强效果好但反向过程多步、算力高；混合判别–生成可减步，但经典 SB 训练用干净语音构造边际、推理却从噪声出发，训练–推理初态不匹配，单步推理仍有空间。

## 方法
EffDiffSE+：条件 DNN 预增强 + bridge DNN 做单步 SB。提出可学习 SB：(1) 用条件 DNN 输出 ˆX_cond 替代干净语音构造条件边际，推理以复高斯 XT′=wXˆXcond+wYY+σZ（最优 T′≈0.3）作单步初态，使训练/推理匹配；(2) 两层辅助网络自适应预测 wX、wY、σ 取代固定解析式；(3) 拓扑升级：sub-pixel 上采样、Snake/SnakeBeta、条件–bridge 交互模块、子带 Conv/DeConv。损失含心理声学条件损失与波形 L1 辅助项。

## 实验与结果
URGENT 2024 数据（排除部分 CommonVoice），约 634.5 h 训练。同数据重训多基线。EffDiffSE+ 约 9.40M、3.84 GMAC/s（对比中最低），PESQ 2.58、POLQA 3.55、NISQA 4.07、ESTOI/LPS 0.84、主观 MOS 3.95（近干净 3.96），总体 rank 1.27，优于 EffDiffSE（rank 3.09）及 SGMSE+、SB、Universe++ 等。消融显示辅助网络与各拓扑逐步抬升。

## 结论
作者认为可学习 SB 初态与激活/拓扑改进能在单步、低复杂度下达到跨侵入/非侵入与主观指标的领先表现。

## 点评
关键是把“单步可行”建立在训练–推理初态对齐上，辅助网络把固定 bridge 权重变成数据自适应，再叠加工程向拓扑。对比公平性较好（同数据同步数预算）。相对多步大模型在 DNSMOS 等单项未必处处第一，但综合 rank 与 MOS 优势明确；仍依赖预增强条件分支质量。
