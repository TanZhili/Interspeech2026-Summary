# Speech Synthesis Evaluation 2

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场讨论合成语音主观/自动评测的偏差、标注成本与任务覆盖：MOS 中的性别评分偏差、无人类标注的训练动力学伪标签、成对比较主动采样、表达性客观化框架、跨口音编解码/TTS MOS 基准，以及多音乐体裁歌唱合成诊断基准。

共同主题是：人类评分并非中性；偏好测试可更灵敏但需智能选对；自动预测器应减少对大规模人类标注的依赖；评测对象从自然度扩展到口音相似性、表达性维度与体裁可分性。

## 论文技术总结

# MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

- 论文编号：67
- 报告人：Wenze Ren
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26_interspeech.pdf

## 问题
MOS 是语音质量金标准，但听者人口学偏差少被系统研究。若男女听者评分标准不同，简单平均会掩盖组间差异，并可能把某种性别的感知标准写进自动 MOS 模型。

## 方法
在 BVCC（含听者/说话人性别元数据）上分析性别差异；基线用 SSL-MOS。提出 gender-aware 架构：共享 SSL 编码器 + Mean Net（总体 MOS）与 Gender Net（条件于抽象二元组嵌入 0/1，不直接喂性别标签），输出 Avg / Male / Female MOS；多任务等权 MSE（L_avg + L_male + L_female）。

## 实验与结果
男性听者评分系统性高于女性（总体 2.988 vs 2.886，Welch t 检验显著）；差距随质量下降而增大（1–2 档差 0.167，4–5 档仅 0.030）。无性别信息的 SSL-MOS 预测更贴近男性 GT（句级 MSE 0.372 vs 女性 0.430）。Gender-MOS 相对 baseline：全听者句级 LCC 0.862 vs 0.853、MSE 0.239 vs 0.290；男性分支 MSE 0.332、女性 0.366，均优于 baseline。

## 结论
MOS 性别偏差是系统性、质量依赖、可学习的；平均标签与其上训练的模型隐含偏男性标准。抽象组嵌入可提升总体与性别特异预测。未来拟做偏差缓解并在更多数据集验证。

## 点评
把听者性别从“标注噪声”升格为可建模结构，并指出简单全局校准不够（差距随质量变），问题抓得准。抽象 0/1 组嵌入既保留基线“性别中立”接口，又逼模型从数据中挖出两组模式，是务实折中。局限是目前仅 BVCC 有完整性别元数据；且“更准预测各组”不等于“更公平的评估标签”，后续仍需明确公平目标（校准、再加权还是报告分组分数）。


# TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation

- 论文编号：449
- 报告人：Natacha Miniconi
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miniconi26_interspeech.pdf

## 问题
主观听测贵、难扩展；有监督 MOS 预测器仍依赖大量人工标注，且跨语言/合成范式泛化差。需要不依赖听者标注、又能服务 TTS 开发（如 checkpoint 选择）的质量信号。

## 方法
TDScore：从零训练 TTS，定期合成并收集中间 checkpoint 音频，用训练迭代 k 与训练 loss 作伪标签；用外部客观质量曲线截断饱和 checkpoint，并加入自然参考句。基于 SSL-MOS 架构，分别训练预测归一化迭代（Ite）与标准化 loss 的模型，用 pairwise ranking（BCE over score differences）。TTS 骨干：FastSpeech 2、FastPitch、F5-TTS，均在 Blizzard 2023 法语 NEB 约 51h 上训练。

## 实验与结果
域内 BC（法）：TDScore–F5–Ite 系统/句级 SRCC 0.74/0.54，优于 DeepFake proxy（0.60/0.50）等无 MOS 方法，并接近/超过部分有监督结果。域外 BVCC：F5–Ite 0.73/0.66；SOMOS：0.38/0.22。迭代预测在自建测试集上最强（F5–Ite 句级 0.90）；loss 预测更不稳，且整体 Ite 优于 Loss。作者归因于 loss 振荡、迭代更能表征学习状态，且 F5 训练中质量提升更平滑。

## 结论
TTS 训练动态，尤其是迭代索引，可作为无人工标注的合成质量伪监督；跨语言仍有差距但优于若干无 MOS 代理。局限是依赖当前 TTS 训练轨迹形态，统一多架构联合训练是未来方向。

## 点评
用“checkpoint 质量单调改善”作免费标签，直接对准开发期需求，比再造一套 MOS 数据更省。Ite 稳、Loss 弱也符合直觉：loss 样本依赖且震荡。脆弱处在于伪标签质量高度依赖“训练过程是否真有可感知递进”——非 F5 架构相关性明显变差，说明方法对生成范式敏感，扩展到任意未来 TTS 前需要更稳的 checkpoint 筛选与多系统联合训练。


# Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation

- 论文编号：446
- 报告人：Korin Richmond
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/valentinibotinhao26_interspeech.pdf

## 问题
偏好类听测（AB、BWS）比 MOS 方差更小、更少量表偏差，但因“必须测全对”的误解采用不足。在听者少、时长紧（如濒危语言 TTS）场景下，需要更高效的系统对采样策略。

## 方法
用 Blizzard 2013 刺激（自然音 + 5 个旧系统 + 4 个神经系统，共 10 系统）先做覆盖尽可能多对/元组的 AB 与 BWS 听测（Prolific，排除后 AB 54 / BWS 57 人）。再从已收集答案库中回放三种采样：随机、merge-rank（MR，含随机/正确初始排序与不同每对最大请求数）、ASAP（信息增益 + batch，每轮 9 对）。BWS 侧对请求对做贪心检索以覆盖 batch。用 TrueSkill 估计分数，报告显著成对差异数与对全量排序的 Kendall 相关。

## 实验与结果
AB 与 BWS 上 ASAP 在显著差分数与排序相关上均最好；MR 因逐对深挖、中间覆盖不全，收敛前显著差更少。按估计听测时长（AB 约 16.9s/题、BWS 约 36.6s/题）对比：同等时长下 BWS 优于 AB，ASAP 再放大差距。实践对照：约 10 人、20 分钟 ASAP-BWS（约 200 听测分钟）约等于 40 人同等时长 AB（约 800 分钟）。

## 结论
ASAP 主动采样能更快揭示系统差异并逼近全量排序；BWS 比 AB 更省时长效率；二者组合适合听者/时长受限的评估设计。

## 点评
用“全覆盖听测作答案银行 + 离线回放采样”干净地比较算法，避开了在线听测噪声。结论对濒危语言等少听者场景很实用。需注意：刺激含明显强弱系统，小间距 SOTA 场景下 ASAP 优势可能更关键（文中亦引用 ASAP 原作者小范围条件结果）；且 BWS 检索不保证请求对一定被 best/worst 命中，信息增益实现依赖工程细节。


# Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment

- 论文编号：2408
- 报告人：Zhiyu Lin
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26l_interspeech.pdf

## 问题
语音到语音（S2S）模型可懂但常缺表现力；主观评分贵，低层声学特征又抓不住感知细微差别。需要把人类对 expressiveness 的偏好对齐成可扩展客观指标，并用于数据筛选与模型改进。

## 方法
DeEAR 四阶段：将表现力拆为 Emotion（wav2vec2 细调 arousal，CNSCED+IEMOCAP）、Prosody（Gemini-2.5-Pro CoT 评分，SRCC=0.73）、Spontaneity（DNSMOS 启发的伪标签 + 对“过干净但朗读感”惩罚，再蒸馏到 wav2vec2）；用约 480 条人工标注、XGBoost 非线性融合三子分；再蒸馏为单一 DeEAR-Base（wav2vec2-xlsr-53 多任务）。应用：按 DeEAR 从开源情感对话语料筛出约 14K 句 ExpressiveSpeech（约 51h），微调 S2S 基座。

## 实验与结果
与专家 MOS：总体 expressiveness PCC/SRCC 0.91/0.85；DNSMOS/UTMOS 反而与表现力负相关。七个 SOTA S2S 基准：DeEAR 与人类排序 SRCC=0.93，Doubao 最高、Qwen2.5-Omni/Gemini 靠后。S2S-FT vs Base：盲听偏好 78.5% vs 10.0%；客观 S_expr 从 2.0 升到 23.4，情绪与自发维度增益最大。

## 结论
少量标注即可得到与人类偏好对齐的多维表现力指标；用其做评估驱动数据策展，能显著提升 S2S 感知表现力。未来拟接入强化学习做端到端优化。

## 点评
把“表现力”拆成可学子任务再非线性融合，比直接回归抽象 MOS 更贴感知瓶颈（一文指出单维短板会卡死总分）。Prosody 依赖 Gemini、Spontaneity 依赖启发式伪标签，可扩展但外部模型与阈值选择会进指标本身；ExpressiveSpeech 顶 15% 阈值经人工审计，说明指标仍需人校准。DNSMOS/UTMOS 与表现力负相关，提醒“干净度指标”不能当表现力代理。


# CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents

- 论文编号：1273
- 报告人：Wen-Chin Huang
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26f_interspeech.pdf

## 问题
神经音频编解码（NAC）与基于其的 LLM-TTS 基准多偏重建质量与客观指标，少主观、少口音等非标准语音。口音相似度如何评、客观指标是否管用、听者口音是否引入偏差，尚缺大规模证据。

## 方法
构建 CodecMOS-Accent：从 VCTK 选 32 说话人、10 口音、160 真值句；9 个重合成 NAC（含低码率配置）+ 15 个开源 voice cloning TTS，共 4,000 样本。众包 25 听者、19,600 标注，三维 5 分：自然度 S-NAT、说话人相似 S-SPK-SIM、口音相似 S-ACC-SIM；并算 O-WER、O-SPK-SIM、O-ACC-SIM、O-UTMOS。

## 实验与结果
真值在 S-NAT 仅排第 9，但说话人/口音相似最高；低层 SpeechTokenizer 仍保留可感说话人与口音线索。系统级：S-SPK-SIM 与 S-ACC-SIM 相关 0.97（句级 0.75）；O-UTMOS 与 S-NAT 相关 0.96；O-SPK-SIM 对 S-ACC-SIM（0.90）甚至高于 O-ACC-SIM（0.81）；O-WER 与主观相关弱。同口音听者对 SPK/ACC（及全数据上的 NAT）给分更高（同口音偏差）。

## 结论
该数据集是作者所知对口音上 NAC/TTS 主观评估规模最大的工作之一；揭示说话人–口音强耦合、客观指标预测力，以及听者口音偏差。拟公开数据并用于训练更好 SQA、尤其口音相似度直接人标监督。

## 点评
把 ICL 式 voice cloning 的“说话人/口音克隆”拆成独立主观维，并系统对比重合成 vs TTS，填补了编解码基准缺主观、缺口音的空白。UTMOS 对 2020 年后系统仍高度相关，提醒“新架构≠绝对质量跃迁”。同口音偏差与听者以美式为主的构成，限制了“普遍自然”结论；口音嵌入指标未必优于说话人嵌入，说明口音客观度量仍需人标驱动。


# MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres

- 论文编号：137
- 报告人：Wenhao Feng
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/feng26_interspeech.pdf

## 问题
歌唱合成（SVS）进步快，但公开数据与评测严重偏流行乐，难系统分析跨流派泛化。流派作为整体风格条件在 SVS 中几乎未被当作一等评测维度。

## 方法
提出 MMGenre：用 Suno V4.5 按层级流派提示生成音乐，Mel-RoFormer 分离人声，STARS 标注音素音高时长，经时长/流派一致性（MuQ-MuLan）过滤与少量人工核验，得到 10 大类、26 子类、3,152 段中文分数–音频对（约 4.36h）。评测 RNN、XiaoiceSing、VISinger/2、DiffSinger、StyleSinger、TCSinger、TechSinger 等；核心指标 GCS-5（Gemini 2.5 Pro 五分流派一致性，与人 Spearman ρ=0.85），辅以 SingMOS 等与 CER。

## 实验与结果
各模型流派剖面高度相似，强对齐集中在 Pop 及相关类，非 Pop（Rock/Rap/Classical 等）普遍低分；合成嵌入跨流派重叠（相对真值可分），呈现“流派坍塌”。零样本风格迁移/技巧控制对 Classical/Rock/Rap 仅小幅抬 GCS-5，远低于 GT。用约 2h Rock 继续训练后 GCS-5 从约 1.5 升至 4.9。整体伪 MOS/CER 仍反映合成质量进步。真/合成 Pop 上模型 MOS 排序相关 ρ=0.90，支持基准相对有效性。

## 结论
MMGenre 提供多流派 SVS 诊断框架；当前模型流派意识强依赖训练分布，而非分数条件可轻松迁移。有限流派专用微调远优于零样本控制。

## 点评
用 T2M 扩流派覆盖是务实数据策略；“坍塌 vs 真值可分 + 微调即大幅回升”把问题钉在数据先验而非符号可控性上，对社区很有诊断价值。GCS-5 依赖 Gemini，且微调后略超 GT 可能含“子类夸张”伪影；中文、AI 生成人声为主，外推到真人多语料库需谨慎，但相对排序在 Pop 验证上已站得住。

