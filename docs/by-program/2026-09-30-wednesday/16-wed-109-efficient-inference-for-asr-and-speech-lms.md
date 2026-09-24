# Efficient Inference for ASR and Speech LMs

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：9
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场关注 ASR 与语音语言模型的高效推理：无资源音节令牌化、无数据无训练压缩、端侧关键词检出的结构剪枝与短时记忆卷积、统一音频理解与生成的高吞吐管线、半自回归并行生成、流式发射策略、自适应令牌采样、LLM 知识合并，以及千类少样本持续学习。核心是在延迟、算力、内存与质量之间取得可部署折中。

离散令牌序列过长推动音节级与自适应合并；基础模型压缩探索通道聚类剪枝；始终在线 KWS 同时做权重与通道剪枝或把 CNN 改为 LSTM 式在线推理。生成侧 vLLM 扩展延迟模式多流采样与 CFG 共调度，Audio-NSP 仅靠数据重构激活并行解码。流式 ASR 用训练无关发射策略包装时间戳基础模型；AdaTS 动态合并低信息令牌降推理成本；LoRA 算术合并把外部 LM 知识并入 ASR 参数而不增推理开销。

## 论文技术总结

# ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling

- 论文编号：315
- 报告人：Nicol Visser
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/visser26_interspeech.pdf

## 问题
纯语音语言模型需把 SSL 特征离散成单元，但帧级 token 序列过长，长程句法建模困难。Sylber、SyllableLM 等音节单元有效，却依赖多阶段微调与专用目标，管线复杂。

## 方法
**ZeroSyl** 训练免费：
1. 取冻结 WavLM Large 第 13 层特征的 L2 范数，平滑后做突出度峰值检测（\(\delta=0.45\sigma\)）得音节边界。
2. 在边界内对第 22 层特征均值池化，球面 K-means（K=10k，LibriSpeech 100h）离散化；层次聚类把静音质心合并，词表约 9116。
3. 用 OPT-125M 在发现单元上做因果 LM（对比实验 6k h / 扩展 60k h Libri-Light）。

## 实验与结果
边界：R-value 75%、token F1 54%，优于 Sylber，接近 SyllableLM 5Hz。发现质量：SNMI 88.9%、bitrate 52 bps，优于对比音节系统。6k h LM：sWUGGY 68.0、sBLIMP 60.5、tSC 68.1，全面高于 Sylber/SyllableLM。扩展：词汇任务仍逊帧级 SpidR，但句法随数据量上升更陡，60k h 叙事接近 SpidR。

## 结论
作者认为高质量音节发现不必复杂多阶段训练；L2 范数已含可用音节位置信号。局限：音节压缩可能伤稀有/未见词的词汇细节；L2 为何编码音节位置仍待解释。

## 点评
工作价值在「极简有效」：用冻结模型的范数峰值替代专门蒸馏边界网络，却在多项口语 LM 基准超过更重的音节管线。扩展实验也诚实标出与细粒度单元的任务分工（词 vs 句）。脆弱点：强依赖 WavLM Large 特定层；静音合并启发式；对非英语/嘈杂语料是否成立未充分验证。


# Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering

- 论文编号：1010
- 报告人：Haoning Xu
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26h_interspeech.pdf

## 问题
语音基础模型（HuBERT、Whisper 等）参数大，端侧难部署。结构化剪枝虽硬件友好，但常按孤立重要性丢弃可能功能冗余却重要的单元，且依赖数据校准/微调；非结构化稀疏又需专用算子。

## 方法
**参数聚类压缩**（数据无关、可训练免费）：
1. 对 MHSA/FFN（及 Whisper 交叉注意力）中结构化单元（注意力头、FFN 中间单元）做 k-means，把相似单元融合成 \(K=\mathrm{round}(N(1-sp))\) 个质心并写回权重，而非直接删除低幅度单元。
2. **混合稀疏**：按层内参数方差把模块分高/中/低三组，高方差层保留更多簇（\(s=0.2\)），全局平均稀疏度不变。
对比基线为同结构的幅度剪枝（MP）。

## 实验与结果
LibriSpeech 上评 HuBERT-large 与 Whisper-large-v3。无微调：HuBERT 50% 均匀稀疏相对 MP，test-clean/other 绝对 WER 降 27.73%/18.61%；Whisper 10% 混合稀疏相对 MP 降 2.86%/5.02%，且相对未压缩基线无显著恶化。HuBERT 聚类后仅 3 epoch 微调，相对 MP 仍有小幅优势。混合稀疏在多数稀疏度优于均匀；过高稀疏（如 Whisper≥30%、HuBERT 60%）会崩溃。

## 结论
作者主张用「合并相似结构」替代「丢弃低幅度结构」，实现可部署的粗粒度、数据/训练免费压缩，并可用方差分配稀疏预算。

## 点评
核心反直觉但合理：高幅度单元若彼此相似，剪枝会留下冗余；聚类融合保留集体信息。数据免费这一点对「训练数据不可得」的商用基础模型尤其实用。脆弱点：极端稀疏仍崩；主要评测在 LibriSpeech 英语 ASR；聚类本身有计算开销，且融合是否损害多语 Whisper 能力正文未深挖。


# OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting

- 论文编号：1253
- 报告人：Alessio Burello
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/risso26_interspeech.pdf

## 问题
端侧个性化关键词检测既要适配用户/环境分布偏移，又受内存、时延与能耗约束。已有自学习流水线主要在线更新权重；架构（通道数）通常只做部署前离线剪枝，未必匹配现场分布。

## 方法
**OnDA** 在 [3] 的 ProtoNet 自学习管线（预训练 → 伪标签 → 端侧 triplet 微调）上加入结构化通道剪枝：
- **OnDA-1**：用数据感知 **HAP**（Hessian-trace 加权幅度）在适配初期、基于伪标签数据剪枝，再微调。
- **OnDA-2**：先微调，再用数据无关全局 L1 剪枝，再二次微调。
可与离线剪枝叠加。剪枝对象为卷积输出通道，得到仍稠密的子网络。

## 实验与结果
MSWC 预训练；HeySnips / HeySnapdragon 个性化评测。相对未剪基线，iso 任务表现（Acc@FARh=0.5）下最高约 9.63× 模型体积压缩；Pareto 前沿显示域内数据剪枝优于直接微调更小的离线剪枝网。Jetson Orin Nano：相对仅权重适配，训练/推理时延与能耗最高约 1.52×/1.57× 与 1.64×/1.77× 改善；数据感知剪枝可前置，从而降低后续微调成本。

## 结论
作者认为个性化 KWS 应同时适配权重与架构；用现场伪标签做在线结构化剪枝，可在保持任务表现下显著压缩并加速端侧训练/推理。

## 点评
问题提得准：分布偏移不只改最优权重，也改「够用多深的通道」。把 HAP 前移到适配起点，用少而贴域的伪标签做架构决策，比「先离线剪小再硬微调」更贴部署现实。脆弱点：伪标签噪声会影响 HAP 分数；二次微调增加流水线复杂度；结论主要来自两类唤醒词数据集与 Jetson 测量，换 MCU 级平台收益需另证。


# Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device

- 论文编号：1343
- 报告人：Szymon Klimaszewski
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/warlewski26_interspeech.pdf

## 问题
端侧 KWS 需在严格算力与内存下做高时间粒度在线推理；滑动窗 CNN 冗余计算多，原 STMC 为帧同步任务保留全部池化状态，对只需稀疏输出的分类任务存在状态冗余。

## 方法
提出 SM-STMC：将卷积骨干按池化/输出切成子模型，经内存缓冲连接；按调度式在时刻 t 只执行必要深度（池化 stride 带来的冗余状态被丢弃）。CNN 离线训练后 STMC/SM-STMC 仅作推理扩展，无额外参数；用独立子模型静态调度以兼容 TensorFlow Lite。输入 Mel 谱（窗 1024、hop 256），VGG 式嵌入 + MLP 分类器，约每 8 帧评一次分类器。

## 实验与结果
Google Speech Commands 11 类。标准 1 s 测试：SM-STMC1 recall/准确率约 93.8%，SM-STMC2 约 91.6%；两端补静音的 2 s 集上离线单窗 VGG 大幅掉点，8× 滑动窗与 SM-STMC1 达约 97.1%。ARM Cortex-M55（int8、TFLite Micro）：相对 8×/s 滑动窗，SM-STMC 总 MCPS 显著更低（如 VGG1 8× 59.36 vs SM-STMC1 11.37）；相对原 STMC 缓冲约减半至更少（如 STMC2 21632→SM-STMC2 7520）。摘要称相对等价频繁 CNN 与 vanilla STMC，MCPS 最高可降约 82% 与 46%。

## 结论
SM-STMC 在保持 CNN 识别性能的同时削减在线卷积冗余状态与算力，无需重训，适合穿戴等资源受限 KWS；分类频率降低会略增延迟，但仍在实时交互可接受范围。

## 点评
抓住 KWS“不必每帧出结果”与 STMC 帧同步设计的错位，用静态子模型调度换部署友好性。效果强依赖池化深度与评测频率；与 LSTM 比算力更省但延迟粒度更粗，边界对齐场景才显出相对离线窗的优势。


# An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation

- 论文编号：1244
- 报告人：Haoran Wang
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26w_interspeech.pdf

## 问题
高吞吐推理引擎面向单流文本自回归，难原生支持 SpeechLM 的多码本 delay-pattern 交织采样、波形解码，以及 CFG 双路前向带来的吞吐腰斩与调度同步开销。

## 方法
基于 vLLM 连续批处理：主–辅分解，仅一条码本流走引擎标准管线，其余 S−1 流在模型内采样并缓存；请求结束后 delay 解交织，GPU 内嵌声学解码器直接出波形。用每请求相位状态机（text / transition / audio / drain）与动态词表掩码管理文–音混合输出。CFG 采用 Paired Request Co-Scheduling：条件与无条件 companion 同批共享一次 backbone 前向，仅在音频相位合并 logits，采样 token 同步写回 companion。在 Bagpiper、OpusLM、OpusLM-Dialogue 上验证。

## 实验与结果
单卡 H100 80GB、FlashAttention-3。相对顺序 PyTorch：Bagpiper decode 约 52.7→5694.5 tok/s，OpusLM 36.5→4582.9，OpusLM-Dial. 53.9→5870.5；MFU 最高约 9.95%。FP32 下与参考实现 token 序列一致；BF16+FA3 有精度漂移但不伤聚合质量（MMAU-mini、LibriSpeech ASR/TTS、Eval2000 UTMOS 与基线接近）。Bagpiper CFG：decode 约 4952→3960 tok/s，约保持非 CFG 吞吐的 80%。

## 结论
在连续批处理引擎内原生支持多流音频生成与端到端合成，并用成对共调度吸收 CFG 开销；跨多种 SpeechLM 最高约 108× 生成吞吐，修改主要落在模型与 logit 层，便于复用。

## 点评
把 delay-pattern 与 CFG 嵌进现有调度/KV 基础设施，而不是另起一套服务，务实可落地。吞吐数字依赖高并发与 H100；质量表中个别指标（如对话 UTMOS）略降，说明精度与批处理路径仍需任务侧核对。开源分支便于复现。


# Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models

- 论文编号：1737
- 报告人：Liang Cao
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cao26b_interspeech.pdf

## 问题
LALM 音频序列远长于文本，逐 token 自回归延迟高；改 NAR/加 MTP 头或草稿模型有结构或显存开销，且文本低熵与音频高熵导致统一置信阈值会使并行解码退化或伤保真度。

## 方法
Audio-NSP：仅通过数据中心 SFT 激活半自回归块生成——在原序列后追加若干 Anchor-Mask 块（锚点+可学习 mask），位置 ID 对齐逻辑位置；定制注意力（前缀因果、块内双向、块间隔离），损失只算 mask 位。推理为 predict–verify–accept；模态感知动态截断：文本 τ_text=0.8、音频 τ_audio=0.2（Top-1 置信度），按置信度接受变长前缀。骨干 VITA-Audio-Plus-Vanilla，块长 W=4。

## 实验与结果
相对 VITA-Base / VITA-MTP：ASR 平均 WER 劣化约 +1.20（MTP +2.14），TPS 最高约 3.42×（LibriSpeech-clean）；SQA 平均 ACC 劣化约 −1.64（MTP −1.78），约 2.4×；TTS 平均劣化约 +0.29（MTP +0.68），约 1.9×。动态截断 Pareto 优于固定步长；Top-1 / Top-10 sum / Entropy 均可调出可用折中，默认 Top-1>0.2。

## 结论
无结构改动即可把预训练 LALM 变为块级生成，并用模态感知截断缓解文本–音频熵差，相对 MTP 在加速与质量保留上更优（约 1.89×–3.42×）。

## 点评
核心洞见是“同一阈值套在音频上会退化成 AR”，用分模态阈值换速度–保真。仍依赖 SFT 与固定 W；TTS 加速弱于 ASR 是有意保守。未改架构利于落地，但训练序列打包与注意力定制实现成本不低。


# Improving streaming ASR with foundation models using emission policies

- 论文编号：3358
- 报告人：Gerard Mas Mollà
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/masmolla26_interspeech.pdf

## 问题
Parakeet、Canary 等语音基础模型离线 ASR 强，流式切块后质量明显下降；依赖内部特征的发射策略难迁移，需要不打开模型黑盒的流式包装。

## 方法
训练无关、模型无关流水线：滑动窗音频缓冲（块长 L_c、最大窗 L_max）增量喂入；用 token 级时间戳过滤早于 T_last 的重复输出；文本侧发射策略控制提交时机——静态 Wait-K、Hold-N，动态 LocalAgreement（连续两假设最长公共前缀）及基于编辑距离阈值 τ 的 LA-Lev。仅要求模型能产时间戳。

## 实验与结果
Open ASR Leaderboard：VoxPopuli、TedLium-v3、Earnings22；模型 Parakeet-tdt-0.6b-v3、Canary-1b-v2。窗参：L_c=2、L_max=20 较稳。相对 NeMo 流式基线，各策略均降 WER；高延迟下 Parakeet+LA 接近离线（如 Earnings22 11.45% vs 离线 11.19%，延迟约 2.25 s）。L_c=1 低延迟设定下 Parakeet+LA 优于或接近 SimulStreaming Whisper（如 Earnings22 12.07%/1.32 s vs 14.92%/1.01 s），延迟略高约 0.4 s。

## 结论
滑动窗 + 时间戳去重 + 纯文本发射策略，可使带时间戳的 SFM 在实时/近实时下接近离线质量，且无需访问内部张量。

## 点评
把“黑盒+时间戳”做成可插拔流式层，利于换模型。LA 等策略用稳定性换延迟，与 AlignAtt 类模型感知策略比更易移植、延迟略逊。图文中部分抽取噪声不影响主结论；多任务 ST 等扩展作者留作未来工作。


# AdaTS: Adaptive Token Sampling for Efficient Speech Language Models

- 论文编号：2753
- 报告人：Sonal Sannigrahi
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sannigrahi26_interspeech.pdf

## 问题
SLM 将密集语音 token 塞进 LLM 上下文，序列长且冗余高，均匀卷积下采样或固定池化易在压缩与语义保留之间失衡，拖累长音频与推理成本。

## 方法
AdaTS：在预训练语音编码器输出上按成对余弦相似度做 score-and-merge——相似度高于阈值 t 的连续子组加权合并（权重 1−sim，强调更不相似单元）。两阶段训练：先冻编码器与 LLM，只训线性/MLP 模态与长度适配（ASR 对齐）；再解冻 LLM 做 ASR/SQA/ST 指令微调。编码器固定 Wav2Vec2Bert，解码器试 Qwen2.5 1.5B、Llama 3.2 1B、EuroLLM 1.7B；采样模块可只在 IT 或两阶段启用。

## 实验与结果
主结果（Qwen2.5 1.5B+AdaTS）：ASR LS Clean/Other 等显著优于 Pooling、WLQF、FLS；Spoken SQuAD F1 58.9、SLUE 37.5、LongSpeechEval 3.5，FLEURS ST COMET 82.0。t=0.85 时平均压缩约 1.65–1.85×（最高可超 4×）；加权平均合并优于简单平均与 Top-1。最佳为 MA 用全长、IT 再下采样；仅 MA 压缩会严重掉点。10 s 音频推理约 2.14 vs 卷积下采样 3.23 TFLOPS（约 34% 降算力；摘要称推理成本约降 40%）。

## 结论
无参相似度合并可在约 2× 平均压缩下保持甚至提升 ASR/ST/SQA，并降低推理算力；对齐阶段宜保留冗余，压缩宜放在指令微调。

## 点评
用内容自适应粒度替代一刀切下采样，小解码器也能压过依赖更大骨干的 CTC 融合路线。阈值对 ASR/ST 更敏感；压缩率随数据变化，部署需按任务标定 t。FLOPS 数字依赖其计算工具设定。


# Merging the Knowledge of LLMs for Automatic Speech Recognition

- 论文编号：2561
- 报告人：Hayato Futami
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/futami26_interspeech.pdf

## 问题
LLM 基 ASR 域适应常靠浅融合/密度比在解码时调用外部 LM，大模型每步推理成本高；需把目标域文本知识并入参数、推理零额外开销。

## 方法
同一预训练 LLM 上：ASR 用 LoRA，目标/源域 LM 亦用 LoRA。域扩展合并（对应浅融合）：θ = θ_pre + Δasr + λα Δlm,tgt；域迁移合并（对应密度比）：再减 λβ Δlm,src。可用 TIES（按幅度剪枝、选符号、只合同号参数）减轻任务干扰。推理仍单次 ASR 前向，无额外模块。

## 实验与结果
CSJ-SPS→CSJ-APS（LLM-jp-3-980M+Conformer）：基线 eval1 CER 13.9；TIESmerge-T 13.3，参数与 RTF 不变（1.1B / 0.45）；浅融合/密度比更低（12.8/12.5）但参数与 RTF 上升。合并可再与 SF/DR/rescoring 组合进一步降 CER。LibriSpeech→SPGISpeech（LLaMA3.2-1B）：基线 WER 11.2→TIESmerge 10.6；SF/DR 约 9.1/9.0。贪心解码下合并仍有效，CSJ 上甚至可优于 DR。

## 结论
跨模态 LoRA 算术合并能稳定提升目标域 ASR，且不增显存与延迟；绝对增益弱于逐步 LM 融合，但可与之叠加，并便于单模型部署。

## 点评
把浅融合/密度比“搬进权重空间”，切中大 LM 融合的成本痛点。跨模态对齐脆弱——加大 λα 易崩 ASR，故增益有限。无目标域配对数据、只需文本时很实用；源域文本缺失则只能做扩展合并。


# Scaling few-shot spoken word classification with generative meta-continual learning

- 论文编号：408
- 报告人：Batsirayi Mupamhi Ziki
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beyers26_interspeech.pdf

## 问题
少样本口语词分类多在小类数设定；若要持续扩到约 1000 类且每类仅 5 条，需在精度、遗忘与适应速度上可扩展的元–持续学习方案。

## 方法
用 GeMCL：编码器 + 生成式分类器，每类嵌入用 Normal-Gamma 先验、观测后闭式更新高斯后验（类参数隔离，免疫灾难遗忘）；元训练优化编码器与先验 α0、β0，元测试冻结元参数、对新词只算类统计。实现为 12 层 12 头 Transformer、MFCC 输入（约 85M 参数），在 MSWC 英语约 8915 词上元训（25-way-5-shot，估计约 477 小时有效数据）。基线为 HuBERT base（LibriSpeech 约 960 h 预训练）全量微调，以及冻骨干只训投影+分类头；类数从 25 增至 1000，每阶段 5-shot 支持集后评查询集。

## 实验与结果
全量微调多数阶段准确率最高但不稳（词级波动均值约 24.55）；GeMCL 波动约 0.48，显著更稳。GeMCL 在 <450 类优于 CH，高类数略逊；1000 类时约落后 1000-way 微调 CH 约 2%。适应时间：GeMCL 少样本适应约 0.06 h vs CH 124 / 全微调 186（摘要称适应约快 2000×）；元训远少于 HuBERT 预训练等价算力。

## 结论
从零训练的 GeMCL 在千类 5-shot 持续设定下可达接近实用 HuBERT 分类头基线的精度，真正增量更新、词级表现稳定，适合持续扩词表部署。

## 点评
把“可扩展少样本 KWS”推到 1000 类并报告过程稳定性，问题设定贴近产品。对比混入数据量与算力不对称，结论更像策略选择（相关小数据元学习 vs 大 SSL 微调）而非纯算法胜负。仅英语 MSWC；跨语与其他持续学习算法仍待验证。

