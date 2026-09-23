# Reasoning with Speech/Audio Language Models
- 日期：Monday 28 September 2026 / 时间：14:30-16:30 / 形式：Poster（Area 9）/ 论文数：10
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场核心是音频/语音大模型（ALM、LALM、SLLM、ALLM）的推理可靠性：情感与共情对齐、时间定位、实体绑定、幻觉抑制，以及用上下文或反事实证据纠正文本先验主导。共同瓶颈是语义文本线索压制声学证据、时间推理脆弱，以及生成过程中出现与音频无关的臆测。

一条主线是显式推理链与数据构造：CogAudio-LLM 用 LIME-440K 做声学–语义解耦并用 EIPS / DR-SAPO 平衡逻辑与共情；Speech-LLM 用视频元数据驱动的 reasoning chains 纠正 ASR 稀有词与命名实体；EA-CoT 则把实体–属性绑定前置，把“能力缺失”改写为“引出失败”。另一条线是时间理解：AudioGround 用确定性边界监督与滑动窗口 Q-Former；失败模式分析则用行为与因果机制视角指出注意力重分配比单纯放大音频注意力更有效。

幻觉与模态偏置成为并列焦点。NAICL 以噪声先验库做即插即用 in-context 约束；LWVS 用静音锚定的向量转向并按层加权；CoRE 用打乱/反转构造反事实音频，按证据增益重打分多选题选项。情感侧 Semantic Drift and Discriminative Re-ranking 则试图在无人工标注下打破 Neutral Bias，同时避免文本增强引入声学幻觉。

值得注意的是，官方标题为 Search-GRT 的条目，其摘要实际讨论流式多说话人 ASR 的四类架构策略（是否多实例、是否细调），与标题主题不一致；本摘要仅据摘要正文归纳，不另行补写检索智能体内容。

## 技术内容

### 情感、上下文与实体推理

**Beyond Semantic Dominance: Cognitive Affective Reasoning and Empathetic Response Alignment in Audio Language Models**（论文 2400；presenter：Zhixian Zhao）
ALM 语义强但复杂情感交互弱，文本语义常压制声学细节。CogAudio-LLM 构建 LIME-440K，引入四步 CoT 机制 EIPS，经多阶段训练把推理蒸馏为隐式生成，并用 DR-SAPO 动态平衡 CoT 逻辑与直接共情回复。

**Towards Deep Contextual Reasoning from Broad Descriptions for ASR with Speech-LLM via Metadata-Driven Reasoning Chains**（论文 1041；presenter：Jakob Poncelet）
ASR 在领域稀有词与上下文相关命名实体上易错，关键词偏置难扩展。方法用视频等宽泛描述作弱语义先验，构造约 400 小时推理增强数据，让 speech-LLM 先出假设转写、再对上下文推理、最后输出校正转写。摘要称在留出 YouTube 衍生测试集上降低错误，尤其稀有词与命名实体。

**Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention**（论文 640；presenter：Ming-Hao Hsu）
SLLM 复杂推理弱于文本模型；作者指出空间/句法/事实任务 S2T≈T2T，但需实体追踪的逻辑任务跌至机遇水平，诊断为 entity binding failure。EA-CoT 在推理前枚举实体并绑定到命题。摘要称即使口语姓名识别有误也可弥合差距，消融支持显式语义绑定。

**Breaking Neutral Bias: Zero-Human-Annotation Fine-Grained Emotion Enrichment via Semantic Drift and Discriminative Re-ranking**（论文 1925；presenter：Qihang Lu）
LALM 存在 Neutral Bias，文本增强易引入声学幻觉。方法用 LLM 多维语义漂移探索情感假设，再用判别式 judge 经 hard-negative contrastive learning 按原始声学过滤。摘要称可将粗糙中性标签转为声学落地的细粒度描述。

### 时间定位、幻觉抑制与证据重打分

**AudioGround: Fine-Grained Temporal Grounding in Audio via Deterministic Boundary Supervision**（论文 3467；presenter：Mingi Kim）
LALM 能描述声音却难定位发生时间；先前或多选过粗，或时间戳不可核验。AudioGround-IT 提供确定性边界监督；AudioGround 扩展 SALMONN，用滑动窗口 Q-Former 压缩特征并加入时间戳条件与绝对时间嵌入。摘要称在多项时间定位基准上显著优于先前 LALM。

**A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models**（论文 3070；presenter：Apoorva Kulkarni）
LALM 时间推理仍弱，现有基准少探机制。作者提出含三类基础任务的分析型基准，行为分析显示文本线索存在时模型常低利用音频；因果机制分析表明跨音频 token 重分配注意力优于单纯放大音频注意力。摘要给出瓶颈层注意力缩放的准确率变化。

**Noise-Aware In-Context Learning for Hallucination Mitigation in ALLMs**（论文 1610；presenter：Qixuan Huang）
ALLM 幻觉限制可靠性，二分类评估难刻画生成任务，细调代价高。NAICL 构建噪声先验库并检索相关噪声样例作上下文，证据不足时更保守生成；同时建立 Clotho-1K 幻觉基准与四类听觉幻觉细粒度指标。摘要报告幻觉率下降。

**Silence is Golden: Mitigating Hallucinations in Large Audio-Language Models via Layer-Weighted Vector Steering**（论文 1421；presenter：Tsung-En Lin）
将向量转向引入音频域：以主动音频对静音基线做对比，抑制无根据幻觉；并据层表征与正确性相关性提出 LWVS。摘要报告 Audio Hallucination QA 上 Recall 提升，并在 MMAU 上保持乃至增强通用音频理解。

**CoRE: Contrastive Evidence-Aware Rescoring for Multiple-Choice Audio Question Answering**（论文 656；presenter：Yiqiang Cai）
LALM 多选 AQA 常偏文本先验。训练无关的 CoRE 用块置换与随机段反转构造反事实音频，对比原音频与反事实分数估计选项证据增益，再用自适应证据门控。摘要称在 DCASE 2025 Task 5 与 AIR-Bench SoundQA 上对 Qwen2-Audio、Kimi-Audio 有一致增益。

**Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering**（论文 2006；presenter：Aounon Kumar）
官方标题如此，但摘要论述流式多说话人 ASR：按 diarization 与 ASR 整合方式归纳四类架构，基于同一对流式 ASR 与 diarization 开源模型衍生四套系统，并从多说话人准确率、单说话人退化、内存与训练复杂度比较，给出部署约束下的选型指引。本条仅据摘要正文归纳。

## 本场要点
- 文本语义主导与声学证据不足，是情感对齐、时间推理与 AQA 的共同失败源。
- CoT / 元数据推理链 / 实体绑定干预，把“不会推理”细化为可引出的绑定与上下文校正问题。
- 确定性边界监督与注意力机制分析，是时间理解的两条互补路径。
- 幻觉缓解偏向训练无关：噪声 in-context、静音锚定转向、反事实证据重打分。
- Neutral Bias 数据范式强调“假设–声学核验”，避免纯文本增强幻觉。
- 条目 2006 标题与摘要主题不一致，阅读与引用时需以摘要为准。

## 覆盖核对
`2400 | Beyond Semantic Dominance: Cognitive Affective Reasoning and Empathetic Response Alignment in Audio Language Models`
`3467 | AudioGround: Fine-Grained Temporal Grounding in Audio via Deterministic Boundary Supervision`
`3070 | A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models`
`1041 | Towards Deep Contextual Reasoning from Broad Descriptions for ASR with Speech-LLM via Metadata-Driven Reasoning Chains`
`640 | Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention`
`1610 | Noise-Aware In-Context Learning for Hallucination Mitigation in ALLMs`
`656 | CoRE: Contrastive Evidence-Aware Rescoring for Multiple-Choice Audio Question Answering`
`1421 | Silence is Golden: Mitigating Hallucinations in Large Audio-Language Models via Layer-Weighted Vector Steering`
`2006 | Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering`
`1925 | Breaking Neutral Bias: Zero-Human-Annotation Fine-Grained Emotion Enrichment via Semantic Drift and Discriminative Re-ranking`
