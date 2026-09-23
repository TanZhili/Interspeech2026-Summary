# Emotional Speech Synthesis

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：7
- 论文数：11
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场聚焦情感语音合成的可控性、细粒度强度、个性化与评测资源。离散情绪标签正让位于连续 VAD/A-V 轨迹、词级残差向量、轨迹学习与指令嵌入；同时关注文本语义与目标情绪冲突、实时匿名中的情绪泄露，以及听者文化/个体差异。

架构上，扩散/流匹配解码器引入自适应振荡非线性以捕捉尖锐韵律；LoRA/正交分支与双向偏好优化改进条件对比；角色扮演侧出现推理时干预的解耦语音代理。资源与评测上发布大规模情绪 TTS 听感印象数据集，并用 LLM-as-judge 等与人评相关。总体从“说某种情绪”走向可连续、可个性化、可实时控制且可评测的情感表达。

## 技术内容

### 韵律动力学、词级强度与连续控制

**Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS**（论文 1655；Nirmesh J. Shah）  
OscillaTTS 在扩散 TTS 解码器中引入自适应振荡非线性，以可控周期调制建模突发振幅与频率变化，并用线性旁路保持稳定。LJSpeech 与 Emotional Speech Dataset 上主客观均有一致提升。

**Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors**（论文 3079；Ji-Hyun Park）  
用词对齐自监督嵌入中的中性–情绪偏差作为无标注局部韵律线索（ERV），压缩到低维瓶颈并由 RoBERTa 从文本与情绪预测，推理时转为加性隐状态偏移注入中性条件 TTS，实现连续词级强度控制。

**Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA**（论文 1798；Chenchen Wan）  
EO-LoRA 用三个低秩分支对齐效价、唤醒、支配，正交正则鼓励分支捕获不同效应；Flow-DGPO 强化流匹配 TTS 的情绪可控并保持可懂度与说话人相似度。摘要称改善连续与时变控制且数据需求有限。

**ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech**（论文 3088；Gaeun Kim）  
用 RVQ 风格提取器与流匹配在潜风格空间学习中性到目标情绪的连续轨迹，使中间强度在训练中被显式学习。韩/英语料上可控性改善且音质保持，主客观显示表达比基线更稳定。

### 个性化、跨模态一致性与资源

**Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces**（论文 1696；Wangzixi Zhou）  
用交互式遗传算法优化个体 A-V 感知空间，使合成情绪更贴近听者知觉。日/中/印尼参与者评估强调个性化与文化适应相对平均 A-V 的重要性。

**Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models**（论文 1986；Yizhou Peng）  
CCG-CFG 按文本情绪与显式语音情绪不一致程度动态缩放，并以文本情绪替代 dropout 条件；硬样本挖掘蒸馏引导信号。CosyVoice2 上情绪识别准确率最高绝对提升约 12%，主观相对提升约 10%，并保持可懂度与音质。

**A Large-Scale Dataset of Listener Impressions of Emotional TTS**（论文 1521；Erica Cooper）  
首个大规模情绪合成语音质量评估数据集：13 套 SOTA 系统与自然情绪语音共 18,208 样本、五类情绪风格，262 名听者评质量与情绪类别匹配、效价/唤醒/支配等。预训练识别器、质量预测与 LLM-as-judge 与人评相关程度因情绪类别而异。

### 实时匿名、扩散偏好与角色扮演/指令

**DECRA: Dynamic Emotion Control for Real-time Speech Anonymization**（论文 2927；Ghady Nasrallah）  
实时流式变声，用因果 SER 在线预测的连续 VA 轨迹闭环控制韵律，并解耦说话人身份与情绪。端到端可流式，GPU 延迟 <80 ms；摘要称 VA 空间情绪转向优于 SOTA，并展示动态时变控制。

**Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS**（论文 1613；Jiacheng Shi）  
从同文情绪对重排联合学习情绪对齐与情绪对比分数函数，无需辅助奖励模型或额外标注，可无缝接入扩散 TTS 以改善可控与表现力。

**DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention**（论文 1627；Wenqiu Tang）  
对冻结骨干做推理时双层控制向量干预（内部认知转向 + 外部表达渲染）。SpeechRole 与 OmniCharacter 上人格与情绪一致性显著优于端到端微调，自然度缩小与 GPT-4o Audio 差距，且无需训练、可扩展。

**EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis**（论文 1834；Ganjun Liu）  
Emotion2embed 监督语义–声学情绪嵌入覆盖 48 种状态（含细粒度与强度）；ICE-Flow 从自由指令生成声学落地嵌入并接入 LLM 合成管线。摘要称情绪可控与自然度优于强基线。

## 本场要点

- 自适应振荡偏置改善扩散 TTS 对尖锐韵律的建模。
- 词级 ERV、VAD LoRA、轨迹学习与指令嵌入推动细粒度连续控制。
- 个性化 A-V 空间与跨模态一致性引导缓解“一刀切”与文情冲突。
- 大规模听感数据集支撑情绪 TTS 自动质量评估研究。
- DECRA 实现 <80 ms 延迟的实时情绪可控匿名。
- 推理时控制向量与双向偏好优化分别服务角色扮演与扩散情绪对齐。

## 覆盖核对

| id | title |
|---|---|
| 1655 | Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS |
| 3079 | Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors |
| 1798 | Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA |
| 3088 | ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech |
| 1696 | Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces |
| 1986 | Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models |
| 1521 | A Large-Scale Dataset of Listener Impressions of Emotional TTS |
| 2927 | DECRA: Dynamic Emotion Control for Real-time Speech Anonymization |
| 1613 | Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS |
| 1627 | DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention |
| 1834 | EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis |
