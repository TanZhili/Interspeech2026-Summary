# Information Extraction and Retrieval

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 12）
- 论文数：7
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场以关键词发现（KWS）与音频检索为主线，并延伸到广播档案中的视听人物检索。开放词表与用户自定义关键词成为共同目标，但落地约束分化为：词库规模与存储、端侧能耗、部署后增量加词，以及流式推理下的对齐一致性。

开放词表 KWS 多依赖多模态对齐与上下文偏置。大规模术语库需要极致压缩特征存储；用户自定义场景则出现脉冲神经网络以累加运算替代浮点注意力，以及参数封顶的模块化扩展分支以冻结基座并避免旧关键词回归。流式设定下，交叉注意力中 Query/Key 角色与 CTC 音素对齐成为关键设计点。

检索侧强调无标注表示：自监督嵌入配合 DTW 或离散化后的 TF-IDF/BM25，在哼唱检索与示例检索上呈现域相关最优策略。视听人物检索则质疑“永远多模态融合”的默认假设——缺席模态会注入噪声，查询自适应的活跃模态检测成为精度关键。

总体方向是：开放词表要可扩展、可流式、可低功耗；检索要按任务选择序列匹配形态；多模态融合要先判断模态是否可用。

## 技术内容

### 开放词表与可扩展关键词发现

**Massive Open-Vocabulary Keyword Spotting**（论文 1444；Leonor Barreiros）
ASR 对训练中罕见的专业术语表现弱，开放词表 KWS 与上下文偏置可缓解，但现有系统难扩到超数百词词库。系统将特征存储相对可比基线压缩至最多约 1/128，支持海量词库且保持开放词表；无需微调 ASR，实体召回与未压缩方案相当，并称对训练未见语言仍有效。

**SPARK: Efficient Audio-Text Matching for User-Defined Keyword Spotting via Spiking Neural Networks**（论文 3336；Seung-Yeop Baek）
用户自定义文本关键词的匹配模型计算与能耗高。SPARK 以 spike-driven attention 在脉冲域端到端处理，用低成本累加替代重浮点运算。在 LibriPhrase 上相对人工神经网络对标物参数量约降 2.1×、能耗约降 21.7×，性能具竞争力。

**Scalable Keyword Spotting via Modular Network Expansion**（论文 987；Viktor Khaymonenko）
嵌入式 KWS 部署后需加新词，但常无原始训练数据且不容旧触发器回归。方法冻结基座（含 BN 统计与核心分类器），仅训轻量扩展分支与新词头。在固定工作点下，相对参数匹配的分模型基线将平均新词 FRR 从 6.46% 降至 4.37%，并优于 adapters/LoRA；在 ≤10k 新增参数预算下 MAC 更低（16.34M vs 18.45M/20.52M）。

### 流式开放词表对齐

**Streaming Open-Vocabulary Keyword Spotting via Role Swapping in Cross-Attention**（论文 1676；Liming Song）
传统框架中语音作 Key/Value 需全局上下文，流式却只有局部帧；注册表示作 Query 仅局部信息却本具全局语义。工作互换角色：流式语音作 Query、注册表示作 Key/Value。以约 0.8M 参数文本注册模型在 LibriPhrase 上报告 easy 负例 EER/AUC 为 6.82%/97.95%，hard 负例为 28.21%/79.19%。

**MPA-KWS: Multi-Modal Phoneme-Level Alignment for Streaming Open-Vocabulary Keyword Spotting**（论文 2485；Jue Zhang）
音素级对齐有助于易混词，但多数非流式；近期 CTC 流式对齐又多限于文本注册。MPA-KWS 用 W-CTC forced alignment 与多模态音素级对比学习，并以 CTC beam-search 动态挖掘难负样本。在 LibriPhrase 上称取得最佳结果。

### 无监督检索与查询自适应多模态

**SSL-based Sequence Matching for Unsupervised Audio Retrieval**（论文 2369；Moreno La Quatra）
用 SSL 表示做无标注音频到音频检索，结合 DTW 与 K-Means+TF-IDF/BM25 等。哼唱音乐检索上直接对 SSL 嵌入做 DTW 更优；口语内容示例检索上离散隐单元聚类方法更有效。

**To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection**（论文 790；Mark Gales）
真实广播档案中目标可能只闻其声、只见其人，或二者皆有；对缺席模态融合会损害精度。框架用跨模态分数一致性检测活跃模态，分类器检测准确率 89%。在 BBC Rewind（逾 12,000 视频）上自适应系统 P@1 达 94.2%，优于仅说话人（82.9%）、仅人脸（93.4%）与固定融合（90.0%），相对 oracle（96.6%）追回约 64% 差距。

## 本场要点

- 大规模开放词表 KWS 的关键瓶颈是特征存储与词库可扩展性，而非仅靠微调 ASR。
- 端侧用户自定义 KWS 出现脉冲网络与模块化增量扩展两条低成本路线。
- 流式开放词表依赖注意力角色互换与音素级 CTC 对齐，并在 LibriPhrase 上报告结果。
- SSL 检索中 DTW 更利音乐、离散匹配更利语音，策略需按域选择。
- 视听人物检索应先检测模态是否活跃，再决定是否融合。

## 覆盖核对

- 1444 | Massive Open-Vocabulary Keyword Spotting
- 3336 | SPARK: Efficient Audio-Text Matching for User-Defined Keyword Spotting via Spiking Neural Networks
- 987 | Scalable Keyword Spotting via Modular Network Expansion
- 1676 | Streaming Open-Vocabulary Keyword Spotting via Role Swapping in Cross-Attention
- 2485 | MPA-KWS: Multi-Modal Phoneme-Level Alignment for Streaming Open-Vocabulary Keyword Spotting
- 2369 | SSL-based Sequence Matching for Unsupervised Audio Retrieval
- 790 | To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection
