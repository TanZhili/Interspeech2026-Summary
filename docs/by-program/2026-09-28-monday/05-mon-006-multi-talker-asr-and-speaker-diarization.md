# Multi-Talker ASR & Speaker Diarization

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 8）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

多说话人 ASR 与说话人日志（diarization）在本场被作为紧密耦合问题讨论。合成会话数据研究（FastMSS + DiCoW / Sortformer）表明最优仿真配方高度任务依赖：增大重叠利于 ASR 却损害 diarization；来源多样性常优于精确域匹配；合成+真实混合可超过仅真实训练。

系统路线上，Dixtral 用 diarization mask 条件化声学编码器（DiCoW→Voxtral）而非 Serialized Output Training 去改解码器，以避免灾难性遗忘；GLAD 以全局—局部融合的动态 MoE 在深层保留说话人特异声学线索；HCM 则被扩展到联合转写—说话人空间聚类，同时服务无目标说话人与目标说话人设定。

流式多说话人 ASR 被归纳为四种架构策略（是否多实例、是否微调），在精度、单说话人退化、内存与训练复杂度间权衡。评测侧提出 tcpSemER（嵌入语义相似度替代编辑距离）并按重叠/非重叠分解 tcpWER，发现 LLM 方案在两说话人有竞争力，但随说话人数与重叠上升而退化，模块化流水线更稳。瓶颈是重叠、远场、说话人数变化与评测是否抓住“改义错误”。

## 技术内容

### 合成数据、条件化 SLM 与 MoE 架构

**Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization**（论文 443；Alexander Polok）
研究合成数据各仿真选择对领先 MT-ASR（DiCoW）与 SD（Sortformer）的影响，并开源高效仿真器 FastMSS，分析轮替动态、源域、声学增强与数据混合。发现增大重叠利于 ASR、损害 diarization；广来源多样性持续优于精确域匹配；仅合成可接近真实基线，合成+真实相对仅真实有显著增益。

**Grounding Spoken LLMs in Multi-Speaker Audio via Diarization Conditioning**（论文 445；Alexander Polok）
提出 diarization-conditioned SLM：用 diarization mask 条件化声学编码器提取目标说话人表示并冻结解码器，实例化为 Dixtral（DiCoW 编码器 + Voxtral）。在 AMI、NOTSOFAR-1、LibriSpeechMix、Mixer6 上说话人归因转写 cpWER 绝对优于所列对比系统；在新的长篇多说话人 QA 基准上，零样本远场内容理解可匹敌 Gemini，微调后在各任务上超过 Gemini 与近讲 Voxtral。

**GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR**（论文 1022；Yujie Guo）
针对端到端 MTASR 中说话人特异声学特征在深层被稀释，提出 GLAD：路由机制动态融合说话人感知全局上下文与细粒度局部声学以自适应选专家。在 LibriSpeechMix 与 CH109 上显著优于现有 SOT 类 MTASR，尤其在高重叠场景；摘要称属首个将全局—局部融合 MoE 用于 MTASR 的工作。

### 假设聚类、流式架构权衡与评测

**Speaker-Aware Hypothesis Clustering and Merging for Target-Speaker-free and Target-Speaker Multi-Talker ASR**（论文 1604；Yosuke Kashiwagi）
在 HCM 框架中把聚类距离重定义为联合转写—说话人空间，以连续说话人嵌入增强。摘要称在相同内容条件下相对常规 HCM 最高相对 WER 降低 46%，并在目标说话人设定通过嵌入选说话人相对离散 speaker-ID prompting 降低 23% WER，LibriMix 上保持竞争力。

**Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs**（论文 2005；Taejin Park）
将流式多说话人 ASR 按 diarization 与 ASR 集成方式归为四类架构，基于同一对开源流式 ASR/diarization 模型派生四种系统（是否多实例、是否微调）。在多说话人精度、单说话人精度退化、内存占用与训练复杂度上系统比较，为不同部署约束提供选型指引。

**Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics**（论文 2912；Naohiro Tawara）
沿重叠鲁棒性、语义保真、说话人数、单/多通道四轴比较 LLM 与模块化流水线。提出 tcpSemER（用嵌入语义相似度替代 Levenshtein），并分解重叠/非重叠 tcpWER。三数据集实验显示 LLM 在两说话人有竞争力，但随说话人数与重叠增加而退化，模块化流水线更鲁棒。

## 本场要点

- 合成会话数据的“最优配方”对 ASR 与 diarization 相反：重叠率不可一刀切。
- Diarization 条件化编码器可把 Spoken LLM 扩展到远场多说话人，而不必 SOT 改解码器。
- 动态 MoE 与说话人感知假设聚类分别从表征路由与假设融合两端加固重叠场景。
- 流式多说话人系统的关键权衡是多实例/微调与内存、单说话人退化之间的取舍。
- 传统 WER 类指标会漏掉改义错误；tcpSemER 与重叠分解提供更细诊断。
- LLM 会话 ASR 在说话人数升高时仍弱于稳健模块化流水线。

## 覆盖核对

- 443 | Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization
- 445 | Grounding Spoken LLMs in Multi-Speaker Audio via Diarization Conditioning
- 1022 | GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR
- 1604 | Speaker-Aware Hypothesis Clustering and Merging for Target-Speaker-free and Target-Speaker Multi-Talker ASR
- 2005 | Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs
- 2912 | Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics
