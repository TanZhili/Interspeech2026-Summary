# Audio Coding and Signal Analysis

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕神经音频编解码、表征稳定性与声学事件分析展开。一类工作把评价轴从传统 Rate–Distortion 扩展到稳定性，指出高保真重建与下游可用离散/连续 token 并不总是同向；另一类工作则在可变帧率、残差矢量量化训练策略上挖掘比特预算与频带一致性。

可变帧率与谐波感知残差划分，都试图在“总比特率严格可比”或“不改推理结构”的约束下改进重建质量与可懂度，说明编解码优化正从单纯堆叠码本转向更精细的时间/频率资源分配。

睡眠相关声事件检测两篇工作把麦克风筛查与可解释分类连接起来：一条路径把自适应线增强器的置信度直接注入注意力与特征调制；另一条路径用孪生相似度作为决策证据，强调临床可解释性。二者共同反映医疗声学分析对“不是黑盒分数”的需求。

Assembly Calculus 框架则提出与深度学习并行的生物启发式稀疏组装体路径，在边界检测与音素/指令分类上给出无需权重训练的边界 F1 与有限分类准确率，提示本场同时容纳主流神经编解码与替代计算范式的对比讨论。

## 论文技术总结

# Representational Instability in Decoupled Audio Encoders

- 论文编号：2487
- 报告人：Ehsan Variani
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/variani26_interspeech.pdf

## 问题
现代音频编码器常按 Rate–Distortion 优化波形重建，再把连续或离散表示交给 LLM/ASR 等下游模型。解耦（open-loop）场景要求表示对无关声学扰动保持语义稳定，但现有高保真神经编解码对细微扰动极度敏感，离散 token 可发生近乎整体重排（Discrete Representation Inconsistency）。缺少统一、架构无关的表示漂移度量，也未把稳定性作为与 rate/distortion 并列的评价轴。

## 方法
提出 Stability–Rate–Distortion（SRD）框架，指出严格追求重建会带来 Stability Penalty。信息分解上将比特率拆成语义信息与 nuisance 信息。度量方面：离散序列用 Unit Edit Distance（UED，语料级微平均 Levenshtein）；连续潜变量提出 Continuous Edit Distance（CED），先 L2 归一化到单位超球面，再用带插入/删除代价（权重=2.0）与几何替换代价的编辑距离递推，并对齐长度做微平均。并讨论 Soft-CED 作为可微训练惩罚的前景。实验在 MSEB SVQ 干净语音上，用 FFT–SpecAugment–iSTFT（时间掩码至多 20%、频率掩码至多 15%）制造扰动，每条干净样本生成 5 个随机增强；分析 EnCodec、SoundStream、Whisper 等，并覆盖多方言设定。

## 实验与结果
抽取全文在实验细节中部截断，定量表格未完整保留。摘要与已读实验设计表明：连续潜变量对轻微扰动相对更稳，但 VQ 瓶颈会把小幅漂移打成截然不同的离散序列（Quantization Penalty）；对 Whisper 类语义编码器，在高资源语言上离散语义 token 较稳，在低资源方言上因语言先验弱而稳定性崩溃（Language Tax，文称评估 26 种方言）。作者强调低码率下高波形保真与表示稳定性 empirically 冲突。

## 结论
作者主张把表示稳定性作为编解码评价的第三轴；高保真重建不等于下游可用的稳定 token。连续表示尚可抵抗小扰动，量化与低资源语言条件会放大脆弱性。

## 点评
核心贡献是把“给机器用的 token 稳不稳”从重建质量里拆出来，并用 CED/UED 做成可比较的几何漂移度量，针对 RVQ 边界穿越导致的级联 token 翻转尤其有解释力。正文抽取在实验段截断，方言税与各编码器的具体数字无法从全文文件完整核对；合成 SpecAugment 也刻意排除真实噪声，结论外推到日常声学条件需谨慎。


# DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection

- 论文编号：2984
- 报告人：Hoyeol Sohn
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sohn26_interspeech.pdf

## 问题
变帧率（VFR）神经语音编解码可按信息密度分配时间分辨率，但侧信息（位置/时长）计入总码率后，相对固定帧率（FFR）的收益常不明确或仅部分指标有改善；既有工作也常缺同架构、严格匹配总码率的对照。问题是：在显式计入侧信息的 matched-total-bitrate 协议下，VFR 能否稳定优于 FFR。

## 方法
DTM-Codec（约 127M）基于 TAAE 两阶段 Transformer，前端/后端改为 STFT/iSTFT，瓶颈改为单码本 VQ（|C|=16384，14 bit/token）。Dynamic Token Masking 在 Stage-1 与 Stage-2 之间保留被选 token、掩码位填可学习 `<MASK>`，并传输二值 keep-mask 供位置感知解码。边界选择用 Path Length Equalization（PLE）：沿编码器轨迹余弦距离累积路径长度，O(N) 等分放置边界；训练时用 Robbins–Monro 控制器把 keep ratio 调到目标（文中 r=0.5）。总码率 = 内容码率 + 位置码率（Stage-1 每步 1 bit）。FFR 对照用均匀 stride 掩码、无位置比特，并以更大码本（|C|=65536，16 bit）匹配总码率。对抗+多尺度 mel/特征匹配训练；数据仅 LibriSpeech-960。

## 实验与结果
LibriSpeech test-clean（2620 句）上多档总码率对比外部系统与 matched FFR。例如 DTM@80Hz 总 1280 bps：UTMOSv2 3.42、UTMOS 4.20、PESQ 2.95、STOI 0.95、Spk-Sim 0.87、WER 2.98；@50Hz/800 bps：3.39 / 4.22 / 2.66 / 0.93 / 0.78 / 2.91；@40Hz/640 bps：3.43 / 4.19 / 2.49 / 0.92 / 0.74 / 3.27；@25Hz/400 bps：3.37 / 4.11 / 2.07 / 0.90 / 0.58 / 4.73，低码率相对 VARSTok/TAAE 等 WER 与感知指标明显更好。全文在 Table 2（FFR→VFR 相对增益）处截断，同架构 matched-rate 的逐指标相对变化数字未完整保留。

## 结论
作者认为在严格计入位置比特的匹配总码率设定下，掩码式 VFR（DTM）配合 PLE 可在低–中码率相对 FFR/外部系统带来广泛重建与可懂度提升；保留原 token 向量并用 `<MASK>` 填空优于平均/重复式上下采样。

## 点评
贡献在于把 VFR 争论拉回“总码率真匹配”这一可检验设定，并用 mask+位置比特替代合并/时长编码，使解码器知道哪些位置是真 token。正文 Table 2 截断，同架构 FFR 对照的完整相对增益需对照 PDF；仅用 LibriSpeech、单码本设定下的结论外推到多域音频也需保留余地。


# HARP: Harmonic-Aware Residual Partitioning for Neural Audio Codecs

- 论文编号：1759
- 报告人：Qiaoyu Yang
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26k_interspeech.pdf

## 问题
标准 RVQ 各阶段频谱纠缠：截断码本时高低频内容被不可预测地去掉，码率缩放不平滑。并行分带编码虽让频带特化，但碎片化潜空间、丢失跨频相干（谐波相位/幅度关系）。需要一种在单一 encoder–decoder 与统一 token 流内施加频率层级、同时保留谐波上下文的训练策略。

## 方法
HARP 只改训练损失，推理与标准 RVQ 相同。将 L=9 个 RVQ 阶段分为 K=4 组（默认 3-2-2-2）：Bass 0–1 kHz、Low-mid 1–4 kHz、High-mid 4–10 kHz、Treble 10–22 kHz。Cumulative decoding：每组用截至该组的累积量化潜变量解码，使高频组在低频已重建的上下文中学习。Subband contribution supervision：对各组波形增量（经 stop-gradient 隔离先前组梯度）做频带加权 mel 重建损失。Soft band weighting：可学习高斯中心/带宽加权 mel 箱，加固定地板 β 避免硬截断伪影。标准重建、对抗与 commitment 损失仍作用于最终输出。

