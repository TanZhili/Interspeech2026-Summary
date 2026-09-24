# Audio Language Models: Reasoning, Reliability, and Multimodal Understanding

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：12
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场审视音频语言模型的推理、可靠性与多模态理解：位置偏差、训练无关隐状态转向、多音频理解瓶颈、噪声下的工具检索、语音–文本检索重排、口语指令数据集、基准中的文本先验泄露、唤醒词半监督难负例、跨模态不稳定性，以及决策级可靠性融合是否真正被使用。共同警示是：高分不一定等于真正“听见”。

评测诊断显示选项顺序可造成高达约 24% 的性能波动；无音频输入仍可保留满分的约 60–72%；多音频输入随并发数急剧下降。缓解手段包括排列自洽、隐状态转向、LLM 合成查询嵌入转向、语音文本重排器，以及口语提示基准 DOWIS。可靠性还延伸到唤醒词自适应难负例生成与跨语/跨模态三元组不稳定性度量。

## 论文技术总结

# Hearing the Order: Investigating Position Bias in Large Audio-Language Models

- 论文编号：1025
- 报告人：Yu-Xiang Lin
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lin26c_interspeech.pdf

## 问题
LALM 常在 MCQ 上评测；选项顺序是否系统影响预测（位置偏差）在音频–语言模型中尚未系统验证，可能扭曲排行与可靠性。

## 方法
在 MMAU、MMAR、MMLU 及其 GPT-4o mini TTS 口语版（过滤 >180 s、固定四选项）上，将正确答案轮流固定到 A/B/C/D 并打乱其余选项。测 Gemini-2.0-Flash、Phi-4-Multimodal、Qwen2.5-Omni-3B/7B、Voxtral-Mini-3B、Voxtral-Small-24B；指标含准确率、Δ准确率、RSD、CKLD。再比有无选项标识符、与文本 LLM 对照，并用循环/全排列多数投票缓解偏差。

## 实验与结果
六模型均有位置偏差：部分约 5% 波动，Phi-4-Multimodal 最大约 24%。偏好方向因模型而异（如偏好 A 或 D）。选项字母标识常提准确率但不稳降偏。与文本基座比：Voxtral 偏差异与 Mistral 相近，Qwen 系音频微调后可偏离文本行为。全排列相对原始与循环通常更好降 RSD/CKLD 并提准确率；打乱选项会改变模型排名。

## 结论
位置偏差在 LALM 中普遍存在，常规 MCQ 评测可能不可靠；排列投票可缓解但算力更贵，需更专门的评测与消偏方法。

## 点评
把 LLM/VLM 已知问题系统迁到 LALM，并对排行敏感性给直接证据，对基准设计很有价值。口语版依赖 TTS，与真实口语分布有差距；全排列成本高，实用评测仍需更轻量折中。


# Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models

- 论文编号：554
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ieong26_interspeech.pdf

## 问题
LALM 上 CoT 能引出推理，但再加强常需额外监督或强化学习；能否在推理时无训练地操纵隐状态以提升口语 CoT？

## 方法
从最后 k 层、提示末 token 取隐状态差作为 steering 向量并注入解码全程（α 缩放 + 范数保持）。三种抽取：Vanilla（每样本 CoT 提示 vs 普通提示）；SGS（外部口语集差均值，复用）；TGS（纯文本集差均值，跨模态迁到语音）。外部数据 BeyondAIME（SGS 用 IndexTTS2 口语化）；超参在 spoken GSM8K 上搜。

## 实验与结果
模型：Voxtral-mini-3B、Phi4-mm、Qwen2.5-Omni-7B、Audio Flamingo 3；评测 VoxEval 数学三级 + SpeechR ReveAL-CoT。相对 CoT，多数设定提升，最高 ALL Δ 约 +4.4%（AF3+TGS）、Voxtral+Vanilla +4.3%。TGS 跨模型平均增益最大（约 +2.5%）。同预算下 Vanilla 常优于 self-consistency（三路生成）。Vanilla 对 α 敏感，SGS/TGS 更稳；TGS 少量文本样本即可接近峰值。

## 结论
无训练隐状态引导可普遍加强 LALM 的 CoT；共享向量尤其是文本导出的 TGS 数据高效且可跨模态迁移。

## 点评
把 LLM steering 落到口语推理，并验证文本差向量可迁到语音，实用价值高。增益因模型而异（Qwen 上 Vanilla 几乎无增益）；依赖开发集调 k、α，自动选参仍开放。


# MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models

- 论文编号：530
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/yang26c_interspeech.pdf

## 问题
实用 LALM 常需同时理解多段音频，但现有评测多为单音频、维度窄、输入规模小，多音频比较与随候选数扩展的能力未系统刻画。

## 方法
提出 MUGEN：35 任务、1750 实例、7 维（语义、说话人、情感副语言、时序、场景事件、音乐、组合推理）；每题 5 个音频候选（部分另加参考音频），文本约束选最佳，强制跨音频比较。基准开源模型与 Gemini-3-pro，以及 Whisper+Gemini 级联。改进：CoT、Self-Consistency，以及 Audio-Permutational Self-Consistency（打乱候选顺序再多数投票，可与 CoT 组合）。

## 实验与结果
开源整体准确率约 17–29%，接近级联；Gemini High 约 69.6%，仍远未饱和。语义维明显高于非语义，时序等更难。候选从 2 增至 5 时准确率明显下降（如 Qwen 五候选仅保留约 66%/48% 的两候选水平，有无参考音频）。APSC 增益最大：Gemini Low 最高约 +6.28%，APSC+CoT 约 +6.74%；CoT 单独近乎无效或略伤。

## 结论
多音频理解是当前 LALM 短板，且随输入数扩展恶化；音频排列自洽优于单纯 CoT，暴露位置敏感与感知瓶颈。

## 点评
用 audio-as-option 堵住转写捷径，对非语义与扩展性诊断很有力。Gemini 与开源鸿沟大；APSC 算力贵。部分数据含 TTS，真实嘈杂多源场景仍待验证。


# From Noisy Speech to Accurate APIs: LLM-driven Embedding Steering for Resilient Tool Retrieval

- 论文编号：3291
- 报告人：Rama Doddipatla
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zorila26_interspeech.pdf

## 问题
语音驱动 tool/API 检索中，API 描述风格混乱且与嵌入训练分布错位，ASR 噪声进一步放大查询–描述失配，微调嵌入成本高。

## 方法
训练无关离线 embedding steering：用 Qwen3-8B 为每个工具生成至多 10 条用户风格用例/查询，嵌入平均得 ellm，与原描述嵌入混合 e′=α e_api+(1−α)ellm（验证取 α=0.5）。查询侧：WhisperSpeech TTS + 混响与 speech-shaped noise（SNR∼U(−5,5) dB）后 Whisper ASR，得到干净/噪声转写。

## 实验与结果
数据集 Gorilla-HF、Ultratool、ToolACE；嵌入 BERT-base、ToolRetriever、bge-base/large。K=10 时各模型/数据集 NDCG 普遍提升；如 bge-large 平均 N@1 在参考查询约 52.7→60.5，噪声查询约 19.3→20.5。弱编码器相对增益最大。K=1 已有收益，K=5/10 更稳；α∈[0.25,0.5] 最优。

## 结论
LLM 合成查询平均嵌入可无重训地增强 speech-to-API 检索，对描述噪声与 ASR 错误均有韧性，易接入现有流水线。

## 点评
把查询扩展做成工具侧表示精炼，模型无关、部署轻。噪声条件 WER 极高时绝对分仍低，steering 是缓解而非根治。语音为 TTS 仿真，真实口语意图分布可能更散。


# A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers

- 论文编号：2154
- 报告人：Inho Kim
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kim26q_interspeech.pdf

## 问题
RAG 知识库同时含语音与文本时，联合嵌入有模态鸿沟与分数失衡；分模态检索后需能跨模态比较的重排器，但缺少跨模态相关性标注。

## 方法
STEREO：文本检索器用 e5-mistral-7b-instruct，语音用 HuBERT 基 SpeechRAG；分数 Z-score 归一后融合取 top-k。用 gpt-4o-audio-preview（纯文本候选用 gpt-4o）打统一相关性分构图。重排器在 ULTRAVOX / Qwen-Audio-Chat / Qwen2-Audio 上 LoRA，以 Yes−No logit 差打分，支持 pointwise/pairwise/listwise；长音频切窗，训练随机窗、推理 mean/max 聚合。

## 实验与结果
Spoken SQuAD（TTS 段落）+ MS MARCO 混合池。Pointwise 最稳：混合域 Spoken SQuAD 上 ULTRAVOX Hit@1 约 0.76 vs Z-score 0.53。下游 QA EM 普遍高于 Z-score（如 Spoken SQuAD mixed 上 ULTRAVOX 生成约 0.36→0.48）。无 Z-score 时语音候选易被淹没；Max 池化在语音占比较高时更好；30s×4 窗在 Spoken SQuAD 上略优。

## 结论
跨模态标注 + ALM 重排可在单模态与混合池中提升证据排序与下游 QA；pointwise 在异构设定更稳，Z-score 对保持语音可见性关键。

## 点评
late fusion + 重排避开联合空间鸿沟，路径清晰。标签依赖专有 ALM，质量有上限（相对 oracle Hit@1 仍有差距）。Spoken SQuAD 为 TTS，作者亦指出自然口语有待验证。


# Do What I Say: A Spoken Prompt Dataset for Instruction-Following

- 论文编号：685
- 报告人：Maike Züfle
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zufle26_interspeech.pdf

## 问题
SLLM 指令跟随评测多靠文本提示，难反映真实语音交互；现有口语指令基准多为 TTS、语种少、与任务输入绑死，难复用到任意下游集。

## 方法
发布 DOWIS：人工撰写并录音的平行文–语提示，与任务输入解耦，可挂任意基准。覆盖 9 任务（ASR、TTS、ST、MT、S2ST、语音/文本摘要、音频分章、SQA）、11 语种、每任务–语言 10 条提示（basic/formal/informal/detailed/short 各 2），总音频约 3h17m。在 Phi-4 Multimodal 与 Qwen2.5-Omni 上系统比较模态、风格与语言。

## 实验与结果
文本输出任务上文本提示显著优于口语提示；Phi 在口语 ASR 等上可出现灾难性失败。语音输出任务（TTS、S2ST）口语与文本接近甚至略优。低资源/跨语（如 cs、nl、sv 等）文语差距更大。非正式与短提示最难；男女说话人有任务依赖的小偏差。Whisper 转写显示提示可懂，差距主要来自模型跟口语指令能力。

## 结论
仅用文本提示会高估指令跟随；需多样口语提示评测。DOWIS 提供可复用的人工录音资源。

## 点评
把“提示模态”从任务数据中拆出，设计对社区很实用。当前仅两模型，且部分任务语言覆盖受限；录音设备杂但作者已用转写排除可懂度主因。


# All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation

- 论文编号：913
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/foo26_interspeech.pdf

## 问题
LALM 基准高分未必等于真听懂：题目可能靠文本先验作答，或仅需局部声学片段，现有“静音替代”等方法有混淆。

## 方法
双轴诊断：Text Prior——对比 Full / 无音频 None / 文本骨干 TB，定义 RTP=Acc_none/Acc_full；Audio Reliance——将音频均分为 N 段独立评测，算保留率 RN，并按 Full/None/片段正确性划分 TS、FS、XS、AH、UN。在 MMAU、MMAR、MMAU-Pro 上评 8 个 LALM。

## 实验与结果
无音频仍保留约 60–72% 满分准确率（模型平均 RTP）。需音频的题目中，仅约 3.0–4.2% 为跨段必需（XS），多数片段已足够。TS 占约 26–39%；语音类 Full–None 差距较大，部分 open/指令类行为不同。多模态训练后 None 常高于 TB，文本先验被强化。

## 结论
当前基准大量混入文本先验与局部线索，不宜直接等同整体听觉理解；建议报告文本先验基线与音频依赖保留率以改进评测。

## 点评
把 VQA/NLI 的“无模态基线”系统迁到音频，对基准可信度是一记清醒剂。片段划分较粗，未覆盖真正长程依赖任务设计；指导原则清晰，落地需基准作者配合重标。


# ADALA: A Wake-up Word Detection Framework Based on Adaptive Semi-supervised learning and Large Language Model

- 论文编号：493
- 报告人：Nianhang Tang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tang26_interspeech.pdf

## 问题
唤醒词检测是开放集拒识问题，固定规则挖负例或低层对抗难覆盖语义/语音相似的未见硬负例，唤醒率与误唤醒难兼顾。

## 方法
ADALA：用 PPO/Actor-Critic 微调 Qwen2.5-14B，结合专家先验提示生成候选短语，CosyVoice2 TTS 成音频；奖励由 WUW 模型与 FunASR 联合判定（误触发且 ASR 非真词给正奖，真词混淆强惩罚等）。生成硬负例与有标/无标真实数据在半监督框架联合训练（监督 max-pool、教师–学生一致性、域对抗减轻 TTS 伪迹）。目标词“xiao fei xiao fei”，并测英语 “Hello Wikka”。

## 实验与结果
室内自建约 1430 小时普通话数据。相对 Hard-Negative Mining：平均唤醒率 87.75%→90.43%，相似词 FAR 5.87%→3.19%；相对 GraphemeAug 在略高 FAR 下显著更高唤醒率。消融：SSL 主抬唤醒率，RL 生成主降 FAR。英语小集：唤醒约 90.42%，FAR 约 1.67%，优于两基线。

## 结论
RL 驱动 LLM 持续生成决策边界硬负例，再与半监督融合，可在保持低误唤醒下提升唤醒率，并具跨语迁移迹象。

## 点评
把“语义级硬负例”做成与检测器共进化的闭环，针对开放集误唤醒痛点。强依赖 TTS 与内部大规模数据；商用工作点（48 小时一次误触发）标定细节与公开复现难度需注意。


# Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models

- 论文编号：1980
- 报告人：Nadir Durrani
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/mousi26_interspeech.pdf

## 问题
语音优先多模态助手应对语义等价的文本与口语查询给出一致的视觉 grounding 判断；现有评测多看单通道准确率，难揭示文–语与跨语决策不一致。

## 方法
构建 10150 个文化 grounding 对比三元组（18 MENA 国图像：1 条支持陈述 Q+、2 条似真不支持 Q−），经需图过滤与人工校验；英–阿翻译 + XTTS 男/女声合成，并加噪声/混响。定义对比不稳定性 CI：在至少答对一条的三元组中，未能全对的条件比例。评 Qwen2.5-Omni 3B/7B、Qwen3-30B-Omni、Phi-4-multimodal。

## 实验与结果
口语相对文本抬高 CI，阿拉伯语更甚（如 Q2.5-3B 阿语文本 CI 0.43→口语 0.71）；英语较稳。放大模型降 CI 但不能消掉跨模态/跨语差距。SNR 降低时阿拉伯语 CI 升更陡。联合文–语输入相对纯音频降 CI，仍不及纯文本。聚合 Q+/Q− 或 F1 可能仍高而 CI 暴露碎片化失败。

## 结论
模态不是中性通道；对比不稳定性揭示准确率掩盖的文–语与跨语不一致。公开基准与 CI 度量供后续稳健性评测。

## 点评
用条件三元组指标补足独立陈述准确率，诊断视角清晰。语音为合成；图像–文化先验与翻译质量仍可能纠缠。对语音助手可靠性评测有直接参考价值。


# When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence

- 论文编号：2989
- 报告人：Jaden Moon
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/moon26b_interspeech.pdf

## 问题
质量感知多模态融合常用各模态可靠性分数加权决策，但分数是否真正在推理时改变预测，还是只与性能相关，现有评测往往分不清。尤其在情感与压力识别中，模型可能因架构灵活性或缺失模式而提升，质量信号本身未必参与决策。

## 方法
将输入拆成证据 E、可用性掩码 M、质量信号 Q，训练后冻结专家与融合规则，仅在 fully observed 测试样本上打乱 Q 的实例对齐（Broken-Q），与匹配质量（Clean-Q）比较 Balanced Accuracy 的置换差距 Δ_perm。质量由信号派生指标（音频 SNR/削波、生理 dropout、视频曝光/模糊等）在 fold 上仅用训练集做分位缩放。融合包括质量加权 late fusion 与以 [M,Q] 为输入的线性 softmax MoE；单模态专家为 LR 与 HGB。主数据 StressID（语音/脸/生理），边界情形 CMU-MOSEI；并用与 corruption/正确性对齐的合成质量做阳性对照，同时报告 oracle 选最优专家的 headroom。

## 实验与结果
StressID 上专家有分歧与可竞争空间（median Δ≈0.20），但原生质量与正确性相关近零（ρ≈0）；Clean–Broken 差距近零（LR −0.002±0.06，HGB −0.011±0.06，MoE −0.003±0.02），尽管 oracle headroom 约 0.35–0.37。阳性对照则显著：corruption +0.071±0.03，correctness-aligned +0.346±0.06。CMU-MOSEI 上语言专家更强，原生质量置换差距 0.004±0.004（不显著），oracle headroom 0.216±0.006。

## 结论
质量感知融合只有在可靠性估计能指出当前样本该信任哪一路输入时才真正影响决策；原生“干净度”类质量往往不够。作者主张用对齐打破式诊断验证质量依赖，而非仅看架构是否“质量感知”。

## 点评
把“能否更好路由”“融合能否用路由信号”“原生质量是否提供该信号”拆开，用冻结后置换检验决策依赖，设计干净。强在阳性对照证明诊断有灵敏度；弱在仅决策级融合、fully observed 评估，且阳性对照主要在 StressID，对 early/mid-fusion 注意力类方法需另设可干预的可靠性通道。

