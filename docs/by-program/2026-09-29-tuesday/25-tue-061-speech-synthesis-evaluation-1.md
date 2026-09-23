# Speech Synthesis Evaluation 1

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：7
- 论文数：6
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场集中反思 TTS 主观评测的效度与维度：大规模成对偏好需语言控制与多感知维度标注；应用情境会显著改变同一系统得分；“自然度”并不等同于跨域“适宜性”；非语言发声（NV）需要功能分类学基准；训练期需要可解释的语音学客观指标；指令式 TTS 的性别偏见呈多维社会线索绑定效应。共同信息是：单一 MOS/自然度分数不足以指导系统选择与优化。

印度语族大规模成对评测（10 语、7 系统、逾 12 万比较）示范可扩展但高方差场景下的多维标注；应用情境实验与跨域适宜性研究则指出生态效度与目标用例必须进入实验设计。NV-Bench、元音空间指标与 ITTS 偏见分析分别补齐副语言可控性、训练期可监测口音相似性，以及提示组合带来的交互偏见。整体趋势是评测协议本身成为一等研究对象。

## 技术内容

### 大规模偏好、应用情境与跨域适宜性

**Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages**（论文 3357；Ashwin Sankar）在 10 种印度语言上用逾 5K 母语/语码混合句评测 7 个 SOTA TTS，收集逾 1900 名母语者给出的 12 万+ 成对比较，并覆盖可懂度、表现力、音质、生动性、噪声与幻觉等 6 维；采用 Bradley-Terry 等模型分析偏好。

**Application context in speech synthesis evaluation: A problem and a solution**（论文 747；Fritz Seebauer）比较四套合成系统在四种应用情境下的评分，发现情境显著改变系统得分，且情境影响因系统而异，提示无指定应用情境的系统对比存在混淆；并讨论数字场景收集评分的相关发现（以官方摘要为准）。

**Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation**（论文 3392；Dominika Woszczyk）在 AI 助手、朗读、演员、动画角色与自发说话者五域测量五套 SOTA TTS 的适宜性与类人度；摘要称适宜性跨域独立于自然度变化，朗读域较强而表现力域仍难，优化一域可能损害他域，且自然度分数倾向惩罚风格化、奖励自发性。

### NV 基准、训练期语音学指标与指令 TTS 偏见

**NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation**（论文 2211；Qinke Ni）提出基于功能分类学的 NV-Bench，含 1,651 条多语野外话语、14 类 NV 及配对真人参考；双维协议包括指令对齐（副语言字符错误率 PCER）与声学保真（相对真实录音的分布差距），并评测多样 TTS、开发两个基线。

**Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training**（论文 1579；Pasindu Udawatta）提出 Vowel Space Overlap 与 Procrustes Normalised Disparity，在训练步量化合成与真值元音空间形状相似度；在两种口音微调设定上计算指标并做感知测试，报告与口音相似性感知显著相关。

**The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS**（论文 66；Kuan-Yu Chen）将提示建模为社会地位、职业刻板与人格描述的组合，分析开源 ITTS 中社会维度相互调制的系统交互偏见；并关联预训练文本编码器语义先验与训练数据偏斜，指出通用多样性提示不足以覆盖这些绑定效应。

## 本场要点

- 成对偏好评测需多维感知标注与语言控制以抑制方差。
- 应用情境是评分的显著混淆因素，必须写入实验设计。
- 自然度 ≠ 适宜性；跨域优化存在权衡。
- NV 合成需要功能分类基准与可控性/保真双指标。
- 语音学元音空间指标可在训练期提供可解释监测。
- 指令 TTS 性别偏见来自多维线索绑定，而非单变量提示。

## 覆盖核对

| paper_id | title |
|---|---|
| 3357 | Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages |
| 747 | Application context in speech synthesis evaluation: A problem and a solution |
| 3392 | Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation |
| 2211 | NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation |
| 1579 | Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training |
| 66 | The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS |
