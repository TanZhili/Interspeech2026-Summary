# Assistive Technologies 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：13
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕听力辅助、人工耳蜗仿真、耳语转换、聋人/重听用户视角、EMG 无声语音、构音障碍 ASR、双参考评测、个性化联邦学习，以及听声/想象语音的共享神经表征。

听力技术从“适应声学环境”走向用可穿戴设备估计现实世界聆听努力与疲劳；耳蜗侧既有随机神经响应的 DNN 近似，也有共振峰对声码语音可懂度相对重要性的实验。

无障碍与病理语音侧，耳语到正常语音强调低资源下对齐与生成解耦；构音障碍 ASR 在重度低可懂度、联邦个性化与“字面 vs 意图”双参考评测上同时推进。立场论文则强调聋人口音与可验证、公平的设计框架。

脑—机与无声接口方面，EMG 静默语音会自发形成音位表征；单被试 EEG 语料用于检验听觉感知与“内心语音”在音素级的对应。

## 论文技术总结

# Steps toward a wearable-informed model of real-world listening effort and fatigue among adults with hearing loss

- 论文编号：2022
- 报告人：David Meng
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/meng26e_interspeech.pdf

## 问题
听力损失者常有听努力与听相关疲劳，助听器算法多只适应声学、不适应用户当下状态；实验室生理指标难反映日常复杂性。

## 方法
46 名轻–中度感音神经性听力损失成人（助听器使用者与非使用者各 23）完成 7–10 天实地研究：Apple Watch 自发起 EMA（不存原始音频，仅提声级、过零率、谱/混响等特征）+ 被动心率/HRV，以及早晚手机问卷（睡眠、日疲劳等）。用可穿戴与声学特征做二分类：高听努力 vs 非高；日疲劳（≥6）vs 非疲劳。

## 实验与结果
无定时提示下日均约 3 次打卡，与既往手机 EMA 相当。听努力：RUSBoost 在 70/30 划分上 recall 92.6%、F1 84.6%；LOPOCV 中 13/25 合格被试 F1>70%。疲劳：Random Forest 准确率 76.2%（显著高于随机）；重要特征含打卡平均 A 计权声级、日最高心率、REM+深睡时长等。LOPOCV 疲劳准确率均值约 63.5%。助听与非助听组疲劳等多数指标无显著组间差。

## 结论
消费级可穿戴结合 EMA 可在真实生活中可行地刻画听努力与疲劳，有望支持未来自适应助听与纵向监测；全文 5 级刻度回归仍难，需二值化才达可用分类性能。

## 点评
把“用户状态感知助听”落到可落地的手表 EMA+隐私友好声学特征，接受度证据有价值。二值化与被试间变异大说明日常标签噪声与个体基线是瓶颈；助听组打卡声级略高的趋势提示策略差异，尚需更大样本验证。


# Towards a Stochastic DNN Approximation of Cochlear Implant Auditory Models

- 论文编号：1872
- 报告人：Theresa Hartmann
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/hartmann26_interspeech.pdf

## 问题
CI 听神经模型可仿真电刺激诱发响应，但计算重；现有 DNN 近似多为确定性、忽略放电随机性，可能削弱时间编码与不同刺激模式比较的可信度。

## 方法
用层次 VQ-VAE-2（约 2.37M 参数）将 Greenwood 谱图映射到每时频 bin 的 Gamma 分布参数（形状 k、尺度 θ），采样近似平均发放率神经图。训练数据含语音/噪声/音乐共 9000 段（每段 10 个随机神经图）；参考模型为 SpecRes 16 电极 + 40 CF×50 纤维。损失为 Gamma NLL + 指数 MSE + VQ commitment。用 JSD 与 NSIM 评分布与结构相似度。

## 实验与结果
DNN 能再现神经图整体时频谱结构与关键随机特性，低频与中频更好；示例显示近似神经图略更噪。客观 JSD/NSIM 表明全局结构与随机性捕获有效，相对全听觉模型更省时，适合大规模仿真。

## 结论
随机 DNN 近似是高效逼近电刺激听神经模型的可行一步，尤其利于保留变异性而非仅平均响应。

## 点评
用可微 Gamma 替代泊松采样，把“随机性”真正写进近似目标，比纯均值回归更贴合 CI 生理。VQ 层次结构利于粗细尺度；高/极高频与噪声细节仍可能是短板，且评测以客观相似度为主、未接下游听感/算法优化闭环。


# WhisperVC: Decoupled Cross-Domain Alignment and Speech Generation for Low-Resource Whisper-to-Normal Conversion

- 论文编号：2002
- 报告人：Dong Liu
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/liu26o_interspeech.pdf

## 问题
耳语缺声带激励、谱形与时序与正常语音差异大，并行耳语–正常数据稀缺；单阶段同时学对齐、音色与生成易不稳，通用 VC 直接用于耳语可懂度崩坏。

## 方法
三阶段 WhisperVC：(1) 配对数据上 Whisper-large V3 内容编码器 + 双编码器 Conformer VAE，soft-DTW 把耳语特征对齐到正常空间；(2) 仅正常语音上 Length–Channel Aligner、说话人条件粗 mel 生成器 + OT-CFM 残差细化，门控路由使正常输入可跳过对齐；(3) 在预测 mel 上微调 HiFi-GAN。主评 AISHELL6-Whisper（约 30h）；英语另用 wTIMIT 对齐 + LibriTTS 生成。

## 实验与结果
AISHELL6：DNSMOS ovrl 3.07、UTMOS 2.83、CER 16.93%、WavLM 相似度 0.95。相对耳语输入质量大幅提升；Seed-VC 零样本 CER 46.4%。消融：去 VAE 对齐 CER→40.2%；残差 CFM 优于全 mel CFM；声码器适配再提质量。正常 VC 路径仍可用，门控有助于保内容。

## 结论
解耦跨域对齐与正常语音生成，可在低资源耳语转换上兼顾可懂度与自然度，并统一 W2N 与常规 VC。

## 点评
把“耳语→正常”最难的分布对齐单独做成 VAE+soft-DTW，再在正常空间做粗到细生成，工程上清晰。通用 VC 对照验证了域差。脆弱处是强依赖配对耳语数据与内容编码器微调，跨语/零资源仍难。


# Bridging the Speech AI Accessibility Gap for Deaf and Hard of Hearing People

- 论文编号：3001
- 报告人：Christian Vogler
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/glasser26_interspeech.pdf

## 问题
聋人/听障（DHH）用户常有“聋口音”并依赖语音 AI，但 STT/TTS/STS 多按健听数据训练；许多 DHH 无法充分听清合成输出以自检，文本又丢失韵律与副语言信息，造成可用性与信任缺口。

## 方法
立场论文：三位可发声的聋人手语者基于亲身经验，提出设计框架 UVG（Usability、Verifiability、Graceful Degradation）与 FATE（公平、问责、透明、伦理）。分别分析 STT（聋语音识别差、幻觉风险、多人会议壁垒）、TTS（无法验证情感/韵律、需保留可理解的个人声音身份）、STS（口音重说与手语口译再配音两场景）及数据/隐私/社区边缘化风险。

## 实验与结果
无新模型实验；引用既往：聋音在受限数字识别仍可有约 13% WER，人类可懂度与 ASR 表现相关性弱，商业 ASR 对 DHH 持续欠佳。强调失败时应停止并告知而非幻觉填词。

## 结论
语音 AI 须以 DHH 为中心设计：可非听觉验证、优雅降级、个性化且可理解的声音身份，并避免无社区参与的数据采集与部署。

## 点评
把“听不清就不能验输出”这一常被忽略的可验证性写成一等公民需求，对 TTS/STS 尤其尖锐。UVG+FATE 可作产品清单。作为立场文缺少量化新基线，但场景拆解（混会、口译配音性别/族裔错配）对工程优先级很有指导性。


# Emergence of Phonetic Representations in EMG-based Silent Speech Interfaces

- 论文编号：2499
- 报告人：Guillaume Toussaint
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/toussaint26_interspeech.txt

## 问题
表面 EMG 静默语音接口标注稀缺；不清楚不同任务（合成/识别/音素分类/对比预训练）学到的表征是否含音素信息，以及 SSL 预训练为何对合成帮助有限。

## 方法
在 Gaddy & Klein 单说话人 18.6h EMG–音频数据上，用残差卷积+12 层 Conformer，训练 EMG→mel（MSE）、→音素（CE）、联合、→字符（CTC），以及 emg2vec 对比预训练再微调。用线性探测评估音素可分性与 mel 回归；Wav2Vec2 算合成 WER；UMAP 可视化。

## 实验与结果
联合任务线性探测音素准确率最高（约 84%）；仅 mel 回归也可达约 74–80%（中层更好）。CTC 识别特征亦出现音素簇。对比预训练探测仅约 37–38%，接近随机，UMAP 无音素簇。不含 MSE 的设置合成 WER 大幅变差，说明声学回归损失对可懂合成必不可少；对比预训练对合成/音素探测无实质提升。

## 结论
EMG 模型即使无显式音素监督也会涌现线性可分音素表征；可懂合成依赖声学回归目标；现有对比 SSL 学到的空间与音素/合成需求错位。

## 点评
用线性探测系统拆开“表征里有没有音素”与“下游能不能合成”，解释了此前 SSL 对合成帮助微弱的现象。单说话人设定限制泛化结论；中层比末层更富音素信息对探针层选择有启示。


# Investigating ASR for Low-Intelligibility Dysarthric Speech

- 论文编号：1326
- 报告人：Jun Wang
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kwon26b_interspeech.pdf

## 问题
构音障碍 ASR 研究多用轻–中度、短时数据；重度低可懂度（本例 SIT 可懂度 20.9%）是否可学、以及重度适配能否泛化到其他患者尚不清楚。

## 方法
一名无神动性脑瘫、语速约 37 词/分的英语说话人，约一年家庭录音，本研究用 21.6h（总约 100h）。说话人相关：从零训 BLSTM-HMM；微调 Whisper tiny–medium.en。另做 Whisper-medium 数据量缩放，并在 TORGO 构音障碍说话人上测跨说话人泛化。

## 实验与结果
说话人相关：BLSTM-HMM WER 13.4%；Whisper-medium 微调后测试 WER 10.5%（微调前 63.4%）。训练从 1h→15h，测试 WER 25.40%→10.52%（相对降约 58.6%）。TORGO：重度说话人多数 WER 降 6–12pp，轻度/中度几乎不变；整体均值 45.8%→41.7%（摘要称重度约 +6.4pp 改善且不伤轻中度）。

## 结论
在充足单说话人数据下，重度构音障碍语音含可学结构规律；基于重度数据微调的 Whisper 可改善其他重度说话人而不显著损害轻中度。

## 点评
用超长单说话人重度数据直接挑战“重度太乱学不会”的假设，缩放曲线很有说服力。跨说话人增益主要落在重度，符合选择性迁移叙事。局限是单供体、Whisper 30s 切分，会话/自然对话泛化仍待证。


# What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR

- 论文编号：750
- 报告人：Hawau Olamide Toyin
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/toyin26_interspeech.pdf

## 问题
口吃等非典型语音同时存在 verbatim（含重复/拖长）与 intended（去流利性障碍）两种合法转写；多数评测只用单一参考并奖励“删掉障碍”，混淆用例与模型排序。

## 方法
在 FluencyBank Timestamped（3430 条）上对 11 个开源 ASR（自回归 seq2seq/transducer 与 CTC 族）分别报 isWER 与 vWER；对齐 CASA 临床口吃事件分析事件类型影响。假设：自回归更擅 intended，CTC 更贴声学 verbatim。

## 实验与结果
排序不一致：NVIDIA CTC verbatim 最优（vWER 17.20）但 intended 仅第 5；Canary-1B intended 最优（isWER 13.85）。Whisper-large-v3 intended 第 2、verbatim 第 3。同数据 NVIDIA 族内范式差异支持“训练范式偏向转写风格”。延长最易、多音节/不完整音节重复最难；intended 难“去掉”碎片，verbatim 难“保真”重复。

## 结论
非典型 ASR 必须按用例声明参考类型；自回归偏语义 intended，CTC 偏 verbatim。单参考“最佳”可能对临床或听写场景不公平。

## 点评
把评测伦理问题形式化得很清楚，双参考排名翻转是强证据。同训练集内比较增强了因果解释。尚未微调、仅英语口吃；临床标记转写（特殊 token）路线未纳入同一基准。


# Relative Importance of Formants to the Intelligibility of Vocoded Speech in Cochlear Implant Simulation

- 论文编号：143
- 报告人：Ying Cai
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/cai26_interspeech.pdf

## 问题
CI 处理器频谱分辨率有限；共振峰对可懂度的相对权重在噪声声码器仿真中如何，以及通道数/包络截止频率是否改变该权重，尚缺系统证据。

## 方法
10 名正常听力普通话听者；MHINT 句经 LPC 提 F1–F3 轨迹生成正弦波语音，再设保留两共振峰条件（去掉 F1/F2/F3 之一）。噪声声码器：N=4/8，包络截止 100/200 Hz，另含宽带对照。单耳耳机听辨，报正确词率。

## 实验与结果
宽带：三共振峰 97.2%；去 F3→85.7%，去 F1→50.7%，去 F2→31.4%，F2 贡献最大。N=8、截止 200/100 Hz 时仍是去 F2 伤害最大。N=4、截止 200 Hz 时去 F1 伤害最大，说明通道数可改变相对重要性。声码化整体降低识别率，但共振峰排序模式与参数交互。

## 结论
CI 仿真下 F2 通常最关键、F3 最弱，与宽带结果一致；但声码器参数（尤其少通道）可重排权重，提示处理器设计应优先保住关键共振峰信息。

## 点评
用稀疏正弦波语音干净剥离共振峰贡献，再叠声码器参数，对 CI 策略有直接启示。听者均为正常听力仿真，真实 CI 用户与噪声/混响场景外推需谨慎；仅测普通话句子。


# Towards Personalized Federated Learning for Dysarthric Speech Recognition

- 论文编号：1559
- 报告人：Tao Zhong
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zhong26d_interspeech.pdf

## 问题
构音障碍 ASR 隐私敏感，适合联邦学习；但说话人异质性强，强制共享同一全局模型次优，面向构音障碍的个性化联邦聚合研究不足。

## 方法
基于 HuBERT 的 FL-ASR：模型拆成说话人无关（SI）与说话人相关（SD）部分。SI 用标准数量加权 FedAvg；SD 用说话人相似度加权聚合——(1) 参数更新余弦相似度；(2) SI 输出 embedding（每轮用随机私有子集）相似度。与数量加权混合，超参 β 平衡。在 UASpeech、TORGO 上对比正则化 FedAvg 等。

## 实验与结果
相对正则化 FedAvg，提出方法取得统计显著 WER 下降：UASpeech 最高绝对 0.99%（相对 3.15%），TORGO 最高绝对 0.56%（相对 4.73%）。个性化相似度聚合优于仅共享全局模型。

## 结论
相似说话人邻域引导的 SD 聚合可在联邦设置下个性化构音障碍 ASR，缓解异质负干扰并兼顾隐私。

## 点评
把“临床相近说话人应互拉、不相近应隔离”写进聚合权重，比盲目全局平均更贴构音障碍异质性。embedding 用随机子集兼顾隐私。增益绝对值不大，但对难任务仍有意义；客户端规模与通信轮次细节依赖完整实验设定。


# Shared Phone-Level Neural Representations of Auditory Perception and ‘Inner Voice’ Production: One-to-One Mapping using a Single-Subject EEG Corpus of Heard and Imagined Natural Speech

- 论文编号：2683
- 报告人：Scott Wellington
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/wellington26_interspeech.pdf

## 问题
想象语音脑机接口缺大规模、时间对齐的自然句表面 EEG；听感知与“内心语音”在音素级是否共享表征不清楚，限制非侵入 AAC 解码策略。

## 方法
发布 CHINS：单被试 BioSemi 64 通道 EEG，听与想象柯南道尔有声书句子各 >10.5h（合计约 21h22m），词级时间对齐字幕引导想象节奏。对 CMU 39 音素提取听/想象 ERP；在 18 个频带子带上比较向量距离，并用凸二次优化学习子带加权以强化听–想象一一对应。

## 实验与结果
想象音素 ERP 在向量空间上通常最接近对应听音素 ERP，支持音素级共享加工。优化子带加权可进一步改善该一对一映射。数据与范式公开。

## 结论
“内心语音”具有可测的音素级神经相关；大规模单被试听–想象对齐语料可为想象语音神经假体提供方向。

## 点评
用自然连贯句而非孤立词、并强制时间对齐，直接对准 AAC 需求。单专家被试降低疲劳但限制群体外推；表面 EEG SNR 仍低，距离分析是表征证据而非端到端解码演示。

