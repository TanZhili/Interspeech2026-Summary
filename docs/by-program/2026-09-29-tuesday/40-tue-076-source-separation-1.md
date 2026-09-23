# Source Separation 1

- 日期：Tuesday 29 September 2026；时间：16:30-18:30；形式：Oral；Area：5；论文数：6
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场源分离/目标说话人提取强调模块化线索、稀疏专家效率、流式空间扫描、因果音视频蒸馏、音乐源恢复级联与困难说话人对采样。线索不再绑定单一模态：WeSep 把注册、空间、视觉、文本线索统一为可组合条件。

边缘与实时约束推动 TF-MoE、Sweep-RSE 与视觉知识蒸馏：在近似不增推理成本下扩容，或把视觉前端压缩数十倍。音乐侧把生成分布拟合与回归重建拆成两阶段；训练侧用课程困难对专门打击音色相近说话人。趋势是可组合条件 + 低延迟结构 + 针对难例的数据课程。

## 技术内容

### 可组合线索、稀疏专家与流式 ROI

**WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction**（论文 784；Ke Zhang）将 TSE 重述为异质线索条件学习，线索模块与分离骨干经标准接口解耦，支持注册/空间/视觉/文本等配置注入；实验揭示模态依赖特性，并在异质线索可用性下稳定优化。

**TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation**（论文 1307；Chenda Li）交替时向/频向 MoE，按帧或 mel 带动态选专家。基于 mel-band-splitting Conformer，在约 4.1 GMACs/s 与 BSRNN 可比成本下，Libri2Mix SDR 高约 +3.8 dB。

**Sweep-RSE: Streaming Region-of-Interest Speech Extraction in Multi-Talker Scenarios via Explicit Spatial Sweeping**（论文 1631；Hogeon Yu）全因果轻量框架，Align & Sweep 显式扫描 ROI，以相位相干锁定目标并建模空间差异拒斥离群；结合区域语音检测，约 1.66M 参数、3.05 GMACs，抑制空区误报。

### 因果音视频、音乐恢复与困难对课程

**Online Audiovisual Speaker Separation Using Efficient Visual Knowledge Distillation**（论文 1999；Cheng Yu）VKD 把因果推断的预训练视觉前端知识渐进蒸馏到轻量学生，动态加权。视觉前端体积压缩逾 48×、算力约 7.5×；结合强在线 AVSS 分离器报告因果设定 SOTA。

**DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration**（论文 2291；Gongping Huang）先用生成 DTT-BSR 拟合干净源先验，再经改版 Demucs 用时域与多分辨率谱损失增强。相对单阶段 DTT-BSR 提升各 stem 的 MMSNR，并在五 stem 上超过 X-LANCE；FAD 分解揭示重建精度与语义分布拟合的权衡。

**Adaptive Hard-Pair Sampling via Curriculum Learning for Speech Separation**（论文 3139；Xueliang Zhang）在线维护说话人对难度矩阵（SI-SDR），温度 Softmax 偏置采样难分离对。Libri2Mix 上整体改进，尤其对音色相近混合，且无额外训练开销。

## 本场要点

- WeSep 把 TSE 线索模块化，适配真实场景中线索时有时无。
- TF-MoE 与 Sweep-RSE 分别从稀疏专家与显式空间扫描服务低算力/流式部署。
- 因果 AVSS 的瓶颈常在视觉前端；VKD 大幅压缩仍保说话人判别嵌入。
- 音乐源恢复适合生成—回归级联，以平衡分布拟合与波形精度。
- 课程困难对采样直接针对相似音色这一残留难点。

## 覆盖核对

| id | title |
|---|---|
| 784 | WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction |
| 1307 | TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation |
| 1631 | Sweep-RSE: Streaming Region-of-Interest Speech Extraction in Multi-Talker Scenarios via Explicit Spatial Sweeping |
| 1999 | Online Audiovisual Speaker Separation Using Efficient Visual Knowledge Distillation |
| 2291 | DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration |
| 3139 | Adaptive Hard-Pair Sampling via Curriculum Learning for Speech Separation |
