# LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression

- 论文编号：191
- 报告人：Chengwei Liu
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26b_interspeech.pdf

## 问题
全双工对话中硬件时延/能量失配与非线性回声使联合 AEC+NS 困难；端到端网络缺少显式多路径对齐，过抑制又伤下游 ASR/VAD。

## 方法
LMPAN：LAEC（子带 TDE+NLMS）+ 三条软时间对齐与能量补偿（ref–mic、mic–LAEC、ref–LAEC）+ GTCRN 精炼 + 注意力融合 LAEC/mic + 残差缩放后处理。动态目标按目标 SNR/SER 保留受控噪声/回声残差。两阶段训练：先对齐 WavLM 表征，再联合谱/回声/SI-SNR/PMSQE（SSL 作正则）。约 480K 参数、126M MACs。

## 实验与结果
AEC Challenge 2023：完整 STL 配置 MOS_avg 4.49（DT EMOS 4.63），可比 DeepVQE-S 且更轻。真实双讲下游：加 DTA 后低 SER 段 WER/DCF/TIR 显著改善（如 SER[−20,−15] WER 24.25→14.38）。消融显示对齐与注意力融合逐步抬升；SER_t=25 dB 对 ASR 最友好。

## 结论
显式多路径对齐、自适应融合与动态目标可在轻量预算下兼顾回声抑制与下游任务保真，适合端侧全双工对话。

## 点评
把“对齐/融合/不过抑”拆成可消融模块，并直接用 ASR/VAD/打断率衡量，比只报 AECMOS 更贴近产品。LAEC 仍作支路而非唯一依赖，设计稳健；最终 AECMOS 最优与下游最优配置略有分歧，需按任务选点。
