# HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement

- 论文编号：601
- 报告人：Jiadong Zhao
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26c_interspeech.pdf

## 问题
轻量 STFT 增强模型常按帧跑，但 50% 以上重叠使相邻帧高度相关，算力在冗余时序上浪费；直接去掉重叠又会伤质量。需要在不改 STFT/ISTFT、不增算法延迟的前提下降低 backbone 内部帧率。

## 方法
提出 HALO：因果插件，在 backbone 前用动态卷积把相邻两帧自适应融合为半帧率特征，backbone 在半帧率上增强，再用对称的动态卷积把每帧还原为原网格上的两帧。门控对 T-F bin 预测 kernel 混合权重。省下的算力用于加宽通道以匹配原 MAC/s。在 DNS3（含 DiDiSpeech 普通话）上插到 GTCRN、DPCRN 系列、LiSenNet、UL-UNAS 等。

## 实验与结果
消融：无重叠 STFT 明显掉点；固定核/抽帧/复制还原均弱于自适应 HALO。GTCRN+HALO（加宽）相对基线 PESQ 2.101→2.198、SI-SNR 11.39→11.90，MAC/s 相近。跨 backbone 在可比算力下均有提升；小模型增益更大，大模型与已高度优化的 UL-UNAS 增益变小。75% 重叠设定下 HALO 仍有效。不加宽时可将 MAC/s 从约 33.8M 降到 22.1M 且接近基线质量。

## 结论
重叠引起的时序冗余是轻量 STFT 增强的共性瓶颈；HALO 以可插拔半帧率算子释放算力并用于加宽，在不增算法延迟下稳定提点。峰值逐步算力未降，峰值感知调度留待未来。

## 点评
问题切在“架构瘦身后仍被 hop 绑死”的系统层，比再削一层更对症。自适应融合/还原比简单抽帧关键。局限是还原在同一步吐两帧，峰值算力仍高；对已很强的 NAS 骨干收益有限。
