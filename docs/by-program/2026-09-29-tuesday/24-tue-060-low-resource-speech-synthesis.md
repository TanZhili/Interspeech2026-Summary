# Low-Resource Speech Synthesis

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：7
- 论文数：5
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场由一篇综述性邀请报告与四篇低资源 TTS 系统/资源工作组成。邀请报告梳理多语跨语迁移、无配对数据、无监督语音单元发现与基础模型如何把“大量转写语音”门槛大幅降低，并讨论真正低资源语言仍面临的语言多样性、合成质量与可靠评测问题。论文侧则覆盖印度语族轻量跨语说话人适配、曼尼普尔拉丁字母部落语言神经 TTS 资源、埃塞俄比亚阿姆哈拉语/阿凡奥罗莫语高质量 SpeechT5 系统，以及把英语 F5-TTS 基础模型适配 11 种印度语言的 IN-F5。

方法共性包括：极短参考（如 10 秒）适配、合成数据质控再微调、音素/字符统一标签集跨语共享音色，以及“从零训练 vs 直接微调 vs 持续高资源暴露”的受控比较。IN-F5 摘要明确挑战“多语系统必须持续暴露高资源数据”的假设。整体上，低资源 TTS 已从“有没有系统”转向“适配策略、数据质控与评测是否可靠”。

## 技术内容

### 邀请报告与印度语族轻量/基础模型适配

**Low-Resource Speech Synthesis: What Have We Solved, and What Remains?**（论文 id 未提供；Sakriani Sakti）邀请报告综述低资源语音合成进展：多语跨语迁移、无配对学习、无监督单元发现与基础模型使数百乃至上千种语言在目标语极少甚至无转写时亦可合成；并讨论真正低资源场景下语言多样性、质量与可靠评测仍待解决。

**Lightweight Cross-Lingual Speaker Adaptation for Indic TTS**（论文 2050；Tarun Kumar）用约 10 秒参考样本，经声线克隆生成、四阶段质控过滤后微调带双位点说话人条件与余弦一致性损失的 FastSpeech2；经 Common Label Set 音素统一，适配音色可跨印地、马拉地、泰米尔、泰卢固合成而无需额外录音。

**IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis**（论文 3366；Praveen Srinivasa Varadhan）从英语预训练 F5-TTS 出发，用不到原预训数据规模约 2% 的数据适配 11 种印度语言；受控比较显示仅印度数据直接微调最优。摘要称 IN-F5 接近人类自然度与说话人相似度，并出现多语种音色迁移、语码转换等涌现能力。

### 区域语言资源与埃塞俄比亚高质量合成

**Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur**（论文 2304；Hoomexsun Pangsatabam）发布 Tangkhul（约 9.58 h）与 Maring（约 10.79 h）标准方言工作室朗读资源（教材、故事与圣经译本等）及自动切分规范化管线；训练 Tacotron 2 / FastSpeech 2 字符级单语系统，并以客观与主观指标评估，作为曼尼普尔拉丁字母低资源语言 TTS 起点。

**High-Quality Speech Synthesis for Under-Resourced Ethiopian Languages**（论文 2658；Rahel Mekonen Tamiru）基于 SpeechT5 为阿姆哈拉语与阿凡奥罗莫语构建系统：先建语音丰富文本语料并专业录音，合计约 200 小时（每语约 100 小时）；为处理阿姆哈拉语叠音与语境敏感发音另建专用数据并将训练扩展至约 113 小时。摘要报告主观 MOS 为阿姆哈拉语 4.65、阿凡奥罗莫语 4.43。

## 本场要点

- 邀请报告界定低资源 TTS“已解决/仍挑战”的边界，强调评测可靠性。
- 极短参考 + 合成质控 + 轻量声学模型是印度语族适配实用路径。
- 英语 TTS 基础模型可作印度多语先验；直接微调可优于持续英语暴露。
- 东北印度拉丁字母部落语言需要配套录音与预处理资源。
- 埃塞俄比亚两语种以大规模录音 + SpeechT5 达到高 MOS。
- 音素统一标签集支撑跨语共享音色而不增录。

## 覆盖核对

| paper_id | title |
|---|---|
| （空） | Low-Resource Speech Synthesis: What Have We Solved, and What Remains? |
| 2050 | Lightweight Cross-Lingual Speaker Adaptation for Indic TTS |
| 2304 | Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur |
| 2658 | High-Quality Speech Synthesis for Under-Resourced Ethiopian Languages |
| 3366 | IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis |
