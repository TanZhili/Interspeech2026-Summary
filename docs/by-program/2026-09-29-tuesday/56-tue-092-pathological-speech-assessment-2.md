# Pathological Speech Assessment 2

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：13
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦病理/认知相关语音评估：痴呆筛查中用转写分数与 Whisper 嵌入融合降低评分误差并补偿缺失运动子测验；原发性进行性失语则用临床 grounding 的层次仿真缓解标注稀缺。多模态检测整合 ASR 声学嵌入与 LLM 增强语言学特征，或用 LoRA-LLM 对多视角语音派生信号做结构化推理。

表示学习侧提出病理感知神经掩码，迫使编码器学习分布式稳健表征而非捷径；图方法用语义/依存/共现多图与门控融合刻画叙述逻辑偏离。临床嗓音质量客观指标则通过盲去混响减轻房间声学对 CPPS 的扭曲。共同主题是：数据稀缺下的仿真与多视图融合，以及可解释、临床对齐的正则。

## 论文技术总结

# Mitigating Scoring Errors and Compensating for Nonverbal Subtests in Speech-Based Dementia Assessment

- 论文编号：2806
- 报告人：Franziska Braun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/braun26_interspeech.pdf

## 问题
基于语音自动化德语 Syndrom-Kurz-Test（SKT）时，病理/方言/结构化应答导致转写错误，且运动子测无法靠语音完成，限制总分与分型准确性。

## 方法
158 名临床受试者。规则基线（RB）从 Whisper 转写算子测分；deep correction 用 RB + Whisper 编码器/解码器嵌入精炼子测分；deep compensation 融合可用言语子测表示以逼近专家总分（补偿缺失运动子测）。并搜索高效子测序列以兼顾分类与效率。

## 实验与结果
RB+ENC/DEC 与专家子测分强相关，ASR 难子测相关可提升最多约 0.35。即使省略运动子测 4/5，补偿模型与专家总分仍可达很高相关（文中称近 0.9 量级）。最优言语子测序（如 1→7→8→6→2）在保持总分相关的同时提升效率。

## 结论
转写分数与 Whisper 嵌入融合可纠评分误差；用言语子测表示可补偿非言语子测缺失，支持更可及的语音化 SKT 筛查。

## 点评
把临床量表自动化中的两类硬伤（ASR 错分、运动项缺失）拆开处理，工程路径清晰。样本量中等、口罩录音与临床场景特定，外推需谨慎；补偿不等于真正测到运动域，诊断解释仍应标注缺失维度。


# HASS: Hierarchical Simulation of Logopenic Aphasic Speech for Scalable PPA Detection

- 论文编号：3080
- 报告人：Harrison Li
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ia_interspeech.pdf

## 问题
原发性进行性失语（PPA）临床数据稀缺；既有不流畅仿真多注入孤立事件，难刻画 logopenic 变异（lvPPA）跨词汇检索与音系编码的多层次表型。

## 方法
HASS：在临床专家指导下用 LLM 生成内容层（词汇检索受损）与音素层（音系错误）严重度条件缺陷，再合成为语音；同管线生成匹配对照（不注入损伤）。语料 4773 句级片段。用 Wav2Vec2+LoRA 分类，严格跨站：Baycrest/Hopkins 患者与 Delaware/Capilouto 对照。

## 实验与结果
跨站：HASS 训练模型 AUC 0.892±0.076、F1 0.800±0.072、dysfluent 召回 0.899±0.066，优于真实数据基线（AUC 0.850、召回 0.659）。纯 HASS 训练在跨语料协议上也可泛化。

## 结论
临床接地的分层仿真可为 lvPPA 检测提供可扩展增强，并改善跨站点泛化与对不流畅样本的召回。

## 点评
把疾病机制写成可控制的双层生成，比“随机插停顿”更贴近表型。合成–真实域差仍在；作者强调对照与患者同管线以隔离合成伪影，但零样本临床部署仍需标定阈值与伦理边界。


# Listening Between the Lines: Joint Learning of ASR Embeddings and LLM-Augmented Linguistics for Dementia Detection

- 论文编号：939
- 报告人：Myungwoo Oh
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jung26_interspeech.pdf

## 问题
痴呆语音筛查需同时捕捉声学与语言生物标记，但多数系统单模态；信息单元等手工语言方案覆盖有限，LLM 又常作黑盒或仅对齐旧 IU 框架。

## 方法
Whisper 双用：编码器输出经时间网络+注意力池化得声学嵌入；ASR 转写经 LLM 抽取 46 维可解释语言特征（词汇/句法/语义连贯/语篇），筛选为 29 维；门控融合两模态。评测 ADReSS / ADReSSo。

## 实验与结果
说话人级 F1：ADReSS 89.47%、ADReSSo 90.14%。多模态优于单模态；优化 29 特征集含部分统计不显著特征却优于显著性过滤集，提示交互作用。相对部分先验工作相对 F1 提升约 19%。

## 结论
声学嵌入与 LLM 增广语言特征经门控融合，可在标准 Cookie Theft 基准上达到强 AD/CN 判别，并强调特征交互而非仅显著性筛选。

## 点评
把 LLM 当成可解释特征抽取器而非端到端分类器，利于临床可沟通性。与同场 park26c 同报 90.14% F1，需注意设定差异；转写错误与 LLM 提示敏感性仍是误差源。


# LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features

- 论文编号：952
- 报告人：Jonghyeon Park
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26c_interspeech.pdf

## 问题
痴呆相关言语改变跨声学、时间、音系与语篇多维；既有方法常单视角或晚融合，限制跨症状综合推理。

## 方法
将四类语音衍生信号写入统一提示：Whisper ASR 转写+对齐停顿标记、语篇主题/聚类线索、时间流利统计、不流畅感知音素序列；对 LLM（最佳 Qwen3-14B）做 LoRA（r=8）微调做 AD/CN 分类，无需模态专用编码器。评测 ADReSSo。

## 实验与结果
最佳多视角 LoRA 模型说话人级 F1 90.14%。逐步消融显示各视角互补；仅转写基线约 81.48%，加入停顿、主题、音素等逐步提升至满分配置。

## 结论
结构化多视角提示 + 参数高效 LLM 适配可统一整合异质言语线索，在 ADReSSo 上达到强判别性能。

## 点评
用单一 LLM 做跨视角推理，避免复杂多编码器融合工程。性能与 jung26 同数，属同一团队互补路线；对对齐与音素识别前端质量依赖高，低资源语言可迁移性待验。


# PAN-Mask: Pathology-Aware Neurological Masking with End-to-End Learnable Weights for Neurological Disorder Detection from Speech

- 论文编号：1006
- 报告人：Qi Sun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26b_interspeech.pdf

## 问题
WavLM 等自监督分类沿用内容无关随机掩码，忽略病理语音中稀疏、局部的临床生物标记，易 shortcut 到少数显著帧。

## 方法
PAN-Mask：轻量检测器提取六类可解释声学描述（节律不规则、停顿、音高单调、能量下降、嗓音质量、周期性），可学习注意力聚合为帧级病理显著性；训练时优先掩蔽高显著性段，迫使编码器学分布式表征。检测器与分类器端到端联合优化。六数据集、三病种（AD/PD/抑郁）、五语言，超参固定。

## 实验与结果
相对随机掩码准确率提升 8.31–22.72 个百分点（平均 13.82%）。框架跨病种/语言无需手工重设特征重要性，并提供可解释显著性洞察。

## 结论
病理感知掩码作为任务感知正则，可提升神经疾病语音检测并抑制 shortcut，同时给出临床可解释线索。

## 点评
把“别只盯最显眼的病理片段”写成可微掩码目标，方向新颖。增益幅度大但依赖各数据集基线强弱；显著性是否真正对齐临床标注仍需外部验证。


# Gated Multi-graph Fusion via Graph Attention Networks for Alzheimer’s Disease Detection

- 论文编号：2578
- 报告人：Xiao Wei
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ga_interspeech.pdf

## 问题
AD 自发言语存在非线性结构破坏与症状异质性；多数系统偏语义向量或简单融合，难刻画语篇“内容–结构–流向”与个体差异。

## 方法
ASR 转写后建三视图图：语义图、依存图、基于规范语料 PMI 的共现图（量化叙事逻辑相对健康常模的偏离）；图注意力编码后经自适应门控按样本融合。在 ADReSSo 上评估。

## 实验与结果
准确率 90.00%。消融表明 PMI 共现图与异质性感知门控对稳健分类关键。

## 结论
多图“内容–结构–流向”建模加门控融合，可提升 AD 自发言语检测并适配症状多样表现。

## 点评
用健康常模 PMI 刻画“叙事流向”偏离，比纯语义嵌入更贴语篇病理。依赖 ASR 质量；图构造与常模语料选择会影响跨域稳定性。


# From Echo to Accuracy: Robust Voice Quality Assessment Using Blind Unsupervised Diffusion-based Dereverberation

- 论文编号：2608
- 报告人：Sven Franz
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/franz26_interspeech.pdf

## 问题
客观嗓音质量指标（如 CPPS）对混响敏感，临床治疗室录音会系统性压低或扭曲病理排序；需不依赖测得 IR 的盲去混响。

## 方法
两库无回声嗓音样本卷积真实治疗室 IR，再用无监督扩散去混响 BUDDy。检验：(H1) 首次去混响对 CPPS；(H2) 混响对 CPPS 水平与排序；(H3) 二次去混响能否恢复水平与排序。

## 实验与结果
低混响录音去混响未引入系统 CPPS 偏置；混响条件下降的 CPPS 经处理后得到补偿。连续言语上嗓音质量排序可重建，CPPS 接近无回声参考水平（跨库一致）。

## 结论
盲扩散去混响可有效缓解房间声学对连续言语客观嗓音评估的扭曲，支持更房间无关的 CPPS 应用。

## 点评
把增强算法目标对准临床声学指标而非听感/ASR，场景贴切。结论主要针对连续言语与所测治疗室 IR；极短元音任务与极端混响外推仍需验证。

