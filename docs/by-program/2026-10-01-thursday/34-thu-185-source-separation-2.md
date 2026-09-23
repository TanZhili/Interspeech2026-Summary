# Source Separation 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：5
- 论文数：8
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场源分离与目标提取从判别式高指标、听感偏弱，走向一步生成校正、音视频流匹配、伪空间条件、编解码器层级网格，以及仅用说话人身份监督。部署场景覆盖智能眼镜点引导提取、半监督联合分离–日记化，以及远场回传中的自身语音消除（OVC）。

监督信号多样化：干净波形不再唯一——对比对齐说话人嵌入、清洁混合+环境噪声半监督、空间点查询与硬负空间采样均出现。效率上强调一步 MeanFlow/流匹配、压缩潜空间 RVQ 网格与毫秒级延迟掩蔽器。

## 技术内容

### 生成校正、视听与伪空间条件

**MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation**（论文 1150；Dohwan Kim）用条件平均速度场一步把判别估计映射到干净语音流形；Data-Space Optimization 结合更长位移区间的 xᵣ 损失与终点 SI-SDR。摘要称以最小算力开销同时提升信号保真与听感，域内/域外均达 SOTA。

**AV-FlowSep: Audio-Visual Target Speaker Separation via Flow Matching**（论文 1960；Pattara Tipaksorn）条件流匹配学习从混合到干净 mel 的直接传输路径，潜空间 Diffusion Transformer 经交叉注意力融入目标说话人时序视觉线索。摘要称最少一步推理即可高感知质量，在 VoxCeleb2/LRS2 的语音–语音与语音–噪声设定上具竞争力或更优并跨数据泛化。

**Pseudo-Spatially Conditioned TF-Locoformer with MHCA+FiLM Fusion for Single-Channel Speech Separation**（论文 2027；Daichi Nitsu）训练时用多通道作特权信息，对比三元组目标预训练单通道编码器以反映空间配置；推理仅单通道。伪空间嵌入经 MHCA+FiLM 条件化 TF-Locoformer。WHAMR! 上 SI-SNRi 由 17.4→17.7 dB（S）、18.6→18.9 dB（M），增参约 1.0–1.2M。

### 编解码器结构、身份监督与空间/日记化

**Improving Audio Codec-based Speech Separation By Stacking Residual Vector Quantization Layers**（论文 2296；Nhu Minh Phuong Dinh）提出 RVQ-Grid：逐层 RVQ 向量堆成 3D 网格并用双轴循环块处理，保留粗到细层次。WSJ0-2Mix 相对既有编解码方法 SI-SDRi +3.6 dB；同编解码条件下 ASR WER 8.6%，推理 MAC 相对 SepFormer 约降 6×。

**Speaker Identity as Sole Supervision for Speech Separation**（论文 2620；Christoph Boeddeker）仅用说话人身份对比目标：分离输出嵌入与辅助话语对齐、批次内负样本排斥竞争说话人；推理不需嵌入，仍为说话人无关分离器。摘要称可从零训到满意性能，并对噪声混合上微调监督模型进一步提升。

**SPOT-TSE: Spatial Point-Guided Target Speech Extraction**（论文 3266；Taewon Ryu）以距离–方位连续空间点查询指定目标，空间查询编码与邻近加权软目标稳定条件，硬负空间采样处理重叠。模拟智能眼镜数据上提升空间选择性、降低 WER，并相对循环基线降算力。

**Semi-Supervised Joint Separation and Diarization for Multichannel Noisy Speech Mixtures**（论文 3308；Yuto Nozaki）半监督扩展 neural FCASA：用清洁语音混合与环境噪声录音监督抑噪，同时无监督分离语音源，目标源于统一多通道生成模型。摘要称多项指标优于 neural FCASA。

**Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement**（论文 3430；Mads Østergaard）定义 OVC：从噪声多说话人混合中去除已注册目标说话人并保留其余语音，算法延迟仅 2 ms。对比 TD-SpeakerBeam 与更轻的 Mamba-MinGRU 掩蔽器；线性 RNN 辅助编码器改进 SDR 与预测 MOS 并降算力。

## 本场要点

- 一步 MeanFlow/流匹配校正弥合判别指标与听感差距。
- 视觉线索与伪空间嵌入为单通道/目标提取提供条件。
- RVQ 层级网格保留编解码粗细结构并显著降推理算力。
- 仅说话人身份监督可训练说话人无关分离器。
- 点引导 TSE 与半监督联合日记化面向可穿戴与嘈杂会议。
- OVC 作为 TSE 补集服务远场低延迟自身语音伪影消除。

## 覆盖核对

| id | title |
|---|---|
| 1150 | MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation |
| 1960 | AV-FlowSep: Audio-Visual Target Speaker Separation via Flow Matching |
| 2027 | Pseudo-Spatially Conditioned TF-Locoformer with MHCA+FiLM Fusion for Single-Channel Speech Separation |
| 2296 | Improving Audio Codec-based Speech Separation By Stacking Residual Vector Quantization Layers |
| 2620 | Speaker Identity as Sole Supervision for Speech Separation |
| 3266 | SPOT-TSE: Spatial Point-Guided Target Speech Extraction |
| 3308 | Semi-Supervised Joint Separation and Diarization for Multichannel Noisy Speech Mixtures |
| 3430 | Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement |
