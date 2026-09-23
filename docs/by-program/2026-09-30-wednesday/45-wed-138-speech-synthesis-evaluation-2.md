# Speech Synthesis Evaluation 2

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：7
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场讨论合成语音主观/自动评测的偏差、标注成本与任务覆盖：MOS 中的性别评分偏差、无人类标注的训练动力学伪标签、成对比较主动采样、表达性客观化框架、跨口音编解码/TTS MOS 基准，以及多音乐体裁歌唱合成诊断基准。

共同主题是：人类评分并非中性；偏好测试可更灵敏但需智能选对；自动预测器应减少对大规模人类标注的依赖；评测对象从自然度扩展到口音相似性、表达性维度与体裁可分性。

## 技术内容

### MOS 偏差、无人类标注与主动成对采样

**MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment**（论文 67；Wenze Ren）  
系统分析 MOS 性别偏差：男性听者持续给出更高分，差距在低质量语音最明显，且难用简单校准消除；聚合标签训练的自动 MOS 模型偏向男性感知标准。摘要提出用抽象二值群体嵌入学习性别特异评分模式，以提升总体与分性别预测准确率。

**TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation**（论文 449；Natacha Miniconi）  
从多个 TTS 模型不同训练检查点收集合成语音，并以迭代索引与损失等训练元数据作伪标注，训练无需人类感知标签的质量预测器。摘要称跨语言与数据集上，迭代标注与人类标注相关。

**Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation**（论文 446；Korin Richmond）  
比较 AB/BWS 成对测试中的随机选对与两种主动采样（排序法与信息增益 ASAP）。摘要称 ASAP 能揭示更多显著差异；同等测试时长下 BWS 比 AB 更有效，ASAP 进一步放大该优势。

### 表达性、口音与多体裁歌唱评测

**Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment**（论文 2408；Zhiyu Lin）  
从情绪、韵律与自发性三维把人类表达性感知映射为客观分数；少于 500 条标注即可与专家评分达到 SRCC=0.85。摘要称据此策展约 14K 表达性话语构建双语 ExpressiveSpeech，并微调 S2S 模型以提升听感表达性。

**CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents**（论文 1273；Wen-Chin Huang）  
发布覆盖 24 个系统、32 名说话人、十种口音、4000 条重合成/TTS 样本的 MOS 基准，收集 25 名听者 19,600 条自然度/说话人相似/口音相似标注。摘要指出说话人相似与口音相似关系紧密、客观指标预测力，以及听者与说话人同口音时的感知偏差。

**MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres**（论文 137；Wenhao Feng）  
提出覆盖 10 大类、26 子类的多体裁歌唱合成诊断基准与自动乐谱对齐流水线。摘要称代表模型体裁区分弱、跨体裁声学特征高度相似；零样本体裁适应收益有限，而轻量体裁特异继续训练可显著提升。

## 本场要点

- MOS 存在质量依赖的性别评分偏差，并会传入自动模型。
- TTS 训练动力学可提供无人类标注的质量伪监督信号。
- 主动采样（尤其 ASAP）使成对偏好测试在同等时长下更有检验力。
- 表达性可被三维客观化并反哺数据策展与 S2S 微调。
- 口音与多体裁基准暴露当前编解码/TTS/SVS 在多样性维度上的评测缺口。

## 覆盖核对

- 67 | MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment
- 449 | TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation
- 446 | Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation
- 2408 | Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment
- 1273 | CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents
- 137 | MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres
