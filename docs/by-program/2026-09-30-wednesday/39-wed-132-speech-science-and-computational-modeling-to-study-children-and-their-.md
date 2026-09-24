# Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Special Session
- Area：14
- 论文数：13

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特刊/专题围绕儿童日常家庭与学前环境中的语音、交互与语言发展：从音素级发音筛查与跨语儿童音素识别，到底向上音节发现、说话人辨别发展，再到日长录音上的婴儿中心多层级标注、哭闹分级、说话人类型分类与儿童指向语检测。

方法上，自监督与 Whisper/HuBERT 类模型在儿童中心日长录音上预训练或微调成为主流；结构化说话人条件、上下文窗口与家庭偏移用于跨家庭泛化。同时强调真实噪声环境相对实验室数据的巨大域差，以及隐私驱动的基准与 ELSI 治理。

发展与社会语言学议题包括：学前遗产语输入输出量化、照料者—儿童韵律对齐的跨语 DTW 分析，以及面向成人/儿童多域统一 ASR 的熵感知 MoE Speech-LLM。

## 论文技术总结

# Phoneme-Level Mispronunciation Screening in Polish-Speaking Children with an Explainable Assistant

- 论文编号：1416
- 报告人：Milosz Dudek
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/dudek26_interspeech.pdf

## 问题
儿童语音障碍早期筛查受专科资源限制；波兰咝音系列密、易替换，通用 ASR 易被语言模型“纠正”而漏检；需可解释、偏保守的看护者筛查（非诊断）。

## 方法
专有 4–8 岁波兰儿童提示语料（201 人）。wav2vec2-large-xlsr-53-polish + 6 层 Transformer 后编码器 CTC；标签含括号化 IPA 替换证据（如 [s]）。LoRA+解冻后 6 层（约 33% 可训）。识别序列与规范序列对齐得诊断向量，再由固定模板助手生成看护者反馈，带不确定时抑制/拒答规则。

## 实验与结果
10 名未见儿童、559 句：精确序列匹配 88.7%；去掉后编码器降至 84.5%。保守筛查代理（目标位发出括号 token 即标记）：精确率 72.9%、召回 61.4%、F1=0.67，目标正确项假警 2.7%。强调非临床诊断，计划临床闭环验证。

## 结论
替换敏感的 token 识别 + 对齐筛查 + 模板助手，可在波兰儿童咝音场景提供低假警、可审计的家庭筛查原型。

## 点评
把“可解释”落成对齐痕迹+模板+拒答，适合看护者产品边界。括号 token 把替换显式化，避开 ASR 过度规范化。仍缺真实看护者/临床验证；召回中等意味着漏检需人工兜底。


# BabAR: from phoneme recognition to developmental measures of young children's speech production

- 论文编号：1132
- 报告人：Marvin Lavechin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lavechin26_interspeech.pdf

## 问题
婴幼儿语音发展研究依赖昂贵人工音素转写，难规模化；儿童（尤其低龄）ASR/音素识别仍极难，公开跨语标注稀缺。

## 方法
整理 TinyVox（PhonBank 标准化）：>50 万条 IPA 转写发声、560 名儿童、5 语、约 388 小时。训练 BabAR：比较多种 SSL 预训练（含儿童日长录音），用 CTC；微调时提供约 20 秒周围音频上下文。在留出纵向数据上提取典型/规范发声比例等发展指标并与文献对照。

## 实验与结果
多语儿童日长录音预训练显著优于成人-only 等替代；加长上下文进一步降错。替换多落在宽语音类别内，适于粗粒度发展分析。自动成熟度指标与文献发展估计对齐。相对既往约 60% PER 的儿童音素系统，正文报告显著改进（精确数字见全文表）。

## 结论
大规模跨语儿童音素数据 + 儿童中心 SSL + 上下文微调，使自动发展度量变得可行。

## 点评
TinyVox/BabAR 直接打通“标注债”与发展科学发展需求。音素清单跨语归一与 CTC 对齐误差仍在，细粒度临床音位诊断需谨慎；公开资源对复现价值高。


# How does children's pronunciation develop? Capturing syllabic change with children's growth using unsupervised syllable discovery

- 论文编号：3104
- 报告人：Koharu Horii
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/horii26_interspeech.pdf

## 问题
儿童发音发展分析常依赖专家转写或成人音素 ASR（自上而下），易淹没儿童特异与中间态发音；需要可扩展、不强制成人范畴的自下而上方法。

## 方法
用 Sylber 无监督音节发现：成人版（LibriSpeech）与儿童适配版（MyST 微调）。在 OGI Kids 957 名 5–15 岁朗读英语上，度量 (1) 与 MFA 音节边界一致（Jaccard、过分割比）反映接近成人节律；(2) 活跃音节簇数反映发音库；(3) 相对目标音节的簇纯度反映稳定性。

## 实验与结果
清晰发展模式：约 5–8 岁音节模式扩展（库增大），随后逐渐稳定并向成人样组织收敛。自下而上能捕捉自上而下难见的细粒度库与稳定性变化；儿童适配模型有助于分离适应效应与真实发展。

## 结论
无监督音节发现可作为大规模儿童发音发展研究工具，揭示“先扩展再稳定”轨迹，并可能推广到构音障碍/方言等难标注数据。

## 点评
把零资源自下而上范式接到发展语音学，避开成人音素硬套。双模型（成人/儿童）设计帮助解释“像成人”与“儿童内部变化”。仍依赖 MFA/提示目标作参照，完全无监督解释边界需谨慎。


# Talker Discrimination and Identification in 7-12-year-old Children: Effects of Talker Gender and Phonological Ability

- 论文编号：3053
- 报告人：Rebecca Holt
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/holt26_interspeech.pdf

## 问题
儿童说话人加工对理解与社交重要，临床群体常有困难；典型发展中男–男 vs 女–女难度、辨别与识别相关、以及音系技能预测作用仍不清，且缺儿童友好的识别范式。

## 方法
29 名 7–12 岁典型发展英语儿童：在线 AX 辨别（同/异说话人）与改良 ABX 识别（听介绍后据理解问题选说话人），含 M–F、F–F、M–M 配对；CTOPP-2 省略与非词重复测音系意识与音系工作记忆；混合效应逻辑回归，年龄作协变量。

## 实验与结果
跨性别配对显著易于同性别；F–F 与 M–M 无显著差异。同性别试验上辨别与识别相关 r=0.44。非词重复显著预测识别（β=0.274），省略与年龄不显著；音系技能不显著预测辨别。改良 ABX 识别范式可行。

## 结论
典型发展儿童对同性别男/女说话人对处理相似；辨别与识别共享方差但仍有独立成分；音系工作记忆支撑识别所需的稳定说话人表征。

## 点评
补齐儿童说话人研究中长期缺失的 M–M 条件，并把辨别/识别放在同一样本。儿童友好识别任务设计利于临床迁移。样本 n=29、远程施测，效应外推与任务策略差异需谨慎。


# Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning

- 论文编号：2746
- 报告人：Mark Hasegawa-Johnson
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/fan26b_interspeech.pdf

## 问题
婴儿中心日长家庭录音标签少、信噪比低、跨家庭域移大；需帧级多说话人层（儿童/女看护/男看护/兄弟姐妹）同时做发声分类，并处理重叠。

## 方法
LoRA 微调 Whisper-large-v2 编码器 + MLP（每 5 帧）下采样 + 两层目标说话人 Transformer + 每层分类器。说话人 token = 共享层 token + 家庭特异偏移。序列级时间平滑损失（λ=0.2）。家庭划分无重叠；输入 30s 片段。

## 实验与结果
跨层平均 Macro-F1 74.88、κ 68.14，优于 TL-TR（69.55/64.04）与多层级评测下的 W2V-LB（67.27/59.27）。去掉 LoRA、家庭偏移或平滑损失均下降。成人层（FAN/MAN）相对 W2V-LB 增益更大；儿童层差距较小，作者归因于 Whisper 成人预训练偏置 vs W2V-LB 家庭预训练。

## 结论
结构化说话人条件 + 参数高效 Whisper 适配，能高效完成婴儿中心多层级帧级音频标注，并更好处理重叠与跨家庭变异。

## 点评
把“家庭特异”与“角色层”拆开编码，直接对症跨家庭域移；多标签层设计贴合真实重叠。Whisper 对婴儿近麦发声仍偏域外，说明预训练分布与架构需一并考虑。


# Advancing Infant Distress Detection: Two- and Three-Way Classification in Real-World Audio Environments

- 论文编号：3234
- 报告人：Kaya de Barbaro
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/galhotra26_interspeech.pdf

## 问题
多数婴儿痛苦分类器在实验室数据上训练，迁到家庭日长录音大跌；现有公开真实数据多把 fuss 与 cry 合并，无法建模看护者随痛苦等级变化的反应。

## 方法
在 deBarbaroCry（婴儿佩戴 LENA 家庭录音）上重标 cry / fuss / non-distress，发布 deBarbaroFussCry（约 4.75h fuss、3.15h cry、其余非痛苦，共 66h 候选段；三分类 κ=0.847）。先强化二分类（痛苦 vs 非），再扩展三分类；比较传统、深度与混合模型，并做跨数据集泛化。

## 实验与结果
最佳二分类 macro F1=0.803（相对先前真实场景基线约 +17.8%）；三分类 macro F1=0.624（首个真实场景等级基准）。实验室训练模型在真实数据上显著退化；真实数据训练模型跨域更稳。数据与代码开源。

## 结论
真实家庭标注与分级（fuss vs cry）对生态有效婴儿痛苦检测必要；二分类可明显提升，三分类仍难但可建立基准。

## 点评
把“等级痛苦”写成发育理论与自动化看护质量测量的前置条件，动机清楚。跨数据集对照再次证明清洁数据乐观偏差。三分类 F1 仍中等，类别不平衡与短 fuss 边界是下一瓶颈。


# BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings

- 论文编号：2772
- 报告人：Théo Charlot
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/charlot26_interspeech.pdf

## 问题
儿童中心日长录音含大量非语音、重叠、远场与儿童声学特性，成人干净语音预训练模型失效；英语日长预训练（如 W2V2-LL4300）规模与语种覆盖不足。

## 方法
BabyHuBERT：在 40+ 语种约 13,164 小时儿童中心录音上做 HuBERT 式两轮掩码预测预训练（先用 PyanNet-VTC 抽语音段，非英语约 43%）。在 BabyTrain-2025（670h）上微调多标签 Voice Type Classification（关键儿童/其他儿童/男成人/女成人），仅训 Transformer。与成人 HuBERT、英语日长 W2V2-LL4300 对比。

## 实验与结果
BabyHuBERT-VTC 在六语料 F1 55.0%–76.1%，平均 66.9%，接近人类标注者 69.8%；一致优于 W2V2-LL4300 与 HuBERT。Vanuatu、Solomon Islands 上相对 HuBERT 绝对 F1 +14.0 / +18.3。模型与代码公开。

## 结论
大规模多语儿童中心域预训练显著提升说话人类别分割，缩小与人类标注差距，并惠及低资源语种研究。

## 点评
用真正“脏”的日长域做 SSL，比继续微调成人模型更对症。多标签 VTC 贴合发育研究“谁在说”需求。预训练依赖 VTC 过滤可能引入偏差；少数语料仍距人类有差距。


# Context-aware child-directed speech detection from long-form recordings

- 论文编号：2780
- 报告人：Théo Charlot
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/charlot26b_interspeech.pdf

## 问题
从日长录音中自动区分儿童指向语（CDS）与成人指向语（ADS）对规模化研究儿童语言环境很关键，但现有方法多在孤立短句上处理、以英语为主，且很少在自动分割后的端到端流水线中评估。

## 方法
在约 22 小时、6 语、182 名儿童的多语料上，微调六种自监督模型（W2V2、HuBERT、WavLM、W2V2-XLSR、W2V2-LL4300、BabyHuBERT），三类标签：KCDS、ADS、OTHER。上下文感知微调：将目标话语对称扩展到总长 x 秒（0–30s），编码器看全窗，但只对原话语帧做均值池化再分类。端到端评估时先用 VTC 2.0 检测成人语音，再分类；基线为“靠近目标儿童发声即判 KCDS”的规则系统。

## 实验与结果
验证集上 BabyHuBERT 平均 F1 最高（53.2%）。加 10 秒上下文后平均 F1 从 53.2% 升至 67.0%（+13.8%），再长则略降。测试集（10s 上下文）KCDS/ADS/OTHER F1 为 81.6%/78.9%/36.2%。heldout（Tseltal+Winnipeg）帧级 F1：人工分割下 BabyHuBERT-addressee 平均 74.1 vs 规则 35.1；VTC 2.0 分割下 38.6 vs 25.6，相对人工分割下降约 35.5 个点。

## 结论
领域匹配的多语儿童中心预训练与约 10 秒上下文是提升 CDS/ADS 分类的关键因素；全自动流水线可行但仍受分割误差传播限制。作者开源代码与模型。

## 点评
把“孤立短句分类”改成保留周围对话上下文，直击人工标注者实际依赖的线索，且用 heldout 与自动分割检验可部署性。OTHER 类仍弱、Tseltal 噪声户外场景掉点明显，说明跨文化/跨条件鲁棒性仍是瓶颈；上下文全编码代价高，文中提出的分层/交叉注意力是合理的后续方向。


# Benchmarking Adult Addressee Classification Across Child- and Adult- Directed Speech Datasets

- 论文编号：2536
- 报告人：
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
官方程序未提供摘要。仅能从标题与会场信息判断主题方向：「Benchmarking Adult Addressee Classification Across Child- and Adult- Directed Speech Datasets」，安排在「Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments」。

## 方法
官方程序无摘要，无法概括具体方法、模型结构或训练流程；此处不作推断。

## 实验与结果
官方程序无摘要，未给出数据集、对比设置或定量结果。

## 结论
官方程序无摘要，无法归纳作者结论与适用边界。

## 点评
该条目目前只有标题与程序位置可参考，后续若有讲义、幻灯片或正式论文，再据此补充问题设定、方法细节与可核验结果。


# Deriving Benchmarking Datasets from Long-Form Recordings: Challenges and Opportunities

- 论文编号：2363
- 报告人：Kaveri K. Sheth
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheth26_interspeech.pdf

## 问题
儿童中心长时录音（LFR）生态效度高，但跨语料格式/同意书异构、缺少共享基准、且标准 ML 流程难以覆盖敏感儿童语音的隐私治理，三者相互牵制，导致多数工具只在单语料上训练评估。

## 方法
提出三件套框架：(S1) 用 DataLad + ChildProject 标准化 27 个含人工标注的儿童语料（18+ 语、14 国）；(S2) 可复现流水线派生四类基准——voice type classification (VTC)、addressee、vocal maturity (VCM)、orthographic transcription，均采用 child-disjoint 划分；(S3) ELSI 角色化生态（Custodian / Tool Creator / Analyst），按原始音频、带标签片段、派生指标分级授权。案例：同 VTC 2.0 架构（BabyHuBERT + 四路二分类头）在公共子集与全集合上重训。

## 实验与结果
表 1 汇总公共与非公共语料的剪辑数、时长与各任务 utterance 量。VTC hold-out：VTC-2.0 平均 F1 65.1；仅公共数据重训 44.4；含私有集合重训 62.2（KCHI 73.4、MAL 68.8 超过原 SOTA 的 70.0/65.1）。人工一致性参考平均 F1 约 69.8。

## 结论
标准化、基准派生与伦理治理必须联动：仅靠公开子集无法达到有竞争力的跨语/跨条件性能；治理使受限语料可参与共享评估而不放开原始音频。

## 点评
把“数据工程 + 基准 + 权限”当成一体问题，比单纯发一个挑战集更贴近 LFR 研究现实。案例清楚说明公共 CHILDES 类数据分布过窄；ELSI 的价值在于把“训练要音频、评估要片段、分析只要指标”拆开，但仍依赖托管方持续运营与同意条款可机读化。


# Measuring English and Vietnamese language input and output in an Australian preschool – A longitudinal study

- 论文编号：3213
- 报告人：Ha Chi Tran
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tran26b_interspeech.pdf

## 问题
澳大利亚学龄前机构对传承语（HL）支持不足，易导致减损性双语。需量化越南语暴露项目中英语/越南语的输入与输出，并比较两年实施是否提升儿童参与与相对语言使用。

## 方法
墨尔本幼儿园越南语暴露项目第二年（IMP-2，2024）与第一年（IMP-1，2023）对照：每期各选 8 段录音（2×10 分钟 + 6×5 分钟），母语者用 Praat 手工标注引导者与儿童的英语/越南语时段，MATLAB 提时长；以 Bayesian 回归（brms）检验实施期与说话人效应。IMP-2：1 名越南语引导者 + 30 名 3–5 岁儿童（13 HL、17 附加语 AL）。

## 实验与结果
儿童总话语占比：IMP-1 约 10.9%，IMP-2 约 25.3%；引导者:儿童时长比由 8.17 降至 2.94。贝叶斯假设：儿童总输出增加（H1，强证据）；引导者英语输入、儿童英语输出增加（H2/H3，极强）；引导者越南语输入减少（H4，极强）；儿童越南语输出增加（H5，中等）。英语在儿童输出中仍占主导。

