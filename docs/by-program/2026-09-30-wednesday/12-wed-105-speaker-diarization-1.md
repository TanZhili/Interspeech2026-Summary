# Speaker Diarization 1

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：4
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖说话人日志（diarization）的空间增强、分割骨干、角色感知域适应、目标说话人打分校准、球面变分聚类、印度多语联合基准、基于音频语言模型的分离，以及音视频主动说话人检测与大音频语言模型端到端日志识别。主线是提升重叠语音、任意说话人数与领域迁移下的可靠性。

空间 DOA 线索被注入序列到序列神经日志；Retention Network、角色感知半监督与 GMM 分数校准分别改进分割、课堂师生角色与短段验证。聚类后端出现面向超球面嵌入的 SphereVBx，简化 EEND-VC。资源与范式上，Indic DiarBench 覆盖印度 22 种法定语言；LlaSep 用离散令牌因果 LM 生成式分离；RT-ASDNet 统一实时音视频主动说话人检测；GLSC-SDR 用全局–局部说话人分类增强 LALM 端到端能力。

## 论文技术总结

# Spatially-Augmented Sequence-to-Sequence Neural Diarization for Meetings

- 论文编号：3473
- 报告人：Li Li
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26la_interspeech.pdf

## 问题
会议场景重叠、混响、说话人嵌入不可靠，多数神经说话人日志化仍只靠声学；空间方位是正交线索，但如何把稳健 DOA 注入可在线/离线的序列日志化模型仍缺清晰方案。

## 方法
SA-S2SND：用 SRP-DNN 估计多说话人 DOA（按帧 IDL 迭代峰检测，至多 2 源），将方位概率矩阵上采样后线性投影，残差加到 S2SND 编码器特征。骨干含 ResNet 提取器、Conformer 编码器与对称检测/表征解码器；多通道时再加交叉通道注意力。两阶段训练：Part A 单通道音频 + DOA（含仿真伪 DOA）；Part B 升级多通道 + DOA。损失 BCE + ArcFace。推理沿用 S2SND 滑窗，可在线后再离线重解码。

## 实验与结果
AliMeeting 远场阵列（NARA-WPE 去混响），无 oracle VAD、无 collar。Small 单通道加 DOA：总 DER 在线 16.03→15.35、离线 13.59→12.59（相对约 4.2%/7.4%）。8 通道 + DOA 相对仅声学基线进一步下降（如 Small E4 在线/离线 12.93/10.84）。Medium + 复合数据 + DOA 离线 DER 10.40，优于文中列出的若干对比系统（含 WavLM-Large 报告 10.80）。多说话人子集增益更大。

## 结论
显式 DOA 与交叉通道建模互补，统一支持单/多通道与在线/离线；仿真 DOA 减轻对匹配多通道语料依赖。未来需加强多说话人 DOA 稳健性。

## 点评
把 DOA 当“方位位置编码”注入，比盲通道融合更可解释；两阶段训练路径清晰。SRP-DNN 每帧最多 2 说话人与会议中 >2 重叠少见的统计相符，但极端重叠仍是盲区。SOTA 对比窗口/预训练条件不完全对齐，数字宜结合协议解读。


# Bidirectional Retention Network-based Segmentation Model for Speaker Diarization

- 论文编号：1032
- 报告人：Jian You
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/you26b_interspeech.pdf

## 问题
EEND-VC 在短窗上做局部分割再聚类，可处理重叠与任意说话人数，但局部分割后端常见 RNN/注意力/Mamba；需在长上下文复杂度与重叠建模之间找更合适的序列骨干。

## 方法
在 Pyannote/DiariZen 管线内，用 WavLM Base+（可学习层加权）前端 + 双向 Retention Network（BiRetNet）后端替换 BiLSTM。Retention 采用 chunkwise recurrent（块长 100 帧≈2s），γ=1 避免衰减；4 个 BiRetNet 块，powerset 损失（N=4, K=2）。嵌入 ResNet34-LM，VBx 聚类。训练两阶段：冻结 WavLM 再可选联合微调；可按数据集做域适应。

## 实验与结果
复合训练集约 952h。冻结 WavLM、无域适应时，BiRetNet 域内 macro DER 15.8%，优于 LSTM 17.3、Attention 17.9、Mamba 16.2。联合微调 + 域适应（S7）macro 15.0%，AISHELL-4 9.9%、VoxConverse 8.5% 达文中所列 SOTA；DIHARD III 约降 4.5 点。3 块 6.5M 后端仍优于更大 Mamba；chunk=100 整体最优。CPU 上 RTF≈1.5，内存随窗长缓增。

