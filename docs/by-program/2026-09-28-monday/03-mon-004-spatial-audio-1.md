# Spatial Audio 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 5）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场空间音频主题覆盖终端近麦检测、声学场景分类跨设备适配、个性化 HRTF/HRIR，以及双耳定位与紧凑阵列 DOA。手机端 Ada-Mic 用 Generalized Cross-Correlation 特征编码 DOA，把距离与朝向因素解耦，服务 No-Hot-Word 唤醒。

个性化双耳渲染是另一主线：HRIR-Former 在时域、无网格条件下从稀疏测量重建任意方向 HRIR，并辅以 ITD/ILD 头；S2RNF 则走 sim-to-real 神经场，把 3D 头模仿真 HRTF 映射到真实测量对应物，降低消声室测量门槛。

感知与定位方面，BiEAR 借鉴内侧橄榄耳蜗（MOC）反馈，用神经控制器在推理中自适应调节双耳听觉滤波器组频率选择性；紧凑线阵端射方向 DOA 退化被理论归因于远场平面波下 TDOA—方位角映射病态，并在 reliability-aware phase transform 框架内提出加权 SRP 与精炼 TDOA。设备异构与无源数据约束下的 MSFDA（FaSoLa）则用后验调整与标签一致性聚合多源模型。瓶颈集中在朝向变化、测量成本、端射病态与设备域移。

## 技术内容

### 近场交互与跨设备场景适应

**Ada-Mic: Orientation-Adaptive and Robust Close-to-Mic Speech Detection on Smartphone Using Generalized Cross-Correlation Features**（论文 224；Irina Kezele）
提出 Ada-Mic，使近麦语音检测可适应更灵活的手机朝向范围。以 Generalized Cross-Correlation 特征作为辅助空间信号隐式编码 DOA，解耦距离与朝向相关特征；轻量模块可嵌入现有检测器。摘要称在困难距离与朝向下准确率相对先前工作最高提升 24%，并对背景噪声鲁棒，推进 No-Hot-Word 唤醒。

**Robust Multi-Source-Free Domain Adaptation via Posterior Adjustment and Label Agreement**（论文 370；Hoyoung Yoon）
在无原始源数据条件下将声学场景分类适配到无标注目标域，应对设备麦克风频响异构。提出 FaSoLa：以后验调整按估计目标先验校正偏差，并以标签一致性按预测一致性优先可靠模型。实验表明可处理多域偏移并显著改善适配性能。

### HRTF/HRIR 个性化与空间上采样

**HRIR-Former: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer**（论文 702；Shaoheng Xu）
从听者稀疏实测 HRIR 预测未测方向的时域 HRIR。HRIR-Former 为 grid-free 双耳 Transformer，含正弦空间特征、Conv1D 精炼与辅助 ITD/ILD 头。在 SONICOM 上相对先前方法改善 NMSE、余弦距离与 ITD/ILD 误差；消融表明最小相位预处理非必要。

**HRTF Personalization via Sim-to-Real Neural Field**（论文 1391；Yoshiki Masuyama）
提出 sim-to-real 神经场 S2RNF：从个体 3D 头模仿真 HRTF 推断受试者特异参数，再用该参数预测真实 HRTF，以降低消声室测量需求。实验称优于原始仿真与现有 sim-to-real 方法。

### 双耳前端与端射鲁棒 DOA

**BiEAR: A Human Auditory-Inspired Adaptive Binaural Front-end for Multi-Speaker Localisation and Distance Estimation**（论文 1618；Hanyu Meng）
BiEAR 受 MOC 反馈启发，用神经控制器在推理中自适应调节双耳听觉滤波器组频率选择性，得到时—频自适应耳表示。在消声与真实房间多说话人定位与距离估计上，相对固定双耳前端提升定位精度与对未见说话人/房间的鲁棒性；可视化显示其随时间强调信息频带。

**End-Fire Degradation-Robust DOA Estimation for Compact Linear Microphone Arrays**（论文 2156；Zheng Wen）
分析紧凑线阵在端射附近 DOA 退化源于远场平面波模型下 TDOA 与方位角非线性映射病态。在 reliability-aware phase transform 框架提出加权增强 SRP 与精炼 TDOA，并采集真实数据集定量评估端射附近性能；实验显著优于基线，代码与数据公开。

## 本场要点

- 手机近麦检测正用 GCC 空间特征显式处理朝向变化，服务无唤醒词交互。
- 无源多源域适应（后验调整 + 标签一致性）针对设备频响异构。
- HRIR/HRTF 个性化并行推进：时域无网格上采样与仿真到实测的神经场。
- 生物启发自适应双耳滤波器组可提升多说话人定位鲁棒性。
- 紧凑线阵端射误差有明确几何病态解释，并可用可靠性感知相位变换缓解。
- 空间音频评测越来越依赖真实房间/端射专用数据与公开代码。

## 覆盖核对

- 224 | Ada-Mic: Orientation-Adaptive and Robust Close-to-Mic Speech Detection on Smartphone Using Generalized Cross-Correlation Features
- 370 | Robust Multi-Source-Free Domain Adaptation via Posterior Adjustment and Label Agreement
- 702 | HRIR-Former: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer
- 1391 | HRTF Personalization via Sim-to-Real Neural Field
- 1618 | BiEAR: A Human Auditory-Inspired Adaptive Binaural Front-end for Multi-Speaker Localisation and Distance Estimation
- 2156 | End-Fire Degradation-Robust DOA Estimation for Compact Linear Microphone Arrays
