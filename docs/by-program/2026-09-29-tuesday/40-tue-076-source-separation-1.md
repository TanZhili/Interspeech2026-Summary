# Source Separation 1

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场源分离/目标说话人提取强调模块化线索、稀疏专家效率、流式空间扫描、因果音视频蒸馏、音乐源恢复级联与困难说话人对采样。线索不再绑定单一模态：WeSep 把注册、空间、视觉、文本线索统一为可组合条件。

边缘与实时约束推动 TF-MoE、Sweep-RSE 与视觉知识蒸馏：在近似不增推理成本下扩容，或把视觉前端压缩数十倍。音乐侧把生成分布拟合与回归重建拆成两阶段；训练侧用课程困难对专门打击音色相近说话人。趋势是可组合条件 + 低延迟结构 + 针对难例的数据课程。

## 论文技术总结

# WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction

- 论文编号：784
- 报告人：Ke Zhang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26k_interspeech.pdf

## 问题
Target Speaker Extraction（TSE）依赖注册语音、空间、视觉或文本等辅助线索，但现有系统多为单线索、架构与训练管道紧耦合，难以在线索可用性动态变化时做系统组合与对比。作者要把 TSE 重述为异构线索条件学习，并给出可配置的模块化框架 WeSep。

## 方法
WeSep 将数据抽象、线索 frontend、分离 backbone 与 Top Model 组合解耦：mix–target 对从模态仓库按 ID 取线索，batch 内可有不同线索子集；frontend 覆盖 speaker（USEF、TF-Map、Contextual、speaker emb 等）、spatial（IPD/ΔSTFT/SDF/CDF、embedding）、visual（MuSE 风格 viseme）、textual（DAE-TSE 式关键词音素编码）；backbone 可选 Conv-TasNet、DPCCN、BSRNN、TF-GridNet、NBC2 等，经标准化接口注入。默认以 BSRNN 在 3 s 段上训 150 epoch，目标为负 SI-SNR，指标 SI-SDRi；并支持因果化与缺失线索零填充的异构训练。

## 实验与结果
Libri2Mix-100：speaker 特征中 USEF+Context 达 16.56 dB SI-SDRi / 98.05% accuracy（SI-SDRi>1 dB），优于纯 speaker emb（13.17 / 92.08）；因果版同配置 14.15 / 95.93，理论延迟 32 ms。多通道混响数据上，handcraft 空间特征（CDF+SDF+IPD+ΔSTFT）在 BSRNN/NBC2 上分别 14.24 / 17.49 dB，优于 embedding 式空间先验。文本关键词（DAE-TSE）16.45 dB，接近最佳音频注册。VoxCeleb2-mix 上 BSRNN+视觉 12.81 dB，高于原 MuSE 的 11.67。注册+空间联合 14.67 dB，优于单线索；异构缺失训练下 Spatial+Speaker / Spatial / Speaker 分别为 13.51 / 12.61 / 10.01 dB，无崩溃。

## 结论
贡献不在新分离网络，而在把线索粒度、跨模态组合与缺失可用性放进同一优化框架，使 TSE 可系统研究并更接近真实选择性收听。工具已开源。

## 点评
这是基础设施向论文：用统一接口把“换线索=换整条管线”变成配置问题，实验表格也因此能在同 backbone 下公平扫特征族。强项是 intra-modal 组合与 missing-cue 零填充都能跑通；若要推到真实部署，还需看异构训练对“全线索最优”是否有代价，以及视觉/文本设定与注册设定在数据分布上的可比性边界。


# TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation

- 论文编号：1307
- 报告人：Chenda Li
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/hu26d_interspeech.pdf

## 问题
边缘部署的语音分离模型参数往往不大，但算力（GMACs/s）很高；简单缩隐藏维度会伤容量。作者要用稀疏 Mixture-of-Experts（MoE）在几乎不增加推理算力的前提下扩大容量。

## 方法
先提出 TF-Conformer：用 mel-band 切分替代 BSRNN 式手工子带，并用 Conformer 替代 RNN，在频率维（F-module）与时间维（T-module）交替建模。再把两侧 Conformer 的 FFN 换成 top-J 稀疏 MoE（默认 J=1）：对均值池化序列描述子做路由，整段共享选中专家；辅以 balance loss。T-MoE 按 mel 子带路由，F-MoE 按时间帧路由，合称 TF-MoE。默认 N=32、R=6、K=80 mel bands，SI-SNR+PIT 训练。

## 实验与结果
Libri2Mix 16 kHz：BSRNN 4.2 G / 13.9 dB SDR；TF-Conformer 4.1 G / 16.4 dB；TF-MoE（E=12）4.1 G / 17.7 dB SDR、17.2 SI-SDR，相对 BSRNN +3.8 dB SDR。消融显示 RNN < Conformer < MoE；E 从 3→12 提升，到 24 反而降约 1.1 dB。路由可视化显示 T-MoE 专家按频带特化、F-MoE 按说话人/发声模式随时间切换。

## 结论
TF-MoE 通过时频双维稀疏专家，在约 4.1 GMACs/s 下把新增参数有效转成分离增益，适合边缘部署；路由分析表明两维专家分别承担频带结构与时变说话人/交叠模式的特化。

## 点评
抓的是“参数便宜、算力贵”的部署错配，用 sequence-level top-1 路由把 MoE 开销压到几乎为零，比只做时域 MoE 的路线更贴合 band-split 分离结构。E=24 退化说明路由可学性是上限；若部署时专家加载/调度有额外开销，论文里的“几乎零算力”还需落到具体硬件实现上验证。


# Sweep-RSE: Streaming Region-of-Interest Speech Extraction in Multi-Talker Scenarios via Explicit Spatial Sweeping

- 论文编号：1631
- 报告人：Hogeon Yu
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/yu26d_interspeech.pdf

## 问题
AR/VR 与助听等场景需要按用户自定义空间窗口做 Region-of-Interest 语音提取，但 ReZero、DPARNet-RSE 等依赖隐式边界条件，在稠密干扰或空区域（Q=0）时易漏提或误放。本文要做轻量、全因果、显式空间扫描的流式方案。

## 方法
Sweep-RSE：先把窗口中心相位对齐到虚拟正前方；CH-SDB 用复数卷积保相位；Physics-Informed Spatial Sweep Attention（SSA）在窗口内用 L 个候选导向矢量扫相位相干性并做动态波束成形；Gated Context Fusion 拼接参考、对齐目标与差分特征以抑区外干扰；因果 Dual-Path Block（改自 SpatialNet）做时频谱细化；Region Speech Detector（RSD）门控空区输出。4 麦方形阵仿真（gpuRIR + VCTK + WHAM!），窗口宽随机 10°–90°，联合 SI-SDR + 0.1 BCE 训练。

## 实验与结果
因果版约 1.66M 参数、3.05 GMACs。Standard/Realistic：Q=0 能量衰减约 96–98 dB（远高于 SpatialNet 等）；Q=1 SI-SDR 10.60/12.88 dB，Q=2 为 13.04/12.64 dB。同 backbone 的隐式 proxy：ReZero-Proxy / DPARNet-Proxy 在 Realistic Q=1 约 10.3–10.4 dB，显式 Align & Sweep 达 12.88 dB（+2.4 dB 以上）。注意力图显示峰值跟随偏心目标而非只盯窗口中心。

## 结论
显式 Align & Sweep 加 RSD，在稠密多讲者与空窗口场景上显著优于隐式条件化，并以 O(1) 流式复杂度与很小算力支持边缘实时；未来拟在 ROI 内进一步拆分多说话人。

## 点评
把“区域提取”从学边界嵌入改成物理可解释的相位相干扫描，空区衰减与高干扰增益是最硬的证据。同 backbone 的 proxy 对照设计得很干净。局限是仿真阵列与固定扫描分辨率；真实阵列校准误差、移动目标与 ROI 内多源拆分仍未覆盖。


# Online Audiovisual Speaker Separation Using Efficient Visual Knowledge Distillation

- 论文编号：1999
- 报告人：Cheng Yu
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/yu26e_interspeech.pdf

## 问题
因果音视频说话人分离（AVSS）相对离线掉点明显：缺少未来上下文，且常用非因果、参数沉重的视觉前端难接入在线系统。需要在严格因果下压缩视觉前端并保住说话人判别力。

## 方法
对预训练 DeepAVSR 用非对称时间 padding 做因果推断；接入 online AV-CrossNet（可选 Mamba narrow-band），按说话人通道对齐音视频特征。再提出 Visual Knowledge Distillation（VKD）：学生保留教师结构但残差通道缩小 16 倍；训练前期教师/学生嵌入加权和（初值约 99%/1%），权重线性过渡，到第 K=50 epoch 完全切到学生，再与分离器联合训至收敛。数据为 LRS2/LRS3/VoxCeleb2 的 2mix，损失为 SI-SDR + 谱幅度。

## 实验与结果
在线系统中，oAV-CrossNet-Mamba-VKD 在 LRS2/LRS3 上 PESQ/SI-SDRi/SDRi 优于既有在线基线（相对最强基线约 +0.3 PESQ、+0.8 dB SI-SDRi 量级）；VoxCeleb2 上 PESQ 优于 Swift-Net-12，SI-SDRi 具竞争力。相对全尺寸因果 DeepAVSR，VKD 将视觉前端压到约 0.23 MB / 1.7 G/s MACs（约 48× 参数、7.5× 算力压缩），LRS2 上甚至 SI-SDRi 14.7 vs 教师 14.1。从零训学生或直接蒸馏后微调均不收敛；相对 Dolphin 的非因果压缩前端，VKD 压缩率更高且在因果设定下提升更大。

## 结论
VKD 用任务导向的渐进蒸馏得到轻量全因果视觉前端，配合强在线分离器达到在线 AVSS 的 SOTA，并显著缩小与非因果系统的差距。

## 点评
贡献在“因果化大视觉前端 + 渐进切学生”的工程配方：单独证明从零训/硬蒸馏不够，动态权重才稳住 AVSS。表格把因果掉点量化得很清楚。脆弱处是依赖教师质量与固定切换日程；VoxCeleb2 上压缩版相对全尺寸教师仍有 SI-SDRi 回退，说明压缩收益与最难数据上的上限仍需权衡。


# DTT-BSR+: A Generative-Regression Cascade for Music Source Restoration

- 论文编号：2291
- 报告人：Gongping Huang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/ni26b_interspeech.pdf

## 问题
Music source restoration（MSR）要在解混的同时逆转压缩、编解码等非线性制作效果。现有系统 FAD 尚可但 MMSNR 普遍偏低，说明语义分布贴近而波形重建不足。作者要把分布拟合与信号重建拆成两阶段。

## 方法
DTT-BSR+：第一阶段用 GAN 式 DTT-BSR 从劣化混合中生成符合干净 stem 先验的估计；第二阶段用去掉 BLSTM 的 Demucs-L，以时间域 L1 + multi-resolution STFT 回归到真值，限制感受野以免改写第一阶段分布。在 MSRBench（3250 条 10 s/48 kHz，8 类 stem）上，第一阶段按既有设定预训练，第二阶段用冻结第一阶段在训练集上的推断结果作输入，Adam 训 150 epoch；训练时 10% 概率用真值替换第一阶段输出，并做随机相位偏移增强。

## 实验与结果
相对单阶段 DTT-BSR，八类 stem 的 MMSNR 均提升，Bass 2.49→9.29 dB、Drums 2.24→8.79、Vocals 3.34→6.72；平均 MMSNR 4.35，优于 X-LANCE-MSR 的 2.28，且在 Vocals/Guitars/Synthesizers/Bass/Drums 五类上更高；八类 Zimtohrli 均为最佳。FAD-CLAP 在部分 stem 随 MMSNR 下降而改善，在 Guitars/Keyboards/Synthesizers/Orchestral 等却上升。消融显示 Demucs-L 作第二阶段整体优于 MSG；Percussions 上单阶段 MSG（2.47 dB）远好于级联（约 0.4 dB），说明第一阶段失真难被第二阶段救回。FAD 分解表明变差主要由语义均值项 Dμ 上升驱动，协方差项变化小。

## 结论
把语义拟合与波形重建分阶段，可系统抬高 MMSNR 与感知指标；但重建精度与语义分布存在 stem 相关权衡，统一架构不足以覆盖全部 stem，尤其 Percussions 需另策。

## 点评
问题诊断（FAD 好、MMSNR 差）直接导出 cascade 设计，比把 MSR 拆成分离/去混响/去噪更贴“目标冲突”。FAD 均值项分析把“听起来像但分布中心漂了”说清楚了。脆弱点在于级联误差传播（Percussions）以及第二阶段可能把生成分布往回归均值拉；后续 stem-aware 或端到端联合训是自然方向。


# Adaptive Hard-Pair Sampling via Curriculum Learning for Speech Separation

- 论文编号：3139
- 报告人：Xueliang Zhang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/shen26e_interspeech.pdf

## 问题
端到端分离在平均 SI-SDR 上已较强，但对音色相近说话人仍易失败；均匀采样使难样本占比过低。既有难例重加权会改有效分布、伤均值，离线难例挖掘又昂贵。需要在线、自适应地加大难说话人对的采样。

## 方法
维护说话人对难度矩阵 D（由分离 SI-SDR 等分数 EMA 更新，并对称化）。每个混合先均匀抽锚说话人，再用温度 Softmax 按 D 抽干扰者：τ 随 epoch 线性衰减，早期近均匀、后期偏难对。仅在中间阶段（Ewarm=20 到 Estop=100）启用；前后仍用标准动态混合。难度更新与采样都在数据层，几乎不增训练开销。在 Libri2Mix 上对 Conv-TasNet、BSRNN、TF-GridNet 做动态混合对比。

## 实验与结果
τ0=20 时：Conv-TasNet 均值 SI-SDRi 保持 16.7 dB；BSRNN 21.0→21.3；TF-GridNet 21.9→22.7。更低初始温度会略伤均值。尾部：低于 10 dB SDRi 的样本数减少（如 TF-GridNet 27→7），bottom 30% 平均 SDRi 上升（Conv-TasNet 12.9→13.2，BSRNN 17.4→17.6，TF-GridNet 18.3→18.8）。难度矩阵可视化显示残差难对逐渐集中到少数说话人簇。

## 结论
课程式难对采样可改善相似音色尾部表现并常保住甚至提升均值，无需改损失或增网络组件；合适初始温度与中间阶段启用是关键。

## 点评
把“难例”落到说话人对矩阵并用温度课程控制，比固定重加权更贴近动态混合管线。强在几乎零开销、可插多种 backbone。脆弱处是难度信号早期不可靠（故需 warmup），且矩阵规模随说话人数平方增长；对超大说话人库可能需要稀疏或聚类近似。

