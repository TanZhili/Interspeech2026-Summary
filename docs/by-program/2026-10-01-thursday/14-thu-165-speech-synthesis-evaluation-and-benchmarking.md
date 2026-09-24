# Speech Synthesis Evaluation and Benchmarking

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：7
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场集中质疑并重建 TTS/歌声/笑声合成的评测范式：多音字、音系忠实度、嗓音重建、笑声音素、日语 G2P、情绪嵌入相似度、短语停顿多参考、野外离散 token TTS 的客观 MOS，以及歌曲细粒度维度与自然多语速 STSM、GSLM 码率与带不确定性的 MOS。主线是“好听”不等于音系/任务成功，且许多客观代理在分布外失效。

语言与音系侧，PolyBench 暴露 LLM-TTS 多音准确率天花板；音系分类器审计 ATR 和谐；日语 G2P 显示解析模式优于直出，并惠及假名输入 TTS。任务对齐评测用 BWS 情境框架与双参考分布度量服务嗓音重建；笑声合成比较自动/人工音素标注与 SPSS vs audio-LLM。

客观指标批判贯穿：情绪嵌入相似度易奖励声学模仿；野外离散 TTS 上 UT-MOSv2 等相关性崩塌；DNSMOS 对加性噪声与生成伪影的惩罚与听感矛盾。SongBench、GRATS、GSLM 码率消融与 ConformalMOS 分别补细粒度诊断、真实语速参考、低码率可行性与区间覆盖保证。

## 论文技术总结

# PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation

- 论文编号：998
- 报告人：Feifan Chen
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lu26_interspeech.pdf

## 问题
LLM-TTS 直接吃文本、多音字消歧隐式完成，ASR 的 CER/WER 难抓发音错；既有中文多音字评测集存在标注错误、覆盖不足与领域偏斜。

## 方法
构建 PolyBench：从《现代汉语词典》第 7 版筛出 494 个高频多音字与 88 个多音词，DeepSeek 生成句子并人工校对，得 Main（6016 句，含 Common/Surname/Dialectal/Colloquial/Literary）、DictWords（2137 词）与 ALLinONE（494 句、同句多读）。用 Qwen3-Omni-Instruct 自动标发音（ALLinONE 上标注准确率 93.06%，接近人工）。评测 3 个 G2P 与 17 个 LLM-TTS，指标 CER、Poly-CharAcc、Poly-PyAcc。

## 实验与结果
Main 上 FireRedTTS-2 最佳，Poly-PyAcc 82.02%（Common 86.01%），仍有约 18% 错读；方言/口语类全面偏低。CharAcc 系统间差约 4%，PyAcc 差约 15%，且 PyAcc 常低于 CharAcc 10–20 个百分点。DictWords 上多数更高、系统差距更大；ALLinONE 上最优也仅 202/494 字全对。G2PW 在姓氏/文言类仍有竞争力。

## 结论
PolyBench 暴露当前 LLM-TTS 多音字消歧仍不足，尤其方言与口语；Qwen3-Omni 可作大规模自动标注器。未来拟扩大字表并改进拼音标注。

## 点评
把“能认出字 ≠ 读对音”拆成 CharAcc/PyAcc，击中 LLM-TTS 评测盲区。自动标注误差会扰动绝对值，但大差距排名仍可用；口语类与词典标音本就不一致时，低分可能混入标注定义问题。


# Towards a Phonology-Informed Evaluation of Multilingual TTS

- 论文编号：3311
- 报告人：Neeraj Kumar Sharma
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/raybarman26_interspeech.pdf

## 问题
MOS 等自然度指标不检验语言特有音系对立；阿萨姆语 ATR 元音和谐由语法决定共现，TTS 可能“好听”却中和或错放和谐条件对比。

## 方法
用 14 名母语者录音（8125 元音 token）建人类基准，提取 Lobanov 归一化 F1–F3、B1、时长及高度/前后特征；Meta MMS TTS（mms-tts-asm）合成同载体句（281 token）。Task 1：LR/RF 做跨域 ATR 分类（H→H、H→TTS 等）。Faithfulness audit：比金标 ATR 与分类器预测，区分 overgeneration（−→+）与 underproduction（+→−）。Task 2：词级三分类和谐类型，用声学聚合与金标/预测 ATR 序列特征。

## 实验与结果
LR 的 H→H 与 H→TTS 准确率均约 82%，宏 F1 0.81；RF 域内更高但迁移落差大。TTS 错配率 0.16，但 underproduction:overgeneration≈7:1（人类近对称）；[+ATR] 中元音 /e/、/o/ 约 1/3 token 被判为 [−ATR]。词级上 H→TTS 时 A+B_pred（宏 F1 0.62）优于 A+B_gold（0.49），说明声学 ATR 轮廓与意图音系不一致。

## 结论
MMS 对中元音 [+ATR] 声学线索系统性 underproduce；框架可推广到其他有可测声学线索的音系对立，但本文仅单系统、单现象、TTS 样本小且类别不平衡。

## 点评
把“听感尚可”与“音系忠实”拆开，用人类训练分类器当声学探针，比 MOS 更对准语法条件对立。结论强度受 TTS token 少（尤其 AgrNoMixYes）与类不平衡约束；方向性偏置比总错配率更有诊断价值。


# An Evaluation Framework for Text-to-Speech Voice Reconstruction

- 论文编号：2600
- 报告人：Ariadna Sanchez
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanchez26_interspeech.pdf

## 问题
语音重建需在提升可懂度的同时保留说话人身份，却无“病前真值”；常用 MOS 自然度/相似度敏感度与可靠性不足，客观指标与听感是否对齐也未充分验证。

## 方法
主观：情境化 Best Worst Scaling，分 INTELLIGIBILITY（只评可懂度）与 RECONSTRUCTION（同时考虑可懂度与想象中的病前身份）。客观：WER/PER、WeSpeaker 余弦相似度、UTMOS，以及双参考 TTSDS2——对高可懂 LibriTTS 子集与 SAP 乱序参考分别打分，再取 TTSDSMean 刻画折中。用 17 个零样本克隆 TTS，在 SAP 193 名英语母语障碍说话人（帕金森等，高/低可懂按 WER 30% 划分）上各生成 1 句。

## 实验与结果
全体说话人：INTELLIGIBILITY 上多数 TTS 高于原录音（StyleTTS2 等领先）；RECONSTRUCTION 上多数低于录音，IndexTTS2、Qwen3-TTS、E2-TTS 领先。低可懂子集上几乎所有系统可懂度更好，但 RECONSTRUCTION 仅 IndexTTS2、Qwen3-TTS 高于录音。客观上 WER/PER/UTMOS/TTSDS|LibriTTS 与 INTELLIGIBILITY 强相关；RECONSTRUCTION 上 Spk.Sim. ρ≈0.75，TTSDSMean 更高（全体 0.81，低可懂 0.73）。

## 结论
情境化 BWS 与双参考分布度量比通用 MOS/单指标更能对齐语音重建任务；零样本系统在严重障碍上仍难同时保身份与提可懂度。

## 点评
把“听得清”和“还是本人”拆成两套听测与一套均值分布分数，直接打中重建折中。数据偏帕金森与高可懂；客观相关是系统级排序相关，不等于样本级诊断。听者想象“病前声音”本身主观，框架对更重障碍会更吃力。


# Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis

- 论文编号：2141
- 报告人：Hiroki Mori
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mori26_interspeech.pdf

## 问题
情境化笑声合成依赖笑声 phone 标注，人工成本高；既有自动识别数据少、未见说话人弱，且识别误差对合成质量的影响未系统验证；音频 LLM 路线是否还需要 phone 标注也不清楚。

## 方法
在 AGSC/OGVC 上新建 11 说话人笑声集，用改进的 XLSR-53 framewise+d 识别器（含时长后处理）。合成对比：SPSS（BiLSTM 参数语音合成，显式用 phone）与 Fish-Speech（音频 LLM，prompt）。条件含 ManualLabel、AutoLabel、AutoLabel+（SPSS 增广）、NoLabel。听测评自然度 MOS 与“笑法/个体性” SMOS。

## 实验与结果
未见说话人：PBE 23.0 ms，替换/删除/插入约 30%/14%/7%，辅特征错 15%，优于先前未见结果。自然度：Fish（约 3.5–3.6）高于 SPSS（Manual 2.71，Auto 2.51，NoLabel 1.62）。笑法相似度：SPSS Manual 3.94 ≫ Auto 3.46 ≫ Fish（约 2.5）；个体性 SPSS Manual 也更高。Fish 上有无 phone 差异不显著；SPSS 上自动标注明显弱于人工。

## 结论
自动标注对未见说话人已可用但仍不足以匹配人工；Fish 自然度好但笑法可控性弱，SPSS 相反——尚无同时兼得的单系统。

## 点评
把“识别准不准”落到合成听感三条轴上，比只报 PBE 更贴应用。自动–人工标注风格不一致可能放大 AutoLabel 劣势；Fish 的 LoL prompt 实验说明 token 模型对笑声结构仍缺显式控制杆。


# Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study

- 论文编号：1800
- 报告人：Tomoki Koriyama
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/koriyama26_interspeech.pdf

## 问题
日语 G2P 需分词、多音汉字与数词–量词不规则读法；端到端 TTS 隐含学读音但可控性与稳健性不足。LLM 是否能替代传统形态分析器，以及何种调用方式更稳，尚缺大规模基准。

## 方法
两种模式：parse——LLM 做形态分析并输出各词假名，再规则后处理助词读法与长音规范化；direct——LLM 一步输出整句假名。在 JVS nonpara30 的 3000 句人工假名标注上算 kana CER；评测 30+ 专有/开源 LLM 与 OpenJTalk、MeCab 等传统工具。另将 LLM 假名喂入 LoRA 微调的假名输入 CosyVoice 2，与 E2E TTS 比发音 CER 与 UTMOS。

## 实验与结果
Claude Opus 4.6 parse CER 0.52%、Gemini 3.1 Pro direct 0.53%，优于最佳传统工具 OpenJTalk 1.03%。多数模型 parse 优于 direct；规模与日语持续预训练（Swallow）显著降错。假名 TTS：Gemini 3.1 Pro 假名 CER 2.38%（oracle 2.10%），低于 Gemini 2.5 Flash TTS 等 E2E（3.96%+），UTMOS 相当。

## 结论
强 LLM + 规则后处理可超传统日语 G2P；显式 G2P 再假名合成在发音准确上优于直接文本 E2E，且不明显损自然度。

## 点评
把“难规则”留给确定性后处理、把分词与读音估计留给 LLM，是务实的工程拆分。小模型 direct 极易崩；parse 在数词–量词切碎时也会引入错误，说明级联并非万能。基准句子来自 JVS，对更野文本泛化仍待验。


# The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation

- 论文编号：39
- 报告人：Yun-Shao Tsai
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tsai26_interspeech.pdf

## 问题
表达性合成与情感 VC 广泛用 emotion2vec 等嵌入的余弦相似度作 EMO-SIM；分类准并不等于零样本相似度可靠，说话人/语言学干扰可能主导距离，从而奖励声学模仿而非情感迁移。

## 方法
对嵌入做均值中心化以缓解各向异性。三类检验：(1) 分类情感三元组（无约束、同说话人同文本、说话人干扰、语言学干扰）；(2) 效价/唤醒的趋势单调性（Spearman ρ）与位移可辨性；(3) 人工偏好对齐（多模型合成候选，Fleiss κ=0.7349，保留 400 个强共识三元组）。另做 emotion2vec 各 Transformer 层探测。对照 emotion2vec/+ 与 HuBERT、Wav2vec 2.0、TERA。

## 实验与结果
同说话人同文本时准确率多仅约 60–70%；语言学干扰下 emotion2vec 在 CREMA-D 可跌至 3.38%，说话人/语言学干扰下常低于随机。位移可辨性近 50%，ρ 近 0。人工对齐约 52–65%，不足以为可靠代理。深层对人类对齐从 L0 约 58% 降到 L7 亚随机约 45%。

## 结论
当前情感嵌入空间不适合零样本 EMO-SIM；高 SER 准确率不能推出可用的情感相似度度量。建议用对比学习等校准抑制非情感声学因素。

## 点评
把“评测指标”本身当成被测对象，用对抗式采样暴露 false resonance，对滥用不加批判的 EMO-SIM 很有杀伤力。均值中心化已尽量抬分辨率，失败更像表征结构问题；尚未给出可替代的成熟指标，实践上仍需谨慎搭配听测。


# LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations

- 论文编号：2225
- 报告人：Hoyeon Lee
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26f_interspeech.pdf

## 问题
短语停顿标注存在一对多合法切分；单参考评测会拒掉与金标不同但仍合理的标注，人工评测又难扩展；直接用 LLM 当裁判捕捉细微韵律差异也有限。

## 方法
提出 LMRE：用 LLM 从少量 few-shot 演示池（与评测参考 disjoint）多次采样生成多参考查找表，保留出现次数超过 Niter/10 的标注；假设标注与任一参考相似度（EM 或 F1）超阈值即接受。韩语测试床含 1356 条标注、五种策略（AP-Only、Comma-IP、音频驱动、文本驱动、合成）与十一配置。

## 实验与结果
可接受组（人工分 4–5）上，单参考相对人工欠接受约 13–27%，LMRE Combined 将差距压到约 7%（分 5 组仅 1.75%）。与人工分相关：Combined† 多参考 F1 达 r=0.621、ρ=0.626，高于单参考（约 0.50）。F1 普遍优于 EM；长句上 EM 增益更明显。小演示池（|PFS|=128）即可泛化到未见句。

## 结论
LMRE 在可扩展自动评测与多参考容忍之间取得折中，比单参考更贴近人工接受行为。

## 点评
把“一对多韵律”落到可复用查找表而非黑盒裁判，确定性与可复现性更好。参考质量仍依赖演示池与 LLM 生成分布；目前验证集中在韩语，跨语迁移需另证。


# Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech

- 论文编号：2203
- 报告人：Shekhar Nayak
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanjotra26_interspeech.pdf

## 问题
UTMOSv2、DNSMOS 等 O-MOS 多在干净/去噪连续语音上训练；对 in-the-wild 离散 token TTS 的生成伪影（幻觉、韵律倒置）可能“听不清但谱面光滑”，客观分与人工自然度可能脱节。

## 方法
四系统对照（文本与说话人固定）：SYS-A StyleTTS 2（连续干净）、SYS-B MQTTS+语义编码器（原始 ITW）、SYS-C 在 A 上加 MUSAN 泡泡噪声且与 B 的 NISQA 对齐、SYS-D 真录音。耳机筛选听测共 768 条自然度评分；评 UTMOSv2、DNSMOS P.835/Pro、PLC-MOS。

## 实验与结果
人工：D>A>B≈C（B/C ΔMOS=0.10，p=0.14）。文件级相关：A 上 UTMOSv2 r=0.51（p<0.01），B 上跌至 −0.01（n.s.）；Steiger 检验确认崩溃显著。DNSMOS 等对加性噪声惩罚更重（OVRL B 3.06 vs C 2.64），与人工等价相悖。B 中 7/32 文件人工 MOS<2.5 但 UTMOSv2>3.8（acoustic camouflage）。

## 结论
在 MQTTS 类 ITW 离散合成上，现行神经 MOS 不宜单独作自然度代理；建议与 ASR WER 等语义指标组合，并建设针对 ITW 生成伪影的指标。

## 点评
用加性–生成配对把“罚错类失真”钉死，比单纯报 OOD 相关下降更有说服力。结论强度受单架构（MQTTS）限制；camouflage 样本说明表面质量指标会主动误导系统排序。


# SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment

- 论文编号：1985
- 报告人：Dapeng Wu
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26h_interspeech.pdf

## 问题
Text-to-Song 评测缺专业粒度；SongEval 等维度语义重叠且分数挤在高分区间，难区分日益接近的顶尖模型。

## 方法
按作曲要素定义七维：Vocal、Instrument、Melody、Structure、Arrangement、Mixing、Musicality（1–10）。用 Hunyuan 生成歌词/提示，收集 Suno 多版本、LeVo、SongBloom、ACE-Step 与真人版权曲等约 2 万样本，经专家校准与过滤得 11717 条标注（约 683.5 小时，中英约半）。以 MuQ 为骨干训自动预测器，并建 352 条外部模型 OOD 集。

## 实验与结果
OOD 上 utterance 级各维 LCC/SRCC 多超 0.78；system 级 LCC>0.95。Musicality 相关显著高于 SongEval。模型对比能拉开 Suno v4.5→v5、MiniMax 等迭代增益，而 SongEval 近乎平台。AB 测试：同模型内判别准确率（LeVo 64%、Suno 62%）明显高于 SongEval（约 43–55%）。

## 结论
SongBench 提供更解耦、更高分辨率的歌曲质量基准与自动评估工具，有助于诊断生成短板。

## 点评
把“好听”拆成可操作的制作维度，直接针对评分压缩与维度纠缠。自动器强依赖专家标签分布；Musicality 仍偏整体审美，与其余六维的独立性需持续监控。


# GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking

- 论文编号：1842
- 报告人：Yu Tsao
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/aghniya26_interspeech.pdf

## 问题
STSM 评测多依赖英语语料或人工变速参考；普通话是声调语言，音高–时长协调敏感，人工缩放无法代表自然语速下的韵律与发音变化。

## 方法
发布 GRATS：25 名说话人、60 句、五档自然录制语速（0.5×/0.75×/1.0×/1.25×/1.5×），共 7500 条平行句、8.1 小时、44.1 kHz；卡拉 OK 式视觉提示控速，无后处理变速。协议：以自然 1.0× 为输入，系统输出与同说话人同句自然目标语速对比。指标含 Whisper CER、PESQ、STOI、DNSMOS、音节时长 MAE、WORLD F0 相关（MFA 对齐）。

## 实验与结果
Phase Vocoder 各档 CER 最低；CLPCNet 等神经法 DNSMOS/STOI 更好，说明可懂度与听感可脱钩。时长 MAE 在 0.5×/1.5× 呈 U 形升高，F0 相关随极端语速下降。实现语速 α 与标称因子总体对齐但仍有自然偏差。

## 结论
自然多语速平行数据使评测对准“是否接近真实目标语速实现”，而非复现确定性缩放；普通话 STSM 需多指标联合解读。

## 点评
把参考从“缩放后的同一条”换成“同文本再录的目标语速”，对声调语言特别关键。局限是朗读、台湾华语；客观指标不能替代音调忠实度听测。


# On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models

- 论文编号：999
- 报告人：Shunsuke Kando
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kando26_interspeech.pdf

## 问题
GSLM 的离散单元序列远长于文本，训练成本高；常规 N=20 ms 设定对语音生成是否冗余、降低码率会否伤重合成与续写，尚缺系统扫描。

## 方法
HuBERT-base 第 9 层特征按 N∈{20…280} ms 分段均值池化，再 K∈{128…16384} 做 K-means（64 种码率）。uLM 为 OPT，训于 LibriSpeech 960 h；u2s 分别为 Tacotron2+PWG 与 VITS（LJSpeech）。评重合成（WER、UTMOS、MCD、LogF0 RMSE）与续写（PPL/VERT、GPT-4.1-mini 成对裁判、MMOS、AB）。

## 实验与结果
重合成：中等 N（40/80）在更低码率下接近 N=20；Tacotron2 更可懂，VITS 声学更好。续写：在 WER<5 且 UTMOS>4 的设定中，N=80–120 大 K 的 LLM 裁判常优于基线；人工 AB 显示 (20,256) 与 (80,4096) 等可竞争。LLM 裁判与 MMOS 的 SRCC 仅 0.323，高于 PPL/VERT 但仍偏低。

## 结论
更低码率仍可支撑可懂重合成与高质量续写，常规高码率对生成任务可能冗余；续写自动指标与人工对齐仍弱。

## 点评
把“理解向”的 N/K 扫描延伸到生成任务，并点出任务最优码率不同（音素保真 vs 语义建模）。评价瓶颈在续写指标——LLM-as-judge 相关性仍低，结论对温度选择与归一化方式敏感。


# ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

- 论文编号：572
- 报告人：Tashfain Ahmed
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/elelu26_interspeech.pdf

## 问题
多数 MOS 预测器只给点估计、无可靠不确定性；人类评分主观且有噪声，部署时难以判断低置信或分布偏移样本。

## 方法
ConformalMOS：冻结上游（M2D2 或 wav2vec）均值池化嵌入 → 两层 MLP 序数头；将 MOS 划为等宽 bin，用高斯平滑软标签训 KL+辅助 L1；再在 10% 校准集上做 split conformal，取残差 (1−α) 分位数为半宽，输出截断到 [1,5] 的区间。

## 实验与结果
BVCC（VoiceMOS 划分）：M2D2 α=0.05 系统级 MSE 0.080、LCC 0.953、SRCC 0.943，优于 FUSE-MOS（MSE 0.086）；句级略弱于 UTMOS。经验覆盖贴近名义水平，校准误差低、区间相对窄；wav2vec 骨干覆盖不足、区间更宽。α 增大则区间变窄、覆盖下降。

## 结论
在交换性假设下可为 MOS 提供有限样本覆盖保证的区间，且不牺牲（甚至提升）系统级点估计；强骨干对校准质量关键。未测跨域，听者分歧建模留作未来工作。

## 点评
把 conformal 接到序数 MOS 头上，比启发式置信更可解释。系统级亮眼、句级仍落后顶尖点估计器；交换性在新 TTS 系统上是否成立是实际部署的硬约束。

