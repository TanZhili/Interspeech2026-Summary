# Speech Enhancement and Restoration

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Long Oral（Cross-area long papers Oral session 5）
- Area：跨领域长文
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。参数量与评测分仅引自摘要。

## 技术趋势

本场为跨领域长文口头报告，覆盖参数高效增强、通用语音恢复、开放式助听器双耳增强、扩散快速采样、神经房间脉冲响应，以及 GAN 声码器的子带条件与相位损失。共同主题是在保真与效率之间引入更贴合语音/声学结构的归纳偏置。

增强/恢复侧：四元数 Conformer GAN 用 Hamilton 积共享幅相参数；SEMamba++ 注入全局/局部/周期频谱模式与多分辨率时频双处理；开放式助听器则把双耳 MVDR 与轻量网络级联，联合增强目标并抑制声学泄漏且无需入耳麦部署。扩散方面，插值 SDE 形式化使面向观测插值的条件扩散可用更少网络评估快速采样。

声学建模与波形生成上，MiNAF 用粗糙房间网格查询的距离分布作为显式局部几何上下文生成 RIR；SCNet 以子带条件网络提供先验并引入幅度感知相位损失，缓解黑盒丢失谱信息与相位缠绕。

## 技术内容

### 参数高效与结构感知增强/恢复

**QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement**（论文 889；presenter：Shogo Yamauchi）  
四元数 Conformer 生成器配合 MetricGAN 式训练；Hamilton 积以结构化权共享编码幅相并减少层参数。VoiceBank+DEMAND 上仅 0.89M 参数达 PESQ 3.48，性能可比 SOTA 且不足其一半规模；35K 参数变体 PESQ 3.23。DNS-Challenge 3 进一步确认真实条件泛化。

**SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns**（论文 665；presenter：Yongjoon Lee）  
针对 SSM 增强未充分刻画频谱周期性与多分辨率分析，提出 GLP 频率特征块、多分辨率并行时频双处理块与可学习映射。摘要称相对多基线取得最佳表现且保持计算效率。

**ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids**（论文 1660；presenter：De Hu）  
开放式助听声学泄漏损害传统双耳增强。ABSE-NET 级联双耳 MVDR 与轻量网络：前者粗增强，后者同时抵消泄漏并补偿 MVDR 失真；网络含频—时依赖学习与卷积注意力的特征融合。相对传统自适应滤波 BSE+ANC，实用部署无需入耳麦克风；实验优于 SOTA。

### 扩散快速求解、RIR 与 GAN 声码

**A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration**（论文 2582；presenter：Bunlong Lay）  
指出为 DPM 设计的快速求解器不能直接用于在目标分布与噪声观测间插值的 SGMSE+ 类模型。工作形式化插值 SDE（iSDE）并为其提出求解器，使多种语音恢复任务可用少至 10 次神经网络评估完成快速采样。

**Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation**（论文 513；presenter：Chen Si）  
MiNAF 在给定位置查询粗糙房间网格，提取距离分布作为局部上下文显式表示，引导神经隐式 RIR 生成。相对依赖场景图像等上下文、未有效利用显式几何的方法，摘要称在多项指标上具竞争力。

**SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Phase Loss**（论文 843；presenter：Nan Xu）  
轻量子带条件网络预测子带信号作先验，经 STFT 得到傅里叶系数并注入骨干以增强重建；幅度感知相位损失用对应幅度加权瞬时相位误差，强调高能量区。客观与主观评价均显示高质量语音生成优势。

## 本场要点

- 四元数结构与感知度量对抗训练可在极小参数下逼近增强 SOTA。
- 通用恢复需要显式注入全局/局部/周期频谱归纳偏置。
- 开放式助听需联合 BSE 与主动泄漏控制，且可免入耳麦部署。
- 插值型条件扩散需要专用快速求解器，而非直接套用 DPM 采样器。
- 显式局部几何距离分布提升神经 RIR 保真。
- 子带条件先验与幅度加权相位损失改善 GAN 波形生成。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 889 | QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement |
| 665 | SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns |
| 1660 | ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids |
| 2582 | A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration |
| 513 | Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation |
| 843 | SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Phase Loss |
