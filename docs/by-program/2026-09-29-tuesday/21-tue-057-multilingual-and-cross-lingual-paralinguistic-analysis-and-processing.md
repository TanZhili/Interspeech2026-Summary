# Multilingual and Cross-Lingual Paralinguistic Analysis and Processing

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：3
- 论文数：6
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场追问副语言任务究竟多“语言无关”。零样本跨语情感识别用监督对比学习做跨语情感对齐，并用说话人对抗抑制说话人线索；系统性工具 Cross-Lingual Transfer Matrix（CLTM）在性别识别与说话人验证上量化供体—受体语言对的迁移结构。合成增强方面，八种声线克隆模型在五项副语言（含临床）任务上多数能保留信号，并把英语临床语音克隆到日语后优于原始跨语迁移。

与人类对比，英语单语听者与英语单语 SLM 在法/日/希/泰基本情感上均显著高于随机，支持普遍性，但人类更擅负面情绪、模型更偏快乐/惊讶。说话人嵌入的跨语泛化在粤—英双语材料上与人类评分及声学结构对照；魅力韵律在卢森堡语—法语双语政治家演讲中，说话人身份解释大部分方差，语言仍带来系统但较小的差异。整体趋势是：用矩阵化评测、对抗/对比学习与克隆增强，把“副语言可跨语”从口号变为可度量、可增强的性质。

## 技术内容

### 跨语情感、迁移矩阵与声线克隆增强

**Learning Emotion-discriminative Representations for Zero-Shot Cross-Lingual Speech Emotion Recognition**（论文 1170；Jinyi Mi）结合监督对比学习与说话人对抗学习，分别促进跨语情感对齐与说话人不变表示；在零样本跨语 SER 设定下相对仅源语训练的基线改善泛化（具体分数以官方摘要为准）。

**Quantifying Cross-Lingual Transfer in Paralinguistic Speech Tasks**（论文 2745；Federico Costa）提出 CLTM，系统量化给定任务内语言对之间的跨语交互；应用于性别识别与说话人验证，并基于多语 HuBERT 编码器分析供体语言效应。

**Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning**（论文 2993；Roseline Polle）在五项副语言任务、公开与临床数据上评测八种声线克隆模型，多数保留信号且退化有限；将英语临床语音克隆为日语后，基于克隆数据训练优于原始跨语迁移。

### 普遍性、说话人嵌入与魅力韵律的语言/说话人方差

**Universality of Speech Emotion Recognition in Humans and Speech Language Models**（论文 3061；Yuka Tatsumi）比较 101 名英语单语听者与两个英语单语 SLM，在法、日、希、泰基本情感上的跨语识别；双方均显著高于随机，但人类对负面情绪更准且倾向中性默认，模型在快乐与惊讶上更优并倾向相应默认。

**Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations**（论文 858；Tianze Xu）在粤—英双语 within/cross-language 条件下，从 18 个 SOTA 模型导出相似度，与人类评分及声学特征做线性混合模型与表征相似度分析；嵌入跨语泛化大体平行人类行为，并依赖 largely shared 的声学基础。

**Speaker or Language? Explaining Variance in Charismatic Prosody Across Luxembourgish and French**（论文 26；Nina Hosseini-Kivanani）分析 10 名政治家在高度可比情境下用卢森堡语与法语演讲的 400 条话语、41 维魅力相关韵律特征；混合效应模型显示说话人身份解释大部分方差，语言解释较少但系统：法语更高 shimmer 与句末 F0，卢森堡语中频谱能量更强等。

## 本场要点

- 零样本跨语 SER 依赖情感对齐与说话人不变约束。
- CLTM 把副语言跨语迁移变成可比较的任务级矩阵。
- 声线克隆可作为临床等标注昂贵任务的跨语增强，且需用下游任务而非仅 WER/相似度验收。
- 人类与 SLM 均显示情感识别普遍性，但情绪类别偏好不同。
- 说话人嵌入跨语泛化与人类感知大体同向。
- 双语魅力韵律中说话人方差主导、语言效应次之但仍系统。

## 覆盖核对

| paper_id | title |
|---|---|
| 1170 | Learning Emotion-discriminative Representations for Zero-Shot Cross-Lingual Speech Emotion Recognition |
| 2745 | Quantifying Cross-Lingual Transfer in Paralinguistic Speech Tasks |
| 2993 | Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning |
| 3061 | Universality of Speech Emotion Recognition in Humans and Speech Language Models |
| 858 | Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations |
| 26 | Speaker or Language? Explaining Variance in Charismatic Prosody Across Luxembourgish and French |
