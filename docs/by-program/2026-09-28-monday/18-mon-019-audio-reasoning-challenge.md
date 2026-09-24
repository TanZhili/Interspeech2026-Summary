# Audio Reasoning Challenge

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Challenge
- Area：14
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为 Interspeech 2026 Audio Reasoning Challenge 及相关系统报告，核心从“听懂/答对”转向“推理链是否事实正确、逻辑自洽、可核验”。组织方引入 MMAR-Rubrics 做实例级 CoT 评估，并分 Single Model 与 Agent 赛道；摘要称 156 队参与，Agent 侧目前在推理质量上领先，单模型则靠强化学习与数据管线追赶。

Agent 方案普遍把 LALM 当工具或证据源：多源观测、声学工具分层、证据编排与一致性校验；也有能力感知的非对称多智能体协作，以及强化视觉/声学多模态证据的投票与路由。单模型侧则强调推理数据构建（如 545k 样本）、自蒸馏、面向推理质量的混合奖励与渐进式 RL，以及训练无关的注意力重标定与幻觉抑制解码。

资源约束线也清晰：紧凑 1.5B 模型用意图感知特征精炼挑战更大模型；在有限算力下，结构化提示与 DSPy 优化相对 ReST 微调更有效。瓶颈仍包括：逻辑叙事差距、密集/空间场景权衡、跨模态注意力偏文本，以及缺席声音事件上的幻觉肯定回答。

## 论文技术总结

# TAD: Token-Adaptive Contrastive Decoding with Confidence-Guided Gating for Hallucination Mitigation in Large Audio-Language Models

- 论文编号：637
- 报告人：Heyu Chang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/chang26_interspeech.pdf

## 问题
LALM 在音频物体幻觉上常对不存在的声音事件回答 “yes”，语言先验压过声学证据。既有 Audio-Aware Decoding（AAD）等对比解码用固定对比强度，未按证据强弱自适应，也未专门针对决定二分类结果的首个解码步。

## 方法
训练无关的 Token-Adaptive Decoding（TAD）：对真实音频与等长全零静音参考分别取 logits，做 AAD 式组合 \(\tilde{\ell}=(1+\alpha)\ell^{audio}-\alpha\ell^{silent}\)。构造 YES/NO 多表面形式 token 集合，用 log-sum-exp 池化得音频/静音下的 yes–no margin，定义 \(\delta=m_{audio}-m_{silent}\)。仅在 t=1 且 \(\delta<\tau\) 时对 YES token 施加惩罚 \(-\gamma\)，后续步只用 AAD logits。默认 \(\tau=0.2\)、\(\gamma=2.5\)。

## 实验与结果
在 AudioCaps-Hallucination（Random/Adversarial/Popular）与 Clotho-AQA 二分类子集上评 Qwen2-Audio-7B-Instruct 与 Gemma-3n-E4B-it（NO 为正类）。相对 AAD，Qwen2 上 TAD 的 F1 提升约 0.059–0.117；Gemma 约 0.025–0.064。Clotho-AQA 上 Qwen2 F1 由 0.810 到 0.816，Gemma 与 AAD 接近。混淆矩阵与首步 ROC 显示 TAD 显著提高对真实 NO 的召回；\(\delta\) 分布上真实 YES/NO 大致分居正负，支持小阈值门控。

## 结论
首步、类条件、置信度门控的对比解码可在不训练的前提下抑制无依据肯定回答，并在幻觉基准上更稳健，同时大体保持 AQA 表现。

## 点评
把干预收窄到“首 token 的 yes 偏置”，比全程固定对比更贴合二分类 AQA 的决策结构，也解释了为何不易全面毁掉已有足够证据时的肯定回答。代价是依赖 YES/NO 词表覆盖与 \(\tau,\gamma\) 选择，对开放式长回答幻觉未必直接迁移；Gemma 上仍可见“更保守换召回”的精度/准确率折中。


# TinyGiantALM: A Compact Audio-Language Model for Intent-Aware Reasoning under Resource Constraints

- 论文编号：491
- 报告人：Vinh-Thuan Ly
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ly26_interspeech.pdf

## 问题
音频推理顶尖系统依赖 7B–30B+ 规模与昂贵 RL，难部署于资源受限环境。小模型若被动吞下全部声学 token，易在混叠场景“致盲”；是否可用架构先验（按用户意图过滤声学）弥补参数不足。

## 方法
TinyGiantALM（约 1.5B）：三流冻结编码器——Whisper-Large-v3-turbo（16 kHz）、HTS-AT（48 kHz）、CLAP 全局语义锚；时间流池化至 N=300 后拼接。Query-guided Projector：2 层 E-Branchformer 编码局部—全局依赖 → 用户指令 masked mean pooling 作 query 的 cross-attention 精炼 → CLAP 驱动的 soft gate 仿射调制。注入 Qwen3-0.6B 的 `<audio>` 位，按 CoTA 的 Plan/Audio Analysis/Logic/Summary CoT 格式做 NTP。在单卡 A100 上训 3 epoch，推理约 5GB VRAM。

## 实验与结果
MMAR 零样本总准确率 46.4%，显著高于多数 7B–13B LALM（如 SALMONN-13B 33.2%、Qwen2-Audio 30.0%），混模态 Sound–Music 达 45.5%（对比若干大模型 9.1%）。挑战单模型榜约第 13：Rubrics 23.77、Acc 46.40，远低于 30B+ Qwen3-Omni+RL（Acc 74）。消融显示 Query 与 CLAP gate 组合相对 Vanilla +8.40；Mix S-M +36.36，但 Mix All 与 Spatial Analysis 有回退。

## 结论
意图感知精炼可在边缘友好规模上保住较强感知与部分推理；详尽多步叙事仍受语言模型规模限制，稠密混叠与空间任务上 gating 有噪声代价。

## 点评
把“小模型该听什么”做成 query 条件投影 + 全局门控，对准混模态崩盘这一痛点，效率叙事与消融都较完整。Rubrics 远低于 Acc 说明答案对了但推理链欠丰；CLAP 全局锚在 Mix All / 空间任务上的负增益也提醒：意图过滤不是万能，过滤会丢掉细物理线索。


# Beyond Symmetric Interaction: Capability-Aware Asymmetric Multi-Agent Collaboration for Audio Deep Reasoning

- 论文编号：2273
- 报告人：Chenxing Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/rong26b_interspeech.pdf

## 问题
音频深度推理需要专家级感知与多步推理。朴素多智能体对称投票/辩论难以利用不同 LALM 的互补能力，忽略角色与能力偏差（弱者拖累强者的“木桶效应”、强模型的“文本补偿”导致协同幻觉），且忽略单智能体采样不稳定性。

## 方法
AsymAudio 三阶段：(1) Intra-Agent Consistency Refinement——决策智能体对同一题重采样，不一致则由 LLM 生成客观内部引导并自校正；(2) Inter-Agent Collaborative Interaction——角色分层：强/中为决策智能体，弱为仅供证据、可挂工具的辅助智能体；反馈非对称：强者收隐式客观声学引导（不暴露对方答案），较弱者收显式同伴上下文；(3) 共识则输出，否则最多 T_max=3 轮，达上限取更强决策智能体答案，再汇总与终答一致的推理路径。实现：Qwen3-Omni Instruct/Thinking 为决策，Captioner+大 LLM 为证据，Whisper-large 作工具。

## 实验与结果
MMAR 平均 74.80（多模态多项领先，如 So-Mu 100%）；MMAU-mini 平均 79.10。消融：对称角色+对称交互 69.80 → 非对称角色 71.60 → 角色+非对称交互 72.30（两轮、无 intra 模块设定）。重采样显示弱模型更不稳定；在答案曾变的子集上，intra 精炼优于首跑与多数投票。交互轮数在 3 轮附近最优，再增略降。挑战 Agent Track 排名第 3。

## 结论
能力感知的非对称协作 + 智能体内一致性精炼，能更好利用异质 LALM 并抑制木桶效应与协同幻觉，在音频深度推理基准上显著优于单模型与常规多智能体范式。

## 点评
核心洞见是“不要让弱智能体和强智能体平权投票”，并用隐式/显式反馈分别防文本补偿与借力校准，问题诊断与机制设计对齐得好。系统重度依赖超大 Qwen3-Omni 家族，成本与可复现门槛高；终局仍偏向最强智能体，需分清增益来自协作协议还是底座规模。


# VISA: A Visual Information Strengthened Audio-Reasoning System for the Interspeech 2026 ARC Agent Track

- 论文编号：2381
- 报告人：Wenming Tu
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tu26b_interspeech.pdf

## 问题
音频推理需在混源、时变信号上做多步、证据可核验的推断；仅靠单次 LALM 回答易不稳，纯转写式 agent 又易传播识别错误。如何在“LALM as a Tool”范式下注入辅助多模态证据、稳定预测并产出符合 MMAR Rubrics 的推理链。

## 方法
VISA 三模块：(1) 多模态特征抽取——librosa 低层声学描述 + Qwen3-Omni-Captioner 高层描述；Agentic SED（候选事件→FlexSED→VLM 校验热图时间戳）；VLM 解读 Mel/CQT/RMS 等可视化谱图；(2) 模型投票——Qwen3-Omni-Thinking 与 Step-Audio-R1 各随机采样 K=3，多数表决，全不一致则贪心回退；(3) 27 类细粒度路由：LLM 评判选 CoT、VLM 谱推理接管计数/节奏等、或直送更强专家模型。LLM 骨干为 GLM-4.6，VLM 为 Qwen3-VL。

## 实验与结果
MMAR 平均准确率 77.4%，多项模态领先常见 agent / 开源推理模型。去掉细粒度路由后 Acc 降至 73.30、Rubrics 62.63。官方 Agent Track：Rubrics 66.23%（第 2），Acc 77.40%（两赛道总最高之一）。

## 结论
声学—视觉线索 + 一致性投票 + 细粒度路由可同时抬高正确率与 rubric 对齐的推理质量；未来可深化视觉线索机制与自适应协同。

## 点评
核心不是再堆工具，而是把“模型何时听不清、何时该看谱图”做成可路由的专家分工，尤其对计数/时长等数值题用 VLM 读谱，针对性强。系统重度依赖大模型合奏与手工 27 类启发式，可维护性与跨基准迁移成本是主要风险。


# The Interspeech 2026 Audio Reasoning Challenge: Evaluating Reasoning Process Quality for Audio Reasoning Models and Agents

- 论文编号：118
- 报告人：Ziyang Ma
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ma26_interspeech.pdf

## 问题
既有音频推理基准几乎只评最终答案正确率，掩盖捷径与不可解释推理；LLM-as-a-judge 的系统级打分又不稳定。社区需要面向 CoT 过程质量的共享任务与更可靠评测协议。

## 方法
举办 Interspeech 2026 Audio Reasoning Challenge：Single Model（端到端、禁外部工具）与 Agent（可编排开源模型/工具）双赛道。提出 MMAR-Rubrics：答案错误则过程分记 0；答案正确时，由 Gemini-2.5-Pro 从人工金标 CoT 生成 k=5 条可检核准则，GPT-4o 做二值判定并附简短理由，实例分为准则满足率。相对系统级 5 分量表，实例级协议提高评分者间/内一致性与人类偏好对齐。

## 实验与结果
156 队 / 18 国家地区报名；终榜 Single 14 队、Agent 16 队。Agent 整体 Rubrics 更高（冠军 69.83 vs 单模冠军 65.29）；准确率差距相对较小。单模前列多为 Qwen3-Omni 家族：两阶段 RL/GRPO、训练无关注意力操纵、高质量 LoRA SFT。Agent 前列：40+ 工具迭代取证、多模型投票+VLM 谱图数值推理、多智能体辩论共识。

## 结论
挑战把评测重心从“答对与否”转向“推理是否事实、逻辑、完整”；开源 MMAR-Rubrics 数据与脚本。当前 agent 在过程质量上领先，单模经 RL/数据管线快速追赶。

## 点评
“答错过程分归零”强制正确性与可检过程绑定，避免华丽胡编拿高分。实例级原子准则比笼统打分更稳，但仍依赖闭源评判模型；双赛道拆分便于公平比较“内化推理”与“工具编排”两条路线。


# Multi-Source Evidence Fusion for Audio Question Answering

- 论文编号：3297
- 报告人：Aivo Olev
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/olev26_interspeech.pdf

## 问题
Agent 赛道要求推理链事实性、逻辑与完整性，而 LALM 易幻觉、声学工具窄而可靠、ASR 居中；等权集成或把工具当神谕无法处理异质可靠性，且下游推理易锚定于 LALM 的错误最终答案。

## 方法
TalTech 多源流水线：Step-Audio-R1 与 Qwen3-Omni 各对全音频+三段切分只报观察不选题；统一分析做印证/分歧标注。25 工具分四档可靠性（Analytic/Probabilistic/Heuristic/LALM）并设置信度上限与权重；印证、直接作答、域适配性再调分。分歧则多轮取证 + 三阶段矛盾检测 + 定向时段复核。最终分两步 LLM：先选答案、再按七段模板写推理（隐藏源模型答案以防锚定）。推理骨干为 Kimi-K2-Thinking。

## 实验与结果
Agent Track 第 1：Rubrics 69.83，Acc 76.9%。双源相对单源回放消融显著降分（约 −3.2～−4.3 pp）。一致/印证/置信度与准确率正相关；工具推翻双 LALM 预测约 8.5%。音乐理论、时序、音频差分等子类最难；节奏类工具无关率很高。端到端约 8–10 分钟/样本。

## 结论
分层可靠性 + 双源融合 + 矛盾驱动验证可产出稠密可核验推理链，在过程质量上大幅领先，准确率仍具竞争力；架构原则或可推广到其他异质证据推理。

## 点评
与“堆工具”路线不同，本文把可靠性建模与隐藏最终答案当作一等公民，直接对齐 Rubrics 对可检事实句的偏好。代价是极高时延与大量手工阈值；权重非从 MMAR 学得，跨任务迁移需重新标定。


# Structured Prompting vs. Self-Training for Audio Reasoning Under Limited Data and Compute: Lessons from Interspeech Audio Reasoning Challenge 2026

- 论文编号：2880
- 报告人：Steven Au
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/noronha26_interspeech.pdf

## 问题
在高质量音频推理轨迹稀缺、算力有限时，应优先提示工程、自动提示搜索，还是自训练改权重？需在同一强底座上比较资源—收益折中。

## 方法
底座 Qwen3-Omni 30B，三路线：(1) Reinforced Self-Training：每题采 16 条轨迹，仅保留成功率 26–75% 的 learning-zone 正确轨迹，qLoRA 三轮迭代；(2) DSPy MIPROv2 自动提示优化；(3) 基于错误分析的结构化提示迭代（Expert Analyst → Category-Aware → Targeted Hints → Structured Reasoning：HEARD→ANALYSIS→ANSWER，禁止 Wait/Actually 式自我推翻）。vLLM 推理，提示实验 bfloat16，ReST 为 4-bit。

## 实验与结果
MMAR 1000 题：基线 67.1%；Structured Reasoning 72.6%（+5.5），16 子类中 13 类提升；MIPROv2 63.3%；ReST 64.7%（低于 4-bit 基线 65.7%）。learning-zone 仅约 21.4% 题、4361 训练样本，对 30B 模型过稀；辅助 CountingQA/MusicBench 迁移不佳（如 Music Theory −15.4%）。

## 结论
资源受限时，系统错误分析+结构化推理格式优于自动提示搜索与稀疏自训练；先激活既有能力再考虑微调。

## 点评
结论实用：对已很强的 Omni 模型，格式约束比再喂少量自生成轨迹更划算。局限是单模型单基准、部分子类样本极少，且 16-bit vs 4-bit 比较仍有精度混杂；ReST 失败更像数据与域失配，不否定大规模高质量 RL/SFT。


# Audio-Cogito: Towards Deep Audio Reasoning in Large Audio Language Models

- 论文编号：988
- 报告人：Longhao Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/li26o_interspeech.pdf

## 问题
现有 LARM 的 CoT 常僵硬、接地弱；公开音频数据多为短标签/字幕，高质量深度推理数据稀缺且多依赖闭源 API，格式与目标模型不匹配还会损害内在推理。

## 方法
开源方案 Audio-Cogito + Cogito-Pipe 四阶段：多域数据采集（声/语/乐及混合，约 545k）；Qwen3-Omni-Instruct 以约 500 条种子题 few-shot 构造 QA（含难负选项）；Qwen3-Omni-Thinking 自蒸馏自由格式 CoT（生成时不给金标答案，强制听音频）；QA 一致性 + Instruct 作 judge 滤幻觉。再对 Thinking 底座 LoRA SFT 一 epoch（ms-swift，lr 1e-5）。评测用 MMAR Acc、Rubrics、仅正确样本上的 CRS。

## 实验与结果
MMAR：Acc 71.70%、Rubrics 62.22%、CRS 0.87，开源 LARM/LALM/OLM 中领先，相对 Qwen3-Omni-Thinking Acc +约 5.44%（相对提升表述），混模态提升明显；部分指标接近或超过 Gemini 2.0/2.5 Flash、GPT-4o Audio 等。挑战赛中位列前列（与官方榜单第 3 档 Acc/Rubrics 一致量级）。

## 结论
全开源数据管线 + 自蒸馏可显著增强深度音频推理并缩小与部分闭源差距；释放 545k 数据集与代码。

## 点评
自蒸馏对齐“生成格式=训练格式”，并故意藏答案逼模型听声音，针对模板化/捷径 CoT。质量仍大体由同族 Omni 模型闭环决定，多样性上限与 judge 偏差需警惕；相对冠军级两阶段 RL，本文更偏高质量 SFT 路线。


# Audio-DeepThinker: Progressive Reasoning-Aware Reinforcement Learning for High-Quality Chain-of-Thought Emergence in Audio Language Models

- 论文编号：1720
- 报告人：Chenxing Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/he26e_interspeech.pdf

## 问题
LALM 多为感知—作答；SFT 模仿 CoT 受示范多样性限制，粗粒度 RL（准确率/格式）不直接约束推理内容，易产生形式上合格却与声学证据脱节的链条。

## 方法
Audio-DeepThinker：(1) 自动造参考链——Captioner 描述 → QA → DeepSeek 生成参考 CoT；(2) 混合推理相似度奖励——LLM 评逻辑路径/关键步覆盖等 + BGE-M3 嵌入相似；仅答对时发放；(3) 渐进两阶段纯 RL（无 CoT SFT）：Stage1 在 AVQA 等基础集上用完整奖励（准确+格式+一致性+混合相似）做 RL-Zero；Stage2 在边界难例上仅用准确+LLM 相似以鼓励策略多样性。优化用 GDPO，底座 Qwen3-Omni-30B-A3B-Instruct。

## 实验与结果
MMAR Acc 74.0%、Rubrics 65.29%，Single Model Track 第 1；MMAU-Test-Mini 78.5%。相对 Instruct 基线 +3.9 Acc。消融：混合相似奖励显著抬高 Acc 与 Rubrics；仅 Stage2 或跳过 Stage1 推理质量更差，说明需先建立基础推理再攻边界。

## 结论
细粒度推理内容监督 + 两阶段课程可使高质量 CoT 从探索中涌现；瓶颈更在奖励设计而非架构。

## 点评
把“推理像不像参考、关键步齐不齐”直接写进奖励，比只奖答对更能对齐 Rubrics。参考链由字幕+大 LLM 合成，仍可能偏文本先验；计算与裁判 LLM 成本高，但作为单模冠军方案，证明 RL 细粒度过程监督可行。


# EChO-Agent: Evidence Chain Orchestration Agent for Audio Reasoning

- 论文编号：1313
- 报告人：Siyuan Zhang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26t_interspeech.pdf

## 问题
复杂音频 QA 中 LALM 缺少问题条件感知、可核验推理链、领域知识与“回头再听”能力；现有工具增强 agent 多解决“采什么信息”，却少把工具输出蒸馏成决策关键证据并做证据—答案一致性校验。

## 方法
EChO-Agent 四阶段：Tool→Evidence→Reason→Verify。按题型静态调度 YAMNet AED、Whisper ASR、SpeechBrain SER、Essentia 音乐分析等；DeepSeek-V3 做相关性过滤、跨观察综合与证据结构化；Qwen3-Omni-Instruct 在原音频+结构化证据上按步进式提示推理，双配置各跑一次；LLM 做格式修复、推理—答案一致性检查与双候选仲裁。

## 实验与结果
MMAR：Acc 71.0%、Rubrics 63.0，Agent Track 约第 5；相对同底座 Instruct 基线 +2.3 Acc、+4.3 Rubrics。消融：去掉证据整合最伤（Acc 65.4 / Rubrics 56.9，甚至低于无工具基线）；去掉观察或验证亦有下降。混模态增益更明显。

## 结论
可审计证据链编排优于把原始工具输出直接塞给 LALM；证据整合是关键，验证主要修最后一公里错误。感知工具粒度（如 YAMNet）仍限制细粒度声音题。

## 点评
消融很有说服力：乱塞工具噪声会负优化，结构化证据才是桥。设计清晰、可复现性强，但静态题型路由与较粗事件标签限制上限；相对冠军级大规模工具迭代/可靠性分层系统，定位更偏精简可审计流水线。


# MATA: A Training-Free Approach to Mitigate Cross-Modal Attention Imbalance in Large Audio Language Models

- 论文编号：1212
- 报告人：Junyu Wang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/wang26t_interspeech.pdf

## 问题
LALM 在自注意力中系统偏向文本 token、低估音频 token（尤其中层融合层），导致声学线索利用不足、推理与幻觉变差；视觉域已有类似研究，音频—文本注意力失衡尚缺系统干预。

## 方法
训练无关的 MATA（More Attention To Audio）：在 softmax 前、仅对序列最后一 token 的 query，把音频 key 区间的原始注意力分乘以 (1+α)。默认 α=0.1，干预解码器约第 10–20 层；无新增参数、开销可忽略。可挂到 Qwen2-Audio、Qwen2.5-Omni、Ke-Omni-R、Qwen3-Omni-Thinking 等。

## 实验与结果
MMAU Test-mini：Qwen2-Audio 59.4→64.8；Qwen2.5-Omni 71.1→73.6。MMAR：Qwen2.5-Omni 56.6→61.2；Ke-Omni-R 64.1→66.8。挑战 Single Model：Thinking + MATA 达 Acc 71.0 / Rubrics 62.6（相对基线 68.6 / 58.7），赛道第 2，且为前列中唯一训练无关方案。消融显示中等 α 与中层干预最佳。

## 结论
在中层直接抬高末 token 对音频的注意力，可无训练提升答案正确率与 CoT 过程质量，是高效缓解跨模态注意力失衡的手段。

## 点评
诊断（中层音频注意力偏低）与干预点（softmax 前、末 token、音频 span）对齐干净，工程上极轻。α 过大可能破坏模态平衡；对已很强的模型增益收窄，且不改变权重本身，复杂场景仍可能需数据或 RL 补齐。


# The 5th ISCA-PECRAC Connecting Early Career Researchers and Social Gathering

- 论文编号：
- 报告人：
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
官方程序未提供摘要。仅能从标题与会场信息判断主题方向：「The 5th ISCA-PECRAC Connecting Early Career Researchers and Social Gathering」，安排在「Monday 28 September 2026 / Audio Reasoning Challenge」。

## 方法
官方程序无摘要，无法概括具体方法、模型结构或训练流程；此处不作推断。

## 实验与结果
官方程序无摘要，未给出数据集、对比设置或定量结果。

## 结论
官方程序无摘要，无法归纳作者结论与适用边界。

## 点评
该条目目前只有标题与程序位置可参考，后续若有讲义、幻灯片或正式论文，再据此补充问题设定、方法细节与可核验结果。

