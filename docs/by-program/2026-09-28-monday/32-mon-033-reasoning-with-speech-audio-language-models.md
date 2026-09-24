# Reasoning with Speech/Audio Language Models

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster
- Area：9
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场核心是音频/语音大模型（ALM、LALM、SLLM、ALLM）的推理可靠性：情感与共情对齐、时间定位、实体绑定、幻觉抑制，以及用上下文或反事实证据纠正文本先验主导。共同瓶颈是语义文本线索压制声学证据、时间推理脆弱，以及生成过程中出现与音频无关的臆测。

一条主线是显式推理链与数据构造：CogAudio-LLM 用 LIME-440K 做声学–语义解耦并用 EIPS / DR-SAPO 平衡逻辑与共情；Speech-LLM 用视频元数据驱动的 reasoning chains 纠正 ASR 稀有词与命名实体；EA-CoT 则把实体–属性绑定前置，把“能力缺失”改写为“引出失败”。另一条线是时间理解：AudioGround 用确定性边界监督与滑动窗口 Q-Former；失败模式分析则用行为与因果机制视角指出注意力重分配比单纯放大音频注意力更有效。

幻觉与模态偏置成为并列焦点。NAICL 以噪声先验库做即插即用 in-context 约束；LWVS 用静音锚定的向量转向并按层加权；CoRE 用打乱/反转构造反事实音频，按证据增益重打分多选题选项。情感侧 Semantic Drift and Discriminative Re-ranking 则试图在无人工标注下打破 Neutral Bias，同时避免文本增强引入声学幻觉。

值得注意的是，官方标题为 Search-GRT 的条目，其摘要实际讨论流式多说话人 ASR 的四类架构策略（是否多实例、是否细调），与标题主题不一致；本摘要仅据摘要正文归纳，不另行补写检索智能体内容。

## 论文技术总结

# Beyond Semantic Dominance: Cognitive Affective Reasoning and Empathetic Response Alignment in Audio Language Models

- 论文编号：2400
- 报告人：Zhixian Zhao
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26h_interspeech.pdf

## 问题
ALM 常被文本语义主导，忽略与字面冲突的副语言线索（讽刺等），且情感推理停留在声学描述，缺少意图/心理层面，回复易流于模板化。

## 方法
提出 **CogAudio-LLM**：构建 **LIME-440K**（约 44 万句、497 小时）——同文多情绪的语义–声学解耦数据，含 EIPS 四步 CoT（感知、意图、心理建模、策略）与 Index-TTS2 合成语音。三阶段训练：SFT 显式 EIPS → 混合显式/仅回复数据做隐式内化 → **DR-SAPO** 双路线 RL（显式路线奖励格式与 CoT 各维逻辑，隐式路线奖励共情，共享共鸣奖励）。底座 Qwen2.5-Omni-7B + LoRA。

## 实验与结果
隐式回复共情：LLM/人工评测全面高于 Freeze-Omni、GLM-4-Voice、Kimi-Audio、Step-Audio、Qwen2.5/3-Omni、GPT-4o-Audio；冲突子集上尤为明显（如 HumDial LLM 冲突 2.91 vs 基线多 <2）。情绪准确率在冲突集从基座约 24% 升至约 46%。消融显示解耦 SFT、混合内化与 DR-SAPO 逐步抬升。

## 结论
解耦数据 + 心理 CoT + 双路线对齐可抑制语义主导并提升共情对齐；真实语音零样本较好，但 TTS 与自发微韵律仍有缝隙。

## 点评
针对“文本捷径 + 浅层情感”双瓶颈，用同文多情绪逼模型听声学，再用 EIPS 把共情做成可监督推理。风险在于训练数据大量合成、裁判（Gemini）与奖励同源偏倚，以及共情分数主观；结论对真实冲突对话的泛化仍需更多野外数据验证。


# AudioGround: Fine-Grained Temporal Grounding in Audio via Deterministic Boundary Supervision

- 论文编号：3467
- 报告人：Mingi Kim
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kim26z_interspeech.pdf

## 问题
LALM 能描述有什么声，却难以精确定位何时发生；既有监督多为粗多选或 LLM 推断时间戳，边界不可验证，限制细粒度时序定位。

## 方法
构建 **AudioGround-IT**（49.9K 指令、835 小时）：拼接 AudioCaps 片段与静音间隙，边界由构造过程确定；四任务（定位、时长、频次、排序）统一要求输出起止时间戳，并控制位置/长度偏置。模型 **AudioGround** 基于 SALMONN：帧级插值对齐 Whisper/BEATs → 滑窗 Q-Former（文本时间戳条件）→ 混合绝对时间嵌入（正弦 + 可学习残差）→ LoRA 适配 LLM。

## 实验与结果
零样本时刻检索相对多种 LALM，在 Clotho-Moment、UnAV-100、TUT-SE2017 的 Original 设定上整体最优（如 Clotho R1@0.5 27.47）；SALMONN 等基线近零。仍低于监督 AM-DETR，但显著缩小差距。消融显示绝对时间嵌入尤其 hybrid 优于仅时间戳条件。

## 结论
可验证的边界监督是 LALM 时序定位的关键瓶颈；少量确定性标注即可大幅提升零样本 grounding。

## 点评
把问题从“多加点时序数据”纠偏为“监督是否可验证”，合成拼接保证 GT，配套滑窗与时间嵌入合理。脆弱处：训练分布仍是拼接短 clip，与真实长音频重叠事件不同；评测依赖自由文本时间戳解析启发式。


# A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models

- 论文编号：3070
- 报告人：Apoorva Kulkarni
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kulkarni26_interspeech.pdf

## 问题
LALM 在时序推理上仍弱，既有基准多报差距却少做机制分析。不清楚失败是单纯“音频注意力不够”，还是音频 token 内部注意力分配不当。

## 方法
基于 TACOS 建 1,657 题三任务基准：Earliest Onset、Latest Offset、Longest Duration（多选，事件间隔/时长差 ≥1s）。行为分析比较 Audio-only / Caption-only / Audio+Caption。因果干预对比：注意力上调（增大音频总注意力）vs ScalingVis 式缩放（重分配音频 token 注意力），从 last / keyword / 两者触发。对开源可复现的 Audio-Flamingo-3、DeSTA2.5 做层定向推理时干预。

## 实验与结果
静音消融近随机，确认需听音频。多数模型 Caption-only 优于 Audio-only，ACQA 增益有限，层注意力偏文本。缩放修复率高于上调（如 AF3 平均约 20.5% vs 15.8%）；Kwd+Last 最好。全层缩放伤性能；单层定向缩放使跨模型任务平均准确率从 55.9% 到 59.1%（无微调）。AF3 偏锐化（α=2），DeSTA 偏平滑（α=0.2）。

## 结论
模态失衡不足以解释时序失败；如何在音频 token 上分配注意力更关键。层定向注意力再分配是有希望的免训练方向。

## 点评
用可控任务 + 因果注意力干预，把“听不够”推进到“听法不对”，对纠偏训练有启发。局限：任务较窄、仅两模型深入、fix rate 只看原本错误样本；作者也承认不能排除弱音频编码器等其他机制。


# Towards Deep Contextual Reasoning from Broad Descriptions for ASR with Speech-LLM via Metadata-Driven Reasoning Chains

- 论文编号：1041
- 报告人：Jakob Poncelet
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/poncelet26b_interspeech.pdf

## 问题
ASR 在稀有词、领域专名上脆弱；现有上下文偏置多为关键词列表，难扩展，也不能像文本 LLM 那样对宽泛主题描述做深层推理。级联文本后编辑又无法核对声学可行性。

## 方法
两阶段：用 YouTube 元数据（标题/清洗描述/标签）+ Whisper 伪标签（及 LLM 注入的声学合理错误）生成约 400 小时推理增强数据——LLM 写出从错误假说到参考的上下文理由。微调 speech-LLM 输出 `<initial-text>-<reasoning>-<final-text>`；与纯 ASR 数据 50/50 混合，初始转录损失掩码。评 Qwen2-Audio、Qwen2.5-Omni、Audio-Flamingo-3、Ultravox 等，测试侧重 M³AV 命名实体子集及 SlideSpeech/SlideAVSR。

## 实验与结果
基座模型直接喂大上下文会严重幻觉。微调后相对纯转写与“带上下文转写”，两阶段显式推理进一步降 WER，稀有词/NE 更明显（如 Qwen2-Audio 在 M 集上 All/Rare/NE 到约 9.3/23.1/23.3）。相对初始假说，推理修正多为正/中性；纯文本 LLM 后编辑反而抬 WER。多底座上趋势一致。

## 结论
用元数据驱动的 CoT 监督，可让 speech-LLM 在保持声学接地的前提下，从宽泛描述做上下文纠错，尤其改善稀有词与命名实体。

## 点评
把“关键词偏置”升级为“主题级理由监督”，且坚持音频条件化以避免文本乱改，方向正确。脆弱处：推理链由文本 LLM 生成可能有牵强样本（虽有过滤）、依赖视频元数据可用性、训练成本与推理长度增加。


# Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention

- 论文编号：640
- 报告人：Ming-Hao Hsu
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/hsu26_interspeech.pdf

## 问题
Speech LLM 在复杂推理上落后文本侧；既有解释多笼统为信息稀释。作者发现差距并非均匀：空间/句法/事实任务 S2T≈T2T，但需实体跟踪的逻辑任务（如 web of lies）S2T 跌至随机。

## 方法
在 VoiceBench BBH 四类各 250 题上对比 Qwen2.5-Omni 与 Phi-4-Multimodal 的 S2T/T2T。诊断为编码器池化模糊离散边界导致 **实体绑定失败**。提出推理时 **EA-CoT**：先枚举实体、记录声明、再逐步推理；其他任务用同构结构化控制提示。用 BL(1024) 分解 token 预算 vs 指令效应；消融格式/逐步/实体枚举；并用 T2T 姓名腐蚀与 MMSU 声学基准检验特异性。

## 实验与结果
web of lies 主导模态差距；排除后差距大幅缩小。EA-CoT 使该任务 S2T 提升约 +13.2（Qwen）/ +24.4 pp（Phi-4），且语音增益超过文本增益。预算扩大 alone ≤1.5 pp，增益几乎全来自指令。消融中实体枚举贡献最大（约全效应 59%）。T2T 100% 姓名腐蚀仅降约 3.6 pp；误转写姓名仍可逻辑正确。通用 CoT 与 MMSU 上无增益，支持特异性。

## 结论
S2T 推理短板主要是实体绑定的引出失败而非能力缺失；显式文本锚定可大幅弥合差距，代价是更长生成与延迟。

## 点评
任务级拆解把笼统“模态鸿沟”钉到绑定问题上，并有因果式提示干预与严格对照，说服力强。边界：TTS 评测、7B 模型、延迟开销；未来需表示层对齐以去掉显式 CoT。


# Noise-Aware In-Context Learning for Hallucination Mitigation in ALLMs

- 论文编号：1610
- 报告人：Qixuan Huang
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/huang26k_interspeech.pdf

## 问题
听觉大模型在重叠事件、噪声与声学不确定时易靠语言先验“补全”，产生幻觉。既有评测多二元分类，难刻画生成式细粒度幻觉；缓解又常需昂贵微调。

## 方法
构建 **Clotho-1K**：从 Clotho 人工筛选修订 1,000 条多事件参考，定义四类幻觉（声学属性、声源/材质、先验驱动、虚构事件），用 LLM-as-Judge 对生成字幕打标。提出免训练 **NAICL**：建宽带噪声–保守描述先验库，用 BEATs 检索 Top-K 声学相似噪声对作上下文，引导证据不足时降低语义承诺、多用声学层表述。

## 实验与结果
多款 ALLM 幻觉率普遍偏高（约 19–40%），Source/Fabricated 为主。Qwen2.5-Omni-7B 上 NAICL 将 HR 从 26.53% 降至 16.98%，四类均降。消融：真实音频 ICL 无效甚至更差；无检索固定噪声仍降 HR 但偏过度保守；2s、结构化描述、检索 3-shot 最佳；Event/Definite 词频降、Acoustic 词频升。

## 结论
噪声可作为弱语义声学下界先验，经检索式 ICL 在推理时校准生成，显著抑制幻觉且无需微调。

## 点评
把噪声从“干扰”反转为“保守生成模板”，思路轻巧、即插即用。脆弱处：依赖 LLM 评判与人工修订参考的主观性；过度保守可能牺牲信息量；目前主测单一底座与 captioning 设定。


# CoRE: Contrastive Evidence-Aware Rescoring for Multiple-Choice Audio Question Answering

- 论文编号：656
- 报告人：Yiqiang Cai
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26f_interspeech.pdf

## 问题
LALM 做多选 AQA 时常被问题/选项的文本先验主导，忽视声学证据。静音对比等干预易引入伪影；解码级对比也不贴选项打分协议。

## 方法
免训练插件 **CoRE**：将波形切成 40 ms 块，随机置换并按概率时间反转，破坏长程时序同时近似保留短时声学；在统一选项似然打分下对比原音频与反事实音频的选项 logits 得证据增益 \(\Delta\)；用 JSD 冲突与单向熵降的几何平均门控 \(\beta\) 做凸插值重打分。评 Qwen2-Audio / Kimi-Audio，DCASE 2025 Task 5（BQA/TSQA/CQA）与 AIR-Bench SoundQA。

## 实验与结果
相对 Default、提示工程、AAD、CoRE-Silence，CoRE 全面最优；如 Qwen BQA 从 30.0 到 40.7，Kimi BQA 43.3→51.9。SSM 验证置换+反转对全局相关破坏最大、局部统计几乎不变。门控消融显示自适应几何平均优于固定 \(\beta\) 或单信号门。

## 结论
信息性反事实音频 + 证据感知门控可在测试时缓解模态偏置；每例多一次前向，拟扩展到生成式 AQA。

## 点评
把视觉对比解码改造成“打乱时序但不抽走音频”的负条件，更贴多选 AQA。强在协议统一与消融完整。局限：CQA 增益较小、\(\tau\)/反转概率固定、对生成答案未验证。


# Silence is Golden: Mitigating Hallucinations in Large Audio-Language Models via Layer-Weighted Vector Steering

- 论文编号：1421
- 报告人：Tsung-En Lin
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lin26g_interspeech.pdf

## 问题
LALM 常生成无音频依据的幻觉；文本式激活操控（如 VISTA）或每步对比解码（AAD）或不够模态化、或开销大。

## 方法
用等长**静音**作负实例，相对有声输入构造模态感知转向向量 \(v_l=F_l(X^+)-F_l(X^-)\)。探层：隐状态与 \(v\) 的余弦相似度 + Cohen’s \(d\)，发现后层与正确/幻觉分离更强。提出 **LWVS**：总能量守恒下加强高影响后层、削弱早层与末层；注入后做范数归一。评 Gemma-3n 与 Qwen2-Audio，Audio Hallucination QA 与 MMAU。

## 实验与结果
纯文本转向（TVS）在 Gemma 上伤性能；MAVS/LWVS 持续提升。Gemma Total Recall 53.4%→69.0%（LWVS）；Qwen MMAU 54.8%→59.2%。Gemma MMAU 大致持平，说明未明显损害一般理解。

## 结论
静音锚定的模态转向 + 层加权可免训练抑制幻觉并常保持甚至提升通用音频理解。

## 点评
把“听没听”写进激活差，并对准后层决策，比均匀操控更合机制。脆弱处：\(\lambda\)/\(\beta\)/层划分需按模型调；主要评判别式 yes/no 与多选，生成式长答未测。


# Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering

- 论文编号：2006
- 报告人：Aounon Kumar
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26d_interspeech.pdf

## 问题
搜索智能体做多跳 QA 时早期差查询导致检索失败、奖励稀疏，错误级联。Search-R1 等纯结果 RL 在 MHQA 上仍弱。

## 方法
**Guided Retrieval Training (GRT)**：RL（PPO）训练时用 ground-truth 信息把检索语料限制到与 GT 最相似的文档子集（E5 嵌入 top-\(\kappa=300\)）；HotpotQA 用给定段落，NQ 用 query+answer 拼接。推理时仍用完整 Wikipedia 搜索。奖励为答案精确匹配。底座 Qwen2.5-3B。

## 实验与结果
相对 Search-R1 等基线，All QA 平均 EM 0.375 vs 0.318；MHQA 平均 0.297 vs 0.206（文称超 40% 提升）。检索准确率与“检索正确条件下的答题准确率”均更高；训练奖励更强、可用更少步达到更好表现。

## 结论
训练期用 GT 引导检索可缓解稀疏奖励，提升子查询与综合答题，且推理可接真实搜索引擎。

## 点评
本质是把“课程式检索约束”写入 RL 环，专治多跳早期失败。注意：本文是文本搜索智能体，与音频模态无直接关系（虽排在 audio-llm 会场）。局限：训练依赖 GT 相关文档、\(\kappa\) 固定、EM 字符串匹配偏严。


# Breaking Neutral Bias: Zero-Human-Annotation Fine-Grained Emotion Enrichment via Semantic Drift and Discriminative Re-ranking

- 论文编号：1925
- 报告人：Qihang Lu
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lu26c_interspeech.pdf

## 问题
LALM/字幕数据常呈 **Neutral Bias**（安全中性描述）；纯文本扩写会声学幻觉，多模态标注又易被视觉/ASR 主导。

## 方法
零人工标注的“假设–验证”流水线：Gemini 与 Qwen3-Omni 协同标注，高一致样本训 **判别式 LALM 裁判**（硬/软负例对比）；低一致样本用 LLM **语义漂移**生成多维情绪假设；裁判用原始音频过滤并按 Drift→Refine→Origin 重排。下游用精炼数据做 SFT。

## 实验与结果
约 2.95 万音频；裁判全量训练后 Balanced Acc 96.07%，消融显示单类负例会过度拒识。下游相对基线：Gemini 偏好胜率 66.15% vs 29.23%；词表多样性（Unique Bigrams、熵）上升；t-SNE 显示情绪分布更贴近参考流形、缓解向 Neutral 塌缩。

## 结论
语义漂移 + 声学接地重排可在无人工下把中性标签炼成细粒度情绪描述，提升下游表现。

## 点评
数据中心路线抓住“中性捷径 vs 文本幻觉”双问题，用音频裁判做物理接地。风险：裁判与评测仍依赖大模型标注、偏好评测同源偏倚；过度过滤可能丢难例。

