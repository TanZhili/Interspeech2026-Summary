# Neural Speech Codecs: Low-Bitrate and Disentangled Coding

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster（Area 6）
- 论文数：9
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场聚焦神经语音编解码的超低码率、内容自适应量化、噪声适配、声调语言 F0 保持、跨编解码互操作、属性解耦、多采样率统一，以及语义引导流式编码。共同目标是在极紧比特预算下保住可懂度、感知质量与下游可用性。

自适应分配出现清浊音驱动量化与伪 VQ 零传输比特；语义侧用对比对齐音素上下文、ASR 监督因果编码或数据增强解耦语义/说话人/韵律。工程互操作上，BridgeCodec 用 Schrödinger Bridge+Mamba 在冻结异构端点间翻译潜变量；统一多采样率模型用适配器与调制器共享 RVQ。噪声与声调则分别用嵌入空间去噪分离与可插拔 F0 注入适配器解决“低码率细节丢失”。

## 技术内容

### 自适应量化、噪声与声调

**VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization**（论文 466；Yang Ai）
按感知敏感度为浊/清帧分配高低码率：浊帧残差标量–向量量化，清帧简单标量量化，全因果可流式。LibriTTS 16 kHz 上低至 1.1 kbps 仍优于基线；相对均匀量化约降码率 27%。

**Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation**（论文 512；Shaokai Li）
FocalSE 在连续嵌入空间做特征去噪、噪声分离与噪声类别识别（ResNet1D-18）。LibriTTS 与 ESC50 上称在低码率与低 SNR 优于既有方法。

**Pitch-Injected Residual Adapter for Tonal Language in Neural Audio Codec**（论文 1224；Chi-Chun Lee）
可插拔 PIRA 向冻结 NAC 注入量化 F0 与清浊信息，膨胀卷积建模变调依赖，CREPE 嵌入损失监督，置信门控抑制入声/清音注入。1.25M–1.65M 参数，五编解码×三声调语言平均 dTER 降 35.7%，开销 ≤0.4 kbps 且保持英语质量。

### 互操作、解耦与多采样率

**BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate**（论文 1338；Zijian Lin）
将跨编解码潜变量翻译写为 Schrödinger Bridge，Mamba 增强 U-Net 捕获长程依赖。极端场景：8 kHz 轻量编码器映射到 48 kHz 解码器、1 kbps，报告优质宽带重建。

**AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation**（论文 1490；Dongmei Wang）
用定制增强分别提取语义、说话人、韵律 token，并以增强损失对齐源与变声语音的语义编码器输出。LibriSpeech test-clean 上 12.5 Hz、三路 token 在重建与解耦上优于 SOTA。

**Unified Neural Speech Coding for Multiple Sampling Rates**（论文 1641；Jiankai Huang）
统一模型支持 16/24/48 kHz：共享编码–解码与 RVQ，采样率感知适配器与变换调制器保证内部网格与表示一致，三阶段渐进训练。性能匹配分采样率专用模型并简化部署。

### 超低码率语义引导与伪量化

**ContextCodec: Content-Focused Context Guidance for Ultra-Low Bitrate Speech Coding**（论文 3355；Chengbin Liang）
双分支解耦声学细节与内容上下文，CLIP 风格对比损失对齐上下文与音素索引；解码各阶段注入上下文，并含轻量自回归潜变量精炼。至 500 bps 仍具质量–可懂度折中，典型手机 CPU RTF 0.4886。

**LitCodec: ASR-Guided Streaming Speech Coding with Unified Quantization**（论文 3474；Son Dang Dinh）
在全因果编码器量化前注入 ASR 监督，用 Finite Scalar Quantization 单码本表示，免双分支。LibriSpeech 流式设定 800 bps、50 token/s：PESQ 2.56、STOI 0.925、WER 2.8%；640 bps 仍 WER 3.1%，而 EnCodec 750 bps 退化至 29.0%。

**An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization**（论文 3506；Xiao-Hang Jiang）
P2PSVQ 含一个 plain VQ 与多个零传输比特的伪 VQ（神经预测辅助 token）。0.5 kbps 重建质量可比竞争编解码器在 2.0 kbps 的表现。

## 本场要点

- 内容/清浊自适应量化比均匀帧码率更省比特。
- 噪声适配可在编解码连续嵌入空间完成去噪与噪声分离。
- 声调语言需要显式 F0 注入以降低编解码 Tone Error。
- BridgeCodec 用最优传输桥接冻结异构编解码端点。
- 数据增强解耦与 ASR/音素对比监督是低码率保语义的两条主路。
- 伪 VQ 与统一多采样率设计分别主攻极低码率效率与部署简化。

## 覆盖核对

- 466 | VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization
- 512 | Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation
- 1224 | Pitch-Injected Residual Adapter for Tonal Language in Neural Audio Codec
- 1338 | BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate
- 1490 | AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation
- 1641 | Unified Neural Speech Coding for Multiple Sampling Rates
- 3355 | ContextCodec: Content-Focused Context Guidance for Ultra-Low Bitrate Speech Coding
- 3474 | LitCodec: ASR-Guided Streaming Speech Coding with Unified Quantization
- 3506 | An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization
