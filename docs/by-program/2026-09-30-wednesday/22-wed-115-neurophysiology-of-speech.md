# Neurophysiology of Speech

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：1
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕言语相关神经信号的表征、跨被试泛化与临床/认知标记展开。一条主线是想象言语、默动与发声条件之间共享表征：用立体定向 EEG 上的线性语谱重建做跨条件迁移，并与非线性网络对比，强调共享结构与刺激级可分性。

第二条主线是跨被试鲁棒：想象言语 EEG 解码用动态图建模与对抗式被试解耦；听觉注意解码用信息瓶颈与对抗学习把任务与被试特征正交分解，并在多个公开集上报告跨被试设定下的表现。

第三条主线从重建走向感知与测量学：高伽马时频特征驱动 WaveNet 式解码器做侵入式 EEG 到可听语音的映射；主观认知下降（SCD）人群在不同韵律表达风格下的皮层言语追踪；以及用贝叶斯广义可加多层模型在降采样下估计 ERP 潜伏期的精度—算力权衡。

整体上，方法从“单条件解码”转向“条件间关系 + 被试不变表示 + 可信时间估计”，服务 BCI、神经导向助听与早期认知标记等方向。

## 论文技术总结

# Relating the Neural Representations of Vocalized, Mimed, and Imagined Speech

- 论文编号：2836
- 报告人：Rupesh Chillale
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maghsoudi26_interspeech.pdf

## 问题
发声、默读口型（mimed）与想象言语的神经表征常被分开解码；它们共享多少结构、线性解码器能否跨条件迁移，对 BCI 很关键。

## 方法
VocalMind 单被试普通话 sEEG（110 电极，100 句×2/条件）：用时间滞后线性模型重建 NSL 皮层谱图，分别得 Gv/Gm/Gi，做条件内与跨条件测试；秩分析测刺激可分性；并复现卷积–RNN 非线性解码器对比。用打乱配对零模型检验显著性。

## 实验与结果
条件内重建显著优于零模型（p≪0.001），发声最优，默读次之，想象最弱；跨条件相关仍显著，默读↔发声迁移较强。秩分析显示默读训练解码器在发声上保留刺激结构（如 AUC 模式），想象侧较弱。非线性亦有跨条件迁移，但线性在刺激级可分性上更优。

## 结论
三种言语产生模式共享可迁移的神经–声学映射；线性解码器可解释且跨条件可用，利于无声输出的 BCI，但想象条件对齐与信息量仍受限。

## 点评
用跨条件迁移直接量“共享表征”，比单条件重建更有理论含量。强在线性可解释与秩分析；弱在单被试、想象对齐难，外推多被试需谨慎。


# Subject-Invariant Dynamic Graph Modeling for Cross-Subject EEG Imagined Speech Decoding

- 论文编号：2884
- 报告人：Saravanakumar Duraisamy
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/duraisamy26_interspeech.pdf

## 问题
EEG 想象言语跨被试泛化差：Transformer 常把电极当可交换 token，忽略拓扑与动态连接，且任务特征易与被试特异性纠缠，LOSO 下常近随机。

## 方法
在预训练 EEG Transformer（如 EEGPT）上做电极对齐池化；按短窗估计多视图动态连接先验（空间/PLV/相干/包络相关等）注入图偏置注意力；用梯度反转层做对抗被试解缠。两套公开 15 人五词想象言语数据（BCI 2020 与 overt/covert 中的 covert），严格 LOSO。

## 实验与结果
完整模型两数据集平均准确率 31.20%±3.12% 与 30.36%±4.05%，高于仅 Transformer 基线（约 20%）及多种常规基线；图先验与 GRL 消融均有贡献，动态先验优于静态；α≈0.5、收缩 ρ=0.2 较稳。

## 结论
结构化动态连接建模加被试不变训练可在严格 LOSO 下改善想象言语 EEG 解码，尽管绝对准确率仍有限。

## 点评
把“电极拓扑 + 动态连接 + 对抗去身份”对上 LOSO 失败模式，问题抓得准。强在双数据集一致增益；弱在五类准确率仍偏低、临床可用性远，且依赖预训练骨干质量。


# Exploiting EEG-based Gamma-Band Time Frequency Feature in WaveNet Decoder Framework for High-Fidelity Speech Reconstruction

- 论文编号：377
- 报告人：Rantu Buragohain
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/buragohain26_interspeech.pdf

## 问题
从侵入式神经信号直接合成可听语音仍难：噪声高、时序失配，线性/短时模型难抓长程依赖，既往谱重建 PCC 常低于 0.7。

## 方法
公开荷兰语 sEEG（10 名癫痫患者朗读 100 词）：提高 gamma（70–170 Hz）包络时频特征并堆叠时间上下文，映射到 logMel；用堆叠因果膨胀卷积残差块的 WaveNet 式解码器（门控激活、残差/跳跃连接）重建，再经全连接输出。按被试训练评估 MSE、PCC、STGI。

## 实验与结果
被试间 PCC 约 0.9014–0.9510，MSE 约 0.317–0.584，STGI 约 0.49–0.54；标准差小，显示相关强但存在被试差异。作者称相对既往线性/浅层非线性有更强相关与时序一致性。

## 结论
高 gamma 特征 + WaveNet 解码可从 sEEG 获得高相关谱重建，推进神经言语合成；仍受电极位置因临床而异与被试变异限制。

## 点评
用因果膨胀卷积对准神经–语音长程对齐问题，PCC 数字亮眼。强在公开数据可复现；弱在朗读词表、电极布局非统一、未充分报告可听合成听感/ASR 指标。


# More than a feeling: Expressive style influences cortical speech tracking in subjective cognitive decline

- 论文编号：527
- 报告人：Matthew King-Hang Ma
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ma26b_interspeech.pdf

## 问题
主观认知下降（SCD）增加痴呆风险，但客观测验正常；自然言语感知中皮层追踪如何随 SCD 与韵律表达风格变化，尚缺清晰神经标记。

## 方法
60 名认知正常粤语老年人（MoCA 正常，SCDS 14–58）听四种表达风格（scrambled/descriptive/dialogue/exciting）；用 mTRF 分别用声学、亚音节切分、音位配列特征编码 EEG，得皮层追踪强度（CTS）。混合模型检验 SCDS×模型×风格交互。

## 实验与结果
音位配列模型 CTS 最高，切分次之，声学最低。SCD 越重，亚音节语言特征 CTS 越弱（切分显著、音位配列边缘），声学模型不显著。SCD 负向调节主要出现在韵律平坦的 scrambled/descriptive，而非 dialogue/exciting。假设中“丰富韵律更敏感”未获支持，作者解释为韵律可能提供补偿脚手架。

## 结论
平坦言语上的高级语言特征 CTS 可能作为 SCD 早期神经候选标记；声学追踪相对保留。

## 点评
把特征层级与表达风格交叉，修正“高负荷场景一定更差”的直觉。强在生态材料与统计交互清晰；弱在仅听、无理解行为金标，且刺激生态与合成风格混杂需谨慎外推。


# Bayesian Generalized Additive Multilevel Models for Accurate ERP Latency Estimation under Moderate Downsampling

- 论文编号：2750
- 报告人：Zixia Fan
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fan26c_interspeech.pdf

## 问题
单试次 Bayesian GAMM 估 ERP 潜伏期计算昂贵，常靠降采样；不同分量潜伏期变异不同，中等/极端降采样对 onset/offset/持续时长的影响不清。

## 方法
普通话 Tone3 吱哑声被动 oddball（20 人，标准/偏差 /ia/）：在 1000/500/250/100 Hz 上拟合 Bayesian GAMM，估 MMN 与 LDN 的 onset、offset、持续；报告收敛诊断与组件特异变化。

## 实验与结果
1000–250 Hz 收敛良好（R-hat≈1.00、无发散）；100 Hz 不稳定（发散约 5%、ESS 低）。MMN 潜伏期从全分辨率到中等分辨率基本稳定、onset 位移小；LDN 随采样率下降出现更晚 onset、更短持续。极端 100 Hz 两分量仍可检出但时间精度下降、可信区间变宽。

## 结论
适度降采样可降算力且对低变异分量（如 MMN）较安全；应避免极端降采样，尤其对高变异晚期分量（LDN）。

## 点评
把“能算”与“估得准”拆开，并按分量变异解释为何同一降采样策略效果不等。强在收敛诊断与组件对照；弱在单范式/单语种，阈值选择仍偏经验。


# DisenEEG-Net: Disentangling EEG features via sufficient information bottleneck and adversarial learning for cross-subject auditory attention detection

- 论文编号：1703
- 报告人：Tasleem Kausar
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kausar26_interspeech.pdf

## 问题
EEG 听觉注意解码（AAD）跨被试泛化难：注意相关与被试特异特征纠缠，域偏移使神经导向助听难以落地。

## 方法
DisenEEG-Net：并行时空 Transformer 提表征后正交分解为任务/被试子空间；充分信息瓶颈约束被试子空间保留身份信息并抑制任务泄漏；GRL 对抗使任务特征被试不变；重建损失保保真。在 KUL、DTU、AVED 上留一被试交叉评测。

## 实验与结果
跨被试：KUL 1 s 窗口 Acc 75.9%±13.3（超 DARNet 约 5+ 点），2 s 76.1%；DTU 约 57.8–58.7%；AVED 音/视频约 54–55%。消融中去时间支路掉约 8.5 点；正交+瓶颈、对抗+重建均有贡献。分析显示 z_task 可做注意分类，z_dom  alone 不能。

## 结论
信息论瓶颈与对抗联合解缠可提升跨被试 AAD，更长时间窗有助；为神经导向助听的域泛化提供可行框架。

## 点评
把正交、充分瓶颈、对抗、重建四约束叠在一起，针对“任务–被试纠缠”较完整。强在三数据集一致超基线；弱在 KUL 方差仍大、绝对准确率在 DTU/AVED 仍接近临界实用。

