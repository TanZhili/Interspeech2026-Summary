# Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：12
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦音频/语音语言模型（LALM / SpeechLLM / SpeechLM）的评测可信度、表征选择与新兴能力边界。评测侧不再满足于“单一准确率”，而是暴露选择题顺序、改写与语言提示对分数的扰动，以及发声类型（phonation）等副语言线索如何改变模型行为与社会偏见表现。

能力侧出现面向工具调用的大规模语音基准，以及在噪声 ASR 条件下用教师引导对抗去噪稳住口语理解语义流形。表征争论则系统比较连续特征与离散 token 在语音、声音与音乐上的取舍，强调语义约束与骨干缩放无法弥补表征信息损失。

低资源设定下的多语言多任务 SpeechLLM 则检验：从 ASR 预训练投影器启动、仅用每任务每语言少量标注数据时，跨语言迁移与零样本任务泛化各自能走多远。整体趋势是：评测协议更严格、任务从理解扩展到行动（tool use），表征与数据效率成为部署前的核心设计问题。

## 论文技术总结

# Robustness Assessment of Large Audio Language Models in Multiple-choice Evaluation

- 论文编号：2503
- 报告人：Fernando López
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lopez26_interspeech.pdf

## 问题
LALM 多用 MCQA 报单一准确率，但对选项顺序、题干/正答/干扰项措辞敏感，且题面文本可能含捷径，使模型不听音频也能答题；现有框架很少量化这些脆弱性。

## 方法
固定音频，对 MMAU（test-mini）、MMAR、MMSU 施加孤立与混合扰动：全部 24 种选项排列；用 gemini-2.5-flash 与 gemma-3-12b-it 生成题干/正答/干扰项各 7 版（含原文）；混合扰动以 0.5 概率独立施加各改动。评测 Audio Flamingo 2/3、Qwen2.5-Omni-7B、Kimi-Audio-7B-Instruct，并加无音频文本 LLM 对照。指标含准确率均值/方差/极值、Consistency Rate（CR）与更严的 Correctness Rate（CoR，须在全部扰动下都答对）。

## 实验与结果
默认设定与公开报告接近。文本 LLM 可明显高于随机，如 gemma-3-27B-it 在 MMAU 达 48.3%（高于随机约 22.6 点）。选项顺序与题干改写方差中等；正答改写方差升高；干扰项改写冲击最大（如 AF2 在 MMAU 准确率 std 达 13.7%）。混合扰动下 CoR 显著低于均值准确率。AF3 总体准确率与稳健性较好；Qwen2.5-Omni 对干扰项改写 CoR 更稳；AF2 最弱。模型偏好更长选项（选最长项约 42–52%，而数据中最长为正答约 45%；当最长为正答时选中率升至约 71–78%）。

## 结论
MCQA 准确率会被语言偏置与措辞扰动抬高或剧烈波动；建议以文本对照为基线，并用混合扰动 + CoR 做可负担的稳健性评测。

## 点评
把“听懂了还是读题蒙对了”拆开，用无音频 LLM 与扰动方差直接打脸单点准确率排行榜。CoR 比均值 accuracy 更能暴露脆弱模型。扰动靠 LLM 改写，虽抽样人工校验语义保留，仍可能引入风格分布偏移；本文刻意固定音频，信号级稳健性留作正交方向。


# Lost in Phonation: Voice Quality Variation as an Evaluation Dimension for Speech Foundation Models

- 论文编号：736
- 报告人：Harm Lameris
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lameris26_interspeech.pdf

## 问题
Speech Foundation Models 能直接处理原始音频，但对音质/发声类型（modal、breathy、creaky、end-creak）等副语言差异如何影响生成与情绪识别，缺少可控、开放式评测；MCQA 易掩盖生成行为偏移。

## 方法
构建 VQ-Bench：以 Buckeye、VCTK 说话人作 F5-TTS 参考，经 VoiceQualityVC 按目标声学参数合成四类平行音质提示（约 148 说话人 ×4 情境 ×5 题，共约 25h17m）。开放式长文任务覆盖治疗、职业建议、面试筛选、叙事；用 gemini-2.5-flash-lite 按量规打 1–5 分。另在 Buckeye 子集上对 xlsr-en-speech-emotion-recognition 做 SER，分析完整 logit。先做性别识别 sanity check。

## 实验与结果
OpenAI 实时 speech-to-speech API 将样本一律判为男性，后续分析转向 LFMAudio2-1.5B。CLMM 显示相对 modal，非 modal 音质在多数维度显著：如职业建议中 breathy/end-creak 更偏 STEM、creaky 更偏 care；面试中多数音质降低 shortlist/薪资/领导力背书；治疗中非 modal 提高 advice agency 与 improvement。女性相对男性在薪资与领导力背书上系统更低。SER：breathy 提高 calm/neutral、降低 fearful/surprised；creaky 降低 fearful/happy；女性提高 fearful/surprised。end-creak 效应更接近 breathy 而非持续 creaky。

## 结论
可控音质变化会系统改变 SFM 的共情、能动性、领导力判断与 SER 概率质量，并再现性别不对称；VQ-Bench 提供可复现的副语言评测框架，部署于招聘/治疗等场景前需纳入音质维度。

## 点评
用平行合成把“怎么说”从“说什么”和说话人身份中拆出，开放式生成比 MCQA 更能暴露社会偏见传导。商业 API 连性别 sanity check 都失败，说明部分系统可能几乎未接地副语言。局限包括二元性别源语料、LLM-as-judge、以及当前仅一个有效开放权重模型——框架价值大于单模型排行。


# Audio2Tool: Speak, Call, Act - A Dataset for Benchmarking Speech Tool Use

- 论文编号：2857
- 报告人：Ramit Pahwa
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/pahwa26_interspeech.pdf

## 问题
语音助手需从语音直接做 tool/function calling，但现有基准域窄、声学单一、缺少分层组合难度；级联 ASR–LLM 会传播识别错误并丢掉副语言，而音频侧工具调用缺少可诊断失败模式的大规模评测。

## 方法
发布 Audio2Tool：约 3 万查询，覆盖 Smart Car / Smart Home / Wearables，152 个已校验函数、23 类。八层难度：Direct、Parametric、Multi-Intent、Implicit、Needle-in-a-Haystack、Correction、Conversation、Intent Blending。查询由 GPT-5.2/Gemini 2.5 Pro/Claude Opus 生成并经多模型裁判与人工抽检。用 Qwen3TTS、CosyVoice-3 零样本克隆，结合 Emilia-Yodas、3D Speaker、VoxPopuli 说话人与车载/室内噪声混合，模拟 in-the-wild。指标：Tool Accuracy、Exact Match、Slot F1。

## 实验与结果
评估端到端 SpeechLM（含 Qwen-3-Omni-30B、Kimi-7B、Qwen-2.5-Omni-7B、Step-Audio2-7B、Audio-Flamingo-8B 等）与 Whisper v3 + Qwen/Gemma 级联。简单 Tier-1 准确率可很高（如 Qwen-3-Omni-30B 92.4%），但 Multi-Intent/Implicit 的 EM/F1 常低于 35%；长文、纠错、多轮与意图混合（Tier 7–8）准确率多低于 56%。更大模型总体更好；端到端尚未稳定优于强 ASR–LLM。噪声消融（babble/机械/脉冲，+15/+5/−5 dB SNR）显示性能随噪声显著下降。

## 结论
Audio2Tool 在真实工具分类与分层声学挑战下暴露：简单指令已较强，组合推理、参数精确匹配与嘈杂/多说话人场景仍是主要瓶颈；公开数据与代码以推动稳健语音工具调用。

## 点评
把“听懂意图”升级为可执行 schema 约束（工具名顺序 + 参数精确匹配），并用八层课程隔离失败模式，比扁平 SLU 意图准确率更贴部署。汽车域占比高、合成 TTS+噪声仍是分布近似；Tier-8 对纯文本工具模型不适用，突显说话人分离是音频特有难点。端到端未系统性赢级联，说明当前瓶颈仍大量在组合与参数 grounding，而非只差一个更大 SpeechLM。


# ML-KD-DRI-GAN: Teacher-Guided Denoising and Triplet-Adversarial Training for Robust Spoken Language Understanding

- 论文编号：670
- 报告人：Ankit Kumar
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26b_interspeech.pdf

## 问题
模块化 SLU 依赖 ASR 转写，替换/插入/删除错误会扭曲语义表示，造成干净训练分布与噪声推理分布的失配。对比学习与一致性方法多做确定性表征对齐，GAN-BERT 等对抗框架也未显式利用 clean–noisy 对应或教师决策边界，难以在严重 ASR 噪声下稳定做意图分类。

## 方法
提出 ML-KD-DRI-GAN：先在干净转写上训练教师（生成器为 768→512→256→512→768 的编码器–解码器瓶颈，判别器用 GAN-BERT 目标），冻结后指导学生。学生生成器对噪声嵌入做多层潜空间对齐（输出级与瓶颈级余弦对齐）；学生判别器经 Bi-DCD 对齐教师瓶颈特征与意图 logits（含温度 KL）；合成生成器产生硬负样本，并在判别器上施加 clean / denoised / synthetic 的 triplet 分离。BERT 编码，分阶段：教师独立训练 → 学生仅对抗预热 10 epoch → 再引入对齐、蒸馏与度量学习。

## 实验与结果
在 SLURP 意图检测（60 类）上，用 SpokenCSE 提供的 Google Web API / Wav2Vec 2.0 噪声假设（中位 WER 约 25% / 60%）。相对 GAN-BERT，N0.25 / N0.60 上绝对提升 4.49% / 6.46%；ML-KD 达 86.99% / 73.56%。消融显示：仅学生 DRI-GAN → 加生成器对齐 → 加判别器 KD → 加 triplet，性能逐步上升。t-SNE 显示类内更紧、类间更清；α/β/γ 在适中区间最优，高噪声下增益更大。

## 结论
多层蒸馏、对抗去噪与 triplet 度量联合，可把噪声嵌入拉回干净语义流形并改善决策边界；作者计划扩展到更多真实声学条件与 ASR 系统。

## 点评
抓的是「嵌入空间去噪 + 教师决策边界迁移」这一类 noisy SLU 问题，比纯对比一致性多了显式生成器去噪与双判别器蒸馏。强在组件可逐步消融、与 DRI-GAN/GAN-BERT 路线衔接清晰；脆弱点在依赖 clean–noisy 配对与两阶段训练超参（α/β/γ），且主结果集中在意图分类与合成噪声假设，对槽位填充与真实部署 ASR 分布的外推仍待验证。


# Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs

- 论文编号：2074
- 报告人：Jing Peng
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/peng26h_interspeech.pdf

## 问题
LALM 里连续特征与离散 token 并存，但既有对比常偏语音、在 LLM 外评估，或忽视声学离散表示与规模效应。需要弄清：对统一音频理解（speech / sound / music），哪类表示更合适，以及 backbone 放大能否弥补前端信息损失。

## 方法
提出 UniARC（基于 XARES-LLM）：音频嵌入接任务 prompt，在统一 seq2seq 指令框架下评测。两种策略：(1) SmolLM2-135M/360M + LoRA 参数高效微调；(2) Llama-3-1B/8B 冻结 backbone，两层 MLP 投影器 + 10-frame 时序拼接做探测。连续编码器含 HuBERT、WavLM、Wav2Vec 2.0、Whisper；离散含 K-means（1000 中心）聚类 token，以及 DAC、WavTokenizer、带语义蒸馏的 SpeechTokenizer。离散索引再映回 codebook 嵌入，与连续表示统一经投影器对齐 LLM。

## 实验与结果
任务覆盖 ASR、意图、情感、说话人/语言识别、环境与事件、caption、音乐流派/乐器等（LibriSpeech、SLURP、CREMA-D、ESC-50、GTZAN、Clotho 等，见表 1）。正文可读部分给出的核心结论：理解任务上编码器效力主要由语义信息丰富度决定；带强语义约束的离散 token 可超过连续特征，而偏重信号重建的高保真表示常在理解任务上失败；放大语言 backbone 难以补偿前端表示不足，前端往往设定性能天花板。抽取全文后半（结果表与分析）出现大量乱码，具体数值表无法可靠读取。

## 结论
作者主张：语义兼容性优先于单纯声学保真或盲目放大 LLM；并给出在语义密度、保真度与效率之间取舍的实践指引。更细的定量对比因抽取损坏未能完整复述。

## 点评
这是表示范式 × 模型规模 × 数据量的系统评测，抓的是「前端语义密度是否构成 LALM 理解上限」。设计上把连续/离散都投影到同一指令框架，便于公平比较。正文后半 OCR/抽取严重乱码，点评只能依赖摘要与方法段的定性主张；若需精确数字应回查 PDF。可能脆弱处在：冻结探测与 LoRA 设定会放大/缩小不同编码器差距，且 codec 采样率等实现细节也会影响结论外推。


# Towards Enabling Multilingual Multitask SpeechLLMs in Data-Scarce Settings

- 论文编号：1229
- 报告人：Seraphina Fong
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/fong26b_interspeech.pdf

## 问题
SpeechLLM 的多语言与多任务常被分开研究，且多依赖大规模数据；低资源场景下，每任务–语言仅有数小时标注时，能否把高资源 ASR 预训练迁移到 ASR、语音翻译（ST）与话题分类（TID），以及零样本跨语言/跨任务能走多远，仍不清楚。

## 方法
统一 SpeechLLM：冻结 Whisper-large-v3-turbo 编码器 + 冻结 EuroLLM-1.7B-Instruct，仅训线性投影器（约 17.31M；语音嵌入下采样 k=5）。任务用特定 prompt，交叉熵训练。流程：可选 CommonVoice ASR 预训练（200h IT 或 500h IT/ES/EN/FR/DE）→ 在 SIB-Fleurs（IT/ES/GL/CS/FIN，每任务约 3–5h）上多任务微调；另对比从零训练、Qwen2-Audio-7B-Instruct 零样本，以及 MEUSLI（28 欧语）投影器 + LoRA。

## 实验与结果
从零多任务：单语 WER 约 129–162%、BLEU 近 0；多语从零对 Romance 更稳，对 CS/FIN 仍差。IT ASR 预训练后 IT 多任务：WER 5.4%、BLEU 48.2%、TID Acc 81.5%。零样本跨语言强弱随与 IT 的语系距离变化（ES 最好，CS/FIN 最差）；排除某任务微调则该任务零样本失败（如无 TID 监督则 Acc/F1 为 0）。多语 CV 预训练后，单语微调通常比联合多语微调更稳；MEUSLI 强多语投影器上两者差距缩小。相对 Qwen2，有监督低资源微调在五语上更均衡。

## 结论
ASR 预训练自举 + 每任务不足 5 小时目标语微调，可使多语言多任务 SpeechLLM 在低资源下可行；跨语言零样本受语言相近性约束，未见任务的零样本不成立，仍需任务监督。研究范围限于三任务与欧洲语言。

## 点评
抓的是「投影器级 ASR 预训练能否撬动低资源多任务」的迁移问题，实验矩阵（单/多语预训练、零样本语言/任务、MEUSLI）设计清楚。强在用同一音频并行标注隔离多任务效应；脆弱点在编码器与 LLM 全冻、依赖欧洲语系与 SeamlessM4T 派生译文，以及 TID 仅七类——对更远语系与更难生成任务的外推需谨慎。

