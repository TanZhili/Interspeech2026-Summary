# Audio signal analysis

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：5
- 论文数：11
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场围绕单声道与多模态音频的“可分析、可微分、可鲁棒”三条线索展开。基频与共振峰估计从传统可解释信号处理向深度可微模型靠拢：既有强调低计算开销与噪声容忍的卷积式音高估计，也有把线性预测做成可微全极点优化、以及用听觉模型构造音高匹配损失，使 DDSP 类合成链路减少对外置 F0 估计器的依赖。瞬时音高侧则把基波提取表述为波形增强问题，以应对陡峭音高变化。

情感与音乐相关工作突出跨模态融合中的信息密度与对齐问题。音频—视频情感识别用状态空间融合与特征重建预训练对抗噪声与丢帧；音乐情感则分别从“压缩冗余音频序列以对齐 MIDI”和“用指令微调与可验证数值奖励对齐 MusicLLM”两条路径推进。笑声分割则转向无监督、多语种异常检测，以缓解英语中心标注数据的局限。

音系与发音分析侧，既有基于 F0 不稳定自动标定吱嘎声起点以替代人工标注，也有对 Whisper 编码器层间孟加拉语音素可分性的探测，以及无边界层次 CNN 做音节重音检测以服务二语学习。整体上，本场共性是：在保持可解释中间表示或语言约束的同时，引入可微损失、预训练与轻量探测，以兼顾精度、效率与跨条件鲁棒性。

## 技术内容

### 音高、共振峰与可微信号处理

**FCPE: A Fast Context-based Pitch Estimation Model**（论文 500；Ruoyi Zhang）提出面向单声道的快速上下文音高估计模型，用改进卷积与深度可分离卷积从 mel 谱提取特征，在噪声容忍与计算效率之间平衡。摘要报告在 MIR-1K 上 Raw Pitch Accuracy 为 96.79%，单卡 RTX 4090 上 RTF 为 0.0062。

**Smooth Formant Tracking with Differentiable Linear Prediction**（论文 1222；Bryn Luisi）提出可微全极点模型 LP-DDSP，通过优化 log-area ratios 并结合 L1/L2 与时间正则化损失，缓解经典线性预测对局部平稳与高斯残差的假设。进一步引入端到端神经共振峰跟踪器 SMELP，将可微 LP 损失纳入联合学习，并与 KARMA、Praat 等基线对比。

**Differentiable Pitch Matching with Auditory Models**（论文 2043；David Marttila）针对 MSS 等谱损失对频率参数梯度不充分、以及缺失基频等感知音高与谱峰不一致情形，基于可微计算听觉模型特征构造音色归一的周期性距离度量，在合成音高匹配任务上相对 Spectral Optimal Transport 与 MSS 给出更有信息量的梯度，面向无外置音高估计器的端到端 DDSP 训练。

**Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement**（论文 3202；Junya Koguchi）将基波滤波表述为语音增强：用 Wave-U-Net 从输入中提取基波波形，再由其解析信号的瞬时频率得到瞬时音高，并在语音、歌声、乐器与劣化语音等场景相对传统确定性方法报告更稳健的结果。

### 情感、音乐与笑声的多模态分析

**Audio-Visual Feature Reconstruction Pretraining for Noise-Robust Emotion Recognition**（论文 605；Ivan Halim Parmonangan）采用 Mamba2 状态空间融合，并在预训练阶段从受损音视频重建干净特征以学习噪声鲁棒表示，下游情感识别在噪声音频及多种视频噪声/干净设定下相对单模态特征重建预训练呈现增益。

**Less is More: Boosting Bimodal Music Emotion Recognition with Adaptive Audio Sequence Compression**（论文 1552；Dinghao Zou）针对音频相对 MIDI 的时序冗余与信息密度失衡，提出 PoolingVQ：用 VQ-VAE 量化局部音频特征得到变化强度索引，并据此动态池化压缩序列。摘要称在 EMOPIA 与 VGMIDI 上促进双模态融合并达到当时最优表现。

