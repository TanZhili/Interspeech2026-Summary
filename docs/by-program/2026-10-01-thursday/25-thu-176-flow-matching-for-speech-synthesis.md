# Flow Matching for Speech Synthesis

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：7
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场以 Flow Matching（流匹配）为主干，覆盖零样本 TTS、表达风格控制、块级并行推理与说话人身份保持等环节。共同取向是：在保持生成质量的同时，用更可控的条件注入、更可靠的轨迹估计，以及与偏好/对比目标对齐的训练，缓解对齐错误、音色泄漏与跨模态风格鸿沟。

推理侧出现“固定块大小不够用”的共识：连续块流匹配虽能兼顾自回归与块内并行，但语音难度非均匀，需用轨迹几何置信度动态截断并重生成不可靠区间。与此并行，统一引导框架试图把数据侧异构增强与模型侧轨迹拉直结合起来，削弱对 Classifier-Free Guidance（CFG）开销的依赖。

风格与副语言控制更强调层次化与解耦：高层说话人属性与低层音质（如 creak）分阶段注入；自然语言提示到声学风格则用最优传输对齐、对比学习与条件流匹配处理一对多映射。鲁棒性与偏好优化则直接针对跳过/重复、文本到参考音频的贴合度，把失败模式或偏好/非偏好信息写进训练目标。

总体看，流匹配已从“能否合成”转向“如何在身份、风格、内容保真与效率之间做可插拔、可诊断的强化”，且多数工作强调与现有流水线兼容而非推倒重来。

## 技术内容

### 属性解耦与层次条件

**Hierarchical Conditional Continuous Normalizing Flows for Creaky Voice Editing under Speaker Identity Preservation**（论文 1341；Petra Wagner）提出层次条件连续归一化流，从结构上解耦高层说话人属性与低层副语言音质。通过分阶段、受控地注入条件信息，约束不同特征对潜表征的影响路径，减少属性间非预期交互，并限制低层编辑向高层特征扩散。以 creak 音质编辑为例，层次方法对音高与性别等高层属性影响更小，从而更好保持感知说话人身份。

### 块级推理与风格跨模态建模

**TC-DBI: A Plug-and-Play Trajectory Confidence-Guided Dynamic Block Inference Strategy for Speech Synthesis with Continuous Block Flow Matching**（论文 1242；Ren Wang）指出固定块大小忽略语音建模难度的非均匀性，易在困难区间导致速度估计不稳。提出由 ODE 积分轨迹“笔直度”导出的 Trajectory Confidence（TC），以及无需改架构的 TC-DBI：截断并重生成不可靠区域以自适应块大小。摘要称 TC 与生成误差强相关，TC-DBI 在可比效率下提升鲁棒性与感知质量。

**Bridging the Gap: A Hierarchical Framework for Cross-Modal Style Modeling in Expressive TTS**（论文 1513；Jiale Chen）针对自然语言提示下的跨模态鸿沟与一对多风格映射，提出 OTAFlow。先用最优传输对齐、对比学习与多任务监督构建统一风格空间，保留实例对应与表达因子可分性；再用条件流匹配刻画残差模态差，由单一提示生成多样声学风格嵌入。接入下游 TTS 骨干后，摘要称在细粒度风格检索与合成风格准确度上显著优于基线。

### 对齐鲁棒、偏好优化与统一引导

**RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching**（论文 3086；Jinhyeok Yang）面向零样本 TTS 中因对齐不完善导致的跳过与重复错误，将对比流匹配扩展为带长度保持的 repeat/skip 潜空间增强，无需外部对齐器或偏好数据即可惩罚真实失败模式。摘要给出 Seed-TTS-eval 上 WER 由 1.44 降至 1.38（约 0.06B 参数），以及 ZERO500 在 NFE=24 时英/韩 CER 分别由 0.48%/0.81% 降至 0.35%/0.57%。

**Improving Flow Matching based Text-to-Speech with Dual-Model Preference Optimization and Classifier-Free Guidance**（论文 2412；Minchuan Chen）认为零样本 TTS 常规范式难以有效融入人类反馈，造成训练目标与评测指标错位。提出用两个独立模型分别建模偏好与非偏好信息的偏好优化，并改进 CFG 以增强对文本与参考音频的贴合。摘要称可显著提升可懂度、说话人相似度与自然度并优于基线。

**Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis**（论文 1015；Zuda Yu）针对流匹配推理延迟高与音色泄漏，提出统一引导：数据侧用异构增强做 Data-guidance，促使语言内容与声学残差解耦；模型侧将轨迹矫正与内在引导目标结合，把条件知识蒸馏进网络权重并拉直推理轨迹，从而消除 CFG 开销。摘要称推理加速近三倍，且说话人相似度相对强基线有提升。

## 本场要点

- 流匹配已成为现代 TTS 核心生成范式，本场重点在推理自适应、风格可控与内容保真。
- 轨迹几何置信度（TC）可驱动块级动态重生成，属可插拔推理策略。
- 层次条件注入用于 creak 等低层音质编辑时，有助于保护音高/性别等身份相关属性。
- OTAFlow 用 OT+对比+条件流匹配处理提示到风格的一对多问题。
- RobustSpeechFlow 与双模型偏好优化分别从失败模式增强与偏好数据利用两侧强化对齐与指标贴合。
- 统一引导框架尝试用数据/模型双路径削弱 CFG 依赖并兼顾速度与音色稳健。

## 覆盖核对

| id | title |
|---|---|
| 1341 | Hierarchical Conditional Continuous Normalizing Flows for Creaky Voice Editing under Speaker Identity Preservation |
| 1242 | TC-DBI: A Plug-and-Play Trajectory Confidence-Guided Dynamic Block Inference Strategy for Speech Synthesis with Continuous Block Flow Matching |
| 1513 | Bridging the Gap: A Hierarchical Framework for Cross-Modal Style Modeling in Expressive TTS |
| 3086 | RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching |
| 2412 | Improving Flow Matching based Text-to-Speech with Dual-Model Preference Optimization and Classifier-Free Guidance |
| 1015 | Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis |
