# Audio Coding and Signal Analysis

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Long Oral（跨领域长文口头）；论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要中出现的表述归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场围绕神经音频编解码、表征稳定性与声学事件分析展开。一类工作把评价轴从传统 Rate–Distortion 扩展到稳定性，指出高保真重建与下游可用离散/连续 token 并不总是同向；另一类工作则在可变帧率、残差矢量量化训练策略上挖掘比特预算与频带一致性。

可变帧率与谐波感知残差划分，都试图在“总比特率严格可比”或“不改推理结构”的约束下改进重建质量与可懂度，说明编解码优化正从单纯堆叠码本转向更精细的时间/频率资源分配。

睡眠相关声事件检测两篇工作把麦克风筛查与可解释分类连接起来：一条路径把自适应线增强器的置信度直接注入注意力与特征调制；另一条路径用孪生相似度作为决策证据，强调临床可解释性。二者共同反映医疗声学分析对“不是黑盒分数”的需求。

Assembly Calculus 框架则提出与深度学习并行的生物启发式稀疏组装体路径，在边界检测与音素/指令分类上给出无需权重训练的边界 F1 与有限分类准确率，提示本场同时容纳主流神经编解码与替代计算范式的对比讨论。

## 技术内容

### 神经编解码：稳定性、可变帧率与谐波残差

**Representational Instability in Decoupled Audio Encoders**（论文 2487；Ehsan Variani）提出 Stability–Rate–Distortion（SRD）评价轴，认为仅优化波形重建会带来 Stability Penalty。作者引入 Continuous Edit Distance（CED）度量几何漂移，并分析 EnCodec、SoundStream、Whisper 等编码器；连续潜变量对微扰相对稳健，而矢量量化瓶颈会把序列打碎，形成 Quantization Penalty。在 26 种方言上还观察到低资源方言稳定性崩溃的“Language Tax”，指出低比特率下高保真与表征稳定经验上冲突。

**DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection**（论文 2984；Hoyeol Sohn）面向可变帧率神经语音编解码。DTM 保留选中的编码器 token，用可学习 `<MASK>` 填充被掩位置，并传输二值 keep-mask；Path Length Equalization（PLE）以近似线性时间选择边界。在严格匹配总比特率协议下，作者报告相对固定帧率基线的重建质量与可懂度提升。

**HARP: Harmonic-Aware Residual Partitioning for Neural Audio Codecs**（论文 1759；Qiaoyu Yang）针对 RVQ 频率纠缠问题：将残差量化阶段按频率有序分组，每组精炼目标频带，同时解码器仍可访问更低频率，使泛音在基频语境中重建。HARP 只改训练损失、不改推理结构；摘要称在语音、音乐与通用音频上优于标准 RVQ 与并行分带，MUSHRA 亦显示感知改进。

### 睡眠声事件与生物启发式语音分析

**Sleep Sound Event Detection Powered by Learnable Multi-Resolution Adaptive Line Enhancer**（论文 130；Chanwoo Park）提出 ACF-SED：把 Adaptive Line Enhancer 的逐帧置信度图直接注入 Transformer 注意力偏置与特征调制。Multi-Resolution ALE Bank 聚合不同去相关延迟的并行 NLMS 滤波器，Confidence-Guided Cross-Path 以门控交叉注意力耦合事件与噪声流。在 Audio-Polygraphy Dataset for Sleep Apnea Analysis 上，摘要报告 Event-F1、Segment-F1 与 PSDS 的检测结果，并支持端到端 AHI 估计。

**Similarity as Evidence: An Explainable Siamese Framework for Snore Sound Classification**（论文 2153；Mengkai Sun）做四类鼾声分类：轻量卷积学 ℓ₂ 归一化嵌入，联合 semi-hard triplet 与类别平衡交叉熵，再用 Class Centroid 非参数分类；以支撑样本与时频激活模式做解释。在 Munich-Passau Snore Sound Corpus 上，摘要给出 macro-recall 从 wav2vec2 的 0.401 提升至 0.638，并在加性噪声下保持稳健；删除与扰动测试用以验证解释忠实性。

**Beyond Deep Learning: Speech Segmentation and Phone Classification with Neural Assemblies**（论文 2041；Trevor Adelson）基于 Assembly Calculus，将连续语音编码为组装体兼容尖峰模式，并跨层次时间尺度组织多区域结构。在边界检测上报告音素/词边界 F1 分别为 0.69/0.61（无需权重训练），音素与指令识别准确率分别为 47.5%/45.1%，主张 AC 动力学系统可作为深度学习的替代路径。

## 本场要点

- SRD/CED 把“重建保真”与“token 稳定、跨方言鲁棒”拆开评价，直接质疑低比特音频 token 的下游可用性假设。
- VFR 侧信息必须计入总比特率；DTM-Codec 用掩码填充与 PLE 边界选择回应这一约束。
- HARP 用训练期谐波感知残差划分改善频带一致性，且推理与标准 RVQ 相同。
- 睡眠声学两条路线：ALE 置信度融合注意力 vs. 孪生相似度可解释分类。
- Assembly Calculus 给出稀疏、Hebbian 式语音切分/分类结果，形成与主流编解码并行的计算视角。
- 本场整体强调：比特与结构约束下的质量提升，以及表征对扰动、方言与临床解释的脆弱面。

## 覆盖核对

| id | title |
|---|---|
| 2487 | Representational Instability in Decoupled Audio Encoders |
| 2984 | DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection |
| 1759 | HARP: Harmonic-Aware Residual Partitioning for Neural Audio Codecs |
| 130 | Sleep Sound Event Detection Powered by Learnable Multi-Resolution Adaptive Line Enhancer |
| 2153 | Similarity as Evidence: An Explainable Siamese Framework for Snore Sound Classification |
| 2041 | Beyond Deep Learning: Speech Segmentation and Phone Classification with Neural Assemblies |
