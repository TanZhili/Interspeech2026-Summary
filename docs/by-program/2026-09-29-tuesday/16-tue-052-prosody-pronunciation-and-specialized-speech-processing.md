# Prosody, Pronunciation and Specialized Speech Processing

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：10
- 论文数：7
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场以韵律重音、声调识别与发音评估为核心，并延伸到儿童语音音系过程推断、手语视频生成与日语带声调标记的评估型识别。句子重音检测普遍借助 Whisper 等预训练表征，但强调：单层固定嵌入不足以刻画相对、语境依赖的韵律凸显，因而出现双流显式声学建模、跨层加权融合，以及把词重音作为辅助任务并用词跨度正则约束句重音概率。普通话声调侧则探索仅依赖超音段 F0、多粒度结构化嵌入与可拆卸辅助分支的 Transformer。

儿童与评估场景更强调可解释结构输出：PhonLLM 联合恢复规范音素序列与音系过程标签，并用规则增强规模化注入过程监督；日语口语评估识别器输出带重音标记的音位标签，以多任务音高损失与双估计器融合缓解标注稀缺。手语视频生成则把 LLM 赋能的姿态潜空间扩散规划与运动条件视频扩散结合，并用 Flow-GRPO 多维奖励对齐。整体上，本场从“端到端黑盒分类”转向显式韵律/音系结构、辅助任务与层融合。

## 技术内容

### 句子重音检测与韵律感知架构

**ProWhistress: An Enhanced Dual-Stream Transcription Architecture for Prosody-Aware Sentence Stress Detection**（论文 1303；Hujian Gu）提出增强双流转写架构，显式融入声学建模以保留细粒度韵律；并针对普通话句重音数据稀缺构建约 12 小时合成 SinoStress-Syn 与约 3 小时真人 SinoStress-Real。摘要称在五个英/普通话数据集上显著优于对比方法。

**A Novel Sentence Stress Detection Framework Leveraging Auxiliary Word-Stress Modeling and Loss Optimization**（论文 1494；Tien-Hong Lo）将句重音检测与辅助词重音建模结合，并提出 word-span stress regularizer（WSR）使 token 级 SSD 概率集中于重读词跨度；在 TinyStress-15K 上相对强基线更优，完整配置取得最佳 SSD 结果。

**WhiSSDapt: Adaptive Fusion of Whisper Layer Embeddings for Sentence Stress Detection**（论文 3236；Jhansi Mallela）观察到单层 Whisper 表示无法最优捕获韵律线索，提出可学习加权层融合框架，以自适应组合不同层的声学与上下文信息用于句重音检测。

### 声调、儿童音系与日语评估识别

**Learning Contextualized Tonal Contours from F0: A Core-Auxiliary Branched Transformer for Mandarin Tone Recognition**（论文 1747；Yi-Fen Liu）仅用超音段 F0，以核心轮廓编码器 C-Net 学习上下文化声调表示，训练期可拆卸辅助分支经交叉注意力与层特异注意力池化提供额外梯度；并编码音节/词/块多粒度 F0 嵌入与节奏编码器 R-Net。摘要称即使推理去掉辅助分支，仍持续优于单分支基线并提升效率。

**PhonLLM: Joint Phone Recognition and Phonological Process Inference for Child Speech**（论文 3378；Ilja Baumann）提出音系过程推断：先无文本条件预训练音素识别，再融合期望音素嵌入与下采样音频 token，由单一解码器输出规范音素与显式过程标签；规则增强管线可规模化注入过程监督并支持多语 G2P 替换。摘要称联合建模提升标注准确率并降低音素错误率。

**Building Tailored Speech Recognizers for Japanese Speaking Assessment**（论文 1672；Yotaro Kubo）构建输出带重音标记音位标签的日语评估识别器；以含音高模式聚焦的多任务辅助损失，以及音标串估计器与文本 token 序列估计器的融合缓解数据稀疏，并报告相对通用多语识别器更有利。

### 手语视频生成

**SignMatch: Aligning Pose Latent Diffusion via Multi-dimensional Rewards for Sign Language Video Generation**（论文 1546；Rongjie Huang）以 LLM 赋能的姿态潜空间扩散规划器耦合运动感知手语视频扩散渲染器，并用 Flow-GRPO 以语义与视觉奖励优化姿态潜空间生成器（不更新视频渲染器）；在 RWTH-2014T 与 How2Sign 上报告翻译类语义指标与视觉指标的一致增益。

## 本场要点

- 句重音检测从单层 Whisper 嵌入转向双流声学建模、辅助词重音与跨层自适应融合。
- 普通话相关工作同时覆盖 F0-only 声调识别与句重音合成/真人基准建设。
- PhonLLM 把儿童发音偏差解释为可结构化的音系过程标签。
- 日语口语评估强调音位+重音标记输出与音高辅助多任务。
- SignMatch 用多维奖励对齐姿态规划与手语视频生成。
- 韵律任务普遍需要显式约束相对凸显与词/句跨度一致性。

## 覆盖核对

| paper_id | title |
|---|---|
| 1747 | Learning Contextualized Tonal Contours from F0: A Core-Auxiliary Branched Transformer for Mandarin Tone Recognition |
| 1303 | ProWhistress: An Enhanced Dual-Stream Transcription Architecture for Prosody-Aware Sentence Stress Detection |
| 1494 | A Novel Sentence Stress Detection Framework Leveraging Auxiliary Word-Stress Modeling and Loss Optimization |
| 3236 | WhiSSDapt: Adaptive Fusion of Whisper Layer Embeddings for Sentence Stress Detection |
| 3378 | PhonLLM: Joint Phone Recognition and Phonological Process Inference for Child Speech |
| 1546 | SignMatch: Aligning Pose Latent Diffusion via Multi-dimensional Rewards for Sign Language Video Generation |
| 1672 | Building Tailored Speech Recognizers for Japanese Speaking Assessment |
