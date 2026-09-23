# Safeguarding Synthetic Speech: Ethical, technical and legal perspectives

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Special Session；Area：14；论文数：5
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本特刊把合成语音治理拆成技术溯源、语言数字保存、同意机制、数据集审计与法规术语对齐。检测侧从二分类走向开集少样本来源归属；同时低资源非洲语言 TTS 提醒：合成能力扩展与保护义务并行。

伦理法律侧批判一次性合同授权无法覆盖作为身份标记的声音；动态同意被提出为更合适的治理模板。数据集审计则显示公平性评估因缺人口统计元数据而基本不可行，且 bona fide 源语料高度重叠会夸大跨集泛化。

政策论文进一步指出：把图像/视频类比套到语音会失效，尤其忽视可独立开发、事后复用的说话人嵌入与复杂工作流。整体趋势是技术对策必须与同意、数据与法律定义同步修订。

## 技术内容

### 检测溯源与低资源合成

**Who Synthesized This? Joint Deepfake Detection and Generative Source Attribution**（论文 2442；Vishal Kumar）少样本开集框架，按 MLAAD v9 推出年份与架构族划分做时间评测；WavLM-Large + LoRA，层次度量学习。未见 2025+ 模型族用仅 12 样本建原型；ASVspoof 5.0 报告 0.49% EER、0.09 minDCF，来源追溯准确率 99%。

**Towards Digital Preservation of Efik: TTS for a Low-Resource African Language**（论文 1868；Offiong Bassey Edet）首个记录在案的 Efik 端到端 TTS 研究：2632 句约三小时单说话人语料，比较 VITS、MMS-TTS、SpeechT5、Orpheus-TTS。母语者评价中 MMS-TTS MOS 最高（3.80±0.63），长语音更稳但仍有声调错误。

### 同意、数据审计与法规语言

**Rethinking Consent Acquisition for Voice Synthesis: from Static to Dynamic Consent**（论文 2379；Matilde Nanni）论证声音兼具数据与身份标记，一次性授权无法充分规制后续使用与身份伤害；检讨一般与特定两类合同同意均难满足知情同意，主张借鉴生物伦理的动态同意。

**Ethical and Technical Limits of Deepfake Speech Datasets**（论文 124；Vojtěch Staněk）审计 39 个 deepfake 语音数据集的可及性、文档、人口/语言覆盖、规模与 bona fide 来源。结论：多数缺人口元数据使公平评估不可行；源语料重叠削弱跨集评价可信度。

**AI Regulation and the Technical Language of Speech Synthesis**（论文 210；Jennifer Williams）追踪 TTS、声转换、说话人验证与识别的汇合，指出现行侧重输出的政策可能遗漏可移植模型与说话人嵌入等工作流组件，导致法律责任界定与技术事实错位。

## 本场要点

- 联合检测与来源归属、时间划分评测，应对合成模型快速迭代。
- Efik TTS 基线显示低资源声调语言仍需更大语料与声调感知建模。
- 静态合同同意不足以治理不可去标识的声音身份；动态同意是备选治理方案。
- 数据集缺人口元数据与源重叠，分别阻断公平评估与夸大泛化。
- 法规用语需覆盖嵌入与复杂工作流，而非仅合成波形输出。

## 覆盖核对

| id | title |
|---|---|
| 2442 | Who Synthesized This? Joint Deepfake Detection and Generative Source Attribution |
| 1868 | Towards Digital Preservation of Efik: TTS for a Low-Resource African Language |
| 2379 | Rethinking Consent Acquisition for Voice Synthesis: from Static to Dynamic Consent |
| 124 | Ethical and Technical Limits of Deepfake Speech Datasets |
| 210 | AI Regulation and the Technical Language of Speech Synthesis |
