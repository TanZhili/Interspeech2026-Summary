# Queer and Trans Speech Science and Technology

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Special Session
- Area：14
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特别场把酷儿与跨性别语音科学/技术置于包容性数据、参与式治理、合成人格偏见与辅助发声技术主权等交叉议题。数据集审计显示主流语音库可测量的酷儿表征极低，并与社群参与式采集之间的价值冲突形成张力分类；同时提出面向边缘社群的参与式策展概念框架。

合成与评测侧揭示商业性化合成人声如何通过嗓音编码并放大性别权力不对称；零样本 TTS 对性别扩展嗓音的人类评分与自动指标常冲突，暴露评测盲区。资源建设包括跨男性态度与语音语料、达罗毗荼语跨性别/同性恋仇恨语音数据集，以及澳大利亚英语男性 f0 与性取向/男性气质取向关系的社会语音学研究。辅助技术则从性别扩展 SGD 用户的生活经验出发，强调嗓音主权与定制权。

## 论文技术总结

# Queer inclusion in speech datasets: An audit and taxonomy of practical tensions

- 论文编号：2904
- 报告人：Brooklyn Sheppard
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheppard26_interspeech.pdf

## 问题
语音技术数据集中 LGBTQIA+（queer）声音是否充分、可测？缺失会加剧下游不公，但敏感身份采集又伴随再识别与误用风险。

## 方法
审计六类多样化语音数据集的性别/身份标注与可测 queer 表征；另审计两套由、为、与 queer 社区共建的语音科学数据作对照。归纳 AI/语音技术惯常采集规范与参与式社区价值之间的张力。

## 实验与结果
六套通用数据集中可测 queer 表征仅约 0–1.4% 说话人，不足以稳健做差距测量。社区共建数据集在标注与参与设计上明显不同。提出四类实践张力的分类法（如规模/效率惯例 vs 安全、同意、参与式治理等）。

## 结论
当前主流语音数据 queer 表征过低；纳入边缘社区需正视采集惯例与社区价值冲突，分类法可指导更负责任的数据实践。

## 点评
用审计量化“看不见”的缺口，并把问题从“缺数据”推进到“为什么难收、该如何收”。不提供捷径式采集清单，而是张力框架——对负责任数据集设计更有用。正文若个别表数字模糊，仍以摘要区间 0–1.4% 为准。


# Sexualised synthetic personas encode and amplify gendered power asymmetries through voice

- 论文编号：2411
- 报告人：Ariadna Sanchez
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ross26b_interspeech.pdf

## 问题
商业 Voice AI（以 ElevenLabs Voice Library 为例）把“flirty / temptress”等性化人设与男/女编码声音一起出售；看似男女人设对等，但听众是否仍按刻板权力关系解读这些声音，尚不清楚。

## 方法
从 Feminist HCI 出发做听力实验：从平台选性化（flirt/flirty/temptress）与中性（informative/presenter/educational）的最热门男/女编码人设，分别合成平台脚本性化文本与 Rainbow Passage 片段。北美英语听者（Prolific，按性别与吸引对象分四组，共约 120 人）对每段选三个形容词（正/负、支配/顺从、性化等标签），并可写自由评论；辅以均值 F0 与语速声学分析，并用混合效应模型检验声音性别、文本类型与听者群体效应。

## 实验与结果
男编码声音更常获 dominant（p<.001）与 positive（p=0.0027）形容词；女编码更常获 submissive 与 sexualised（均 p<.001）。性化文本下女/男性化形容词占比约 57%/46%，换 Rainbow 文本后降至 36%/18%，表明文本对男声影响更大，女声的气声、叹息等副语言特征仍推动性化解读。仅吸引女性的男性听者更倾向给性化女声性化词、更少负面词。性化男声均值 F0（70.08 Hz）低于信息男声（110.88 Hz）；性化声音语速更慢（约 2.4 vs 3.8 音节核/秒）。定性评论显示女声常被指夸张、刻板、uncomfortable。

## 结论
平台性化人设呈现狭窄的二元异性恋吸引力图式：女声被听成更顺从、更性化，男声更正面、更支配；即便文本相同，女声风格仍强化该不对称。作者认为此类“创意”预设忽视酷儿/跨性别表征，且表演中难以看到真人的能动与收益。

## 点评
把商品化 TTS 人设放进态度形容词与内容–风格解耦设计里，直接钉住“平台声称性别对等、听感是否对等”。强在把权力不对称落到可统计的听感标签与声学差异上；弱在刺激来自单一平台、人设与提示词高度预设，外推到其他 Voice AI 产品需谨慎。


# Lived Experiences of Power and Agency: Achieving Voice Sovereignty in Assistive Speech Technology for Nonbinary Users

- 论文编号：2663
- 报告人：Juliana Francis
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hope26_interspeech.pdf

## 问题
性别扩展群体中的 SGD（speech-generating device）使用者处于残疾与性别边缘交叉处；既有工作多盯“声音是否够性别肯定”，较少问用户对声音的权力、能动以及更广义的身份对齐。

## 方法
招募 3 名成年非二元 SGD 用户，间隔一周完成两次开放式 Google Forms 问卷（首轮含人口与设备使用；次轮在日常反思后补充）。问题覆盖日常设备使用、挑战情境、预演/脚本、身份表达限制与声音定制愿望。对回答做归纳主题分析，并区分促进因素与障碍。

## 实验与结果
抽出三大主题：(1) SGD 融入日常（身体/认知情绪/社会）；(2) 身份表达（广义、性别、方言地理）；(3) 横切的权力与能动。用户常把设备随身、依赖脚本与理解自己的伙伴，但在嘈杂/潮湿环境、疲劳、被催促、不被接受 AAC 的场合受阻。声音选择常牺牲身份换可懂度；明确希望更多性别中性/queer、“gender weird”及地域口音选项。能动方面强调“Its my voice and i want the power”、多声音随时切换；障碍包括物流速度、他人不等待与安全感。

## 结论
即便样本很小，质性证据表明 SGD 既能扩展表达，也在技术与社会层面限制主权。作者提出 voice sovereignty（定义、控制并施行自己声音的权威），呼吁后续以完整参与式行动研究让用户进入设计与评估，并指出当代 TTS 在技术上已能支持许多需求，但辅助场景仍缺身份中心的评测与部署实践。

## 点评
把能动/权力/主权从性别肯定的单一轴拉开，落到“可懂度优先”“被催促”“想要 uncanny valley”等具体日常摩擦，对 SGD 设计问题设定很有用。三人样本适合开题需求评估，不适合量化推广；讨论里对 SOTA TTS 能力的映射是展望性的，正文并未用这些系统做用户实测。


# TMASC: Transmasculine Attitude and Speech Corpus

- 论文编号：2637
- 报告人：Sidney Wong
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wong26_interspeech.pdf

## 问题
跨男性（transmasculine）语音健康研究相对跨女性不足，常默认睾酮替代治疗（TRT）降 f0 即足够；临床问卷又难与声学对照，也缺少社区尺度而非个体诊断的基准。

## 方法
介绍众包多模态语料 TMASC：2017 年 7–10 月在线招募，经伦理审批；196 份问卷（约 60 题，覆盖自我感知、沟通因素、睾酮史、干预与人口学），其中 66 人另录咳嗽/清嗓、自选语言的 North Wind and the Sun 朗读及是否绑胸等。数据经 LaBB-CAT 采集，匿名问卷与声学放在 OSF（需注册）。用例用 Praat/REAPER 提 mean/mode f0，展示自我感知、社区基准与工具校准。

## 实验与结果
被试以 22–37.5 岁、欧美/英语或德语区居多；朗读英语 50、德语 16。自我感知“声音阳刚度”与 mean f0 仅弱线性关系，而声音满意度与 mean f0 关系更线性；满意者密度峰多在 100 Hz 以下，部分满意者呈约 100 Hz 与 130 Hz 双峰。校准上 Praat 中位 f0 137.8 Hz、均值 150.7 Hz（88.2–489 Hz），REAPER 均值约 114–119.1 Hz（78–185 Hz），显著更低。

## 结论
TMASC 不是诊断工具，而是提供感知+声学的社区资源与众包建库路径；存在非纵向、非实验室录音、英语问卷偏倚与地理覆盖局限，但证明可低成本建立社区适宜基准。

## 点评
把“跨男性语音不等于降 f0”落到可复用的问卷–声学配对与工具差异警示，对临床与社语音学研究都有基建价值。用例偏探索可视化，众包音质与选择偏倚会限制直接当金标准用。


# No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices

- 论文编号：709
- 报告人：Juliana Francis
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/francis26_interspeech.pdf

## 问题
性别扩展（GE）声音在训练数据中稀缺，零样本 TTS 克隆与自动评测是否对 GE 与非 GE（N-GE）表现不公，且自动指标是否与人听一致，尚不清楚。

## 方法
评测 CosyVoice2、E2TTS、F5TTS、XTTS、Zonos、LinaSpeech。N-GE 取 Globe（美式英语、男/女各半，共 14 人）；GE 取 MAGES（自我认同标签，14 人）。每人约 10 秒参考音，合成 15 句 Harvard sentences（16 kHz，-20 dB）。16 名听者做类 MUSHRA 相似度（0–100；每数据集 4 说话人×3 轮）。自动侧：ECAPA-TDNN / TitaNet-L / ReDimNet-M 说话人相似度、UTMOS 与微调 wav2vec2 的 AMOS、Whisper WER，并算 ICC。

## 实验与结果
人听：E2TTS、F5TTS、CosyVoice2 的 GE 相似度显著高于 N-GE；XTTS、LinaSpeech 则 GE 显著更差（效应量更大，如 LinaSpeech d=.704）；ZONOS 无显著差异。说话人相似度与 AMOS 在模型间常互相矛盾，且常与人听不一致（如 UTMOS 对所有模型都判 N-GE 更好；ZONOS 上三套嵌入结论互斥）。WER 仅 LinaSpeech 的 GE 显著更高。作者推测读语音训练与 spontaneity/EMILIA 类数据差异可能部分解释表现分裂。

## 结论
零样本 TTS 对 GE 的人听表现因模型而异，但自动评测管道存在盲区；需要更多代表数据与更贴合人听的指标，且建库须以社区参与、隐私与同意为先。

## 点评
同时打“合成偏置”和“评测器偏置”，对把嵌入相似度/AMOS 当 GE 公平性金标准的做法很有警示力。说话人仅各 14、人听子集更小，结论是方向性证据而非全面排行；Globe 的性别标签部分由分类器补全，也会污染 N-GE 对照。


# The First Dravidian Speech Datasets for Transphobic and Homophobic Hate Speech: Creation, Annotation, and Multimodal Benchmarking

- 论文编号：2368
- 报告人：Jesin James
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lakshmi26_interspeech.pdf

## 问题
泰卢固语与马拉雅拉姆语等达罗毗荼低资源语言中，针对 LGBTQIA+ 的仇恨检测几乎全是文本；缺少可捕捉语气、音高、韵律等副语言线索的标注语音数据。

## 方法
构建两类语料：Elicited Speech（母语者朗读社交媒体上整理的恐同/恐跨/中性句，16 kHz/16-bit）与 Social Media Audio Extract（YouTube/Instagram 公开片段人工裁剪标注）。三名母语者标注 {Homophobia, Transphobia, None}，Cohen’s κ 约 0.78（Telugu）/0.77（Malayalam）。基线：语言专用 Wav2Vec 2.0 均值池化声学嵌入 + Whisper 转写后 IndicBERTv2 [CLS] 文本嵌入，线性投到 768-D，注意力加权融合后经双分支多尺度分类器做三分类；并与 speech-only、text-only 对比。

## 实验与结果
Elicited：Telugu 630、Malayalam 269；Social：Telugu 73、Malayalam 100。同域（Config 1）多模态 F1：Malayalam 0.9566、Telugu 0.8652；跨域测社交音频（Config 2）降至 0.4721 / 0.5907；混合（Config 3）部分回升。同域多模态优于单模态（如 Malayalam 相对 speech-only +8.7%、text-only +15.2%）；跨域时 text-only 更稳，多模态甚至低于文本（Malayalam 文本相对多模态约 +50.4%），显示声学对噪声/俚语/ASR 误差更敏感。

## 结论
首次提供 Telugu/Malayalam 恐同恐跨语音数据集并给出多模态基线：同域强、跨域弱。局限含说话人偏少且偏男性、社交样本平台偏倚与噪声；需域适应与更鲁棒融合。

## 点评
把“副语言对仇恨识别有用”和“读稿到真实音频会崩”同时用同域/跨域拆开，对部署很诚实。社交集规模小，跨域数字波动大；仇恨内容敏感，公开释放需严格治理。


# Masculinity and Sexual Orientation as Predictors of f0 Variation in the Speech of Australian English Speaking Men

- 论文编号：1906
- 报告人：Timothy Shea
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shea26_interspeech.pdf

## 问题
男性性取向（SO）与传统男性气质取向如何影响基频相关变量，在澳大利亚英语（AusE）中几乎未系统检验；既有文献对 local f0、动态性与音域结论也不一致。

## 方法
77 名 AusE 男性（全澳中小学教育；18–52 岁，均值 30.4；gay 27、straight 38、其他 12 后并入 gay/bi+）。一对一图片描述任务：前六张中性、后三张 LGBTQ 主题；录音 44.1 kHz。问卷含人口学与 8 项 Male Roles Attitude Scale（MRAS）均值 z 分数。MacReaper 估 10 ms local f0；以 ≥200 ms 停顿切 utterance，算每隔第 5 个估计点的 |Δf0|（动态性）与 utterance 内 f0 range。线性混合效应模型，简化含 SO、MRAS、年龄组（≤30 / >30）、话题的交互。

## 实验与结果
Local f0：仅年龄显著，>30 约低 7.3 Hz；SO 与 MRAS 不显著。f0 differences：>30 组 MRAS 越高动态性越低；年龄×SO、话题×SO 交互显著——gay/bi+ 在 LGBTQ 话题比中性话题动态性更高（post-hoc p=0.005），straight 无此话题效应。f0 range：仅话题×SO 显著，gay/bi+ 在 LGBTQ 话题音域更大（p<.001），straight 无差异。

## 结论
AusE 男性 speech 中 local f0 不受 SO/男性气质态度驱动；动态性与音域的效应嵌在年龄与话题交互中，说明 gay/bi+ 说话人会在 LGBTQ 话题上扩展表达性，而非单一“更高音高”共同体。

## 点评
把 SO、霸权男性气质态度与话题风格转移放进同一模型，避免把“听起来更 gay”简化成均值 f0。效应依赖交互与年龄二分，对个体预测力有限；图片描述任务也未必覆盖自然会话中的立场转换。


# Towards participatory speech dataset curation: A queer case study and conceptual framework

- 论文编号：2908
- 报告人：Brooklyn Sheppard
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheppard26b_interspeech.pdf

## 问题
语音数据常靠众包扩规模，但对酷儿等边缘群体易成短期“参与清洗”；性别标注可能 outing，且历史上存在 “gaydar”、内容审核误伤等 AI 伤害，社区对开发者信任不足。

## 方法
以酷儿社区为案例综述：常见采集与标注实践的不适配、参与式 AI（如 PARQAIR-MH）、敏感语音伦理（神经障碍语料）、StammerTalk 共创口吃数据，以及田野语言学双向知识共享。据此提出面向边缘社区的概念框架，强调共设计与双向过程，而非单向研究员→产出流水线。

## 实验与结果
本文为概念框架文，无新实验数字。框架四阶段可循环嵌套：(1) Community——谁被服务、谁被排除；(2) Project formulation——语体类型、公开与否与允许用途、存储与撤销/维护；(3) Modes of participation——协作方式、录音/标注/组织等角色、致谢与署名；(4) Personal autonomy——共识点与个人选择、对贡献使用与身份披露的控制。对比图示传统自上而下与共设计双向迭代。

## 结论
参与应尽早进入数据集策展；框架作规范性治理基础设施而非硬性清单，帮助语音研究者与边缘社区共同定义目标、风险与能动。

## 点评
把“要更多酷儿数据”改写成“如何在不加剧伤害的前提下共创数据”，对 ASR/合成公平性讨论补了治理层。正文抽取在个人自主一节末尾截断，细节问题清单的完整收束需对照 PDF；框架尚未在本文用一次真实建库闭环验证。

