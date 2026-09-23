# Corpus Creation, Summerisation and Understanding

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Oral
- **Area**：12
- **论文数**：6
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场把“语料如何建、摘要如何做、理解如何可比可复现”连成一条数据—评测—应用链。长会议文档摘要强调在多段候选组合中用树搜索与自奖励做免训练选择，以缓解多阶段管线误差累积与参考摘要质量差的问题。统一实验框架则针对后处理不一致导致的评测不可比，以及跨数据规模/管线的训练难复现。

低资源场景同时覆盖跨语言文本/语音摘要、语言文献记录中的 ASR 冷启动优先级、以及人机协作会话语料构建与质控角色分工。另一条线用 IPA 引导的双转录做数据中心式语料精炼，把口语—书面对齐锚定在语音实现上，以服务文本规范化与领域 ASR。

趋势可概括为：摘要从黑盒端到端转向可组合、可搜索；语料工程强调可及工作流、阈值门控人机验证与语音学约束的规范化；评测与训练协议统一成为“选型可部署”的前提。

## 技术内容

### 长文档摘要与统一理解评测

**Segment-level Tree Search for Long Meeting Document Summarization**（论文 3011；Sangwon Ryu）  
会议文档长且会话结构复杂；多阶段先抽取再摘要易累积误差且缺中间校验。提出免训练框架 S3：将长文档分段、每段生成多个摘要候选形成搜索树节点，用自奖励引导的蒙特卡洛树搜索选最佳组合并精炼为最终摘要。摘要称即使用 7B 模型，也可达到与更大 72B 模型可比的效果，并产出长度合适的摘要。

**A Unified and Reproducible Experimentation Framework for Speech Understanding**（论文 1225；Jing Peng）  
部署导向选型受后处理不一致导致的评测不可比、以及跨规模/管线训练难复现困扰。提出 SURE：标准化预测格式、规范化与打分，并在真实声学与语言压力下评估从传统管线到 Speech LLM 的多种范式。此外引入代理辅助训练转换流程，将论文与代码映射为统一协议下、匹配开放数据子集上的可版本化可运行训练管线，以提升可比性与可复现性。

### 低资源跨语言摘要与语料构建

**Bridging Languages and Modalities: Lightweight Cross-Lingual Text and Speech Summarization for Low-Resource Scenarios**（论文 2655；Chaimae Chellaf）  
跨语言摘要需理解源语细微差别、筛选要点并在目标语重构意义，数据稀缺时尤难。提出用多语言句子与话语嵌入在严格数据约束下同时处理语音与文本输入；基于 CrossSum 与为三种低资源语言新采集的跨语言语音评测集开展实验。摘要称该方法在跨语言摘要、尤其低资源口语场景上具有较强潜力。

**Easper: An Accessible ASR Pipeline for Language Documentation**（论文 2781；Aso Mahmudi）  
转写是语言文献记录瓶颈；田野语言学家常缺乏使用多语言 ASR 的专业知识。Easper 提供开源无代码工作流，可从 ELAN 标注直接在云资源上迭代微调 ASR。并用其在三种瓦努阿图语言上评估“先转写哪些录音”的优先级策略，比较按声学干净度与按语言丰富度优先时的 CER 轨迹。摘要称优先词汇丰富叙事并增加声学—语音重复（即使噪声环境）可更快提升转写质量。

**VāṇīSetu: A Human-AI Collaborative Framework for Scalable Conversational Speech Corpus Creation in Low-Resource Settings**（论文 2607；Rishabh Kumar）  
提出人机协作框架 VāṇīSetu，并以印地语农业会话语料 KrishiVāṇī 为案例。整合 ASR、轻量与大模型后校正，以及增强标注工具 Vāgyojaka 上的多阶段人工验证；关键贡献是 Annotator→Validator→Verifier 的角色分离与阈值门控质控架构。受控标注研究称 mT5 后校正可显著降低标注工作量并保持转写保真，且较小微调 LM 在领域校正上优于更大 LLM。

### 语音学约束的语料精炼

**IPA-Guided Dual Transcription for Data-Centric Speech Corpus Refinement**（论文 2221；Jeong-Ju Choi）  
高质量语料需要口语与书面一致对齐，但多对多映射导致转写不一致并损害下游。提出以 IPA 引导双转录实现一致口语—书面对齐：音素中间条件语音转文本模型同时输出 IPA 与正字法文本，再由微调 LLM 从正字与语音输入生成一致口语—书面对。通过锚定语音实现而非仅文本，可迭代精炼噪声或领域语料；摘要称文本规范化与领域 ASR 经语料精炼后有实质提升。

## 本场要点

- 长会议摘要可用段级候选 + 自奖励树搜索免训练组合，缓解误差累积。
- SURE 统一预测格式与打分，并用代理辅助流程提升训练管线可复现性。
- 低资源跨语言摘要依赖多语言嵌入，并扩展到语音评测集。
- Easper 降低语言文献 ASR 使用门槛，冷启动应优先语言丰富与语音重复。
- VāṇīSetu 用角色分离阈值质控做人机协作语料生产。
- IPA 双转录把规范化锚定在语音实现，服务数据中心式语料精炼。

## 覆盖核对

| id | title |
|---|---|
| 3011 | Segment-level Tree Search for Long Meeting Document Summarization |
| 1225 | A Unified and Reproducible Experimentation Framework for Speech Understanding |
| 2655 | Bridging Languages and Modalities: Lightweight Cross-Lingual Text and Speech Summarization for Low-Resource Scenarios |
| 2781 | Easper: An Accessible ASR Pipeline for Language Documentation |
| 2607 | VāṇīSetu: A Human-AI Collaborative Framework for Scalable Conversational Speech Corpus Creation in Low-Resource Settings |
| 2221 | IPA-Guided Dual Transcription for Data-Centric Speech Corpus Refinement |
