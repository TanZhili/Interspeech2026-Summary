# HRIR-Former: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer

- 论文编号：702
- 报告人：Shaoheng Xu
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26c_interspeech.pdf

## 问题
个性化 HRIR 测量成本高；从稀疏方向上采样时，既有学习方法多在频域、依赖最小相位或固定方向网格，损害时域保真与空间连续。需在任意目标方向做时域、无网格双耳 HRIR 重建。

## 方法
HRIR-Former：把测量/目标方向当 token，掩码补全；正弦几何编码（P=6）+ 信号投影 → Transformer 编码器（3 层，D=256，4 头）；MLP 解码全长双耳 HRIR，掩码融合保留测量点；按俯仰–方位重排后 Conv1D 时域细化；辅助 ITD/ILD 头。损失：缺失方向 Lrec + λ_HRTF 复 HRTF 损失 + λ_ITD/ILD。SONICOM（48 kHz，K=256，约 793 方向），180/20 受试者训/验；M∈{3,5,19,100} 稀疏度。指标：NMSE、CD、ITD-E、ILD-E。

## 实验与结果
相对 Nbr、HRTF-Sel、NF-CbC/LoRA、RANF 等：各 M 上 ILD-E 最优；最稀疏 M=3/5 时 ITD-E 最优（18.5/16.4 µs）。NMSE 自 −6.90 至 −10.20 dB，CD 自 0.233 至 0.102（随 M 改善）。消融（M=5）：去正弦编码劣化最大；去 ITD/ILD 头主要伤 ITD；去 Conv1D/LHRTF 均变差；最小相位预处理反而变差。

## 结论
时域无网格 Transformer 可在稀疏测量下重建任意方向 HRIR，无需最小相位假设；各模块均有贡献。未来将做听感测试。

## 点评
把 RIR 式连续空间建模迁到双耳 HRIR，并显式保 ITD/ILD，是自然且必要的扩展。与频域基线比时侧重双耳线索是公平策略；NMSE/CD 无直接跨方法对照，听感仍缺。正弦编码是无网格能力的关键。