## 结论
两年结构化暴露可提高儿童总体产出与参与，但英语仍主导；方法可复用于其他 HL 项目。局限：未分开分析 HL 与 AL 子群。

## 点评
用可比时长切片 + 贝叶斯证据比，把“第二年更敢说”做成可核验的定量结论，对学前 HL 项目评估很实用。因一半儿童回流且 AL 比例高，英语上升与引导者越南语下降可能反映包容性 translanguaging，而非项目“失败”；分群纵向分析是必要补强。


# Dynamic Time Warping Reveals Prosodic Alignment in Caregiver–Child Interactions across Languages

- 论文编号：2356
- 报告人：Olivier Rüst
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rust26_interspeech.pdf

## 问题
偶发 CDS（紧跟儿童话轮的照料者话语）在结构上更简化，但其韵律对齐机制不明：是短时 priming，还是随儿童年龄变化的社会 accommodation？

## 方法
ACQDIV 中英、日、俄语料（纵向自然互动，主要母子对）。取儿童话轮 offset 后 2s 内的非重叠照料者跟随话轮，计算 Δt；用 Praat/parselmouth 提 F0，均值中心化后 DTW 归一化距离度量音高轮廓相似度。分语言 Bayesian 多层 LogNormal 回归：Norm DTW Dist ~ Δt + Age + (1|child)。用证据比（ER）比较 priming（仅短时对齐、无年龄效应）与 accommodation（短时对齐 + 年龄增大相似度下降）。

## 实验与结果
Δt：俄语正相关（更近更相似，ER≈284.7）；英语无可信效应；日语反而反向。儿童年龄：英、日、俄均与距离正相关（年龄越大越不相似；英/俄 ER=Inf，日 ER≈299），支持跨语言的 accommodation。

## 结论
CDS 的部分韵律特征可由照料者–儿童互动中的对齐产生，并以年龄相关的 accommodation 为主；短时效应受文化/语言调节。局限：仅 F0、语种与文化有限。

## 点评
用 DTW + 发展时间尺度把“CDS 是否只是一般对齐”操作化，并清晰对立 priming vs accommodation。跨语言不一致的短时效应提醒不要把英语模式外推；整句 DTW 可能稀释局部模仿，后续宜做亚话轮尺度分析。


# Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR

- 论文编号：877
- 报告人：Abeer Alwan
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26c_interspeech.pdf

## 问题
Speech-LLM 在成人 ASR 上强，但儿童语音差异大、年龄与环境异构；单模型难平衡，且适配儿童常损害成人性能。公开儿童语料上尚缺强 Speech-LLM 结果。

## 方法
基于 Canary-Qwen 的 MoE Speech-LLM：Mixture-of-Projectors (MoP) + Mixture-of-LoRAs (MoL) 为各域专用专家；Classifier-based Domain Router (C-DR) 做粗到细路由（数据集级粗域 + OGI-S 年龄细域）；Entropy-Aware Routing (EAR) 按归一化路由熵插值共享专家。五域：OGI-S 三年龄组、MyST、Libri-Clean。训练时专家用真值硬路由，C-DR 与 MoE 分开训；推理支持硬/软路由。

## 实验与结果
单数据集微调可达新 SOTA（OGI-S Avg WER 10.93 / MyST 8.34）。C-DR MoE（软路由 + EAR）OGI-S Avg 11.08、MyST 8.58、Libri-Clean 1.61，优于 single-expert 与 vanilla-routing MoE，且不伤成人。消融：MoP+MoL 同时最好；仅 MoP 优于仅 MoL。粗到细加权层分类器路由最准。

## 结论
显式域路由 + 双层 MoE + 熵感知共享专家，可在统一 Speech-LLM 中同时服务成人与多域儿童 ASR。据作者称，这是首个在公开儿童语料上给出强结果并联合分析成人/儿童/年龄的 Speech-LLM 框架。

## 点评
把“儿童≠单一域”做成层次路由，并用熵处理年龄边界模糊，比可训练 gate 更可解释。EAR 能超过真值年龄路由，说明声学发展阶段未必对齐生日年龄。参数开销约 +5% 可接受；共享专家单独并不强却能补不确定样本，是实用设计取舍。

