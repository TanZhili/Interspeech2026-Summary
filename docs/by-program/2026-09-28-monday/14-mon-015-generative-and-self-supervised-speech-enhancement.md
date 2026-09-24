# Generative and Self-Supervised Speech Enhancement

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：6
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场生成式与自监督语音增强高度集中于 flow matching / 扩散，并把条件信息从浅层噪声特征推向语义、谐波、SSL 与说话人先验。Seed-Enh 在解耦语义（冻结 Whisper）与音色（CAM++）空间做 flow matching 融合；HFMSE 显式提取基频定位与谐波掩码作强条件；PhASE-Flow 直接在 SSL 潜空间对“音素条件声学表示”做流匹配；另有工作用 wav2vec 2.0 + FiLM 锚定扩散反向过程。

噪声鲁棒带宽扩展 VeRe-Flow 用速度对比正则与干净 SSL 表示对齐提供多层干净监督。条件说话人嵌入方面，G-MaP-SE 以 GMM 干净嵌入先验匹配噪声条件嵌入，免注册音频。无监督线则分析 GAN 先验泄漏（对齐噪声先验可减泄漏），并提出多判别器 UFL-GAN 结合自监督辅助。

训练动力学与简化建模同样受关注：SGCM 从连续时间扩散梯度冲突的理论下界导出自适应更新方向；Autonomous Rectified Flow 论证线性插值目标向量场本征时不变，从而去掉显式时间步条件。边缘部署侧 WaveNorm 以因果时域神经 AGC 满足 ITU 响度规范。瓶颈是噪声下条件不可靠、合成—真实域隙、先验泄漏与扩散训练冲突。

## 论文技术总结

# Seed-Enh: Generative Speech Enhancement in Decoupled Semantic and Timbre Spaces

- 论文编号：200
- 报告人：Zengqiang Shang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/shang26_interspeech.pdf

## 问题
多数增强方法直接在声学域（STFT/Mel/波形）操作，噪声与语音纠缠，易学捷径，出现过抑制、高频衰减与背景空洞，并损害说话人音色。解耦语义–音色在合成/变声中有效，但在增强中应用仍有限。

## 方法
Seed-Enh 在解耦语义与音色空间做生成式增强，分三阶段：(1) 语义：将输入后半段（训练时加低复杂度音色扰动）送入冻结 Whisper-Large-v2 编码器，取最后一层 1024 维语义表示；(2) 音色：前半段用 CAM++ 提 192 维全局说话人嵌入，并与对应 Mel 与语义做上下文学习；(3) 融合：以标准高斯为源、语义与音色为条件的 DiT flow matching 生成干净 Mel，经 BigVGAN 合成波形。训练两阶段：先用干净音频学变声/重建，再在 SNR −5~15 dB 的噪声–干净对上微调。推理用 Euler 求解器 25 步；有干净参考时可提更好音色，也可做零样本变声。

## 实验与结果
干净数据为 Emilia（约 101k 小时多语），噪声为 DNS Challenge 库；评测 DNS blindtest 与 LibriTTS+wham，指标含 DNSMOS（OVRL/SIG/BAK）、SIM、CER。Seed-Enh 在两测试集 OVRL 最高（3.095 / 3.193），优于 FullSubNet、TFGridNet、SGMSE、StoRM、SB、AnyEnhance、FlowSE 等。LibriTTS+wham 上 SIM 0.890、CER 0.167。零样本变声在嘈杂参考下明显优于 Seed-VC（OVRL 3.225 vs 2.461，SIM 0.823 vs 0.726）。谱图显示更能抑制噪声并恢复谐波与高频细节。

## 结论
作者认为在解耦语义–音色空间增强可避免声学域纠缠干扰，在抑制噪声的同时恢复高频细节，并支持嘈杂输入下的零样本变声。

## 点评
做法抓住“声学缠绕导致语义/音色互相拖累”这一类问题，把 Whisper 的噪声鲁棒语义与 CAM++/上下文音色分开优化，再 flow matching 融合，比直接在 Mel 上 flow matching（如 FlowSE）更结构化。代价是依赖半段切分与冻结大编码器，且 CER 仍高于判别式模型；生成式路线偏感知质量而非波形保真。


# VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion

- 论文编号：712
- 报告人：Sujin Koo
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/koo26_interspeech.pdf

## 问题
噪声鲁棒带宽扩展（NR-BWE）需同时补全高频并抑噪。标准 flow matching 只单向监督速度场，噪声下速度估计模糊，轨迹易偏离干净语音流形；现有方法在高频重建与抑噪之间仍难兼顾。

## 方法
VeRe-Flow 在 flow matching 上引入多层干净监督。源分布为高斯，目标为干净高分辨率 Mel；以噪声低分辨率 Mel 与冻结 XEUS 的 SSL 特征为条件。骨干在 FLowHigh 上加入 DiC 风格 Conv ResBlock（卷积–Transformer–卷积三明治）。损失：(1) VeCoR：吸引预测速度靠近干净速度、排斥噪声扰动高分辨率对应的噪声速度；(2) REPA 式表示对齐：将第一层 Transformer 隐状态经 MLP 与干净 XEUS 表示做余弦对齐。总损失为两者加权和。波形用 BigVGAN 重建。

## 实验与结果
数据为 Valentini-Botinhao（合并 84 说话人训练），评测官方测试集，输入经低通后下采样至 8 kHz，输出 16 kHz。主配置：高斯先验 + Euler，NFE=2。相对非生成与生成基线（含重训的 FLowHigh、NU-Wave2），提出方法 LSD 最低（1.10）、DNSMOS OVRL 最高（3.12），生成基线中 MOS 最高（4.14±0.65）。消融显示 XEUS 优于 WavLM / Wav2Vec 2.0；Conv ResBlock、XEUS、REPA、VeCoR 逐步带来增益。

## 结论
作者认为在速度与表示两层做干净导向正则，可有效引导 NR-BWE 的生成轨迹；在 Valentini-Botinhao 上全面优于对比的生成基线。据称是首次将速度对比正则用于语音生成。

## 点评
针对“噪声条件下流匹配速度歧义”这一具体失败模式，用干净/噪声速度对比 + 干净 SSL 对齐双向拉回流形，问题定位清晰。与纯条件 CFM 相比，额外监督直接约束轨迹方向。脆弱点在于依赖成对干净高分辨率与语义一致的噪声版本构造 \(u^{\mathrm{noisy}}\)，以及冻结 XEUS 的域匹配；消融也显示各模块对 LSD 与 DNSMOS 的贡献分工不同。


# HFMSE: Harmonic-Guided Speech Enhancement with Flow Matching

- 论文编号：722
- 报告人：Xinhong Li
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/li26l_interspeech.pdf

## 问题
生成式增强依赖条件信息质量：浅层噪声 Mel/波形难以保留谐波等结构，易出伪谱；高层语义条件又假设预训练模型能从噪声中抽准语义，与增强任务前提冲突，形成循环依赖。

## 方法
HFMSE 用显式谐波先验引导 flow matching。条件编码器从随机掩码的干净目标 Mel 与噪声 Mel 提条件；DiT 学习噪声到干净 Mel 的速度场，推理时掩码覆盖全长（无需外部干净参考），配合 CFG 与 BigVGAN 合成。谐波编码器两步：(1) 用 Mel 尺度 Pitch-Harmonic Conversion Matrix（MPCM）做软基频定位；(2) 再与 MPCM 作用生成谐波掩码，经门控聚合后作为持续结构条件注入生成过程，而非仅作后处理或辅助损失。

## 实验与结果
训练约 2000 h（VCTK、LibriTTS、Common Voice、DNS5 干净 + WHAM!/DNS5 噪声，SNR −5~20 dB，40% 加混响），24 kHz 训练、16 kHz 评测。在 DNS Challenge 2020 上对比回归、扩散、离散 token 与 FlowSE 等。HFMSE 在有混响 / 无混响 / 真实录音多数 DNSMOS 与 Spk Sim 上达最优或接近最优（如无混响 OVRL 3.485、Spk Sim 0.958；真实录音 OVRL 3.296）。消融显示去掉谐波编码器比去掉噪声语音条件跌幅更大；去掉门控或掩码训练也会下降。

## 结论
作者认为用物理启发的谐波结构先验作条件，可规避噪声浅层特征与脆弱语义条件的局限，在 DNS 2020 上达到 SOTA 级感知表现。

## 点评
路线选择“低层、噪声相对稳健的结构先验”而非语义 token，直接回应条件不可靠问题，适合重噪/混响下语义提取失败的场景。MPCM + 软基频避免硬 F0 估计的脆性。风险在于强依赖谐波假设：清音/非谐波帧靠扩散掩码缓解，但极端非语音噪声或高度非周期语音上先验可能变弱；相对 FlowSE，收益声称在低 SNR 与混响更明显。


# PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement

- 论文编号：916
- 报告人：Jun Gao
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gao26e_interspeech.pdf

## 问题
现有 flow matching 增强多在 Mel/STFT 域建模，SSL 仅作外部条件。Mel 缺相位、STFT 分布重尾且声学属性缠绕，生成难度大；未充分利用 SSL 低层声学与高层语音层的层级结构。

## 方法
PhASE-Flow 全程在 WavLM-Large SSL 空间工作：第一层 Transformer 作声学表示（生成目标流形），最后一层作语音（phonetic）条件。冻结 WavLM 从噪声输入提两路表示；DiT-based FM 用 OT 路径与 x-pred 目标学习干净声学表示分布，训练时以概率丢弃噪声声学条件以强化语音条件；推理用 4 步 Euler ODE。增强声学表示由独立训练的 Vocos 风格声码器（注意力 + ConvNeXt + iSTFT）还原波形。

## 实验与结果
干净数据约 1021 h（DNS5 LibriVox、VCTK、EARS、LibriSpeech，经 DNSMOS/UTMOS 过滤），噪声与 RIR 在线混合（SNR −5~15 dB，50% 混响）。在 DNS 2020 no-reverb / with-reverb 上对比 TF-GridNet、StoRM、LLaSE-G1、AnyEnhance、FlowSE。no-reverb：UTMOS 4.11、SBS 0.93、LPS 0.97、dWER 2.79%（最低），DNSMOS 3.40。with-reverb：非侵入指标领先生成基线，SpkSim 0.75、dWER 13.19%。消融表明声学 SSL 域优于 Mel/STFT；语音条件在 SSL 域带来全面增益，在 Mel 域则主要改善内容相关指标。

## 结论
作者认为在 SSL 域做 phonetic 条件的声学 flow matching，比频谱域更结构化，能提升感知质量与说话人相似性并抑制幻觉，且仅需四步采样即可高效推理。

## 点评
把“条件 SSL”升级为“在 SSL 流形上生成”，利用层间解耦对齐语义与声学，针对频谱缠绕与表示失配。四步采样是实用卖点。脆弱处：依赖 WavLM 层选择与声码器先验；混响集上生成式方法 SpkSim/dWER 仍可能差于噪声或判别式 TF-GridNet，幻觉问题未完全消除。


# Bridging Self-Supervised Learning and Speech Enhancement: A Wav2Vec2-Conditioned Framework

- 论文编号：964
- 报告人：Shuubham Ojha
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/ojha26_interspeech.pdf

## 问题
扩散式语音增强感知质量较好，但缺少语言学引导，对未见噪声/声学条件泛化弱。常见条件方式为拼接或独立条件网络；SSL 特征虽含噪声下仍可用的音素信息，如何低开销注入扩散 U-Net 仍不明确。

## 方法
在 StoRM（复 STFT 域 OUVE 分数匹配）上，用冻结 wav2vec 2.0 base 从噪声波形提最终 Transformer 层特征（768 维）。经三层 MLP 投影为 FiLM 的 \(\gamma,\beta\)，仅在 U-Net bottleneck 做仿射调制。时序聚合采用由线性–高斯状态空间稳态卡尔曼滤波导出的指数平滑（EMA），\(\alpha=1\) 用于主实验。对比 128/32 通道配置，反向采样 30 步。

## 实验与结果
VoiceBank-DEMAND：相对同宽 StoRM，OURS-128 PESQ 从 2.4862 提到 2.8742（约 +0.4），STOI 亦升；SI-SDR 略降（作者归因于更激进抑噪）。DNSMOS 上 OURS-32 OVRL 3.359 略优于 StoRM-32 的 3.347。LibriMix（32 通道）上相对 StoRM-32 全面更好（PESQ 2.01 vs 1.64 等）。消融：仅 bottleneck FiLM 优于 encoder/decoder 多处调制；EMA 在侵入/非侵入指标间比 mean pool 更均衡。OURS-32 RTF 0.55，可快于实时。

## 结论
作者认为用时序平滑的 wav2vec 2.0 FiLM 条件能以极小算力开销提升扩散增强的 PESQ/STOI/DNSMOS；bottleneck-only 最有效。未来拟扩大评测、主观听音并尝试 WavLM/HuBERT。

## 点评
贡献在于“在何处、如何压缩”注入 SSL：bottleneck + EMA 有理论动机且算力占比极低，工程可落地。相对改表示域的大改方案，这是轻量插件。脆弱点是 SI-SDR 回落与谱上更强抑噪可能伤保真；\(\alpha=1\) 接近极端平滑，条件几乎成全局向量，细粒度音素时序可能被抹掉。


# Text-Annotated Noisy Speech as Supervision: A Dual-Learning Framework for Target-Domain Clean-Free Speech Enhancement

- 论文编号：1259
- 报告人：Xueliang Zhang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26j_interspeech.pdf

## 问题
深度增强多在合成噪声–干净对上训练，难以泛化到真实场景；目标域往往没有与噪声对齐的干净参考。真实噪声+转写（ASR 语料）更易获得，需要无干净目标的目标域适配方法。

## 方法
提出 SwitchSE：在同一 GCRN 复谱映射骨干上，用可学习 switch embedding 沿时间维拼到噪声复谱前端，指示增强模式或 ASR 模式。每个 batch 只含一种数据类型并只激活对应损失：增强模式用时频 L1（对干净谱与波形）；ASR 模式用冻结 WeNet U2++（GigaSpeech）的 CTC 损失，以转写监督增强结果更利于识别。训练时在 VCTK 干净–噪声 batch 与 CHiME-3 噪声–转写 batch 间随机切换；推理时通过 switch token 偏向感知质量或 ASR 友好输出。

## 实验与结果
VCTK 合成混合（SNR −10~10 dB 训练）预训练；用 CHiME-3 真实噪声约 2.9 h（1600 句）微调。表 1：仅 VCTK 的 GCRN 在 CHiME WER 升至 63.66；仅 ASR 微调保住 WER 但 P.808 MOS 差。SwitchSE 的 \(S_{\mathrm{Enh}}\) 在 CHiME 达 P.808 MOS 3.23，\(S_{\mathrm{ASR}}\) WER 20.27，同时 VCTK 上 PESQ/STOI 仍接近原基线。去掉 \(z_s\) 表现居中；加长 switch 到 4 帧可进一步降 WER（18.09）但略损 MOS。

## 结论
作者认为少量真实噪声–转写数据即可做无干净参考的目标域微调，并在感知增强与 ASR 友好之间可控折中，同时保留源域合成集表现。

## 点评
抓住“真实域有转写、无干净参考”的数据现实，用模式开关避免多任务同 batch 互相拉扯，比单纯 ASR 微调或单纯合成预训练更可操作。边界在于 WER 绑定提供训练信号的同一 U2++，反映的是识别器特定友好性而非通用 ASR；骨干仍为 GCRN，更强增强骨干上的迁移有待验证。


# G-MaP-SE: Guided Speech Enhancement via GMM-Based Prior Matching

- 论文编号：2148
- 报告人：Yike Zhu
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26b_interspeech.pdf

## 问题
说话人嵌入条件可加强增强，但常需干净注册音；若直接从噪声语音抽嵌入，噪声与域偏移会使条件脆弱，甚至伤害增强。

## 方法
G-MaP-SE：离线在干净语音嵌入（冻结 ECAPA-TDNN，192 维，ℓ2 归一化）上拟合对角协方差 GMM 先验；推理时对噪声嵌入做温度 softmax 软匹配，用混合权重加权 GMM 均值得到匹配先验嵌入 \(e_{\mathrm{prior}}\)。经轻量门控融合注入 MP-SENet 编码器后的中间 TF 特征。训练时条件类系统均用干净目标嵌入作 oracle 条件以保证稳定；MaP 无训练参数，换数据集只需重拟合先验而无需重训骨干。默认 \(\tau=0.2\)，\(K=192\)。

## 实验与结果
在 VoiceBank+DEMAND 训练并做域内测试，跨域评 DNS 2020 无混响集。域内各条件变体差距较小；跨域上 G-MaP 相对 Noisy-Cond 全面提升，并明显缩小与 Oracle-Cond 的差距（如 WB-PESQ 2.794 vs Noisy-Cond 2.765，接近 Oracle 2.796）。用 DNS 干净数据重拟合先验可在不重训骨干时进一步适配目标域。余弦相似度分布显示 \(e_{\mathrm{prior}}\) 比 \(e_{\mathrm{noisy}}\) 更靠近干净嵌入。消融：\(\tau\) 约 0.2、\(K\) 约 192 较优。

## 结论
作者认为 GMM 先验匹配能在无注册音条件下 refinement 噪声嵌入，提升噪声与域偏移下的引导增强鲁棒性，并可即插即用换先验。

## 点评
把个性化/引导增强的“干净注册”瓶颈换成“干净嵌入分布先验 + 匹配”，部署负担小，且先验可按域替换。设计克制：冻结提取器防止嵌入空间漂移。局限是匹配可能分到次优原型（部分样本相似度不升）；VBD 规模限制先验多样性，域内增益有限，主要价值体现在跨域。


# Analysing Adversarial Priors for Data-driven Unsupervised Speech Enhancement

- 论文编号：2511
- 报告人：Dominik Klement
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/klement26_interspeech.pdf

## 问题
监督增强依赖成对数据，存在训练–部署域差。无监督 GAN 方法用非成对先验，但单分支模型常因一致性损失过强或干净语音先验过弱出现源泄漏（噪声渗入干净估计）。

## 方法
双分支无监督 GAN：共享 DAC 风格编解码器，两条 RoFormer 分支分别估计干净语音与噪声，再用闭式标量 \(\alpha^*,\beta^*\) 线性合成重构噪声输入。三类判别器（干净、噪声、混合）用 LS-GAN 施加分布先验；生成器损失含一致性（多尺度 Mel + SI-SDR）、对抗/特征匹配、以及防止静音塌陷的能量最大化项。编解码器用预训练 DAC 初始化。

## 实验与结果
VCTK+Demand 上相对 MetricGAN-U、MOS-GAN、unSE、unSE+，双分支 PESQ 2.58、COVL 3.08 最高；单分支变体全面更弱。域内干净先验明显优于域外（OOD 干净先验导致噪声泄漏到干净支路）。对齐的噪声先验可把语音→噪声泄漏从 0.23 降到 0.02、噪声→语音从 0.10 降到 0.03（风噪混合实验），减轻过抑制。CBAK 偏低，说明背景伪影仍可能存在。

## 结论
作者认为先验对齐决定分离行为；显式建模噪声并用易采集的环境噪声先验，可减少交叉泄漏并提升感知质量，优于单分支无监督 GAN。

