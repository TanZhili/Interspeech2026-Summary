# Challenges in Speech Data Collection, Curation, and Annotation

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：14

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场专题讨论语音数据采集、整理与标注的挑战：长上下文医疗对话合成、印度真实电话 ASR 基准、临床嗓音采集工具、澳式英语发音反馈数据集、喜马拉雅低资源自发多语语料、达基尼方言感知方法、工业故障多模态数据、高保真房间声学仿真对增强的影响、广播 SSL 过滤权衡、隐私优先的野外韵律采集、游戏化韵律标注与表示探测、大规模音源分离自动整理、神经指纹辅助标注，以及认知启发的阿尔茨海默多模态增强。主线是数据本身成为一等公民的研究方法。

合成与仿真被用来填补长上下文与稀缺病理数据；真实世界基准强调非脚本、多方言与拼写变体；开源工具与隐私优先协议降低合规与偏见成本。低资源与接触变体要求说话人分层与方言感知标注。工业与音乐侧展示通道级基准与自动清洗流水线；SSL 过滤策略在 ASR 收益与通用音频理解之间存在可量化权衡。

## 论文技术总结

# Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization

- 论文编号：2901
- 报告人：Yanis Labrak
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/labrak26_interspeech.pdf

## 问题
长上下文音频推理（>5 分钟）缺少训练与评测资源；开放式摘要/笔记类任务难用自动指标，真实临床音频又受隐私限制。现有公开资源规模小或仅有文本，难以支撑长对话 SOAP 笔记生成。

## 方法
全开源权重流水线三阶段：人格属性采样（724 条主诉等）→ Gemma3-27B 多轮对话生成 → Qwen3-TTS 人格条件声音克隆，再经重叠/停顿、音效、scaper 时间线与 PyRoomacoustics 诊室 RIR、Opus 压缩等声学仿真。参考 SOAP 先抽 grounding 事实 JSON 再生成笔记；评测用两阶段 LLM-as-a-judge（Kimi K2）及 ROUGE/医学概念 F1。释放 Synth-DoPaCo：8,800 对话、1,329 小时音频，均分约 9 分钟。

## 实验与结果
湿音频上 Whisper Large V3 WER 约 2–3%，Qwen3-ASR 约 10–14%。参考笔记 faithfulness 5.0；级联（Whisper/Qwen3-ASR + Qwen3-Thinking）faithfulness 约 3.1–3.3，E2E Omni 约 2.7；逐 claim 幻觉率 E2E 约 32%、级联 22–24%、参考约 1%。表面 ROUGE 上 E2E 可更高，但忠实度与简洁度更差。UTMOS 与真实 mock 接近（1.27 vs 1.28）。

## 结论
合成管道可同时作训练与可控评测资源；当前开源系统中级联因更高忠实度、更低幻觉更可取，瓶颈在长对话临床推理而非近天花板的 ASR。局限包括参考笔记为 LLM 生成、仅英语双人首诊、声学难度可能仍低于真实临床。

## 点评
把隐私受限的临床长音频任务做成可复现的 sim2real 评测床，并强调 faithfulness 优于表面重叠指标，方向对。强在人格多样性、声学仿真与 grounding 笔记流程；弱在参考与裁判都偏 LLM、WER 偏低暗示难度可能不足，外推真实部署需谨慎。


# Voice of India: A Large-Scale Benchmark for Real-World Speech Recognition in India

- 论文编号：3189
- 报告人：Kaushal Bhogale
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhogale26_interspeech.pdf

## 问题
现有 Indic ASR 基准多为脚本化、较干净语音，公开榜易过拟合；单参考严格 WER 惩罚印度语言自然拼写与语码混合变体，且聚合指标掩盖地区差异，难反映真实电话对话表现。

## 方法
构建闭源评测集 Voice of India：非脚本电话双人对话，按人口比例从 139 区域簇采样，覆盖 15 种主要印度语言，306,230 句、536 小时、36,691 说话人。多轮人工交叉校验转写，并用 Gemini 等构建拼写/切分变体 lattice；用 Orthographically-Informed WER（OIWER）评测。评估 14 个系统（含 Sarvam、Gemini、IndicConformer、OmniASR 等），并按地区、音质、语速、时长、人口统计切片分析。

## 实验与结果
多数模型多语 WER 常超 20；SARVAM AUDIO 在 15 语中 13 语最低，但仍在 Bhojpuri（20.9）、Maithili（24.8）超阈值。地区 WER 约 4%（Nainital）至 44%（Mannarakkat），印地语带与都市偏低，南印与北比哈尔等偏高。公开 FLEURS 上强的模型在 VoI 上显著变差；音质差、过慢/过快、短句均抬高错误。人口统计差异较小（女性略好约 3.1–4.3%，年轻略差）。

## 结论
真实印度口语 ASR 仍有明显语言与地区鸿沟；多参考/ orthography-aware 评测更能反映识别质量。作者按失败模式给出分档改进建议（低资源方言、短句/噪声、语言检测失败等）。

## 点评
把“能上榜”与“能上线”拆开，用地理与条件切片暴露偏差，对 Indic ASR 很有针对性。强在规模、lattice/OIWER 与闭源防过拟合；弱在完整测试集需申请、部分 API 在个别语言上崩溃式失败需结合语言检测一起解读。


# CalliOpeNLP: A Standalone Digital Health Voice Data Collection Research Tool

- 论文编号：1783
- 报告人：Brian Stasak
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stasak26_interspeech.pdf

## 问题
临床嗓音数据采集常依赖当面人工操作，易受交互偏差（Hawthorne 效应、治疗性提示不一致）、无关闲聊拉长录音、事后才质控、以及商业工具收费/数据外传等问题，缺少开源、可本地部署的自动化方案。

## 方法
发布 Python 开源工具 CalliOpeNLP：先采集人口学信息，再用 pyttsx3 合成语音 + 屏幕文字引导 18 项临床验证嗓音任务（Cape-V 短语、计数、Happy Birthday、最大发声 /a/ /s/ /z/、音高范围、Rainbow Passage、My Voice 等）。sounddevice 按任务计时录音（7–45 s，44.1 kHz），自动命名标签；Whisper tiny（可换 large）本地转写；对“朗读”任务用 Levenshtein 与 FuzzyWuzzy token-set-ratio 与金标准比对，阈值默认 0.70 时提示警告并允许重录；会话结束生成报告。表演性任务暂不自动合规评分。

## 实验与结果
正文为工具设计与流程说明，未报告大规模用户试验数值；强调 tiny 模型约 <3 s/任务、全程离线无第三方传输，并给出 GitHub 发布地址。合规阈值与最优设定称仍在进一步测试。

## 结论
作者认为自动化可统一指令与任务顺序、近实时合规反馈、减少人工切分与交互偏差，便于多站点一致建库；工具面向临床嗓音生物库，也可扩展到非医疗语音采集。表演性任务自动合规与阈值标定仍是后续工作。

## 点评
把“采集协议 + 本地 ASR 合规”做成可改参数的开源流水线，切中临床嗓音建库的实际痛点。强在离线隐私与任务级自动切分标签；弱在尚无系统可用性/合规准确率实验，且表演性任务依赖示例回放而非自动评分，ASR 在病理嗓音上误差会直接影响合规判定。


# Pronunciation and Intonation Structured Markup (PRISM): A Dataset for Australian English Pronunciation Feedback

- 论文编号：2830
- 报告人：Olga Maxwell
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maxwell26_interspeech.pdf

## 问题
商业/自动发音反馈工具反馈有限、常缺科学依据，且忽视世界英语与 ESL 语音变异；现有学习数据语言覆盖窄或不开源，难以支撑面向澳大利亚英语（AusEng）、含韵律的个性化反馈。

## 方法
从 CommonVoice 英语分区（v21.0）按人口学分层抽取 Hong Kong、South Asia、Indonesia 口音子集；Montreal Forced Aligner（english_mfa）做词级对齐并由语音学家校正。三位语音学家按 AusEng 与自组织音系/韵律方案标注：13 大类、53 细类（元音/辅音、核调、停顿、突出、节奏、拼写、连读等），“error”定义为相对 AusEng 的差异。平台 ingest TextGrid；本文报告 859 条标注的初步分布。

## 实验与结果
分段错误约占 49.9%，韵律约 46.1%；最常见细类为 pause insertion（10.2%），其后 linking、rhythm 等。口音不均衡：印尼说话人贡献约 42.6% 观察（仅 3 人但人均录音多），Hong Kong 停顿与辅音比例更高，印尼元音/节奏/重音更突出，南亚多见摩擦音（齿擦音停顿化）等口音特异模式。说话人表：南亚 50/82、香港 19/53、印尼 3/82。

## 结论
作者提供面向 AusEng 反馈的开放标注框架与初步错误模式，强调音系–计算机跨学科协作；标注验证与互评信度为进行中工作，并指出开放数据人口学不平衡等挑战。

## 点评
把“对/错二元”换成相对 AusEng 的语言学可解释类目，并显式纳入韵律，适合教学反馈建模。强在透明编码与口音对比；弱在说话人极不均衡（尤其印尼）、全文在结果段有截断、且尚无互评信度与下游模型数字，现阶段更像方法与数据白皮书。


# Collection and Curation of a Spontaneous Multilingual Speech Corpus for Low-Resource Himalayan Languages

- 论文编号：2634
- 报告人：Abhijit Sinha
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sinha26_interspeech.pdf

## 问题
东喜马拉雅走廊语言多样但自发多语语料稀缺；野外采集噪声不一、转写成本高，需要在一致协议与元数据下收集可计算的验证型资源，而非仅堆数据量。

## 方法
采集 Bodo、Dzongkha、Gorkhali（Nepali）、Sherpa 共 320 名母语者（每语 80 人）、约 146 小时室内自发独白（每人 5 段，均长约 5.5 分钟），44.1 kHz 或 16 kHz 原样保存，带年龄/性别/环境元数据；不因质量剔除。用 YIN 提 F0、WebRTC VAD 估语速做声学刻画；语种识别将音频重采样 16 kHz、切 10 s，说话人独立 80/20，比较 MFCC 与 pitch/intensity/loudness 及融合，分类器为 SVM 与 CNN。无转写。

## 实验与结果
语言级均值 F0：Bodo 173.7、Dzongkha 163.4、Gorkhali 156.5、Sherpa 141.9 Hz；语速亦有系统差异。单特征 CNN：MFCC 85.95%、loudness 76.09%、pitch 仅 56.86%。融合后 MFCC+Loudness 91.97%，全特征（MFCC+Loudness+Intensity+Pitch）达 92.95% accuracy（balanced 92.41%）。性别分布不均（Sherpa 74 男/6 女）会影响音高分离解读。多语预训练表示初步实验未达竞争力。

## 结论
一致协议下的自发语料即使无转写也可支撑声学刻画与说话人独立 LID；谱特征为主、能量/韵律互补。语料可用于喜马拉雅低资源语言后续建模与文献记录。

## 点评
用“声学结构 + LID 可学性”做语料验证，比单纯发布小时数更有说服力。强在四语平衡说话人数与严格说话人分割；弱在性别失衡、无转写限制下游 ASR、设备采样率混杂，且 LID 准确率不能直接外推到其他任务。


# Spontaneous Dialect-Aware Speech Corpus for Low-Resource Dakhini, A Southern Indo-Aryan Language: Methods, Challenges, and Insights

- 论文编号：2640
- 报告人：Anindita Mondal
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mondal26b_interspeech.pdf

## 问题
Dakhini（德干接触变体）口语资源匮乏；无标准书面语、声望低，录音场景易触发向标准 Hindi/Urdu 的语码切换（观察者效应），若缺乏结构清单，采集到的可能是“干净但不地道”的数据。

## 方法
先做结构与社会语言学预研形成诊断特征清单；电话场景、熟人男女配对对话，非对称知情（仅 anchor 知情，对方事后告知并知情同意）；Hyderabad 约 160 说话人（17–50 岁，约 70% 男），每通约 20 分钟取约 5 分钟。pyannote 说话人日志后保留未知情说话人；IndicConformer Hindi ASR 预转写，将与标准形式的偏差当作方言信号，规则标签 PA/PV/MAUX/MP-KO/MP/SF/LD，按标签密度分流人工复核。

## 实验与结果
正文以方法与案例为主：预调研中弱势群体在正式场合更常用 Dakhini（如劣势背景男 10/15、女 11 使用），受教育群体更常转向标准语（男 6/15、女仅 2）。给出标准–Dakhini 对应表（如 itnaa→ittaa、aadmii→admii、省略 hai、kaiku/nakko 等）。未报告大规模 ASR 词错误率等下游基准数字；结论段在抽取文本中截断。

## 结论
作者强调真实方言建库依赖结构知识、社区嵌入招募与降低监控感的采集设计，而非仅录音设备；方言感知规则标注可把 ASR 标准化错误转化为有用信号，为方言敏感 ASR/对话建模奠基。

## 点评
把社会语言学观察者效应直接写进采集协议（电话 + 非对称知情），对非声望变体很关键。强在诊断清单驱动的 QC 与半自动标注 triage；弱在正文几乎无量化语料/系统评测、伦理上的隐蔽录音需严格事后同意执行，且全文尾部截断限制对最终规模声明的核对。


# Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals

- 论文编号：838
- 报告人：Xiaoxiao Miao
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26f_interspeech.pdf

## 问题
公开工业故障数据多在实验室、单模态（音频或振动）、面向轴承/电机等部件；噪声常缺失或事后合成，难评测产线级系统在真实厂噪下的多通道融合。

## 方法
发布 SSCC 单速链板输送机数据集：3 路音频（Zoom H5、iPhone 11、Xiaomi）+ 4 路振动（电机单轴 + 对端三轴，100 kHz），同步切 5 s，共 6,669 样本。覆盖正常与 lean/dry/loose/screwdrop 四类故障，速度档 20–100、负载重/中/轻，以及现场录制厂噪由扬声器回放的干净/噪声条件。协议：无监督故障检测（仅正常训练、跨速度 zero-shot 到 vel=100）与监督分类（hold-out vel=80 等）；统一通道级 kNN 探针（检测 k=1，分类 k=11），比较 BEATs、CED、DaSheng、EAT、ECHO、FISHER 等预训练编码器的 audio/vibration/融合表示。

## 实验与结果
检测 AUROC：多数编码器音频优于振动（如 FISHER 音频 0.954 vs 振动 0.546）；融合常提升振动并有时超过单模态（BEATs 融合 0.891）。分类准确率普遍较高（如 ECHO 音频 Acc 0.975，DaSheng 融合 0.967）；振动对 screwdrop 更有利，音频对 loose 更好，融合多数情况下最优。

## 结论
数据集提供可复现的多模态工业故障基准；模态贡献因任务与故障类型而异，简单距离基线已有可用表现，但仍有高级表示与融合的提升空间。

## 点评
把产线级输送机、多设备音频与真实厂噪注入放进同一评测协议，补上 MaFaulDa/HUSTmotor 类数据的缺口。强在通道级公平探针与跨工况划分；弱在仍为实验室平台回放噪声、低速仅正常干净条件，且基线冻结编码器+kNN，不能代表专用工业模型上限。


# Improving multichannel speech enhancement through accurate room-acoustic simulations

- 论文编号：2512
- 报告人：Georg Götz
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gotz26_interspeech.pdf

## 问题
多通道语音增强训练常依赖简化几何声学（如镜像源 ISM）合成 RIR，难以刻画模态、衍射与刚性散射体；仿真保真度对真实阵列增强与下游 ASR 的影响尚缺系统比较。

## 方法
固定 SpatialNet-small（16 kHz，Eigenmike 六通道子集）与训练流程，比较三类增广：ISM-U（随机房间/T20）、ISM-M（匹配混合法房间尺寸与 T20）、Hybrid（Treble SDK 波场+几何混合，频率相关材料，含 Eigenmike DRTF）。在实测 Motus/Arni6DoF RIR 构造的 LibriCSS-EM6（约 5000 句、六种重叠条件）上评测增强后 Kaldi 转写的中位 WER。

## 实验与结果
Hybrid 在各重叠条件下均最优；相对 ISM-U 中位 WER 相对改善最高约 38.3%（OV40），总体约 30%；相对 ISM-M 总体约 16.3%。除 0L 对 ISM-M 的置信区间跨零外，其余配对改善均显著。未增强噪声混响 WER 约 73–88%。

## 结论
更高物理保真度的房间声学仿真可在不改网络与训练策略的情况下提升多通道增强与下游识别；仿真保真度本身构成可迁移的增益来源。

## 点评
把“增广保真度”从网络架构里拆出来，用实测阵列评测闭环，结论对数据中心路线很有说服力。强在 ISM-M 控制场景参数后仍见差距；弱在阵列与网络固定为 Eigenmike/SpatialNet，外推到商用小阵列需再验证。


# Data Filtering Trade-offs in Self-Supervised Speech Representation Learning: A Study on Unconstrained Broadcast Audio

- 论文编号：50
- 报告人：Yaroslav Getman
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/getman26_interspeech.pdf

## 问题
用原始广播音做 SSL 预训练时，是否只留语音、是否只留目标语，常凭启发式决定；能量 VAD 等廉价过滤对表示质量的影响缺少受控比较。

## 方法
在约 20,400 小时芬兰 AlfaTV 存档上固定 wav2vec 2.0 Base，比较四种过滤：Raw（30 s 切分）、能量 VAD（Auditok）、神经 VAD（pyannote）、神经 VAD+音频 LID（ECAPA）。保留量约 100%/86.5%/58.4%/42.3%。在 Common Voice、FLEURS、VoxPopuli 上微调 ASR；ML-SUPERB 冻结探测 CER；ARCH 评非语音事件与音乐分类。

## 实验与结果
E-VAD 全面劣化 ASR（如 CV test WER 39.4 vs Raw 34.2）；N-VAD+LID 最佳（CV test 21.5，相对 Raw 绝对降最多约 12.7 点），N-VAD 次之。冻结探测趋势一致。ARCH 上 Raw 在 8 任务中 6 项最优，选择性过滤可降最多约 9 个百分点；N-VAD 在 ASR 与通用音频间较均衡。神经过滤 RTF 远高于能量法。

## 结论
无普适最优过滤：神经 VAD（±LID）利于目标语 ASR，但牺牲通用音频理解并增加预处理成本；能量 VAD 看似省事却常伤 SSL。应按下游目标权衡。

## 点评
把广播 SSL 过滤做成四档对照并同时测 ASR 与 ARCH，直接打穿“多滤一点总更好”的直觉。强在同架构同步数；弱在领域偏芬兰电视、LID 无域内金标，跨语广播上 LID 收益可能更大。


# Collecting Prosody in the Wild: A Content-Controlled, Privacy-First Smartphone Protocol and Empirical Evaluation

- 论文编号：2417
- 报告人：Timo K. Koch
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koch26_interspeech.pdf

## 问题
野外采集韵律时，语义与韵律常纠缠；存原音频又有隐私与合规障碍。缺少可在手机上标准化词内容、仅上传特征的可落地协议。

## 方法
在 PhoneStudy EMA 中嵌入朗读模块：每日末次提示朗读正/中/负价脚本句；设备端 openSMILE 提特征后立即删除原音频，仅同步特征向量。德国配额样本 Android 用户两期各约两周；用特征过滤无效录音，并以随机森林做说话人性别与瞬时效价/唤醒预测作诊断。

## 实验与结果
提示发起率 67.8%，发起后三句完成率 96.9%；过滤后 9,877 条、560 人。条件对 F0 范围无显著差，HNR 与 voiced segments/s 有小幅条件效应；说话人 ICC 约 0.33–0.69。性别预测平衡准确率约 91.8–92.0%（eGeMAPS/ComParE）；效价/唤醒相关较弱（ρ 中位数约 0.02–0.13）。

## 结论
内容受控 + 端上删原音的协议可规模化采集可分析韵律特征；说话人信息保留强，瞬时情感自报预测弱，适合作为野外韵律基线模块而非情感金标准。

## 点评
同时解决“词内容控制”与“GDPR 友好”，工程完整且有大样本合规数据。强在隐私设计与合规率；弱在朗读≠自发韵律、情感预测弱说明特征对状态敏感度有限，且仅 Android。


# From Game-Based Annotation to Representation Probing: Cross-Validated Prosodic Speech and Privacy Implications

- 论文编号：2459
- 报告人：Sia Vosh Sepanta
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sepanta26_interspeech.pdf

## 问题
情感语音库常标注人少、演员少、短句缺语境；游戏化采集能否产出可用韵律数据，以及语音–LLM 中间表示是否泄露情感/年龄等隐私属性，需要实证。

## 方法
Actor’s Challenge（GWAP）：玩家交替“试镜”按情境录中性句与“选角”匹配语境并打分，形成自验证。当前约 240 用户、1,018 录音、七类情绪。用 emotion2vec 嵌入 + 轻量分类器做 ASER，并与 RAVDESS、Emozionalmente 交叉；再以 Whisper→MEUSLI→EuroLLM 冻结管线探测情感与年龄泄漏。

## 实验与结果
4 类 ASER：AC 英/意 Acc 约 0.73/0.75，混合降至 0.60；RAVDESS 0.92。跨库到 AC 较差（约 0.32–0.40），AC→RAVDESS 可达 0.93。表示探测 7 类情感：LLM 隐状态 Acc 0.21，投影/编码器约 0.41–0.42，表明情感在中间层已可分。

## 结论
游戏化自验证可构建多语语境化韵律库；情感线索可被下游模型利用，但中间表示的情感/人口属性可探性带来隐私风险，发布与使用需谨慎。

## 点评
把标注一致性内置进游戏循环，并延伸到表示隐私，视角新。强在自验证与跨库对照；弱在规模仍小、参与衰减、态度韵律覆盖不足，ASER 数字更像可用性探针而非 SOTA 竞赛。


# Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset

- 论文编号：190
- 报告人：Yu Ji
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ji26_interspeech.pdf

## 问题
音乐源分离缺大规模细粒度乐器标注；网络爬取易有标签噪声与混音，人工建库成本高，常见 4-stem 粒度不足。

## 方法
定义 7 类固定 stem（Piano/Drums/Bass/Acoustic Guitar/Electric Guitar/Strings/Wind-Brass）；冻结 Dasheng 编码器上训练每类单源二分类器（3 s/16 kHz）；多语关键词爬 YouTube 得 ACMID-Uncleaned；分段检测后从 48 kHz 原音频拼接纯净段得 ACMID-Cleaned。开放爬虫与检测权重。

## 实验与结果
检测器七类平均准确率 97.14%（Dasheng 优于 Music2Latent/CNN）。用清洗数据训分离模型：相对未清洗平均 SDR 提升明显（Cleaned 平均 4.63 vs Uncleaned 2.24 dB）；与 MoisesDB+MedleyDB 合并后平均 SDR 6.05，相对原基线约 +1.16 dB。清洗后时长大幅收缩（如 Wind-Brass 2259.72→102.64 h）。

## 结论
自动单源检测可有效清洗网络乐器数据并支撑更细粒度 MSS；清洗质量比单纯堆未清洗小时数更关键。

## 点评
把“solo 爬取 + 纯度分类”做成可复现流水线，直接打标签噪声。强在检测准确率与下游 SDR 闭环；弱在依赖 YouTube 许可与版权、不含人声、阈值权衡会牺牲规模。


# Leveraging Discriminative Capabilities of Self-Supervised Neural Audio Fingerprinting for Efficient Speech Data Annotation

- 论文编号：1436
- 报告人：Kemal Altwlkany
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/altwlkany26_interspeech.pdf

## 问题
行业语音（如语音信箱）需内部标注、不可众包，重复样本浪费昂贵标注时间；若只能标子集，随机抽样会偏向高频重复条。

## 方法
用仅在音乐上训练的预训练 Conformer 神经指纹（PTC）做：(1) 去重；(2) 在嵌入空间 farthest-point sampling 选多样子集。在 Infobip 5 万语音信箱与公开 robocalls 上去重；用 VCTK 合成增强副本验证；线性探针比较 PTC 与 WavLM 对性别/口音/说话人区分。

## 实验与结果
语音信箱中 24,983/50,000 为重复，可标量减半；robocalls 近重复约 64.8%。合成集上 PTC 检出唯一数略偏高（2158 vs 2000）。探针：说话人 F1 PTC 96.36 vs WavLM 82.28（大效应）；性别两者均高；口音 WavLM 略优。FPS 相对随机抽样在嵌入空间更分散。

## 结论
音乐指纹嵌入可迁移到语音去重与多样性子采样，帮助隐私受限场景把有限标注时间花在不重复、更分散的样本上。

## 点评
把工业重复分布与指纹检索对接，实用性强。强在真实重复率与探针量化；弱在指纹非为语音任务训练、口音上不如 WavLM，且去重阈值需业务侧复核假阳。


# Cognitive-Heuristic Guided Multimodal Data Augmentation for Alzheimer’s Disease Detection Using LLM and TTS

- 论文编号：1724
- 报告人：Cheng Gong
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26e_interspeech.pdf

## 问题
基于语音的阿尔茨海默病（AD）检测数据稀缺；常见文本/语音增广缺少认知相关约束，难以保持语言–声学一致的 AD 行为模式。

## 方法
从真实数据提取认知属性向量（流畅度填料、MATTR 词汇复杂度、停顿比/语速）；双源 RAG（临床知识+患者范例）约束 LLM 生成带 `<pause>`/`filler` 的脚本；CosyVoice2 属性引导 TTS 同步实现停顿与犹豫。在 ADReSSo 上以约 1:1 增广训练 ERNIE、MM-AD、CogniAlign 等，并对比传统文本/声学扰动与 VC/TTS。

## 实验与结果
多模态检测：CogniAlign Acc 0.789→0.831，MM-AD 0.732→0.803，ERNIE 平均指标亦升。文本侧相对删除/回译/GPT-2，认知约束文本 Acc 0.857 最优。作者报告认知驱动增广稳定提升检测表现；另有尺度敏感性实验（正文后续表）。

## 结论
以认知启发式锚定多模态生成，可合成更贴近 AD 语言–声学共变的训练样本并提升检测；样本已公开演示。

## 点评
把“填料–停顿–词汇贫乏”写成可检索约束再驱动 TTS，比盲目扰动更贴任务。强在跨模型一致增益与文本消融；弱在合成分布仍依赖有限真实种子、临床外推与幻觉风险需人工把关。

