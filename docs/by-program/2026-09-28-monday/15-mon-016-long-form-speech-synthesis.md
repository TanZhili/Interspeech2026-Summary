# Long-Form Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：7
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕长文本、多角色与细粒度韵律控制下的语音合成展开。与单句 TTS 不同，长篇有声书与对话合成更强调跨句语境、说话人一致性与边界自然度；多篇工作从训练期建模与推理期补丁两条路径切入。

一类工作把“长上下文”做成显式机制：有的引入章节级语境与风格解耦，有的在不重训长文本的前提下用 soft attention prior、有状态分句推理与历史文本编码维持韵律连贯。另一类则转向系统编排，用多智能体闭环做角色建档、合成质检与人机反馈改写，把长音频叙事当作生产流程而非单模型任务。

细粒度控制是本场另一主线。Flow-matching / LLM-based TTS 在强调、词级强度与节奏上仍受数据稀缺与声学先验冲突制约；多篇采用 SFT→偏好对齐→在线强化学习的级联优化，并用韵律工具或自建偏好对提供奖励。动态韵律预测则强调“基于已生成语音再预测当前音节韵律”，以提升个性化相似度。

与“把合成做得更好”并列的是“把问题说清楚”：有工作用大规模匹配语料揭示神经 TTS 在全局 F0 变异压缩与局部音高翻转增多、元音空间收缩等层次上的解离；也有工作为非人声/设计声效转换提供数据与基准。内存瓶颈同样突出——分钟级对话在密 mel 上的条件流匹配迫使分块，压缩潜空间成为可行折中。

总体看，长篇合成正从“能念完”转向“可控、可检、可评”：语境与状态化推理解决连贯性，偏好/RL 解决局部强调，评测与数据则约束指标掩盖的真实失真。

## 论文技术总结

# audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook

- 论文编号：2125
- 报告人：Min Liu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26p_interspeech.pdf

## 问题
现有 TTS 偏单句，有声书多角色长篇缺少句间上下文建模与细粒度情感/音量/语速控制；提示音易把韵律绑定到 prompt，损害语义–韵律对齐与角色一致性。

## 方法
Audiobook-CC 基于 cosyvoice2（改用 BigVGAN）：AR 语音 LM 输入说话人嵌入 \(V\)（Cam++，来自同说话人但语义无关句）、前后文文本序列 seqC、离散属性控制 seqE（九类情感×四级强度、音量、语速）、文本与语音 token。解耦训练：timbre/persona 来自 \(V\)，韵律由当前文本与上下文决定。控制标签由 LLM 解析后规则归一；用自蒸馏合成高强度情感数据（PER<2%、SS>0.7 等过滤）缓解稀缺。三阶段微调（约 100 万→15 万上下文+指令→自蒸馏增强小时量级数据）。

## 实验与结果
章节级 M-MOS 4.25（Infer-ctx&inst），相对最强基线约 14% 相对提升；对话 S-MOS 4.11。ABX 上 Infer-ctx&inst 章节偏好 73.0%。解耦相对非解耦显著提高 S-MOS（约 3.45→3.93）；高强度–低强度情感区分在 Text-Unrelated 上明显强于 cosyvoice2；自蒸馏降低 PER 并恢复情感 F1。

## 结论
作者认为上下文机制、风格–提示解耦与自蒸馏共同提升多角色有声书的连贯性、语义对齐与情感可控性。

## 点评
针对有声书特有的“角色稳定 + 语义驱动韵律 + 长文连贯”三角，用无关内容说话人嵌入解耦是关键设计。控制离散化便于组合指令。依赖大规模内部有声书/剧集数据与章节标注，复现门槛高；后文上下文在推理时依赖已知剧本，对开放式生成需另想办法。


# MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data

- 论文编号：1461
- 报告人：Jing Yao Li
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26f_interspeech.pdf

## 问题
神经 TTS 短句质量高，长文易韵律漂移、说话人不一致与句界伪影。压缩序列、加长上下文或朴素分句拼接各有分辨率损失、硬掩码或需改架构/重训的问题。

## 方法
MagpieTTS-LF：纯推理期扩展 MagpieTTS（Koel-TTS 式编解码器 + 神经编解码 token）。(1) 软注意力先验：在上一时刻最高注意力位置邻域赋固定权重，远处给 \(\varepsilon>0\)，以 \(\lambda\log P_t\) 加到 softmax，引导单调对齐且保留远距上下文；(2) 有状态分块：跨句传递历史文本 token、对应编码器隐状态与注意力跟踪 \(\tau\)；(3) 历史文本编码支持篇章级韵律规划。无需长文重训或改结构。

## 实验与结果
自建 Long-Form HifiTTS（约 20 段 3–4 分钟 MLS 拼接）上对比 XTTS、Qwen3-TTS、VibeVoice。WER/CER 最低（0.025/0.012）；WavLM SSIM 最高且最稳；句界能量跳变 14.04 dB，综合 PBD 最优。全程说话人相似与 UTMOSv2 更稳、方差更小。超参：\(\varepsilon=0.1\)，\(w=(0.2,0.8,1.0,0.8,0.2)\)，\(\lambda=1.0\) 等。

## 结论
作者认为推理期软先验 + 跨块状态传递即可在不训练长文数据的情况下显著改善长距可懂度、韵律连贯、说话人一致与边界自然度，并可推广到其他分块编解码 TTS。

## 点评
价值在于“部署即用”：不碰权重，专治分句拼接的边界能量不连续与上下文断裂。软先验相对二值流式掩码更温和。局限是依赖 MagpieTTS 训练期已有的 CTC/注意力先验归纳；对非编解码器或非 AR 架构需再适配；评测长文为拼接构造，真实叙事节奏多样性可能更复杂。


# AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling

- 论文编号：1180
- 报告人：Wen Wu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ren26d_interspeech.pdf

## 问题
长篇音频叙事需整合语音、音效与配乐，现有智能体系统常出现角色设定与声线不匹配、缺乏缺陷自纠、以及用户难用自然语言局部改稿。

## 方法
AuDirector 闭环多智能体：(1) 身份感知前期：Director 解析剧本与角色档案，Casting 用 EmbeddingGemma 粗检索 + Director 精选（320 条多样声库），并为每句生成 7 维情感指令；(2) 协同合成与校正：Acoustic 用 IndexTTS2 / TangoFlux / MusicGen 分层生成语音与非语音，Critic（MiMo-Audio、CLAP）打分，低于阈值则改情感指令/提示/种子并最多 \(N_{\max}\) 次重生成，Mix 混合；(3) 人机精修：Interaction 解析自然语言反馈，只对受影响脚本片段做定向再生。主 LLM 为 Gemini-3-Pro。

## 实验与结果
100 场景（40 播客 + 60 广播剧）对比 WavJourney、PodAgent 及无 Critic 变体。客观上 AuDirector 在 PQ、CE、VRM 领先（VRM 4.23）；主观 MOS-M/Emo/Ali/Aes 等整体最优或接近最优，Critic 带来除 MOS-Q/M 外的普遍增益。交互指令执行准确率平均 90%（增益控制 96%，结构编辑 84%）。作者指出非语音细粒度（如呼吸紧张度）仍受限。

## 结论
作者认为身份感知选角、闭环自纠与自然语言精修共同提升长篇音频故事的结构连贯、情感表现与声学保真，并支持人机协作。

## 点评
把“编排质量”与“单模型生成质量”拆开，在后端统一时用选角 + Critic 闭环解释 MOS-M/Emo 优势，评测设计较干净。系统工程性强，依赖外部 LLM/TTS/SFX 栈。脆弱点在重叠音效时的定位歧义（结构编辑 IEA 较低），以及环境声多样性不足仍会破坏沉浸感。


# Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion

- 论文编号：932
- 报告人：Seolhee Lee
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26i_interspeech.pdf

## 问题
人到非人语音转换（H2NH-VC）对游戏/影视等重要，但公开数据与基准稀缺，多依赖内部语料，难以公平对比与泛化评估。

## 方法
发布 Designed Vocalizations Dataset：从 VCTK 与 Freesound 收集言语与非言语源（动物、感叹、拟声等），用 Dehumaniser 2 内置与自研预设（部分经 Cubase 后处理）生成设计音色。训练为非并行 raw/designed；测试为 (source, reference) 对，reference 为同源经预设 \(G_p\) 处理。提供预设风格与源音色的 seen/unseen 划分。用 H2NH-VC 作基线评测。

## 实验与结果
训练约 5,654 源 × 40 预设 → 226,160 设计样本；测试 120 源 × 47 预设 = 5,640。四场景：seen–seen MOS 3.81、Cos.Sim 0.667；unseen–unseen MOS 3.49、Cos.Sim 0.610；交叉约 3.66。能量相关 PCC-E/RMSE-E 跨场景几乎不变；未见源时 CER/WER 反而更低（作者推测转换较弱、输出更接近源）。

## 结论
作者认为该公开数据集与基准可支撑非人设计发声转换的可复现研究，并给出基线结果供后续对比。

## 点评
贡献在资源与评测协议而非新算法：用专业 DSP 预设把“设计音色”可复现化，并显式拆开源/风格泛化。局限是基线仅一个模型，且 ASR 指标在弱转换时可能误导；效果模块覆盖仍可扩展。


# ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching

- 论文编号：185
- 报告人：Jihwan Kim
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26_interspeech.pdf

## 问题
零样本对话 TTS 的 flow matching 在密集 Mel 上做分钟级单次生成时显存爆炸，常被迫切块，损害长程一致性。

## 方法
ZipL-Dialog：确定性 Mel 自编码器将 100 Hz Mel 压到 25 Hz（\(r=4\)，\(D=100\)）连续潜空间；在潜空间做掩码条件 flow matching（前缀上下文干净、目标区线性插值噪声）；辅助 Mel 域重建损失 \(\lambda=0.5\)。ZipFormer 下采样改为较温和的 [1,1,2,1,1]，避免默认激进层级在压缩后损害短音素分辨率。预训练后在 OpenDialog 英语子集微调。

## 实验与结果
相对 ZipVoice-Dialog：最大峰值显存最多降 11.22×（CoVoMix2：36.21→3.23 GB），推理最多快约 2.23×。UTMOS 最优或并列最优；WER/cpSIM 略逊未压缩基线。消融：确定性 AE 优于 VAE（WER 3.634 vs 6.535）；加 \(L_{\mathrm{mel}}\) 全面提升；默认 [1,2,4,2,1] 与无下采样均严重损害质量。

## 结论
作者认为 25 Hz 潜空间 CFM + 适配层级可大幅降低长对话合成的显存与时延，并保持有竞争力的感知自然度。

## 点评
把“长序列显存”问题落到时间压缩，并用确定性瓶颈 + Mel 监督对抗 VAE 过平滑，针对性强。效率收益清晰；代价是客观可懂度与说话人相似的小幅回退，说明压缩仍损局部细节。


# Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS

- 论文编号：2730
- 报告人：Rong Wang
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26ea_interspeech.pdf

## 问题
MOS 与谱距离只给全局分，无法定位合成相对自然语音的偏离层级：是韵律垮了、音段垮了，还是两者独立？

## 方法
在 LJ-TTS（13,100 句配对）上分析四系统（Tacotron2-DDC、FastSpeech2、Glow-TTS、MixerTTS），共享 HiFi-GAN。韵律：21 个句级 F0/强度/时间特征 + LASSO 分类。音段：元音空间面积、按发音部位的 F2 轨迹、locus equation。人–机边界经 MFA 迁移并抽查校验。

## 实验与结果
韵律呈跨时间尺度解离：全局 F0 变异压缩（\(d=-0.55\)），局部 pitch inflection 升高（\(d=+0.82\)）；语速/浊音比等时间指标无显著差。元音三角形面积仅剩人类 9–30%；齿龈/软腭处 F2 条件运动减弱，齿龈 locus 斜率系统偏高。韵律与音段偏差 Spearman 近零。LASSO AUC≈0.851。架构上 FastSpeech2 韵律偏差小但元音塌缩最重，Glow-TTS 局部变调过量等。

## 结论
作者认为神经 TTS 并非“单调平坦”，而是全局–局部 F0 协调与音段目标/协同发音各自偏离；二者基本不相关，应作为独立质量维度，补充 MOS。

## 点评
用语音学可解释指标拆开 MOS 黑盒，结论“解离而非平坦”有说服力。局限在单说话人朗读英语、两阶段声学模型；作者也承认在更口语/端到端系统上差距可能更大。


# Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning

- 论文编号：2284
- 报告人：Jiangnan Ye
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ye26b_interspeech.pdf

## 问题
细粒度强调控制因标注稀缺与韵律复杂而难；规则调音高/能量常不自然，LLM-TTS 指令微调又数据饥渴。

## 方法
在 F5-TTS 上加 Emphasis Encoder（4 层 Transformer），融合 `<strong>` 等标签嵌入。三阶段：(1) 2.5 h 人工中文强调数据 SFT；(2) 用 SFT 采样 + WPT 突显度排序构造偏好对做 Flow-DPO；(3) Flow-CPS（FlowGRPO 变体）以 WPT 为奖励做组相对优势在线 RL。标签可由 DeepSeek 辅助生成。

## 实验与结果
突显度：F5 0.86 → SFT 1.22 → DPO 1.42 → GRPO 1.45（CosyVoice 1.32）；WER 约 1.62–1.63% 稳定，SIM≈0.71–0.72。主观：E-MOS 2.51 vs CosyVoice 2.16，N-MOS 3.47 vs 3.06。名词强调控制准确率 GRPO 63%（DPO 37%，CosyVoice 22%）。

## 结论
作者认为 SFT→DPO→Flow-CPS 流水线可在有限标注下显著提升强调强度与可控性，同时保持可懂度与说话人相似。

## 点评
把 LLM 对齐套路迁到 flow-matching TTS，并用 WPT 作可计算突显度奖励，缓解标注瓶颈。风险是奖励模型与人类感知不完全一致；主要评测在中文强调场景，跨语与更复杂话语焦点泛化未充分展开。


# CraftTTS: Fine-Grained Prosody Control for Text-to-Speech

- 论文编号：2018
- 报告人：Qihang Lu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yang26l_interspeech.pdf

## 问题
零样本 TTS 全局克隆强，但严格词级强度/语速控制易破坏声学先验，产生伪影、停顿或不自然情绪泄漏。

## 方法
CraftTTS 三阶段对齐 CosyVoice 2：(1) 计算驱动数据：DeepSeek-V3 打 strong/weak/fast/slow 标签，Indextts2 多轮 AR 续写 + best-of-N（音色相似/时长代理语速）构造偏好正样本，无人工标注；(2) 联合 SFT+DPO 增强局部标签敏感；(3) GRPO，奖励解耦为停顿感知 ASR CER、情绪锚定强度对比、语速方向正则，平衡局部可控与全局自然。

## 实验与结果
中文 InstructTTSEval 等评测：相对 CosyVoice 2 基线，完整 CraftTTS 提升 NMOS（3.87 vs 3.67）、STMOS/SPMOS，SMOS 略升；CER 7.01%（基线 6.36%）、Sim 略降。消融与主观表明 Stage 2/3 逐步改善细粒度表达。

## 结论
作者认为零样本偏好构造 + SFT/DPO/GRPO 对齐可使 LLM-TTS 在保持零样本能力下达到更强词级韵律可控。

## 点评
与强调控制工作同属“对齐管线迁到 TTS”，特色是无人工偏好数据与多维解耦奖励，直接针对局部控制破坏全局先验的冲突。CER/Sim 小幅回退提示可控性–保真仍有张力；依赖教师 TTS 质量与 LLM 标注可靠性。


# Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity

- 论文编号：2312
- 报告人：Zhenwei Mou
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mou26b_interspeech.pdf

## 问题
个性化 LLM-TTS 常整体建模参考语音属性；显式韵律多为整句静态预计算（如 CoT），忽略已生成语音中的风格信息，限制说话人相似。

## 方法
在 CosyVoice LLM 上按音节动态预测韵律：音节韵律向量（时长、能量均值、基频均值与范围）经 k-means（512）量化；每音节先用 PQ 嵌入在已生成韵律/语音 token 条件下预测韵律 token，再条件生成该音节语音 token。训练 CE 损失加权 \(\alpha=0.5\)。约 50k 小时中文数据。

## 实验与结果
相对 CosyVoice(50k) 与静态 CoT：MOS 自然度相当或略好；偏好测试在 ESD/内部集上更偏好提出方法（约 48–52% vs 对方约 29–33%）。客观：三测试集 CER 更低；ESD 情绪 SIM/ACC 与能量 RMSE 等多项更好。作者还观察到动态预测有助于缩小小规模与大规模训练间的韵律学习差距。

## 结论
作者认为把已生成语音纳入音节级韵律预测可增强风格学习，从而提升说话人相似且不损自然度。

## 点评
相对“先整句韵律再语音”的 CoT，闭环利用自生成历史更贴合说话风格的时序依赖。实现绑定 CosyVoice 与音节级中文设定；韵律离散化粒度（512）与采样超参对风格保真仍敏感。

