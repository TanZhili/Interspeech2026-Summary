# Child Speech and Health

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接儿童语言样本分析、儿童发音障碍检测、自发语音呼吸健康评估、自闭症儿童手势—焦点韵律、儿童口吃自动检测，以及音频语言模型在口吃儿童混合说话人场景下的语义推理。

方法上，临床指标自动化从端到端 LLM 提示转向可分解零样本流水线；病理声学用自编码器嵌入或异构图融合多尺度结构；健康评估尝试从日常自发语音提取呼吸生物标志。发展障碍相关工作同时覆盖多模态手势效应与保留临床上不流畅信息的指令引导 ALM。

## 论文技术总结

# Correct Then Detect: Zero-Shot FVMC Annotation for Child Language Sample Analysis

- 论文编号：2593
- 报告人：Wei Bo
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hou26b_interspeech.pdf

## 问题
Finite Verb Morphology Composite (FVMC) 对识别 Developmental Language Disorder (DLD) 临床有效，但依赖人工标注强制时态语境（正确/错误/省略），无监督语料，端到端 LLM 提示易幻觉。

## 方法
零样本分解：① 受限语法纠错（仅动词形态与省略 be/助动词等）——GECToR 标签受限或 LLM 提示纠错；② 在纠正句上用 Stanza UD 规则检测强制语境；③ 最小编辑距离对齐原文，按替换/插入判定 correct / incorrect / omitted。在 ENNI 儿童叙事（SLP 金标）故事级评测，对比直接 LLM 标注。

## 实验与结果
直接非推理 LLM 很弱；推理模型（如 GPT 5.2-R、Sonnet 4.6-AT）显著提升。提出管道更优：GPT 5.2+Stanza 在 correct/omitted F1 达 97.05%/70.23%；Sonnet 4.5+Stanza 在 incorrect F1 60.15%；相对最强推理 LLM 基线三类分别 +1.99/+4.72/+6.21。纠错用非推理模型即可，成本低于全程推理。

## 结论
据作者称，这是首个实用零样本 FVMC 自动标注管道；任务分解优于端到端 LLM。未来接 ASR、扩展到会话及其他语法指标。

## 点评
把临床规则拆成“纠错 + 句法检测 + 对齐”，让 LLM 只做擅长的受限改写，是临床 NLP 里可复用的范式。incorrect/omitted 仍远低于 correct，类别极不平衡与省略检测难度仍在；仅 ENNI 叙事，会话场景外推未证。纠错范围若漏改/过改会直接污染对齐标签。


# Detection of Incorrect Place of Articulation in Polish Sibilants Using Convolutional Autoencoders

- 论文编号：2624
- 报告人：Wojciech Pieniążek
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pieniazek26_interspeech.pdf

## 问题
儿童齿擦音错误很常见，早期诊断依赖言语治疗师，资源有限。需自动检测波兰语清卷舌擦音/塞擦音 /ʂ/、/tʂ/ 的错误发音部位（尤其齿化相对规范卷舌）。

## 方法
4–8 岁儿童语料（/ʂ/：149 人 1746 次；/tʂ/：151 人 586 次），SLP 标注 PoA；中心麦 44.1 kHz，手切音段→64×64 语谱图。三种卷积自编码器（CAE / SCAE / MTCAE）学潜表示，SVM-RBF 分类；说话人独立 10 折；潜维 d∈{10…30}，类别加权处理失衡。

## 实验与结果
以敏感性为主。/ʂ/ 最佳 MTCAE 敏感性约 81–84%、准确率约 73%；顶尖配置多为 MTCAE/SCAE。/tʂ/ 顶尖十个敏感分类器均为 MTCAE，敏感性最高约 84%。Kruskal-Wallis 显示自编码器类型对性能有显著影响。约三分之二极端超参配置因退化被剔除。

## 结论
自编码器嵌入 + SVM 可在具挑战性的儿童语音上检测错误 PoA；多任务变体整体最有效。为儿科构音辅助筛查提供特征学习路径。

## 点评
小样本、说话人独立、以敏感性优先，设定符合筛查场景；多任务把类别信息压进瓶颈，比纯重构更贴诊断。类别严重失衡、仅二分卷舌 vs 齿化、手切语谱图，限制现场端到端部署；未与端到端 CNN 直接对照，贡献更偏表示学习比较。


# SpiroPhonia: Non-Invasive Respiratory Health Assessment from Spontaneous Speech

- 论文编号：2571
- 报告人：Roksana Khanom
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khanom26_interspeech.pdf

## 问题
COPD 诊断依赖肺量计等临床设施，难连续居家监测。既有语音呼吸研究多靠朗读/持续发声等受控任务；自发对话是否含稳健、受试者无关的呼吸生物标志仍不清楚。

## 方法
SpiroPhonia：从公开访谈等收集英语自发语音，医师核验标签，201 人（102 呼吸疾病 / 99 对照，45–95 岁）。预处理切 10–30s、带通与轻降噪；提声学扰动（F0、jitter/shimmer、HNR、共振峰）、MFCC 统计、停顿时序特征；统计筛选后递归特征选择；可解释分类器（如 Linear SVM、Gradient Boosting）做受试者无关评测，并讨论筛查/端侧配置。

## 实验与结果
多组特征组间显著（如 RAP/DDP jitter、MFCC10、停顿率/每分停顿数）。最佳模型约 78% accuracy、80% F1、87% AUC（摘要）；表中 Linear SVM（5 特征）accuracy 约 78%、AUC 约 79%。作者称与受控录音方法竞争力相当，支持日常语音编码呼吸信息。

