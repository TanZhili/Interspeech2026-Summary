# Speech and Language Technologies in Healthcare

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：13
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖急诊分诊对话仿真、临床访谈转写隐私与角色归因、急救电话情感分诊假设检验、手术机器人语音指令安全识别，以及构音障碍修复/评估、口吃检测与老年语音零样本在线自适应。共同主题是：医疗场景不能只看通用 WER，而要保全否定、情态与时间线索，控制误识别导致的不安全动作，并在数据受监管限制时用结构化 EHR 驱动对话仿真。

临床可及性方面，构音障碍工作引入共振峰引导的显式谱空间校正再合成；口吃则用多实例学习从片段级标签推断帧级，或以自注意力权重特征做跨语零样本检测；老年 ASR 用跨话语音—文提示实现零样本在线说话人自适应。评估上，DIALOG-DeID 提出 speaker-attributed WER 与 Qualifier/Temporal Preservation 等超越 WER 的指标；法语急救电话研究则提示元数据可能比情感特征更能预测优先级。整体上，本场强调安全、可审计语义线索与跨说话人/跨语鲁棒。

## 论文技术总结

# TriageSim: A Conversational Emergency Triage Simulation Framework from Structured Electronic Health Records

- 论文编号：819
- 报告人：Dipankar Srirag
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/srirag26_interspeech.pdf

## 问题
急诊分诊依赖短时口语互动，但隐私与监管使真实护患多轮对话与音频难以公开；现有临床数据多为结构化结果或事后笔记，诊断向模拟也缺少音频、声学变异与明确分诊决策框架。

## 方法
TriageSim：以 MIMIC-IV-ED 与 ESI Handbook、ETEK 教学案例为种子临床状态；用 Gemini/GPT 等生成患者与护士 persona（口音、不流畅率、风险容忍、指南遵守等）。多智能体：dialogue master 持有真值并响应生命体征查询；护士 agent 按 ATS 或 ESI 算法提问/查体征/做分诊并记录红旗；患者 agent 仅知主诉与疼痛等。对话后做短语边界标注，按国籍/性别从声库取样，用 Qwen-3-TTS 零样本克隆，再混入 ESC-50 环境音（固定相对增益）。代码已公开。

## 实验与结果
生成约 814 段对话（~26 小时，四级口音）。患者不流畅可控：意图与实测 Spearman ρ=0.57。护士行为：经验与信心单调相关；低风险容忍略增过度分诊（0.40）；严格指南遵守平均查体征 2.88 次。声学：整体 WER=10.8（Whisper-Large-V3-Turbo），护士 5.7、患者 16.0；说话人一致性 99.98；UTMOSv2≈3.42。医学保真：专家盲评 50 段，主诉嵌入余弦相似 0.83，红旗检测 P/R=0.94/0.96。分诊分类二次加权 κ：合成文本/ASR/音频上均仅 fair（如 ATS 文本均值约 0.33），模态间差距小。

## 结论
框架能从结构化 EHR 生成临床连贯、交互稳定且带可控语言/行为/声学变异的分诊对话；下游分诊分类难，瓶颈更在会话临床推理而非转写噪声。

## 点评
贡献在于把分诊协议写进 agent 策略并同时交付文本+音频，评测覆盖语言、行为、声学与医学保真，比纯文本角色扮演更贴近语音研究需求。合成数据上的高红旗一致性可能偏乐观；分类 κ 偏低也提醒：有了对齐语料仍不等于自动分诊已可部署。


# DIALOG DeID: Role and Privacy Aware Transcription for Clinical Interviews Beyond WER

- 论文编号：1489
- 报告人：Dominic Dwyer
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/oliveira26_interspeech.pdf

## 问题
精神病学等双人临床访谈里，“谁说了什么”以及否定、情态/不确定、时间锚点等词面线索直接影响评分；传统 WER/DER 无法刻画误归属与意义关键线索丢失，且需在 IRB 约束下做转写去标识。现有工具分散，缺少统一、可审计流水线。

## 方法
DIALOG-DeID：可配置段级表示上串联 ASR（WhisperX/Amazon/Azure/Google）、diarization（如 pyannote）、LLM 角色映射（clinician vs interviewee）、文本 DeID（Presidio / LLM span / 云 API），并可选下游 PSYCHS 严重度回归。评测除 WER、DER 外提出：(i) 置换不变流对齐的 speaker/role-attributed sWER；(ii) Qualifier/Temporal Preservation F1（QTP-F1），用固定词表检查否定/情态/时间线索类型是否在对应流中保留。另做 1.5× 变速相对 WER、语义审计（线索丢失与硬否定翻转）、DeID span F1，以及在去标识角色标注转写上用词数与线索密度的 ridge 回归拟合 PSYCHS 复合分（LOSO）。

## 实验与结果
PSYCHS-Bench：25 段英文学术访谈 10 分钟片段；AMI 作重叠压力测试。固定 pyannote 时 Amazon 最佳：WER 13.3±1.4、sWER 33.1±6.7、QTP-F1 0.88；其他后端 WER 相近但 sWER 可高至 40+。WER 与 sWER 中等相关（ρ=0.55），与 QTP-F1 弱相关。审计：Amazon/WhisperX 线索丢失 20%/24%，硬否定翻转 2%/4%。1.5× 时 WhisperX RTF 0.06 但 WERrel 20.0，Amazon RTF 0.18、WERrel 12.29。DeID 上 Presidio 在姓名/日期等类别 F1 较强。11 会话子集回归：RMSE=3.84、CCC=0.44、Spearman ρ=0.53。

## 结论
聚合 WER 会掩盖归属错误与线索丢失；角色感知保真与 QTP 监控应作为一等指标。隐私处理后的转写仍可保留一定临床可评分信号。局限：临床样本量小、无声学匿名、QTP-F1 仅为词面代理、未充分分解 diarization/角色映射误差。

## 点评
工作把临床转写评测从“字对不对”推到“归属与否定/时间线索是否还在”，指标设计可审计、与访谈评分逻辑对齐。弱点是 QTP 不建模辖域与改写，sWER 仍受 diarization 瓶颈主导；小样本可行性回归不能外推为可靠自动评分。


# Revisiting Emotion-Based Triage: Evidence from French Emergency Call Data

- 论文编号：1265
- 报告人：Elio Stasica
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stasica26_interspeech.pdf

## 问题
文献常假设语音情感可直接反映急诊电话医疗紧急度，但多为模拟数据、情感分类准确率作终点，且优先级标签未必对齐真实调度方案，也未区分患者本人与第三方来电者。情感 alone 是否对临床优先级有增量信息仍缺实证。

## 方法
SAMU54 真实呼叫：每优先级随机 50 通，共 250 通（P3/P2 SNP/P2 AMU/P1/P0）。DiariZen 说话人分离后人工校对，拼接主说话人片段。分类情感：Lajavaness（Wav2Vec，五类：pleased/relaxed/neutral/sad/tense）；维量情感：SpeechDimEmo 帧级 arousal/valence 取中位数。用比例优势序次逻辑回归，经 AIC 选型：模型1 Priority~Emotion+Speaker Role+Age+Sex；模型2 含 Valence、Arousal、角色、年龄、性别及 Arousal×角色、Valence×Arousal。并检验分类情感能否由维量预测。

## 实验与结果
分类与维量表征对齐弱。模型1：年龄（β=0.035, p<0.001）与来电角色（家属/其他/医护相对患者均显著升高优先级）显著；各情感相对 Neutral 不显著；relaxed 从未被预测。模型2：年龄、男性、角色主效应显著；arousal/valence 主效应不显著；Arousal×Other（β=-1.00, p=0.024）与 Arousal×Valence（β=-0.24, p=0.036）显著；分层显示家属来电中更高 arousal 反而关联更低优先级。排除 P0 后 arousal/valence 主效应仍不显著。元数据整体比情感 alone 更具预测力。

## 结论
在真实法文 ECC、调度员标注优先级上，分类情感在纳入元数据后无增量；维量情感存在角色依赖交互，但情感 alone 是弱代理。作者质疑纯情感分诊路线，建议更大样本与临床 grounding 后再谈部署。

## 点评
价值在于用真实呼叫与专业优先级标签直接检验文献默认假设，并显式建模说话人角色——这解释了为何“紧张=紧急”可能不成立。样本每级仅 50、P0 几乎无患者本人说话，因果解释需谨慎；依赖现成法语 SER 也可能把模型偏差带入回归。


# Surgical-Robot Command Spotting: Safety-Aware Learning for Compositional Commands

- 论文编号：3372
- 报告人：Jaewon Lee
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26y_interspeech.pdf

## 问题
手术室语音控制助手机器人需在口罩与 OR 噪声下把短指令映射为结构化动作；误识可导致不安全运动。多数指令是“方向 × 步数(1–5)或连续运动”的组合，再加少量功能指令。把 51 类合成指令当独立分类会忽略组合结构，且 softmax 对“五步↔四步”与“五步↔一步”同等惩罚，不利于抑制灾难性大步误差。

## 方法
轻量共享编码器（2D conv stem + 1D depthwise-separable CNN，输出 24×128）上做头级时间注意力池化，分别预测方向、模式（function/step/continuous）与步幅。步幅用 CORAL 序次回归（阈值化二分类解码）；仅对 step 模式样本计步幅损失；训练期加 51 类辅助头稳定表示，推理去掉。英语 Google Speech Commands v2 预训练编码器后再在韩语 OR 指令上微调。输入 40-bin log-mel。

## 实验与结果
韩语 OR 指令集：5 说话人、7140 句、Clean/Noise×Mask/No-mask，LOSO。完整模型联合成功 95.36%，步指令 MAE 0.0338、灾难误差 CSE（|Δ|≥3）0.60%；优于 Flat-51（93.14%）、BC-ResNet-6（93.65%）及无 CORAL/无头级注意力变体。去掉预训练降至 88.97%。四条件下联合成功约 94.9–96.2%。模型约 181K 参数、5.99M MACs/2s。

## 结论
因子化+序次步幅学习在未见说话人与口罩/噪声条件下兼顾成功率与安全向步幅误差。局限：说话人少、评测为预切 2s 片段而非流式、噪声为回放重录，外推到真实 OR 流式闭环仍受限。

## 点评
把安全关键从“分类对不对”细化到“大步是否灾难”，CORAL 与 CSE/MAE 指标设计对齐手术控制风险。弱点是 5 人 LOSO 方差大（难说话人可拉低）、封闭词表与预切片段简化了真正始终在线检测与拒识问题。


# Formant-Guided Speech Repair for Enhanced Comprehension of Dysarthric Speech

- 论文编号：1217
- 报告人：Xin-Yu Chen
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26n_interspeech.pdf

## 问题
构音障碍严重损害可懂度；VC 对重度病例可懂度提升有限，TTS 管线又常损失韵律/身份。多数神经重建黑箱忽略元音共振峰等感知关键线索，且多在英语孤立词上评测，对汉语与跨病理泛化不足。

## 方法
模块化修复：构音障碍适配 ASR（冻结 Wav2Vec2.0 + Conformer + RNN 解码，CTC/CE 混合）→ FAST（共振峰对齐频谱变换）→ 说话人自适应 TTS（XTTS v2，仅微调 speaker encoder）。FAST：MFA 得 phone 边界，Praat 估 F1/F2，相对 AISHELL-1（汉语）或 TORGO 健康对照（英语）按元音类与性别参考计算偏差，用 α 控制高斯加权频谱扭曲幅度，再 iSTFT 与后处理。TTS 以 FAST 校正语音作条件与音色参考，并结合 ASR 文本。

## 实验与结果
数据：CDSD、MDSC、MSDM（汉语）、TORGO（英语）。主库 CDSD 上 CER 由输入 80.97% 降至 Full 22.33%（相对降约 72.4%）；MDSC/MSDM/TORGO Full 分别为 38.44/34.50/15.42。优于 DiffDSR、RnV、Liu 等基线，并在 CDSD/MDSC 上优于 Oracle TTS（真值文本）。消融去掉 FAST 或 SPK 约恶化 4–7 个绝对点。主观（18 听者，CDSD）：可懂度/理解/流畅约 2.3→4.4+，听努力 3.81→1.49（降约 60.9%）。κ=2.0 时 VSA 约升 10.6%、FCR 降低。

## 结论
显式共振峰校正再合成可同时提升可懂度与自然度，且文本正确 alone 不足以修复塌缩的声学实现。局限包括级联 ASR 错误传播与说话人相似度相对输入略降的可懂度–身份权衡。

## 点评
把临床“元音空间塌缩”写成可解释的频谱扭曲，并与 ASR–TTS 级联衔接，消融与 VSA/FCR 证据链较完整。脆弱处在于依赖 ASR/对齐质量与健康语料参考均值，重度非典型共振峰或对齐失败时 α 校正可能错向；跨语言泛化仍依赖语言特定参考。


# Stuttering Classification and Segmentation with Attention-Based Multiple Instance Learning

- 论文编号：1091
- 报告人：Petar Sušac
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/susac26_interspeech.pdf

## 问题
口吃严重度评估（如 SSI-4、SES）需要不流畅段时长，但多数数据集只有 clip 级多标签，不便帧级分割。现有 MIL 口吃方法多为 instance+max pooling，且常依赖合成不流畅预训练；embedding+注意力 MIL 尚未用于多标签口吃分类。

## 方法
以 wav2vec2-large / wavlm-large / whisper-medium 为骨干，HConv 聚合多层，经 BiLSTM（4×512）与投影后：(1) instance 头 + max pooling；(2) Ilse 式 MIL 注意力池化 + bag 分类头。训练仅用 clip 标签（加权 BCE，含标注者一致性权重）；帧级推理时 instance 模型去掉 max pooling，embedding 模型对正例用 softmax 前注意力权重+sigmoid。先冻骨干再解冻微调。

## 实验与结果
训练 SEP-28k-E；clip 级 FluencyBank 交叉评测；帧级用 FluencyBank CASA gold（732 段不流畅）。SEP-28k-E 多标签上 Whisper/WavLM 变体在 Block/Sound/Word/Interjection 等达 SOTA 级 F1（如表 1 Whisper+attn：Bl 0.35、Wd 0.78、Int 0.82）。FluencyBank 单标签：Whisper+attn F1 0.90，优于 Shih 等 0.85。帧级：Whisper+attn F1 0.70，相对 YOLO-Stutter 0.47、StutterCut 0.45 约提升 23%+（摘要所述）；注意力变体优于同骨干 max pool。长时 block 因 3s 窗仍困难。

## 结论
仅用 clip 级弱监督即可做零样本式帧级分割，且注意力 embedding MIL 在帧级召回上更有利。作者称在 SEP-28k-E clip 与 CASA 帧级达 SOTA。

## 点评
把弱监督 MIL 接到多标签口吃并引入注意力可解释权重，切合临床“要时长”需求。评测与基线设定不完全对等（基线常假设 clip 必含不流畅），跨标签体系（SEP-28k vs CASA）只能做单标签聚合；3s 上下文是长 block 的结构性瓶颈。


# Evaluating Zero-Shot Cross-Lingual Stuttering Detection Based on Self-Attention Weights of Temporal Acoustic Vector Sequence

- 论文编号：1886
- 报告人：Genzo Miyahara
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miyahara26_interspeech.pdf

## 问题
口吃事件检测（SED）依赖大规模标注语料，低资源语言难以直接训练；跨语种迁移时，音素/词汇层面的重复与语言相关，而“相似声学模式的重复/延长”结构可能更跨语。需检验何种表征能在零样本跨语设定下保持检测能力。

## 方法
SAWF：对冻结的时序声学向量序列 S 计算 X=SS^T/√d_S（可多层堆叠），将自注意力权重矩阵当“图像”，用改过的 VGG-19（全局平均池化以支持变长）做多标签 SED。骨干对比：源语 ASR 微调 wav2vec2、xlsr-53、Whisper-medium encoder。零样本：英（SEP-28k）、汉（AS-70）、德（KSoF）互训互测，含 Cmn+En→De 多源。

## 实验与结果
单语上 SAWF 与基线互有胜负（英多类更强，汉基线常更强）。零样本多数设定 SAWF 优于 Bayerl 风格基线；Whisper 骨干总体最强，xlsr 在部分重复类较弱。摘要称跨语 F1 可达单语设定的 77–98%。对德：Cmn+En→De 的 Whisper 在词重复 F1 0.40，优于 StutterFuse 的 0.20；在 block/prolongation/sound 等声学主导类仍落后 StutterFuse 约 10–23 点。多源优于单源；En→De 常优于 Cmn→De。

## 结论
SAWF 能降低对语言特定声学细节的依赖，尤其利于词重复等结构类；SOTA StutterFuse 在部分声学类仍领先。多语联合训练可进一步弥补语言距离。

## 点评
把“重复/延长”显式做成时间–时间相似图，归纳偏置清晰，适合跨语零样本。弱点是插话类受 Whisper 训练去 filler 影响、block 仍难，且相对检索增强 SOTA 在声学主导症状上仍有差距——说明结构特征与声学细节需要互补而非替代。


# Phoneme Error and Uncertainty Features for Interpretable Dysarthric Speech Assessment

- 论文编号：1138
- 报告人：Zihan Zhong
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhong26c_interspeech.pdf

## 问题
构音障碍多维感知评估耗时主观；SSL 嵌入强但不透明，WER 过粗且受语言模型偏置，对齐式 GoP 依赖规范音素目标、在病理失配下易偏。需要语句级、可解释、少依赖强制对齐的评估特征。

## 方法
冻结 CTC 音素识别器（wav2vec2-xls-r-300m-timit-phoneme）自由解码，构建 PED（11 维）：6 个相对规范音素（G2P）的错误率（PER、sub/del/ins、PFER、长度比）+ 5 个后验不确定度（EDL 的 evidence/aleatoric/epistemic，及 softmax margin/entropy 均值）。另提训练免费 ME=0.5(1−m)+0.5H。在 SAP 语句级 DAB 评分上做逻辑回归筛查与 Lasso 序次回归；并训深度≤4 决策树做可检查流水线。对比 GoP-maxlogit、Whisper WER、HuBERT Large、Acoustic12。

## 实验与结果
SAP 说话人分层划分（约 11k 有标注样本）。单特征：ME 在四主维平均 AUROC/ρ 约 0.79/0.543，优于 EDL、GoP、PER、WER。全 PED 四主维平均筛查 AUROC 0.80，接近 HuBERT 0.81；PED+Ac12 达 0.83。序次相关上 HuBERT 仍略优（ρ 0.62 vs PED+Ac12 0.59）。去掉不确定度特征 AUROC 从约 0.764 降至 0.694。决策树平均 AUROC 约 0.78，接近逻辑回归。次要嗓音维上 PED alone 较弱，加声学特征后 Harsh Voice 可超 HuBERT。

## 结论
CTC 后验不确定度可作构音失真代理，PED 在筛查上逼近 SSL 且可解释；浅树提供可人工检查路径。更细严重度排序仍受益于高维嵌入。

## 点评
把“过度自信的 CTC 后验”转成临床可用的不确定度探针，并与错误分解并列，解释性与性能的折中设计清楚。依赖 TIMIT 微调音素器与英语 G2P，跨病因/跨语言外推及次要嗓音维仍弱；树深度人为限制以保证可读，非最优精度。


# Decoding while Adapting: Zero-Shot Online Speaker Adaptation via Audio-Textual Prompts for Elderly Speech Recognition

- 论文编号：620
- 报告人：Chengxi Deng
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26_interspeech.pdf

## 问题
老年语音异质性强、数据少、构音与语言能力下降，且切段 ASR 丢失跨句上下文。既有适配常有伪标签批处理延迟，或只做声学/分开建模，缺少跨句音文融合的在线说话人建模。

## 方法
在 LoRA 微调的 Whisper-medium 上：用当前及前几句历史语音嵌入与（训练用真值、推理用贪心解码）历史文本，经 Early/Late/CMF/Dual CMF 等融合后由 Q-Former 压缩为紧凑在线说话人 prompts，拼接到编码器侧，实现“边解码边适配”。多任务损失：ASR CE + 说话人分类 + 与离线 SAT prompts 的 MSE。对比 i/x-vector、ECAPA、仅音频 prompts、批处理 Enc/Enc&Dec prompts 等。

## 实验与结果
DementiaBank Pitt（英 WER）与 JCCOCC MoCA（粤 CER），训练/测试说话人不重叠（零样本）。音文 prompts 相对 SI：绝对 WER/CER 降 0.61%/1.22%（相对 2.99%/4.48%），显著；相对批处理 Enc&Dec prompts 性能可比且 RTF 加速最高约 9.83×。优于 i/x-vector、ECAPA；Dual CMF + 约 3 句历史较优。t-SNE 显示音文 prompts 说话人表征更一致。性能对适配数据量不敏感，异于批处理。

## 结论
跨句音文双模态 prompts 可在低延迟下做未见说话人在线适配，同时刻画老年语音的声学与语言侧缺陷。作者强调相对批处理适配的实时性优势。

## 点评
“decoding while adapting”直接针对老年对话助手的延迟痛点，文本历史补足话题/语言一致性是合理归纳。增益绝对值不大但统计显著，且依赖前序解码质量——早期错误可能污染 prompts；粤语基线从原始 Whisper 极高 CER 起步，LoRA 域适应仍是主贡献，在线适配是增量。

