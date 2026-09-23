# Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Oral
- **Area**：12
- **论文数**：6
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场聚焦音频/语音语言模型（LALM / SpeechLLM / SpeechLM）的评测可信度、表征选择与新兴能力边界。评测侧不再满足于“单一准确率”，而是暴露选择题顺序、改写与语言提示对分数的扰动，以及发声类型（phonation）等副语言线索如何改变模型行为与社会偏见表现。

能力侧出现面向工具调用的大规模语音基准，以及在噪声 ASR 条件下用教师引导对抗去噪稳住口语理解语义流形。表征争论则系统比较连续特征与离散 token 在语音、声音与音乐上的取舍，强调语义约束与骨干缩放无法弥补表征信息损失。

低资源设定下的多语言多任务 SpeechLLM 则检验：从 ASR 预训练投影器启动、仅用每任务每语言少量标注数据时，跨语言迁移与零样本任务泛化各自能走多远。整体趋势是：评测协议更严格、任务从理解扩展到行动（tool use），表征与数据效率成为部署前的核心设计问题。

## 技术内容

### 评测稳健性与副语言敏感度

**Robustness Assessment of Large Audio Language Models in Multiple-choice Evaluation**（论文 2503；Fernando López）  
指出 LALM 多用 MCQA 评测，但选项顺序微调会显著改变结果，且文本题干与选项含语言提示，模型可不依赖音频作答。在 MMAU、MMAR、MMSU 与四种模型上系统研究，发现语言偏差普遍存在，并对选项顺序与题干/选项改写敏感。提出更简单的评测协议与度量，以更细致评估 MCQA 框架下的 LALM。

**Lost in Phonation: Voice Quality Variation as an Evaluation Dimension for Speech Foundation Models**（论文 736；Harm Lameris）  
Speech Foundation Model 可直接处理原始音频并对副语言变化作响应，但其如何解释非词汇线索仍少研究。引入 VQ-Bench：含模态、气声、嘎裂与句末嘎裂等平行合成发声类型的受控评测套件，在四个生态有效域的开放生成与情感识别上评估。摘要称不同模型在发声条件下的代理性、共情与领导力判断出现系统性偏移，并出现薪资与领导背书上的性别不对称。

### 工具调用、噪声 SLU 与表征范式

**Audio2Tool: Speak, Call, Act - A Dataset for Benchmarking Speech Tool Use**（论文 2857；Ramit Pahwa）  
现有基准在领域广度、声学多样性与组合推理复杂度上不足。Audio2Tool 含约 30,000 条查询，覆盖智能车、智能家居与可穿戴三大域，并设从直接命令到多意图与“大海捞针”的多层复杂度；用零样本音色克隆 TTS 与多样噪声模拟野外条件。摘要称 SOTA SpeechLM 与 ASR-LLM 管线在简单命令上表现强，在组合与声学挑战下显著下降。

**ML-KD-DRI-GAN: Teacher-Guided Denoising and Triplet-Adversarial Training for Robust Spoken Language Understanding**（论文 670；Ankit Kumar）  
ASR 错误扭曲语义表征并损害 SLU。提出 ML-KD-DRI-GAN：教师在干净转写上训练，学生通过对抗去噪把噪声嵌入映射到干净语义流形，含生成器多层潜在对齐与判别器 Bi-DCD 知识蒸馏，并用合成生成器产生难负样本做三元组分离。摘要称在噪声 SLU 基准上相对 GAN-BERT 有一致增益，并在 SLURP 上给出中重度 ASR 噪声下的绝对提升数值。

**Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs**（论文 2074；Jing Peng）  
LALM 使用连续特征或离散 token，一般音频理解的最优表征仍有争议。用 UniARC 在 speech/sound/music 上系统比较，覆盖 SmolLM2-135M 至 Llama-3-8B，并分析数据量、模型容量与计算效率关系。摘要称 tokenization 中的语义约束对理解至关重要，且放大骨干无法补偿音频表征信息损失（尤其数据有限任务）。

### 低资源多语言多任务

**Towards Enabling Multilingual Multitask SpeechLLMs in Data-Scarce Settings**（论文 1229；Seraphina Fong）  
多语言与多任务常被分开研究或依赖大语料。在低资源条件下把 SpeechLLM 扩展到 ASR 之外的语音翻译与主题分类；每任务每语言仅用 3–5 小时标注数据，检验从 ASR 预训练投影器启动是否支持有效多任务适配。摘要称跨语言表现受语言相似度影响，且零样本不扩展到未见任务；ASR 预训练 bootstrapping 加有限目标语微调可支撑低资源多语言多任务。

## 本场要点

- MCQA 分数对选项顺序、改写与文本提示敏感，需更稳健的 LALM 评测协议。
- 发声类型可作为副语言评测维度，暴露模型社会偏见与行为偏移。
- Audio2Tool 将 SpeechLM 评测推向多域工具调用与组合/噪声压力测试。
- 教师引导对抗去噪与三元组分离用于缓解 ASR 噪声对 SLU 的损害。
- 连续 vs 离散表征比较强调语义约束，骨干缩放难补表征信息损失。
- 低资源多语言多任务依赖 ASR 预训练启动，跨任务零样本仍受限。

## 覆盖核对

| id | title |
|---|---|
| 2503 | Robustness Assessment of Large Audio Language Models in Multiple-choice Evaluation |
| 736 | Lost in Phonation: Voice Quality Variation as an Evaluation Dimension for Speech Foundation Models |
| 2857 | Audio2Tool: Speak, Call, Act - A Dataset for Benchmarking Speech Tool Use |
| 670 | ML-KD-DRI-GAN: Teacher-Guided Denoising and Triplet-Adversarial Training for Robust Spoken Language Understanding |
| 2074 | Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs |
| 1229 | Towards Enabling Multilingual Multitask SpeechLLMs in Data-Scarce Settings |