## 实验与结果
摘要称在语音、音乐与通用音频上优于标准 RVQ 与并行分带，并在两种码率条件的 MUSHRA 上有感知提升；预训练模型与脚本公开。抽取全文在 soft band weighting 公式处截断，客观指标表与听测具体分数未出现在全文文件中。

## 结论
作者认为仅通过训练期累积解码与软分带监督，即可在标准 RVQ 架构内形成低频优先的频率层级，使丢弃后期阶段时先丢高频、质量更平滑，并保留谐波相干。

## 点评
思路抓住 RVQ“频谱无结构”与并行分带“有结构但丢跨带上下文”的互补缺陷，用训练目标而非新架构解决，部署成本为零，这对 token 流要接 LM 的场景很实用。正文实验段抽取不完整，具体增益与失败样本类型无法从文本核验；软目标是否在噪声/非谐和内容上仍稳定特化，是自然的脆弱点。


# Sleep Sound Event Detection Powered by Learnable Multi-Resolution Adaptive Line Enhancer

- 论文编号：130
- 报告人：Chanwoo Park
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26_interspeech.pdf

## 问题
阻塞性睡眠呼吸暂停（OSA）常规 PSG 成本高、不便筛查；麦克风事件检测是潜在低成本替代。传统 Adaptive Line Enhancer（ALE）多只作预处理，滤出的增强谱送入网络，而自适应滤波内部的逐帧置信度图被丢弃。需要把 ALE 内部状态真正注入 SED 注意力与特征调制，以更好区分鼾声、低通气与阻塞性呼吸暂停并支持 AHI 估计。

## 方法
提出 ACF-SED。Multi-Resolution ALE Bank（MRAB）在共享 STFT 上并行三个可学习步长的 NLMS 滤波器，decorrelation delay/长度分别为 (τ,L)=(1,8)、(3,15)、(6,24)，输出事件/噪声分量与置信度图 Ci=|E|²/(|E|²+|Z|²)。双流 CNN 分别编码增强 mel 与噪声 mel；Learnable Confidence Pooler 在分辨率与频率轴上加权得到标量置信轨迹 c。Confidence-Guided Cross-Path（CCP）中事件路径用 Symmetric Confidence-Biased MHA 与 ALE-Aware Feature Modulation，噪声路径为轻量 FFN，再经门控交叉注意力融合；MLP+sigmoid 输出三类帧级概率（snore、hypopnea、obstructive apnea）。

## 实验与结果
摘要称在 Audio-Polygraphy Dataset for Sleep Apnea Analysis（APSAA）上 Event-F1、Segment-F1、PSDS 达 SOTA，并支持端到端 AHI 估计。抽取全文在 CCP 模块描述中部截断，具体对比数字与消融未保留。

## 结论
作者认为把多分辨率 ALE 置信度直接注入 Transformer 注意力与特征调制，可把经典自适应滤波状态变成 SED 的可学归纳偏置，从而提升睡眠呼吸事件检测并服务 AHI 筛查。

## 点评
设计点在于“ALE 不只是前端滤波，而是把周期性/非周期性置信度当作注意力偏置”，对医院谐波噪声与伪周期鼾声这类场景有明确物理动机。正文结果段缺失，SOTA 声明无法用数字核实；三类事件边界模糊与仅音频估计 AHI（缺真实睡眠时间）仍是临床落地的主要风险。


# Similarity as Evidence: An Explainable Siamese Framework for Snore Sound Classification

- 论文编号：2153
- 报告人：Mengkai Sun
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26f_interspeech.pdf

## 问题
鼾声音频可反映上气道阻塞部位（VOTE：Velum/Oropharyngeal/Tongue base/Epiglottis），但临床数据小、类别极不平衡、噪声与设备变异大；softmax 黑盒分类既难解释“为何判为某类”，也对扰动敏感。需要把相似度本身变成可检验的决策证据，并做忠实性/稳定性验证。

## 方法
对 4 s、16 kHz 窗计算 80-bin log-Mel（20–2400 Hz）并做 CMVN；轻量 3 块 Conv-BN-ReLU-MaxPool CNN 得到 D=256 的 ℓ₂ 归一化嵌入。联合 semi-hard triplet 与 effective-number 加权 class-balanced CE（λ=1），P×M 批采样（4×8）。推理主规则为非参数 Class Centroid（欧氏距离最近类原型），另报告 softmax 头作对照。解释：每类固定靠近质心的 support 样本，用末层卷积通道平均激活上采样为时频证据图，并与 query–support 相似度对照；另做 deletion 与扰动稳定性检验。数据为 MPSSC 官方四类划分（Train/Val/Test 共 282/283/263，T 类极少）。

## 实验与结果
摘要与已读实验设置：干净条件 macro-recall 由 wav2vec2 基线 0.401 提升至 0.638，中等加性噪声下仍具竞争力；deletion/扰动分析支持解释区域对置信度贡献与结构稳定性。全文在 baselines/推理头细节处截断，完整表与噪声档位数字未全部保留。

## 结论
作者认为在小样本、长尾鼾声分类上，度量学习嵌入 + 质心推理可提升少数类召回，并用 support 级时频证据把“像谁”变成可审计解释，而非仅后验可视化。

## 点评
把 Siamese 相似度从“更好的表征”推进到“可定量检验的证据”，对临床可解释性诉求是对症的；质心规则与 support 可视化一致，比纯 CAM 更易沟通。T 类样本极少、域偏移与设备噪声仍可能使嵌入几何塌缩；正文结果表截断，噪声鲁棒与各推理头差距需对照 PDF。


# Beyond Deep Learning: Speech Segmentation and Phone Classification with Neural Assemblies

- 论文编号：2041
- 报告人：Trevor Adelson
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/adelson26_interspeech.pdf

## 问题
深度学习语音系统依赖海量数据与反向传播，表示稠密、难组合、持续学习易灾难遗忘。Assembly Calculus（AC）以稀疏神经元集合、Hebbian 可塑性与 winner-take-all 为操作原语，生物动机更强，但既有 AC 工作假设离散可分符号输入，缺少把连续语音映射到装配、跨时间尺度组织区域、以及无全局损失时如何读出边界/类别的方案。

## 方法
两条并行 AC 管线。（1）编码：概率 mel 二值化（能量作 Bernoulli 发放概率）供边界检测；MFCC 经高斯群体编码再阈值化供分类。（2）分割：两级 refractory 区域（β=0，无权重训练），Level-1 吃帧级 mel 尖峰、Level-2 吃 Level-1 装配；变化量 c(t)=1−a(t)·a(t−1)/k 的峰作边界。（3）分类：每类一个 RecurrentArea（β>0），Hebbian/ABS 可塑性学习类特异轨迹，用共振分数 Rc 读出类别。任务覆盖连续语音中的音素/词边界检测与音素、命令分类。

## 实验与结果
摘要报告：无权重训练即可检到音素边界 F1=0.69、词边界 F1=0.61；音素与命令识别准确率分别为 47.5% 与 45.1%。抽取全文在分割方法细节处截断，数据集、基线对照与完整结果表未保留。

## 结论
作者认为 AC 动力学系统可作为深度学习之外的语音处理备选：局部可塑性即可形成边界敏感轨迹与类模板，显示稀疏装配动力学对分割与分类具有可行性。

## 点评
价值在于把 AC 从符号玩具推到真实连续语音接口，并明确区分“变则边界、稳则类别”的两种区域配置。绝对精度仍远低于现代 DL，且正文实验截断；若缺少强基线与错误分析，更宜视为概念验证而非性能竞争。

