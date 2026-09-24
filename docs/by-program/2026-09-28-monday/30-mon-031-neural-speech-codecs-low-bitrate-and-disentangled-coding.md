# Neural Speech Codecs: Low-Bitrate and Disentangled Coding

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster
- Area：6
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦神经语音编解码的超低码率、内容自适应量化、噪声适配、声调语言 F0 保持、跨编解码互操作、属性解耦、多采样率统一，以及语义引导流式编码。共同目标是在极紧比特预算下保住可懂度、感知质量与下游可用性。

自适应分配出现清浊音驱动量化与伪 VQ 零传输比特；语义侧用对比对齐音素上下文、ASR 监督因果编码或数据增强解耦语义/说话人/韵律。工程互操作上，BridgeCodec 用 Schrödinger Bridge+Mamba 在冻结异构端点间翻译潜变量；统一多采样率模型用适配器与调制器共享 RVQ。噪声与声调则分别用嵌入空间去噪分离与可插拔 F0 注入适配器解决“低码率细节丢失”。

## 论文技术总结

# VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization

- 论文编号：466
- 报告人：Yang Ai
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26b_interspeech.pdf

## 问题
多数神经语音编解码器对每帧均匀量化，未利用浊音感知更敏感、清音可少码的事实，低码率浪费比特。

## 方法
VoCodec（因果 StreamCodec 风格）：MDCT + 因果 ConvNeXt/LSTM 编码；能量检测器在 F0 搜索带判浊/清；浊帧 RSVQ、清帧简单 SQ，并传 1 bit 浊音标志。掩码训练加速流式。16 kHz 平均约 1.1 kbps（随浊音比约 0.55–1.55）。

## 实验与结果
LibriTTS 1.1 kbps：STOI 0.916、ViSQOL 4.115、MUSHRA 75.18，优于多数流式基线，接近非流式 BigCodec；参数 9.31M、FLOPs 2.62G。相对均匀量化约省 27% 码率。ABX 偏好与 1.5 kbps 他法可竞争。浊/清分项 LSD 显示优先保浊音质量。

## 结论
按浊音驱动分配码率，可在流式低码率下保持高重建质量并显著省比特。

## 点评
把传统 CELP 的浊清分治迁入神经 RSVQ/SQ，感知分配逻辑清晰。能量阈值浊音检测粗，噪声/混响下误判会错配量化器；与内容自适应码率（非仅浊清）仍可结合。


# Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation

- 论文编号：512
- 报告人：Shaokai Li
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26e_interspeech.pdf

## 问题
神经语音编解码器在真实噪声下重建严重退化；多数嵌入空间增强只盯干净目标、忽略待抑制噪声成分，低码率低 SNR 更差。

## 方法
FocalSE 接在 DAC 连续嵌入空间：focal modulation 压缩/解压 + Transformer 得 focal mask，掩蔽噪声嵌入得增强嵌入；SEMamba 过滤后减去增强嵌入分离噪声嵌入；ResNet1D-18 做噪声类别识别。先清洁预训练 DAC，再冻编码器微调 FocalSE。

## 实验与结果
LibriTTS+ESC50，6/2.5 kbps × −5–10 dB：完整 FocalSE 全面优于 DAC、SECE、FD-CBR 及去掉 NR/ND 变体（如 6 kbps/−5 dB：PESQ 2.116、STOI 0.892、SI-SDR 5.403）。噪声分离与识别两者都带来增益。参数约 222M（完整）。

## 结论
在编解码器嵌入空间联合干净恢复、噪声分离与噪声识别，可显著提升低码率低 SNR 重建。

## 点评
相对只学干净掩码，显式分离噪声并分类提供互补监督，切中低 SNR 难点。算力与参数较基线 DAC 明显增大；依赖 DAC 与 ESC50 噪声类型，未见噪声外推需另测。


# Pitch-Injected Residual Adapter for Tonal Language in Neural Audio Codec

- 论文编号：1224
- 报告人：Chi-Chun Lee
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26g_interspeech.pdf

## 问题
神经音频编解码器多在非声调语料上按 PESQ/STOI 训练，对 F0 失真不敏感；声调语言中 F0 区辨词义，且有跨音节变调，端到端微调又易遗忘、数据不足。

## 方法
PIRA：冻结 NAC，在量化潜空间注入残差。WORLD Harvest 抽 F0/UV，F0 量化为 4 bit + 1 bit UV（≤0.4 kbps 开销）；膨胀卷积 Pitch Injector 建模长程变调；置信网络按帧门控（抑制入声/清音）。CREPE 嵌入损失提供音高梯度。参数约 1.25–1.65M，可完全移除以服务非声调场景。

## 实验与结果
闽南/粤/越三语 × EnCodec/DAC/Mimi/WavTokenizer/BigCodec：平均相对降低 codec 引入的 dTER 约 35.7%（如 EnCodec–闽南 dTER 0.267→0.171），F0-RMSE 等同步改善，英语质量基本保持。优于全量微调；消融证实膨胀卷积、置信门控与 CREPE 损失均必要。

## 结论
即插即用的音高残差适配可在不改预训练编解码器的情况下显著恢复声调可懂度，且对非声调部署零损伤。

## 点评
把“感知损失看不见音位 F0”转成显式侧信息注入，适配低资源声调语。依赖前端 F0 估计质量；对入声等非 F0 主线索声调的门控是否过抑需个案检验。


# BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate

- 论文编号：1338
- 报告人：Zijian Lin
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26d_interspeech.pdf

## 问题
神经编解码器编码器–解码器强耦合，异构设备/非对称带宽下无法互通；标准扩散要求高斯先验，会冲掉源潜变量中的语音结构。

## 方法
BridgeCodec：冻结源编码器与目标解码器，用 Schrödinger Bridge 在潜空间做最优传输映射；骨干为 Mamba 增强 U-Net 捕捉长程依赖。两阶段：潜空间对齐再音频域精炼。极端设定：8 kHz 轻量源 → 48 kHz 目标，1 kbps。

## 实验与结果
相对源编解码：STOI 0.23→0.88，MEL 10.01→1.65，SIM 0.81→0.96，MOS 4.12（接近目标 4.24）。1 NFE 仍稳健，利于低延迟。WER 略升（约 2.11 vs 源 1.92）归因于高频生成幻觉。

## 结论
SB + Mamba 可桥接失配、冻结端点，在超低码率下完成窄带→宽带重建并保持互通。

## 点评
把“互通缺口”形式化为潜空间运输而非重训端点，工程价值高。验证集中在一对 8→48 kHz 设定；跨任意编解码器对的泛化与延迟仍取决于桥接模型大小。


# AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation

- 论文编号：1490
- 报告人：Dongmei Wang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26y_interspeech.pdf

## 问题
解耦编解码器常从同一源抽全部属性，交叉干扰大；低帧率表示又难保语义，声转换 WER 偏高。

## 方法
AugCodec：语义支路用扩散 VC 语音 + wav2vec2.0（层平均）经 ConvNeXt 与帧堆叠压缩；说话人支路用同说话人另一句 + ECAPA-TDNN→FSQ；韵律支路保留 STFT 低频 + 粗 hop（160 ms）FSQ。增强损失对齐源与 VC 的语义编码器输出。语义 VQ + 全局说话人/韵律 FSQ，总约 12.5 Hz 三流。

## 实验与结果
LibriSpeech test-clean：AugCodec-3 WER 5.12、PESQ 1.99、UTMOS 3.04（约 400 bps），优于 BiCodec/Mimi 等同帧率设定。去增强损失 WER/PESQ 变差。声转换：12.5 Hz 下 WER 约 5.87 vs BiCodec 65.43。

## 结论
分源增强抽取语义/说话人/韵律可显著加强解耦与低比特重建，并改善声转换可懂度。

## 点评
用“输入变体”强迫属性分离，比同源多头+对抗更直接。推理重建改回原句提取，训练–推理分布差；VC 质量上限会渗入语义支路。


# Unified Neural Speech Coding for Multiple Sampling Rates

- 论文编号：1641
- 报告人：Jiankai Huang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26l_interspeech.pdf

## 问题
多数神经语音编解码器绑定单一采样率；跨 16/24/48 kHz 需外权重采样或多模型，感受野物理时长与频谱统计不一致导致共享量化困难。

## 方法
统一模型：共享 SEANet+LSTM 骨干与单一 RVQ；Sampling-Rate Adapter（SRAT）在波形端可学习对齐到内部 16 kHz 网格；Sampling-Rate Modulator（SRMT）做率条件仿射校准中间特征。三阶段渐进训练（单率→混合等）。

## 实验与结果
1.5 kbps：16 kHz ViSQOL/STOI/PESQ 约 4.21/0.920/2.369；24 kHz 4.22/0.919/2.353；48 kHz 4.14/0.889/2.750，与专用模型可比且单权重。去掉 SRAT/SRMT 或渐进训练均降质。MACs 约 2.1–2.6G，参数 19.65M。

## 结论
轻量率感知适配与调制可使一套权重原生服务多采样率，质量接近专用模型并简化部署。

## 点评
相对“外权重采样或分模型”，把时间网格与特征校准内化进网络，部署更干净。内部锚定 16 kHz 可能对最高频细节仍有折中；消融显示两组件缺一不可。


# ContextCodec: Content-Focused Context Guidance for Ultra-Low Bitrate Speech Coding

- 论文编号：3355
- 报告人：Chengbin Liang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26d_interspeech.pdf

## 问题
超低码率（<1 kbps）下比特需在“听感细节”与“说了什么”间零和分配；声学编解码偏音色，混合语义支路又常泄漏副语言且指导随解码衰减。

## 方法
ContextCodec（DAC 式 GAN+FSQ）：双支路解耦声学与内容上下文；CLIP 风格对比损失将量化上下文对齐 MFA 音素索引以抑副语言泄漏；上下文在每级解码注入；轻量自回归潜变量精炼做分相位归一化量化。目标含 500/1000 bps。

## 实验与结果
约 500 bps：多语/VCTK 上 PESQ/STOI/WER 优于同档混合基线（如 VCTK WER 5.85%）；主观偏好领先。手机 CPU RTF 0.4886。消融显示音素对齐与上下文注入改善可懂度；属性可预测性分析中音素准确率升、说话人等泄漏降。

## 结论
内容优先的上下文引导可在 500 bps 级取得更好的质量–可懂度权衡，并可达移动端实时。

## 点评
把超低码率明确成“先保住语言消息”的设计原则，CLIP–音素对齐比松散 SSL 语义更贴通信场景。依赖强制对齐文本；多语 WER 仍偏高，极限信道下需再压码率与鲁棒性。


# LitCodec: ASR-Guided Streaming Speech Coding with Unified Quantization

- 论文编号：3474
- 报告人：Son Dang Dinh
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dinh26b_interspeech.pdf

## 问题
波形编解码低码率损音素；语义编解码多用非因果 SSL 或双支路，难流式；需同时满足因果、单码本、语义保真。

## 方法
LitCodec：因果 Conformer 编解码 STFT 特征；量化前对嵌入做 CTC ASR 监督（SpecAugment 掩蔽仅加在语义支路）；FSQ 单码本统一语义–声学 token；动态 chunk 训练兼顾流式/离线。推理卸掉 ASR 头。V1 800 bps/50 Hz，V2 640 bps/40 Hz；4 帧@50 Hz 算法延迟 80 ms。

## 实验与结果
LibriSpeech：V1 PESQ 2.56、STOI 0.925、WER 2.8%，流式设定最优；V2 640 bps WER 3.1%（EnCodec 750 bps 为 29.0%）。消融：无 ASR 监督 WER 升至 3.5%；量化后监督弱于量化前；动态 chunk 提升流式稳健。

## 结论
量化前因果 ASR 监督 + FSQ 单流可在流式低码率下同时保住听感与可懂度。

## 点评
相对双支路语义码，把语言结构“压进瓶颈之前”更契合流式单 token 序列。UTMOS/说话人相似度非全面领先；英语 LibriSpeech 外的泛化与噪声条件未充分展示。


# An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

- 论文编号：3506
- 报告人：Xiao-Hang Jiang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26h_interspeech.pdf

## 问题
RVQ 后续级贡献递减却同等耗比特，超低码率（如 0.5 kbps）质量骤降；放大模型可达质量但部署重。

## 方法
P2PSynCodec：MDCT + 轻量 ConvNeXt 编解码；Plain-to-Pseudo Synergistic VQ——1 个 plain VQ 产出可传输基本 token，N 个伪 VQ 用 Conformer+BiLSTM 由基本/先前伪 token 预测辅助 token（零传输比特），码本查找后求和送解码器。训练期可与教师编解码器协同。16 kHz 仅 0.5 kbps。

## 实验与结果
LibriTTS 0.5 kbps：UTMOS 3.947，接近甚至优于若干高复杂度基线，参数 22.99M、FLOPs 3.31G（远小于 BigCodec）。ABX：0.5 kbps 听感可与 2.0 kbps 级编解码竞争。伪 VQ 数量影响分析显示适度 N 提升质量。

## 结论
用可预测伪量化级换“零比特辅 token”，可在超低码率逼近更高码率重建质量且保持轻量。

## 点评
把 RVQ 尾部浪费改成解码端预测，码率会计直接砍到单 VQ。伪 VQ 依赖 plain token 信息量；信道误码时预测链可能级联失败，需额外保护策略。

