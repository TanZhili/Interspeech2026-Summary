# Grand Special Challenges Poster Showcase

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster
- Area：14
- 论文数：13

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场是多项 Interspeech 2026 Grand / Special Challenge 的集中展示：跨域音频表征、语用意图语音翻译、野外无监督多语语音（UPS）、阿拉伯语发音偏误评测（IQRA）、以及颈表振动语音过度功能监测（NeckVibe）。挑战综述与参赛系统并列，便于对照任务设定、数据约束与领先方法。

表征学习侧，BEST-RQ-2 把掩码预测拆成 contextualize-then-predict 并用 ViT 上下文编码器；WQ-Fusion 用动态门控融合 Whisper 与 Qwen；UPS 相关工作则在大规模异构网络音频上强调从零或继续预训练，并揭示离散单元 CPT 与对比式 CPT 在内容–说话人信息上的权衡，以及本地诊断与官方 probe 排名不一致的风险。

发音评测挑战把声学保真与规范音先验解耦：prompt-free CROTTC-IF、两阶段域适应融合框架，以及挑战综述报告的 F1 大幅跃迁，共同指向“真实偏误数据 + 细粒度对齐/适应”驱动进展。NeckVibe 则转向真实世界周监测：日内时间分割、层次化特征（含耦合特征）、表格模型与 MIL 注意力堆叠，是 PVH/NPVH 检测的主要方法论差异；摘要普遍称 PVH 相对更易分、NPVH 更难。

语用翻译挑战明确以语用保真为目标，并报告最佳系统相对人类评分仍有差距，同时反思评测方法本身的优劣。

## 论文技术总结

# BEST-RQ-2: Contextualize-Then-Predict, a Two-Step Approach for Self-Supervised Audio Representations

- 论文编号：2488
- 报告人：Ludovic Tuncay
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/tuncay26_interspeech.pdf

## 问题
BEST-RQ 用冻结随机投影离散目标做掩码预测很稳，但原 Conformer 与“掩码原位输入”难支持 JEPA 式“先上下文、再预测”；通用音频域（语音/环境/音乐）需要更好的架构分解。

## 方法
**BEST-RQ-2**：ViT 上下文编码器只看未掩码 mel 块；轻量 ViT 预测器在预训练时对掩码块预测 8192 码目标，推理丢弃。对照 BEST-RQ（Conformer）与 BEST-RQ (ViT)（同 tokenizer/目标但单阶段原位掩码）。AudioSet 约 1.9M×10s，200k 步。

## 实验与结果
X-ARES 线性探测：BEST-RQ-2 MoM/Overall 0.50/0.49，优于 BEST-RQ 0.43/0.45 与 BEST-RQ (ViT) 0.44/0.43；语音略换环境/音乐增益。kNN 上同样领先同类。文称 XARES-LLM 上两步分解带来一致迁移增益，推理算力不变。

## 结论
跨域平均提升主要来自 contextualize–then–predict 分解，而非仅换 ViT；ViT 本身更重分配域内表现。

## 点评
干净消融把“编码器换骨”和“预测分解”拆开，对挑战赛式通用编码器很实用。冻结随机目标保持简单；语音域相对 Whisper 等仍可能偏弱，需按下游权衡。


# WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation

- 论文编号：3228
- 报告人：Gongping Huang
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/lin26n_interspeech.pdf

## 问题
单编码器难以同时覆盖语音精细结构与非语音/高层语义；静态拼接 Whisper 与 Qwen 虽已强，但不能按任务动态取舍。

## 方法
**WQ-Fusion**：冻结 Whisper-large 与 Qwen2-Audio 双骨干 → Adaptive Feature Modulation 对齐 → 位置编码 → 元素级门控 Transformer 动态路由。面向 Interspeech 2026 Audio Encoder Capability Challenge Track A（XARES-LLM 类评测）。

## 实验与结果
总体分 0.836，高于最强单编码器（如 Qwen 约 0.796）与简单拼接（约 0.832）；消融显示 AFM + 门控逐步抬升至 0.836。Whisper 偏语音、Qwen 偏非语音/语义，融合后互补。

## 结论
动态门控融合异构编码器可提升跨域通用表示，优于静态拼接。

## 点评
挑战赛系统文：核心洞察是“互补 inductive bias + 可学路由”。依赖两大冻结骨干，部署重；门控是否真正按任务解释仍需更多诊断。


# The Interspeech 2026 Challenge on Transfer of Pragmatic Intent in Speech-to-Speech Translation

- 论文编号：390
- 报告人：Nigel G. Ward
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/ward26_interspeech.pdf

## 问题
现有语音到语音翻译（S2ST）多评语义与自然度，很少系统评语气、意图等语用保真，难以支撑跨语言对话。

## 方法
挑战设计：英↔西双语者会话重演得到语用对齐测试集（En→Es 240、Es→En 199 句）；主观评“语气/感觉/意图”1–5 分；自动用 Segura 语用相似度量。条件：音频 S2ST（C1）与语用特征向量映射（C2）。报告 4 队正式提交结果。

## 实验与结果
Es→En 音频：人类重演 4.59，最佳系统 CUHK-SZ 3.46，Seamless 2.98；最佳相对人类落后约 1.2 分。Segura 上 CUHK-SZ 亦略优于 Seamless。自动度量与人类相关约 0.51；文中讨论评测优缺与各队系统要点。

## 结论
语用保真仍明显落后人类；挑战建立了数据与评测基线，并暴露自动度量跨条件可比性等问题。

## 点评
把“对话里听起来像不像那个人想表达的”做成可评挑战，填补 S2ST 评测空白。评委少、部分评委参与造数、自动度量局限作者已坦陈；价值在议程设定多于刷榜数字。


# BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation for Unsupervised Speech in the Wild Challenge

- 论文编号：2966
- 报告人：Prakriti Subedi
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/subedi26_interspeech.pdf

## 问题
UPS Challenge 要求在无标签、声学多样的 MLCommons Unsupervised People’s Speech 上学习多语语音表示，并用冻结表示在 LID（macro-F1）、ASR（CER）、说话人聚类（ARI）上评估。多数语言缺乏标注，现有监督预训练难以覆盖；挑战还要求 Open Filtering 子赛道上的可复现流水线。

## 方法
以 HuBERT 式掩码离散单元预测训练双向 Mamba-2（BiMamba2）编码器：每层前向/反向 Mamba2 SSM 与对角跳连相加。主模型 d_model=768、12 层，约 47.88M 参数。伪标签由对 80 维 log-mel 帧的 MiniBatchKMeans（k=200）离线得到；掩码约 75% 有效帧、3–5 连续块。损失为掩码位置交叉熵 + VICReg（方差/协方差）+ 弱 LID 交叉熵（λ_lid=0.05）。数据经 VAD 与质量过滤后约 250 小时、67 语种；批次 70% 语言均衡采样、英文硬顶 10%。推理时将帧级输出按前/中/后三段平均并 L2 归一化，经 Dynabench ModelController 提交。

## 实验与结果
官方 Dynabench：主结果取 step 19,500——ARI 0.735（高于 Whisper/HuBERT-large/XLSR/wav2vec 2.0），macro-F1 0.073，CER 0.870。step 48,000 的 CER 恶化至 0.998；小模型（d=512, 8L）全面更弱。本地 holdout 反而偏好 late checkpoint，且本地 LID 高估、ARI 低估官方分，作者分析为语言重叠与探针方法不一致。

## 结论
BiMamba2 + 掩码离散单元在说话人聚类上超过四条基线，但 LID/ASR 仍弱于监督基线，受数据规模与语种覆盖限制。晚期训练出现 CER 退化与嵌入几何变化；本地诊断不能可靠预测官方排名。缺组件消融、单次运行、伪标签未迭代 refinement。

## 点评
做法把线性复杂度双向 SSM 接到 HuBERT 式目标上，并靠 VICReg/弱 LID 稳住多语嵌入。强项是说话人聚类与对本地–官方失配的实证诊断；脆弱点是固定 k-means 目标易过拟合簇边界、LID 监督过弱且语种覆盖不足，内容任务难以追上大规模监督/SSL 基线。


# Content–Speaker Trade-offs in Continued Self-Supervised Pre-Training Across SSL Paradigms for Multilingual Speech

- 论文编号：2946
- 报告人：Danner Schlotterbeck
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/schlotterbeck26_interspeech.pdf

## 问题
Continued Pre-Training（CPT）常用在域适应，但既有工作偏对比学习架构；离散单元模型（HuBERT/WavLM）的伪标签来自源域，直接续训是否有效、以及 CPT 是否在内容与说话人信息间造成灾难性遗忘，缺少跨范式对照。

## 方法
从 UPS 用 VAD 密度与语言稀缺评分策展 100h/500h 子集。对 HuBERT、WavLM（含帧内混叠去噪）在目标数据上重算 k-means 伪标签并接新投影头续训掩码预测；对 OmniASR（wav2vec 2.0 对比）直接恢复原生对比目标。共享 span masking（约 57% 帧）、AdamW、5 epoch。另消融伪标签：MFCC（第一轮式）vs 中间层 embedding（不同层与 K）。下游用 UPS 官方探针：LID Macro-F1、说话人 diarization ARI、ASR CER；并用 LibriSpeech 线性 CTC 探针看遗忘。

## 实验与结果
内容指标常有提升但不稳：如 HuBERT-base 100h 上 F1 .56→.67、CER .72→.65，但三随机种子 CER 方差大（.55–.74）。离散单元模型 ARI 系统性崩溃（HuBERT .76→.32，WavLM-base+ .59→.31，WavLM-large .76→.38），OmniASR ARI 略升 .37→.42。MFCC 伪标签损害内容（F1/CER）却大致保住 ARI；embedding 伪标签则相反。LibriSpeech 探针上离散单元有不同程度遗忘，OmniASR WER 反而改善。全文末尾抽取略有截断。

## 结论
CPT 可使表示偏向语言内容，离散单元模型上说话人信息稳定受损，内容增益高方差；伪标签性质（MFCC vs embedding、聚类层）决定内容–说话人权衡。局限为算力下的短日程、子集策展，未扩到全量 UPS。

## 点评
核心贡献是在相同数据与探针下把“续训离散单元是否可行”做成跨范式对照，并钉住伪标签类型这一旋钮。强在揭示可复现的说话人退化；弱在多数配置单次运行、内容增益解释需谨慎，且尚未给出显式保说话人（如 adapter）的解法。


# Unsupervised Speech in the Wild Challenge: Learning Robust Multilingual Representations

- 论文编号：3113
- 报告人：Rafael Mosquera Gómez
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gomez26_interspeech.pdf

## 问题
现有 SSL 多在 LibriSpeech、CommonVoice 等较干净语料上预训练，对网络爬取语音中的自发对话、噪声、长尾语种覆盖不足。需要在仅允许使用 Unsupervised People’s Speech（UPS）的约束下，公平评估多语表示质量。

## 方法
组织 UPS 2026 Challenge：训练数据为 UPS（约 80 万小时公开许可网络音频，Silero VAD 检出约 52.2 万小时语音，Whisper 编码器检出约 89 种语言）。提交须暴露冻结编码器的帧级嵌入接口；下游探针由官方固定：(1) FLEURS 子集 73 语种 LID，线性分类器，macro-F1；(2) 同子集 few-shot CTC ASR，逐语种字符表，macro CER；(3) VoxTube 派生 70 语种/398 说话人聚类，按语种 oracle 说话人数算 ARI 再宏平均。总分按三任务排名均值。经 Dynabench 统一评测。

## 实验与结果
14 队共 80 次有效计分：Macro-F1 均值 0.362（最大约 0.949），CER 均值 0.787（最低约 0.538），ARI 均值 0.457（最大约 0.947）。单模型不统治全任务：LID 最强多为 whisper-baseline / Nx；CER 最强为 WavLM-large 变体；ARI 最强为 qwen3-encoder-baseline。日文等非拉丁脚本 CER 系统性更高；瑞典语/丹麦语等 ARI 更难，且与子集说话人数与性别失衡有关。

## 结论
挑战表明在异构“野外”网络音频上可推动多语 SSL，但三任务探测互补性质，无单一系统全面最优；评估还受正字法与聚类子集构成影响。作者希望推动更稳健、语言无关且说话人感知的表示学习。

## 点评
这是赛道说明书式论文：价值在统一数据约束、冻结编码器与多任务探针设计，而不是提出新架构。对参赛与后续复现最有用的是任务定义、数据集构造与“无模型通吃”的实证；诊断部分也提醒 CER/ARI 解读需结合脚本与子集组成，不能只看排行榜总分。


# Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis

- 论文编号：711
- 报告人：Haopeng Geng
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/geng26_interspeech.pdf

## 问题
MDD 需要忠实刻画细粒度声学偏差，但沿用 ASR 的 CTC 会因稀疏后验与延迟发射抹掉短暂错误线索（声学陷阱）；显式规范音素提示或强 LM 又易把预测拉回规范文本（语言学陷阱），且推理依赖提示限制自发场景。

## 方法
提出无提示的 CROTTC-IF：(1) CROTTC——用一维最优传输求单一单调帧–标签对齐（OTTC），并对两路增强视图的帧级后验做对称 KL 一致性正则（CR），损失为 L_CR + η(L_OTTC)；无 blank 主导的稠密对齐。(2) Indirect Fusion（IF）——训练期把规范音素与错误标注作特权信息，经融合网络与双头错误检测教师反传到编码器/解码器；推理丢弃教师，仅用 AM/LM 浅融合搜假设。(3) 另构造 LLM-MDD，用多模态 LLM 与不同提示模板量化显式规范先验的影响。全文自 LLM-MDD 训练细节起抽取被截断。

## 实验与结果
摘要与引言报告：CROTTC-IF 在 L2-ARCTIC 上 F1 71.77%，在 Iqra’Eval2 排行榜 F1 71.70%；无辅助数据与显式规范提示。评测覆盖 L2-ARCTIC、ERJ、speechocean762 与阿拉伯语 Iqra’Eval2。因后半正文截断，更细消融与 LLM 对比数字无法从全文完整核对。

## 结论
作者认为解耦声学建模与显式规范先验、用稠密帧对齐 + 训练期特权知识迁移，可在无提示推理下得到稳健 MDD。边界与完整 LLM 实验结果因抽取截断未能充分呈现。

## 点评
问题诊断清晰：针对 CTC 稀疏/延迟与规范泄漏分别改对齐目标与训练期知识注入，推理仍保持 prompt-free，路线与 CAPT 实际约束契合。抽取文本在 LLM-MDD 一节中断，实验数字与 LLM 分析只能部分采信；实现上也依赖最优传输与多任务权重调参，对低资源标注质量敏感。


# IQRA 2026: Interspeech Challenge on Automatic Assessment Pronunciation for Modern Standard Arabic (MSA)

- 论文编号：2445
- 报告人：Yassine El Kheir
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kheir26b_interspeech.pdf

## 问题
阿拉伯语 MDD 长期缺统一基准与开放标注数据；上一版 IqraEval 无真实人为误读训练数据，最佳 F1 约 0.47。MSA 音位复杂（咽音、强调对立等）且存在双言现象，需要可复现的共享评测与真实误读语料。

## 方法
组织 IQRA 2026：任务给定语音与带元音符号参考文本，预测实际发音音素序列（68 音素 MSA 清单），与规范/verbatim 对齐后算 TA/FR/FA/TR、Precision/Recall/F1（主指标）与 PER。训练资源含 Iqra train（~79h）、Iqra TTS（~52h）及新增真实误读 Iqra Extra IS26（1,333 句，~1.5h）；测试 QuranMB.v2（1,643 句）。基线为冻结 mHuBERT + 加权层和 + BiLSTM-CTC，F1=0.4414。

## 实验与结果
19 队参赛；13 队超基线。榜首 whu-iasp F1=0.7201（相对基线 +0.2787），UTokyo 0.7170，RAM 0.7157；前六均 F1>0.67 且 PER≤0.0445。方法覆盖增强 CTC/时间建模、SSL+LM、生成式 LALM（Kalimat 第 6）。共性发现：真实误读数据对顶名次至关重要；低名次系统常高召回低精确。相对上一版最佳约翻倍。

## 结论
开放训练数据、真实误读语料与多样建模共同推动阿拉伯语 MDD；仍缺音素级诊断到学习者可读字符/变音符反馈的映射，以及面向自然语言反馈的生成式评测。

## 点评
作为挑战综述，价值在数据补齐（尤其 Extra IS26）与全榜诊断，而非单一模型。顶名次方法路径多样却分数接近，说明数据质量与对齐精度比单纯堆模型容量更关键；后续瓶颈明确指向字符级可操作反馈与更大规模真实学习者语料。


# A Fusion-Aware Two-Stage Framework for Mispronunciation Detection and Diagnosis in Low-Resource Modern Standard Arabic

- 论文编号：1553
- 报告人：Gongping Huang
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26j_interspeech.pdf

## 问题
低资源 MSA 上 MDD 受数据稀缺与合成–真实域差距制约；Transformer/LSTM 易全局平滑，难以保留强调对立、重叠辅音等局部音位线索，简单混合合成与真实数据还可能加重域偏移。

## 方法
混合架构：wav2vec2-xls-r-300m 编码器 + 因果膨胀 TCN + CTC。两阶段训练——Stage1 在 Iqra train（~79h）与 Iqra TTS（~80h）学通用映射；Stage2 在真实学习者 Iqra Extra IS26（~2h）适应。推理：Stage1 最优 checkpoint + Stage2 多个 checkpoint（共 K=6）经混淆网络对齐投票，并用由融合假设自估计的 MKN 3-gram 重打分，λ=0.2 偏重声学以免过度纠正。

## 实验与结果
盲测 QuranMB.v2：系统 F1=0.7201，相对基线 0.4414 提升 63.1%，居 IqraEval.2 榜首。消融：两阶段单 checkpoint 0.6825；仅 Stage1 0.4629；仅 Stage2 0.6681；naive Mix 0.4305（低于基线）；Stage2 上 TCN 优于 LSTM（0.6467）与 Transformer（0.6000）。集成+LM 相对单 checkpoint 再相对提升约 5.5%。

## 结论
TCN 局部归纳偏置、两阶段域适应与多 checkpoint 集成共同缓解合成–真实差距与低资源过拟合，刷新低资源 MSA MDD 表现。作者认为该流程可推广到其他数据稀缺语言。

## 点评
把挑战里“真实误读虽少但关键”落成可消融的课程式训练，并用 TCN 显式对抗语义平滑，工程闭环完整。弱点是高度依赖 Extra IS26 与集成后处理，单模型上限与对其他测试域的迁移仍需验证；声学权重 λ=0.2 的设定也表明语言学先验仍是双刃剑。


# The Interspeech 2026 NeckVibe Challenge: Voice Disorder Detection via Real-World Monitoring of Neck-Surface Vibration

- 论文编号：3049
- 报告人：Ahmed Yousef
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yousef26b_interspeech.pdf

## 问题
诊所短时评估难以反映日常用嗓；麦克风 ambulatory 记录易受环境干扰。需用颈表加速度计（ACC）大规模监测，推动超越简单线性分类与全日汇总特征的 VH（嗓音过度功能）检测。

## 方法
发布 NeckVibe Challenge 数据：582 人（PVH/NPVH 与匹配对照）一周日常监测，约 46,400 小时；智能手机采颈表 ACC（11,025 Hz），帧级 50 ms 提取 14 维可解释嗓音特征（SPL、CPP、H1–H2、spectral tilt、L/H、IBIF 气流相关量等）及发声/歌唱/暂停掩码。任务1：PVH vs 其余；任务2：NPVH vs 其余。80%/20% 按受试者分层划分，主指标 AUC。基线约 PVH AUC 0.82、NPVH 0.78。

## 实验与结果
6 队完成提交。Task1 全队超基线，最佳 AUC 0.93（SR），其次 0.92（DD）。Task2 更难，4 队超基线，最佳 AUC 0.86（SM、VA）。顶尖方法共性：日内时间窗或 Δ/ΔΔ 动态特征、特征比、XGBoost/CatBoost/逻辑回归、语音–歌唱上下文分离、以及 MIL/CNN 等时序建模。讨论后半抽取略有截断。

## 结论
挑战表明捕捉日内变异与关系型特征可提升 ambulatory VH 检测；NPVH 分离更难且队间差异大。结果有助于理解真实用嗓与 VH 病理的关系，并推动个性化嗓音管理。

## 点评
作为数据挑战组织文，贡献在大规模 ACC 特征发布与双任务设定。参赛结果清楚指向“不要只做全日均值”——时间结构与特征交互更关键；同时 Task 定义（vs 全部非目标类）与既往文献（vs 匹配对照）不完全等同，跨文数字对比需谨慎。


# Temporal Partitioning of Vocal Activity for Detecting Vocal Hyperfunction from Neck-Surface Accelerometer Data

- 论文编号：1435
- 报告人：Władysław Średniawa
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azarski26_interspeech.pdf

## 问题
用长期颈表 ACC 检测 PVH/NPVH 时，仅靠全日汇总统计可能抹掉日内用嗓变异；既往基线 AUC 约 PVH 0.82、NPVH 0.78，需更好的时间切分与特征工程以提升区分度。

## 方法
在 NeckVibe 数据上分任务建模。PVH：策略1——将日切为 10 个部分重叠时间窗，对 CPP、H1–H2、spectral tilt、L/H、ACC 幅度、SPL 等在 voiced 帧上取 mean/median/SD/10th/90th 及 voiced 比例，并全日汇总 IBIF；用强正则 XGBoost。策略2——语音/歌唱分开聚合、减为 4 个非重叠时段，用逻辑回归。最终对两模型概率平均做集成。NPVH：在 Cortés 式短窗上网格搜索窗长与 voiced 比例阈值，最佳为 300 s 且至少 10% 语音+歌唱，再聚合到受试者级，用另一套正则 XGBoost。严格 LOGO（按受试者）验证。

## 实验与结果
训练集聚成：PVH 集成 LOGO AUC 0.891（单模型约 0.871/0.881）。官方测试：PVH 集成 AUC 0.925（第 1）；NPVH AUC 0.820（第 4），均超基线。SHAP 显示下午/晚间 H1–H2 低变异、高 IBIF CQ 等指向 PVH；NPVH 更依赖短窗高分位统计而非宽时段模式。经典 MLP/CNN/LSTM 易过拟合。

## 结论
按日切分与语音–歌唱分离能提升 ambulatory VH 检测；PVH 与 NPVH 最优时间尺度不同（宽窗日内结构 vs 短窗瞬态）。集成与特征工程优于浅层神经网络在该受试者规模下的表现。

## 点评
把挑战组织文里的“日内变异”落到可复现的切窗与双模型集成，并用 SHAP 把预测接到声门闭合相关生理解释，工程与可解释性兼顾。脆弱处在任务特定超参与手工特征空间，换设备/人群时窗设置可能需重搜；NPVH 召回仍偏低，反映该类异质性更大。


# A Hierarchical Feature Engineering Framework for Automated Classification of Phonotraumatic and Non-Phonotraumatic Vocal Hyperfunction

- 论文编号：3437
- 报告人：June-Woo Kim
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26x_interspeech.pdf