## 结论
BiRetNet 作为 EEND-VC 局部分割后端在多数集合上优于 LSTM/Attention/Mamba；与 WavLM 微调及域适应结合可达强综合表现。代码已公开。

## 点评
控制前端与公平对比后端是亮点；Retention 线性复杂度对长窗友好。增益幅度相对 Mamba 不大，SOTA 声明依赖域适应与 Optuna 调参。NOTSOFAR-1 仍难，说明高密度重叠场景瓶颈未必只在后端选择。


# Role-Aware Semi-Supervised Domain Adaptation for Teacher-Student Speaker Diarization

- 论文编号：155
- 报告人：Zhen Liao
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liao26_interspeech.pdf

## 问题
通用说话人日志化到课堂老师–学生场景会因远场、噪声与标注稀缺而失效；教育分析需要的是角色（教师 vs 学生）而非个体 ID，学生侧是“多对一”粗标签，重叠时传统 PIT 难以解耦。

## 方法
发布 TSSD 数据集（45 场标注 26.57h + 174 段未标注 110.20h）。框架：源域复合数据预训练 DSE-CBM（冻结 WavLM + ConBiMamba），再 Mean Teacher 半监督域适应。监督支路用 Role-Aware Union Loss：C>2 通道中选一作教师，其余 max 并集拟合集体学生标签，诱导通道特化。一致性用 PIT-MSE 对齐学生/教师模型输出排列。推理 ECAPA-TDNN + AHC。

## 实验与结果
TSSD 测试：开源管线 DER 26–35%；监督微调 21.42%；Mean Teacher 基线 19.77%；加 Role-Aware Union → 17.75%（confusion 5.20→2.70）；加 PIT-MSE → 17.80%；二者结合 16.95%（0s collar；0.25s 为 12.67%）。标注/未标注比 r=1.0 最优。可视化显示 Union 损失在多学生重叠时能激活多通道而非压成单通道。

## 结论
粗角色监督 + 半监督域适应可把课堂声学解成可聚类的角色流；TSSD 与方法为教育场景角色日志化提供可扩展范式。

## 点评
把“身份区分”改成“角色并集”切中课堂标注现实，confusion 下降与通道可视化相互印证。依赖教师多为单说话人的假设；学生侧特化质量仍受粗标签上限约束。开源数据与代码对低资源课堂研究有直接价值。


# Leveraging Diarization Labels for Robust Score Calibration in Target Speaker Tagging via Gaussian Mixture Modeling

- 论文编号：896
- 报告人：Hee-Soo Heo
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/heo26_interspeech.pdf

## 问题
Target speaker tagging（TST）需在日志化后给片段贴注册说话人身份；对话片段长短不一导致验证分数方差大，同标签平均可聚合会话信息，但欠聚类会把异说话人分数混在一起，朴素平均很脆。

## 方法
对每个日志标签下的验证分数集拟合两成分 GMM（EM）：一成分对应正确聚类片段，另一吸收误聚类；每片段取其后验最大成分的均值作校准分。对比 Label-level 全平均与同标签 Top-K 近邻平均。日志化用高分辨率嵌入 + 谱聚类；识别用 ECAPA/ResNet + AS-Norm。标签段数 <5 时不校准。

## 实验与结果
TST-Bench（合成，>204k 段）：ECAPA 上 GMM 在 FAR=0.5% 时 DIR 93.64%，相对 Baseline 88.79%、Label-level 81.82%；ResNet293 等同趋势。ICSI 真实会议：GMM 多数工作点最优或并列最优。C=2 在严格 FAR 最优；C=1 几乎无校准，C≥3 放宽 FAR 略有收益但严格点不稳。方法跨嵌入架构有效。

## 结论
用会话内分数分布的混合建模，可在利用日志标签聚合的同时显式抗欠聚类；两成分是容量与估计稳定性的较好折中。信道/设备多峰留待未来。

## 点评
问题诊断清楚：短段方差 + 欠聚类不对称伤害。GMM 校准几乎零训练成本、嵌入无关，工程可插拔。严格 FAR 上相对 Label-level 的巨大反差是核心卖点；对极短簇或分数近单峰时收益有限属预期 graceful degradation。


# SphereVBx: Spherical Variational Bayes Clustering for Simplified EEND-VC Diarization

- 论文编号：2224
- 报告人：Petr Pálka
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/palka26_interspeech.pdf

## 问题
现代说话人嵌入多在单位超球上、角间隔训练，VBx 仍用高斯 PLDA 后端；EEND-VC 第二阶段常依赖滤短嵌、滤后余弦重分配等启发式。需要与超球几何匹配、能简化聚类流程的贝叶斯方法。

## 方法
SphereVBx：保留 VBx 变分推断，将 PLDA 换成 T-PSDA（vMF 说话人/先验），在超球上做混合聚类；简化版用 GMM 替代 HMM。特殊设置 d=D、κ_b=0、κ_w=1 得无预训练参数的 SphereVBx-PF（相似度与余弦单调相关）。EEND-VC 中用时长可靠性权重替代丢弃短嵌；可选 Multi-Stream 变体在窗内联合分配以强制 cannot-link。

## 实验与结果
级联 VAD+VBx+OSD：SphereVBx 平均 DER 22.1 vs VBx 22.7，PF 22.2。EEND-VC（固定 DiariZen 局部模型）：Baseline 平均 12.65（MSCE 0.37）；SphereVBx 12.52；MS-SphereVBx-PF 12.48。多数集合持平或略优，同时去掉短嵌过滤与事后余弦重分配等启发式。

## 结论
超球贝叶斯聚类在级联管线提升聚类，在 EEND-VC 上性能相当或更好且第二阶段更简洁；PF 变体免后端预训练，便于部署。实现已开源。

## 点评
把“余弦常常胜过 PLDA”收进 VBx 概率框架，理论与工程对齐得好。EEND-VC 上绝对 DER 降幅不大，价值主要在简化与统一约束/可靠性加权。对嵌入几何假设强，非单位范数后端需另议。


# Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages

- 论文编号：2484
- 报告人：Deovrat Mehendale
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mehendale26_interspeech.pdf

## 问题
印度语 ASR 进展多在单说话人；会议/对话需联合日志化与说话人归因 ASR，但现有基准几乎不含 22 种法定印度语，且常把日志化与 ASR 拆开评，掩盖短段/重叠上的级联失败。

## 方法
发布 Indic DiarBench：约 108h，覆盖全部 22 种 scheduled 语言。近场会议 ~53h（22 语）、远场 ~27h（前 8 语）、YouTube in-the-wild ~28h（前 10 语）。人工校正说话人归因转写 + RTTM；支持英–印语码混的两种转写规范。指标：无 collar DER、cpWER、WDER。评测能联合输出 ASR+日志化的商用 API 与多模态 LLM（不含纯日志化模型）。

## 实验与结果
时长加权：Indic 特化 Sarvam DER 16.0 / cpWER 38.8 / WDER 33.1 最优；AWS 23.5 / 43.7；其他 API 与 GPT-4o/Gemini 明显更差（Gemini DER 74.0 但 WDER 尚可）。错误分解：Sarvam 较均衡；LLM 以 Miss 为主。重叠率与 DER/cpWER 强相关；近场高重叠语（如 Telugu、Maithili、Dogri）更难；Dravidian 近场 cpWER 约高 Indo-Aryan 5 点。

## 结论
开放基准填补印度多说话人归因转写空白；联合评测显示特化管线领先，通用 LLM/API 在时间戳与小话语上仍弱。数据偏评估用，in-the-wild 仅 10 语。

## 点评
22 语 + 三声学条件 + 联合指标，对包容性语音技术很有建设性。只评“能联合输出”的系统公平于应用场景，但排除 Pyannote 等使与学术日志化文献不可直接比。码混双规范降低假 WER 惩罚，设计务实。


# Speaker Separation via Audio Language Modeling

- 论文编号：2864
- 报告人：Luca Lanzendörfer
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lanzendoerfer26b_interspeech.pdf

## 问题
传统分离依赖连续时频表示、掩码/PIT 与任务专用结构；离散编解码令牌虽已支撑 TTS 等生成，盲多说话人分离能否用因果语言模型从混合令牌一次解码出各说话人流仍少探索。

## 方法
LlaSep：XCodec2 将混合与各源编为 50Hz 离散令牌；Whisper-small 语义特征线性投影作条件；在 LLaSA-1B 骨干上监督微调，自回归生成最多 4 路说话人令牌流（特殊说话人分隔符）。构建 MLSEE-Conversation：MLS/Emilia/EuroSpeech 合成约 15k 小时、7 语、多种重叠模式。推理采样多次取均值。

## 实验与结果
LibriCSS：平均 DER 23.43%（PixIT 32.65%；掩码基线因固定两路输出 DER 极高）；DNSMOS-OVRL 3.13、ScoreQ-NR 3.95、ScoreQ-Ref 0.37，均优于对比。MLSEE 2 说话人 DER 28.11%、4 说话人 43.79%，仍优于 PixIT。CallHome 英/德：DER 24.84 vs PixIT 30.20，感知质量明显更高。生成流感知干净，但非字面复现源波形，内容保真依赖编解码与令牌准确率。

## 结论
令牌级语言模型可作为多说话人分离/日志化的可行范式；音质优势明显，说话人数增多时自回归误差累积。代码、检查点与数据开源。

## 点评
把分离写成“从混合前缀生成多流”，与掩码路线形成清晰对照：音质换可逆性。DER 仍不算低，且与固定两输出基线对比时对方吃亏。对真实电话场景零样本仍有效，说明合成对话预训练有迁移；4 说话人退化提示序列长度是瓶颈。


# RT-ASDNet: Unified, Real-Time Active Speaker Detection

- 论文编号：448
- 报告人：Okan Köpüklü
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kopuklu26_interspeech.pdf

## 问题
现有音视频主动说话人检测多为多阶段：外部门脸检测 → 每人提特征 → 分类，计算随人数线性增长，难实时，且无法端到端。需单次前向、与人数无关的统一检测。

## 方法
RT-ASDNet：音频流 SincDSNet（原始波形 sinc 卷积 + DSConv）；视频流 3D-CNN + FPN/MSF（可变形卷积融合多尺度），在滑窗关键帧（最后一帧）上做无锚框检测。音频嵌入空间广播后与视觉特征拼接；CenterNet 式热图（说/不说两类）+ 尺寸 + 偏移头。端到端训练于 AVA-ActiveSpeaker；损失 focal + L1。

## 实验与结果
验证集 IoU≥0.5 mAP：3D-ResNet-18 在 16 帧 288² 达 75.8，RTF 0.009（RTX 6000）；轻量 MobileNet/ShuffleNet mAP 75.3/70.9。32 帧约 77.3，64 帧 77.3 饱和；分辨率升至 352² 达 77.5。与 SOTA 离线/因果方法（mAP 90+，但用真值人脸只做分类）不可直接比；本文作为联合检测+分类的实时基线。人脸更大、人数更少时更好。

## 结论
首次将 ASD 做成单阶段联合人脸定位与说话分类，推理代价与场景人数无关，适合实时；精度与强离线分类器仍有差距，但协议更难。

## 点评
问题定义清楚：常数时间/帧比刷分类 mAP 更贴部署。与“给真值框再分类”的文献比分不公，作者已说明，作为新任务设定基线合理。分类仍受益于更长时上下文而定位不依赖，设计与损失分工一致。


# Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition

- 论文编号：774
- 报告人：Yuhang Dai
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dai26b_interspeech.pdf

## 问题
LALM 端到端说话人日志化与识别（SDR）在语义转写上强，但说话人可分性弱：对话数据少、缺少显式说话人表征优化，声学相近说话人易混淆。

## 方法
GLSC-SDR：在 Qwen2.5-Omni-7B 上用 LoRA 联合训练 SDR 与说话人分类。GLSC：对高质量单说话人段提 ERes2Net 嵌入，HDBSCAN 聚类得全局标签；簇内说话人再局部重编码得局部标签，拼接为层次监督。数据经 ASR 质量过滤（WER>30% 或插入错误>2 丢弃）。无需改 LLM 骨干结构。

## 实验与结果
AliMeeting / AISHELL-4 / AMI-SDM：GLSC-SDR 的 cpWER 分别为 25.43 / 23.49 / 23.32，优于同骨干 SFT（26.77 / 26.34 / 27.16）及若干相关工作；SCA 与 Δcp 同步改善。消融显示仅全局或仅局部分类弱于 GLSC。簇数过少/过多损害 cpWER。

## 结论
层次全局–局部说话人分类可增强 LALM 的说话人判别而不牺牲转写，在会议基准上达到有竞争力或更优表现，且不依赖大规模真实对话仿真。

## 点评
把 SV 式度量学习思想接到 LALM 多任务，而不堆额外说话人编码器，工程上干净。层次标签依赖嵌入聚类质量；过滤规则可能丢掉难例。相对 TagSpeech 等，优势在联合优化而非架构增补。

