# Cross-Lingual and Multilingual Speech Recognition 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
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

本场多语/跨语识别与 Speech LLM 聚焦语言干扰、公平性、低资源参数高效适配、编码器融合，以及编解码器 SSL 的语言敏感性。错误分析表明语义保持来自音系–形态–句法–词汇的跨维交互，且不同架构整合语言信息的机制不同。

系统方向包括：语言感知蒸馏查询与门控缓解共享投影器干扰；共享–私有 Fusion-LoRA 与置信门控 Mean-Teacher；多编码器融合；形态感知分词对抗 Indic 形态破碎；SpeechLLM 解码器层冗余剪枝；弱掩码残差可靠度域适应；以及代码切换兴趣点对比训练。公平侧用 MinMaxGAP 正则量化并缩小多语多模态情感识别的性别差距。

## 论文技术总结

# How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR

- 论文编号：920
- 报告人：Simon Gonzalez
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26c_interspeech.pdf

## 问题
多语 ASR 替换错误对语义保持的影响难以用 WER 刻画；先前多用 WALS 等语言层类型学代理，不清楚从 ASR 输出直接量测的音系/形态/句法/词汇特征如何交互、是否因架构而异。

## 方法
在 FLEURS 42 语、>154 小时上跑 Whisper 与 Seamless；仅分析对齐后的替换错误。因变量为句级语义相似度 SENT（paraphrase-multilingual-MiniLM）；自变量为词级 PHN（phonemizer+Levenshtein）、MOR/SYN（Stanza POS/依存差）、SEM（fastText）。用 glmmTMB 混合效应 beta 回归，分阶段加入维度交互、ASR 三阶交互与语言效应。

## 实验与结果
主效应均显著：PHN 负向最强（β=-0.31），SEM 正向最强（β=0.84）。交互模型显著改进拟合；最强为 MOR:SYN（χ²=165 量级改进中 χ²=113）。Seamless 基线更好（Whisper β=-0.20）；Whisper 对 PHN/SEM/SYN 退化更敏感，但更会利用形态保持。语言随机效应差异大（如越南语维度强但句级一般，捷克语音系差但句级可补偿，乌尔都语句级最差）。

## 结论
句级语义保持来自跨维度系统交互而非孤立错误；Whisper 与 Seamless 以不同机制整合语言学信息；类型学差异导致不同错误剖面，多维框架比聚合准确率更有信息量。

## 点评
把评价从 WER 拉到“意义是否保住”，并对架构做交互建模，对多语部署诊断有价值。仅替换错误、依赖 Stanza/phonemizer/嵌入工具链，插入删除与工具误差会偏置结论；属分析研究，未给出可直接落地的纠错或训练改法。


# Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision

- 论文编号：2446
- 报告人：Shreyas Gopal
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gopal26_interspeech.pdf

## 问题
用 ASR 配对数据做上下文蒸馏可训英语 Speech LLM，但多语共用静态 Q-Former query 易语言干扰，低资源语被主导语淹没；大规模任务 SFT 又昂贵。

## 方法
冻结 Whisper-large-v3 编码器与 Llama-SEA-LION-v3-8B-IT；可训 Q-Former + 语言感知模块：query bank（每语一组）与门控网络（卷积 LID 或注意力池化），对输入语音做 soft 混合或 hard 选择（STE）；调度教师强迫稳定早期门控。损失：输入蒸馏（音频尾嵌入对齐文本头）、输出蒸馏（LLM 末隐状态对齐）+ LID CE。仅用约 5.8K 小时多语 ASR 数据。

## 实验与结果
相对匹配多语基线 ML-DiVA：开放指令跟随平均约 +14%（hard-gating；印尼 3.04→3.71）。自建 Audio-MLQA 上相对既有 Speech LLM 基线约 +32%；相对 ML-DiVA 闭集平均约 +3%（3.96 vs 3.85）。消融：L=256 显著降蒸馏损失；硬选择优于软混合；两种门控 LID 准确率均 >94.9%。

## 结论
语言感知 query 路由可在 ASR-only、骨干冻结条件下缓解多语干扰，高效扩展指令跟随与口语 QA；并释放多语评测数据。

## 点评
在 DiVA 式蒸馏上加 LID 门控，用最小可训容量打多语，工程上很实用。评测依赖 GPT-4.1 与 TTS 合成问句，与真实口音/噪声分布有差距；中文相对最弱、与主导语差异大，说明 bank 规模与数据配比仍是瓶颈。


# ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition

- 论文编号：3143
- 报告人：Zi Haur Pang
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/pang26b_interspeech.pdf

## 问题
Speech LLM 做多语多模态 SER 时，性别表现差距如何随语言与模态变化尚缺系统基准；多模态融合不保证更公平。

## 方法
在 MELD-ST（英/日/德，人工标注说话人性别）上基准多种 Speech LLM。提出 ERM-MinMaxGAP：LoRA 微调 Qwen2-Audio，主损失为交叉熵 ERM；正则 R=（各语言内男女损失差的最大值）^p（主设 p=2）；λ 按验证集性别差距相对阈值 ε 用投影梯度式自适应升降。评估单模态（仅语音）与多模态（语音+真值转写）。

## 实验与结果
多语设定相对最强基线：单模态 W-F1/ACC 约 +5.5/+9.8，多模态约 +5.0/+3.6；整体性别 AVG 差距分别降约 0.1 与 1.4 量级（摘要称 0.1%/1.4%），多模态下 AVG 再降 0.80。偏差强依赖语言与模型；多模态常提准确率但不稳定缩小性别差。消融：固定大 λ 可压差距但伤 SER；自适应 λ 在性能–公平折中更优；p=2 较 p=1 更利于公平。

## 结论
给出多语多模态 Speech-LLM SER 性别偏差基准，并表明惩罚最差语言内性别损失差可同时提升识别与公平折中。

## 点评
把“最差语言间隙”作为优化目标，避免平均公平掩盖某一语的极端偏差，适合多语部署。性别为人工标注、模态用金标转写，真实 ASR 转写误差下的公平性未测；固定大 λ 的效用–公平权衡表明超参仍关键。


# Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA

- 论文编号：1183
- 报告人：Jie Liu
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/liu26h_interspeech.pdf

## 问题
低资源多语 ASR 联合训练中，共享 LoRA 子空间易负迁移；一致性/自训练在预测不可靠时会放大确认偏置与跨视图不稳。

## 方法
冻结 Whisper-small，用 SPF-LoRA：共享分支学跨语共性、每语私有分支建模特异分布，可学习门控 β_ℓ 融合。训练上用 MT-CR：仅对可训适配器做 EMA 教师；双增强视图上学生 CE + 教师置信度门控（c_t>τ）的 KL 一致性；两阶段先监督训 SPF，再升温 λ、收紧 τ。

## 实验与结果
Kathbath 五语（gu/hi/mr/pa/ur）。SPF-LoRA 宏平均 WER 23.93%，加 MT-CR 至 19.85%，优于 small+LoRA（30.73%）与 medium+LoRA（22.46%）；Gujarati 38.86%→25.04%。消融：可学习融合优于纯共享/纯私有/固定求和；置信度门控是 MT-CR 关键；注入范围扩至 qkvofc 最佳。相对 LoRA 五语 CER 均下降。

## 结论
共享–私有 Fusion-LoRA 加置信度门控 Mean-Teacher，可在冻结骨干的参数高效设定下缓解负迁移并提升低资源多语 ASR。

## 点评
把“容量竞争”拆到私有 LoRA、用门控过滤不可靠一致性，针对性强。实验限于印欧系五语与 Whisper-small；最差语仍明显更高，门控阈值与增强强度需调，跨语系泛化未验证。


# Speech Encoder Fusion for LLM-based Automatic Speech Recognition

- 论文编号：1039
- 报告人：Jakob Poncelet
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/poncelet26_interspeech.pdf

## 问题
Speech-LLM 通常绑定单一预训练声学编码器；不同编码器错误互补，简单拼接未必充分利用，多语/分离场景更需自适应融合。

## 方法
在投影到 LLM 前融合两路等长编码器特征：对比 concat、sigmoid 门控、帧内多头门控、位置 Transformer、时间交织 Transformer（再池化）。编码器冻结；2 层 MLP 投影 + QLoRA（rank 4）微调 LLM。荷兰语：Whisper-large-v3 + NeLF + Tweety-7B；英语：Whisper + Wav2Vec2-FT + Llama-3.1-8B；亦可融 ECAPA2 做带说话人标注转写；可选第二阶段把解码器假设并入提示。

## 实验与结果
荷兰语单语：时间 Transformer 最佳（clean/other 6.8/8.3），优于 concat 与单编码器。英语：sigmoid 门控最好（2.8/5.5）。联合英荷训练时多头门控最佳（NL 6.5 / EN 2.5）。分离 ASR：时间 Transformer SA-WER 18.1、Spk-Conf 3.6。并入解码假设后荷兰语可到 5.6/7.8，优于纯文本纠错。

## 结论
精心设计的并行编码器融合在开销有限下全面优于特征拼接，适用于单语、多语与分离 ASR；短时 ASR 设定下仍可进一步用历史文本与更大 LoRA 提升。

## 点评
系统比较多种融合，并覆盖低资源语与说话人编码器，实用价值高。LLM 侧 rank/量化偏弱，英语难追上专用 ASR；时间 Transformer 在分离任务上强、英语上未必最优，融合策略需按任务选型。


# Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

- 论文编号：3002
- 报告人：Daigo Takizawa
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/takizawa26_interspeech.pdf

## 问题
基于神经音频编解码器（NAC）离散 token 的 SSL 更省存储与算力，但语言敏感性来自 NAC 还是 SSL 预训练尚不清楚；若每语需重训 NAC 则削弱效率优势。

## 方法
控制实验解耦：RQ1 在 NAC 重建波形上做 ASR/SER；RQ2 固定 NAC、变 SSL 预训练语；RQ3 固定 SSL 与下游语一致、变 NAC 训练语。英/日/中，DAC 等公开 NAC；codec-based HuBERT（冻结 NAC 码本嵌入求和作输入）。用相对波形基线的 CoV 度量跨语变异。

## 实验与结果
RQ1：DAC 最稳，重训语（EN+/JP/ZH/All）对重建下游影响有限（ASR CoV 约 2%）。RQ2：SSL 预训练语与下游对齐显著更好，错配则 ASR/SER 大幅变差（CoV 可达 37–43%）。RQ3：SSL 对齐后更换 NAC 训练语差异小，不必按目标语重训声学 NAC。

## 结论
下游主要敏感于 SSL 预训练语言，而非 NAC 训练语言；可跨语复用单一声学 NAC，但 SSL 预训练语应与目标语对齐。

## 点评
把编解码器与 SSL 阶段拆开做因果式对照，结论对工程选路很清晰。范围限于英日中与声学型 DAC；语义型编解码器、更多语种与任务是否同样不敏感仍待验证。


# SuTRA: Structurally-Unified Tokenization with Root Awareness

- 论文编号：291
- 报告人：Vaibhav Rathore
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rathore26_interspeech.pdf

## 问题
BPE 等子词优化压缩却忽略形态；印地语系等富形态语言以 akshara（辅音+matra）为书写原子，频率合并常切断词根与词缀（Morphological Shattering），并导致语义难恢复（Semantic Blindness）。现有形态数据集对印地语系边界标注不足。

## 方法
SuTRA 两阶段：预分词用正字规则把词绑成 akshara 单元，并用金标准词典或字符级 seq2seq 标出禁止跨越的形态边界；训练阶段在 BPE 式合并中用得分 S(a,b)=f(a,b)·Ψ(a,b)^γ_t，其中 Ψ=1−冲突次数/频次，γ_t 从高到低退火（先保词根、后挂词缀）。另构建 Hindi/Marathi/Gujarati 约 56 万词 LLM 核验形态切分金标准（IndicCorp + 规则分解 + Gemini 核验），表面边界保证可拼接还原。

## 实验与结果
形态对齐 Boundary F1：SuTRA 印地 0.586、马拉地 0.617（均最高），古吉拉特 0.584（接近 Unigram）。语义可恢复性：印地 Linear R² 相对 BPE 约 +34%（0.4464 vs 0.3329）。Hi↔Mr 翻译（3 层 Transformer，共享 32k 词表）：Marathi→Hindi chrF2 38.84、COMET 0.6554 最优；反向接近最强基线；摘要称平均 +8.08 chrF2。扰动稳健性上 Jaccard 高、Root-Affected 近零，优于纯统计分词。

## 结论
用轻量形态先验约束频率合并，可降低 Morphological Shattering，使整词语义更易从子词线性恢复，并提升翻译与扰动稳健性，而不显著推高 fertility/词表规模；未来可扩到其他富形态语言及 TTS/ASR。

## 点评
关键不是换更大模型，而是在词汇学习目标里显式惩罚跨词素合并，并保住 akshara 原子性。金标准依赖 LLM 核验，边界质量会传导到合并惩罚；对 Sandhi 强融合与词典外词仍依赖 seq2seq 推断，可能是主要误差源。虽放在 ASR 相关会场，正文实验以文本分词与 MT 为主。


# Measuring the Redundancy of Decoder Layers in SpeechLLMs

- 论文编号：1873
- 报告人：Adel Moumen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/moumen26_interspeech.pdf

## 问题
SpeechLLM 中 LLM 解码器常占 >90% 参数，语音任务是否真需要全部深度？冗余能否跨任务复用尚未系统刻画。

## 方法
SLAM 框架：WavLM Large + MLP 投影 + Qwen2.5 / Llama 系列（1–8B）。用层间角距离找最优连续可删块；剪枝后对接收层 MLP 加 LoRA，并可选解冻投影做 healing。在 ASR（LibriSpeech、Loquacious）上量化可剪比例（相对 WER≤0.25），再迁移到 CoVoST2 AST（En→De、Fr→En，Whisper 编码器）。

## 实验与结果
文本与语音角距离热图几乎一致，冗余主要继承自预训练 LLM；深层更可删。联合 decoder+projector healing 远优于只修一侧。7–8B 可删约 28–44% 层仍保持可接受 ASR（约保留 ~60% 解码层）；更小模型可删比例更低。AST 可删约 32%，且 ASR 最优剪枝路径几乎可直接用于 AST。Llama3.1-8B 删 40% 层约 35% 加速、显存 15.72→10.37 GiB。

## 结论
解码器冗余大体模态与任务无关；可基于文本前向定剪枝路径，用单剪枝骨干加适配器服务多任务，降低计算成本。

## 点评
用角距离 + 局部 healing 把“多余容量”测清楚，并显示跨 ASR/AST 路径可迁移，对压缩部署很有启发。阈值依赖相对退化阈值；LoRA 微调解码器反降可剪性；更多家族、语种与推理类任务仍待覆盖。


# Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models

- 论文编号：1767
- 报告人：Yuan Li
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26aa_interspeech.pdf

## 问题
无监督域适应中伪标签噪声大；仅靠置信度易受过置信误导，且丢弃不确定区域会造成边界监督不足。

## 方法
WMR²L：用最大置信度与非最大类残差离散度共同定义 token 权重（utterance 内标准化 + 高斯核），可靠 token 满权。弱置信掩码：对高权 token 以概率 r 将损失乘 λ 而非硬删，促从不可靠区恢复。多扰动一致性（时频掩码、随机裁剪缩放、均衡等）算 S=l·平均 WER，保留一致性最好的 τ 比例样本作伪标签。在 Whisper-medium 上微调。

## 实验与结果
相对 Whisper 基线相对 WER 降：CHiME-4 noisy 约 13.8%、SLURP 25.0%、CORAAL accented 15.7%；WMR²L+MP 全面优于 Confidence/Margin/Entropy+MP、STAR、Beam/Sample 等。CoVoST2 爱沙尼亚/印尼/威尔士翻译 BLEU 亦提升。Large-v3 上同样有效。消融：弱掩码优于强掩码/无掩码；m-r-eq 扰动组合最佳。

## 结论
置信度–残差可靠性加权 + 弱掩码 + 语音多扰动过滤，可提升跨域 ASR 与语音翻译的伪标签利用与泛化。

## 点评
针对过置信与选择性伪标偏差，用残差离散度与弱掩码补监督，思路细。滤波在伪标生成时只做一次，迭代自训动态未充分讨论；超参（α、r、λ、τ）与扰动组合对口音/噪声域可能需重调。


# Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition

- 论文编号：3465
- 报告人：Tung X. Nguyen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26i_interspeech.pdf

## 问题
语码转换（CS）错误集中在嵌入语与切换边界（POI）；标准微调缺少针对这些易混片段的显式信号。

## 方法
CS-NMG：用冻结种子 ASR 的 N-best 定位 POI，仅替换 POI 构造 near-miss，并用 LLM（Gemini）离线扩展替换候选；经声学边际、音素距离、文本距离三层门控保留“难但合理”负例。Whisper-small + LoRA：POI 加权 CE（WCE）锚损失 + 多负例 InfoNCE 式对比排序（长度归一化分数）。推理仍为标准 ASR。

## 实验与结果
CS-FLEURS cmn-eng 与 ViMedCSS vie-eng：WCE+CL（tri-level）相对 CE 约降 2+ 点 WER/PIER（如 cmn-eng 16.67/17.25→14.06/15.10；vie-eng 24.72/21.95→21.87/18.74），优于 WCE、MWER 与仅 N-best 负例。消融：LLM 扩候选需门控才稳定；三层门控整体最优（约 3.8 NM/utt）。

## 结论
面向 POI 的 near-miss 对比训练比单纯上权 POI token 更能抑制跨语混淆，在总体 WER 与 PIER 上一致改进且无增推理模块。

## 点评
把偏好对齐落到声学合理的局部负例，切中 CS 错误分布。依赖外部 LLM API 与 prompt，离线成本与可复现性是短板；目前两语对、单骨干，门控阈值跨脚本迁移需谨慎。

