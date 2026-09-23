# Multilingual, Cross-lingual & Low-Resource ASR

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：8
- 论文数：11
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场围绕多语/低资源 ASR 的表征对齐、参数高效迁移与领域数据稀缺展开。一类工作在 Speech LLM / 多语 SSL 之上设计渐进或对齐感知的继续预训练，避免过早把各语言压入共享空间或把声—符对齐全部推到微调阶段；另一类用 LoRA/MoE-LoRA、供体语言选择与双层优化，在冻结主干前提下实现跨语适配。领域场景覆盖空管、中亚长尾语言、拉脱维亚医学听写、达罗毗荼语族、非正式波斯语、希腊歌词转写与声调语强制对齐。

数据侧手段包括声学属性仿真与口音可控合成、聚类级预训平衡与域感知采样、LLM 驱动的格式化整理与伪标校正，以及非正式语体新建语料。模型诊断则指向 Whisper 解码器自注意力与交叉注意力失衡、词长与词表稀疏导致的替换错误等。整体趋势是：对齐与路由成为多语 SLM/ASR 的核心工程点，合成与 LLM 后处理成为低资源领域的常规补数策略。

## 技术内容

### 多语表征对齐与 Speech LLM / SSL 继续预训练

**PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs**（论文 1734；Pei Zhang）提出多阶段多任务的 Progressive Alignment Representation Training，训练中逐步解冻 SLM 参数并分阶段引入不同多语任务，以细粒度对齐多语言、多任务的语音—文本表示，缓解冻结 LLM、仅训编码器导致的语言表示坍缩。

**Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning**（论文 1185；Xuyang Wang）在多语 SSL 之上增加中间阶段，联合优化 SSL 与 CTC，使表征学习受文本对齐约束；并分析对齐阶段不同建模单元对 ASR 的影响，引入语言感知双码本量化器。

**BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR**（论文 2771；Xiaodong Cui）将预训练 ASR 编码器经可训桥接对齐到 LLM token 空间，解码器侧用 MoE-LoRA 与路由器做语言特化；训练表述为双层规划，并用单环、无值函数惩罚求解器高效优化。

### 低资源语言、语体与跨语 LoRA 迁移

**GigaAM Multilingual: Foundation Model for Underrepresented Languages**（论文 2483；Andrei Kuzmenko）面向中亚代表性不足语言（哈萨克、吉尔吉斯、乌兹别克），以 HuBERT 风格目标在约 200 万小时音频上预训练 Conformer；预训用聚类级数据平衡、微调用域感知采样，并在受控对比中相对 Whisper Large v3、Omnilingual-1B 等在目标语尤其是自发语音上报告增益。

**Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR**（论文 1133；Spandan Dey）用供体语言 LoRA 初始化低资源受体适配，并提出先按谱系过滤、再按正字法—分布相似性选最优供体的两阶段策略；摘要称供体知情初始化持续优于仅受体适配。

**Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages**（论文 1007；Kumud Tripathi）分析达罗毗荼语相对印欧语更高 WER 与词长/词表稀疏、字符级替换等因素，并指出微调后解码器自注意力与交叉注意力失衡；提出 Weighted-Attention（自适应平衡注意力来源）与 Self-Conditioning（回注中间预测以提升 token 一致性），摘要称在低资源与黏着语上持续降低 WER。

**The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation**（论文 2454；Hadi Alizadeh）发布 Toorintan-Persian Informal Dataset，经针对性规范化后微调模型；摘要称在非正式数据上训练的模型可跨正式/非正式语体泛化，并在 WER 与 BLEU 上优于既有基线。

### 领域稀缺数据、歌词转写与声调语对齐

**Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition**（论文 2422；Zhe Zhang）为空管场景构建含 TTS、声线转换、L2→L1 与可控 L1→L2 口音转换等的合成管线，以缓解信道噪声、非母语口音与数据稀缺；在 ATCO2 上对 Whisper 微调的实验表明该合成数据有助于提升识别。

**Low-Resource Medical ASR for Rich Transcription in Latvian**（论文 3469；Arturs Znotins）比较端到端直接生成格式化报告与“逐字转写 + LLM 后编辑”两阶段管线；用 LLM 将遗留逐字稿转为格式化数据，并加入约 75 小时 LLM 校正伪标，叠加 50 小时人工医学听写，报告在 WER、标点与医学实体识别上显著改善。

**Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation**（论文 1371；Dimitrios Damianos）首次系统研究希腊语自动歌词转写上的 Whisper 适配，考察缩放、转写—翻译多任务比例与两阶段语到唱适配，并基于 Greek Audio Dataset 经源分离与 CTC 强制对齐构建片段级语料；摘要称缩放持续受益，多任务对较小容量模型主要起正则作用。

**CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages**（论文 1770；Hongchen Wu）在跨语强制对齐中引入自动声调映射的 tone encoding，在六种类型多样的声调语言上，报告与人工专家映射相当，并匹配或优于语言特定声学模型表现（摘要所述对比范围）。

## 本场要点

- 多语 SLM/SSL 强调渐进解冻与对齐感知继续预训练，避免表示坍缩与对齐滞后。
- LoRA/MoE-LoRA、供体选择与双层优化成为参数高效跨语适配工具。
- 合成数据、口音转换与 LLM 格式化/伪标是空管、医学等低资源领域的关键补数手段。
- 非正式语体、达罗毗荼语解码器失衡、希腊歌词与声调语对齐构成具体语言挑战样本。
- GigaAM 等基础模型用数据平衡策略对抗头语言主导。
- 所有具体小时数、准确率等仅转述摘要，未外推。

## 覆盖核对

| paper_id | title |
|---|---|
| 1734 | PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs |
| 1185 | Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning |
| 2422 | Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition |
| 2483 | GigaAM Multilingual: Foundation Model for Underrepresented Languages |
| 3469 | Low-Resource Medical ASR for Rich Transcription in Latvian |
| 1133 | Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR |
| 1007 | Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages |
| 2454 | The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation |
| 2771 | BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR |
| 1371 | Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation |
| 1770 | CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages |
