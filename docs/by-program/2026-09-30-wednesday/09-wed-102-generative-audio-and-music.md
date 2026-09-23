# Generative Audio and Music

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：（跨领域长文 Oral；程序未单列 Area 编号）
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场为跨领域长文 oral，主题是生成音频与音乐：从控制、主体性与评测的综述，到否定理解失败、整曲生成、连续扩散口语语言模型扩展律，以及视频到音频的统一 Foley 框架。主线是超越纯文本提示，追求可解释、可编辑的条件与语义忠实性。

综述强调文本提示易用但音乐上含糊，创作者需要 MIDI、歌词、分轨、参考音频与合成器旋钮等控制；评测也不能只靠感知质量与 Fréchet 距离。实证工作则暴露 T2A 模型对否定提示几乎无效（否定与肯定输出近乎声学相同），整曲生成用半自回归块流匹配与跨对偏好优化改善歌词–人声对齐与多偏好训练，连续扩散 SLM 在大规模数据下可产生富情感多说话人多语语音但长程连贯仍难，视频到音频则整合多模态控制、帧级时序对齐与细粒度语义。

## 技术内容

### 综述与否定理解基准

**Beyond Text-to-Music: Control, Agency, and Evaluation in Generative Audio**（Survey Talk；Lauri Juvela）  
综述生成音频从语音合成扩展到音乐、歌声、环境声、乐器与制作，并与 TTS、变声、增强、分离、韵律与神经声码等语音问题对照。覆盖基于神经编解码的音频语言模型、扩散/流匹配、Transformer 与可微 DSP；中心主题是控制与评测：为何仅有感知质量与 Fréchet 距离不足，以及条件遵循、音乐连贯与创作主体性如何指导交互式音乐工具。

**Negation in Audio Generation Models**（论文 1756；Bikash Dutta）  
提出 Audio Negation Benchmark：约一百万条否定提示，覆盖四类否定与三种否定范围，源自 AudioCaps。人工标注子集中 99.6% 正确引入目标否定。用 AQA 协议探测否定事件有无；对 AudioGen、AudioLDM2、TangoFlux 的摘要结论是否定音频 AQA 召回均低于 0.05，否定与肯定提示产生近乎相同声景，否定理解仍是开放问题。

### 整曲生成、连续扩散 SLM 与视频到音频

**DiffRhythm 2: Efficient and High Fidelity Song Generation via Block Flow Matching**（论文 128；Yuepeng Jiang）  
半自回归块流匹配实现忠实歌词–人声对齐而无需时长标签或显式约束；5 Hz 音乐 VAE 支持长序列高保真重建。提出跨对偏好优化在同一模型中联合学习多奖励维度偏好对，以及随机块表示对齐损失改善乐感与结构。摘要称可生成最长约 210 秒歌曲，主客观优于开源模型且保持效率。

**Scaling Properties of Continuous Diffusion Spoken Language Models**（论文 2980；Eeshan Gunesh Dhekane）  
探索连续扩散口语 LM 是否比离散 AR 更可行，并提出音素 Jensen-Shannon 散度（pJSD）度量语言质量。摘要称 CD SLM 对验证损失与 pJSD 呈现扩展律，最优 token–参数比随算力升高而下降；扩展至约 160 亿参数与数千万小时会话数据可生成富情感、韵律、多说话人、多语语音，但长篇连贯仍是重大挑战。

**FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision**（论文 112；Shiyao Wang）  
统一 VTA 框架：条件注入支持音频控制 VTA 与 Foley 扩展，多模态动态掩码保持训练同步，副词式数据增强结合信号处理与 LLM 强化细粒度文本监督。在 AudioCaps、VGGSound、Greatest Hits 上摘要称可控 VTA 表现有竞争力。

## 本场要点

- 综述把控制与评测（条件遵循、连贯、主体性）置于文本提示之上。
- 否定基准显示主流 T2A 对否定几乎无效（AQA 召回 <0.05）。
- DiffRhythm 2 用块流匹配与跨对偏好优化生成最长约 210 秒歌曲。
- 连续扩散 SLM 呈扩展律，大规模下仍难保证长程连贯。
- FoleyGenEx 统一多模态控制、时序对齐与细粒度语义的视频到音频。

## 覆盖核对

| id | title |
|---|---|
| Survey Talk | Beyond Text-to-Music: Control, Agency, and Evaluation in Generative Audio |
| 1756 | Negation in Audio Generation Models |
| 128 | DiffRhythm 2: Efficient and High Fidelity Song Generation via Block Flow Matching |
| 2980 | Scaling Properties of Continuous Diffusion Spoken Language Models |
| 112 | FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision |
