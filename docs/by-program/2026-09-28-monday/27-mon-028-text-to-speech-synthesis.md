# Text-to-Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为跨领域长口头报告，覆盖流匹配 TTS 的在线 RL、离散流匹配零样本合成、通用 GAN 声码器目标、零样本评测、文本到音频指令遵循，以及可流式零样本风格转换。主线是：生成质量之外，还要可控优化、可区分评测与实时风格迁移。

训练侧，FlowTTS-GRPO 把 ODE 轨迹改写为 SDE 路径，直接对开源 FM 模型做在线 RL；DiFlow-TTS 在离散空间做流匹配以降低连续 token 优化难度；RAF 用 SSL 辅助判别器与相对论配对提升 GAN 声码器域内保真与泛化。评测与对齐侧，I2D 用迭代自参考放大系统差距；ALLM 细粒度反馈构造偏好对改进多事件时序指令。系统侧 StyleStream 以 Destylizer+DiT Stylizer 实现约 1 s 端到端延迟的流式转换。

## 论文技术总结

# FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech

- 论文编号：1102
- 报告人：Haoxu Wang
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26s_interspeech.pdf

## 问题
TTS 的 RL 后训练多集中在 LLM 侧；Flow Matching 因 ODE 确定性难直接做在线 RL，且零样本克隆需同时兼顾说话人相似、可懂度与感知质量，多奖励易冲突。

## 方法
FlowTTS-GRPO：将 FM 的 ODE 采样转为等价 SDE 引入随机性，用 GRPO 在线优化开源 FM（CosyVoice 3.0 的 FM 部分、F5-TTS），无需额外随机生成器/价值网。奖励含说话人相似、ASR/CER、DNSMOS 等；对比概率式单奖励分配与按 batch 标准差归一化后的加权和。训练省略 CFG 加速收敛；对 F5 引入硬文本增广（词/句重复）。LoRA 微调 FM。

## 实验与结果
Seed-TTS-Eval：F5 经 FM-GRPO 后中英 CER/WER 与 SS、DNSMOS 提升（如 test-zh CER 1.81→1.55，SS1 0.760→0.777）；CosyVoice 3.0-0.5B 主要抬升 SS 与 MOS（SS1 0.777→0.804），CER 基本持平——符合“LM 管可懂度、FM 管声学细节”观察。加权归一化奖励收敛更稳。

## 结论
作者认为 ODE→SDE + GRPO 可直接后训练开源 FM TTS，多目标加权与硬样本策略有效，且 FM-RL 与 LLM-RL 作用互补。

## 点评
把 Flow-GRPO 从图像/增强迁到零样本 TTS，并点明混合系统中应 RL 哪一模块，实用。代理奖励仍可能 reward hacking；主观偏好相对客观表较简。硬样本仅中文侧为主。


# DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching

- 论文编号：1043
- 报告人：Son Nguyen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26d_interspeech.pdf

## 问题
零样本 TTS 中 AR 延迟高，连续流匹配空间复杂；离散扩散训练与采样配置强耦合。需要在因子化编解码离散空间做更灵活的离散流匹配。

## 方法
DiFlow-TTS：以预训练 FACodec 得韵律/内容/声学离散码与说话人嵌入。Phoneme-Content Mapper 将音素对齐到内容码并产内容嵌入；Factorized Discrete Flow Denoiser 在离散流匹配框架下用分头同时预测韵律与声学概率速度，条件于内容嵌入与参考提示的韵律/声学/说话人。PCM 确定性，流去噪器并行生成多属性。

## 实验与结果
作者报告相对基线在自然度、内容准确与韵律保持上有竞争力，模型可小至约 11.7×，推理加速可达约 34×（摘要/贡献声明）。作为 DFM 应用于因子化语音码的首批框架之一。

## 结论
作者认为在因子化离散码上做离散流匹配是可行的紧凑低时延零样本 TTS 方向，并提供分属性速度场分解设计。

## 点评
相对连续 FM，离散有限支撑降低优化难度；分头建模韵律/声学是相对同质 DFM 的关键扩展。正文抽取后半数字表不完整，规模与对比细节以作者声明为主；强依赖 FACodec 解耦质量。


# RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

- 论文编号：646
- 报告人：Yongjoon Lee
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26e_interspeech.pdf

## 问题
GAN 声码器架构进步快，但训练目标常不足以学到可泛化表示；提升泛化往往牺牲单步效率（如扩散/大模型）。需在保持 GAN 效率下同时抬升见域保真与未见域泛化。

## 方法
RAF：用 WavLM/HuBERT 等 SSL 嵌入与频域度量定义 real–fake 的 quality gap；判别器用相对论配对（RpGAN 式）估计 discriminator gap，对抗目标使两者对齐，生成器最小化判别器差距。应用于 BigVGAN-base、HiFi-GAN、Vocos 等，对照 LSGAN/SAN/WaveFM 等。

## 实验与结果
多数据集上客观与主观一致提升；摘要称 RAF 训练的 BigVGAN-base 在感知质量上可超过 LSGAN 训练的更大 BigVGAN，且参数仅约 12%。跨源域与未见集泛化增强。

## 结论
作者认为 SSL 辅助的相对论配对对抗反馈是提升通用 GAN 声码器的有效训练框架。

## 点评
改损失不改推理图，部署友好。SSL 选择（WavLM 末卷积层、HuBERT 第 22 层）有感知/音素依据。与 MetricGAN 系需区分：RAF 强调配对相对反馈而非直接回归可微指标。未见域增益取决于 SSL 覆盖面。


# Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation

- 论文编号：2414
- 报告人：Shengfan Shen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shen26d_interspeech.pdf

## 问题
零样本 TTS 客观指标（WER/SIM/预测 MOS）在 SOTA 区间易饱和、与人类排序相关弱；主观评测贵且难复现。

## 方法
I2D：对每个模型做多轮自条件合成——上一轮输出作下一轮参考，最多 10 轮；强模型退化慢、弱模型快，从而拉开差距。跨轮聚合（均值/加权）客观分。在 LibriTTS、Seed-TTS-Eval、CV3-Eval 上评 11 个 AR/NAR/混合系统，并做人机相关分析。

## 实验与结果
第 1 轮分数高度拥挤、UTMOSv2 等系统级 SRCC 弱（摘要称约 0.118）；迭代聚合后 UTMOSv2 系统级 SRCC 升至约 0.464。第 10 轮 utterance/system 级相关整体增强。可观察内容/说话人/自然度/情感克隆轨迹差异。

## 结论
作者认为迭代自条件退化可放大模型差、提升客观指标可区分性与人机对齐，适合自动化零样本 TTS 评测。

## 点评
评测协议创新：用误差累积当“压力测试”。代价是算力×迭代次数，且强依赖首轮参考质量；可能偏爱“抗自条件”而非单次生成最优的系统。与 VoiceMOS “zoomed-in”问题直接对话。


# Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models

- 论文编号：1111
- 报告人：Chun-Yi Kuan
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kuan26_interspeech.pdf

## 问题
TTA 在 FAD/CLAP 等全局指标上已强，但多事件与时间顺序指令常失败；现有偏好数据多靠 CLAP/启发式/人工，缺可扩展的指令级正确性监督。

## 方法
用 ALLM 作细粒度裁判，判定目标事件是否存在与时间序是否正确；经基准与人工校验后，将满足/不满足样本构造成偏好对做 DPO。提出 S3Bench：叙事多事件指令约 1200 例（2–4 事件，LLM 生成叙述，仅评测不用训练）。

## 实验与结果
ALLM 与人在存在/时序判断上高一致（协议约 89.8%/93.5%）。DPO 后在既有基准与 S3Bench 上事件完整度、时序与联合指令遵循准确率提升，同时保持音频质量竞争力。

## 结论
作者认为 ALLM 细粒度反馈可规模化改进 TTA 指令遵循，并提供叙事评测基准 S3Bench。

## 点评
把理解侧 ALLM 接到生成侧训练信号，打通“能听懂指令→能生成符合指令”。依赖 ALLM 偏置；S3Bench 叙述由 LLM 生成，可能与裁判同族。相对 Baton 人工标注更可扩展，相对 CLAP 更对准事件/时序。


# StyleStream: Real-Time Zero-Shot Voice Style Conversion

- 论文编号：404
- 报告人：Yisi Liu
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26c_interspeech.pdf

## 问题
零样本语音风格转换需要把源句改成未见目标说话人的音色、口音与情感，同时保留语言内容。现有方法内容–风格解耦不干净：大码本语义 token（如 CosyVoice 2，6561）仍泄漏口音/情感；Vevo 等纯自监督量化又易损伤可懂度。实时语音转换多只做音色，尚无端到端流式的整体风格转换。

## 方法
StyleStream 分 Destylizer 与 Stylizer。Destylizer：冻结 HuBERT-Large（训练流式时解冻并改因果）+ Conformer，FSQ 码本 `[5,3,3]`（45 码）与 ASR 解码器联合做 seq2seq ASR；推理用 FSQ 前的连续表示作内容特征（50 Hz），而非离散码。Stylizer：WavLM-TDNN2 风格编码器 + 16 层 DiT，以频谱 inpainting + OT 路径 conditional flow matching 训练，CFG=2、NFE=16。声码器为因果 Vocos（16 kHz）。流式用 chunked-causal attention，默认 600 ms chunk，端到端延迟约 1 s（`L = t_chunksize + t_proc`）。

## 实验与结果
Destylizer 在约 1300 h LMG（LibriTTS+MSP-Podcast+GLOBE）训练；Stylizer 在 Emilia 英语音约 50k h。评测 StyleStream-Test：300×10=3000 源–目标对。离线 StyleStream：WER 9.2%，S/A/E-SIM 0.852/0.640/0.827，主观 A/E/S-SMOS 最高（约 4.32/4.42/4.36）；流式 WER 15.3%，风格相似度仍领先 Vevo 等。chunk 增大（200→1000 ms）降低 WER、提高相似度与 UTMOS。RTX A6000 上 600 ms chunk 处理约 0.429 s，可流式。全文抽取在 baselines/消融中段截断，后续分析数字不全。

## 结论
作者认为以 ASR 监督 + 紧凑 FSQ + 连续软单元，可更干净地解耦内容与风格，并首次实现约 1 s 延迟的实时零样本风格转换，口音/情感相似度明显优于先前系统。流式相对离线牺牲可懂度。

## 点评
核心抓的是“内容提取瓶颈过宽导致风格泄漏”与“非自回归等长建模便于流式”两点；相对 CosyVoice 2/Vevo，把监督 ASR 与极窄码本压在一起、却用预量化连续特征喂 DiT，是合理折中。PDF 抽取在实验后半截断，消融与延迟表不完整，流式 WER 仍偏高，口音/情感泛化边界需对照完整原文。

