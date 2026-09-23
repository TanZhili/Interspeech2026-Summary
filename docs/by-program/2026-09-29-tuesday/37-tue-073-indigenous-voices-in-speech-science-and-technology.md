# Indigenous Voices in Speech Science and Technology

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Special Session；Area：14；论文数：7
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本特刊把原住民与少数语言语音技术同时放在算法、数据治理与用户体验三条线上。南部班图语声调条件课程学习、Warlpiri 跨语相似度迁移、北萨米半监督伪标签、普什图语 Common Voice，展示低资源 ASR/语料建设的技术路径。

与此同时，ELSI 平台与毛利语 TTS 强调社群主导的数据策展与治理；澳大利亚原住民英语使用者访谈揭示 ASR 迫使使用者“说得像白人”。趋势是：没有社群控制与语言正义，单纯刷低 WER 不足以称为成功的原住民语音科技。

## 技术内容

### 低资源 ASR、迁移与语料

**Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition**（论文 2905；Vukosi Marivate）面向 6 种南部班图语，结合混合难度、声调统计门控适配器与分阶段课程；社区语料训练并测 NCHLT 迁移。W2V-BERT 与 Whisper 在 Nguni / Sotho-Tswana 上互有优势；声调条件 W2V-BERT 跨数据集平均 WER 28.41%，Xitsonga 迁移 23.79%。

**Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR**（论文 1837；Pravina Mylvaganam）融合预训练声学相似度与类型学/音素库/语法相似度排序源语言。Whisper 上阿萨姆语、印地语显著降低 WER/CER；声学相似度最强预测微调表现，音素库与类型学更好解释零样本。

**Two-stage semi-supervised learning with pseudo-labels: A case study on Northern Sámi ASR**（论文 2497；Priyanshi Pal）比较全量教师伪标签与基于 WER 的多教师一致性子集。更大教师可相对改进小模型域外 CER 3.8–33.3%；同等数据量下伪标签收益可媲美人标；人标+伪标时两阶段微调优于单步混合。

**Pashto Common Voice: Building the First Open Speech Corpus for a 60-Million-Speaker Low-Resource Language**（论文 1432；Hanif Rahman）社区建设使语料从 1.5 小时/5 贡献者增至 147 小时/1483 说话人。MCV23 含 107,781 片段（60,337 已验证；82.33 验证小时）。Whisper Base 在 MCV20 微调后测试 WER 13.4%，相对零样本 99.0%。

### 治理、社群主导合成与用户体验

**From Academic Tool to Community Infrastructure: A Call for Indigenous Partnership in Speech Data Governance**（论文 2489；Kaveri K. Sheth）介绍 ELSI 平台管理含 10 个原住民社群的儿童中心音频；指出托管权集中于欧洲学术方，对照 CARE/OCAP 发出共同设计社群托管与强制访问控制的呼吁。

**Indigenising Speech Technology: Building a TTS Model for te Reo Māori**（论文 1443；Gianna Leoni）原住民主导的毛利语 TTS，聚焦数据策展、采集与质控决策；主张对原住民/濒危/少数语言而言，细致质控可优于“数据越多越好”的默认假设。

**‘I have to talk proper white ways’: Australian Aboriginal English Speakers’ Experiences with Voice Technologies**（论文 1595；Celeste Rodríguez Louro）原住民主导深度访谈：使用者报告 ASR 对非原住民更友好，并感到需切换为“白人说法”以获更好识别，揭示技术交互中的语言顺从压力。

## 本场要点

- 班图语声调课程与 Warlpiri 相似度排序，说明语言结构信息可指导模型与源语选择。
- 北萨米伪标签与普什图语 Common Voice，展示半监督与社区众包两条扩展路径。
- ELSI 与 CARE/OCAP 对齐要求把托管权交还社群，而非仅学术开放科学。
- 毛利语 TTS 以质控策展反驳单纯堆数据逻辑。
- 澳大利亚原住民英语使用者体验暴露 ASR 的结构性排斥与“说白”压力。

## 覆盖核对

| id | title |
|---|---|
| 2905 | Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition |
| 1837 | Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR |
| 2489 | From Academic Tool to Community Infrastructure: A Call for Indigenous Partnership in Speech Data Governance |
| 1443 | Indigenising Speech Technology: Building a TTS Model for te Reo Māori |
| 1595 | ‘I have to talk proper white ways’: Australian Aboriginal English Speakers’ Experiences with Voice Technologies |
| 2497 | Two-stage semi-supervised learning with pseudo-labels: A case study on Northern Sámi ASR |
| 1432 | Pashto Common Voice: Building the First Open Speech Corpus for a 60-Million-Speaker Low-Resource Language |
