# Benchmarking Foundation Models

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Long Oral
- Area：（跨领域长文 Oral；程序未标 Area 编号）
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场 Long Oral 用新基准重新定义“基础模型够不够好”：低资源口语意图、ASR 幻觉分型、指令感知检索、人际立场、非言语发声（NVV）可控性，以及质量评估模型的可解释频带重要性。共同主题是：聚合指标（如 WER、总体音质）掩盖细粒度失败模式与用户意图多样性。

数据侧出现可扩展的野外挖掘（关键词+LLM 伪标、音视频弱监督）服务低资源/非书面语言。评测侧强调多维分型（词汇/语音/形态/语义幻觉）、指令动态相关标准、LLM-as-judge 稳健性，以及 NVV 的可控、落点与显著性是否与音质解耦。可解释性工作则把网络敏感频带与人类听感对照，推动人机评价对齐。

## 技术内容

### 低资源数据与 ASR 幻觉分型

**TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset with Scalable Data Mining In-the-Wild**（论文 1511；Kai-Wei Chang）发布台湾台语（台湾闽南语）真实口语意图数据 TaigiSpeech：21 名年长说话人、约 3k 话语，面向医疗与家庭助手等意图检测。探索两级监督的数据挖掘：经中间语言的关键词匹配+LLM 伪标注，以及最少文本监督的音视频框架，以扩展低资源/非书面语言数据构建。将以 CC BY 4.0 发布。

**Hallucination Benchmark for Speech Foundation Models**（论文 2347；Alkis Koudounas）提出 SHALLOW：首个沿词汇、语音、形态、语义四维分析 ASR 幻觉的基准。标准 WER 难以区分幻觉与语音不准。SHALLOW 在各维提供定向指标，形成可解释行为剖面。摘要称高质量识别时与 WER 强相关，WER 升高时相关下降，从而暴露聚合指标忽略的细粒度错误。

### 指令检索、立场与 NVV 生成评测

**INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval**（论文 1026；Chen-An Li）针对固定相似度匹配无法适配多样用户意图，提出指令感知语音检索基准 INSPIRE：自然语言指令动态指定相关标准（语义、说话人、风格、环境声及其组合）。评估大音频语言模型、级联流水线、自监督语音模型与对比音文模型四类范式。摘要称尚无方法稳健覆盖全部意图：文本路径偏语义、弱副语言；语音路径偏声学、弱指令跟随。

**StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech**（论文 2938；Yuzhe Wang）基于 Seamless Interaction，定义 9 个立场维、标准化单说话人与交互评测，并报告 LLM-as-judge 的稳健性、偏差与立场推断。摘要称共情与礼貌最易；温暖与自信中等可分且有正向偏斜；诚实最难且提示顺序偏差高；注意可分但与人类对齐弱；交互立场更敏感、方差大，尤其冲突调节。

**NVV-SuperBench: Beyond Words, Beyond Quality—Benchmarking Nonverbal Vocalizations in Speech Generation**（论文 2513；Liumeng Xue）发布英/中双语 NVV 生成基准，统一 45 类分类法，并在音质之外评可控性、落点与感知显著性。基准覆盖 15 个提示式/标签式控制系统，含客观指标、听测与 LLM 多评分。摘要称 NVV 可控常与音质解耦；低 SNR 口腔线索与长时情感 NVV 仍是瓶颈。

### 质量评估可解释性

**How Frequency Band Importance Affects Neural Network Predictions and Human Perception for Speech Quality Assessment**（论文 2382；Ada Lamba）用 Shapley、偏依赖图与扰动分析三个质量评估模型的关键频带，并做听测比较人是否对相同因素敏感。摘要称网络与人皆对有害因素更敏感；网络聚焦输入中对应低频带的小部分。工作朝统一人与网络的可解释性迈进一步。

## 本场要点

- 低资源口语意图数据可用野外挖掘与弱多模态监督扩展。
- ASR 幻觉需与一般识别错误分维评测，WER 不足以刻画。
- 指令感知检索暴露现有范式在语义 vs 副语言上的结构性短板。
- StanceBench / NVV-SuperBench 把社会立场与非言语发声纳入可重复评测。
- 质量评估模型的低频带偏好可用可解释工具与听测对照。
- 本场整体推动“细粒度、意图化、可解释”的基础模型评测议程。

## 覆盖核对

| id | title |
|---|---|
| 1511 | TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset with Scalable Data Mining In-the-Wild |
| 2347 | Hallucination Benchmark for Speech Foundation Models |
| 1026 | INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval |
| 2938 | StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech |
| 2513 | NVV-SuperBench: Beyond Words, Beyond Quality—Benchmarking Nonverbal Vocalizations in Speech Generation |
| 2382 | How Frequency Band Importance Affects Neural Network Predictions and Human Perception for Speech Quality Assessment |
