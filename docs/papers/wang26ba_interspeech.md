# Optimal Source Placement for TDoA-based Geometry Calibration of Distributed Microphone Arrays

- 论文编号：1691
- 报告人：Xu Wang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26ba_interspeech.pdf

## 问题
分布式麦阵几何自标定常用随机校准声源，相对几何可导致较高 CRLB；若声源位置可控（如移动机器人），如何放置以提升标定精度仍开放。

## 方法
在含 capture time offset（CTO）的 TDoA 模型下推导几何标定 FIM/CRLB，再在房间盒约束内最小化 CRLB 迹得到最优声源位置（一阶段联合优化，SPSA-Adam + 投影）。多阶段方案先联合优化 K=4 个最小可辨识声源，再逐个追加，以降复杂度；并给出 3D 扩展与复杂度分析。实践中用粗估麦位置代替真值构造目标。

## 实验与结果
相对随机放置，一阶段在不同 σd 下 MSEr/MSEδ 更低，且对麦位置初值误差不敏感（σr 至 1 m 时 MSEr 仅增约 0.0034 m²）。声学仿真（GCC-PHAT、RT60=0.3 s、SNR=15 dB、M=N=10）：一阶段 MSEr=0.0489 vs 随机 0.240；多阶段随 K 增大精度逼近一阶段、耗时更短。不同 RT60/SNR 下 one-stage 仍优于随机。

## 结论
最小化含 CTO 的 TDoA CRLB 可指导校准声源放置；多阶段适合算力受限场景。未来将考虑 TDoA 异常值。

## 点评
把“声源放哪”明确成 CRLB 优化，补上标定侧最优放置空白。依赖粗麦位与盒约束，工程上合理；真实机器人路径、障碍与异常 TDoA 会进一步约束可行域。
