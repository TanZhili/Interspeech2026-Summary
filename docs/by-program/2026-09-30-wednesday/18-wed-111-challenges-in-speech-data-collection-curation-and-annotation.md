# Challenges in Speech Data Collection, Curation, and Annotation

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：14
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场专题讨论语音数据采集、整理与标注的挑战：长上下文医疗对话合成、印度真实电话 ASR 基准、临床嗓音采集工具、澳式英语发音反馈数据集、喜马拉雅低资源自发多语语料、达基尼方言感知方法、工业故障多模态数据、高保真房间声学仿真对增强的影响、广播 SSL 过滤权衡、隐私优先的野外韵律采集、游戏化韵律标注与表示探测、大规模音源分离自动整理、神经指纹辅助标注，以及认知启发的阿尔茨海默多模态增强。主线是数据本身成为一等公民的研究方法。

合成与仿真被用来填补长上下文与稀缺病理数据；真实世界基准强调非脚本、多方言与拼写变体；开源工具与隐私优先协议降低合规与偏见成本。低资源与接触变体要求说话人分层与方言感知标注。工业与音乐侧展示通道级基准与自动清洗流水线；SSL 过滤策略在 ASR 收益与通用音频理解之间存在可量化权衡。

## 技术内容

### 合成基准、真实世界 ASR 与临床采集工具

**Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization**（论文 2901；Yanis Labrak）  
三阶段开源权重管线：人格驱动对话、多说话人音频合成（重叠/停顿、房间声学、声音事件）与 LLM 参考 SOAP 笔记。发布 8,800 段合成会话、约 1.3k 小时音频与参考笔记；摘要称级联系统仍显著优于端到端模型。

**Voice of India: A Large-Scale Benchmark for Real-World Speech Recognition in India**（论文 3189；Kaushal Bhogale）  
闭源基准：非脚本电话会话，15 种主要印度语言、139 区域簇，306,230 句、536 小时、36,691 说话人，转写计入拼写变体。提供区县级地理分析及音质、语速、性别、设备等因素诊断。

**CalliOpeNLP: A Standalone Digital Health Voice Data Collection Research Tool**（论文 1783；Brian Stasak）  
开源 Python 独立工具：18 项临床验证嗓音任务的计算机生成口说说明，录音、标注并经低延迟语音转文本分析跟踪依从，避免不安全数据传输，服务临床嗓音生物库。

**Pronunciation and Intonation Structured Markup (PRISM): A Dataset for Australian English Pronunciation Feedback**（论文 2830；Olga Maxwell）  
对 CommonVoice 人口分层子集做词级强制对齐与人工标注，用语者学知情编码类标注相对澳英的发音“差异”。报告港/南亚/印尼三口音组的初步错误模式，并讨论开放数据人口失衡挑战。

### 低资源多语/方言与工业多模态数据

**Collection and Curation of a Spontaneous Multilingual Speech Corpus for Low-Resource Himalayan Languages**（论文 2634；Abhijit Sinha）  
320 名博多、宗喀、廓尔喀（尼泊尔语）、夏尔巴母语者自发语料，跨藏缅与印欧、含声调/非声调。描述一致录制与元数据协议；声学分析显示音高、能量与时间动态系统差异；语种识别最高准确率 92.95%。

**Spontaneous Dialect-Aware Speech Corpus for Low-Resource Dakhini, A Southern Indo-Aryan Language: Methods, Challenges, and Insights**（论文 2640；Anindita Mondal）  
基于电话会话考察语码转换、性别与教育背景变异；自发语音见音系缩减、助动词省略与分词变异，正式语境转向标准印地/乌尔都形式。提出说话人分层与方言感知标注指南。

**Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals**（论文 838；Xiaoxiao Miao）  
单速链式输送机多模态数据：三路音频与四路振动，覆盖正常与四类故障、多速度/负载及现场复现工厂噪声。提供无监督故障检测与监督分类的标准协议，以及通道级 kNN 基线。

**Improving multichannel speech enhancement through accurate room-acoustic simulations**（论文 2512；Georg Götz）  
比较几何声学低保真与波场+几何混合高保真仿真增强的 SpatialNet。在实测数据上，高保真训练相对低保真最高使中位 WER 相对降约 38%。

### 过滤权衡、隐私韵律采集与自动整理/增强

**Data Filtering Trade-offs in Self-Supervised Speech Representation Learning: A Study on Unconstrained Broadcast Audio**（论文 50；Yaroslav Getman）  
芬兰广播数据上比较无过滤、能量 VAD、神经 VAD、神经 VAD+LID。能量 VAD 持续损害表示；神经 VAD+LID 用约 42% 数据可将 ASR 绝对 WER 最高降约 12.7%，但更选择性过滤使通用音频理解最多降约 9 个百分点。

**Collecting Prosody in the Wild: A Content-Controlled, Privacy-First Smartphone Protocol and Empirical Evaluation**（论文 2417；Timo K. Koch）  
脚本朗读标准化词汇内容（含提示效价），设备端提韵律特征后立即删除原始音频。N=560、9,877 条录音；用提取特征诊断预测自我报告性别与瞬时效价/唤醒。

**From Game-Based Annotation to Representation Probing: Cross-Validated Prosodic Speech and Privacy Implications**（论文 2459；Sia Vosh Sepanta）  
基于网页交互游戏语料，玩家兼表演者与标注者形成自验证机制。情绪识别与 LLM 对齐语音表示探测显示韵律嵌入编码稳定情感模式，中间表示仍可识别情绪属性，引出隐私考量。

**Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset**（论文 190；Yu Ji）  
七类乐器 taxonomy、乐器特异单源检测器、多语关键词爬取与自动清洗。检测器七类平均准确率 97.14%；用清洗数据训练 SOTA，标准基准平均 SDR 提升 1.16 dB。

**Leveraging Discriminative Capabilities of Self-Supervised Neural Audio Fingerprinting for Efficient Speech Data Annotation**（论文 1436；Kemal Altwlkany）  
将音乐检索神经指纹用于语音去重（产业数据标注量约减半），并显示其嵌入比 WavLM 等更好捕捉语音声学属性；用最远点采样保持多样性、避免偏向过表示样本。

**Cognitive-Heuristic Guided Multimodal Data Augmentation for Alzheimer’s Disease Detection Using LLM and TTS**（论文 1724；Cheng Gong）  
检索增强 LLM 生成认知知情文本，属性引导 TTS 复现 AD 相关声学特征。多基准上摘要称增强数据持续提升基于语音的 AD 检测性能。

## 本场要点

- 合成长上下文医患对话同时服务训练与可控评测，级联仍强于端到端。
- Voice of India 强调非脚本、多方言与拼写变体的真实 ASR 评测。
- 开源临床采集与隐私优先手机协议降低合规与偏见成本。
- 喜马拉雅多语与达基尼接触变体需要分层与方言感知整理。
- SSL 过滤在 ASR 与通用音频理解之间存在明确权衡。
- 自动清洗、指纹去重与认知启发增强把规模化数据策展工程化。

## 覆盖核对

| id | title |
|---|---|
| 2901 | Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization |
| 3189 | Voice of India: A Large-Scale Benchmark for Real-World Speech Recognition in India |
| 1783 | CalliOpeNLP: A Standalone Digital Health Voice Data Collection Research Tool |
| 2830 | Pronunciation and Intonation Structured Markup (PRISM): A Dataset for Australian English Pronunciation Feedback |
| 2634 | Collection and Curation of a Spontaneous Multilingual Speech Corpus for Low-Resource Himalayan Languages |
| 2640 | Spontaneous Dialect-Aware Speech Corpus for Low-Resource Dakhini, A Southern Indo-Aryan Language: Methods, Challenges, and Insights |
| 838 | Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals |
| 2512 | Improving multichannel speech enhancement through accurate room-acoustic simulations |
| 50 | Data Filtering Trade-offs in Self-Supervised Speech Representation Learning: A Study on Unconstrained Broadcast Audio |
| 2417 | Collecting Prosody in the Wild: A Content-Controlled, Privacy-First Smartphone Protocol and Empirical Evaluation |
| 2459 | From Game-Based Annotation to Representation Probing: Cross-Validated Prosodic Speech and Privacy Implications |
| 190 | Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset |
| 1436 | Leveraging Discriminative Capabilities of Self-Supervised Neural Audio Fingerprinting for Efficient Speech Data Annotation |
| 1724 | Cognitive-Heuristic Guided Multimodal Data Augmentation for Alzheimer’s Disease Detection Using LLM and TTS |
