# Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement

- 论文编号：2774
- 报告人：Buye Xu
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/fan26d_interspeech.pdf

## 问题
可穿戴端侧增强受算力与延迟约束，轻量模型场景建模弱；Knowledge Boosting 用服务器模型帮忙，但对一般语音增强增益有限，且未充分利用中间表征与混合波束成形中的空间统计。

## 方法
服务器为冻结的因果 SpatialNet；端侧为 TinyGRU+MCWF。三点协作：(a) 将延迟后的服务器增强谱拼到多通道输入；(b) 从 SpatialNet 第 0/4/8/12 层抽特征，经 1×1 压缩与延迟后用 FiLM 分层调制 TinyGRU；(c) Collaborative MCWF：边端各自估目标后算交叉协方差，用网络预测的 α(t) 融合延迟服务器统计与当前边端统计，再经可学习时变平滑求 MCWF。

## 实验与结果
DNS-Challenge 语音/噪声 + 8 通道圆阵 Pyroomacoustics 仿真；Standard SNR∈[−5,10] dB，Challenging ∈[−10,−5] dB。64 ms 延迟下，完整 (a)(b)(c) 相对 TinyGRU+MCWF：Standard SI-SDR 1.97→5.74 dB，Challenging −1.16→2.33 dB；边端仅多约 1.5% 参数、2.4% MMACs。放大 TinyGRU-Large（+198% 参数）仍远不及协作。延迟 96/128 ms 时 SI-SDR 降至约 4.39/4.26 dB，仍高于基线。

## 结论
在冻结大模型与可接受通信延迟下，延迟输出、分层特征与协方差融合可显著缩小端云差距，且边端开销很小。

## 点评
核心洞见是空间统计比谱细节更耐延迟，因而把 boosting 做到 MCWF 统计层而非只拼输出。α(t) 自适应权衡“准但旧”与“新但弱”，在突变噪声时是否足够灵敏仍依赖仿真设定；服务器仍需在线可达。
