# Pronunciation Diversity

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本跨领域长论文/综述场围绕发音多样性：生成语音模型能否再现语用制约的语调变异、SSL/ASR 模型如何编码非标准音系过程（AAE 辅音丛缩减）、双语者对语音助手的语音趋同，以及可控口音规范化与无提示偏误检测。主题从描写/评测生成多样性，落到模型内部表征与人机语音适应，再到可调节的发音转换与 MDD。

方法光谱宽：Functional PCA 与贝叶斯回归比较人类与 GSM 语调；层析探测 wav2vec 2.0 / Whisper；词汇影子实验测 VOT 与元音时长趋同；掩码离散扩散上的可控口音规范化；以及 CROTTC-IF 的 prompt-free MDD。共同张力是：多样性既是需要保留/理解的社会语音事实，也是 ASR 差距与学习/配音场景中需要可调强度的对象。

综述条目在 JSON 中无 paper_id，按 Survey Talk 处理；其余论文照常列出。

## 论文技术总结

# Pronunciation Diversity

- 论文编号：
- 报告人：Farhat Jabeen
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
自然语音中的语调变化很大程度由句法与语用结构塑造；而非确定性生成语音模型（GSM）可能产生偏离这些模式的语调。需要评估 GSM 能否模拟概率性语调变异，并捕捉其语用条件。

## 方法
报告分两部分：先回顾评估 GSM 模拟概率性语调变异的已有研究；再聚焦印地语话语小品词「-hii」，考察其语用关联与在人类语音、GSM 生成语音中的语调实现。分析采用 Functional Principal Component Analysis 与 Bayesian regression，刻画并比较两类来源的语调变异；并用客观声学度量评估当代 GSM 对自然语调变异及其语用制约的刻画程度。

## 实验与结果
摘要说明了分析对象（人类 vs GSM 语音中的「-hii」）与方法工具，但未给出具体数值结果或数据规模。

## 结论
旨在同时揭示 GSM 在生成语用合适口语方面的潜力与局限；定量结论需以正式材料为准。

## 点评
把生成模型评估落到语用小品词与语调变异上，问题切口具体。摘要给出了分析工具名称，但缺少结果数字，点评无法判断 GSM 与人类差距大小。


# Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English

- 论文编号：808
- 报告人：Hamid Mojarad
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mojarad26_interspeech.pdf

## 问题
商用 ASR 对非裔美式英语（AAE）词错率可高达主流美音的约两倍；辅音丛缩减（CCR，如 test /tEst/→[tEs]）是重要音系来源，但现有层探测多关注一般音位/口音，很少剖析模型内部如何编码 AAE CCR——是简单删除，还是保留底层停顿线索的梯度变体。

## 方法
数据来自 CORAAL 的 DCA/DCB/DTA（156 说话人）。用 MFA + CMU 字典训练定制声学模型并对齐；为易 CCR 词生成缩减发音变体；聚焦七类单语素双辅音丛（/ft,nd,nt,st,sk,pt,mp/），词型上限采样后得 6760 token（3409 规范 / 3351 缩减）。冻结 wav2vec2-base 与 Whisper-small 的 12 层编码器，按 MFA 时间戳对丛帧均值池化为 768 维。探测器用单隐层 MLP（200 ReLU），说话人独立 4-fold。任务一：缩减检测（不平衡/平衡/逐丛）。任务二：对共享鼻音 C1 的 /nt/ vs /nd/ 做片段恢复（仅缩减训练、仅规范训练、仅 C1 训练）。另设计协同发音门控探测（截断处）。

## 实验与结果
摘要与引言结论：两模型均能高准确率区分缩减与规范形式；缩减段仍保留底层停止音线索，表明 CCR 被编码为结构化梯度音系变异而非单纯删除。正文抽取在协同发音探测方法处截断，层间准确率曲线与逐丛数字表未见。

## 结论
作者认为现代语音编码器对 AAE CCR 有结构化音系编码；探测有助于从“黑盒 WER 偏置”转向理解偏差机制。边界是全文截断导致定量层结果不可核验，且仅覆盖高频双辅音丛。

## 点评
工作把 ASR 公平性问题落到可检验的音系过程编码上，双探针（检测+恢复）设计直接对应“删没删 / 删了还知不知道是什么”。强处是说话人独立、控词频与单语素限制；脆弱处是强制对齐标签噪声、probe 表达力有限，以及抽取截断使“高准确率”缺少层间证据支撑。


# Bilingual Speaker Phonetic Alignment to Voice Assistants

- 论文编号：2391
- 报告人：Alyssa Allen
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/allen26_interspeech.pdf

## 问题
语音助手 ASR 偏爱标准美式英语（SAE），影响非 SAE 用户如何与真人/系统声音互动。语言调节（phonetic alignment）可衡量用户是否把助手当社会行动者；鲜有研究针对墨西哥西语主导的西–英双语者，在 L1 西语与 L2 英语上分别对真人与合成音的 VOT、元音时长收敛。

## 方法
在线词汇影子跟读（PsychoPy/Pavlovia）：参与者先读词表，再跟读人类或助手（Siri）逐词。刺激：英语 9 个低词频单音节词（测 /i,I,E,æ,O,u,U,2/ 与词首 /k,t/ VOT）；西语 9 个词（重读元音 /i,e,a,o,u/）。话者均为成人女声；英语人声为美音母语者，西语人声为非沿海墨西哥西–英双语者，机器分别为 Mexican-Spanish / US-English Siri。Prolific 招募墨西哥居民双语者，67 人中音质筛后 N=50；任务后问卷收集方言区、性别、助手可懂度等。测量基线与影子阶段的元音时长与 VOT 收敛。

## 实验与结果
摘要：在元音时长与 VOT 上跨语言、跨条件均出现收敛，表明双语者对机器声音也以类人方式响应；条件与语言主效应被方言区、性别等社会信息缓解。问卷：68% 每日用助手；感觉被英语助手理解的评分明显低于西语（图 1），而听懂英语助手却普遍很高。抽取文本在西语刺激表处截断，统计模型与效应量数字未见。

## 结论
作者认为西语主导双语者在西语与英语下都会向人声与助手声收敛，支持将助手视为类人社交对象；收敛量受方言与性别等社会因素调制。边界是影子任务社交复杂度低，且全文截断导致收敛幅度的人机对比证据不完整。

## 点评
用经典语音学对齐指标检验 CASA/拟人化，把“助手偏 SAE”从识别错误扩展到用户发音调节。强处是双语交叉设计与可懂度自评对照；脆弱处是刺激词少、口音单一女声，以及截断使“人机收敛量是否真更小”无法用正文数字核实。


# Controllable Accent Normalization via Discrete Diffusion

- 论文编号：1056
- 报告人：Qibing Bai
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bai26b_interspeech.pdf

## 问题
口音归一化（AN）把 L2 口音转为 L1，但多数系统只能一次性“全归一”，缺少口音强度旋钮；语言学习与配音等场景需要可调保留。已有连续扩散用起始时间步控强度，但固定时长、难调节奏。

## 方法
提出 DLM-AN：在 SSL 离散语音 token（WavLM）上做吸收式掩码离散扩散（扩展 LLaDA）。Token encoder 经 CTC 音素引导得到内容表示；Common Token Predictor（CTP）用源–目标 LCS 标“共同 token”并预测置信度，高置信源 token 可复用初始化反向过程——复用越多保留口音越多；Duration Ratio Predictor 用条件 flow matching 预测 dur_tgt/dur_src 以匹配母语节奏；DLM decoder 双向 Transformer 迭代去噪，CFG 可选；flow-matching 合成器 + HiFT 声码器波形。联合损失 LDLM+β1 LDP+β2 LCTP+β3 LCTC，先母语预训练再半合成并行微调。

## 实验与结果
摘要称在多口音英语上 DLM-AN 取得对比系统中最低 WER，口音减弱有竞争力，且口音强度控制平滑可解释，时长缩放稳健。正文有 CTP 可视化（中式口音样本上口音重区域置信度低）。抽取文本在采样算法处截断，完整对比表与客观/主观分数未见。

## 结论
离散扩散 + 共同 token 复用提供可解释的口音强度控制，并配合时长比预测；作者认为内容保真（低 WER）与可控归一可兼得。边界是依赖并行/半合成监督与音素对齐质量。

## 点评
关键不是再做一个全量口音转换，而是把“哪些 token 像母语、哪些该改”显式成 CTP，用复用比例当旋钮，比改扩散时间步更可解释。脆弱处是 LCS 标签对 token 音位性敏感、训练依赖伪并行，且全文截断使“最低 WER”无法与具体基线数字核对。


# Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis

- 论文编号：711
- 报告人：Haopeng Geng
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/geng26_interspeech.pdf

## 问题
MDD 需要忠实刻画细粒度声学偏差，但沿用 ASR 的 CTC 会因稀疏后验与延迟发射抹掉短暂错误线索（声学陷阱）；显式规范音素提示或强 LM 又易把预测拉回规范文本（语言学陷阱），且推理依赖提示限制自发场景。

## 方法
提出无提示的 CROTTC-IF：(1) CROTTC——用一维最优传输求单一单调帧–标签对齐（OTTC），并对两路增强视图的帧级后验做对称 KL 一致性正则（CR），损失为 L_CR + η(L_OTTC)；无 blank 主导的稠密对齐。(2) Indirect Fusion（IF）——训练期把规范音素与错误标注作特权信息，经融合网络与双头错误检测教师反传到编码器/解码器；推理丢弃教师，仅用 AM/LM 浅融合搜假设。(3) 另构造 LLM-MDD，用多模态 LLM 与不同提示模板量化显式规范先验的影响。全文自 LLM-MDD 训练细节起抽取被截断。

## 实验与结果
摘要与引言报告：CROTTC-IF 在 L2-ARCTIC 上 F1 71.77%，在 Iqra’Eval2 排行榜 F1 71.70%；无辅助数据与显式规范提示。评测覆盖 L2-ARCTIC、ERJ、speechocean762 与阿拉伯语 Iqra’Eval2。因后半正文截断，更细消融与 LLM 对比数字无法从全文完整核对。

## 结论
作者认为解耦声学建模与显式规范先验、用稠密帧对齐 + 训练期特权知识迁移，可在无提示推理下得到稳健 MDD。边界与完整 LLM 实验结果因抽取截断未能充分呈现。

## 点评
问题诊断清晰：针对 CTC 稀疏/延迟与规范泄漏分别改对齐目标与训练期知识注入，推理仍保持 prompt-free，路线与 CAPT 实际约束契合。抽取文本在 LLM-MDD 一节中断，实验数字与 LLM 分析只能部分采信；实现上也依赖最优传输与多任务权重调参，对低资源标注质量敏感。

