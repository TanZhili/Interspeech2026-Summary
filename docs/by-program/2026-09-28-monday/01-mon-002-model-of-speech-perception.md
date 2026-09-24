# Model of Speech Perception

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral
- Area：1
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从语音感知出发，把人类听者实验与计算模型并置。一侧用 Whisper、Qwen2.5-Omni-7B、Wav2Vec2.0 等神经模型对照 L2 元音知觉训练；另一侧用多层感知机与 Lobanov、Nearey 等归一化在 L2LP 框架下拟合非母语元音范畴。

感知侧还触及 Speech-to-Song 错觉中的音素分布偏差与听音指令模式，以及 informational / modulation / energetic masking 的相互作用如何抬升可懂度。这表明“刺激结构 + 听音任务设定”仍是解释主观现象的关键杠杆。

工程侧则把听感努力（LE）与可懂度（SI）预测推向增强语音、合成语音与双耳场景：PHOBI 与 HASANet+ 在大规模主观评分上给出高相关。另有工作用概率单纯形约束闭合 CLIP/CLAP 类对比模型的 modality gap，把几何先验引入跨模态对齐。

合起来看，本场瓶颈在于：人类实验成本高、归一化选择依赖听者画像、掩蔽机制相互抵消难以单点解释；走向则是把 LLM/多语 ASR、经典语音学归一化、听力学预测模型与几何表示学习放在同一感知问题谱系中比较。

## 论文技术总结

# English Vowel Perceptual Training under Multitalker Babble: A Comparison of Humans and Large Language Models

- 论文编号：966
- 报告人：Wenwei Dong
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dong26b_interspeech.pdf

## 问题
二语（L2）听者对母语中缺失的语音对比感知困难，高变异语音训练（HVPT）在多说话人 babble（MTB）背景下可能有益，但用真人听者逐一试不同 babble 说话人数成本高。此前工作对比了荷兰语 L2 听者与 Wav2Vec2.0 在 2/6 说话人 babble 训练下的元音辨别，但单语模型在 speech-shaped noise（SSN）上远弱于听者。本文问：多语模型（Whisper、speech LLM）能否像听者一样从 MTB 训练中受益、谁的提升趋势更接近听者，以及与测试噪声匹配的训练是否优于 babble。

## 方法
数据与先前听者实验一致：英式单音节词中的 /E/–/æ/ 与 /eI/–/aI/；pre/posttest 各 64 试次（quiet 与 SSN），训练 100 试次；babble 由 2 或 6 名美式英语说话人朗读段落混合而成。70 名荷兰母语者做二选一 HVPT，训练期给纠正反馈，半分到 2/6-talker babble；测时 quiet 与 SSN。模型侧对 Wav2Vec2.0（wav2vec2-base-960h）、Whisper-large-v3、Qwen2.5-Omni-7B 先测预训练表现，再在 2-talker、6-talker、quiet、SSN 四类训练集上微调后复测。指标为选词正确率：Whisper 用识别文本与两选项的编辑距离；LLM 用提示直接二选一，并以 LoRA 微调；Wav2Vec2.0 用强制对齐置信度与 CTC 微调。

## 实验与结果
听者：元音对与 test×背景交互显著；/eI/–/aI/ 优于 /E/–/æ/；quiet 优于 SSN；仅在 SSN 上 posttest 显著高于 pretest（约 +3.44%），2 与 6 talker 训练条件无显著主效应。Quiet 测集上 babble 训练后听者 6-talker 总均提升约 2.59%（不显著）；Wav2Vec2.0 仅在 2-talker 上总均 +4.68%，LLM 在 2/6-talker 上分别 +4.68%/+3.12%，Whisper 近乎天花板无提升。SSN 测集上各方均受益，且 6-talker 优于 2-talker；听者 6-talker 后 /E/–/æ/ 80.89%、/eI/–/aI/ 93.21%；Wav2Vec2.0 与 Whisper 平均多在 70% 以下，LLM 最高平均约 78.12% 与 90.62%，更接近听者。Quiet/SSN 训练：quiet 测集上 quiet 训练三模型均有提升（LLM 总均 +4.68%），SSN 训练仅 LLM 总均 +9.37%；SSN 测集上 quiet 训练使 Wav2Vec2.0 下降 7.81%，Whisper/LLM 分别 +6.25%/+9.37%，SSN 训练使 Whisper 总均提升最大（+28.12%）。

## 结论
多语模型也能从 MTB 训练中受益；在 SSN 上 speech LLM 准确率与听者更接近、趋势更一致，而 Whisper/Wav2Vec2.0 在 quiet 上偏高、SSN 上偏弱。匹配噪声训练可带来更大提升（尤其 Whisper 在 SSN→SSN），但 babble 训练对逼近听者模式仍有参考价值。局限包括 quiet 上的天花板效应、模型与听者测试流程不完全对等，以及抽取文本末尾讨论略有截断。

## 点评
工作把 L2 感知训练条件筛选问题转成可复用的神经模型探针，核心不在刷 ASR 分数，而在看谁在 quiet/SSN 上的相对难度与训练增益像听者。Speech LLM 的提示式二选一更贴近听者任务，LoRA 微调也更像“短时感知适应”；弱点是模型天花板、微调轮数少、以及用识别/编辑距离代理感知判断，可能夸大或扭曲与真人的可比性。


# How Speaker Normalization Procedures Influence the Computational Modelling of Non-native Vowel Perception: Implications for the L2LP model

- 论文编号：1574
- 报告人：Jooyoung Lee
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26l_interspeech.pdf

## 问题
用神经网络建模非母语元音感知时，说话人归一化几乎是必需的，但既有比较多在单语内做；跨语言场景下既要消说话人差异，又要保留 L1–L2 音系间有意义的声学距离（L2LP 假设分离感知语法）。何种归一化最能复现无英语知识的西班牙语听者对美式英语元音的归类，以及这对 L2LP 的 Full Copying 意味着什么，尚不清楚。

## 方法
用 DIMEx100 墨西哥西班牙语五元音（/i,e,a,o,u/）的 F1–F2 中点训练 MLP（2 输入、两层 128 隐单元、5 输出），在六种输入处理下只改归一化：raw Hz、gender-wise Z、Lobanov、Nearey 1/2、Gerstman。为模拟 L1 听者，把从西班牙语样本估计的归一化参数套到 TIMIT 九个美式英语单元音上，得到 5×9 归类概率矩阵，再与 Escudero & Chládková 的真人归类矩阵比 MAE、RMSE、Pearson r、top-1 类别匹配数（/9）。训练/测样本约 123,884 / 14,091；跨语言模拟用 TIMIT 测集 10,825 token。

## 实验与结果
Lobanov 全面最优：MAE 13.93、RMSE 23.30、r=0.75、匹配 7/9；其次多为 Nearey 1 与 gender-wise Z（各 6 匹配）；Gerstman 最差（MAE 25.60、r=0.16、匹配 3）。矩阵上 Lobanov 最接近真人的块对角模式，且是唯一把英语 /u/ 主要映到西班牙语 /u/ 的方法（其余多映到 /o/）。

## 结论
尽管人们担心 Lobanov 会过归一化、抹掉跨语言差异，它反而最贴合“无目标语知识”听者；作者据此把 Full Copying 延伸到 L1 归一化行为本身，并推测随 L2 发展、需保留跨语言对比时 Nearey 类方法可能更合适。局限：仅 F1–F2、MLP 架构较简。全文末尾结论句有抽取截断。

## 点评
核心贡献是把“归一化方法排行榜”绑到明确的听者状态（L2LP 初始态），而不是追求类别可分性最高的那一种。用西班牙语参数去归一化英语输入，是设计上刻意的 L1 滤波器；脆弱点在于真人基线来自合成元音、模型输入只有两个共振峰，且“过归一化=Full Copying”仍是事后解释，需用不同水平学习者数据验证 Nearey 是否随水平上升更优。


# Closing the Modality Gap via Simplex-Constrained Representations

- 论文编号：2849
- 报告人：Shubham Gupta
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gupta26_interspeech.pdf

## 问题
CLIP/CLAP 等对比多模态模型虽对齐配对样本，但模态质心仍系统性分离（modality gap），可能扭曲跨模态相似度；既有办法多改目标或架构。作者问：仅改输出几何——从单位球面到概率单纯形——能否在几乎不动预训练骨干的情况下大幅闭合该间隙且不伤检索。

## 方法
冻结 LAION-CLAP（音–文）与 FLAVA（图–文），加共享轻量 Linear/MLP adapter（可训参数 <1%）。欧氏分支：L2 归一化到球面，用余弦；单纯形分支：同一 adapter 后 softmax 到 ∆^{d−1}，用负 Total Variation 打分。另设 XAttn（共享交叉注意 + 欧氏余弦）对照 ReTreever（同注意机制 + 多分辨率单纯形），以及 MRL 作为欧氏 coarse-to-fine。用对称 in-batch InfoNCE（DPR 式）训练。指标：质心 ℓ₂、silhouette、几何校正 RelGap（质心距/模内散布），检索 NDCG@10。数据：Clotho、SoundDescs、AudioCaps、MS-COCO、Flickr30k。

## 实验与结果
五基准上，把相同 adapter 换成 softmax 单纯形后，质心 ℓ₂ 从约 0.36–0.81 降到约 0.005–0.020（降幅 97–99%），RelGap/silhouette 亦改善，NDCG@10 持平或更好（如 Clotho T2A 0.259→0.382；SoundDescs 上 ReTreever 0.535/0.542）。XAttn 仍保留大间隙，而 ReTreever 显著更小，说明闭合主因是输出几何而非交叉注意。Coarse-to-fine：MRL 间隙随维数增大（AudioCaps 2-d→256-d 约 0.032→0.534），ReTreever 全程 <0.06。估计 Dirichlet α̂ 显示高维单纯形嵌入偏稀疏，间隙仍小，支持“真对齐”而非纯距离尺度假象。

## 结论
单纯形的非负与单位质量和（及 softmax 对全局 logit 平移不变）构成跨模态校准先验，可在不改骨干下闭合 modality gap 并保持检索；共享交叉注意本身不足以消除间隙。单纯形还可启用 JS/Hellinger/KL 等分布相似度。

## 点评
论证干净：同容量 adapter、同注意机制只换输出域，把“几何先验”从架构容量里剥出来。TV 分数与概率预算共享坐标是可解释的机制；脆弱点在于实验全在冻结骨干上微调小头，未见端到端或生成式任务，且 RelGap 虽校正尺度，单纯形稀疏区与球面对“好对齐”的语义是否等价仍依赖检索代理指标。


# Effects of distributional bias in vowels and consonants on the Speech-to-Song Illusion

- 论文编号：2956
- 报告人：Haruki Kagotani
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kagotani26_interspeech.pdf

## 问题
Speech-to-Song（STS）错觉多强调韵律与语义；音段层音素出现分布是否有偏（类似押韵/重复）是否也会增强“听成歌”的程度，以及把评分框架从 song-likeness 换成 rap-likeness 是否改变错觉强度，尚缺直接检验。

## 方法
构造日语约 9 拍短句，2×2：元音偏倚 × 辅音偏倚（Non-bias / Vowel-only / Consonant-only / Both），用 Shannon 熵确认偏倚；辅音按响音 vs 阻塞音操控。40 句由盲于假设的男播音员录制。120 名日语母语者在线听：每试先听一次再评，再重复 10 次（ISI 400 ms）再评；Song 块评 song-likeness，Rap 块评 rap-likeness（7 点），并评主观理解度。指令顺序与刺激集交叉平衡。因变量为重复后减重复前的评分变化；三因素重复测量 ANOVA（Instruction × Vowel Bias × Consonant Bias）。

## 实验与结果
三主效应均显著：Rap 指令变化大于 Song（M=0.95 vs 0.84；F(1,119)=6.20, p=.014）；有元音偏倚 > 无（1.00 vs 0.80）；有辅音偏倚 > 无（0.97 vs 0.82）。仅 Vowel×Consonant 交互显著；简单效应显示 Non-bias 显著低于三种有偏条件（均 p<.001），三种有偏条件之间无显著差异（ps>.10）。Instruction 与偏倚无交互。

## 结论
音段分布偏倚足以增强 STS/STR 式音乐化；元音或辅音单侧偏倚已够，双侧叠加无显著加成。Rap 指令整体抬高变化量，但不特化放大偏倚效应。作者认为 rap 更容忍自然语调波动、更贴近言语节奏。局限：部分刺激语义不连贯；未来需与音高稳定性等韵律指标联合建模。文末 Future Works 有抽取截断。

## 点评
把“押韵式分布偏倚”从语篇直觉落到可操纵的熵控制与 2×2 设计，并把 STS 量表扩到 rap，是对言语–音乐边界研究的有用扩展。弱点是刺激在偏倚最大化下牺牲语义自然度，可能与已知的“低语义合理性促错觉”混杂；且因变量是评分差而非是否发生错觉的阈值判据。


# Deep learning-based predictions of perceived listening effort and intelligibility across enhanced, synthetic, natural, and binaural speech

- 论文编号：1891
- 报告人：Dirk Eike Hoffner
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hoffner26_interspeech.pdf

## 问题
听者实验测 listening effort（LE）与 speech intelligibility（SI）成本高；现有深度感知模型多针对特定任务。能否用原理不同的非侵入式模型 PHOBI 与 HASA-Net+，在双耳空间、助听器式增强、合成语音等训练未必覆盖的条件下同时预测 SI 与 LE。

## 方法
PHOBI：LibriSpeech 上训练的 hybrid ASR 前馈网，丢弃 HMM，用 triphone 后验的 Mean Temporal Distance（时间滞后上的平均 KL）作不确定性代理。HASA-Net+：WavLM-Large + 听力图特征 → BLSTM → 多头注意，教师–学生学 HASPI/HASQI；本文只用 HASPI 支路。三套听测：SI spatial（8 名正常听力，OLSA+SSN，三房间、噪声方位变化测 SRT）；LE enhanced（11 人，AdaptDRC 增强，SSN/CAF，Krueger ESCU 量表）；LE synthetic（23 人，Google TTS 德语句，多种噪声/SNR/空间配置）。LE 用独立 G¨ottinger 句子集做线性映射；SI 用模型心理测量函数取 50% 点作 SRT，双耳用 better-ear（取较高输出）；PHOBI/HASA-Net+ 均可用单参考条件校正偏移。

## 实验与结果
空间 SRT：无回声室相关最高（PHOBI/HASA-Net+ r=0.97/0.94；RMSE 1.0 vs 1.8/4.5 dB 校正/未校正）；办公室 0.91/0.88，食堂 0.94/0.91；PHOBI 平均 RMSE 约低 1.4 dB。LE enhanced：整体 r=0.98（HASA-Net+）与 0.94（PHOBI），RMSE 1.9 vs 1.2 ESCU；多数条件下增强降低实测与预测 LE，但 CAF 在 −10/−15 dB 上模型预测升、主观降。LE synthetic：全局 r≈0.94/0.96，噪声子集内相关更低（HASA-Net+ 0.43–0.75；PHOBI 0.62–0.91）。全文摘要称逾 10,500 条评分、相关总体 >0.88。

## 结论
两模型都能刻画空间释放掩蔽与增强带来的 LE 下降，并对合成语音有较好泛化；PHOBI 平均略优。局限：better-ear 简化双耳整合；嘈杂人声噪声下 PHOBI 难分目标/干扰；噪声簇内主观分差小导致簇内相关偏低。

## 点评
价值在“同一对 SI 代理模型跨 LE/增强/TTS/双耳”的压力测试，而不是提出新骨干。MTD 式不确定性与 HASPI 蒸馏代表两条可迁移路线；脆弱处是 LE 依赖事后线性标定、SRT 依赖参考偏移校正，以及 CAF 负 SNR 上增强方向预测反了，说明干扰语片段仍是盲预测瓶颈。


# Mutual Cancellation between Masking Effects Benefits Speech Intelligibility

- 论文编号：1290
- 报告人：Yixin Gu
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gu26_interspeech.pdf

## 问题
竞争语音带来 informational masking（IM）与 modulation masking（MM），并与 energetic masking（EM）纠缠；既往用全局 SNR 或事后校正难以干净分离。本文在跨语言设置下用高能 glimpse 比例（HEGP）约束 EM，检验语言相似性与调制保留程度如何共同决定可懂度，以及 MM 释放能否抵消 EM 代价。

## 方法
目标为 Harvard 英语句（以 “the” 起首）；竞争语音（CS）为英语同库句或普通话语料拼接摘录。由同一 CS 派生：LPC 阶 50/12/5 的谱–时调制噪声（STM）、Hilbert 包络调制的时间调制噪声（TM）、长时谱平稳噪声（TS）；普通话 TM 用普通话包络乘英语 TS。对每对目标–掩蔽器用自适应调 SNR，使 HEGP=0.3/0.4/0.5（低分=更强 EM），共 2 语言 ×3 EM ×6 掩蔽器=36 条件。25 名正常听力美式英语母语者听 180 句，打字复述目标词，指标 WRR。

## 实验与结果
HEGP↑ → WRR↑；CS 条件 WRR 最低，调制保留减弱时 WRR 渐进上升。0.3/0.4 HEGP 上英/普差异很小；0.5 HEGP 上普通话派生掩蔽器 WRR 56.9%，比英语侧高约 5.6 ppt，且普通话 CS/STM-50 显著优于英语对应条件。相对 CS，高/中 EM 下要到 STM-5 才显著提升；普通话 TM 相对 STM-5 再显著提升，英语 TM 则否。TM vs TS 多数不显著（普通话高 EM 除外）。ANOVA：EM、masker 主效应大，language 小但显著；language×masker 不显著。Glimpse 分析：高能 glimpse 数按设计对齐，非高能/总 glimpse 随调制减弱而减少，解释英语 TM 需更高 SNR 才能达同 HEGP。

## 结论
听者表现是“语言不相似带来的 IM 释放”与“英–英条件下电平线索减弱带来的 IM”之间的相互抵消；降低谱–时/时间调制可释放 MM，甚至在总 glimpse 更少的 TS 上仍可接近 TM，体现 MM 释放对 EM 的抵消。讨论指出 LPC 掩蔽器仍可能可懂，IM 与 MM 难以彻底拆开。正文讨论末尾有抽取截断。

## 点评
用 HEGP 对齐而非固定 SNR，是把“EM 控制”做实的关键设计；跨语言 + 调制梯度让 IM/MM 争论可操作化。脆弱点是 LPC 噪声仍可能残留可懂度、TM/TS 统计差异弱，以及 IM/MM 概念边界作者自己也承认未闭合——结果更适合读作“掩蔽效应相互抵消”的现象证据，而非纯净因果分解。

