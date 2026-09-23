# Text Processing for Speech Synthesis

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：7；论文数：10
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场核心是“文本前端如何决定合成可懂、可认、可听”。低资源希腊语、希伯来语、韩语与汉语多音字工作，都把对齐清洗、G2P/变体音素标记、词典增强与确定性提示，视为与声学模型同等关键的瓶颈。

多方言/多语言路线依赖统一 IPA 或罗马化以减少表音歧义，并用 MoE、PEFT、语音 token 预测目标提升语音对齐；日语 SpeechLLM 则用偏好对齐解决“书面语输出不宜合成”的语域错配。

听者侧出现语域可听性研究，以及语境条件重音基准 CAST：文本模型能从话语推断重音，但 TTS 常无法在语音中实现。整体趋势是前端语言表征、提示/对齐策略与评测基准同步细化。

## 技术内容

### 低资源与语言特异前端

**Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS**（论文 2481；Alexandros Potamianos）用 WhisperX 对齐清洗有声书，微调 Parler-TTS；发现 LLM 风格提示导致说话人漂移，改用确定性提示，并以约 3.5 小时单说话人 LoRA（约 5% 参数）锚定身份。摘要给出 WER 10.7%、MOS-I 4.00、MOS-C 4.24 等结果。

**SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis**（论文 2055；Kwangsung Kim）把选定同位音现象写入输入而非留给模型隐式学习。12.75 小时设定 SALT-N CER 3.30% 且 NMOS 最高；1 小时设定仅 SALT-N CER 低于 10%（8.19%）。

**G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation**（论文 1064；Feifan Chen）小 BERT + 词典适配器，用隐状态 mix-pooling 动态构词表示。约 3.99M 参数，CPP 准确率 99.15%，未见读音零样本 70.79%。

**Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine**（论文 887；Heejo You）提出面向对象、音节—语素连通与递归重估的规则 G2P，相对 g2pk 更快更准（摘要：3.14 ms vs. 14.98 ms；85.7% vs. 27.2%）；96 个 VITS 模型统计验证可懂度显著提升。

**Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech**（论文 604；Morris Alper）发布 Phonikud G2P（完整 IPA）、ILSpeech 语料、希伯来 G2P 基准与音频到 IPA 模型；报告更准音素预测，且小规模本地 TTS 配合 Phonikud 可接近大型专有系统。

### 多方言/多语言、可听性与语境重音

**DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization**（论文 2447；Ziqi Chen）统一 IPA 前端 + 方言感知 MoE 文本编码器，PEFT 扩展低资源方言；GRPO 强化学习降低目标及相关方言 WER。

**UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction**（论文 909；Sangmin Lee）以统一罗马化覆盖约 495 种语言，并加语音 token 预测目标；跨语言与资源条件优于近期文本编码器基线，并对未见语言有泛化。

**Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input**（论文 894；Maja Jønck Hjuler）比较会话、正式书面、简化书面与 LLM 生成语域的合成可听性（N=47）。书面来源合成可听性高于电台文本；LLM 文本与维基来源相当。

**Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization**（论文 976；Mengjie Zhao）用偏好对齐使日语 SpeechLLM 输出更简洁口语、宜于合成；发布 SpokenElyza 基准，报告在其上大幅改进并大体保持书面评测表现。

**Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark**（论文 2743；Avihu Dekel）提出 CAST：对比性语境对要求不同重读词。文本 LLM 常能从语境恢复目标重音，但 TTS 常无法在语音中实现；并发布基准与合成语料。

## 本场要点

- 提示确定性、LoRA 说话人锚定与对齐清洗，是低资源高质量 TTS 的关键配方。
- 韩/汉/希伯来前端强调变体音素、多音字开放词表与完整 IPA，减少正字法欠指定。
- IPA/罗马化 + MoE/PEFT/语音 token 预测支撑多方言与超多语言扩展。
- 合成可听性依赖语域；LLM 文本未必劣于维基书面文本。
- SpeechLLM 口语对齐与 CAST 语境重音，暴露“文本对了、语音重音不对”的鸿沟。

## 覆盖核对

| id | title |
|---|---|
| 2481 | Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS |
| 2447 | DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization |
| 2055 | SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis |
| 1064 | G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation |
| 909 | UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction |
| 894 | Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input |
| 887 | Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine |
| 604 | Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech |
| 976 | Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization |
| 2743 | Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark |
