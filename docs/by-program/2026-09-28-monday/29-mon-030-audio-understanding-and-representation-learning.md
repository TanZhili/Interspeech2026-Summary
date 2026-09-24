# Audio Understanding and Representation Learning

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster
- Area：5
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖视听 VAD、长会话目标说话人提取、脚本化检测护栏、多通道分离–日志统一、长音频层次活动语法、说话人归属副语言事件、音乐艺术字幕、并行不变语音分词，以及 AAC/少样本提示学习。共同主题是：理解任务要从“能分类”走向“抗捷径、可归因、层级一致、语义不变”。

会议/多说话人前端强调空间先验：DOA 引导免日志归因，空间信息同时进入系统与自适应仿真以降低重叠区混淆。事件理解则走向联合帧级预测与语法引导层次解析。表示学习侧，并行话语对齐把说话人探测准确率压到近随机；字幕与分类侧则用双 MoE 动态奖励路由或音频侧提示补文本提示不足。评测意识突出：SEAM 显示去掉防捷径组件会使外部泛化骤降。

## 论文技术总结

# MAC-VAD: A Modality-Aligned Cross-Attentive Framework for Robust Voice Activity Detection

- 论文编号：384
- 报告人：Bruhanth Mallik
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mallik26_interspeech.pdf

## 问题
纯音频 VAD 在噪声、混响、重叠下脆弱；音视频融合易模态坍塌，且缺少面向多模态 VAD 的大规模野外基准。

## 方法
MAC-VAD：WavelNet（可学习小波滤波）音频编码 + BiLSTM；EfficientViT（CasiaWebface/CelebA 预训练）视觉编码 + VTN；Dynamic Audio-Visual Cross Attention（对称交叉注意 + 温度门控 + 残差）。冻结 Wav2Vec 2.0 教师经适配器蒸馏；总损失含融合/单模态 CE、蒸馏 MSE、交叉注意同步 MSE。由 AVA-Speech 整理为 MMVAD（Speech vs Non-Speech + 人脸裁剪）。

## 实验与结果
WavelNet+Eff-ViT+Distil：Acc 93.52%、F1 86.39%，优于无蒸馏与单模态。DAVCA 融合 F1 高于拼接/相加/双线性/普通交叉注意。Wav2Vec 2.0 教师优于 HuBERT/xLSR/WavLM。相对 TS-TalkNet、ACLNet、LightASD、Pyannote，AUROC 97.85% 最高。MUSAN 噪声 0–15 dB 下 Acc 仍约 92%。模型 21.4M，GPU 约 21.9 ms/帧。

## 结论
模态对齐交叉注意加自监督蒸馏可显著提升野外多模态 VAD，并在噪声下保持稳健，超过代表性主动说话人检测与音频 VAD 基线。

## 点评
视觉单模态已强于音频，融合+蒸馏主要补齐召回与噪声鲁棒；DAVCA 门控针对模态失效是合理设计。MMVAD 由电影标注重标，与通用 VAD 边界定义不完全等同，跨域部署需再测。


# Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR

- 论文编号：787
- 报告人：Yichi Wang
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26m_interspeech.pdf

## 问题
长时多方会话说话人活动极不均衡且重叠多；滑窗 CSS 有跨窗身份不一致与串扰，常需额外 diarization；基于注册嵌入的 TSE 又可遇不可得或不稳。

## 方法
PATSE：以目标 DOA 为先验。TIGER 骨干 + TAC 多通道融合；空间编码器由麦克风对 IPD 与 DOA 理论相位差构造 PSF，自注意细化后经 FiLM 调制分离特征。活动感知损失：静音区残差能量 + 有声区 SNR。每目标独立抽取后 VAD 切句送 Whisper Large-v3，无需显式 diarization。发布真实房间回放数据集 LibriReplay-DOA。

## 实验与结果
LibriReplay-DOA（约 7 h，15°–120°、多种重叠比）：PATSE PT+FT 总体 WER 14.0%，优于 CSS(TIGER) oracle 分配（32.8%）与 Sortformer+GSS（38.4%）等。真实三方 TEIDAN：WER 20.50%、DER 13.83%，均优于 DSB/FastMNMF/CSS/GSS 管线。

## 结论
会议场景说话人方位相对稳定时，DOA 条件 TSE 可直接产出说话人归因流并简化下游 ASR，无需 diarization；在真实与回放数据上均优于 CSS 与级联基线。

## 点评
抓住 CSS“跨窗置换+串扰”与 diarization 边界不可靠的耦合痛点，用稳定空间先验换身份一致性，工程路径清晰。依赖 DOA 可得与说话人基本静止；极近角与极高重叠仍难，真实移动场景需另验。


# SEAM: Shortcut-Aware Real-Time Detection of Scripted vs. Spontaneous Speech for Interview Guardrails

- 论文编号：1480
- 报告人：Pranay Manocha
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kovalev26_interspeech.pdf

## 问题
稿读/自发语音分类可用于面试护栏，但标签常与语料身份、信道、录音伪迹纠缠，内部持出高分可能是捷径学习，外域一移即崩。

## 方法
SEAM：统一波形预处理（去直流、70 Hz 高通、−23 LUFS、限幅）；溯源一致的 seam-aware 采样禁止跨录音拼接；约 14 h 非语音噪声库按 40–70% 窗长混入破“干净=稿读”启发式。训练语料：People’s Speech/PodcastFillers（自发）与 LibriSpeech/Spoken Wikipedia（稿读）。DistilHuBERT + 均值池化 + MLP，仅解冻顶层 Transformer，8 s 窗。另设对抗性外部面试评测集（720 片段，风格×信道交叉）。

## 实验与结果
全量训练：内部 test Acc/AUC 0.962/0.977，外部 Acc/AUC 0.952/0.971。消融去掉噪声库与 seam 后内部 AUC 升、外部 AUC 从约 0.90 降至 0.73。8 s 窗优于 2/4/12 s；顶层解冻优于仅头或更深解冻。INT4 量化至 41.8 MB，外部性能几乎不降。多语零样本抽取文本末尾截断。

## 结论
稳健的实时稿读检测依赖捷径感知的数据与评测设计，而非更大骨干；压缩后仍可部署为人工复核的窄护栏信号，非独立裁决器。

## 点评
用“内部升、外部降”的消融直接证明捷径学习，评测设计比刷榜更有价值。外部集专有、英文为主，风格与语体/信道仍部分纠缠，护栏用途需保持人工在环。


# MCA-DCF-DS: An Adaptive Framework for Unified Diarization and Separation with Spatial Information

- 论文编号：1539
- 报告人：Shutong Niu
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/niu26b_interspeech.pdf

## 问题
DCF-DS 级联 diarization 与分离主要靠频谱线索，高重叠易崩；CHiME-8 空间管线中 GSS 重聚类降 confusion 却抬 miss，NSD 反向，存在 MI–CF 权衡。

## 方法
MC-DCF-DS：在 DCF-DS 分离输入拼接 IPD，并用 mask-MVDR 波束形成，通道级活动概率融合。MCA-DCF-DS：用 SI-SSD（长窗空间聚类）得低 CF 先验，以 NSD-MS2S 重叠检测滤除非重叠单说话人段，仿真保留空间关系的多通道适应数据；教师软标签 KL 蒸馏微调 NSD-MS2S。Whisper-large-v3 作 ASR 后端。

## 实验与结果
NOTSOFAR-1 多通道评测：MC-DCF-DS tcpWER 可至 20.17%（基线 28.28%；无 IPD/MVDR 更差；单通道 DCF-DS 31.72%）。SI-SSD 低 CF 高 MI，NSD 降 MI 抬 CF。Eval-Sim+KD：DER 13.83%，tcpWER 17.86%，优于同 Whisper 后端下的 CHiME-8 Task 2 冠军（18.74%）。

## 结论
系统级空间特征与数据级空间适应互补，可改善分离质量并缓解 diarization 的 MI–CF 权衡，同后端下超过挑战赛冠军。

## 点评
把冠军管线里暴露的 miss/confusion 跷跷板转成“用低 CF 空间先验造适应数据 + KD 控噪声标签”，工程针对性强。依赖多麦空间聚类质量与会话级适应算力；跨会议泛化与实时性仍是边界。


# Grammar-Guided Hierarchical Parsing for Long-form Audio Activity Recognition

- 论文编号：2157
- 报告人：Peng Zhang
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26da_interspeech.pdf

## 问题
长时音频活动–子活动–事件本有层级与次序，MultiAct 等按层独立解码易全局不一致，且常需多层监督。

## 方法
仅用事件检测器（SlowFast+ActionFormer）得有序事件段与类后验；从训练脚本诱导 Hierarchical Activity Grammar（PCFG）：活动→子活动序列，子活动→锚点事件夹噪声非终结符（吸收杂音/漏检）。Earley 风格 MAP 解码最大化声学证据 + λ 语法先验，输出 Act–Sub–Event 解析树，由此导出子活动切分与活动类别，训练不需子活动/活动标签。

## 实验与结果
MultiAct（约 8.97 h）。事件 mAP 几乎不变（略升）。子活动：Eval Edit 24.6→35.3，但高 IoU F1/帧准确率未必升（边界受事件提案限制）。活动：Val Top-1 73.3%，Eval 66.7%/mAUC 75.0（无高层标签）。λ≈0.3 最佳；噪声节点显著提升各指标。

## 结论
语法引导解析可在仅事件监督下恢复可解释层级结构并改善时间次序一致性；边界精度与语法权重敏感仍是局限。

## 点评
把长时活动识别从多层神经网络头换成“事件证据 + 程序语法先验”，强在可解释与跨层一致性。Edit 升而严格 IoU 不升暴露其对检测器时间粒度的依赖；语法由训练脚本诱导，开放域活动扩展成本高。


# SA-UAED: Joint Frame-Level Detection of Audio Events, Speaker Activities, and Speaker-Attributed Paralinguistic Events

- 论文编号：2486
- 报告人：Zekun Lan
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lan26_interspeech.pdf

## 问题
SED/SD 难以把笑、咳等副语言事件归因到具体说话人；细粒度标注稀缺，且通用说话人嵌入对短暂非言语突发表征不佳。T-UAED 联合 SED 与 diarization 但仍忽略副语言。

## 方法
仿真管线：脚本生成时间线 → ChatterBox-Turbo 用 LibriSpeech 参考合成说话人特异笑/咳 → PANNs 过滤 + VAD 裁剪 → 与 LibriSpeech 语音、DESED 背景按 15% 重叠混合，得 500 h LibriPara（帧级标签，50 Hz）。SA-UAED 在 T-UAED 上为笑/咳各加专用 FC，把 ECAPA-TDNN 嵌入投到独立副语言查询子空间，与事件查询并行进 Transformer 解码器。

## 实验与结果
LibriPara 测试：基线笑/咳 SB-F1 仅 0.371/0.282；SA-UAED 升至 0.476/0.473，DER≈8.07 几乎不变；共享适配器反而更差。EARS 真人素材零样本混合：笑 SB-F1 0.259→0.409，咳 0.375→0.470。通用 SED 略降（如 SB-F1 0.984→0.979）。

## 结论
专用副语言子空间 + 可控仿真数据可大幅提升说话人归因副语言检测，同时基本保持 SED/SD。未来拟做自监督对齐与开放集发声。

## 点评
抓住“言语偏置嵌入压不住笑/咳身份”这一声学失配，用解耦查询而非硬塞共享投影。仿真依赖 TTS 副语言保真；EARS 评测仍按同一混合协议，真实重叠现场泛化需再验。


# Music Artistic Captioning: Towards Translating Music into Expressive Language

- 论文编号：2618
- 报告人：Ubaid Ullah
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ullah26_interspeech.pdf

## 问题
歌剧等叙事性强、结构演变的长时音乐难以得到既忠于可闻线索又像节目单散文的长文描述；成对音–文数据稀缺，微调易过拟合措辞且难控风格。

## 方法
训练免费框架 MAC：多尺度结构分析（全局等分、MSAF 功能段、局部滑窗）→ MIR 低层声学 + MERT 高层语义/情绪聚成证据字典并口语化 → 分层上下文提示 LLM（GPT-OSS 20B）做槽位约束 JSON 字幕；一次性 Iterative Prompt Optimization 校准风格与忠实度。

## 实验与结果
短基准：MQAD 上 MAC 多项领先；MusicCaps/SongDesc 增益不一（人工标题常含 MIR 难覆盖的文化线索）。无参考艺术设定：Opera/MSD 上 Emo/Art 领先（如 Opera Art 0.55 vs FUTGA 0.35），Sem 逊于 Qwen-Omni。去掉层级上下文伤 Art；去掉 IPO 伤 Emo/Art。

## 结论
用多尺度伪证据约束现成 LLM，可在无任务微调下生成更有叙事连贯与情感对齐的长时音乐描述，跨数据集更稳健。

## 点评
把“长时幻觉”压成可审计的证据槽位，适合节目单式生成。Art/Sem 指标自建、LLM 评判有偏；证据层漏检（罕见乐器/文化语境）时仍会偏短基准上的人工标题。


# Content is What Remains: Invariant Speech Tokenization from Parallel Utterances

- 论文编号：2817
- 报告人：Laurin Wagner
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wagner26b_interspeech.pdf

## 问题
离散语义语音 token 常蒸馏自 HuBERT/WavLM，仍泄漏说话人、韵律与信道，抬高 H(z|c)，损害压缩与下游解耦。

## 方法
PINT：洞察为“同文多说者并行时内容是唯一共享因子”。Stage A 在 HuBERT-base 上用 soft-DTW 对齐并行句、词级对比、音素解码 CE；Stage B 用 EMA 教师生成共享离散目标，学生 CTC 对齐，辅以边际/正交正则（K=200）。并行语料含 ARCTIC/VCTK/ESD 等，非并行靠增强与 Kokoro 合成造伪并行。

## 实验与结果
说话人探针准确率 93.1%→1.2%；ABX 误差约降 42%；离散 WER 12.13 vs HuBERT 21.37。噪声上 token 熵近 0。同规模 LM 困惑度降约 27–30%（约 1.95 vs 2.78/2.67）。压缩：去重后约 12.6 tok/s vs 基线 ~25。消融显示需真实并行；纯合成或仅 AR/CTC 损失更弱。

## 结论
上游把 SSL 表征洗成内容不变 token，可作为编解码器的即插语义目标，比改编解码器架构更正交有效。

## 点评
用并行数据把不变性写进目标函数，比事后对比或投票更干净；情感探针仍约 32% 说明韵律未完全剥离。依赖对齐与（伪）并行语料，低资源语言需合成扩展。


# Context-Adaptive Automated Audio Captioning with Symmetric Dual-MoE and Dynamic Reward Routing

- 论文编号：2897
- 报告人：Seyun Ahn
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ahn26_interspeech.pdf

## 问题
AAC 常优化统一目标，RL 奖励又多静态加权，难以按声学场景调整生成策略与评价侧重。

## 方法
对称双 MoE：策略侧在 BART 解码器上层插入 LoRA 专家，由交叉注意状态路由（top-1）；奖励侧分解语义、语法、词汇多样性与 ATFT 细粒度音文对齐，声学全局表示动态加权；组内标准化后用 GRPO 更新。先 CE 监督再 RL。

## 实验与结果
Clotho：BLEU4 0.174、CIDEr 0.414、FENSE 0.464、MOS_n/a 最高。AudioCaps：语义与 SPIDEr-FL 领先，CIDEr 略逊纯 CIDEr-RL。消融去掉任一奖励或任一侧 MoE 均降；交叉注意路由优于纯文本/纯音频路由。词汇多样性相对 SFT 有提升但仍低于人工。

## 结论
策略与奖励双侧上下文自适应可协同提升字幕对齐与人类偏好，尤其对齐敏感指标。

## 点评
把“场景不同、该强调什么”同时写进生成与打分，比单侧 MoE 或固定奖励更一致。奖励分解与路由增加训练复杂度；AudioCaps 上 CIDEr 未全面碾压说明与 n-gram 目标仍有张力。


# Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models

- 论文编号：885
- 报告人：Hyebin Cho
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cho26_interspeech.pdf

## 问题
少样本音频分类的提示学习几乎只调文本侧，音频编码器冻结导致域移与类内声学变异难以对齐。

## 方法
ASPL：在 CLAP-HTSAT 音频管道三阶段做共享仿射调制（γ⊙X+β）——log-mel 频谱、patch embedding、早期 Swin block；参数与类别数无关。作为即插模块与 CoOp/CoCoOp/PALM 文本提示联用，编码器冻结。

## 实验与结果
11 数据集 16-shot：CoOp 平均 73.56→ASPL* 75.54；CoCoOp 76.45→ASPL 77.85；PALM 77.86→ASPL* 79.26。与动态文本提示搭配时较轻的 ASPL 常更优；与静态/类提示搭配时加结构调制的 ASPL* 更好。参数开销极小，单数据集偶有波动。

## 结论
显式调制音频表征空间可与文本提示互补，形成双侧对齐，提升少样本适应。

## 点评
把“提示”从文本 token 扩展到声学管道早期仿射，参数效率高、即插即用。增益约 1% 量级且依赖基线；CREMA-D 等上不稳定，说明频谱级调制对情感类任务未必总利。


# Audio-Language Prompt Learning for Few-Shot Audio Classification

- 论文编号：1173
- 报告人：Qisheng Xu
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26l_interspeech.pdf

## 问题
少样本 ALM 适应以文本提示为主，音频侧欠适应，声学相近类别（如吉他/贝斯）可分性不足。

## 方法
MALP（PENGI 骨干）：音频/文本特异提示做残差适配 `(1−λ)f+λP`，再经共享提示拼接融合加强跨模态对齐；先模态特化再共享对齐。仅训提示，编码器冻结。

## 实验与结果
11 数据集 16-shot 平均准确率 78.35%，相对 CoOp/CoCoOp/PALM 分别 +7.21/+4.88/+1.77。CREMA-D、RAVDESS、NS-Instruments 等细粒度集增益更明显。消融：仅音频提示 77.33、仅共享 76.89，二者合用最佳。随 shot 数增加稳步上升。

## 结论
音频特异 + 共享提示的多模态提示学习可平衡模态内判别与跨模态对齐，改善少样本音频分类。

## 点评
与 ASPL 同类问题，但用嵌入残差+共享拼接而非声学早期调制；在 PALM 同套评测上平均更高。λ 与模板固定，跨骨干/零样本设定外推未充分展开。

