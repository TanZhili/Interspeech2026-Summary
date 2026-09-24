# Speech Enhancement and Restoration

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为跨领域长文口头报告，覆盖参数高效增强、通用语音恢复、开放式助听器双耳增强、扩散快速采样、神经房间脉冲响应，以及 GAN 声码器的子带条件与相位损失。共同主题是在保真与效率之间引入更贴合语音/声学结构的归纳偏置。

增强/恢复侧：四元数 Conformer GAN 用 Hamilton 积共享幅相参数；SEMamba++ 注入全局/局部/周期频谱模式与多分辨率时频双处理；开放式助听器则把双耳 MVDR 与轻量网络级联，联合增强目标并抑制声学泄漏且无需入耳麦部署。扩散方面，插值 SDE 形式化使面向观测插值的条件扩散可用更少网络评估快速采样。

声学建模与波形生成上，MiNAF 用粗糙房间网格查询的距离分布作为显式局部几何上下文生成 RIR；SCNet 以子带条件网络提供先验并引入幅度感知相位损失，缓解黑盒丢失谱信息与相位缠绕。

## 论文技术总结

# QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement

- 论文编号：889
- 报告人：Shogo Yamauchi
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yamauchi26_interspeech.pdf

## 问题
轻量语音增强压缩参数时常损害相位建模，引入听感伪迹；需在少参数下联合保持幅度与相位。

## 方法
提出 QC-GAN：用 Hamilton 积实现四元数 FC/卷积/多头自注意，将 Conformer 式编解码改写为 Quaternion Conformer；输入为 Δlog|Y|、log|Y|、归一化相位 cos/sin 组成的四元数特征。编码器用 QG-Dilated DenseNet，瓶颈为两阶段时–频 Q-Conformer，解码双分支估计幅度 mask 与复残差；MetricGAN 判别器逼近 PESQ。损失含 RI/Mag/Time/可微 PESQ/GAN。

## 实验与结果
VoiceBank+DEMAND：Base（0.89M）PESQ 3.48，接近更大 SoTA 且参数不到一半；Tiny（35K）PESQ 3.23，优于多数同等极紧凑模型。DNS-Challenge 3 盲测用 DNSMOS/P.808 验证泛化。消融显示四元数相对全实数替换相位误差更低。

## 结论
四元数结构归纳偏置以约 1/4 参数耦合幅度–相位，结合 MetricGAN 可在紧凑模型上达到高保真增强。

## 点评
把 SE 的相位难题对准 Hamilton 积的分量耦合，比单纯通道缩减更有理论抓手。MetricGAN+可微 PESQ 强推听感分数，需防指标过拟合；Tiny 变体展示可扩展性，但极低容量下复杂噪声场景仍可能受限。


# SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns

- 论文编号：665
- 报告人：Yongjoon Lee
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lee26f_interspeech.pdf

## 问题
通用语音恢复（噪声、混响、带限、削波等）中，时–频双路径常对时间与频率用同构模块，频率侧缺少全局/局部选择性与谐波周期性建模；单分辨率处理难兼顾多尺度谱模式与效率。

## 方法
提出 SEMamba++：Frequency GLP 并行连接 FAN 直作用于频率轴的全局–周期（GP）支路与卷积局部（L）支路，再点卷积选择融合；多分辨率并行 TFDP（仅频率下采样，时间分辨率保留），各分辨率独立 Time Mamba + Frequency GLP 后自底向上融合；幅度解码用按频带可学习 softplus 映射。训练用 LSGAN（MS-SB-CQTD+MRD）及 mag/相位/一致性/RI/mel/特征匹配等重建损失。

## 实验与结果
在 VCTK-GSR（噪声/混响/带限/削波仿真）上训练，并用 URGENT 2025、DNS 2020、CCF-AATC 等做域外评测；指标含 SCOREQ、UTMOS、DNSMOS 等。正文报告相对 MP-SENet、SEMamba、MaskSR、Universe++、VoiceFixer、USE-Mamba 等多基线，SEMamba++ 在计算效率可接受下取得最佳总体表现；消融支持 GLP、并行多分辨率与 LSGAN 相对纯 MetricGAN 的贡献。

## 结论
为频率轴显式注入全局–局部–周期归纳偏置，并以并行多分辨率 TFDP 捕获多样谱模式，可提升通用语音恢复质量。

## 点评
相对「时间 Mamba + 朴素频率模块」的 SEMamba，GLP 与并行多分辨率直接对准 GSR 的异构失真（尤其带限需全局、谐波需周期）。LSGAN  vocoder 式目标减轻只刷 PESQ 的偏置。全文末段抽取不完整处不影响方法主线；具体数值以论文表格为准。


# ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids

- 论文编号：1660
- 报告人：De Hu
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/hu26f_interspeech.pdf

## 问题
开放式助听器存在外噪声经通气孔漏入耳道，损害双耳增强；传统主动 BSE+ANC 常需耳道深部误差麦，佩戴不适且难部署。

## 方法
提出 ABSE-NET：BMVDR 粗增强后，将左右参考麦与 BMVDR 输出的实虚部拼入轻量网络；编码器–特征增强（重复 L 次 F-TDL：频率/时间依赖学习，含 RMB-Conv1D 与因果 C-RMB-Conv1D）–ConvAtt（通道与频–时注意）–解码器，输出经次级路径抵消泄漏并补偿波束形成失真。损失为 −SI-SDR − λ·STOI。训练可用误差麦建模，推理部署无需耳内误差麦。

## 实验与结果
Librispeech+NOISEX-92，HRIR 来自 Hearpiece。ABSE-NET 约 0.112M 参数、0.184G FLOPs；SI-SDR 9.869 dB、PESQ 3.626、STOI 0.955，PESQ/STOI/CSIG/COVL 优于 ASE-TM 等，参数与算力远小于 DeepANC/ASE-TM；空间线索 ΔILD/ΔIPD 保持较好。相对无泄漏处理的 BMVDR 与带泄漏 BMVDR 均有明显听感与客观提升。

## 结论
模型驱动粗增强 + 轻量神经后处理可在无耳内误差麦部署下联合做开放式助听器主动双耳增强。

## 点评
把泄漏消除与失真补偿并入同一后滤波映射，避开实时耳内反馈回路，贴近可穿戴约束。F-TDL 用重参数多分支卷积换注意力，利于助听器算力。性能依赖次级路径与泄漏建模假设，真实个体耳道差异仍需现场校准验证。


# A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration

- 论文编号：2582
- 报告人：Bunlong Lay
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lay26_interspeech.pdf

## 问题
SGMSE+ 等条件扩散用插值 SDE（iSDE）在干净语音与退化观测之间插值，无条件图像生成用的 DPM-Solver 等快速采样器不能直接套用，导致反向过程需大量 NN 评估。

## 方法
统一形式化 iSDE：均值 μ_t=(1−k(t))x_0+k(t)y，漂移 f_t=γ(t)(y−x_t)，并给出 k(t)↔γ(t) 关系及由目标方差求 g(t) 的公式；归纳 OUVE、BBED、最优传输、布朗桥等，并提出修正参数含义的 fOUVE。基于指数 Runge–Kutta，推导面向 y≠0 与 DSM/score 估计的 iSDE-pS-κ 求解器（含 κ∈[0,1] 的 PF-ODE/反向 SDE），对部分 SDE 给出权重闭式解。

## 实验与结果
在降噪、带宽扩展、去削波、MP3 解码、去混响等多恢复任务上，提出求解器约 10 次 NN 评估即可达到与自适应 RK45（>40 NFE）相近的恢复质量。

## 结论
iSDE 统一形式与专用快速求解器使条件扩散语音恢复可在少步采样下接近高阶 ODE 求解器表现，并为后续条件版 DPM 变体铺路。

## 点评
把「观测插值」从无条件高斯终点显式拆开，是把 DPM-Solver 思想迁移到 SGMSE+ 族的关键。fOUVE 修正 σ_min/σ_max 可解释性有助调参。全文实验表抽取不完整，具体客观分数以原文表格为准；算法贡献本身已较完整。


# Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation

- 论文编号：513
- 报告人：Chen Si
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/si26_interspeech.pdf

## 问题
RIR 是房间声学仿真的核心；近年神经隐式方法（NAF、NACF、NeRAF 等）多用图像或隐式网格作上下文，几何信息间接且粒度粗。场景专用模型缺结构化局部几何，而 Mesh2IR 等生成式全局网格编码又偏场景泛化、细粒度物理细节易被稀释。

## 方法
提出 MiNAF（Mesh-infused Neural Acoustic Field）：在 Tx/Rx 位置用 Fibonacci 格点发射 N 条射线，查询粗糙房间网格，收集到首次命中点的距离 d、法向 n、邻域射线距离均值/标准差 μ/σ，以及按距离阈值的占用直方图 occ；各特征经非线性投影后与正弦位置编码的坐标拼接成上下文。时间索引也做位置编码并与上下文逐元素相乘，再连同 Rx 朝向 θ 与双耳通道 c 输入 MLP，分别预测 STFT 的 log-magnitude 与瞬时频率（IF），经 iSTFT 还原时域 RIR。损失为谱 L1 加 Schroeder 能量衰减曲线项。

## 实验与结果
数据为 SoundSpaces（基于 Replica），选取 6 个房间（矩形/非矩形单室与多室），80%/5%/15% 划分；另在更大、更稀疏的 GWA 公寓上评测。指标为 T60、C50、EDT；对比 Opus/AAC 插值与 INRAS、NAF、NACF、AV-NeRF、NeRAF 等。正文抽取在对比表中途截断，仅可见部分基线数值（如 NACF T60 2.36%、C50 0.50 dB、EDT 0.014 s），MiNAF 自身完整数字与结论段未出现在可用全文中。引言称在少样本条件下可优于先前 SOTA，并有项目页补充材料。

## 结论
作者主张用网格射线探测得到的显式局部几何能更好引导神经隐式声学场，从而更准地生成任意 ⟨Tx,Rx⟩ 的 RIR；因全文后半缺失，作者最终定量结论与边界表述无法从正文完整核对。

## 点评
设计抓的是“局部几何（距离分布/法向）应直接进入场景专用声学场，而不是只靠图像或隐式特征格”。射线统计特征预计算分布，减轻 MLP 自己从原始距离推断几何的负担，物理可解释性较强。当前可用全文在实验结果表中途截断且含乱码，MiNAF 相对基线的具体增益只能依据方法叙述推断，不能当作已核实数字使用。


# SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Phase Loss

- 论文编号：843
- 报告人：Nan Xu
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26e_interspeech.pdf

## 问题
GAN 声码器常黑盒生成，细粒度谱信息易丢；全带 iSTFT 相位连续性差；现有相位损失等权对待所有时频点，忽视大幅值区相位误差对听感更关键。

## 方法
以 iSTFTNet 为骨干（Snake 激活），旁路 CondNet 用 ConvNeXtV2 预测低频子带幅度/相位并 iSTFT 生成约 6 kHz 子带波形，再经 STFT+耦合块注入骨干上采样层。提出幅度感知抗卷绕相位损失：sin²(Δθ/2) 乘目标幅度 M。判别器用 MPD/MRD（同 BigVGAN）；重建含全带/子带 mel 与相位项。

## 实验与结果
LibriTTS train-clean-100（24 kHz）训练；域内与 VCTK 域外各 500 句。SCNet PESQ ID/OD 4.02/3.78，MOS 4.21/4.14，优于 BigVGAN、Vocos、HiFTNet 等；约 15.86M 参数。CosyVoice 声学特征上 MOS 4.09。dev 子集 2M 步 PESQ 4.007，接近更大 BigVGAN。

## 结论
子带条件先验与幅度加权相位损失可提升 GAN 声码器客观与主观质量，并保持有竞争力的推理速度。

## 点评
用低频子带先验替代易错 F0/NSF 路径，更稳地注入谱结构；幅度加权直接对准「大能量相位更重要」的听感直觉。子带仅到 6 kHz，高频细节仍依赖骨干黑盒，跨采样率部署需重设 hop/ISTFT 配置。

