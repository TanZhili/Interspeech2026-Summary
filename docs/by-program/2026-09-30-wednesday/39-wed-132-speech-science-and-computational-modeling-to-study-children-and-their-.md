# Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments

- 日期：2026年9月30日（周三）
- 时间：14:00-16:00
- 形式：Special Session
- Area：14
- 论文数：13
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。其中一篇条目摘要为空，仅能据题名说明。

## 技术趋势

本特刊/专题围绕儿童日常家庭与学前环境中的语音、交互与语言发展：从音素级发音筛查与跨语儿童音素识别，到底向上音节发现、说话人辨别发展，再到日长录音上的婴儿中心多层级标注、哭闹分级、说话人类型分类与儿童指向语检测。

方法上，自监督与 Whisper/HuBERT 类模型在儿童中心日长录音上预训练或微调成为主流；结构化说话人条件、上下文窗口与家庭偏移用于跨家庭泛化。同时强调真实噪声环境相对实验室数据的巨大域差，以及隐私驱动的基准与 ELSI 治理。

发展与社会语言学议题包括：学前遗产语输入输出量化、照料者—儿童韵律对齐的跨语 DTW 分析，以及面向成人/儿童多域统一 ASR 的熵感知 MoE Speech-LLM。

## 技术内容

### 儿童发音筛查、识别与发展轨迹

**Phoneme-Level Mispronunciation Screening in Polish-Speaking Children with an Explainable Assistant**（论文 1416；Milosz Dudek）  
面向波兰语儿童咝音替换的筛查流水线：wav2vec2 CTC 识别器 + 对齐错误分型 + 模板 grounding 的看护助手（筛查非诊断）。摘要称 10 名未见儿童、559 条话语上精确序列匹配 88.7%；以替换证据 token 为保守筛查代理时精确率 72.9%、召回 61.4%（F1=0.67），目标正确项误报率 2.7%。

**BabAR: from phoneme recognition to developmental measures of young children's speech production**（论文 1132；Marvin Lavechin）  
基于 TinyVox（多语超 50 万条儿童发声音标转写）训练跨语儿童音素识别 BabAR。摘要称在多语儿童中心日长录音上预训练显著更优，微调时提供约 20 秒周围音频上下文进一步提升；错误多落在宽语音学类别内，自动成熟度度量与文献发展估计一致。

**How does children's pronunciation develop? Capturing syllabic change with children's growth using unsupervised syllable discovery**（论文 3104；Koharu Horii）  
用无监督音节发现模型 Sylber 自下而上分析 5–15 岁 957 名儿童。摘要称呈现音节模式扩展（约 5–8 岁）后逐渐向成人样稳定的发展模式，能捕捉自上而下方法难见的细粒度变化。

**Talker Discrimination and Identification in 7-12-year-old Children: Effects of Talker Gender and Phonological Ability**（论文 3053；Rebecca Holt）  
在典型发展 7–12 岁儿童上检验说话人辨别与识别。摘要称男女说话人对准确率相近；辨别与识别中到强相关；语音工作记忆预测识别准确率，为临床群体后续研究提供范式验证。

### 日长录音理解、哭闹与说话人类型

**Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning**（论文 2746；Mark Hasegawa-Johnson）  
LoRA 微调 Whisper 编码器 + 目标说话人感知 Transformer，做多层级长上下文帧级预测；序列平滑损失与因式说话人 token（共享层级 token + 家庭偏移）用于时间连贯与跨家庭稳健。摘要面向家庭日长录音的婴儿中心音频标注。

**Advancing Infant Distress Detection: Two- and Three-Way Classification in Real-World Audio Environments**（论文 3234；Kaya de Barbaro）  
重标注真实世界语料，发布首个连续日长儿童佩戴音频上 cry/fuss/非窘迫标注集。摘要称最佳二分类 macro F1=0.803、三分类 0.624；实验室训练模型在真实条件下失败，而本文模型泛化更稳健。

**BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings**（论文 2772；Théo Charlot）  
在 40+ 语言约 13,000 小时儿童中心录音上训练自监督模型。摘要称语音类型分类 F1 在六个语料上为 55.0%–76.1%，并在瓦努阿图与所罗门群岛上相对 HuBERT 绝对提升 14.0 与 18.3 点。

**Context-aware child-directed speech detection from long-form recordings**（论文 2780；Théo Charlot）  
在 182 名儿童的多语数据上微调六种自监督模型，并引入周围上下文。摘要称域内儿童中心预训练显著优于成人语音模型；上下文带来平均 F1 绝对提升 13.8%；端到端流水线在自动分割下性能下降但仍优于规则基线。

**Benchmarking Adult Addressee Classification Across Child- and Adult- Directed Speech Datasets**（论文 2536；未提供）  
官方程序未提供摘要与报告人字段；仅能从题名判断其聚焦儿童指向语与成人指向语数据集上的成人受话人分类基准。

### 基准治理、遗产语输入与多域 ASR

**Deriving Benchmarking Datasets from Long-Form Recordings: Challenges and Opportunities**（论文 2363；Kaveri K. Sheth）  
提出覆盖 27 个儿童中心数据集标准化集合、四类语音处理基准可复现流水线，以及嵌入伦理治理的 ELSI 角色生态；并以语音类型分类案例说明三者相互依赖。

**Measuring English and Vietnamese language input and output in an Australian preschool – A longitudinal study**（论文 3213；Ha Chi Tran）  
量化墨尔本越南语暴露项目两次实施前八节课的英越输入输出时长。摘要称儿童总说话量增加、英语仍占主导，越南语儿童输出上升而引导者输入下降，并给出可迁移的量化方法学含义。

**Dynamic Time Warping Reveals Prosodic Alignment in Caregiver–Child Interactions across Languages**（论文 2356；Olivier Rüst）  
在英、日、俄语料上用 DTW 量化音高轮廓相似度与话轮时间邻近性、儿童年龄的关系。摘要称时间相邻话语音高轮廓更相似，且相似度随儿童年龄下降，与社交适应一致，并可能受文化与语言规范调节。

**Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR**（论文 877；Abeer Alwan）  
提出分类器域路由、Mixture-of-Projectors 与 Mixture-of-LoRAs，并以熵感知路由在边界引入共享专家。摘要称在公开儿童语料上相对基线一致提升且保持成人 ASR，并称是首个用 Speech-LLM 统一多域儿童与成人 ASR 的工作。

## 本场要点

- 儿童音素识别与筛查依赖大规模儿童专属数据与可解释、安全边界清晰的助手设计。
- 自下而上音节发现可揭示自上而下音素映射难捕捉的发展轨迹。
- 日长录音任务强调儿童中心预训练、上下文与家庭条件化，以及哭闹分级等真实世界标注。
- 基准建设需同时解决异构语料、跨语泛化评估与儿童隐私/伦理治理。
- 韵律对齐与遗产语输入输出测量把计算建模连接到发展与社会语言学问题。

## 覆盖核对

- 1416 | Phoneme-Level Mispronunciation Screening in Polish-Speaking Children with an Explainable Assistant
- 1132 | BabAR: from phoneme recognition to developmental measures of young children's speech production
- 3104 | How does children's pronunciation develop? Capturing syllabic change with children's growth using unsupervised syllable discovery
- 3053 | Talker Discrimination and Identification in 7-12-year-old Children: Effects of Talker Gender and Phonological Ability
- 2746 | Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning
- 3234 | Advancing Infant Distress Detection: Two- and Three-Way Classification in Real-World Audio Environments
- 2772 | BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings
- 2780 | Context-aware child-directed speech detection from long-form recordings
- 2536 | Benchmarking Adult Addressee Classification Across Child- and Adult- Directed Speech Datasets
- 2363 | Deriving Benchmarking Datasets from Long-Form Recordings: Challenges and Opportunities
- 3213 | Measuring English and Vietnamese language input and output in an Australian preschool – A longitudinal study
- 2356 | Dynamic Time Warping Reveals Prosodic Alignment in Caregiver–Child Interactions across Languages
- 877 | Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR
