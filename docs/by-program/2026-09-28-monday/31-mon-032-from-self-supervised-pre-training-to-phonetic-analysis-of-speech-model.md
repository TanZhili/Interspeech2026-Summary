# From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 日期：Monday 28 September 2026 / 时间：14:30-16:30 / 形式：Poster（Area 8）/ 论文数：11
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场围绕自监督语音预训练的适配能力与表征可解释性展开。一侧工作把 HuBERT 式掩码预测扩展到多采样率、双模式（流式/非流式）与伪标签在线精炼，目标是缓解单一采样率假设、上下文不一致与伪标签监督偏弱等瓶颈；另一侧则用更轻量的 tokenizer、音素/韵律探测与错误分析，追问预训练表征究竟编码了哪些语音学信息。

在预训练适配上，多采样率自适应下采样、在线预测编码与双模式层归一化、以及 BEST-RQ 的 PCA / 码本迭代精炼与蒸馏，分别针对时间分辨率错配、流式未来上下文缺失、以及固定在线量化监督不足。共同取舍是：在尽量保留原有目标与结构（便于复用既有分析）的同时，提升跨条件可用性。

面向下游鲁棒性时，点击辅音、构音障碍语音等低资源或非典型语音成为试金石：Wav2Vec2 / HuBERT 在点击语言上的细调结果，以及以 FiLM / Gated-FiLM 对 HuBERT 前端做可懂度通道调制，都指向“通用 SSL 表征可泛化，但仍需轻量条件化才能贴近特定人群语音”。

表征侧则出现两条互补线索。一是把连续语音压成可接入大模型的离散单元：ZipCodec 用 flow-matching 解码器换取极轻编码器，并用 Encoder Consistency Regularization 增强语义容量。二是从音系竞争时间进程、韵律 ABX、次声门共振与原始波形声学模型的音素错误模式出发，检验模型是否像人一样增量竞争、是否对韵律敏感、以及错误是否更多反映音素相似性本身。视频推理中的音频 token 压缩则把“保留声学线索”与“控制计算开销”并置，成为跨模态场景下的新瓶颈。

总体来看，本场瓶颈从“把 SSL 做准”转向“在混合速率、流式约束、非典型语音与音系/韵律可测性下把 SSL 用对、说清”。指标与机制均以各摘要自述为限，跨论文不可直接横向换算。

## 技术内容

### 自监督预训练适配与伪标签精炼

**MSR-HuBERT: Self-supervised Pre-training for Adaptation to Multiple Sampling Rates**（论文 1354；presenter：Zikang Huang）
问题是现有语音 SSL 常假设单一采样率，混合速率因时间分辨率错配而困难。方法在 HuBERT 上用 multi-sampling-rate adaptive downsampling CNN，把不同采样率波形映射到共享时间分辨率且不做重采样。摘要称在 16–48 kHz 实验中优于 HuBERT，并保留掩码预测目标与 Transformer 编码器以便复用既有分析。

**Online Predictive Coding for Dual-Mode Self-Supervised Speech Models**（论文 1997；presenter：Keita Goto）
双模式 SSL 需同时处理流式与非流式，注意力上下文范围不同导致优化困难；先前 online registers 收益有限。本文引入 Online Predictive Coding（OPC）对 registers 做多步未来预测正则，并加入 Dual-mode Layer Normalization。在 LibriSpeech 与 WSJ 上细调 ASR，摘要称 OPC 缩小在线–离线差距，并给出 160 ms 延迟下的 WER 变化。

**Enhancing BEST-RQ Pseudo-Label Quality Through Online Refinement for Automatic Speech Recognition**（论文 650；presenter：Jingjing Xu）
BEST-RQ 用固定在线量化生成伪标签，监督弱于迭代精炼的 HuBERT 式方法。作者提出三项改动：量化器线性投影换 PCA、迭代码本精炼、以及通过 codebook distillation 更新的额外码本。在 Librispeech 960h 预训练、100h 监督细调设置下，三项全开时摘要报告 test-other 相对 WER 下降。

**IACC-HuBERT: Intelligibility-Aware Channel Conditioning of HuBERT Frontend for Dysarthric Speech Conformer ASR**（论文 2375；presenter：Hemant Kumar Kathania）
构音障碍语音缺乏专用基础模型，需适配已有 SSL。方法用 FiLM-only 与 Gated-FiLM 按说话人可懂度对 HuBERT 特征做通道调制，仅训练少量参数，并接入端到端 Conformer ASR。摘要给出相应 WER，并强调可懂度感知的通道条件化。

### 离散化、跨模态压缩与音系/韵律分析

**ZipCodec: Simple and Pretrained-Model-Free Speech Tokenizer via Flow-Matching**（论文 2941；presenter：Lingxuan Ye）
多数语音 tokenizer 依赖大规模预训练或多阶段管线。ZipCodec 单阶段、无预训练教师，把声学重建交给 Zipformer-based flow-matching 解码器，编码器仅 4.4M 参数，并用 ECR 损失自监督增强语义容量。摘要称声学与语义表现有竞争力，并改进零样本 TTS。

**Preserving Acoustic Cues for Video Reasoning: An Efficient Uniqueness-Driven Token Compression Framework**（论文 3512；presenter：Zichao Nie）
视频推理需要视觉与声学线索，但 MLLM 常丢弃音频或仅用 ASR 文本，全量音频 token 又过重。Flash-VAReason 基于信息唯一性理论，经 Audio Time Fusion、Budget Control、Spatial Dynamic Compression 压缩音频 token。摘要称可将音频 token 量级下降并保留最具信息量的线索。

**Pretrained self-supervised speech models can recognize unseen consonants**（论文 2848；presenter：Chihiro Taguchi）
预训练数据偏向高资源语言，点击辅音等罕见音素可能欠表示。作者在两种点击丰富的科伊桑语言上细调并比较 Wav2Vec2 与 HuBERT。结果称细调模型识别点击比非点击更准确，提示自监督可泛化到罕见音素。

**Do Machines Listen Like Humans? A Temporal Benchmark for Phonological Competition in End-to-End ASR**（论文 401；presenter：Linkai Peng）
关注 ASR 是否具有类人增量词汇激活与音系竞争时间进程。基准用模型内部激活轨迹与人眼动数据做逐点比较。摘要称因果模型能复现起首竞争者早竞争、押韵词晚而弱竞争的模式，而非因果“前瞻”模型不能，架构约束对类人加工很关键。

**From Continuous Speech to Subglottal Resonances: Automatic Signal Generation, Estimation, and Tracking Framework**（论文 2464；presenter：Chigozie Uzochukwu Udeogu）
次声门共振（SGR）获取困难限制其应用。框架用监督多尺度频谱学习从语音生成含次声门信息的加速度计信号，并自动估计与跟踪 SGR。摘要报告 Sgr1–3 的 RMSE 量级，并在 TIMIT 上给出估计误差上界式描述。

**Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations**（论文 478；presenter：Haitong Sun）
S3M 对音位对比敏感，但对韵律对比缺乏直接度量。prosodic ABX 扩展 ABX 框架，用少量样例、无需显式标签评估韵律对比，并发布英日最小对数据集，结合普通话数据评估重音、音高重音与声调。摘要称模型与层排序在多种条件下常保持，利于低资源场景。

**Phonetic Error Analysis of Raw Waveform Acoustic Models**（论文 798；presenter：Zhengjun Yue）
在 TIMIT 上对原始波形声学模型做超出总体 PER 的错误分析：按宽音素类分解 PER，并由替换错误构混淆矩阵。模型结合 SincNet / Sinc2Net 或非参数 CNN 与 BLSTM。摘要给出 Dev/Test PER、WSJ 迁移后的提升，并指出 BLSTM 更利过渡依赖类、迁移对辅音改进更大，混淆模式与 Filterbank 系统一致。

## 本场要点
- 多采样率、双模式与 BEST-RQ 伪标签精炼，是 HuBERT/SSL 预训练在工程约束下的主要扩展方向。
- 非典型语音（点击辅音、构音障碍）用于检验通用 SSL 的泛化与轻量条件化适配。
- ZipCodec 与 Flash-VAReason 分别从“轻量离散化”和“跨模态 token 预算”压缩声学接口成本。
- 音系竞争时间基准、韵律 ABX、SGR 估计与原始波形错误分析，把评价从总体错误率推向语音学可解释性。
- 因果 vs 非因果架构差异被摘要强调为类人增量加工的关键约束。
- 多数工作仍保留或兼容既有 SSL 目标/编码器结构，以便复用分析与改进。

## 覆盖核对
`1354 | MSR-HuBERT: Self-supervised Pre-training for Adaptation to Multiple Sampling Rates`
`1997 | Online Predictive Coding for Dual-Mode Self-Supervised Speech Models`
`650 | Enhancing BEST-RQ Pseudo-Label Quality Through Online Refinement for Automatic Speech Recognition`
`2848 | Pretrained self-supervised speech models can recognize unseen consonants`
`2375 | IACC-HuBERT: Intelligibility-Aware Channel Conditioning of HuBERT Frontend for Dysarthric Speech Conformer ASR`
`2941 | ZipCodec: Simple and Pretrained-Model-Free Speech Tokenizer via Flow-Matching`
`3512 | Preserving Acoustic Cues for Video Reasoning: An Efficient Uniqueness-Driven Token Compression Framework`
`401 | Do Machines Listen Like Humans? A Temporal Benchmark for Phonological Competition in End-to-End ASR`
`2464 | From Continuous Speech to Subglottal Resonances: Automatic Signal Generation, Estimation, and Tracking Framework`
`478 | Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations`
`798 | Phonetic Error Analysis of Raw Waveform Acoustic Models`
