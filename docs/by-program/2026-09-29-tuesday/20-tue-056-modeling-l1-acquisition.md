# Modeling L1 Acquisition

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：1
- 论文数：6
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场从一语习得与自发口语加工角度考察韵律、切分、象似性、语义相关与词汇竞争。语码转换研究把语言通用的宏观韵律特征用于诊断西—英语自发语料中 CSW 与单语产出差异，并强调说话人因素；婴儿导向语上的词切分计算模型则检验“编码梯度语音细节是否必然损害边界检测”，相对成人导向语给出不同结论。习得时间（AoA）建模把词象似性与音系 surprisal/熵对照，揭示儿童与成人加工的发展性分离。

自发时长与句子语境下的词汇竞争进一步把语义/预测性推到前台：语义相关对词时长呈显著非线性效应；跨通道启动实验显示，孤立词中次音素模糊度对竞争的梯度调制在句子语境中被语境可预测性覆盖。儿童捲舌咝音部位偏移则用高频能量等摩擦噪声特征服务早期构音诊断。整体上，本场连接计算切分、信息论与心理语言学实验，突出语境与说话人变异相对纯音段表征的主导作用。

## 技术内容

### 多语韵律、婴儿导向切分与习得预测

**The Sound of Code-Switching: Prosodic Profiles of Spontaneous Spanish-English Speech**（论文 249；Debasmita Bhattacharya）在大规模西—英自发语料上，用语言无关韵律特征比较语码转换与单语产出，发现 CSW 韵律与英/西单语均有意义差异，且说话人特异因素对变异影响更大；定位为对该问题的语言可泛化、宏观与模型诊断式研究。

**Gradient phonetic detail is less detrimental to word segmentation in infant-directed speech**（论文 2920；Gabriel Scharff）在婴儿导向语上测试编码语音细节是否损害词边界检测；四种算法中两种无退化、另两种仅轻微退化，并联系 IDS 更短词、更多孤立词与更小词表等特性，对比既往 ADS 上细节编码损害切分的发现。

**Word Iconicity and Phonological Surprisal as Predictors of Age of Acquisition**（论文 1551；Alexander Kilpatrick）用机器学习与回归分析考察象似性、音系 surprisal/熵与 AoA；摘要称象似性稳健预测更早习得，而 surprisal/熵对习得效应弱且不一致，但对成人加工结果有更强预测，体现发展性分离。

### 语义相关、语境预测与儿童咝音诊断

**Non-linear Effects of Semantic Relevance on Word Duration in Spontaneous Speech**（论文 1062；Kun Sun）在 Buckeye 语料上用 GAMM 检验目标词与局部语境的语义相关是否预测词时长，在控制说话人与既有语言因素后，语义相关为词时长的显著预测变量并呈现非线性效应。

**From Words to Sentences: Contextual Predictability Overrides Phonetic Ambiguity in Lexical Competition**（论文 3106；Will Chih-Chao Chang）两项跨通道启动：孤立词复制次音素模糊度对词汇竞争的梯度效应；句子条件下高可预测语境更好消解竞争，但竞争不再受语音模糊度调制，支持预测编码/贝叶斯推断等自上而下预期账户。

**Informativity of high-frequency bands on the place of articulation shift in retroflex sibilants produced by children**（论文 2606；Oliwia Skórzewska）分析 186 名波兰学龄前儿童捲舌擦音/塞擦音在规范捲舌及牙、邮龈、齿间等部位；提取 34 维帧级摩擦噪声特征，并用线性混合效应模型量化构音变异，强调高频能量等信息量。

## 本场要点

- CSW 韵律相对单语有系统差异，说话人因素权重大。
- IDS 上梯度语音细节对计算词切分的损害弱于既往 ADS 发现。
- 象似性预测早习得，音系 surprisal 更关联成人加工。
- 自发词时长受语义相关非线性影响；句子可预测性可覆盖次音素模糊度效应。
- 儿童咝音部位偏移可用高频摩擦特征做诊断取向分析。
- 本场方法横跨语料韵律、计算切分、回归/GAMM 与心理语言学启动实验。

## 覆盖核对

| paper_id | title |
|---|---|
| 249 | The Sound of Code-Switching: Prosodic Profiles of Spontaneous Spanish-English Speech |
| 2920 | Gradient phonetic detail is less detrimental to word segmentation in infant-directed speech |
| 1551 | Word Iconicity and Phonological Surprisal as Predictors of Age of Acquisition |
| 1062 | Non-linear Effects of Semantic Relevance on Word Duration in Spontaneous Speech |
| 3106 | From Words to Sentences: Contextual Predictability Overrides Phonetic Ambiguity in Lexical Competition |
| 2606 | Informativity of high-frequency bands on the place of articulation shift in retroflex sibilants produced by children |
