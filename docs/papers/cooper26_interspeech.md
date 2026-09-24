# A Large-Scale Dataset of Listener Impressions of Emotional TTS

- 论文编号：1521
- 报告人：Erica Cooper
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/cooper26_interspeech.pdf

## 问题
情感 TTS 的金标准仍是听测，但成本高、难快速迭代。现有自动质量评估（如 UTMOS）多在中性合成语料上训练，难以泛化到情感合成；情感 TTS 还需评估表达力与目标情绪匹配度，而公开听测结果与含合成样本的标注数据几乎空白。

## 方法
构建大规模听感数据集（非提出新合成模型）：
1. 收集/生成约 18,208 条样本：自然情感语音（主要 ESD）+ 13 类合成系统（Emo-DPO、EmoSpeech、ECSS、GPT-Talker、EmoKnob、Tortoise、MaskGCT、VALL-E X、Vevo、PromptTTS++、ParaSpeechCaps、MiMo-Audio、Gemini API 等），覆盖克隆、文本提示说话人与 API 预设音色。
2. 262 名美式英语母语听者评分：QMOS、EMOS、自由选择感知情绪类别、valence/arousal/dominance（SAM 量表）；多数样本约 7 次评分。
3. 分析评分关系，并用 SSL-MOS、UTMOS、Emotion2Vec、Gemini LLM-as-judge 做零样本预测实验。

## 实验与结果
组内系统排名给出（跨组因内容/说话人不同不可直接比）：如 ESD 自然语音 QMOS/EMOS 3.71/3.90；Gemini API 4.21/3.89；Tortoise QMOS 高但 EMOS 偏低。目标情绪选择比例与 EMOS 相关约 0.92。VAD 分布相对自然语音的 EMD 与 EMOS 呈强负相关（按情绪有所不同）。零样本预测：UTMOS 对 QMOS 系统级 SRCC 总体 0.80；Gemini 对 EMOS 总体 0.84；各情绪差异大（如 Angry 更具挑战）。

## 结论
作者贡献首个面向情感合成语音质量评估的大规模听感数据集，将公开以支持自动评估模型开发；现有预测器有一定相关性但仍有明显提升空间，且表现依赖情绪类别。

## 点评
这是「评测基础设施」论文：价值在于把多系统、多轴标注做成可训练资源，而不是比拼某个 TTS 分数。分析部分有用地提醒：QMOS/EMOS/VAD 可互补，中性 MOS 预测器不能直接当情感评测银弹。脆弱点：系统间条件不完全对齐（作者已强调），零样本预测不等于专用评估模型上限；公开后实际训练效果仍待社区验证。
