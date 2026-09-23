# Grand Special Challenges Poster Showcase
- 日期：Monday 28 September 2026 / 时间：14:30-16:30 / 形式：Poster（Area 14）/ 论文数：13
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场是多项 Interspeech 2026 Grand / Special Challenge 的集中展示：跨域音频表征、语用意图语音翻译、野外无监督多语语音（UPS）、阿拉伯语发音偏误评测（IQRA）、以及颈表振动语音过度功能监测（NeckVibe）。挑战综述与参赛系统并列，便于对照任务设定、数据约束与领先方法。

表征学习侧，BEST-RQ-2 把掩码预测拆成 contextualize-then-predict 并用 ViT 上下文编码器；WQ-Fusion 用动态门控融合 Whisper 与 Qwen；UPS 相关工作则在大规模异构网络音频上强调从零或继续预训练，并揭示离散单元 CPT 与对比式 CPT 在内容–说话人信息上的权衡，以及本地诊断与官方 probe 排名不一致的风险。

发音评测挑战把声学保真与规范音先验解耦：prompt-free CROTTC-IF、两阶段域适应融合框架，以及挑战综述报告的 F1 大幅跃迁，共同指向“真实偏误数据 + 细粒度对齐/适应”驱动进展。NeckVibe 则转向真实世界周监测：日内时间分割、层次化特征（含耦合特征）、表格模型与 MIL 注意力堆叠，是 PVH/NPVH 检测的主要方法论差异；摘要普遍称 PVH 相对更易分、NPVH 更难。

语用翻译挑战明确以语用保真为目标，并报告最佳系统相对人类评分仍有差距，同时反思评测方法本身的优劣。

## 技术内容

### 跨域音频表征与 UPS / 语用挑战

**BEST-RQ-2: Contextualize-Then-Predict, a Two-Step Approach for Self-Supervised Audio Representations**（论文 2488；presenter：Ludovic Tuncay）
保留冻结随机投影离散目标，引入两步 contextualize-then-predict：ViT 只处理未掩码频谱区域，轻量预测器推断掩码目标后丢弃。摘要称相对 Conformer 的域表现转移，主要增益来自分解阶段；在 X-ARES / XARES-LLM 上总体迁移更优且推理算力不变。

**WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation**（论文 3228；presenter：Gongping Huang）
双编码器融合 Whisper 与 Qwen，经 Adaptive Feature Modulation 与逐元素门控注意力做动态特征选择。摘要报告在 Interspeech 2026 Audio Encoder Capability Challenge（Track A）上总体分数 0.836，优于最强单编码器基线。

**The Interspeech 2026 Challenge on Transfer of Pragmatic Intent in Speech-to-Speech Translation**（论文 390；presenter：Nigel G. Ward）
挑战针对现有语音到语音翻译不优先语用保真的问题，介绍设计、数据、评测与提交结果。摘要称最佳系统在 5 分制上落后人类 1.2 分，并讨论评测方法的优劣。

**BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation for Unsupervised Speech in the Wild Challenge**（论文 2966；presenter：Prakriti Subedi）
BiMamba2 编码器按 HuBERT 式掩码离散单元预测，在 67 语约 250 小时无标注数据上训练，目标含伪标签预测、语种识别与 VICReg。官方评估给出 ARI、语种 macro-F1 与 CER，并分析本地–官方指标尺度与检查点排序差异。

**Content–Speaker Trade-offs in Continued Self-Supervised Pre-Training Across SSL Paradigms for Multilingual Speech**（论文 2946；presenter：Danner Schlotterbeck）
在三类 SSL 架构上研究 CPT：重算伪标签并恢复掩码预测可改善标签稀缺域的内容任务，但种子与数据规模方差大；离散单元模型 CPT 会损害说话人可分信息，对比式模型无此效应。摘要强调未充分记录的任务特化模式。

**Unsupervised Speech in the Wild Challenge: Learning Robust Multilingual Representations**（论文 3113；presenter：Rafael Mosquera Gómez）
介绍 UPS 2026：在异构网络音频条件下评测表征学习，仅允许用 Unsupervised People's Speech 从零或继续预训练，评测语种识别、少样本 ASR 与说话人聚类。摘要给出数据集小时量级与任务设定。

### 阿拉伯语 MDD（IQRA）与颈表振动（NeckVibe）

**Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis**（论文 711；presenter：Haopeng Geng）
针对 CTC 忽略短暂偏误线索与显式规范先验偏向目标音的问题，提出 prompt-free 框架：CROTTC 强制单调帧级对齐，IF 策略隐式注入偏误信息。摘要报告 L2-ARCTIC 与 Iqra'Eval2 上的 F1。

**IQRA 2026: Interspeech Challenge on Automatic Assessment Pronunciation for Modern Standard Arabic (MSA)**（论文 2445；presenter：Yassine El Kheir）
第二届 IQRA 挑战综述，引入真实人类偏误数据 Iqra_Extra_IS26；提交系统涵盖 CTC-SSL、两阶段细调与大型音频语言模型等。相对首届 F1 跃升 0.28，归因于新架构与真实偏误数据。

**A Fusion-Aware Two-Stage Framework for Mispronunciation Detection and Diagnosis in Low-Resource Modern Standard Arabic**（论文 1553；presenter：Gongping Huang）
预训练编码器加因果扩张时序卷积，两阶段先学母语/合成映射再适应稀缺真实学习者数据，并做多检查点集成与 N-gram 重打分。摘要报告 QuranMB.v2 测试 F1 及相对基线提升，称位列 IqraEval.2 前列。

**The Interspeech 2026 NeckVibe Challenge: Voice Disorder Detection via Real-World Monitoring of Neck-Surface Vibration**（论文 3049；presenter：Ahmed Yousef）
发布一周日常活动颈表加速度计监测数据集（含 VH 与对照、监测小时量级）。摘要给出 PVH/NPVH 基线与最佳 AUC，并归纳优胜方法：日内变异、非线性模型、言语–歌唱线索与特征比等。

**Temporal Partitioning of Vocal Activity for Detecting Vocal Hyperfunction from Neck-Surface Accelerometer Data**（论文 1435；presenter：Władysław Średniawa）
集成框架对 PVH/NPVH 分类，关键是对日间特定发声活动时段做时间分割。官方测试集上摘要报告 PVH AUC 与名次，以及 NPVH AUC 相对基线的提升。

**A Hierarchical Feature Engineering Framework for Automated Classification of Phonotraumatic and Non-Phonotraumatic Vocal Hyperfunction**（论文 3437；presenter：June-Woo Kim）
层次特征含静态、动态、比值与刻画源–滤波器相互作用的耦合特征。单变量分析对 PVH 可分性强、对 NPVH 有限；摘要称耦合特征对两任务关键，并给出 PVH/NPVH AUC。

**Attention-Based Multiple Instance Learning with Tabular Stacking for Ambulatory Detection of PVH and NPVH**（论文 2355；presenter：Kiran Yerpude）
受试者级 CatBoost 表格模型与固定窗帧级特征的深度 MIL（1D 残差网 + 门控注意力池化）堆叠。摘要报告官方测试 PVH/NPVH AUC 与名次。

## 本场要点
- 挑战场同时覆盖表征学习、语用翻译、野外多语 SSL、阿拉伯语 MDD 与真实世界嗓音监测。
- BEST-RQ 两步预测与跨编码器动态融合，是跨域音频表征的两条主路径。
- UPS 凸显大规模野生音频预训练约束，以及 CPT 下内容–说话人信息权衡与本地诊断不可靠性。
- IQRA 进展与真实偏误数据、帧级对齐/两阶段域适应密切相关。
- NeckVibe 中 PVH 相对 NPVH 更易检测；时间分割、耦合特征与 MIL+表格堆叠是领先思路。
- 语用意图翻译仍显著落后人类，评测方法本身亦被挑战组织者反思。

## 覆盖核对
`2488 | BEST-RQ-2: Contextualize-Then-Predict, a Two-Step Approach for Self-Supervised Audio Representations`
`3228 | WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation`
`390 | The Interspeech 2026 Challenge on Transfer of Pragmatic Intent in Speech-to-Speech Translation`
`2966 | BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation for Unsupervised Speech in the Wild Challenge`
`2946 | Content–Speaker Trade-offs in Continued Self-Supervised Pre-Training Across SSL Paradigms for Multilingual Speech`
`3113 | Unsupervised Speech in the Wild Challenge: Learning Robust Multilingual Representations`
`711 | Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis`
`2445 | IQRA 2026: Interspeech Challenge on Automatic Assessment Pronunciation for Modern Standard Arabic (MSA)`
`1553 | A Fusion-Aware Two-Stage Framework for Mispronunciation Detection and Diagnosis in Low-Resource Modern Standard Arabic`
`3049 | The Interspeech 2026 NeckVibe Challenge: Voice Disorder Detection via Real-World Monitoring of Neck-Surface Vibration`
`1435 | Temporal Partitioning of Vocal Activity for Detecting Vocal Hyperfunction from Neck-Surface Accelerometer Data`
`3437 | A Hierarchical Feature Engineering Framework for Automated Classification of Phonotraumatic and Non-Phonotraumatic Vocal Hyperfunction`
`2355 | Attention-Based Multiple Instance Learning with Tabular Stacking for Ambulatory Detection of PVH and NPVH`
