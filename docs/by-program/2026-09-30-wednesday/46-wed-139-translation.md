# Translation

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：12
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场从同声传译自动评分、多语 Indic→英语直接 S2ST、重音跨语迁移、思维链语音翻译是否真用语音，到台语—中文字幕语料自动构建与非洲野外语音识别基准。

焦点从“语义准确”扩展到评分量表对齐、发音动作空间统一、词汇重音保留，以及对声学线索的真实依赖程度。数据侧强调低资源与野外噪声，用多模态半监督与领域纵向基准揭示现代模型的真实差距。

## 技术内容

### 同传评测、发音空间 S2ST 与重音迁移

**Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting**（论文 1105；Ziyu Zhang）  
构建 1,101 段专业标注同传片段，覆盖意义传递、表达质量与感知时延。摘要称结构化 LLM 提示与标量监督会塌缩量表维度；在相同骨干上用双回归头 LoRA 适配 COMET-KIWI，held-out 上 LQ/EXP Pearson 分别为 0.388/0.301，优于冻结基线，并相对评分者一致性解释结果。

**ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation**（论文 2384；Khushal Yadav）  
在通用发音动作空间中做多语 Indic→英语直接 S2ST：Conformer 编码器对源发音特征做中间 CTC，解码器用卷积增强差分 Transformer。摘要称 11 种 Indic 语言（含每语约 10 小时极端低资源）上，166M 参数模型在 BLEU/COMET/chrF 上优于 1.2B SeamlessM4T，且 VRAM 更高效。

**Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation**（论文 2321；Yuchen Song）  
构建重音标注中文数据与基于 XLS-R 的普通话重音检测器，并结合 EmphAssess 提出跨语重音客观指标；再微调 CosyVoice3 得重音感知 S2ST。摘要称重音翻译能力显著优于既有系统且翻译质量有竞争力，指标与人类主观判断强相关。

### CoT 语音依赖、低资源语料与非洲基准

**Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation**（论文 800；Federico Costa）  
通过输入归因、损坏转写鲁棒性与韵律感知评估 CoT S2TT。摘要称 CoT 很大程度上复制级联行为、过度依赖文本转写；向 CoT 注入噪声转写等训练干预可增强声学依赖与鲁棒性。

**A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus**（论文 2096；Yuan-Fu Liao）  
用三模态 AVLM 与迭代伪标注，从含硬编码中文字幕的在线视频自动构建台语语音—中文字幕语料。摘要称 AVLM 将字幕识别 CER 从 36.8% 降至 9.3%；所得约 860 小时语料使 Whisper 跨语转写 CER 从 57.8% 降至 37.8%，台—中翻译 BLEU 从 0.2016 倍增至 0.4033。

**AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition**（论文 3140；Busayo Awobade）  
面向非洲部署条件的基准：全支持语言含野外非脚本音频，并按政府、金融、健康、农业等十个领域及数字/命名实体做纵向评测。摘要称对 Sahara-v2、Gemini 3 Flash、Omnilingual CTC 等新一代模型暴露专业化噪声场景下的真实泛化差距。

## 本场要点

- 同传自动评测需解耦量表维度，而非单一标量塌缩。
- 通用发音动作空间支持极低资源多语 Indic→英语直接 S2ST。
- 英→中 S2ST 开始系统评测并保留词汇重音。
- CoT S2TT 未必真正使用语音，需专门干预提升声学依赖。
- 多模态半监督与领域纵向野外基准分别服务低资源语料构建与真实部署评测。

## 覆盖核对

- 1105 | Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting
- 2384 | ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation
- 2321 | Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation
- 800 | Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation
- 2096 | A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus
- 3140 | AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition
