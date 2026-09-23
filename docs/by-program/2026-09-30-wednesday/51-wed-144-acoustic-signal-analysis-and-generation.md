# Acoustic Signal Analysis and Generation

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：5
- 论文数：7
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要，不补写摘要未给出的数字与细节。

## 技术趋势

本场围绕声学信号的分析、表征与生成展开，覆盖量化部署、语言—音频预训练、乐器音色迁移、语音表征编解码、助听场景音乐增强、指令式时域编辑，以及判别器驱动的扩散生成。共同主线是：在保持任务性能或声学保真的同时，把控制粒度、表征紧凑性与部署效率一并推进。

在表示学习一侧，ProLAP 用概率嵌入刻画音频与文本的多对多层次关系，并配套层次诊断数据；SARA 则用双流 VAE 融合冻结 SSL 语义锚与残差声学编码，缓解纯声学编解码与纯语义 token 之间的内容—保真权衡。二者都在“语义约束 + 声学细节”的张力下寻找更可生成的潜空间。

在可控生成与编辑一侧，AdaTT 针对乐器音色迁移中结构控制与目标音色冲突，做目标自适应的音高/响度控制缩放；EMKR 在 Stable Audio Open 上实现加、删、替、移、延等时域局部编辑，并强调未编辑区保持。另有工作把冻结的噪声条件语音分类器子网络化为扩散骨干，缩短判别与条件生成之间的模型栈。

面向实际听感与部署，BeatGain 按主拍节奏放大打击事件、削弱弱拍外事件，服务人工耳蜗用户的节奏清晰度；ESC 则针对音频激活校准范围过大导致的量化信息损失，用进化策略做激活缩放，支撑 INT8 无损与近无损 INT4。整体上，本场把“听得清、编得准、压得住、控得住”连成一条从分析到生成的闭环。

## 技术内容

### 高效部署与语言—音频表征

**Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models**（论文 119；Lucas RAKOTOARIVONY）  
针对语音模型量化中音频激活校准范围过大、标准校准易丢信息的问题，提出 ESC：将激活缩放建模为优化问题，并以进化策略驱动两步局部—全局方案求解。摘要称 ESC 在全 INT8 下可保持性能不变，且是首个在多语音任务上对全 INT4 达到近无损的校准方法；与 PTQ 结合后，在 AST 模型上相对精度下降约 1%。

**ProLAP: Probabilistic Language-Audio Pre-Training**（论文 845；Toranosuke Manabe）  
指出语言—音频通常被假设为一一对应，而实际是多对多且存在层次，音源叠加使层次建模更难。ProLAP 在联合嵌入空间用概率分布表示输入，并引入 AudioCaps-HC、AudioCaps-EC 诊断集。通过音频遍历与包含性测试，摘要称其在语义层次刻画上显著优于确定性基线，并给出直观不确定性估计，同时不牺牲音文检索性能。

### 乐器/语音生成与表征融合

**AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control**（论文 1828；Dabin Kim）  
认为细粒度结构条件下的音色模糊来自乐器特有表达细节与目标音色冲突（如小提琴音高主导颤音施加到长笛）。AdaTT 在 ControlNet 框架内，用文本提示按帧缩放音高与响度控制以匹配目标乐器，并给出半自动数据管线教模型哪些细节该变/该留。结果称音色保真与自然度更优，同时保留谱面级内容。

**SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations**（论文 2082；Peijie Chen）  
零样本 TTS 依赖稳健语音表征；声学 codec 保真但缺语言约束，SSL 语义 token 对齐准但丢声学信息。SARA 用双流 VAE 直接融合冻结 SSL 语义锚与专用残差声学编码器，无需复杂正则即可得到紧凑潜空间。摘要称重建优于强基线；下游零样本 TTS 自然、有表现力，加速推理下仍稳健，速度与算力权衡更有利。

**Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation**（论文 3448；Rostislav Makarov）  
经典 classifier guidance 需分类器与扩散模型分开训练。本文冻结 log-Mel 空间噪声条件分类器，挂接轻量子网络复用中间表示，仅以 Denoising Score Matching 训练该子网络。摘要称预训练分类器可被改用于条件生成，在单骨干下实现高质量语音，并降低内存与计算开销。

### 听感增强与时域指令编辑

**BeatGain - A Rhythmic Pattern Enhancement Algorithm for Music Listening with Cochlear Implants**（论文 2713；Benjamin Lentz）  
人工耳蜗用户音乐感知有限，常偏好清晰节拍与较低乐器复杂度。BeatGain 在混音框架内放大与主拍对齐的打击事件、衰减较弱非拍事件。客观指标显示复杂度低于原信号与基线 remix；听音实验中节奏清晰度全面显著优于对照，整体质量除一项外亦更优，支持节奏导向增强作为 CI 音乐增强的补充。

**Edit the Moment, Keep the Rest: Time-Localized Audio Editing via Instruction**（论文 3044；Jinwoo Jung）  
时域精确控制的音频编辑研究较少。EMKR 基于 Stable Audio Open，支持增删替换移动与延长；用（指令、输入、目标）三元组训练，指令携带编辑时刻，并引入显式编辑区间与源事件掩码以在移动/延长时保留原事件实例。真实数据混合实验称可对复调音频做约 100 ms 精度的局部编辑并保持未编辑区。

## 本场要点

- 语音量化校准需针对音频激活大动态范围；ESC 把缩放做成进化策略优化。
- 语言—音频层次关系适合用概率嵌入刻画，并需专门诊断任务验证。
- 音色迁移中结构控制应随目标乐器自适应，避免源乐器表达细节硬套。
- 语义锚 + 残差声学编码可缓解 TTS tokenizer 的内容错误与保真损失权衡。
- 节奏结构增强对 CI 用户音乐听感有独立价值；指令式时域编辑强调“改局部、留其余”。
- 冻结分类器可作扩散骨干，缩短判别模型与生成模型之间的鸿沟。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 119 | Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models |
| 845 | ProLAP: Probabilistic Language-Audio Pre-Training |
| 1828 | AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control |
| 2082 | SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations |
| 2713 | BeatGain - A Rhythmic Pattern Enhancement Algorithm for Music Listening with Cochlear Implants |
| 3044 | Edit the Moment, Keep the Rest: Time-Localized Audio Editing via Instruction |
| 3448 | Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation |
