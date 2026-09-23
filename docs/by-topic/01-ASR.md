# 语音识别（ASR）

本文是 Interspeech 2026（悉尼，2026年9月27日–10月1日）语音识别及相关方向的专题技术综述。材料仅依据官方节目摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)）与 [ISCA 会场列表](https://www.isca-archive.org/interspeech_2026/index.html)；不补写摘要未给出的指标、数据集或方法细节。模型名称仅在摘要显式出现时保留。

覆盖范围取自 `topics_assigned.json` 中主题为 **asr / asr-multitalker / asr-decoding / retrieval / translation** 的全部 **24** 场次、合计 **169** 篇（含特邀综述与 Show-and-Tell）。日程横跨周一至周四：

- **周一 9月28日** 11:00-13:00 · Oral · [Multi-Talker ASR & Speaker Diarization](../by-program/2026-09-28-monday/05-mon-006-multi-talker-asr-and-speaker-diarization.md)（6 篇）
- **周一 9月28日** 11:00-13:00 · Oral · [Search Methods and Inference Algorithms](../by-program/2026-09-28-monday/06-mon-007-search-methods-and-inference-algorithms.md)（6 篇）
- **周一 9月28日** 11:00-13:00 · Long Oral · [Robust and Efficient ASR](../by-program/2026-09-28-monday/09-mon-010-robust-and-efficient-asr.md)（6 篇）
- **周一 9月28日** 11:00-13:00 · Poster · [Information Extraction and Retrieval](../by-program/2026-09-28-monday/16-mon-017-information-extraction-and-retrieval.md)（7 篇）
- **周二 9月29日** 09:00-11:00 · Oral · [Resource Constrained Speech Recognition](../by-program/2026-09-29-tuesday/06-tue-042-resource-constrained-speech-recognition.md)（6 篇）
- **周二 9月29日** 09:00-11:00 · Poster · [Multilingual, Cross-lingual & Low-Resource ASR](../by-program/2026-09-29-tuesday/15-tue-051-multilingual-cross-lingual-and-low-resource-asr.md)（11 篇）
- **周二 9月29日** 14:00-16:00 · Oral · [Language and Dialect Recognition](../by-program/2026-09-29-tuesday/22-tue-058-language-and-dialect-recognition.md)（6 篇）
- **周二 9月29日** 14:00-16:00 · Poster · [Cross-Lingual and Multilingual Speech Recognition 1](../by-program/2026-09-29-tuesday/34-tue-070-cross-lingual-and-multilingual-speech-recognition-1.md)（9 篇）
- **周二 9月29日** 16:30-18:30 · Oral · [Multilingual & Low-Resource ASR](../by-program/2026-09-29-tuesday/42-tue-078-multilingual-and-low-resource-asr.md)（6 篇）
- **周二 9月29日** 16:30-18:30 · Poster · [Robust ASR: Uncertainty and Confidence](../by-program/2026-09-29-tuesday/53-tue-089-robust-asr-uncertainty-and-confidence.md)（10 篇）
- **周三 9月30日** 09:00-11:00 · Poster · [Efficient Inference for ASR and Speech LMs](../by-program/2026-09-30-wednesday/16-wed-109-efficient-inference-for-asr-and-speech-lms.md)（10 篇）
- **周三 9月30日** 14:00-16:00 · Oral · [Domain Adaptation & Accented ASR](../by-program/2026-09-30-wednesday/26-wed-119-domain-adaptation-and-accented-asr.md)（6 篇）
- **周三 9月30日** 14:00-16:00 · Oral · [Multi-Speaker Processing, Personalization, and Adaptation](../by-program/2026-09-30-wednesday/27-wed-120-multi-speaker-processing-personalization-and-adaptation.md)（6 篇）
- **周三 9月30日** 14:00-16:00 · Oral · [Robust and Real-World ASR Systems](../by-program/2026-09-30-wednesday/28-wed-121-robust-and-real-world-asr-systems.md)（6 篇）
- **周三 9月30日** 16:30-18:30 · Oral · [Translation](../by-program/2026-09-30-wednesday/46-wed-139-translation.md)（6 篇）
- **周三 9月30日** 16:30-18:30 · Poster · [Robust ASR: Hallucinations and Biases](../by-program/2026-09-30-wednesday/53-wed-146-robust-asr-hallucinations-and-biases.md)（9 篇）
- **周三 9月30日** 16:30-18:30 · Poster · [New Architecture and Analyses for ASR and Speech LMs](../by-program/2026-09-30-wednesday/54-wed-147-new-architecture-and-analyses-for-asr-and-speech-lms.md)（6 篇）
- **周四 10月1日** 09:00-11:00 · Oral · [New Training Methods for ASR](../by-program/2026-10-01-thursday/05-thu-156-new-training-methods-for-asr.md)（6 篇）
- **周四 10月1日** 09:00-11:00 · Oral · [Code-Switching ASR](../by-program/2026-10-01-thursday/06-thu-157-code-switching-asr.md)（6 篇）
- **周四 10月1日** 09:00-11:00 · Oral · [Information Extraction and Retrieval / Survey Talk](../by-program/2026-10-01-thursday/07-thu-158-information-extraction-and-retrieval-survey-talk.md)（5 篇）
- **周四 10月1日** 09:00-11:00 · Poster · [ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency](../by-program/2026-10-01-thursday/15-thu-166-asr-under-real-world-constraints-streaming-adaptation-and-efficiency.md)（10 篇）
- **周四 10月1日** 09:00-11:00 · Show And Tell · [Speech Recognition, Enhancement and Real-Time Systems](../by-program/2026-10-01-thursday/19-thu-170-speech-recognition-enhancement-and-real-time-systems.md)（4 篇）
- **周四 10月1日** 14:00-16:00 · Oral · [Long-form Audio & New Attention Approaches](../by-program/2026-10-01-thursday/26-thu-177-long-form-audio-and-new-attention-approaches.md)（6 篇）
- **周四 10月1日** 14:00-16:00 · Poster · [Cross-Lingual and Multilingual Speech Recognition 2](../by-program/2026-10-01-thursday/37-thu-188-cross-lingual-and-multilingual-speech-recognition-2.md)（10 篇）

主题分布：asr 19 场、retrieval 2 场、asr-multitalker / asr-decoding / translation 各 1 场。多语低资源、流式/效率、多说话人与幻觉/不确定性是贯穿多日的主线；检索与翻译分别以关键词发现/示例检索与言语翻译评测—系统为侧翼。

---

## 技术趋势

### 稳健与高效 ASR

稳健性被拆成可诊断的子系统问题，而不只是“再加噪声增强”。一端是幻觉：从 Whisper 编码器激活/SAE 导向、解码器中间层探测，到对比解码（Whisper-CD）、音频锚输入与输入级门控，形成“内部表征—免训练推理干预”链条；另一端是数据与风格——嵌入选择从十万小时野外数据挑专科子集、把逐字/意译当作可控潜变量、测试时熵最小化统一自回归适应。效率侧则把激活位宽、帧间差分敏感 PTQ、亚 1-bit 分解、敏感度感知剪枝与 KV 池化并列为端侧手段；流式上出现统一离线/流式 Transducer、块内边界感知卷积、发射策略黑盒封装，以及分离前端与干净后端解耦的稳健流式管线。

### 多语、低资源与方言

共享技术动作是：**对齐与路由**压过单纯堆数据。多语 SLM/SSL 用渐进对齐、对齐感知继续预训练、语言平衡梯度投影与共享—私有 Fusion-LoRA 对抗主导语偏见与负迁移；参数高效路径包括供体 LoRA、MoE-LoRA/双层优化、FFN 后验升 MoE、GC-LoRA/MambAdapter 注入局部或状态空间结构。低资源侧强调错误类型诊断（南亚脚本混淆、印地/马拉雅拉姆复杂度分层、印度 22 语现实评测 lattice）、合成与课程（空管、希腊方言、R-MFT）、以及方言特有失败——普通话同音语义漂移的对比偏好、地理坐标条件化、西/法变体解码器偏置。评测本身成为贡献：Vimarsha、AfriVox-v2、Vividh-ASR、AppTek 客服长对话等刻意降低“干净基准乐观”。

### 多说话人与日志条件化 ASR

合成数据配方、日志条件化冻结解码器的 spoken LLM、全局—局部 MoE、说话人感知假设聚类，以及流式多说话人四架构选型，共同指向：**说话人信息必须在声学前端被显式保持或注入，而不是只靠序列化输出硬训解码器**。级联系统用日志三方共识剪泄漏；端到端 LLM 用 CoT 人数推断 + GRPO 结构约束，或切换 token 掩码抵抗未见切换次数。评测上 tcpSemER 与重叠分解提醒：编辑距离会漏掉改义错误，LLM 管线随重叠与人数上升更脆。

### 解码、搜索与推测

AR/NAR 张力推动半自回归与推测：CTC 起草 + 注意力/LLM 验证、NAR-MBR 期望效用、掩码扩散 NAR、扩散 LM 重打分与 CTC 联合。对比解码与多负例声学扰动成为长音频免训练补丁。理论工作试图统一“何谓自回归搜索”，便于只改搜索策略的消融。整体攻击的是：**在不重训大模型前提下，用草稿、约束 lattice、对比 logits 或并行采样换精度—时延**。

### 关键词发现与检索

开放词表 KWS 收敛到可扩展存储、流式对齐（注意力角色互换、音素 CTC）、端侧脉冲/模块扩展/通道剪枝，以及说话人门控的双零样本拒识。检索侧 SSL+DTW/离散匹配按任务分域；声学 NER 强化组织实体跨度；分词器 wav2tok 2.0 强调成对 token 对齐以利示例检索。人机闭环（Audio-KWS 门控纠错记忆、坐席 UI 回灌偏置）把检索接到持续纠错。

### 语音翻译与跨语生成

翻译场同时覆盖评测与系统：同传量规对齐、印地语族发音空间 S2ST、英中重音迁移、CoT 是否真用声学、台语字幕半监督建库、非洲野外域垂直基准。表达性言语翻译特邀综述把声纹/情感/局部韵律推到议程中心。与 ASR 交界处，级联字幕的时延—稳定边界、语码转换的偏好/强化学习/脚本保真，说明**翻译与转写共享“别把声学证据交给文本捷径”的压力**。

### 幻觉、偏见、不确定性与置信

幻觉检测走向模型内部（谱动力学、中间层、SAE）；缓解则有锚音频、对比解码、置信融合与小 LM 交叉注意力。偏见实验显示预训练可掩盖微调性别配比，儿童零样本误差更偏声学，老年/方言/语码需专用数据与对比目标。置信估计用 RanD 连续目标覆盖多种 ASR 头；上下文偏置则用匹配强度估计、熵门控音素偏置与声学检索门控，对抗过偏置与热词幻觉。

---

## 技术内容

### 周一 9月28日 · Multi-Talker ASR & Speaker Diarization

*11:00-13:00 · Oral · [docs/by-program/2026-09-28-monday/05-mon-006-multi-talker-asr-and-speaker-diarization.md](../by-program/2026-09-28-monday/05-mon-006-multi-talker-asr-and-speaker-diarization.md) · topic=`asr-multitalker`*

**Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization**（论文 443；Alexander Polok）

针对合成对话数据对 MT-ASR（DiCoW）与说话人日志（Sortformer）的影响做系统消融，并开源高效模拟器 FastMSS；结论强调最优仿真配方高度任务依赖——增大重叠利于 ASR 却损害日志，且宽域源多样性优于精确域匹配；纯合成可接近真实数据，合成+真实显著优于仅真实。

**Grounding Spoken LLMs in Multi-Speaker Audio via Diarization Conditioning**（论文 445；Alexander Polok）

提出日志条件化的 spoken LLM：用日志掩码条件化声学编码器提取目标说话人表示，冻结解码器，避免 Serialized Output Training 的灾难性遗忘；实例化为 Dixtral（DiCoW 编码器接入 Voxtral）。在 AMI、NOTSOFAR-1、LibriSpeechMix、Mixer6 上说话人归属转写相对若干商业/开源基线有大幅 cpWER 改善，并在远场多说话人 QA 上展示零样本与微调结果。

**GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR**（论文 1022；Yujie Guo）

端到端多说话人 ASR 中深层易稀释说话人特异性声学特征。GLAD 用全局—局部感知的动态 MoE 路由，融合说话人全局上下文与细粒度局部声学以引导专家选择；在 LibriSpeechMix 与 CH109 上显著优于既有 SOT 多说话人方法，高重叠更稳健。

**Speaker-Aware Hypothesis Clustering and Merging for Target-Speaker-free and Target-Speaker Multi-Talker ASR**（论文 1604；Yosuke Kashiwagi）

在 Hypothesis Clustering and Merging（HCM）中把连续说话人嵌入并入联合转写—说话人空间距离，改善同内容多说话人与目标说话人设定下的聚类/选择；相对常规 HCM，同内容条件下报告最高约 46% 相对 WER 下降，目标说话人设定相对离散说话人 ID 提示约 23% WER 下降。

**Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs**（论文 2005；Taejin Park）

把流式多说话人 ASR 按日志与 ASR 集成方式归为四类架构，共用开源流式 ASR/日志底座派生四套系统，系统比较多说话人精度、单说话人退化、显存与训练复杂度，给出部署约束下的选型指引。

**Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics**（论文 2912；Naohiro Tawara）

沿重叠鲁棒、语义保真、说话人数与单/多通道四轴比较 LLM 与模块化管线；提出用嵌入语义相似度替代编辑距离的 tcpSemER，并按重叠/非重叠分解 tcpWER。实验显示 LLM 在双说话人上有竞争力，但随人数与重叠上升更易退化，模块化管线更稳健。

### 周一 9月28日 · Search Methods and Inference Algorithms

*11:00-13:00 · Oral · [docs/by-program/2026-09-28-monday/06-mon-007-search-methods-and-inference-algorithms.md](../by-program/2026-09-28-monday/06-mon-007-search-methods-and-inference-algorithms.md) · topic=`asr-decoding`*

**Constrained CTC decoding for Efficient Diacritic Restoration**（论文 3220；Rufael Marew）

面向阿拉伯语转写的变音符恢复，以 CTC 非自回归语音—文本变音；解码时由未变音转写构造字符级 lattice，硬约束合法变音假设。在 ArVoice、ClArTTS 上相对更复杂的多模态基线显著降低变音错误率，兼具效率。

**Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding**（论文 3058；Hoseong Ahn）

Whisper-CD 为免训练对比解码：用高斯噪声、静音与时间平移三类声学扰动构造负向 logits，经 log-sum-exp 聚合后逐 token 对比干净音频 logits。在五个英语长音频基准上最高可降约 24.3 pp WER（CORAAL），吞吐相对 beam search 约高 48%。

**Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding**（论文 1953；Long Wu）

半自回归推测解码 SASD：在联合 CTC-attention 框架中，高置信用 CTC 贪心、低置信用注意力解码器精修。在 AISHELL-1、WenetSpeech 与工业数据上 CER 可比注意力重打分，速度约 2.8×–3.5×。

**Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts**（论文 2680；Avihu Dekel）

对语音 LLM 做自推测解码：低熵帧直接采纳 CTC 贪心假设，否则一次前向用放松准则验证，失败则从已接受前缀恢复自回归。九语料五语言上可同时加速并降 WER；HuggingFace Open ASR 上 1B LLM+440M CTC 达 5.58% WER，iRTF 约 4.4×，相对 AR 仅约 12% 相对 WER 上升。

**Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition**（论文 2971；Hiroyuki Deguchi）

NAR-MBR：对 NAR 输出分布采样，最大化期望效用而非输出概率；利用 NAR 一次前向高效多样本。在 LibriSpeech、Switchboard、AMI 与网络演讲语料上优于既有 NAR，且快于 AR。

**A Generalized Formalism of Auto-Regressive Decoding for Speech Processing**（论文 2768；Julia Gachot）

为语音处理中的自回归搜索给出显式纳入准则与统一理论形式化，便于围绕解码策略设计基准与消融，厘清何谓 AR/非 AR。

### 周一 9月28日 · Robust and Efficient ASR

*11:00-13:00 · Long Oral · [docs/by-program/2026-09-28-monday/09-mon-010-robust-and-efficient-asr.md](../by-program/2026-09-28-monday/09-mon-010-robust-and-efficient-asr.md) · topic=`asr`*

**MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding**（论文 488；Sabato Marco Siniscalchi）

MDM-ASR 用掩码扩散做 NAR ASR：预训练语音编码器 + 条件于声学与部分掩码转写的 Transformer 扩散解码器；提出迭代自校正训练与位置偏置熵界置信采样，弥合训推失配。多基准上持续优于既有 NAR，并接近强 AR，保留并行解码。

**Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders**（论文 1989；Georgii Aparin）

用 Whisper 音频编码器激活与稀疏自编码器（SAE）潜变量检测非语音幻觉，两者均线性可分且深层更强；提出激活空间与 SAE 潜空间导向。小/大模型非语音测试集幻觉率分别由约 72.63%/86.88% 降至 14.11%/27.33%，语音 WER 仅小幅退化。

**Which Data Matter? Embedding-Based Data Selection for Speech Recognition**（论文 3073；Zakaria Aldeneh）

从约 10 万小时野外伪标数据中，用说话人、音素与语义互补嵌入做相关性/多样性选择；CTC 模型上策略选择约 5% 子集可相对全数据最高约 36.8% 相对 WER 下降，服务领域专科模型。

**Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing**（论文 2792；Laurin Wagner）

把逐字/意译转写风格当作可控潜变量：用覆盖感知解码器任务 token 与平行风格对激活；德语不流畅 F1 自英语零样本由约 10% 升至 79%。并提出监督交叉注意力微调改善不流畅词级时间戳，以及 verbatimize 任务以规模化生成规范逐字稿。

**Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy**（论文 1060；Kiet Anh Hoang）

流式逆文本规范化：适配预训练文本到文本模型，引入 Read-Tag-Write 策略与架构/训练/推理优化；越南语实验精度可比非流式、优于混合 FST，满足实时时延。

**Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models**（论文 944；Chee-En Yu）

为自回归模型推导熵最小化测试时适应的严格目标，分解为 token 级策略梯度与熵项，统一解释既有启发式。以 Whisper 为试验台，在噪声、口音、多语等 20+ 域上一致提升。

### 周一 9月28日 · Information Extraction and Retrieval

*11:00-13:00 · Poster · [docs/by-program/2026-09-28-monday/16-mon-017-information-extraction-and-retrieval.md](../by-program/2026-09-28-monday/16-mon-017-information-extraction-and-retrieval.md) · topic=`retrieval`*

**Massive Open-Vocabulary Keyword Spotting**（论文 1444；Leonor Barreiros）

大规模开放词表关键词发现：相对可比基线把特征存储压缩至最多约 1/128，支持海量术语库且无需微调 ASR；实体召回与未压缩方案相当，并称对训练未见语言仍有效。

**SPARK: Efficient Audio-Text Matching for User-Defined Keyword Spotting via Spiking Neural Networks**（论文 3336；Seung-Yeop Baek）

SPARK 用脉冲驱动注意力做用户自定义文本关键词的音频—文本匹配，以累加替代重浮点；LibriPhrase 上相对 ANN 对标物参数约降 2.1×、能耗约降 21.7×。

**Scalable Keyword Spotting via Modular Network Expansion**（论文 987；Viktor Khaymonenko）

部署后增量加词：冻结基座（含 BN 与核心分类器），只训轻量扩展分支与新词头，避免旧触发器回归；相对参数匹配分模型基线平均新词 FRR 由 6.46% 降至 4.37%，并优于 adapters/LoRA。

**Streaming Open-Vocabulary Keyword Spotting via Role Swapping in Cross-Attention**（论文 1676；Liming Song）

流式开放词表：交叉注意力中互换角色，流式语音作 Query、注册表示作 Key/Value；约 0.8M 参数文本注册模型在 LibriPhrase 上报告 easy/hard 负例 EER/AUC。

**MPA-KWS: Multi-Modal Phoneme-Level Alignment for Streaming Open-Vocabulary Keyword Spotting**（论文 2485；Jue Zhang）

MPA-KWS 用 W-CTC 强制对齐与多模态音素级对比学习，并以 CTC beam-search 挖掘难负样本，服务流式开放词表；LibriPhrase 上称取得最佳结果。

**SSL-based Sequence Matching for Unsupervised Audio Retrieval**（论文 2369；Moreno La Quatra）

无标注音频检索：SSL 嵌入配合 DTW 或 K-Means+TF-IDF/BM25；哼唱检索偏 DTW，口语示例检索偏离散隐单元聚类。

**To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection**（论文 790；Mark Gales）

广播档案视听人物检索：用跨模态分数一致性做活跃模态检测（分类准确率 89%），再决定是否融合；BBC Rewind 上自适应 P@1 94.2%，优于固定融合与单模态。

### 周二 9月29日 · Resource Constrained Speech Recognition

*09:00-11:00 · Oral · [docs/by-program/2026-09-29-tuesday/06-tue-042-resource-constrained-speech-recognition.md](../by-program/2026-09-29-tuesday/06-tue-042-resource-constrained-speech-recognition.md) · topic=`asr`*

**Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR**（论文 1569；Woori Jeon）

DiffAQ：用帧间激活差分度量声学变化率，按比例分配 Hessian 重要性，使 GPTQ 类 PTQ 在 2–3 bit 超低比特把精度集中到音变关键帧；跨 Whisper 规格一致降 WER，2-bit 时基线常退化。

**Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition**（论文 683；Benedikt Hilmes）

忆阻器模拟计算中，变换后位置编码大输出值严重损伤 ADC；调整特定层 ADC 权重/精度比特相对降退化约 50% 且能耗估计稳定；若不可改 ADC，去掉编码相关线性变换可相对降约 30%。

**Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR**（论文 698；Woosuk Choi）

系统评估 Whisper tiny.en/base.en 的 80+ 种 INT/FP PTQ 配置：激活位宽远比权重格式关键；NVFP4 W4A16 在约 6.4× 压缩下距全精度约 0.07% WER；给出 20–80 MB 内存预算的 Pareto 与六条选型指引。

**Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition**（论文 2063；Jinsu Yeo）

LittleASR 用可变秩二值分解混合精度，把非关键层压到亚 1-bit，突破常规整数量化的 1-bit/参数下界，服务端侧 Conformer-Transducer。

**Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR**（论文 3411；Julian Irigoyen）

对 Whisper-small 做敏感度诊断：解码器 FFN 脆弱，解码器自注意力与晚期编码器层有可移除冗余；无微调下剪 50% 解码器自注意力在 LibriSpeech test-other 绝对降 WER 2.38%，剪后四层编码器 50% 降 1.72%，跨语料仍有增益。

**Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR**（论文 2124；Yi Wu）

KV-Pooling 对 Key/Value 平均池化利用语音时间冗余，保留 Query 分辨率；KV-Pooling-Zipformer 按层设差分池化步长，RNN-T 上 AISHELL-1/LibriSpeech 绝对降 CER/WER，RTF 约改善 10%。

### 周二 9月29日 · Multilingual, Cross-lingual & Low-Resource ASR

*09:00-11:00 · Poster · [docs/by-program/2026-09-29-tuesday/15-tue-051-multilingual-cross-lingual-and-low-resource-asr.md](../by-program/2026-09-29-tuesday/15-tue-051-multilingual-cross-lingual-and-low-resource-asr.md) · topic=`asr`*

**PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs**（论文 1734；Pei Zhang）

PART 以多阶段多任务渐进对齐训练多语语音到文本 LLM：逐步解冻 SLM 并分阶段引入任务，缓解仅训编码器导致的语言表示坍缩。

**Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning**（论文 1185；Xuyang Wang）

对齐感知继续预训练：在多语 SSL 上联合 SSL 与 CTC，使表征受文本对齐约束，并分析建模单元与语言感知双码本量化。

**Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition**（论文 2422；Zhe Zhang）

为空管构建含 TTS、声线与可控口音转换的合成管线；在 ATCO2 上微调 Whisper 的实验表明合成数据有助于识别。

**GigaAM Multilingual: Foundation Model for Underrepresented Languages**（论文 2483；Andrei Kuzmenko）

GigaAM Multilingual：HuBERT 风格目标在约 200 万小时上预训练 Conformer，聚类级平衡与域感知采样，面向中亚代表性不足语言；相对 Whisper Large v3、Omnilingual-1B 等在目标语尤其自发语音上报告增益。

**Low-Resource Medical ASR for Rich Transcription in Latvian**（论文 3469；Arturs Znotins）

拉脱维亚医学听写：比较端到端格式化与“逐字+LLM 后编辑”；用 LLM 整理遗留稿并加约 75 小时校正伪标与 50 小时人工数据，改善 WER、标点与医学实体。

**Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR**（论文 1133；Spandan Dey）

Whisper 上 LoRA-to-LoRA 跨语迁移：先谱系过滤再按正字法—分布相似选供体；供体知情初始化持续优于仅受体适配。

**Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages**（论文 1007；Kumud Tripathi）

分析达罗毗荼语更高 WER 与词长/词表稀疏，以及微调后解码器自/交叉注意力失衡；提出加权注意力等两项解码器增强。

**The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation**（论文 2454；Hadi Alizadeh）

发布 Toorintan-Persian Informal Dataset，规范化后微调；非正式数据训练可跨语体泛化，WER/BLEU 优于既有基线。

**BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR**（论文 2771；Xiaodong Cui）

BELLA：编码器经桥接对齐到 LLM token 空间，解码器用 MoE-LoRA 路由；训练为双层规划并用单环无值函数惩罚求解。

**Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation**（论文 1371；Dimitrios Damianos）

希腊语自动歌词转写的 Whisper 适配：考察缩放、转写—翻译多任务与两阶段语到唱；基于 Greek Audio Dataset 构建片段级语料，缩放持续受益。

**CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages**（论文 1770；Hongchen Wu）

CrossPhon-Tonal 在跨语强制对齐中引入自动声调映射的 tone encoding；六种声调语上与人工专家映射相当，并匹配或优于语言特定声学模型（摘要所述范围）。

### 周二 9月29日 · Language and Dialect Recognition

*14:00-16:00 · Oral · [docs/by-program/2026-09-29-tuesday/22-tue-058-language-and-dialect-recognition.md](../by-program/2026-09-29-tuesday/22-tue-058-language-and-dialect-recognition.md) · topic=`asr`*

**Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation**（论文 3091；Spandan Dey）

系统评估口语语言识别在白盒梯度对抗下的脆弱性，并提出 SDART：对抗样本挖掘、无教师防御蒸馏（动态在线标签平滑）与语言一致性正则；跨库与架构在干净与对抗样本上均优于多种常规对抗稳健法。

**Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0**（论文 975；Zhen Peng）

几何探测 Wav2Vec 2.0 五类汉语方言表征的三阶段轨迹：浅层声学差、中层高分散保留细语音细节、深层空间收缩但仍符合传统谱系；口音识别宜用中层，粗方言分类宜用深层。

**Robust Language Identification Using Semi-positive Contrastive Learning**（论文 2502；Shubham Sharma）

SpCL 用双模态音—文编码器与半正对比损失，区分同域强正对与跨域同语半正对，无需显式域适应；12 种印度语言多域实验上优于声学/语音学基线，未见域更稳健。

**Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR**（论文 3333；Pouya Mehralian）

Predict-Then-Adapt：冻结编码器上装轻量坐标回归头，先预测经纬度再做地理条件化方言 ASR；荷兰方言上 10–30 秒语音均值大圆误差约 15–25 km，CRH+GLoRIA 接近 oracle 坐标且参数/时延增量极小。

**Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties**（论文 458；Rodrigo Nieto）

西/法语十种变体、约 20 小时性别平衡语料上评七模型：法语偏欧陆变体，西班牙语出现多米尼加优于半岛、智利错误最高等非均匀差距；词汇与声学分析并诊断错误主要在解码器，反映与训练分布的语言距离。

**DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR**（论文 1228；Tao Zhang）

DASR-CPO：无参考对比偏好优化，用数据驱动混淆挖掘压制普通话同音语义漂移；MagicData 四川话（4.53 h）上 CER 24.85%→22.58%，方言实体 F1 72.82→74.15，推理零开销。

### 周二 9月29日 · Cross-Lingual and Multilingual Speech Recognition 1

*14:00-16:00 · Poster · [docs/by-program/2026-09-29-tuesday/34-tue-070-cross-lingual-and-multilingual-speech-recognition-1.md](../by-program/2026-09-29-tuesday/34-tue-070-cross-lingual-and-multilingual-speech-recognition-1.md) · topic=`asr`*

**Cross-Lingual Compositional Learning for Code-Switched Lip Reading**（论文 1163；Jeonghyeon Joo）

CoCoVSR 用跨语组合学习仅凭单语语料适配预训练多语唇读到语码转换，无需额外采集或合成；中英 CSLR 称 SOTA，并在所见/未见多语集上保持竞争力。

**Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR**（论文 977；Ryo Magoshi）

文本域适配 LLM-ASR：显式建模语音—文本对齐以生成更具表现力的伪音频提示，弥合模态缝；相对既有仅文本法改善整体错误率与 OOV 覆盖。

**Content-Aware Dynamic Compression for Efffcient Speech Recognition based on Large Language Model**（论文 230；Bingqian Wang）

内容感知动态压缩：用 CIF 按转写 token 数自适应对齐语音嵌入，训练与推理均可内容引导下采样；AISHELL-1/LibriSpeech 在可比平均嵌入长度下相对降错 12–26%，并可大幅缩短 ASEL/TTFT。

**Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition**（论文 1630；Kentaro Shinayama）

把预训练 Transformer 的 FFN 后验升级为 MoE 以扩容多语微调，推理只激活单一专家保持活跃参数不变；硬语言路由与可学习软路由均在 10 语 CommonVoice 及亚洲语评估上持续改善。

**Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition**（论文 2455；Hongxu Zhu）

可配置多语 ASR 中用 utterance 级编码器线索丰富的 token 无关语言表示替代解码器逐步执行的神经 LSM，把每 token 开销从二次降到线性；长句峰值推理时延可降逾 90% 且精度可比。

**GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation**（论文 822；Abeer Alwan）

GC-LoRA 向预训练 Transformer 编码器注意力输出投影注入 Conformer 风格局部卷积，捕获域特异局部依赖；在声学降质、带限、方言、儿童等多域相对基线最高约 10.9% WER 相对下降。

**MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio**（论文 1522；Umberto Cappellazzo）

MambAdapter 把轻量 Mamba 注入低秩瓶颈适配器并跨适配器参数共享；四类音频分类与五语识别上在更紧参数预算下匹配或超过强 PETL 基线。

**PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration**（论文 1787；Minsik Lee）

PhonePrune：音素集生成与音素感知校准保护“音素票”脆弱子网；50% 稀疏下尤其在韩/日 Common Voice 相对 Distil-Whisper 约 13.4%/13.8% WER 相对下降。

**Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian**（论文 1659；Yun Hao）

低资源西弗里西亚语上评估 LLM 生成纠错，并用非公开离线集控制污染；多数设定 GER 有效，最佳 GPT-5.1 结果可超 oracle WER，离线集增益表明非纯记忆。

### 周二 9月29日 · Multilingual & Low-Resource ASR

*16:30-18:30 · Oral · [docs/by-program/2026-09-29-tuesday/42-tue-078-multilingual-and-low-resource-asr.md](../by-program/2026-09-29-tuesday/42-tue-078-multilingual-and-low-resource-asr.md) · topic=`asr`*

**ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning**（论文 1077；Kiet Anh Hoang）

ViP-VL：ChunkFormer 上 Acoustic Stacking 与感受野对齐实现同步 8× 下采样，BEST-RQ 框架加掩码选择策略；约 1.7 万小时无标注越南语预训练，在 ASR/情感/方言/说话人验证四下游称新 SOTA 并开源。

**Dissecting ASR Failures in Low-Resource South Asian Languages**（论文 1382；Agha Ali Raza）

用 11 类错误体系剖析乌尔都、旁遮普、普什图、信德语：脚本混淆主导 Whisper 失败，SeamlessM4T 相对最好但仍远非生产级；跨语污染、稀有词与短句更难；标准 WER 可因正字法夸大约 3.1 点，转写后处理最高可回收约 25 点 WER。

**Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition**（论文 3408；Kavya Manohar）

Vividh-ASR 按工作室/广播/自发/合成噪声四档复杂度评测印地与马拉雅拉姆；早大更新与难到易课程促发 R-MFT，使 244M Whisper 匹配或超过常规微调的 769M；CKA/SVD 显示有效适配集中于解码器。

**Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR**（论文 1915；Wei-Qiang Zhang）

统一梯度投影 UGP：在统一投影空间用语言平衡重放的参考梯度约束更新，缓解主导语偏见；与数据级重放互补。跨低资源语组与规模有效适配并抑遗忘，Whisper-large-v3 上平均遗忘近零。

**Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning**（论文 2567；Vassilis Katsouros）

希腊方言低资源 Whisper 适配：邻域供体增强、识别—翻译多任务与由跨语翻译逐步过渡到方言 ASR 的课程；塞浦路斯/克里特/麦西尼亚三设定持续优于常规微调。

**Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations**（论文 3348；Kaushal Bhogale）

Vimarsha：覆盖印度 22 种排定语言约 100 小时，结合人口多样现场与难声学野外样本，并用变异 lattice 允许多合法转写；十模型排名在真实条件下显著重排，暴露地理/人口与语速等失败模式。

### 周二 9月29日 · Robust ASR: Uncertainty and Confidence

*16:30-18:30 · Poster · [docs/by-program/2026-09-29-tuesday/53-tue-089-robust-asr-uncertainty-and-confidence.md](../by-program/2026-09-29-tuesday/53-tue-089-robust-asr-uncertainty-and-confidence.md) · topic=`asr`*

**Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition**（论文 1040；Izabela Krysińska）

TOL 课程：由粗粒度语音学目标逐步过渡到音素级 CTC，缓解 blank 峰化与早期对齐不稳；英/法/波兰语上降 PER、加速收敛并更稳。

**Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization**（论文 1471；Wanting Huang）

Align-Consistency 把一致性正则扩展到 Align-Refine 非自回归迭代精修；全监督下对基座 CTC 与精修步均施 CR 增益可加，半监督用快速非 AR 在线伪标进一步提升。

**COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation**（论文 1097；Jhih-Rong Guo）

COALA 把 SLM 潜表示映射到判别空间量化音频段与候选实体匹配强度，并处理多稀有词共现时的训练坍塌；LibriSpeech 上跨不同偏置表规模持续改善上下文偏置。

**UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models**（论文 1577；Yong-Jie Hou）

UGPCB 免训练解码时偏置：熵门控与双模态对比惩罚抑制过偏置与同音误类；Dolphin base 上召回升约 16.04%（F1 90.81%），千 distractor 下召回仍升约 14.26%。

**Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs**（论文 2229；Vinayak Abrol）

严格仅训适配器对齐扩散 LLM 与冻结语音编码器：扩散相对自回归在适配器瓶颈下更耐误差传播，跨数据规模 RTF 与 ASR 更优。

**DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition**（论文 3232；Jaeeun Baik）

DASH 自蒸馏：多层编码器隐表示在干净—噪声成对视图上一致，并用原型分配 KL 稳定训练；LibriSpeech 多样噪声提升且保干净精度，额外开销约 4% 微调时间。

**Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition**（论文 879；Gaopeng Xu）

Whisper-Aware LLM：自监督量化声学物理缺陷，经置信融合解码向 LLM 提供高层指令与帧级注意力调制；AISHELL6-Whisper 相对 CER 降约 17%，幻觉率由逾 25% 降至 4.5%。

**Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models**（论文 1278；Bi-Cheng Yan）

因果中介与行为分析探测 SLM-ASR 幻觉，发现多头自注意力对文本 token 过度偏向；AudioSLM 以小 LM、对齐线索与交叉注意力抑幻觉，LibriSpeech 上优于部分 LLM-ASR。

**Rank-Distance Based Confidence Estimation for ASR**（论文 1355；Nagarathna Ravi）

提出连续目标分 RanD 的置信估计，覆盖 CTC/RNN-T/TDT/AED；印地与英语上优于 SOTA CEM，并泛化到失配域。

**Training-Free Intelligibility-Guided Observation Addition for Noisy ASR**（论文 1096；Haoyang Li）

免训练可懂度引导观测加性：由后端 ASR 可懂度估计融合噪声与增强语音权重；跨多种 SE-ASR 与数据优于既有 OA，并分析帧/句级与切换式变体。

### 周三 9月30日 · Efficient Inference for ASR and Speech LMs

*09:00-11:00 · Poster · [docs/by-program/2026-09-30-wednesday/16-wed-109-efficient-inference-for-asr-and-speech-lms.md](../by-program/2026-09-30-wednesday/16-wed-109-efficient-inference-for-asr-and-speech-lms.md) · topic=`asr`*

**ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling**（论文 315；Nicol Visser）

ZeroSyl 免训练从冻结 WavLM 中层 L2 范数抽音节边界与嵌入，K-means 离散后训 LM；跨词法/句法/叙事基准优于既有音节分词，且音节单元在句法建模上缩放更好。

**Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering**（论文 1010；Haoning Xu）

数据无关、训练无关的通道聚类压缩与层间混合稀疏；HuBERT-large 50% 稀疏相对幅度剪枝大幅降 WER，Whisper-large-v3 10% 稀疏亦有相对大幅改善且相对未压缩无显著恶化。

**OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting**（论文 1253；Alessio Burello）

OnDA 首次把端侧权重适应与在线结构化通道剪枝耦合做个性化 KWS；HeySnips/HeySnapdragon 最高约 9.63× 模型体积压缩（等任务），Jetson Orin Nano 上训练/推理时延与能耗相对仅权重适应有提升。

**Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device**（论文 1343；Szymon Klimaszewski）

把 STMC 用于模块化 CNN 的在线类 LSTM 推理，减冗余计算；相对等频标准 CNN/原 STMC 最高约 82%/46% MCPS 下降，GSC 11 类准确率最高 93.8%。

**An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation**（论文 1244；Haoran Wang）

基于 vLLM 的统一音频理解与生成推理管线，原生支持 delay-pattern 解交织与多流采样，并在连续批内共调度 CFG 条件/无条件请求，CFG 吞吐维持非 CFG 的约 80%。

**Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models**（论文 1737；Liang Cao）

Audio-NSP 仅数据中心 SFT 激活半自回归并行生成；针对文本—音频熵差提出模态感知动态截断，最高约 3.42× 加速且质量优于 MTP 基线。

**Improving streaming ASR with foundation models using emission policies**（论文 3358；Gerard Mas Mollà）

免训练、模型无关流式封装：滑窗缓冲、token 时间戳管理与纯文本发射策略；使 Parakeet、Canary 等带时间戳 SFM 在实时中接近离线质量而无需内部张量。

**AdaTS: Adaptive Token Sampling for Efficient Speech Language Models**（论文 2753；Sonal Sannigrahi）

AdaTS 按信息量自适应合并语音 token，LLM 所见长度可降 2× 以上；ASR/SQA/ST 常优于标准下采样，推理成本约降 40%。

**Merging the Knowledge of LLMs for Automatic Speech Recognition**（论文 2561；Hayato Futami）

通过 LoRA 参数算术把外部 LM 合并进 LLM-ASR，推理无额外 LM 开销；CSJ/LibriSpeech 域扩展与迁移一致改善目标域且不损速度/显存。

**Scaling few-shot spoken word classification with generative meta-continual learning**（论文 408；Batsirayi Mupamhi Ziki）

生成式元持续学习 GeMCL 在每类仅五样本下顺序学习区分约 1000 个口语词类；相对反复全微调 HuBERT 等，性能可比冻结特征头方案但适应约快 2000×、数据与时间少得多。

### 周三 9月30日 · Domain Adaptation & Accented ASR

*14:00-16:00 · Oral · [docs/by-program/2026-09-30-wednesday/26-wed-119-domain-adaptation-and-accented-asr.md](../by-program/2026-09-30-wednesday/26-wed-119-domain-adaptation-and-accented-asr.md) · topic=`asr`*

**SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training**（论文 856；Minglin Wu）

SEA-MDD 在 wav2vec 2.0 Transformer 块嵌入 MLP 测试时训练模块，训测均自监督更新，使误发音检测诊断动态适配新样本分布。

**Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper**（论文 1373；Mehedi Hasan Bijoy）

MoAA：可学习软口音码本加权检索注入口音线索并路由轻量口音适配器，对抗性别头减泄漏，无参考幻觉抑制；AESRC 上 WER 7.49%、CER 3.81%。

**Contrastive Regularization for Accent-Robust ASR**（论文 949；Van-Phat Thai）

监督对比学习作 CTC 微调的口音不变辅助目标，无结构改动与显式口音监督；L2-ARCTIC 未见口音最高约 25–29% 相对 WER 下降，表征几何更紧凑。

**Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR**（论文 1969；Carlos Carvalho）

评 11 种合并算法于 10 个欧洲葡萄牙语域，并提出 BoostedTSV-M 缓解秩坍缩；总体优于全微调且在单模型中保 OOD/英多语泛化。

**Activation Steering for Accent Adaptation in Large Audio Language Models**（论文 2166；Ting Dang）

层间均值移位估计口音敏感带（中层编码器），推理时无参数激活导向对齐口音与标准嵌入；八口音一致降 WER。

**AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization**（论文 710；Sang-Hoon Lee）

AccentDrift：稀疏语音标记化+口音/音色适配器的实时口音转换，缓存感知流式约 520 ms 时延，优于既有并行口音转换并保留内容与说话人身份。

### 周三 9月30日 · Multi-Speaker Processing, Personalization, and Adaptation

*14:00-16:00 · Oral · [docs/by-program/2026-09-30-wednesday/27-wed-120-multi-speaker-processing-personalization-and-adaptation.md](../by-program/2026-09-30-wednesday/27-wed-120-multi-speaker-processing-personalization-and-adaptation.md) · topic=`asr`*

**Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction**（论文 3191；Suresh Singh）

级联多说话人 ASR 中用预训练日志作多模态校验，按时间包含、词汇交叉验证与时间对齐三方共识剪除泄漏片段；高泄漏子集相对 cpWER 最高约降 29%。

**Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts**（论文 2297；Yunrui Cai）

未知说话人数下联合多说话人 ASR/日志：CoT 增广 SFT 先推断人数，再用 GRPO+多维约束奖励优化排列不变精度与结构约束；Libri3Mix/Dynamic-Mix 上 GRPO 相对 SFT+CoT 约 35%/54% 相对 cpWER 下降。

**KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting**（论文 1586；Wenbin Jiang）

KFC-KWS 用 CTC 峰化后验选关键帧，跨音频/音素/文本融合；LibriPhrase 平衡 AUC 98.73%，hard 子集 AUC 97.65%、EER 7.75%。

**Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising**（论文 3422；Sergio Burdisso）

LLM-ASR 仅文本适配表述为去噪，多视图噪声驱动组批混合源音文、投影噪声稿、合成损坏源/目标稿，保对齐且无新参数；相对未适配最高约 25.4% 相对 WER 改善。

**AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning**（论文 288；Haoyu Zhang）

AQA-TTRL：测试时强化学习，多数票伪标+置信加权与多次采样稳定优势；MMAU/MMAR/MMSU 上 Qwen2.5-Omni 7B/3B 平均升约 4.42%/11.04%，适配后 3B 可超未适配 7B 直推。

**AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR**（论文 2029；Long Wu）

AFG-Bias：跨模态声学检索从大候选表选热词，声学融合门控注入解码抑幻觉；三 LLM-ASR 骨干在金融/医学相对 CER 最高约降 74.1%，AISHELL-1 热词 F1 最高升约 5.4 点。

### 周三 9月30日 · Robust and Real-World ASR Systems

*14:00-16:00 · Oral · [docs/by-program/2026-09-30-wednesday/28-wed-121-robust-and-real-world-asr-systems.md](../by-program/2026-09-30-wednesday/28-wed-121-robust-and-real-world-asr-systems.md) · topic=`asr`*

**Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades**（论文 1821；Shinyoung Sun）

大规模分析 LLM 语音翻译级联的时延—稳定权衡：过激端点可致排队雪崩（中位 RTF>1）；区分首字与稳定文本时延，并指出 Whisper 提示条件化损害短块流式 ASR；定义中位 RTF≤1 的运营阈值。

**Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR**（论文 689；Daniele Giuseppe Falavigna）

Fed-SpeechLLM：英意双语非 IID 联邦 SpeechLLM，语言感知梯度聚合与采样聚类缓解多语失衡，选择性聚合编码器与投影、冻结 LLM；性能接近中心化。

**Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses**（论文 127；Yiteng Huang）

智能眼镜佩戴者识别：多通道差分 ASR 融合波束形成、麦克风选择与轻量侧聊检测；模拟与真实数据相对传统最高约 18.0% 相对 WER 下降。

**ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era**（论文 2698；Masao Someki）

ESPnet3：配置驱动数据组织与分片、统一 Python 工作流；OWSM 预训每轮约省 21.1 分钟且多节点 GPU 利用率>80%，新模型/数据约 46 行代码可接入。

**SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR**（论文 3436；Kavya Manohar）

SCRIBE 诊断评测：砂提容忍对齐与领域词注入，分解词法/标点/数词/领域实体错误；并发布印地/马拉雅拉姆/卡纳达富转写开源模型与 LLM 整理管线。

**Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction**（论文 363；Taira Ashikawa）

增量 ASR 后纠：Audio-KWS 门控从音频检索相关纠错记录再经 LLM 编辑；Earnings-21/CSJ 约 70% 提示压缩且改善 WER/CER 与 Bias-F1。

### 周三 9月30日 · Translation

*16:30-18:30 · Oral · [docs/by-program/2026-09-30-wednesday/46-wed-139-translation.md](../by-program/2026-09-30-wednesday/46-wed-139-translation.md) · topic=`translation`*

**Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting**（论文 1105；Ziyu Zhang）

同传人工评分语料（1101 段）对齐意义/表达/时延量规；结构化 LLM 提示与标量监督易坍缩量规。双回归头 LoRA 适配 COMET-KIWI 在保留谈话级测试集上 Pearson LQ/EXP 达 0.388/0.301。

**ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation**（论文 2384；Khushal Yadav）

ARTIST：印地语族到英语端到端 S2ST，中间 CTC 监督源发音特征到语言无关量化空间，卷积增强差分 Transformer 解码；约 166M 参数在 11 语（含每语约 10h）上 BLEU/COMET/chrF 超 1.2B SeamlessM4T。

**Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation**（论文 2321；Yuchen Song）

英→中 S2ST 词汇重音迁移：构建重音标注中文数据与 XLS-R 普通话重音检测器，结合 EmphAssess 提客观指标，并微调 CosyVoice3；重音翻译能力显著优于既有系统且翻译质量具竞争力。

**Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation**（论文 800；Federico Costa）

归因、损坏转写与韵律意识评估表明 CoT 语音翻译 heavily 依赖文本转写、近似级联；向 CoT 注入噪声转写等训练干预可增强声学依赖与稳健性。

**A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus**（论文 2096；Yuan-Fu Liao）

台语语音—中文字幕：三模态 AVLM + 迭代伪标与 VLM 融合 OCR；字幕 CER 36.8%→9.3%，860 小时语料使 Whisper 跨语转写 CER 57.8%→37.8%，台—中翻译 BLEU 约翻倍。

**AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition**（论文 3140；Busayo Awobade）

AfriVox-v2：全支持语种野外非脚本音频，十行业域垂直与数字/命名实体专项；评 Sahara-v2、Gemini 3 Flash、Omnilingual CTC 等，暴露现代语音模型在噪声非洲场景的泛化缺口。

### 周三 9月30日 · Robust ASR: Hallucinations and Biases

*16:30-18:30 · Poster · [docs/by-program/2026-09-30-wednesday/53-wed-146-robust-asr-hallucinations-and-biases.md](../by-program/2026-09-30-wednesday/53-wed-146-robust-asr-hallucinations-and-biases.md) · topic=`asr`*

**From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales**（论文 1420；Ivan Viakhirev）

光谱敏感性定理预测深层由分散区到吸引子区相变；Whisper Tiny–Large-v3-Turbo 对抗下中等规模交叉注意力秩坍缩约 13.4%，大模型自注意力秩约 −2.34% 进入压缩吸引态。

**Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition**（论文 2666；Abhijit Sinha）

成人→儿童严格零样本下 Wav2Vec2/HuBERT/Data2Vec 各层混合 ASR：最佳 WER 相近但表征变异大，LLM 后纠几乎无助，错误主要由声学表征局限驱动。

**Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms**（论文 3047；Seshan S）

控制微调数据性别组成：预训练 ASR 上男女 WER 无一致方向，从头训练则随组成呈方向性差距；大规模预训练掩盖微调配比效应。

**Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition**（论文 1124；Naijun Zheng）

有限真实数据训 LLM 多说话人：双编码器交织、长度感知说话人 ID 损失与重叠区 ASR 损失自适应加权；AliMeeting/Aishell4 相对开源基线约 18%/24% 相对提升。

**Multi-Talker ASR Unaffected by Speaker Change Count**（论文 1582；Naoki Makishima）

自注意力中说话人切换 token 掩码，使模型无法从上下文推断切换次数，避免训练未见更多切换时崩溃。

**WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations**（论文 102；Hui Wang）

WildElder：野外中文老年语音细粒度标注语料（转写/年龄/性别/口音强度），开源并定位为具挑战 ASR/画像基准。

**Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval**（论文 907；Pranshu Nema）

ASR 后专名接地：细 G2P、粗 Soundex 与语义嵌入融合；Whisper-large-v3 / Qwen3-ASR-1.7B 的 Recall@1 相对精确匹配分别升 36.4/23.6 个百分点。

**From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection**（论文 338；Jan Jasiński）

真实语音人工标注上比较文本指标、LLM 与解码器内部探测；无参考时 Whisper 解码器中间层探测最强，文本+内部晚融合最佳。

**Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR**（论文 1314；Saurabh Kumar）

输入前拼接罕见短锚音频免改模型检测非语音幻觉，并比较五种推理策略；整体 WER 32.18%→13.23%，非语音幻觉错误率 0.14%，时延可比 VAD 管线。

### 周三 9月30日 · New Architecture and Analyses for ASR and Speech LMs

*16:30-18:30 · Poster · [docs/by-program/2026-09-30-wednesday/54-wed-147-new-architecture-and-analyses-for-asr-and-speech-lms.md](../by-program/2026-09-30-wednesday/54-wed-147-new-architecture-and-analyses-for-asr-and-speech-lms.md) · topic=`asr`*

**Convolutional Dynamic Rotary Positional Encoding**（论文 1312；Euijin Hong）

CD-RoPE 用深度可分卷积按局部声学扭曲旋转时间索引；Branchformer 相对 RelPos 全 LibriSpeech 测试一致降 WER，参数少约 2.2M，SRB 时域扰动优势最大。

**Diffusion Language Models for Speech Recognition**（论文 2070；Davyd Naveriani）

将 MDLM/USDM 用于假设重打分，并与 CTC 帧级分布联合生成候选；二者均可显著提升文本准确率，代码与配方公开。

**Do speech foundation models really learn words?**（论文 2676；Robin Huo）

残差化剔除音素后 HuBERT/wav2vec 2.0 后期层仍编码相对独立于局部语音内容的词，可增强词发现中的高阶语言信息。

**Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception.**（论文 2439；Baptiste Ramonda）

CLEAR+合成语音与声学降质下，可读性指数与 WER 近乎解耦，挑战以文本复杂度代理机器可懂度的假设。

**Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains**（论文 905；Simon Gonzalez）

探测显示语音嵌入对声学/语音学属性线性可及较强，对形态/句法结构弱，信息呈分布式梯度。

**I Am No One: Style-Aware Paraphrasing for Text Anonymization**（论文 3175；Ahmed Sohair Khan）

风格感知少样本 LLM 改写压制 stylometric 指纹；博客/评论归属 F1 降 60–70%，内容质量保持，优于 DP 等基线，风险延伸至 ASR 转写。

### 周四 10月1日 · New Training Methods for ASR

*09:00-11:00 · Oral · [docs/by-program/2026-10-01-thursday/05-thu-156-new-training-methods-for-asr.md](../by-program/2026-10-01-thursday/05-thu-156-new-training-methods-for-asr.md) · topic=`asr`*

**Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization**（论文 1195；Andrei Andrusenko）

统一 RNNT：块限注意力+动态分块卷积支持离线/流式，并提出 MCR-RNNT 模式一致性正则缩差距；改善低时延流式且保离线，框架与英语检查点开源。

**BACON: Boundary-Aware Convolution for Streaming Conformer Models**（论文 1455；Hainan Xu）

BACON 替换流式 Conformer 因果卷积：块内通道分组为因果与边界感知双向，扩感受野且参数不变；单/多说话人 ASR 与语译任务精度升、时延可比。

**Progressive Alignment Objectives for Aligner-Encoder based ASR**（论文 2132；Jaeyoung Lee）

InterAligner 加深对齐器中间目标与 InterCTC，使对齐沿深度渐进形成；LibriSpeech 17 层 Conformer 上由仅最终对齐器 5.0/7.8 降至 3.1/5.6 WER，长句增益最大。

**From Bilevel to Trilevel: Joint Training for Speech Recognition**（论文 1738；Jen-Tzung Chien）

三层联合训练：监督、无监督与蒸馏目标，用顺序惩罚双层梯度下降折叠下层；FastConformer+LibriSpeech 上优于两阶段预训微调与既有双层法。

**LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR**（论文 2149；Jaeyoung Lee）

LLM-as-Joiner：Aligner-Encoder 产生 U 个 token 级语音状态注入预训练 LLM（上层 LoRA），上下文短于 speech-as-prefix；LibriSpeech 与多语 Common Voice 超同规模基线，并与轻量识别头联合训练有额外增益。

**Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging**（论文 371；Ka Hyun Park）

源无关语音分类：元学习目标中心模型合并多源预训练，在稀缺目标标签下缓解表征错位；Macro-F1 最高超基线约 14.5 点。

### 周四 10月1日 · Code-Switching ASR

*09:00-11:00 · Oral · [docs/by-program/2026-10-01-thursday/06-thu-157-code-switching-asr.md](../by-program/2026-10-01-thursday/06-thu-157-code-switching-asr.md) · topic=`asr`*

**LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR**（论文 1113；Yuxuan He）

LLM-HB：MoE 适配器+辅助语言头捕获多语表示，LLM 提示注入热词；ASRU2019 相对基线 MER 约降 20.30% 至 5.85%（15 distractor），并发布热词表。

**Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech**（论文 642；Yue Heng Yeo）

以 Code Mixing Index 引导偏好学习，使 TTS 合成更忠实语码边界；微调 Whisper Large 在 SEAME DevMAN/DevSGE 上 MER 12.1%/17.8%→8.9%/14.2%。

**Reinforcement Learning for Data-Efficient Code-Switched ASR**（论文 2667；Ziwei Ye）

GRPO 可验证奖励：错误率+脚本保真，两遍草稿精修；仅 TTS 语码数据、10% 数据匹配全量 LoRA，跨 10 语对，零样本迁移到真人语码集。

**Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs**（论文 110；Minh Duc Pham）

DPO 对齐 Audio LLM 英—普通话语码：针对漏语、翻译代转写、幻觉构造偏好对；10 万对（570h）上分布内 MER 最高约降 89.6%，分布外约 20.0%。

**Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR**（论文 1099；Enes Yavuz Ugan）

贝叶斯因子化适配把切换相关知识并入强多语 ASR 而不覆写；少量合成数据下语码词错误约降 32.87%，总体 WER 约降 5.31% 且保单语。

**Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation**（论文 3334；Nabeel Mohammed）

孟加拉—英语语码流式：动态块在线+VAD 对齐推理与脚本锚定借词注入；提出 CS-WER 诊断切换/词根/后缀，并迁移到经期医学域。

### 周四 10月1日 · Information Extraction and Retrieval / Survey Talk

*09:00-11:00 · Oral · [docs/by-program/2026-10-01-thursday/07-thu-158-information-extraction-and-retrieval-survey-talk.md](../by-program/2026-10-01-thursday/07-thu-158-information-extraction-and-retrieval-survey-talk.md) · topic=`retrieval`*

**Expressive Speech Translation**（论文 特邀/综述；Philipp Koehn）

特邀综述：言语到言语翻译中的表达性保持（声纹、情感、停顿、语速、重音等），覆盖数据、合成、表征、架构、LLM 与评测，指出领域尚缺共识。

**Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification**（论文 1130；Ming-Hsiang Hu）

ZP-KWS：音素监督音频编码器 × GE2E 紧凑说话人编码器（约 0.9M）乘法晚融合，双零样本拒识；LibriPhrase 等上目标-only FRR@1%FAR 相对最强基线最高约降 60%，总参约 1.55M。

**wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval**（论文 141；Adhiraj Banerjee）

wav2tok 2.0：分阶段对比+VQ 后再 CTC/DTW 对齐一致性，可扩展对齐感知分词；QbE-STD 上持续优于 BEST-STD 与通用分词器。

**Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition**（论文 3115；Spandan Dey）

声学 NER 中组织实体难：LLM 定向语义增强、类别边界监督与结构约束实体学习；显著改善组织识别并保 ASR。

**AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification**（论文 1316；Sourav Ghosh）

AnySimLite 把多种语音相邻分类化为细粒度文本相似，词/字符双通道少样本；最差情况性能降幅<7% 而模型体积约 <1/250 的 qLLaMA_LoRA-7B。

### 周四 10月1日 · ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency

*09:00-11:00 · Poster · [docs/by-program/2026-10-01-thursday/15-thu-166-asr-under-real-world-constraints-streaming-adaptation-and-efficiency.md](../by-program/2026-10-01-thursday/15-thu-166-asr-under-real-world-constraints-streaming-adaptation-and-efficiency.md) · topic=`asr`*

**A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR**（论文 3380；Yinchang Yang）

123M 全开源日语缓存感知流式 RNNT/CTC；CER 分层策展与五域渐进微调。五测试集平均 CER 12.4%（RNNT），优于更大 OWSM-CTC v4 / ReazonSpeech，RTFx 批 1220、流式 446。

**Robust Streaming ASR with Decoupled Separation and Recognition**（论文 1503；DeLiang Wang）

解耦在线分离前端与仅干净数据训的流式 ASR 后端，避免多条件训练伤干净语音；LibriSpeech/CHiME-4/LibriCSS 持续优于 MCT，并可模块化包裹大预训练模型。

**Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints**（论文 3545；Hanwen Zhang）

MACR：仅对目标词类内吸引、对难负例边距排斥，不把异构 Unknown 全局聚拢；GSC V2 事件级流式在 ≤0.5 FA/h 相对 CE 超 40% 相对 FRR 下降，推理零开销。

**Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting**（论文 3546；Hanwen Zhang）

因果时间关系蒸馏：传教师时间拓扑而非逐点特征，下三角掩码保证历史可实现；GSC V2 因果 1D-CNN 准确率 95.12%→96.91%，1.0 FA/h 下 FRR 约减半。

**Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR**（论文 2309；Seunghee Ma）

无重放持续 ASR：熵引导 token 级蒸馏定义保留方向，冲突时保留投影；相对 LwF 顺序适配后平均 WER 相对降 7.2%，Common Voice 多语退化平均降 51.5%。

**Parameter-Efficient Continual Learning for Automatic Speech Recognition**（论文 3169；Steven Vander Eeckt）

PECL：按奇异值划分头尾子空间，只在低能尾子空间做近似旋转适配并跨任务权重平均；两基准遗忘更少、总体更优。

**MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition**（论文 2111；Theresa Pekarek Rosin）

MoDiCoL 模块化诊断持续学习数据，可控组合语言内容、说话人与声学环境，并配真实启发课程评三种持续策略。

**SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation**（论文 3243；Ye-Eun Ko）

SCOLoRA：按说话人嵌入相似动态平衡子空间对齐与正交分离；持续说话人适配上改善新说话人并减遗忘。

**Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition**（论文 322；Anmol Guragain）

MoPE-LoRA：六类发音方式低秩专家+音素监督与声学门控的帧级路由，专家跨口音共享；L2-ARCTIC 零样本留一口音相对单 LoRA 约 12.3% 相对改善。

**First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks**（论文 1858；Siqi Cai）

First-to-Spike：输出层首峰即退出，配合 WTA 与混合时间训练；语音与神经生理数据上更高精度、更低时延与能耗。

### 周四 10月1日 · Speech Recognition, Enhancement and Real-Time Systems

*09:00-11:00 · Show And Tell · [docs/by-program/2026-10-01-thursday/19-thu-170-speech-recognition-enhancement-and-real-time-systems.md](../by-program/2026-10-01-thursday/19-thu-170-speech-recognition-enhancement-and-real-time-systems.md) · topic=`asr`*

**A light weight Continuous Speaker Verification System for Real time Monitoring**（论文 3584；Harish Rajamani）

通话中连续说话人验证：ReDimNet-B1+三元组投影，跨语/噪声/混响增强；RTF 0.05、318M MACs，TidyVoice EER 2.08%。

**WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications**（论文 3588；Harish Rajamani）

WaveNorm 时域神经 AGC：内容感知增益，满足 ITU-T P.56/P.79，约 6 dB 降噪，49M MACs、55KB，适边缘实时。

**Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices**（论文 3602；Atila Orhon）

Argmax Pro：移动端编排十亿级模型做实时转写+日志+自定义词表，基于上下文偏置与流式日志并发研究，对标云端功能。

**A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction**（论文 3610；Shiva Shankar Arumugam）

MACE 人机闭环：实时实体建议，UI 纠正回灌为上下文偏置或后替换规则；ContextASR-Bench+Whisper-large-v3 上 NE-WER/EditRate 相对无偏置约降 17.1%/18.6%。

### 周四 10月1日 · Long-form Audio & New Attention Approaches

*14:00-16:00 · Oral · [docs/by-program/2026-10-01-thursday/26-thu-177-long-form-audio-and-new-attention-approaches.md](../by-program/2026-10-01-thursday/26-thu-177-long-form-audio-and-new-attention-approaches.md) · topic=`asr`*

**AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR**（论文 2047；Eugen Beck）

发布 AppTek Call-Center Dialogues：十四种英语口音、十六类客服角色扮演长对话，降低与大规模预训重叠风险；口音与切分策略显著影响开源 ASR 表现。

**Segmental Attention Decoding With Long Form Acoustic Encodings**（论文 341；Xinwei Li）

分析 AED 切分训练隐式绝对位置与长形连续编码不兼容，提出显式位置、长上下文训练、段拼接与语义切分四项改动以弥合精度差距。

**M-LAMA: Multimodal Automated Scoring of Long-form Spoken English**（论文 1542；Minh Dao-Xuan-Quang）

M-LAMA 双编码器融合原始音频、ASR 文本与题目，三阶段训练应对钟形分数；87,226 场会话上结构化多模态对齐提升五项评分可靠性。

**Attentive Mamba: Channel-wise Local Attention for Speech Recognition**（论文 1708；Jen-Tzung Chien）

Attentive Mamba：因果深度卷积上下文化后在时间局部窗做跨通道注意力，动态参数化 SSM 状态转移，实验确认利于 ASR。

**Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition**（论文 929；Da-Hee Yang）

AVSR 对比解码按注意力动态与预测分歧自适应缩放干预强度，避免干净条件过纠；LRS3 跨干净与低 SNR 一致提升。

**Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models**（论文 593；Ravi Kumar）

LEAF-X：熵引导注意力加权与多层 rollout（可选因果消融）生成稀疏 token—帧归因，相对强基线更忠实稳定。

### 周四 10月1日 · Cross-Lingual and Multilingual Speech Recognition 2

*14:00-16:00 · Poster · [docs/by-program/2026-10-01-thursday/37-thu-188-cross-lingual-and-multilingual-speech-recognition-2.md](../by-program/2026-10-01-thursday/37-thu-188-cross-lingual-and-multilingual-speech-recognition-2.md) · topic=`asr`*

**How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR**（论文 920；Simon Gonzalez）

在 FLEURS 上从 Whisper/Seamless 输出测语音学—形态—句法—词汇相似度：语义保持来自跨维交互，两架构整合语言信息机制不同。

**Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision**（论文 2446；Shreyas Gopal）

语言感知蒸馏：查询库+门控选/混查询 token 的 Q-Former，缓解共享投影语言干扰；指令跟随相对匹配多语蒸馏基线约 +14%，并合成 Audio-MLQA，最佳模型相对既有 Speech LLM 约 +32%。

**ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition**（论文 3143；Zi Haur Pang）

ERM-MinMaxGAP 在 MELD-ST 英/日/德多模态情感识别上加自适应公平权重与 MinMaxGAP；Qwen2-Audio 上性能升约 5.5%/5.0% 同时缩性别差距。

**Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA**（论文 1183；Jie Liu）

共享—私有 Fusion-LoRA + Mean-Teacher 置信门控一致性；Kathbath 上相对 Whisper-small+LoRA 宏 WER 约降 35.4%，五语均提升。

**Speech Encoder Fusion for LLM-based Automatic Speech Recognition**（论文 1039；Jakob Poncelet）

融合多预训练语音编码器（学习组合与 Transformer 融合等）增强 LLM-ASR；单语/多语与日志语音识别均有提升且开销有限。

**Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens**（论文 3002；Daigo Takizawa）

固定 NAC 或 SSL 预训练语言做交叉实验：下游对 NAC 训练语不敏感，对 SSL 预训练语强依赖——NAC 可跨语复用，SSL 语需对齐目标语。

**SᴜTRA: Structurally-Unified Tokenization with Root Awareness**（论文 291；Vaibhav Rathore）

SUTRA 形态感知分词保 akshara 并惩罚跨形态边界合并，缓解 Morphological Shattering；印地/马拉地/古吉拉特新分割数据上 Boundary F1/语义可恢复性与翻译 chrF2 均有摘要所述增益。

**Measuring the Redundancy of Decoder Layers in SpeechLLMs**（论文 1873；Adel Moumen）

跨两 LLM 族与 1–8B 尺度，SpeechLLM 解码器冗余大体继承自文本 LLM；7–8B 约仅需 60% 解码层仍可保较好 ASR，且冗余块跨编码器/任务/语言可共享。

**Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models**（论文 1767；Yuan Li）

WMR2L：置信与残差分散联合加权伪标，弱置信掩码与多扰动一致性；CHiME-4/SLURP/CORAAL 相对 WER 降约 13.8%/25.0%/15.7%，语译亦有增益。

**Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition**（论文 3465；Tung X. Nguyen）

POI 感知对比：扰动语码关键区并用 LLM 扩近错假设，声学/音素/文本过滤难负例后 LoRA 微调 Whisper-small；CS-FLEURS 与 ViMedCSS 上总体与语码感知错误率均降逾 2%。

---

## 跨会场判断

- **正在固化**：Whisper/语音 LLM 作为默认底座；LoRA/适配器/MoE 路由与“冻结大块、只动接口”成为多语、口音、域适配的默认工程形态；开放词表 KWS 与热词偏置普遍要求可扩展词库、流式对齐与过偏置抑制。
- **正在固化**：免训练或轻干预推理补丁（对比解码、锚音频、发射策略封装、观测加性）被用来修补已部署大模型的长音频幻觉与流式缺口，而不是每次重训。
- **正在固化**：评测叙事从单一 WER 转向错误类型、重叠/语义度量、方言与野外条件、富转写与实体代价——SCRIBE、tcpSemER、Vimarsha、AfriVox-v2 等把“测什么”本身当作贡献。
- **仍开放**：合成多说话人数据的最优配方高度任务依赖（重叠利于 ASR、伤日志），真实远场+高重叠+未知人数下 LLM 端到端与模块化管线谁更稳，尚无统一赢家。
- **仍开放**：多语持续学习中主导语偏见、负迁移与灾难性遗忘的联合治理（梯度投影、共享—私有、尾子空间旋转、说话人相似条件正交）方法多、可迁移处方仍少。
- **仍开放**：CoT/级联翻译是否真正使用声学与韵律、表达性 S2ST 的数据与指标共识，以及语码转换中“保单语能力 vs 学切换”的帕累托边界。
- **仍开放**：端侧极限压缩（亚 1-bit、激活格式、忆阻器 ADC）与大模型精度之间的可复现权衡；剪枝作正则、解码器层冗余等现象提示容量利用不均，但跨任务通用剪枝图仍缺。
- **仍开放**：幻觉/偏见的因果定位（编码器谱相变 vs 解码器文本偏置 vs 预训练数据配比）已有诊断，但可泛化的训练目标与评测协议尚未像 WER 那样标准化。

---

*统计：24 场次，169 篇条目。生成自 `data/topics_assigned.json` 指定主题过滤。*