**Aligning MusicLLM with Emotion using Instruction Tuning and Feedback-Driven Alignment**（论文 2293；Takuya Hasumi）考察 MusicLLM 对齐 arousal/valence 回归：对比任务感知指令微调与带可验证数值奖励的反馈驱动对齐，后者在 arousal 与 valence 上相对仅指令微调有实质提升，并报告在提升情感回归的同时维持 MusicQA 能力。

**MultiLinguahah : A New Unsupervised Multilingual Acoustic Laughter Segmentation Method**（论文 2352；Sofia Callejas）将笑声分割建模为基于能量分割序列的异常检测，对 BYOL-A 表示施加 Isolation Forest；在含脱口秀、情景喜剧与 AudioSet 短音频等四个数据集上对比，强调现有方法对多语语境欠优化，而该方法在非英语设定更优。

### 音系特征、编码器探测与重音检测

**Automatic identification of the onset of creaky voice according to F0 instability**（论文 1430；Joshua Penney）基于 F0 不稳定（常伴随八度跳变）自动识别吱嘎声起点，并与既往澳大利亚英语韵尾清浊对比研究中的人工标注起点比较，报告自动方法与人工标注者表现相近，且对原研究问题的结论一致。

**Layer-wise Probing of Whisper's Encoder Representations for Bengali Phone-like Units**（论文 2199；Munim Thahmid）用 MMS 强制对齐 uroman 转写得到类音素片段，在说话人不相交设定下对 Whisper 各层训练线性探针。摘要指出 small/medium 在中后层达峰，large-v3 形成较宽的后层平台且末层退化更轻；相对 wav2vec2-XLSR，有监督 ASR 训练更利于在更深编码器层保留语音细节，并辅以 ABX、对齐置信度过滤等验证。

**Boundaryless Speech-to-Syllable Representations with Hierarchical CNN for Linguistically Inspired Automatic Stress Detection**（论文 3144；Namrata Mokshagundam）用层次 CNN 时间压缩将帧级嵌入变为音节级表示，无需显式边界，并以 Post-net2.0 损失施加“每词恰一重读音节”约束。摘要报告在 ISLE 语料德语与意大利语学习者子集上分别达到 94.86% 与 96.24%，相对边界相关及既往无边界 SOTA 有最高约 18.67% 与 16.12% 的提升。

## 本场要点

- 音高/共振峰估计并行推进：高效卷积（FCPE）、可微 LP（LP-DDSP/SMELP）、听觉模型音高损失与 Wave-U-Net 基波增强瞬时音高。
- 情感与音乐任务强调跨模态密度对齐：特征重建预训练、PoolingVQ 动态压缩、MusicLLM 反馈对齐。
- 笑声分割走无监督多语异常检测，针对英语中心标注数据局限。
- 音系侧自动化替代人工：F0 不稳定标定吱嘎起点；无边界 CNN 服务二语重音检测。
- Whisper 层间探测表明有监督 ASR 相对纯 SSL 更利于深层保留类音素信息。
- 可微性与可解释中间表示（log-area ratios、基波波形、量化索引）是贯穿本场的方法共性。
- 摘要中给出的具体指标（如 RPA、RTF、ISLE 准确率、WER 相关表述等）均仅转述官方摘要，未另行推算。

## 覆盖核对

| paper_id | title |
|---|---|
| 500 | FCPE: A Fast Context-based Pitch Estimation Model |
| 605 | Audio-Visual Feature Reconstruction Pretraining for Noise-Robust Emotion Recognition |
| 1222 | Smooth Formant Tracking with Differentiable Linear Prediction |
| 1430 | Automatic identification of the onset of creaky voice according to F0 instability |
| 1552 | Less is More: Boosting Bimodal Music Emotion Recognition with Adaptive Audio Sequence Compression |
| 2043 | Differentiable Pitch Matching with Auditory Models |
| 2199 | Layer-wise Probing of Whisper's Encoder Representations for Bengali Phone-like Units |
| 2293 | Aligning MusicLLM with Emotion using Instruction Tuning and Feedback-Driven Alignment |
| 2352 | MultiLinguahah : A New Unsupervised Multilingual Acoustic Laughter Segmentation Method |
| 3144 | Boundaryless Speech-to-Syllable Representations with Hierarchical CNN for Linguistically Inspired Automatic Stress Detection |
| 3202 | Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement |
