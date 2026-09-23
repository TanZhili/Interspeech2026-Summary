# Neural Audio Codec Architectures

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：6
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场聚焦神经音频编解码架构，核心矛盾是：下游语音/音频语言模型需要低帧率、语义可分的离散表示，而极端时间压缩又容易损伤可懂度与频谱细节。多篇工作在低码率下同时追求高保真重建与信息解耦（语义、音色、韵律、残差等流）。

解耦成为主线：多流残差、语义–声学分层码本、说话人解耦加基频注入、以及固定长度全局说话人令牌配合动态帧率，都试图降低说话人信息泄漏、减轻下游 SLM 建模负担，并支持变声与可控合成。低帧率方面出现 5 Hz 级超低帧率编解码，以及把固定帧率自编码器转为动态帧率瓶颈的“弹性时间”机制，以适配信息密度不均的区域。

训练策略上，有工作用预训练理解模型编码器做语义引导与自引导提升码本利用率；也有工作强调单阶段优化或相似度驱动的动态帧聚合。总体趋势是：编解码不再只做重建，而是为生成、变声与长上下文建模提供可控、低冗余的离散接口。

## 技术内容

### 多流解耦与通用低帧率编解码

**MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement**（论文 301；Jingyu Li）  
低码率多尺度残差编解码将语音编码为语义、音色、韵律与残差四流，在有竞争力的低码率下实现高保真重建并具备信息解耦能力。基于该编解码构建两阶段 TTS 语言模型，摘要称在轻量设计与较少数据下相对若干更大模型获得更低 WER 与更好说话人相似度，并支持音色与韵律独立操控的变声。

**OmniCodec: Low Frame Rate Universal Audio Codec with Semantic–Acoustic Disentanglement**（论文 494；Jingbin Hu）  
面向语音、音乐与通用声音的统一低帧率神经编解码。采用分层多码本与语义–声学解耦，利用预训练理解模型的音频编码器，并以自引导策略提升码本利用率与重建。摘要称在与 Mimi 相同码率下重建更优，且表示对下游生成任务更具语义信息。

**SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion**（论文 3108；Hounsu Kim）  
单阶段优化的说话人解耦、基频注入编解码：局部令牌来自预训练自监督编码器的连续预量化特征，经音调编解码注入归一化 F0，并用全局条件反归一化与软标签音调重建目标。在 16/24 kHz 上摘要报告重建有竞争力、零样本变声强，且说话人探测准确率在对比系统中最低，暗示说话人泄漏减少。

### 极端/动态时间压缩与双流令牌化

**U-Codec: Neural Speech Codec under Extreme Temporal Compression for Fast High-Fidelity Speech Generation**（论文 2398；Xusheng Yang）  
U-Codec 在 5 Hz（每秒 5 帧）下追求高保真重建与快速生成。引入基于 Transformer 的帧间长程依赖模块，并系统探索 RVQ 深度与码本大小。接入基于 LLM 的自回归 TTS（全局–局部层级架构）后，摘要称相对高帧率编解码推理加速约 3×，同时保持相似度与自然度。

**Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding**（论文 3031；Dimitrios Bralios）  
提出 Elastic Time，将固定帧率自编码器转为动态帧率：学习轻量潜空间预测器决定可跳过并稍后重建的帧，推理时贪婪选边界。摘要称支持部署期码率控制，并相对基线改善效率–质量权衡，利于生成与长上下文下游建模。

**A Dual-Stream Discrete Neural Codec with Fixed-Length Global Speaker Tokens and Dynamic Frame Rates for Low-Bitrate Speech Tokenization**（论文 3314；Boyang Zhang）  
双流离散编解码：单码本时变令牌流 + 少量固定长度全局说话人令牌；基于相似度的动态帧聚合可在推理时用阈值控令牌率，自适应反聚合恢复基帧率用于波形重建。摘要称低码率下可懂度与音质强，比特率–质量权衡优于固定速率基线并保持说话人相似度。

## 本场要点

- 多流/分层码本把语义、音色、韵律或说话人与内容显式拆开，服务 TTS 与变声。
- OmniCodec 强调跨域统一低帧率与语义–声学解耦。
- U-Codec 验证 5 Hz 离散令牌用于加速 LLM-TTS 的可行性。
- Elastic Time 把固定帧率瓶颈改为可部署调节的动态帧率。
- SDP-Codec 与双流说话人令牌方案共同压低说话人泄漏与令牌冗余。
- 码本利用率、RVQ 配置与动态聚合成为低码率高质量的关键杠杆。

## 覆盖核对

| id | title |
|---|---|
| 301 | MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement |
| 494 | OmniCodec: Low Frame Rate Universal Audio Codec with Semantic–Acoustic Disentanglement |
| 2398 | U-Codec: Neural Speech Codec under Extreme Temporal Compression for Fast High-Fidelity Speech Generation |
| 3031 | Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding |
| 3108 | SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion |
| 3314 | A Dual-Stream Discrete Neural Codec with Fixed-Length Global Speaker Tokens and Dynamic Frame Rates for Low-Bitrate Speech Tokenization |
