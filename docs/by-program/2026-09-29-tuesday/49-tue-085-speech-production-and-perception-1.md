# Speech Production and Perception 1

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：1
- **论文数**：10
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场连接语音产生物理建模、自声感知与质量/相似度的人机对齐，并延伸到 EEG 注意切换解码与唇读转语音。产生侧关注一维噪声尺度因子相对三维湍流仿真的适用边界、声带接触/脱接触的更渐进几何建模，以及颈皮振动对耳周麦克风拾音的影响。

感知与评测侧用交互式滑杆逼近自然自声、大规模实验拆解“讨厌自己录音”的回放—意象差距，并检验 MOS 预测与说话人嵌入距离是否对齐人类。神经与视觉接口则提出状态引导的注意切换解码框架，以及用文本—视频对齐把冻结 TTS 改造为唇同步语音生成器；SSL 模型的跨语言发音编码则用芬兰语—俄语 EMA 探测。

趋势是：物理与感知约束进入合成与评测；“像人一样听/像自己一样听”成为模型对齐目标；多模态与脑机接口继续服务可穿戴听力与无声语音应用。

## 技术内容

### 发声物理与耳周拾音

**Noise Scaling Factor for the One-Dimensional Voice Production Model**（论文 559；Tsukasa Yoshinaga）  
声门湍流噪声影响音质；一维噪声模型中尺度因子很少对照三维显式湍流发声仿真检验。对元音 /a/、/u/ 评估尺度因子：正常发声 /a/ 上传统因子与 3D 结果吻合较好；不完全闭合的气声及 /u/ 声门上收缩配置下最优因子偏离传统值。结论是一维湍流噪声建模需随声道流动配置调整。

**Improved modeling of vocal fold contacting and de-contacting in a geometric vocal fold model**（论文 753；Tianyi Zhang）  
面向更自然的发音合成，提出生物力学动机的声门部分接触阶段更渐进开闭，并支持声门面积波形左右偏斜。在发音合成器中与无改进机制模型做感知 A/B；摘要给出新模型偏好比例与五分制 MOS 均值对比，显示新模型更受偏好。

**The Effect of Neck Skin Vibration on the Periauricular Acoustic Receiver**（论文 170；Ruoyan Li）  
自说时除口腔辐射外还有颈及表面结构振动。用头表麦克风阵列，结合假头、真人与仿真比较，发现靠近颈部的耳周接收器检测到与颈皮振动相关的显著空气传播分量，提示仅把口腔辐射当作唯一声源的自说仿真需修正。

### 自声感知、MOS 与说话人相似度对齐

**SELFIX: An Interactive System for Natural Self-Voice Approximation**（论文 1395；Pavo Orepic）  
录音自声不适因天然发声经头振滤波；既往频谱均衡难收敛到通用滤波器。SELFIX 用音高、声道等感知动机维度约束搜索；初步研究（N=25）中被试反复调节四个随机无标签滑杆，一致性调整与高匹配/置信支持有效性。摘要称所有人提升低频，男性还降音高并增长声道，表明自声逼近超出单纯频谱均衡。

**What Makes Us Hate Our Own Voice? Large-scale experiments on Playback–Imagery Gaps and Individual--Speech Feature Effects**（论文 973；Koki Fukuda）  
以日本被试（N=459）比较录音回放与同句发声意象的印象评分。回放比意象产生更负面情感评价（尤其不适），自我相似感未呈现相同模式；探索性特质—声学交互提示听者对声学线索权重因人而异，差距亦受顺序与块结构调制。

**Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations**（论文 1478；Reo Shimizu）  
对语音施加声学劣化、韵律错误及音高/语速等说话人特性操控，比较人类与 MOS 预测模型。多数模型能跟踪声学劣化，但对韵律错误不敏感；对说话人特性出现双分离：模型有人类没有的强平均 F0 偏置，却对人类敏感的语速与 F0 变异不敏感。

**Do speech foundation models perceive speaker similarity as humans do?**（论文 1172；Hayato Yagi）  
比较 40 余个模型说话人嵌入距离与人类连续说话人相似度评分的对齐，并分析何种模型配置更贴近人类感知，为更感知接地的基础模型提供依据。

### 注意解码、唇读合成与 SSL 发音编码

**SGAD: A State-Guided Adaptive Decision Framework for Robust EEG-Based Auditory Attention Switch Decoding**（论文 1815；Yuting Ding）  
EEG 非平稳与混杂控制不足限制注意切换解码。SGAD 经因果状态检测推断注意转移态，并用状态引导自适应门控动态调节时间平滑；引入六层评估协议检验跨音频/说话人/被试泛化。摘要称提升准确与稳定并保持低响应延迟，同时提示数据划分相关偏置。

**LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech**（论文 518；Souvik Ghosh）  
将冻结预训练 TTS 适配为唇同步语音生成器：用文本—视频对齐模块对齐音素表征与唇嵌入，弥合冻结 VSR 与 TTS 的模块鸿沟。摘要称在多英语基准达 SOTA 且训练数据显著更少，并展示法/德/西/葡零样本多语言唇读转语音能力。

**How Bilingual Are SSL Speech Models? Cross-Lingual Probing of Articulatory Encoding with Finnish and Russian EMA**（论文 1324；Ruchi Pandey）  
用芬兰语—俄语双语者 EMA 评估 SSL 潜表征与发音运动相关。摘要称即便约 5 分钟训练数据也有较强预测（Pearson r 最高约 0.68），多语言模型优于单语，中间层最有效编码发音特征，舌运动比唇更可预测；任务类型与语言水平亦影响表现。

## 本场要点

- 一维发声噪声尺度因子需随气声与声道收缩配置调整。
- 更渐进的声带接触/脱接触可提升合成句感知偏好。
- 耳周拾音不可忽略颈皮振动相关空气分量。
- 自声不适与回放—意象差距、交互式感知维度调节相关。
- MOS 与说话人嵌入对齐暴露相对人类的韵律/特性盲区。
- SGAD、LipAdapter 与 EMA 探测分别推进注意解码、唇读合成与 SSL 可解释发音编码。

## 覆盖核对

| id | title |
|---|---|
| 1395 | SELFIX: An Interactive System for Natural Self-Voice Approximation |
| 559 | Noise Scaling Factor for the One-Dimensional Voice Production Model |
| 753 | Improved modeling of vocal fold contacting and de-contacting in a geometric vocal fold model |
| 170 | The Effect of Neck Skin Vibration on the Periauricular Acoustic Receiver |
| 1478 | Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations |
| 1172 | Do speech foundation models perceive speaker similarity as humans do? |
| 973 | What Makes Us Hate Our Own Voice? Large-scale experiments on Playback–Imagery Gaps and Individual--Speech Feature Effects |
| 1815 | SGAD: A State-Guided Adaptive Decision Framework for Robust EEG-Based Auditory Attention Switch Decoding |
| 518 | LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech |
| 1324 | How Bilingual Are SSL Speech Models? Cross-Lingual Probing of Articulatory Encoding with Finnish and Russian EMA |
