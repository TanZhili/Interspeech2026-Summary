# Instruction-following and Controllable Speech Synthesis

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：7
- **论文数**：11
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场围绕指令跟随与可控语音/音效合成：从综艺音效的多智能体分层精炼，到方向跟随 TTS、开放指令表达合成，再到指令监督稳定性、偏好后训练与交叉注意归因诊断。控制对象从全局风格扩展到音素插值、口型—音素对齐的 EMG 合成，以及能耗友好的脉冲声码器。

数据侧强调可扩展伪三元组、野外视听指令语料与漂移过滤；评测侧揭示说话人相似度掩盖口音—情绪纠缠，并主张针对口音的主观/客观度量。生成机制上出现跳跃扩散统一离散时序与连续频谱，以缓解两阶段对齐塌缩与单阶段对齐不稳。

## 技术内容

### 指令/方向控制与数据精炼

**ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows**（论文 561；Li Liu）  
综艺音效依赖人工剪辑，生成方法在时间精度、内容多样与语境理解上不足。ARCHES 用多智能体协作与检索增强，经规划—生成—精炼迭代，含 AURA、AXIS 与 Creative Experience Bank。并构建 VSSE-Bench；摘要称主客观指标显著优于 SOTA。

**Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction**（论文 919；Kenichi Fujita）  
方向跟随 TTS 需相对参考话语按方向文本改表达并保持说话人与内容，但缺相对修改训练数据。提出可扩展伪三元组管线：印象可控 TTS 生成风格变体，LLM 由印象差生成自然语言方向。摘要称仅伪三元组即可稳定保说话人修改，与录音数据结合可进一步提升方向对齐。

**Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions**（论文 930；Junhui Zhang）  
用野外视听数据构建约 1000 小时、覆盖千余细粒度情绪/风格的指令标注语料；无提示 GPT 配合属性思维 token，再由 flow-matching 注入参考音色，并支持说话人微调迁移指令控制。扩展 InstructTTSEval；摘要称指令遵循与表现力强。

**Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering**（论文 1227；Yizhong Geng）  
LLM 改写结构化风格标签时，无约束改写中逾 40% 含语义漂移。提出可控多样化、漂移过滤与属性对齐监督（以声学扰动锚定韵律）。在 InstructTTSEval 中文划分上摘要给出指令跟随与漂移率改善数值，并称三机制互补。

### 后训练稳定、评测诊断与扩散机制

**Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction**（论文 1881；Wenhuan Lu）  
异构自动指标融成标量奖励易导致候选分数分离弱、监督含糊。引入 ChatScorer 辅助奖励与基于间隔的偏好构造；在编解码 TTS 上实例化多种后训练方法，摘要称减少不良输出并提升生成稳定性，同时保持可懂度与说话人相似度竞争力。

**Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems**（论文 2749；Matthew Hayden）  
案例显示两系统 SSM 可比却可能掩盖口音错误；情绪条件可能无意改变口音（口音—情绪纠缠）。用口音 SMOS、嵌入可视化与余弦距离评估：一系统口音变异大，另一稳定。主张针对性主客观度量以揭示隐藏合成错误。

**How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech**（论文 2805；Nityanand Mathur）  
将 DAAM 式交叉注意归因适配到语音扩散模型 CapSpeechTTS，跨层与 ODE 步提取 token 热图。摘要称风格 token 时间方差更低（全局条件）、风格注意与 F0/能量相关、早期步与深层风格条件最强，并在特定层注意熵最低与风格重要性峰值共现。

**Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion**（论文 2875；Jiabao Ai）  
用跳跃扩散在同一过程中以离散跳跃建模时序结构、连续扩散精炼频谱内容。摘要在 LJSpeech 上给出相对 Grad-TTS 的 WER/UTMOSv2 对比，并称完整迭代变体可在分布外慢语速中自适应插入自然停顿而非均匀拉伸。

### 高效声码、音素潜空间与 EMG 合成

**Spiking Vocos: An Energy-Efficient Neural Vocoder**（论文 1086；Yukun Chen）  
脉冲声码器 Spiking Vocos：Spiking ConvNeXt 降 MAC，幅度捷径保留信号动态，自架构蒸馏缩小与 ANN 差距，Temporal Shift 增强时域融合。摘要称性能可比 ANN 而能耗约为其 14.7%。

**PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation**（论文 2277；Nina Goes）  
音素条件 VAE 学习结构化连续潜空间：类条件高斯先验与对比目标促类内紧凑与类间解耦，推理时可插值实现音系类间平滑过渡；摘要称结构在英语数据上可泛化且不牺牲合成质量。

**TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis**（论文 3485；Dongyub Han）  
将帧级对齐音素序列经交叉注意直接注入解码器条件 mel 生成，并给出把语义指导重分配到帧级 EMG 的精炼策略以接入任意音素/文本校正。在 Gaddy silent EMG 上摘要给出 WER 下降并称达 SOTA。

## 本场要点

- 指令/方向控制依赖可扩展伪数据、野外指令语料与漂移过滤。
- 多智能体分层精炼服务综艺音效等强语境生成。
- 偏好后训练需处理异构奖励；说话人相似度可能掩盖口音—情绪纠缠。
- 交叉注意归因揭示风格字幕如何塑造扩散 TTS 声学。
- 跳跃扩散统一时序结构与频谱精炼；脉冲声码关注能效。
- 音素结构潜空间与帧对齐音素条件分别服务可控插值与 EMG 合成。

## 覆盖核对

| id | title |
|---|---|
| 561 | ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows |
| 919 | Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction |
| 930 | Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions |
| 1086 | Spiking Vocos: An Energy-Efficient Neural Vocoder |
| 1227 | Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering |
| 1881 | Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction |
| 2749 | Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems |
| 2805 | How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech |
| 2875 | Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion |
| 2277 | PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation |
| 3485 | TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis |
