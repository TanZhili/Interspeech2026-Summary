# Benchmarking Foundation Models

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场 Long Oral 用新基准重新定义“基础模型够不够好”：低资源口语意图、ASR 幻觉分型、指令感知检索、人际立场、非言语发声（NVV）可控性，以及质量评估模型的可解释频带重要性。共同主题是：聚合指标（如 WER、总体音质）掩盖细粒度失败模式与用户意图多样性。

数据侧出现可扩展的野外挖掘（关键词+LLM 伪标、音视频弱监督）服务低资源/非书面语言。评测侧强调多维分型（词汇/语音/形态/语义幻觉）、指令动态相关标准、LLM-as-judge 稳健性，以及 NVV 的可控、落点与显著性是否与音质解耦。可解释性工作则把网络敏感频带与人类听感对照，推动人机评价对齐。

## 论文技术总结

# TaigiSpeech: A Low-Resource Real-World Speech Intent Dataset and Preliminary Results with Scalable Data Mining In-the-Wild

- 论文编号：1511
- 报告人：Kai-Wei Chang
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26d_interspeech.pdf

## 问题
台湾闽南语（Taiwanese Hokkien）在老年群体中使用比例高，却缺乏面向照护/家庭助手的真实口语意图数据；低资源、书写不统一也使标注训练数据难扩。

## 方法
发布 TaigiSpeech：21 名老年说话人（54–78 岁，男 8 / 女 13），8 类意图（SOS CALL、BREATH EMERG、FALL HELP、PAIN GENERAL；CALL CONTACT、LIGHT ON/OFF、CANCEL），共 3,079 句、约 6.1 小时。用场景想象提示（Gemini）与可选无声视频（Veo）诱发自发表达，非朗读脚本。另探索两类野生数据挖掘：经中间语（普通话字幕）的关键词匹配 + LLM 伪标，以及少文本监督的音视频多模态挖掘。计划 CC BY 4.0 公开；基线含轻量网络、SSL 语音模型，以及 Whisper/Qwen3-ASR 级联 LLM。

## 实验与结果
摘要与引言报告：在野生挖掘数据上训练的模型迁移到真实老年录音时性能显著下降，存在明显域失配，凸显真实基准必要性。各意图约 384–387 句，平均时长约 7.15 s。全文抽取在数据采集段中途截断，详细基线数字表未完整可读。

## 结论
作者将 TaigiSpeech 定位为低资源、面向老年应急与家居助手的首个台湾闽南语口语意图基准，并强调野生挖掘可扩规模但无法替代真实老年评测。

## 点评
场景设计贴合跌倒/呼吸困难等老年刚需，数据采集流程（多设备 UI、家乡口音元数据）务实。正文抽取严重截断，实验数字与消融只能依赖摘要级描述；点评中域失配结论可信，但具体准确率/F1 无法从当前全文文本核实。


# Hallucination Benchmark for Speech Foundation Models

- 论文编号：2347
- 报告人：Alkis Koudounas
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koudounas26b_interspeech.pdf

## 问题
现代 ASR 会产生看似流利却未锚定于音频的幻觉；WER 把所有错误等权对待，无法区分音似替换与语义颠倒等危害程度不同的现象，也缺少标准化分类与度量。

## 方法
提出 SHALLOW（SpeechHALL-ucinationOvervieW），从四维分解 ASR 错误：(1) Lexical Fabrications：插入/替换/删除比加权（插入权最高，全插入非 fillers 记 1）；(2) Phonetic Fabrications：metaphone 编码上 Hamming、Levenshtein、Jaro-Winkler 平均；(3) Morphological Errors：依存结构 Jaccard 发散 + LanguageTool 语法/拼写/标点加权；(4) Semantic Errors：滑窗嵌入局部语义失配与全局语义指标。用 GPT-4o 构造 1,050 条合成假说–参考对，隔离各幻觉类型以校验指标正交性；并在真实模型与多域数据上评测。权重经可分性搜索与人工标注验证。

## 实验与结果
合成数据上 t-SNE 显示四类指标可分；WER-only（高 WER 但义近）样本语义分低，而局部/全局语义替换样本 SE 高（表 1 示例）。引言称 Encoder–decoder（如 Whisper）错误更均衡，decoder 向多模态（如 Phi-4）更偏流利、形态/语义更好但音似替换更多。SHALLOW 与 WER 在低错误率时相关强，高 WER 时解耦。正文抽取在语义误差公式段截断，完整跨模型数值表未完整可读。

## 结论
SHALLOW 提供可解释的 ASR 幻觉画像，能在 WER 失效的困难条件下仍区分错误类型，支持按应用需求做模型选型与架构迭代。

## 点评
把“幻觉”从笼统 WER 拆成可操作维度，对医疗/法律转录很有价值。权重与工具链（metaphone、LanguageTool）偏英语表层；全文结果段截断，架构对比与跨域数字需谨慎引用摘要陈述。


# INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval

- 论文编号：1026
- 报告人：Chen-An Li
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26r_interspeech.pdf

## 问题
传统语音检索按固定声学/语义相似度匹配，无法按自然语言指令切换相关准则（内容、说话人、风格、环境声及其组合）。指令感知检索在文本/图像已成熟，语音侧缺系统基准。

## 方法
提出 INSPIRE：给定口语查询 q 与文本指令 z，对库中文档打分排序。四个子集——DailyTalk（对话续接）、VCTK（同说话人，硬负例为同文异人）、Expresso（说话人/风格）、Synthetic（Natural Questions 经 GPT-4o-mini TTS + ESC-50 环境声，多属性组合）。每类意图用 GPT-5.2 生成 20 条指令再随机抽样。规模约 680 查询、4,080 查询–指令对、17,225 文档。基线四类：LALM 嵌入、ASR+字幕再 BM25/稠密文本检索、不看指令的 SSL 语音嵌入、CLAP 式对比音文；另有 LALM/文本重排。合成子集质量：Whisper WER≈0.03、说话人 SVM≈0.9998、emotion2vec 风格准确≈0.87、UTMOS≈3.76。

## 实验与结果
摘要结论：无一现有方法稳健覆盖全部意图；偏文本路径语义检索相对更好但弱于副语言属性，偏语音模型对声学属性稍好却难跟指令。正文在实验设置（LALM 列表）处截断，具体 nDCG/Recall 等数字未完整可读。

## 结论
作者将指令感知语音检索立为可评问题，并呼吁统一架构同时做指令跟随与细粒度声学匹配。

## 点评
子集设计把“同一查询、不同指令→不同正例”写死，问题定义清楚。合成多属性可控性强，但真实噪声/自发对话泛化仍开放；因结果段抽取缺失，量化对比只能采信摘要定性结论。


# StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech

- 论文编号：2938
- 报告人：Yuzhe Wang
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26fa_interspeech.pdf

## 问题
语音到语音对话模型依赖韵律与互动细微差别传达社会意图，但现有评测多盯转写/自然度，缺少对人际立场（empathy、礼貌、支配等）的标准化自动评判基准。

## 方法
StanceBench 基于 Seamless Interaction Improvised 子集的角色提示，定义 9 个立场维（S0–S8），每维正/负两极（每极约 3–4 个代表角色）。Category 1 单说话人片段（温暖、同情、礼貌、自信、真诚、注意）；Category 2 带对方上下文的互动维（社交投入、权力取向、冲突调节）。用能量 VAD 抽 IPU，拼成 30–45 s 说话人段或转轮附近的 CONTEXT/TARGET 窗。法官模型在统一量规下做 P/N 二选一并输出概率与证据；评测 Qwen2.5-Omni-7B、Kimi-Audio-7B、Granite 级联转写、gpt-audio、Gemini-2.5-Flash。固定种子抽取 25% 会话共 2431 段、484 说话人；角色提示作弱标签，报告稳健性与可分性。

## 实验与结果
摘要：共情与礼貌最易；温暖与自信中等可分且有正向偏斜；诚实最难且提示顺序偏置高（需跨轮证据）；注意可分但与人类对齐弱；互动维更依赖语境，阈值间隙与方差大，冲突调节尤甚。正文抽取止于评判提示与一致性检查，完整数值表未完整可读。

## 结论
StanceBench 提供统一流水线评估音频 LLM 作为立场法官的能力与局限，并为后续评估 S2S 对话模型选定较可靠的法官候选。

## 点评
把人际立场操作成量规两极对比，比笼统“风格分”更可诊断。弱标签依赖演员角色提示，与真实自发立场仍有距离；诚实维的顺序偏置提示法官对跨轮证据敏感。结果细节因抽取截断需以摘要为准。


# NVV-SuperBench: Beyond Words, Beyond Quality—Benchmarking Nonverbal Vocalizations in Speech Generation

- 论文编号：2513
- 报告人：Liumeng Xue
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xue26c_interspeech.pdf

## 问题
笑声、叹息、抽泣等非言语发声（NVV）对类人语音关键，但现有评测很少同时检验系统是否生成目标 NVV、位置是否正确、是否显著且不伤语音质量。

## 方法
NVV-SuperBench：统一 45 类 NVV 分类（呼吸、喉生理、笑声谱、哭声谱、情感发声、口腔杂类），英/中各 2,250 条（每类 50）。三阶段建数：从 InstructTTSEval 挖种子（Gemini 标注 + 人工多数表决）→ 按类控制生成 text / text_with_nvv / caption → 自动一致性 + 人工质检补齐。控制接口分 prompt（自然语言 caption）与 tag（如 [laugh]）。评 15 个系统（8 tag + 7 prompt）。客观：WER/CER、DNSMOS、CLAP（prompt）、NVV P/R/F1 与归一化标签距离（tag，Gemini GT 条件验证）；另有主观听测与 LLM 多评审。

## 实验与结果
摘要与导论：NVV 可控性常与整体语音质量解耦；低 SNR 口腔线索与长时情感 NVV 是持续瓶颈；不同控制接口表现差异大。正文在客观指标定义处截断，各系统具体分数未完整可读。

## 结论
该基准把 NVV 生成评测从笼统质量扩展到可控性、位置与显著性，揭示当前系统短板并支持跨接口公平比较。

## 点评
分类学覆盖远超多数 TTS 标签集，评测轴设计对“会不会笑在对的位置”很贴题。依赖 Gemini 做种子与验证存在幻觉风险，作者用约束编辑与人工审核缓解。因结果表抽取缺失，系统排名只能采信摘要定性结论。


# How Frequency Band Importance Affects Neural Network Predictions and Human Perception for Speech Quality Assessment

- 论文编号：2382
- 报告人：Ada Lamba
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lamba26_interspeech.pdf

## 问题
自动语音质量评估网络预测常与人类 MOS 相关不佳；需要弄清网络依赖哪些频带，以及人类是否对相同因素敏感，以解释人机不一致。

## 方法
对 MOSNet（CNN）、DNSMOS（CNN）、SCOREQ（wav2vec2 变体）用 SHAP、偏依赖图（PDP）与频带扰动（功率缩放 0.25–1000）分析 161 个 50 Hz 频带。评测集为未见训练数据的 IUCOSINE（100 条，MOS 分布匹配）。另做 IRB 听感实验：200 人英语流利受试者，对原声与单频带扰动对做质量分与偏好，并报告噪声量、语噪比、失真、噪声类型等因素影响。关注基频区、辅音/元音重要带，以及各模型 SHAP 幅度最大的经验带。

## 实验与结果
IUCOSINE 上 SCOREQ LCC/SRCC 约 0.63，DNSMOS/MOSNet 相关更低（约 0.19–0.23）。SHAP：三模型均更依赖低频带（约 <band 40）；MOSNet 高频几乎无影响，DNSMOS 高频多为负贡献。摘要：网络与人都对有害因素比有益因素更敏感，且网络关注输入中较小部分对应低频。正文在 PDP/扰动与听感结果中段截断，完整人机对照数字未全部可读。

## 结论
作者认为这是迈向统一人与网络可解释性的一步：若决策依赖频带不同，人机相关差可能来自决策机制差异而非单纯工程参数。

## 点评
多模型×多解释方法×听感对照的设计少见，直接针对质量评估人机失配。低频偏置与语音感知文献方向一致；SCOREQ 相关更高是否因其表示更宽频仍待结果段补全后核实。抽取截断限制了对扰动曲线与听感结论的定量复述。

