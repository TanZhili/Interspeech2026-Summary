# Streaming Speech Synthesis

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
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

本场围绕流式/低时延语音生成：神经网络编解码器与单码本语音语言模型、流式零样本音色转换、以及面向增量文本的 LLM-TTS。共性目标是在有限前瞻条件下保持韵律自然、说话人一致与可懂度。

编解码与表征侧，HybridCodec 融合双流解耦与 SSL 蒸馏；WavSLM 把 WavLM 量化蒸馏为单码本自回归流。流式 VC 则批评 ASV 说话人嵌入对帧级生成不友好，并改进分块扩散与音色编码器鲁棒性。

流式 TTS 侧，FlashTTS、CTC-TTS、S5-TTS 与韵律边界感知后训练分别从多 token 预测/均值流蒸馏、CTC 对齐与交错策略、有限前瞻掩码、以及边界早停+滑动窗上下文等角度压低首包时延并抑制长文崩溃。另有一篇舞蹈到音乐扩散生成，扩展到多舞者与非人类舞者场景。

整体趋势是：把语义—声学解耦、原生双流输入输出与对齐/边界控制组合起来，服务实时对话系统。

## 论文技术总结

# HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec

- 论文编号：3393
- 报告人：Arjun Gangwar
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/gangwar26_interspeech.pdf

## 问题
语义–声学解耦编解码有两路：蒸馏进 RVQ-1（快但语义弱）与双流+推理时 SSL（语义强但慢）。需要兼得解耦强度与推理速度。

## 方法
HybridCodec：公共因果 CNN 编码器（24 kHz→25 Hz）分语义/声学支路；语义 VQ（16384）经轻量 ConvNeXt 解码蒸馏 w2v-BERT-2.0 第 16 层（训练时冻结，推理去掉 SSL）；声学支路对“公共潜变量−语义解码”做 RVQ。GAN+谱重建+蒸馏训练。对比 DAC、DAC(Distill)、DualCodec。

## 实验与结果
60k 更新 LibriSpeech：HC-SED-AED RVQ-1 WER 15.36% 最优；高码本层重建具竞争力。跨语/零样本（SeedTTS-en、CV-French）语义仍强。相对 DualCodec 约 3× 加速（RTF 约从 0.042 量级降至约 1/3）。消融显示双流+蒸馏组合对 RVQ-1 最关键。

## 结论
双流结构加语义蒸馏可在无推理 SSL 下保持强 RVQ-1 语义与快速推理，适合下游语音 LLM tokenize。

## 点评
把 DualCodec 的解耦与 Mimi 式蒸馏拼成“训练重、推理轻”的折中，工程动机清楚。25 Hz 低帧率有利于长上下文 LM；声学质量与纯 DAC 仍有取舍。


# WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

- 论文编号：2803
- 报告人：Luca Della Libera
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/libera26_interspeech.pdf

## 问题
多数语音语言模型依赖文本预训练、多码本层级或混合架构，偏离文本式单流自回归范式。能否用单码本同时建模语义与声学？

## 方法
WavSLM：FocalCodec-Stream 将 WavLM-6 特征压成单流离散 token（50 Hz，可流式，块大小 4，理论延迟 80 ms）；解压特征接 WavLM-large 第 7–24 层作因果骨干，next-chunk 预测（C=4）。无文本监督，约在 Libri-Light 60k 小时训练。变体词汇量 2k/4k/65k（约 305–370M 参数）。滑窗注意力支持持续生成。

## 实验与结果
似然评测：WavSLM-4k 声学一致性 Avg 69.5，多项与更大文本预训练模型可比（如 Spk 88.5、Gend 90.5）。生成：WavSLM-2k UTMOS 3.72、Sim 91.8，优于 LLaMA-Mimi 1.3B/8B 的 UTMOS，且 RTF 更高。消融显示窗口与块大小影响一致性–质量权衡。

## 结论
充分表达的单码本表征可使纯语音、单流、可流式 SLM 在更小规模下达到有竞争力的一致性与生成质量。

## 点评
刻意剥离文本与多码本复杂性，把问题还原为“表征是否够好”。结果支持中层 WavLM+单码本路线；与 7B 级文本预训练模型比参数与数据更省，但口语内容任务仍有差距。


# VOSSA: Voiceprint Optimization for Streaming Speech Architectures

- 论文编号：2763
- 报告人：Mu-Ruei Tseng
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26c_interspeech.pdf

## 问题
流式 VC 常用冻结 ASV 嵌入，其设计刻意压制说话人内音素/韵律变化，与帧级声学生成冲突；另训说话人编码器又增复杂度。

## 方法
VOSSA 以 TVTSyn 为骨干：从冻结内容编码器的 CNN 末层与每隔一层 MHSA 特征拼接，经 ASP+MLP 得全局说话人嵌入，与 VC 目标联合训练，去掉外部说话人编码器。双路径训练：LibriTTS 自重建 + VoxCeleb 非平行转换。六数据集评测，并做 F0、F1 共振峰诊断与听感测试。

## 实验与结果
NISQA-MOS、WER 与 TVTSyn 相当；归一化目标相似度显著更高；HNR 接近 TVTSyn 且优于多数基线。自重建上 F0 MAE/PCC 与元音 F1 的 Wasserstein 距离最优。听感：相对 TVTSyn，说话人相似 46→54、可懂度 44→56、活力 48→52（百分比偏好）。

## 结论
中间层内容表征足以支撑说话人条件，可在保持流式延迟的同时改善音高动态与元音区分线索。

## 点评
把“说话人嵌入从哪来”从 ASV 惯性改到内容编码器中层，对准生成所需的音素条件可变性。声学诊断（F1/F0）比只报 SIM 更能说明表征差异。


# MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion

- 论文编号：1961
- 报告人：Guobin Ma
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ma26c_interspeech.pdf

## 问题
MeanVC 的 chunk 自回归去噪训练加倍序列长度、小块质量差，且 MRTE 直接吃参考 Mel，对低质参考敏感；160 ms 块端到端延迟约 211 ms。

## 方法
MeanVC 2：（1）Future-receptive chunking（FRC）按 DiT 层调度 past/future 注意力掩码，去掉 clean-chunk teacher forcing，支持 40 ms 块+有界未来上下文；（2）Universal Timbre Token Encoder（UTTE）由全局说话人嵌入建 UTT key–value，用 BNF 查询经交叉注意力取细粒度音色，降低对参考 Mel 质量依赖。仍用 mean flows 1-NFE。约 18M 参数。

## 实验与结果
Table 1：MeanVC 2 延迟约 109.9 ms，SSIM 0.710、SMOS 3.89、DNSMOS 3.89，全面优于同约 80 ms 输入窗的 MeanVC(80)；相对 MeanVC(160) CER/NMOS 略逊但延迟近半。消融：去掉前向掩码 CER 飙至 20.65%；去掉 UTTE SSIM 降至 0.682。参考鲁棒实验显示 UTTE 优于 MRTE。

## 结论
FRC+UTTE 使流式零样本 VC 在约 110 ms 延迟下显著提升相似与稳健性，优于原 MeanVC。

## 点评
同时打训练友好度、短块上下文与参考质量三个痛点，产品向很强。有界未来上下文是延迟–质量的明确旋钮。


# FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation

- 论文编号：1692
- 报告人：Hanke Xie
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/xie26b_interspeech.pdf

## 问题
对话系统要求 TTS 低延迟且支持流式文本输入；单码本 LLM-TTS 常需缓冲整句，自回归慢且多步流匹配抬高首包延迟。

## 方法
FlashTTS（Qwen2.5-0.5B）：滞后多轨堆叠输入（语音/文本/语言并行）支持增量文本；Stage2 加 Multi-Token Prediction 并行预测多 token；声学端用 X-pred mean flow + 块注意力，2-NFE 出 Mel，再 HiFi-GAN。约 30 万小时开源数据训练。与 CosyVoice2（10-NFE）等同规模基线对比。

## 实验与结果
MiniMax 多语子集：MTP-3（2-NFE）FPL 325 ms、TPS 73、RTF 0.632、WER 18.8、SIM 0.695；相对 CosyVoice2 的 FPL 843 ms/RTF 0.913/WER 26.2 明显更快更清晰。Stage1 2-NFE FPL 377 ms。CMOS 与基线接近或略优。

## 结论
原生流式输入轨 + MTP + 2-NFE mean flow 可把首包延迟压到约 325 ms，同时保持零样本克隆与跨语可懂度，适合作对话级联 TTS。

## 点评
同时砍“等整句”与“慢解码”两条延迟路径，工程完整。MTP 抬速时对 SIM/CMOS 有轻微代价，需按场景选 MTP-3/5。


# Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input

- 论文编号：1192
- 报告人：Changsong Liu
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26i_interspeech.pdf

## 问题
流式文本输入的 LLM-TTS 缺前瞻导致韵律差，且交错生成历史无限膨胀引发长文崩溃；强对齐标注成本高。

## 方法
对预训练 CosyVoice2 LLM 做韵律边界感知后训练：用 WhisperX 弱时间对齐，随机插入 boundary marker 并截断对应语音目标，教模型在有限未来文本下提前停。推理时每 k 词一块、lookahead f 词，滑动窗口用上一块文本/语音作 prompt，KV 缓存 O(k+f)。流匹配与声码器冻结。

## 实验与结果
Seed-TTS-Eval：标准句 WER 4.03%、长文 4.77%；交错基线长文 WER 70.97%（摘要写 71.0%→4.8%）。说话人/情感相似长文显著更高（SPK-SIM 0.65 vs 交错 0.56；相对摘要称 +16.1%/+1.5%）。主观长文 MOS 4.13 vs 交错 3.18。TTFA 约 1296 ms，RTF 0.782。

## 结论
仅用弱对齐后训练即可让现有 LLM-TTS 在流式文本输入下稳定长文合成并改善韵律，无需改注意力结构。

## 点评
边界标记 + 有界滑动窗口直接对准“韵律缺前瞻”与“长文崩溃”两大痛点，且不改架构，迁移成本低。长文 WER 断崖式改善是最强证据。


# CTC-TTS: LLM-Based Dual-Streaming Text-to-Speech with CTC Alignment

- 论文编号：653
- 报告人：Zhijian Ou
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26e_interspeech.pdf

## 问题
多数 LLM-based TTS 不做低延迟双流（文本边进、语音边出）。高质量双流依赖准确的文本–语音对齐与合理的交错训练序列；现有方法常用 MFA 等 GMM-HMM 强制对齐（流水线重、不够灵活），或固定比例交错文本/语音 token，难以刻画对齐规律。

## 方法
提出 CTC-TTS：用 CTC ASR（Whistle Conformer）做音素–语音对齐，经 Viterbi 得路径并将 blank 归到后续音素；NAC（WavTokenizer）帧率与 CTC 为 3:1，每音素对应三个语音 token。按词构造 bi-word 块：当前词音素 + 词间分隔符 + 下一词音素 + 当前词语音 token + ⟨eob⟩。两变体：CTC-TTS-L 沿序列长度拼接（偏质量）；CTC-TTS-F 将音素与语音 embedding 沿特征维堆叠（可从首音素起生成，降首包延迟）。单码本 NAC 上用 decoder-only Transformer，对语音 token 与 ⟨eob⟩ 做交叉熵（文本位置不计入损失）。

## 实验与结果
单说话人（VoiceAssistant400K）：相对 LLMVox，CTC-TTS-F 的 WER/CER 更低且 FPL-A 更短（约 159 ms vs 167 ms）；CTC-TTS-L 可懂度最好（WER 1.50%、CER 0.79%）但 FPL-A 约 210 ms；三者 UTMOS 均为 4.15。多说话人零样本（LibriSpeech 训练）：continuation 上 CTC-TTS-L WER 4.82%、MOS 4.33，优于 MFA+bi-word 与 ELLA-V 类序列；cross-speaker 上 CTC-TTS-L WER 6.33%、MOS 4.23。消融显示 CTC 对齐与 bi-word 交错均重要；CTC 在跨说话人域外更稳，MFA 在域内 continuation 上仍有竞争力。

## 结论
以 CTC 对齐替代 MFA，配合 bi-word 交错，可在流式与零样本任务上优于固定比例交错与 MFA 基线；L/F 两变体提供质量–延迟折中。未来可换神经 G2P 与更精细的神经强制对齐。

## 点评
核心是用“结构够用、不必帧级精确”的 CTC 对齐降低流水线成本，再用当前词+下一词的局部前瞻平衡流式条件。L 走长度拼接、F 走特征堆叠，把质量与首包延迟拆开权衡。脆弱处是依赖冻结 CTC/G2P/NAC 质量，以及 bi-word 仍需一词前瞻（L 甚至两词才出声），极短句或强共发音场景下对齐噪声可能被放大。


# PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation

- 论文编号：248
- 报告人：Jaekwon Im
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/im26_interspeech.pdf

## 问题
现有 dance-to-music 多依赖单人人体姿态（SMPL/2D 关键），难覆盖多人舞、非人类角色，且姿态估计抖动；公开数据（如 AIST++）歌曲少、背景简单，易过拟合、难泛化到真实视频。

## 方法
提出 PF-D2M：用 Synchformer 视觉特征代替姿态，条件 DiT（初始化自 Stable Audio Open 的 VAE/DiT）生成音乐 latent；文本用 T5-base 交叉注意力；视觉特征上采样后与 DiT 输入通道拼接，并经 AdaLN 调制；速度预测 + CFG。渐进训练：Stage 0 保留文本–音频生成能力；Stage 1 在 VGGSound 上学视听同步；Stage 2 按 2:4:1 混合 AIST++、FMA/MoisesDB（无演唱过滤后约 191h）、VGGSound 微调，文本侧用空视觉 embedding。推理 DPM-Solver++ 100 步、CFG=5。

## 实验与结果
AIST++（按未见曲目切测试集）客观节奏指标：PF-D2M (S2) BHS 99.8、HSD 1.9、F1 94.3，多数指标 SOTA，BCS 略低于 Text-Inv/LORIS。主观（20 人、四类野外视频：单/多人 × 人/非人）：对齐与音质均明显优于 LORIS、Text-Inv，多人与非人场景差距更大。Stage 2 相对 Stage 1 结构更连贯、更少“现场收录感”。

## 结论
无姿态、用视频视觉特征 + 渐进训练，可在多样舞姿视频上生成对齐且音质更好的音乐；局限是生成时长较短，且缺合适客观评测集。

## 点评
用 Synchformer 视听同步特征绕开姿态管线，再靠 Stable Audio 初始化与多模态混合微调缓解 AIST++ 过拟合，路线清晰。节奏指标相对 GT 对齐，难反映“另有合理节奏”的感知质量，作者也强调主观评测更关键。脆弱处是短片段生成、依赖文本标签质量，以及野外场景仍可能受视觉噪声与剪辑影响。


# Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead

- 论文编号：235
- 报告人：Muyang Du
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/du26_interspeech.pdf

## 问题
级联 LLM–TTS 里多数 TTS 需整句上下文才开声，端到端响应延迟高。增量 TTS 已有研究，但多限于单/少说话人，零样本与自然度不足；T5-TTS 的 encoder–decoder 单调对齐适合稳健合成，却缺流式变体。

## 方法
提出 S5-TTS（Streaming T5-TTS）：词级流式，编码器处理已见词 + k 个前瞻词，解码器自回归生成当前词的 FSQ codec chunk；用交叉注意力 argmax 是否进入前瞻区判定词边界，chunk 间两帧重叠 + Hanning 交叉淡入。训练/推理对 encoder 自注意力与 decoder 交叉注意力施加 lookahead-causal mask；用 Conv 辅助注意力 + MAS 得到音素–codec 对齐以构造 decoder mask，并加 CTC 辅助损失。再以全上下文 T5-TTS 为教师做 Interleaved Multi-Source Distillation（IMSD）：成对语音数据与 ASR 过滤后的文本-only 软标签交错批蒸馏（隐状态 MSE + logits KL + CE）。

## 实验与结果
LibriTTS+HiFiTTS 训练（约 845h）。k=2 为自然度–可懂度折中（偏好测试 65.9% 优于 k=1）；k=3 可懂度明显变差。消融：去掉 encoder/decoder LCM 均伤 WER。IMSD 后 LibriTTS unseen：WER 2.65%、UTMOS 3.72，接近 T5-TTS；MOS 3.71 vs T5 3.75。UltraChat：蒸馏后 MOS 4.12 vs T5 4.21，E2E 延迟约 0.356s vs T5 0.868s。相对更大 AR/NAR 基线，在约 4.67K 小时数据上 STOI/PESQ 更优。

## 结论
有限前瞻下的流式 T5-TTS，配合因果 mask、辅助对齐与 IMSD，可接近全上下文质量并显著降低级联系统端到端延迟，且支持零样本说话人。

## 点评
把 T5-TTS 的单调交叉注意力优势搬到词级流式，并用 mask 对齐训练–推理分布，是务实增量路线；IMSD 用文本-only 软标签补自然度也贴合对话场景。脆弱处是依赖固定 k 前瞻（过大反而伤对齐）、词边界靠注意力启发式，以及蒸馏仍需强教师与 ASR 过滤算力。

