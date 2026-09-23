# Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：10
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本特邀专场把太平洋原住民语言的语音科学、文档化与技术适配放在同一议程。技术侧关注低资源基础模型持续适配中的表征漂移与可塑性—稳定性两难、大规模语种识别拓扑中浮现的“太平洋宏观簇”，以及马克萨斯语等真实转写数据上的微调、跨波利尼西亚迁移与“ASR 是否真正节省文档化时间”的人因实验。语言科学侧则用感知—声学—标注三角测量可接受发音范围，并报告法属波利尼西亚多种语言塞音 VOT、毛利语塞—元音协同发音等基线描写。

社区治理与合作治理同样是主线：巴布亚新几内亚 Hula 社区自建众包平台 Vavanagi、毛利语 TTS 的机构—企业合作案例，以及首个毛利语情感语音库 Pā-Kakare（16 类社区定义情感）。另有工作半自动采集库克群岛毛利语语速的社会语音学变异。整体上，本场强调技术必须与社区治理、文化相关评测与扎实语音描写同步推进，而非单向“低资源微调”。

## 技术内容

### 低资源适配、规模化表征与文档化 ASR

**Continual Adaptation for Pacific Indigenous Speech Recognition**（论文 2215；Ting Dang）在真实太平洋数据上实证研究数据量、适配策略与表征漂移；分析序贯语言习得的持续学习框架。摘要指出适配语言距离较远的太平洋原住民语言会诱发严重内部表征漂移，模型面临严格的可塑性—稳定性两难，并讨论 LoRA 等策略表现。

**Scaling Self-Supervised Speech Models Uncovers Deep Linguistic Relationships: Evidence from the Pacific Cluster**（论文 3205；Minu Kim）将基于 S3M 的语种识别从 126 扩展到 4,017 种语言，发现约 1K 规模前系统发育恢复平坦、4K 模型出现质变，并浮现把谱系无关的巴布亚、大洋洲与澳大利亚语言聚在一起的太平洋宏观簇，归因于捕获共享结构的集中编码。

**Speech Recognition to Accelerate Documentation of Marquesan and Cook Islands Māori**（论文 3276；Rolando Coto-Solano）基于约 17 小时马克萨斯语自然口语转写做三类实验：多语基础模型单语微调（Wav2Vec2 中位 CER=16、WER=30）、与库克群岛毛利语的迁移/联合训练，以及人工从 ASR 草稿校正是否节省时间（约 0.7× 等相关结果见摘要）。

**Automating Sociophonetic Research in Under-Resourced Languages: A Case Study of Speech Rate in Cook Islands Māori**（论文 3507；Rolando Coto-Solano）结合田野与在线数据，用识别计算约 60 名说话人、共 7.5 小时音频的语速（mora/秒）；面部自动年龄估计效果不佳需人工。摘要报告部分岛屿（如 Nga Pū Toru）年轻说话人语速显著更快。

### 发音描写、可接受范围与协同发音

**Mapping Acceptable Pronunciation Range for te reo Māori through Perceptual, Acoustic, and Marker Evaluative Data**（论文 1561；Catherine I Watson）以声学测量、语音学家转写与流利说话人评价三角测量毛利语元音可接受变异范围；在 /a u/ 与 /ai ae au/ 上发现可接受为单元音的变体在双元音中受罚，挑战“双元音仅为元音拼接”的常见看法。

**Oral stop realisation in three French Polynesian languages**（论文 899；Janet Fletcher）考察塔希提、马克萨斯（北/南）与 Rurutu 的 VOT 与清塞音实现；摘要称三者均为清音短滞后，平均 VOT 约 20 ms，并报告部位与后接元音对 VOT、闭塞时长等的影响模式。

**A preliminary exploration of stop-vowel coarticulation in Māori**（论文 1456；Isabella Shields）基于 7 名流利女性朗读语料中 524 个重读元音 token，用 GAMM 分析 F1/F2，显示 /p t k/ 语境对共振峰有显著影响，提示塞音协同发音改变元音质量。

### 社区平台、合作治理与情感资源

**Vavanagi: a Community-run Platform for Documentation of the Hula Language in Papua New Guinea**（论文 815；Bri Olewale）介绍社区运营的 Hula 文档平台，支持众包英—Hula 翻译与录音及长者审核；摘要称 77 名译者、4 名审稿人产出逾 1.2 万平行句对、约 9k 独特 Hula 词，并自定位为同类规模语言中首个社区主导语言技术倡议（Level 5）。

**Working Together on Technologies: A Case Study of Collaboration in Aotearoa**（论文 1573；Ben Hutchinson）以 Te Taura Whiri i te Reo Māori 与 Google 合作 TTS 为案例，聚焦伙伴关系中的相互理解与对齐挑战，而非技术实现细节。

**Pā‑Kakare: The First Emotional Speech Database for Te Reo Māori**（论文 1543；Himashi Rathnayake）发布首个毛利语情感语音库，采用社区研究确定的 16 类情感；含 4 名专业演员 3,840 条高质量录音（每情感 15 句），并报告 F0、强度与语速跨情感类别的系统差异。

## 本场要点

- 太平洋低资源适配凸显表征漂移与持续学习中的稳定性—可塑性冲突。
- 超大规模语种识别拓扑中出现跨谱系的“太平洋宏观簇”。
- 文档化 ASR 需同时报告 CER/WER 与人工校正是否真正省时。
- 语音科学补齐可接受发音范围、VOT 与塞—元音协同发音等描写空白。
- 社区自建平台与机构—企业合作案例强调治理与文化对齐。
- Pā-Kakare 等资源按社区情感范畴而非假定普世情绪类别构建。

## 覆盖核对

| paper_id | title |
|---|---|
| 2215 | Continual Adaptation for Pacific Indigenous Speech Recognition |
| 3205 | Scaling Self-Supervised Speech Models Uncovers Deep Linguistic Relationships: Evidence from the Pacific Cluster |
| 3276 | Speech Recognition to Accelerate Documentation of Marquesan and Cook Islands Māori |
| 1561 | Mapping Acceptable Pronunciation Range for te reo Māori through Perceptual, Acoustic, and Marker Evaluative Data |
| 899 | Oral stop realisation in three French Polynesian languages |
| 1456 | A preliminary exploration of stop-vowel coarticulation in Māori |
| 815 | Vavanagi: a Community-run Platform for Documentation of the Hula Language in Papua New Guinea |
| 1573 | Working Together on Technologies: A Case Study of Collaboration in Aotearoa |
| 1543 | Pā‑Kakare: The First Emotional Speech Database for Te Reo Māori |
| 3507 | Automating Sociophonetic Research in Under-Resourced Languages: A Case Study of Speech Rate in Cook Islands Māori |