## 点评
把无监督增强的失败模式明确为“一致性 vs 先验”张力下的源泄漏，用噪声支路作 sink 是清晰机制解释。实践上强调环境噪声易采、可对齐，部署友好。脆弱点在干净先验域外匹配差时仍易泄漏，且 CBAK 提示抑噪与自然度之间仍有残余伪影。


# UFL-GAN: A Multi-Discriminator GAN for Unsupervised Speech Enhancement

- 论文编号：2565
- 报告人：Satvik Bejugam
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/bejugam26_interspeech.pdf

## 问题
多数深度增强需成对噪声–干净数据，真实场景难获得。现有无监督 GAN（如 MetricGAN-U、UnSE）或全局判别器收敛慢、难抓局部，或高噪下生成器信息不足。

## 方法
UFL-GAN：生成器为 NTVF，在对数幅度谱上估计幅度掩码并用噪声相位 ISTFT 重建；将预训练 APC（LibriSpeech 960h）表示经线性层拼入 CDF 块以补长时上下文。判别器双路：句级（时间池化后出单一分数）与帧级（每帧打分），采用 CMGAN 风格卷积头与 LSGAN（干净→1，噪声/增强→0）。训练仅用非成对干净与噪声，无参考重建损失。

## 实验与结果
VoiceBank+DEMAND：PESQ-WB 2.64、eSTOI 0.82、CSIG 3.99、CBAK 3.27、COVL 3.35、SI-SNR 15.95、DNSMOS 3.30；eSTOI/CSIG/CBAK/COVL 优于所列无监督基线，PESQ/DNSMOS 接近 QMixCAT，SI-SNR 接近 UnSE。消融：帧级略优于句级；双判别器 + APC 全面最优。

## 结论
作者认为句级与帧级对抗互补，外加 APC 辅助可在无成对数据下达到均衡的侵入/非侵入指标；未来拟扩展到混响与削波。

## 点评
针对“全局打分粗糙、局部打分易整段静音”的张力做双尺度判别，并用 APC 预测未来帧的归纳偏置抗噪，设计动机清楚。仍依赖非成对干净语料而非纯噪声域适应；与 QMixCAT 等伪标签路线比，GAN 先验路线在 PESQ 上未全面领先，优势在复合 MOS 与可懂度。


# Self-adaptive Gradient Conflict Mitigator for Continuous-Time Diffusion Models

- 论文编号：3059
- 报告人：Takumi Hirose
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/hirose26_interspeech.pdf

## 问题
连续时间扩散训练目标是对时间积分的总损失，实际按随机采样的单时刻 \(L_t\) 更新；不同时刻梯度不对齐会导致梯度冲突，拖慢收敛或损害最终性能。

## 方法
提出 DELLBO：对一阶近似的损失下降量取所有概率测度下的最小内积，作为可处理下界。由 Sion 极小极大定理推出最优更新方向为凸包中距原点最近点的单位方向。据此提出 SGCM：用可学习密度 \(m_\alpha(t)=\min\{\lambda s(t),1\}\)（\(s(t)\) 为经验 SNR，\(\lambda=\mathrm{softplus}(\alpha)\)）重加权单时刻梯度，仅增一个可学习参数。

## 实验与结果
在 SGMSE+ 骨干上，WSJ0-CHiME3 与 VoiceBank+DEMAND 对比基线及 SNR / Max-SNR / Min-SNR 加权。训练过程中 SGCM 的 \(\Omega(\mu)\) 最小，最接近理论最优方向。WSJ0-CHiME3 上五项指标均最优（如 PESQ 3.04 vs 基线 2.96）；VBD 上整体最优或接近最优（PESQ 2.85 vs 2.77）。启发式加权往往更差甚至崩溃。

## 结论
作者认为凸包几何刻画了连续时间扩散中的梯度冲突；SGCM 以极低开销逼近最优更新，在语音增强上一致提升质量。

## 点评
贡献偏优化理论：把“时刻间冲突”形式化为 DELLBO 并给出可落地的单参数重加权，与随意 SNR 启发式形成对照。实验排序与 \(\Omega(\mu)\) 一致，论证闭环。局限是经验假设（均值方向近似不变）仅用于动机密度形式；验证主要在 SGMSE+ 增强，向更大曲率感知或非语音扩散任务的推广仍待检验。


# Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow

- 论文编号：1679
- 报告人：Wen Zhang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26z_interspeech.pdf

## 问题
多数生成式增强仍用显式时间步嵌入调节向量场。线性边界锚定路径下目标速度场本应与时间无关；强制时间条件易过拟合轨迹，低 NFE 或数值偏离时恢复变差。

## 方法
Autonomous Rectified Flow（ARF）：直线路径 \(x_t=(1-t)x_0+t(y+\sigma z)\)，目标速度 \(u=y+\sigma z-x_0\) 等价于噪声本身，与 \(t\) 无关。网络 \(v_\theta(x_t,y)\) 不接收时间嵌入，直接回归 \(u\)；推理从噪声先验 \(\phi_1=y+\sigma z\) 沿自治 ODE 用 Euler 回积到干净端。基于 NCSN++，冻结时间步与噪声调度模块；\(\sigma=0.5\)。

## 实验与结果
VoiceBank+DEMAND：NFE=5 时 PESQ 3.11、eSTOI 0.88；NFE=1 时 PESQ 3.00、SI-SDR 19.91，优于同步数 FlowSE/BBED。统一 27.8M 消融中去掉时间嵌入后 NFE=1 RTF 降至 0.02（FlowSE 0.05）。跨域 DNS 上与 FlowSE 总体相当，强混响下两者均明显下降。

## 结论
作者认为线性路径增强中显式时间条件冗余；自治整流流可提升低 NFE 质量与推理效率，并保持与传统流相当的泛化。

## 点评
抓住边界锚定线性流中“目标速度恒定”这一数学结构，把去时间嵌入从工程省参提升为原则选择，对单步/少步生成特别有利。脆弱点在混响等非加性退化上仍弱；与 MeanFlowSE 等单步流的对比显示优势主要来自去掉时间调制而非更大模型。


# WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications

- 论文编号：2115
- 报告人：Harish Rajamani
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/ijjada26_interspeech.pdf

## 问题
传统 AGC 用固定攻放时间常数，在动态音量/噪声下易削波、增益泵动、噪声放大与响应滞后，且对内容无感知。需要低延迟、边缘可部署的内容感知响度归一化。

## 方法
WaveNorm：因果时域端到端 AGC。编码器为三层扩张分组 Conv1D（dilation 2/4/8）+ BN/PReLU，捕捉多尺度包络；GRU（隐层 32）瓶颈保证增益轨迹平滑；对称转置卷积解码器隐式施加增益并重建波形。感受野约 27 样本（~0.56 ms）。训练对齐 ITU-T 响度归一化目标，损失为 0.5 MSE + 0.5 多分辨率谱损失。宣称约 49M MACs、55 KB 内存。

## 实验与结果
相对 WebRTC AGC 与 Carnival AGC：干净 TIMIT 与噪声 VoiceBank+DEMAND 上输出 RMS 更集中、电平不变性更好；时域可变增益示例中过渡更均匀。作 Silero VAD 前端：FPR 最低 0.272、AUC 最高 0.96。作 DFN2/DTLN/GTCRN 前端时 NISQA/DNSMOS 全面提升（如 DFN2 NISQA 3.22→3.57）。输出 ASL 约 −26 dBov、响度 −26~−28 LUFS，符合 P.56/P.79。

## 结论
作者认为轻量时域神经 AGC 可在边缘实时稳定归一化响度，并作为模型无关前端改善 VAD 与抑噪。

## 点评
把 AGC 从启发式包络检测换成内容感知波形映射，并用 RMS 分布与下游任务验证“电平不变性”的实用价值，工程导向明确。复杂度数字利于嵌入式选型。局限是主结果偏分布与下游，缺少与传统 AGC 在主观泵动/可懂度上的系统听感对照；训练依赖 DNS3 等构造的宽动态数据，极端远场+强噪仍需实机验证。

