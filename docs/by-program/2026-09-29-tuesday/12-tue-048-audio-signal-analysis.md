# Audio signal analysis

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
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

本场围绕单声道与多模态音频的“可分析、可微分、可鲁棒”三条线索展开。基频与共振峰估计从传统可解释信号处理向深度可微模型靠拢：既有强调低计算开销与噪声容忍的卷积式音高估计，也有把线性预测做成可微全极点优化、以及用听觉模型构造音高匹配损失，使 DDSP 类合成链路减少对外置 F0 估计器的依赖。瞬时音高侧则把基波提取表述为波形增强问题，以应对陡峭音高变化。

情感与音乐相关工作突出跨模态融合中的信息密度与对齐问题。音频—视频情感识别用状态空间融合与特征重建预训练对抗噪声与丢帧；音乐情感则分别从“压缩冗余音频序列以对齐 MIDI”和“用指令微调与可验证数值奖励对齐 MusicLLM”两条路径推进。笑声分割则转向无监督、多语种异常检测，以缓解英语中心标注数据的局限。

音系与发音分析侧，既有基于 F0 不稳定自动标定吱嘎声起点以替代人工标注，也有对 Whisper 编码器层间孟加拉语音素可分性的探测，以及无边界层次 CNN 做音节重音检测以服务二语学习。整体上，本场共性是：在保持可解释中间表示或语言约束的同时，引入可微损失、预训练与轻量探测，以兼顾精度、效率与跨条件鲁棒性。

## 论文技术总结

# FCPE: A Fast Context-based Pitch Estimation Model

- 论文编号：500
- 报告人：Ruoyi Zhang
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/luo26_interspeech.pdf

## 问题
单声道基频估计对 MIDI 转写与歌声转换很关键；深度模型（如 RMVPE）准但算力高、难实时。需在噪声鲁棒与效率间折中。

## 方法
FCPE：16 kHz 波形→log-mel（1024/160）→嵌入，可选谐波嵌入；堆叠轻量 CNN 块（深度可分离 Conv1D + GLU/Swish，Conformer 卷积模块风格）建模帧间上下文；输出 360 维分音分箱概率（C1–B7，20 分音间隔），BCE 训练；推理用局部加权平均解码（置信度阈值 0.05）。训练用 DDSP 重合成 M4Singer/VCTK 作真值，加随机移调、噪声与 mel 掩码（空白/高斯）强迫上下文推断。

## 实验与结果
MIR-1K 干净 RPA 96.79%（10.64M 参），接近 RMVPE（90.42M，97.77%）；多 SNR 白噪/真实噪声下仍有竞争力。RTX 4090 上 RTF 0.0062，显著快于既有深度基频器。已用于 RVC/SVC 社区。

## 结论
深度可分离卷积 + 上下文训练策略可在接近 SOTA 精度下大幅降延迟与参数，适合实时应用。

## 点评
问题抓的是工业实时基频，而非再堆大 U-Net。强处是重合成真值与掩码增强对噪声鲁棒；脆弱处是分类+局部平均仍可能倍频/半频错，且重合成分布与真实歌声差距需留意。


# Audio-Visual Feature Reconstruction Pretraining for Noise-Robust Emotion Recognition

- 论文编号：605
- 报告人：Ivan Halim Parmonangan
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/parmonangan26_interspeech.pdf

## 问题
音视频情绪识别在背景噪声、混响、丢帧等真实腐蚀下，脏模态可能主导融合并压制干净模态；现有跨模预训练多对齐语义，缺少显式去噪，Transformer 对长序列又二次昂贵。

## 方法
冻结 EAT（音频）与 Timesformer（视频）提特征；两阶段自监督重建：先单模 Mamba2 编码器从腐蚀特征重建干净特征（80 epoch），再冻结编码器训交叉注意力融合 + Mamba2 解码器（200 epoch，MSE + GradNorm 调模态权重）。下游对富化后的单模 token 做 attention pooling + cosine 分类器。预训练用 LRS2+FSDNoisy18K/AIR 等；下游 RAVDESS，噪声集与预训练不重叠。

## 实验与结果
无预训练：干净音频约 77%、视频 93%；噪声音频可落到 39–70%。单模重建预训练改善噪声表现；多模融合预训练在多样噪声/干净视频组合上进一步稳定增益，显著检验优于无预训练与仅编码器预训练。相对可比 Transformer 解码器，Mamba2 方案 FLOPs 略低。

## 结论
显式跨模特征重建预训练可提升噪声下情绪识别鲁棒性，并避免脏模态拖累干净模态，同时保持高效序列建模。

## 点评
把“对齐”换成“从脏重建干净”，直接对准部署噪声。强处是腐蚀类型丰富且预训练/下游噪声源隔离；脆弱处是下游仍分模分类、RAVDESS 表演语料，以及随机划分非说话人独立可能偏乐观。


# Smooth Formant Tracking with Differentiable Linear Prediction

- 论文编号：1222
- 报告人：Bryn Luisi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/luisi26_interspeech.pdf

## 问题
经典线性预测（LP）共振峰估计快且可解释，但假设局部平稳与高斯残差、帧间独立；混合神经方法更准却难可微、难嵌入端到端系统。

## 方法
LP-DDSP：以 log-area ratio（LAR）为可优化变量，经 Forward Levinson 得全极点系数，损失为残差 L2+0.5 L1+0.1 帧间 LAR 时序正则，Adam 迭代优化，再求根得共振峰。SMELP：CNN 由 STFT 预测 LAR，同一可微 LP 损失 + 与自相关 LP 系数 MSE + 共振峰监督 MSE，LSTM 解码轨迹。VTR Formants（TIMIT 子集）评测，仅在有共振峰音素上比 RMSE。

## 实验与结果
测试集总体 RMSE：LP-DDSP 246 Hz，优于 LP 基线 378、Praat 344，接近 KARMA 254；SMELP 166，优于 LP-LSTM 171，F1/F2/F4 最低。谱包络可视化显示 LP-DDSP 轨迹更平滑。

## 结论
可微 LP 损失可同时缓解非高斯残差与帧独立假设，并支撑可解释端到端共振峰跟踪；可扩展到其他语音处理任务。

## 点评
把经典全极点物理参数接进 DDSP，保留可解释性又允许反向传播。强处是 L1+时序正则设计清楚；脆弱处是仍依赖根挑选启发式，SMELP 监督仍用自相关 LP 作伪标签可能带偏差。


# Automatic identification of the onset of creaky voice according to F0 instability

- 论文编号：1430
- 报告人：Joshua Penney
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/puggaardrode26_interspeech.pdf

## 问题
嘎裂声（creak）研究常需标出 modal→creak 精确起点（如段性 /t/ 声门化），现有自动工具多只判断窗口内有无 creak，短段与边界仍靠人工。

## 方法
用 REAPER 估 F0 与 GCI（不惩罚八度跳）；在 RMS 峰值之后搜索；取 F0 导数达峰值 ≥80% 的首帧，再选最近 GCI 为 creak 起点。在先前 AusE /hVt/ 年轻说话人已标 glottalization 的 474 项上与人工起点比 creak 时长与 G/V 比；ICC 与混合效应模型复现短/长元音差异。

## 实验与结果
时长分布相近，自动法略偏长；ICC=0.768（95% CI [.712,.813]），一致性良好但未达优秀。人工与自动标注的 G/V 模型均显示短元音比例显著高于长元音，配对模式一致。有个别负时长异常（元音后残留周期）。

## 结论
基于 F0 不稳的自动起点标注可接近人工，并在语言学分析上得出同类结论，可减轻大量手工标注负担。边界是依赖已确认含 creak 的样本，且对元音后周期敏感。

## 点评
把“八度跳是噪声”翻转成“八度跳是 creak 信号”，补齐窗口检测器缺的时间定位。强处是用真实语音学问题（G/V）做功能等价验证；脆弱处是预筛选含 creak、阈值 80% 经验化，对无大跳的 creak 亚型可能漏检。


# Less is More: Boosting Bimodal Music Emotion Recognition with Adaptive Audio Sequence Compression

- 论文编号：1552
- 报告人：Dinghao Zou
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zou26_interspeech.pdf

## 问题
音频+MIDI 双模态音乐情绪分类中，预训练音频特征序列远长于紧凑 MIDI（信息密度失衡），全局池化抹掉瞬态，重训低帧率 tokenizer 又太贵。

## 方法
PoolingVQ：冻结 MERT-95M / MIDI-BERT；K-means 初始化 VQ 码本量化音频帧；滑窗（5 帧、步长 3，约压到 25 Hz）按窗内唯一码数 U 选 Avg / 加权 Avg / Max 池化，约压短 2/3。融合用简单拼接（MIDI 插值对齐）或两阶段交叉注意力；损失 CE+VQ commitment。EMOPIA（≤60s）与 VGMIDI（≤130s）四象限分类。

## 实验与结果
Cross-Attention+PoolingVQ：EMOPIA Acc/F1 0.8953/0.8955，VGMIDI 0.600/0.6018；macro-F1 超 BFAM 约 12.5%（EMOPIA）与 5.48%（VGMIDI）。简单拼接在 EMOPIA 亦已很强（0.8837/0.8844）。

## 结论
码本引导的自适应池化可在不重训骨干下压缩冗余音频序列并提升双模态融合，达到所述 SOTA。

## 点评
问题抓的是序列长度不对称而非再设计大融合器；“变化大 max、平稳 avg”贴近音乐动态。脆弱处是规则阈值启发式、强依赖 MIDI 可用性，以及 VGMIDI 绝对分数仍偏低显示域难度。


# Differentiable Pitch Matching with Auditory Models

- 论文编号：2043
- 报告人：David Marttila
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marttila26_interspeech.pdf

## 问题
DDSP 合成常用 MSS 损失，但对频率参数梯度振荡，迫使依赖外部 f0 估计器；谱域损失（含 SOT）在缺失基频等“感知音高≠谱峰”时仍易失效。

## 方法
用可微 CARFAC 听觉模型得多通道活动；帧级构造稳定听觉像（SAI，ACF 或 TTI）、耳蜗图与音高图；对音高图做音色归一（按耳蜗能量去加重）后，用 1-Wasserstein + L1 定义听觉音高距离 L_APD。在纯音匹配任务上对目标（正弦、缺失基频谐波、方波、真唱元音）用梯度下降估频率，报告粗/细梯度方向正确率（CGA/FGA）与最小损失到真音高的音分误差。

## 实验与结果
TTI-2048 在多数目标上 CGA 最高（如 160 Hz 正弦 94.3%，缺失基频 95.8%），细尺度亦强；相对 OrigMSS/SOT 在缺失基频与复杂音色上更不易陷到远离真音高的极小。部分设定仍有数百音分偏差。

## 结论
基于听觉模型的可微音高距离可为频率参数提供更信息丰富的梯度，朝摆脱外部 f0 估计器的端到端 DDSP 迈进一步。边界是合成匹配任务、非完整训练管线。

## 点评
用缺失基频等感知用例打穿“谱=音高”假设，音色归一是关键工程点。强处是梯度方向指标设计清楚；脆弱处是计算贵、真唱元音仍难，且尚未嵌入完整 DDSP 训练证明端到端收益。


# Layer-wise Probing of Whisper's Encoder Representations for Bengali Phone-like Units

- 论文编号：2199
- 报告人：Munim Thahmid
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thahmid26_interspeech.pdf

## 问题
多语语音编码器哪一层对音位信息最线性可分，在孟加拉语与监督 ASR（Whisper）上研究不足；说话人混叠评测也偏松。

## 方法
OpenSLR53 子集 2000 句；MMS 强制对齐 uroman 转写，按规则合并为 phone-like 标签；冻结 Whisper-small/medium/large-v3 编码器，帧中心三分之一池化，说话人独立线性探测（可选 MLP）。对照组：wav2vec2-XLSR、英语 MFA+LibriSpeech；另做置信过滤、ABX、时长分层、送气/卷舌对比等。

## 实验与结果
峰值 Macro-F1：small L8/12=0.837，medium L15/24=0.858，large-v3 L26/32=0.860；相对深度约 0.63–0.81。large-v3 末层仅降约 2 pp，XLSR 末层降约 14 pp。送气塞音/塞擦音早期即可分，鼻音/咝音推动中层增益。英语 MFA 锚点亦在中后层。

## 结论
孟加拉语 phone-like 可分性在 Whisper 中后层最强；监督 ASR 预训练比 SSL 更能把音位细节保留到更深编码器层。边界是 uroman/MMS 标签非规范音位库。

## 点评
严格说话人独立 + 缩放曲线，把“中层音位峰”推广到南亚语与 Whisper。强处是鲁棒控制齐全；脆弱处是对齐噪声与罗马化坍缩音位对立，解释需限在送气/卷舌等稳定对比。


# Aligning MusicLLM with Emotion using Instruction Tuning and Feedback-Driven Alignment

- 论文编号：2293
- 报告人：Takuya Hasumi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hasumi26_interspeech.pdf

## 问题
MusicLLM 在 MIR 上强，但情绪回归（arousal/valence）常不优于数据集均值；缺少把连续分数当显式目标的训练。

## 方法
冻结音乐编码器 + 可训投影与 LLM 解码器。先指令微调：GPT-4o 模板生成伪 QA，下一词似然学分数格式。再反馈对齐：GRPO，奖励为解析失败 −200、否则 −(预测−真值)²。数据 DEAM、MERGE；并测与 MusicQA 联合训练是否伤开放问答。

## 实验与结果
仅 IT：回归有限；IT+FDA（无 MusicQA）DEAM R² arousal/valence 达 0.56/0.55，MERGE 0.55/0.29。含 MusicQA 时 IT+FDA：DEAM 0.48/0.35、MERGE 0.50/0.24，同时 BLEU/METEOR/ROUGE 基本保持。开源 Qwen2-Audio/Phi-4-Multimodal 零样本 R² 为负。

## 结论
指令微调可赋予粗回归能力，可验证数值奖励的反馈对齐显著 refinement（尤其 valence），且可与 MusicQA 共存。边界是仍难全面超过专用编码器/探测基线。

## 点评
把 LLM 回归从“会说话”推进到“平方误差可优化”，GRPO 避开评论家网络很务实。强处是保持开放问答；脆弱处是模板填分格式依赖、MERGE 半自动标签噪声，以及相对 MusicFM probing 的绝对差距。


# MultiLinguahah : A New Unsupervised Multilingual Acoustic Laughter Segmentation Method

- 论文编号：2352
- 报告人：Sofia Callejas
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/callejas26_interspeech.pdf

## 问题
笑声分割通常依赖昂贵人工标注且数据偏英语；监督 SOTA 在多语、野外声学条件下不稳定。

## 方法
MultiLinguahah（无监督）：声源分离或双声道相减去语音 → 能量阈值切事件 → BYOL-A 编码（可在目标无标训练集上继续自监督）→ Isolation Forest 把笑声当异常。评测 StandUp4AI（多语新标）、AudioSet（人工插入笑声）、Friends、Kuznetsova；IoU@0.3/0.7 的 Recall/F1；对比 Gillick、Omine、Liu 及与 Omine 融合。

## 实验与结果
美式脱口秀上 Omine 仍更强（IoU0.3 F1 0.679 vs 0.506）；Friends TV 上本文 0.910/0.735 超 Liu 0.878/0.503；法语/西语等非英语脱口秀上 MultiLinguahah 或 Omine+本文组合常优于纯监督基线。短笑声上相对 Omine 优势更明显。

## 结论
无监督异常检测在多语与多域笑声分割上更稳健；英语室内监督模型不跨语。可与监督模型互补。

## 点评
把笑声的跨语声学共性当成“可隔离异常”，避开标注瓶颈。强处是多语新标注与域覆盖；脆弱处是能量阈值敏感、依赖分离质量，英语脱口秀上仍落后强监督。


# Boundaryless Speech-to-Syllable Representations with Hierarchical CNN for Linguistically Inspired Automatic Stress Detection

- 论文编号：3144
- 报告人：Namrata Mokshagundam
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mokshagundam26_interspeech.pdf

## 问题
英语音节重音检测对 CALL 关键，但既有方法依赖人工边界或强制对齐，标注贵且对齐误差会传导；部分“无边界”法仍用音素边界。

## 方法
全边界无关：自监督帧级嵌入 → 编码器抓上下文 → 分层 CNN+池化把帧序列压成固定最大音节数表示 → 非自回归或自回归解码器输出每音节重音概率。损失用 BCE 或 Post-net2.0（强制一词恰一重音）。真音节数来自 ISLE 标注用于截取输出。评德语（GER）、意大利语（ITA）L2 英语学习者。

## 实验与结果
Post-net2.0 CNN：GER 94.86%、ITA 96.24%，相对边界相关与先前无边界 SOTA 最高增益约 18.67%/16.12%。作者称持续优于 DNN、LSTM 与既有方法。

## 结论
分层时间压缩可直接学 speech-to-syllable 表示，结合语言学单重音约束，在无显式切分下达到高准确重音检测。边界是仍需已知音节个数截断输出。

## 点评
核心是用 CNN 层级下采样替代对齐，抓住 CALL 部署痛点。强处是 Post-net2.0 注入语言学先验；脆弱处是“无边界”仍依赖数据集给的音节数 n，以及表演/朗读 ISLE 与自发口语差距。


# Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement

- 论文编号：3202
- 报告人：Junya Koguchi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koguchi26_interspeech.pdf

## 问题
瞬时基频估计（IPE）需要从含谐波与噪声的语音中提取基波再算瞬时频率，但传统基于自相关、相位偏差等准则的通道选择在域外信号与未见噪声下脆弱，帧级离散估计又难以平滑跟踪 vibrato、chirp 等连续变化。

## 方法
将基波滤波表述为增强问题：Wave-U-Net 以语音波形为输入、直接回归基波波形，再对其解析信号求瞬时频率，从而省去复杂滤波器组的通道选择。训练损失为基波与残差（谐波+噪声）的 MAE 以保证混合一致性，并加带幅度掩码的瞬时频率 MAE（λ=5）；幅度低于 −100 dB 阈值的区域不计入 IF 损失。网络 L=6 层上下采样，输出 tanh，其余 Leaky ReLU，上采样用插值而非转置卷积以减轻混叠。

## 实验与结果
训练/评测覆盖 Bagshaw、Keele、CMU ARCTIC、PTDB-TUG、MOCHA-TIMIT、MIR-1K、MDB-stem-synth（共约 20.67 小时，说话人/歌手/乐器不重叠），噪声来自 NOISEX92、QUT-NOISE（30% 概率、SNR 0–30 dB）。对比 IRAPT、Halcyon、NINJAL。干净条件 RPA50：Proposed 88.47，Halcyon 86.80，NINJAL 84.87，IRAPT 83.84；SNR 0 dB 时 Proposed 仍 86.40，而 NINJAL 降至 62.35、Halcyon 76.30。CAPRICEP 调制响应显示干净条件下 NINJAL 随机分量更小，噪声下 Proposed 更稳，作者推测下采样混叠可能残留谐波。

## 结论
DNN 直接提取基波后再做 IPE，可省略通道选择，并在强噪声下优于确定性 IPE。未来拟改进抗混叠下采样并用于实际语音/歌声分析。

## 点评
做法抓住的是“先可靠滤出单正弦再求导相位”这一 IPE 链路中最脆的一环，用增强式回归替代启发式通道打分，自然带来噪声鲁棒。相对 NINJAL 等在干净强调制上的精度，代价是相位细结构可能受网络混叠影响；适用边界更偏含辅音、噪声的一般场景，而非纯元音 vibrato 精分析。