## 问题
颈表加速度计可监测日常嗓音过度功能（VH），但多依赖单特征时间平均，忽略动态与源–滤波生理耦合；PVH 与 NPVH 子类型在自然场景下仍难稳健区分。

## 方法
在 NeckVibe 上分层构造特征：(i) 静态分布（mean/SD/P5/P95/偏度/峰度/IQR 等，含 vocal dose）；(ii) 一/二阶差分动态描述；(iii) 相对变异比率（如 ΔSD/mean）；(iv) 生理动机耦合项（如 CPP/spectral tilt、CPP/H1–H2、CPP/ΔSD、IBIF naq/ΔSD 等）。仅 voiced 帧聚合到受试者级；缺失 IBIF 在 ML 中按折内中位数填补。用 Welch t + BH-FDR 做单变量检验；RFECV（XGBoost）选特征后比较 LR/SVM/RF/XGBoost/LightGBM；分层 10-fold 按受试者分组。

## 实验与结果
CV：PVH 最佳 AUC 0.891±0.04（耦合+逻辑回归）；NPVH 最佳 0.728±0.10（耦合+LightGBM）。PVH 大量特征 FDR 显著且效应大；NPVH 无特征通过 FDR。官方测试：PVH AUC 0.917，NPVH 仅 0.579。SHAP 显示 PVH 多特征分布式贡献，NPVH 更依赖高阶动态且不稳定。

## 结论
PVH 近乎可用线性/多变量结构分离，耦合特征有增益；NPVH 与对照分布重叠大，当前手工特征不足。作者建议未来用原始波形 SSL 捕捉非平稳微颤等线索。

## 点评
把“特征层次是否带来增量”做成可消融对照，并用统计显著与 ML 对照解释 PVH/NPVH 不对称，方法清晰。弱点是测试集 NPVH 崩塌暴露日级汇总对功能失调类不够；任务表述在文中多为 vs 匹配对照，与挑战“vs 全部非目标”不完全一致时需注意解读。


# Attention-Based Multiple Instance Learning with Tabular Stacking for Ambulatory Detection of PVH and NPVH

- 论文编号：2355
- 报告人：Kiran Yerpude
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yerpude26_interspeech.pdf

## 问题
PVH/NPVH 标签只在受试者级，而全日 ACC 切成大量短段，信息段难定位；既往多靠手工汇总+浅层模型，难以同时建模短期突发与跨日持续低效发声。

## 方法
双分支堆叠：预处理保留 voiced、非歌唱、设备开启帧，鲁棒去极值并显式编码缺失。(1) CatBoost：多掩码条件下日级稳健统计（含偏度/峰度/Gini/帧差等）再跨日 mean/min/max；NPVH 另加 CPP/f0 等交互特征。(2) MIL：每受试者最多 24 个 12 s 窗，1D SE-ResNet 编码 + 门控注意力池化到受试者表示，类加权 BCE+focal。(3) 5-fold Stratified GroupKFold 的 OOF 概率经分位数变换后，与差/积组成元特征，逻辑回归 stacking。

## 实验与结果
官方测试：PVH AUC 0.891（第 3），NPVH AUC 0.861（第 1）。OOF：堆叠 PVH 0.886、NPVH 0.757，均优于单分支。消融显示去掉交互特征、日级广播统计、缺失指示或分位数归一化会伤 NPVH；相对 CatBoost-only，完整系统增益很小（约 +0.001–0.002），作者强调互补与校准而非大幅刷分。

## 结论
长时分布统计与注意力 MIL 分别契合 NPVH 弥散低效与 PVH 短暂高强度事件；堆叠与校准对挑战双任务有效。未来可多任务、受试者自适应并做外部验证。

## 点评
病理假设驱动的双尺度设计与挑战榜结果（尤其 NPVH 第 1）对齐得好。诚实报告“深度分支增益有限”是优点；脆弱点在窗数/长度与手工统计空间的超参敏感，以及 NPVH 校准仍偏保守。

