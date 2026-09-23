# Neurophysiology of Speech

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 1 - Oral 2）
- Area：1
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。主张均锚定各摘要原文。

## 技术趋势

本场围绕言语相关神经信号的表征、跨被试泛化与临床/认知标记展开。一条主线是想象言语、默动与发声条件之间共享表征：用立体定向 EEG 上的线性语谱重建做跨条件迁移，并与非线性网络对比，强调共享结构与刺激级可分性。

第二条主线是跨被试鲁棒：想象言语 EEG 解码用动态图建模与对抗式被试解耦；听觉注意解码用信息瓶颈与对抗学习把任务与被试特征正交分解，并在多个公开集上报告跨被试设定下的表现。

第三条主线从重建走向感知与测量学：高伽马时频特征驱动 WaveNet 式解码器做侵入式 EEG 到可听语音的映射；主观认知下降（SCD）人群在不同韵律表达风格下的皮层言语追踪；以及用贝叶斯广义可加多层模型在降采样下估计 ERP 潜伏期的精度—算力权衡。

整体上，方法从“单条件解码”转向“条件间关系 + 被试不变表示 + 可信时间估计”，服务 BCI、神经导向助听与早期认知标记等方向。

## 技术内容

### 想象/发声表征与侵入式语音重建

**Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech**（论文 2836；presenter：Rupesh Chillale）  
利用公开立体定向 EEG，为发声、默动与想象言语分别训练线性语谱重建模型并做跨条件泛化评估。摘要称单条件训练的线性解码器通常可成功迁移，暗示共享言语表征；基于排序的刺激级可分性分析显示条件内/跨条件均保留刺激特异结构。与非线性网络相比，二者均有跨条件迁移，但线性模型在刺激级可分性上更优。

**Exploiting EEG-based Gamma-Band Time Frequency Feature in WaveNet Decoder Framework for High-Fidelity Speech Reconstruction**（论文 377；presenter：Rantu Buragohain）  
从侵入式 EEG 的高伽马频段（70–170 Hz）提取时频特征，经基于 WaveNet 的解码器映射到语音表示，以服务严重言语障碍者的沟通。框架用堆叠因果膨胀卷积残差块与门控激活捕获短时构音与长程时序并保持因果性；残差与跳跃连接促进特征传播与训练稳定。实验显示预测与真实语谱相关性强，并指出稳健性与被试间变异并存。

### 跨被试 EEG 解码与解耦表示

**Subject-Invariant Dynamic Graph Modeling for Cross-Subject EEG Imagined Speech Decoding**（论文 2884；presenter：Saravanakumar Duraisamy）  
针对未见被试上想象言语 EEG-BCI 性能显著下降，提出融合多视角动态连通先验、通道图注意力与梯度反转层对抗式被试解耦的框架。严格留一被试协议、15 名被试上，两个独立数据集平均分类准确率分别为 31.20%±3.12% 与 30.36%±4.05%，摘要据此强调结构化连通建模与被试不变训练的重要性。

**DisenEEG-Net: Disentangling EEG features via sufficient information bottleneck and adversarial learning for cross-subject auditory attention detection**（论文 1703；presenter：Tasleem Kausar）  
为跨被试听觉注意解码（AAD）提出 DisenEEG-Net：并行 Transformer 编码潜在 EEG 表示后分解为正交的任务/被试子空间；充分信息瓶颈保留必要被试信息并抑制任务泄漏，对抗训练强化任务特征的被试不变性，解码器在解耦中保持保真。摘要称在 KUL、DTU、AVED 上跨被试设定达到当时最优表现。

### 认知标记与 ERP 时间估计

**More than a feeling: Expressive style influences cortical speech tracking in subjective cognitive decline**（论文 527；presenter：Matthew King-Hang Ma）  
SCD 使痴呆风险加倍。60 名认知正常老年被试听不同表达风格（scrambled、descriptive、dialogue、exciting）言语并采集 EEG；用声学、亚音节切分与音位配列特征建立编码模型。皮层追踪强度（CTS）上亚音节语言特征优于声学特征；SCD 更严重对应更弱的（1）亚音节而非声学特征 CTS，以及（2）韵律平坦言语（scrambled、descriptive）的 CTS，提示其作为早期认知下降潜在神经标记。

**Bayesian Generalized Additive Multilevel Models for Accurate ERP Latency Estimation under Moderate Downsampling**（论文 2750；presenter：Zixia Fan）  
单试次贝叶斯 GAMM 在高采样率下计算昂贵。被动 oddball 范式下比较全分辨率到极端降采样的 ERP 潜伏期估计：失匹配负波潜伏期在中等降采样前较稳定、起始变化小；晚期辨别负波则起始更晚、时程更短；极端分辨率下两成分仍可检出但时间精度下降。结论是可以降采样降成本，但应避免极端降采样。

## 本场要点

- 发声/默动/想象言语共享线性可迁移的语谱重建表征，线性模型在刺激级可分性上更有优势。
- 跨被试想象言语与 AAD 均依赖被试不变表示：动态图+对抗解耦，或信息瓶颈+正交子空间。
- 高伽马时频 + WaveNet 式解码支撑侵入式 EEG 可听语音重建。
- SCD 与韵律平坦条件下的亚音节 CTS 被提出为早期认知下降潜在标记。
- ERP 潜伏期的贝叶斯 GAMM 显示中等降采样可接受，极端降采样损害时间精度。
- 方法轴从条件内解码扩展到条件间关系、跨被试泛化与测量可信度。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 2836 | Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech |
| 2884 | Subject-Invariant Dynamic Graph Modeling for Cross-Subject EEG Imagined Speech Decoding |
| 377 | Exploiting EEG-based Gamma-Band Time Frequency Feature in WaveNet Decoder Framework for High-Fidelity Speech Reconstruction |
| 527 | More than a feeling: Expressive style influences cortical speech tracking in subjective cognitive decline |
| 2750 | Bayesian Generalized Additive Multilevel Models for Accurate ERP Latency Estimation under Moderate Downsampling |
| 1703 | DisenEEG-Net: Disentangling EEG features via sufficient information bottleneck and adversarial learning for cross-subject auditory attention detection |
