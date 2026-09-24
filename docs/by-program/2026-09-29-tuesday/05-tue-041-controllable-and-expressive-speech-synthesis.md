# Controllable and Expressive Speech Synthesis

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕可控、表情化 TTS/VC：改进 Classifier-free Guidance 的无条件嵌入、Lombard/清晰度多级控制、跨语口音强度、粗到细韵律控制、韵律导向 codec，以及公开嗓音印象语料与防泄漏训练。共同瓶颈是细粒度表情/口音/印象控制常与说话人音色、文本语义纠缠，导致泄漏或不可解释的强度调节。

控制接口多样化：可学习 null embedding 与分模态无条件嵌入；声乐用力与清晰度伪标签 + 词级强调；口音子空间加权语言嵌入；音素对齐的音高/响度/时长；把韵律建模为相对文本与说话人条件的残差；以及数值嗓音印象（VI）的双话语解耦或无参考控制。公开 LibriTTS-VI 直接回应“无公开语料”障碍。

评价维度在说话人相似度、稳定性、表情、口音相似度、可懂度（含噪声中）与 VI 均方误差之间权衡；摘要强调更大 guidance scale 下的鲁棒性与数值控制相对提示式 TTS 的精确性。

## 论文技术总结

# Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis

- 论文编号：803
- 报告人：Biel Tura-Vecino
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/turavecino26_interspeech.pdf

## 问题
TTS 中 CFG 常用固定零向量作无条件表示，难以区分说话人与文本等正交条件，且可能落在训练分布外，导致大引导尺度下不稳定。需要更稳的无条件基线与可解耦的属性引导。

## 方法
模型：Qwen3-0.6B AR 骨干 + 轻量扩散头预测 64 维 VAE 潜变量，Perceiver 编码说话人，BPE 文本。将固定 ∅ 换为可学习 null 嵌入 ¯s、¯t；训练时各条件独立以 0.1 概率替换。推理可写解耦 CFG：分别对说话人/文本无条件隐藏态施加 ws、wt。对比固定零向量与可学习 null，并与 FishSpeech、Qwen3-TTS、VoxCPM、IndexTTS2 等对比；客观指标含 CER、SECS、PRO、PMR、PQ、UTMOS、Pitch std、SRR；主观多模型 CMOS。

## 实验与结果
耦合 CFG：可学习 null 对 w≥1.0 更稳，说话人相似度平台高于固定零向量峰值；w=0.8 时 SECS 0.817 vs 0.755，CER 相近且 Pitch std 更高。解耦 wt=0.4、ws=1.2 进一步抬 SECS/PRO。CMOS：可学习变体自然度/相似度均为正，固定零为负；解耦版相似度偏好更强、自然度略低于耦合版。文本引导上存在稳定性–表现力权衡，说话人引导存在相似度–绝对质量权衡。

## 结论
可学习 null 提供更稳、有意义的无条件基线，提升相似度与表现力并对大 CFG 更鲁棒；独立 null + 解耦权重可在推理时细粒度控属性。

## 点评
改动小但打在 CFG 实现细节上：把“缺条件”学成域内锚点，比硬塞零向量更合理。解耦引导把相似度与可懂度/表现力的折中显式化，利于产品侧调参；局限是评测说话人偏表现力强，听感上“更像参考”未必总被判为更自然。


# Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS

- 论文编号：1159
- 报告人：Seymanur Akti
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/akti26_interspeech.pdf

## 问题
Lombard 效应（更大音量、更高音高、更慢语速、更平谱倾斜、更清晰发音）可提升噪声下可懂度，但现代 TTS 多训在非 Lombard 风格，缺少对发声力度与构音的统一、可解耦控制，尤其超构音建模不足。

## 方法
基于 Matcha-TTS（流匹配 + MAS 时长）与 Vocos 声码器。用 Expresso 的 default/enunciated/fast/projected 风格构造构音 β 与发声力度 α 伪标签（并入 LJ Speech 作中性扩充，约 11h+）。各属性映射到 32 维连续嵌入，与说话人嵌入拼接；双注入：编码器侧控时长/语速，解码器 U-Net 侧控谱–韵律。推理 α、β∈[0,1] 连续插值，并可按词赋不同 β 做局部强调。基线为 RMS 增益 + 线性时拉伸。

## 实验与结果
Harvard Sentences 上，提高 β 显著降 WER、升 MVD，α 主要抬谱倾斜；相对基线更有效。噪声实验（餐馆 babble、叠语、白噪，SNR=10/5/1，RMS 归一）：构音持续降 WER；发声力度在固定 SNR 下对 WER 帮助有限但对 SII 有增益；联合缩放在 SNR=1 时尤其有益。CMOS（10 人）：自然度 1.97±0.32、噪声可懂度 1.13±0.24（相对基线/中性）。另支持词级强调。

## 结论
双轴连续控制可模拟 Lombard 相关清晰度与力度变化，并在噪声听感上带来可懂度增益；词级控制可针对性加强片段。

## 点评
把 Lombard 拆成“构音 vs 力度”并分别打进时长与声学通路，比单一风格标签更贴真实适应机制。伪标签依赖 Expresso 离散风格到连续轴的映射，数据规模与说话人数有限，极端 α 还会偏离 ASR 分布；噪声评测做了 RMS 归一以排除简单响度作弊，设计合理。


# CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations

- 论文编号：1744
- 报告人：Nirmesh J. Shah
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/annamdevula26_interspeech.pdf

## 问题
跨语 TTS（尤其低资源、音系多样的印度语）中口音与说话人属性纠缠，LLM-codec TTS 虽有跨语能力却难显式控制口音强度；过强口音伤可懂度，需要转换与连续强度调制。

## 方法
Neucodec（50 token/s）离散化；Perceiver Resampler（Ns=32）从参考声学 token 得说话人/风格嵌入；GRL 对抗分类器抑制嵌入中的口音/语言信息；可学习语言嵌入扩展到所有 latent slot 并相加，推理用 λ e_lang1+(1−λ)e_lang2 插值口音强度。Qwen2.5-0.5B AR 预测声学 token。数据：Indic 多语约 986 小时 + L2-ARCTIC 微调。指标：口音相似度/泄漏、UTMOS、SpkSim；20 人 MOS。

## 实验与结果
Indic：Proposed UTMOS 3.181、AccLeak 0.203、AccSim 0.371、SpkSim 0.842，优于 IndicF5、XTTS-v2。L2-ARCTIC：UTMOS 4.001、AccLeak 0.439、AccSim 0.686，口音控制度优于 CVAE/GST。主观口音相似度 MOS 高于基线；强度 0→1.0 时 AccSim 单调上升。

## 结论
对抗解耦 + 加权语言嵌入可在保留说话人的同时做跨语口音转换与连续强度控制，适用于低资源多语设定。

## 点评
核心是把“口音当可加条件、说话人当需洗掉的泄漏”，用 GRL+语言嵌入插值实现强度旋钮，工程清晰。强度分析与泄漏指标对齐目标；脆弱点是口音评测依赖 GenAID/微调口音嵌入的代理质量，且 SpkSim 在 L2 上略低于部分 GST 基线，解耦仍有折中。


# CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis

- 论文编号：1760
- 报告人：David Harwath
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zheng26c_interspeech.pdf

## 问题
零样本 TTS 自然度与音色克隆已强，但词/音素级细粒度表现力控制仍难：说话人、韵律、风格常纠缠，现有控制多在句级提示，无法对齐到局部音高、响度或时长并保持目标音色。

## 方法
CTRLSPEECH 基于 DiTAR：VAE 将 16 kHz 波形压成 40 Hz、64 维连续潜 token；按 patch（4 token）做因果 AR + 局部扩散（flow-matching）生成。粗控制：CampPlus 说话人嵌入与/或 prompt 语音；细控制：音素对齐的量化 pitch（WORLD→Mel→128 bins）、A 加权响度（64 bins）、强制对齐音素时长帧数，叠加到音素嵌入。约 2 万小时英文（Emilia+GigaSpeech）训 0.1B/0.6B；推理 CFG 32 步、scale 1.5。支持先粗生成再迭代改局部控制。

## 实验与结果
零样本：0.6B 在 LibriSpeech-PC WER 2.46%、SIM-o 0.65，Seed-TTS WER 2.58%、SIM-o 0.63，优于复现 DiTAR；SMOS 亦更好。说话人消融：嵌入+prompt 最佳。有控制信号时 LJSpeech 上 pitch RMSE 67.86→38.39 Hz、loudness 6.35→4.56 dB；音素时长 MAE 28.08→11.86。

## 结论
全局音色 + 音素对齐韵律信号可实现粗到细的可编辑表达合成，同时保持有竞争力的零样本质量。局限：主英文；依赖 pitch/对齐质量；纯文本仍难预测精确局部韵律；未显式建模情感等。

## 点评
抓住“可编辑局部韵律”而非再堆提示词，连续潜空间比离散 codec 更利于细微起伏。控制信号显式、可测（RMSE/MAE）是强项；工程上依赖对齐与提取器误差，且 UI 迭代流程对标注成本敏感。


# ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion

- 论文编号：2146
- 报告人：Jeongsoo Choi
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26d_interspeech.pdf

## 问题
神经语音 codec 常把内容、说话人、韵律缠在一起，利于零样本克隆但不利于变声：变声需改音色、严保源内容与韵律。把韵律当独立可交换流往往丢掉说话人相关韵律细节。

## 方法
ProsoCodec：将韵律建模为条件残差——编码器/解码器以 ASR 文本与 SV 说话人嵌入作前缀，BSQ 离散瓶颈迫使 token 编码内容/说话人之外的韵律变化；编码器仅用低频 mel，解码器用全频 prompt。扩散 DiT 解码器 + 条件流匹配；训练交替随机 span mask 与同说话人双话语策略（prompt 与源不同句），减轻 prompt 风格泄漏。推理：源 token + 源文本 + 参考说话人/prompt。LibriTTS 585 h 训练，Vocos 合成。

## 实验与结果
合并 LibriTTS test + VCTK：ProsoCodec WER 4.451、SIMr 0.565、SIMs 0.167、f0 RMSE 0.428、P-MOS 3.852，整体优于 DDDM-VC、UniAudio、HierSpeech++、FACodec、Seed-VC、Vevo。消融：去掉双话语抬 RMSE；去文本条件 WER 暴涨；去说话人条件泄漏加重；全频 mel 略差。瓶颈约 12.5 Hz、4096 码本（150 bps）权衡较好；无 codec token 则退化为跟 prompt 韵律的零样本 TTS。

## 结论
文本/说话人前缀 + 离散瓶颈可学韵律残差，双话语与低频输入抑制风格泄漏，变声在内容、音色、韵律与自然度上更均衡。

## 点评
不走对抗解耦，而用“先验吃掉内容/音色、瓶颈只剩残差”的信息论思路，对变声更贴切。双话语训练直接打 prompt 抄袭；脆弱点是依赖外部 ASR/SV 质量，且码率过低会伤内容、过高又泄漏源音色。


# LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control

- 论文编号：2231
- 报告人：Junki Ohmura
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ohmura26_interspeech.pdf

## 问题
数值化语音印象（VI，如明亮度等 11 维 1–7 分）可控 TTS 缺公开语料；且易出现印象泄漏——合成被参考音频自身 VI 拉偏。单参考同时供说话人与 VI 条件可能造成纠缠。

## 方法
发布 LibriTTS-VI：在 LibriTTS-R 上人工标注 130 句×10 维（+语速由 ASR WPM），训练 VIE 并按音高/能量/WavLM 相似句扩充到全库。骨干 VIC：HuBERT+BiLSTM 参考编码器、Control Module、STL，接 VITS。提出 VIC-dis：同说话人另一句 r′ 作说话人条件、VI 仍来自目标句；VIC-srf：用高斯噪声替换参考分支，纯 VI 控制。对比 VIC-base 与 Qwen3-TTS VoiceDesign（VI→NL 提示，零样本/微调）。

## 实验与结果
客观：VIC-srf 将 RVI-MSE 从 base 的 0.61 降到 0.41，∆V 从 0.22 到 0.05（泄漏近消失）；调制斜率平均 0.199>dis 0.159>base 0.121。QVD 数值控制弱（斜率 0.068），且文本语义与 VI 纠缠。主观多维调制 MSE：srf 0.92 vs base 1.15。质量 MOS 大多保持，部分极端调制略降。

## 结论
公开 VI 语料使可复现；双话语解耦与无参考生成显著减轻印象泄漏并提升数值可控性，优于基于 NL 提示的 LLM-TTS 在精细 VI 上的表现。

## 点评
问题定义清楚：泄漏来自“同一句既当身份又当印象”。解耦与无参考两条路互补；公开语料是社区价值。标注一致性中等、VIE 代理误差会传导到评测；部分维（如 Powerful–Weak）仍难学，极端调制可能伤自然度。

