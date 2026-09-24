# A Dynamic Knowledge Distillation Framework for Mitigating Spatial Ambiguity in Lightweight Dual-Channel Speech Enhancement

- 论文编号：1524
- 报告人：Yifei Yang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26i_interspeech.pdf

## 问题
轻量双通道 SE 靠空间线索优于单通道，但目标与干扰方位接近时空间信息失效， unconstrained 空间依赖会导致空间模糊，甚至不如单通道；既有缓解多需距离/DOA 辅助或额外模式切换开销。

## 方法
提出 Dynamic Spatial-aware Knowledge Distillation（D-SKD）：冻结单通道 SC-GTCRN 为教师，双通道 DC-GTCRN（幅度 + sin/cos IPD）为学生。Dynamic Arbitrator Module 按样本比较师生混合损失相对差距 ΔL，用 ReLU(tanh(γ·ΔL)) 得到动态蒸馏权重：仅当教师更好时蒸馏。总损失 = 任务损失 + μ·λ_dyn·蒸馏损失（均用 SI-SNR + 复谱混合损失）。推理仅保留学生，无额外参数。

## 实验与结果
DNS-3 仿真双麦 4 cm，分段角/平均角/角扫描测试。0°–15° 上 D-SKD 将 DC-GTCRN PESQ/STOI 从 1.742/71.80 提到 1.793/72.96，大角度基本保持；去掉 DAM 虽近角更好但大角度明显变差。h.size=16/32/64 及 LiSenNet、UL-UNAS 上趋势一致；h.size=32 时近角可追平单通道教师并提升其他区间。

## 结论
作者认为用空间不变单通道教师做动态仲裁蒸馏，可在无角度监督、无推理开销下缓解近角空间模糊，并适用于多种轻量双通道模型。

## 点评
把“空间不可靠时回退频谱”做成样本级门控蒸馏，比硬切换多任务更适合边缘部署。权衡是近角提升有限、强蒸馏可能伤空间能力（无 DAM 即见）；教师上限决定近角天花板。