## 结论
自发语音可提供紧凑、可解释的 COPD 相关声学–频谱–时序标志，通向语音设备上的被动筛查。数据可应请求用于学术研究。

## 点评
把场景从实验室任务推到野生对话，并强调少特征可解释模型，部署叙事清晰。公开网络数据有选择偏差（谁愿意上镜谈病、录音质量），标签靠内容核验而非统一肺功能金标；与年龄/说话风格混杂需谨慎。适合筛查线索，不宜替代临床诊断。


# Effects of Co-speech Gesture on the Acoustic Realization of Focus in Cantonese-speaking Children With and Without Autism Spectrum Disorder

- 论文编号：1008
- 报告人：Zhuoran Li
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26p_interspeech.pdf

## 问题
伴随手势是否调制焦点的声学实现仍研究不足；ASD 儿童在韵律焦点与手势–语音整合上均有困难，粤语儿童中二者如何交互尚不清。

## 方法
22 名 ASD、25 名典型发展（TD）粤语儿童，操纵指示/意象手势与有无焦点，测目标及前后音节的 mean f0、f0 range、时长；线性混合效应模型 + Tukey 事后比较。

## 实验与结果
意象手势使两组目标音节时长均显著加长。TD 还会缩短后焦点音节时长以强化焦点凸显。ASD：指示手势下目标与后目标音节均缩短；意象手势对非焦点句目标音节扩大 f0 range（两组皆有）；ASD 的 mean f0 对手势无可靠效应，TD 在后目标位置有小幅升高。

## 结论
两组呈现不同手势–韵律耦合：TD 用后焦点压缩强化凸显，ASD 在指示手势下出现手势–韵律权衡式缩短，符合弱中央统合与增强感知功能等对多模态整合困难的解释。

## 点评
把手势类型、焦点位置与临床分组交叉设计，直接检验“手势是否塑造而非仅同步于韵律”。效应量多中小，但方向一致且与理论对齐。样本中等、任务为诱导实验，外推到自然会话需谨慎；声学与手势因果方向仍可能双向。


# Paediatric-HGNN: A Hybrid Heterogeneous Graph Neural Network for Detecting Disfluency in Children’s Speech via Multiscale Acoustic Fusion

- 论文编号：1131
- 报告人：Rashini Liyanarachchi
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liyanarachchi26_interspeech.pdf

## 问题
成人口吃检测模型难迁移到儿童：声学变异大，病理口吃与典型发展性不流畅高度重叠，黑盒模型临床可解释性不足。

## 方法
Paediatric-HGNN（CaPIN）：异构图连接词节点（词汇意图）与帧节点（细粒度声学），多尺度融合；仅用 UCLASS + FluencyBank Voices-CWS 儿科自发语料；说话人独立 5 折；主评测 3 类（Fluent / Core Stutter / Typical Disfluency），并报 4 类对照；对比成人 SEP-28k 迁移与 ResNet+BiLSTM、StutterNet 等。

## 实验与结果
加权准确率 82.4%±2.7%；Fluent F1 0.904，Typical Disfluency F1 0.386，Core Stutter F1 0.280。成人迁移后 Typical Disfluency F1 骤降至约 0.08。4 类 UCLASS 上 Fluent F1 0.90，相对多数基线明显更高，病理细类仍难。

## 结论
儿科专用图建模与词–帧层级交互有助于区分发展性与病理不流畅；成人 SOTA 不能直接当儿科诊断工具。层次注意力提供一定可解释性。

## 点评
抓住“典型不流畅 vs 核心口吃”这一临床关键区分，并用词节点注入语义，是正确问题设定。Core/Typical F1 仍偏低，类别稀少与自发语料限制明显；与基线的分类体系对齐依赖映射，跨论文对比需谨慎。


# Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech

- 论文编号：2909
- 报告人：Chibuzor Okocha
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/okocha26_interspeech.pdf

## 问题
儿童口吃语音在声学与结构上异于成人；ALM 能否在无显式说话人分离的混说访谈中做儿童聚焦语义推理、保留临床相关不流畅，尚不清楚。

## 方法
两任务：儿童向语义摘要（保不流畅、排除成人泄漏）；儿童语音蕴含（分层难度）。指令引导聚焦儿童。评测多款 ALM，辅以 Whisper/Granite ASR + 文本 LLM 级联与 transcript-oracle；LLM 裁判 + BERTScore；零样本提示变体。

## 实验与结果
摘要：Audio Flamingo 3、Kimi 总体较好（Overall 约 3.43/3.13）；Kimi 访谈 BERTScore F1 0.478。蕴含：Qwen2.5-Omni 最佳 ACC/F1 0.681/0.683；多数模型偏预测 entailment，矛盾类弱。难度从易到难 ACC 仅小幅下降（约 0.449→0.417）。提示工程收益有限。推理随不流畅与说话人干扰加重而明显变差。

## 结论
ALM 可从口吃儿童语音抽取高层语义，但在混说与高不流畅下忠实性与推理稳健性仍不足；需锚定转写基准以分离识别与推理误差。

## 点评
把“儿童焦点 + 保留不流畅 + 防成人泄漏”写进任务定义，比一般音频摘要更贴临床。LLM 裁判与偏 entailment 偏差会抬高表观分数；无说话人分离的设定现实但把难度堆叠，失败原因（声学 vs 指令遵循）仍需更细诊断。

