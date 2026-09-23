# Real-Time, Low-Latency and Edge Speech Enhancement

- 日期：Tuesday 29 September 2026；时间：16:30-18:30；形式：Oral；Area：6；论文数：6
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场统一主题是在严格算法延迟与边缘算力下做语音增强。HALO 通过减半内部帧率消除 STFT 重叠冗余；LaCo-SENet 与 LCA 框架把延迟从“因果/非因果二元”变成可配置连续谱。

传感与结构路径包括皮肤贴附加速度计 FiLM 调制、因果时频 Mamba + 渐进蒸馏，以及面向助听器的分布式双耳 RT-Tango。趋势是：同一骨干服务多延迟档、用插件/适配器切换前瞻，并借助辅助模态或状态空间模型压低内存与 MAC。

## 技术内容

### 帧率、可配置延迟与适配器

**HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement**（论文 601；Jiadong Zhao）因果插件：骨干前自适应降帧、后还原到原 STFT 网格，算法延迟不增。DNS3 上在匹配复杂度下对多种轻量模型一致增益，省下的预算可用于加宽通道。

**Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding**（论文 817；Yunsik Kim）LaCo-SENet 用非对称时间填充与双缓冲流式（状态缓冲 + 前瞻缓冲），并选择性更新以防未来帧泄漏。固定约 1.37M 参数骨干覆盖 12.5–75.0 ms；12.5 ms 全因果 PESQ 3.35，不低于此前 46.5 ms 因果 SOTA 的 3.27。

**Latency Controllable Speech Enhancement**（论文 2997；Hiroshi Sato）因果增强模型加 Latency Control Adapters，一批内多延迟训练使单模型支持七档延迟；相对每延迟独立模型质量更好，推理 MAC 恒定，存储参数减 76%。

### 边缘多模态、状态空间与双耳助听

**Real-Time Speech Enhancement on Edge Devices Guided by Harmonic and Voice-Activity Cues Utilizing Skin-Attachable Accelerometer**（论文 3119；Yonghun Song）LAU-NetV2 把 ACC 压成嗓音活动与谱谐波线索，经 FiLM 调制时频特征；约 46k 参数（较先前多模态少约 68×）。TAPS+DNS 上 PESQ 由 1.78 升至 2.78；可穿戴 MCU 原型运行约 48.66 ms。

**RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation**（论文 3197；Sung-Feng Huang）全因果时频 Mamba，固定大小循环状态利于长语音。渐进 KD 把 8 层教师压到 1 层学生。Voicebank-DEMAND 上 8 层在 25 ms 延迟约束下 PESQ 3.32；1 层学生由 3.06 升至 3.18，相对教师约 2.75× 加速且稳态 RTF 不变。

**RT-Tango: Real-Time Distributed Binaural Speech Enhancement for Low-Power Hearing Aid Devices**（论文 3301；Zahra Benslimane）两阶段分布式架构：ERB 特征压缩、分组循环掩码估计与时间稀疏化；非对称 STFT 解耦谱分辨率与算法延迟。报告竞争增强质量同时显著降 MAC，并可低至约 8 ms 超低延迟运行。

## 本场要点

- 重叠 STFT 冗余可用半帧率插件回收算力而不增算法延迟。
- 非对称填充/LCA 使单模型覆盖从十余毫秒到数十/上百毫秒延迟档。
- 皮肤加速度计以廉价 FiLM 线索替代重型并行多模态编码。
- 因果 Mamba + 渐进蒸馏兼顾长序列状态效率与浅层部署。
- RT-Tango 把双耳助听的延迟、算力与设备间通信一并纳入设计。

## 覆盖核对

| id | title |
|---|---|
| 601 | HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement |
| 817 | Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding |
| 2997 | Latency Controllable Speech Enhancement |
| 3119 | Real-Time Speech Enhancement on Edge Devices Guided by Harmonic and Voice-Activity Cues Utilizing Skin-Attachable Accelerometer |
| 3197 | RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation |
| 3301 | RT-Tango: Real-Time Distributed Binaural Speech Enhancement for Low-Power Hearing Aid Devices |
