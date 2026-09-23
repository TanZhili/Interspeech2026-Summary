# Tones

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 2）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场从音系演化、方言对比、感知训练、二语范畴感知、连读变调跨代差异，到自监督模型是否补偿声调语境，系统讨论汉语声调及相关方言。共同主题是：声调不止是 F0，而是多线索竞争与语境依赖的动态系统。

产出侧，平顶山高降调对显示年轻说话人在音高差异收窄时加重吱嘎发声与时长权重；湘方言不同高度对立系统在不同元音语境下扩展 F0 范围并依赖更多线索；厦门闽南语跨三代数据显示本调与变调在高度与斜率上并非声学等价，青少年压缩本调空间却强化部分变调对立。

感知侧，粤语母语者的非语言音高训练可改善噪声中部分声调词识别，但“拥挤”声调空间收益有限；景颇语母语者对普通话声调的范畴感知受母语声调清单制约。模型侧，纯预训练 wav2vec2.0 嵌入相似度未见语境补偿，探测分类器仅部分复现，提示某些音系规律可能需要监督目标才能抽象。

## 技术内容

### 多线索权重与方言声学

**Beyond Pitch: Multidimensional Cue Reweighting of Two High-Falling Tones in Pingdingshan Mandarin**（论文 361；Zhuo Chen）
考察平顶山两高降调在音高退化时其他线索是否增强。32 名不同年龄说话人语音与 EGG，分析音高、发声、时长、能量。混合效应与随机森林显示：老年主要靠音高；年轻说话人音高差收窄后，吱嘎发声与时长相对权重显著上升，体现从音高主导到多维线索系统的再加权。

**Tonal Contrasts in Different Vowel Contexts and Different Tonal Systems**（论文 1215；Mingxing Li）
比较两湘方言（三高度 vs 四高度）在 [ɹ̩]、[i]、[a] 语境下的对立声调。测量 F0 轨迹、均值、时长、强度及 H1*-H2*、HNR、CPP。主要发现：高调通常更短、更强、更周期；[i] 上 F0 范围更宽；XGBoost+SHAP 确认 F0 重要，且高度对立更多的系统倾向依赖更多线索。

**Acoustic Differences Between Citation and Sandhi Tones Across Three Generations in Xiamen Southern Min**（论文 2138；Peggy Pik Ki Mok）
49 名厦门闽南语三代说话人 F0 轮廓比较。变调与本调在高度与斜率上均有差异，即便传统记同调值；青少年本调空间压缩但强化如 /44/>[22a] 与 /24/>[22b] 对立，老年多中和，中年居中，显示稳定语音学分化与年龄分级变化。

### 感知训练、跨语言范畴与模型补偿

**Tone-space Distribution Modulates Transfer from Non-linguistic Pitch Training to Cantonese Tone-in-Noise Perception in Native Speakers**（论文 1274；Yi Weng）
29 名粤语成人在 14 天内完成 8 次 126–217 Hz 纯音辨别训练。辨别阈值下降；噪声词识别改善更明显，T1/T3/T4 收益可泛化到新说话人，T2/T5/T6 收益有限，支持条件依赖的垂直迁移并提示拥挤声调空间需定向训练。

**Categorical Perception of Mandarin Tones in Jingpo Native Speakers**（论文 1602；Binghao Wang）
27 名景颇与 23 名普通话母语者对 12 条合成声调连续体做辨认与辨别。景颇可区分多数普通话音位范畴，但 Tone 35 与 Tone 214 间未表现范畴感知（或与景颇缺降升调有关），且若干对立的 CP 程度显著低于普通话组，支持感知同化模型解释。

**Perceptual compensation for tonal context in self-supervised speech models**（论文 2409；James Kirby）
伪复现普通话声调语境补偿实验，比较纯预训练 wav2vec2.0 与普通话 ASR 微调模型。纯预训练嵌入相似度无补偿证据；探测分类器有部分补偿与层间范畴化提升，但孤立测试音节上未能复现人类表现，提示监督目标或对抽象部分音系规律必要。

## 本场要点

- 声调演化可见“音高主导→多维线索再加权”，发声与时长可补偿收窄的 F0 对立。
- 元音语境与声调系统高度数共同调节 F0 范围与线索依赖结构。
- 本调与变调可在亚音位层面持续分化，并呈跨代差异。
- 非语言音高训练向噪声粤语感知的迁移受声调空间拥挤度调节。
- 母语声调清单塑造二语普通话范畴感知边界。
- 纯 SSL 预训练未必涌现声调语境补偿，监督微调可能关键。

## 覆盖核对

- 361 | Beyond Pitch: Multidimensional Cue Reweighting of Two High-Falling Tones in Pingdingshan Mandarin
- 1215 | Tonal Contrasts in Different Vowel Contexts and Different Tonal Systems
- 1274 | Tone-space Distribution Modulates Transfer from Non-linguistic Pitch Training to Cantonese Tone-in-Noise Perception in Native Speakers
- 1602 | Categorical Perception of Mandarin Tones in Jingpo Native Speakers
- 2138 | Acoustic Differences Between Citation and Sandhi Tones Across Three Generations in Xiamen Southern Min
- 2409 | Perceptual compensation for tonal context in self-supervised speech models
