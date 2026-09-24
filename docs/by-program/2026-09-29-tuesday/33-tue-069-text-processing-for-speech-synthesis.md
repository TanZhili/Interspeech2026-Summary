# Text Processing for Speech Synthesis

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：7
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场核心是“文本前端如何决定合成可懂、可认、可听”。低资源希腊语、希伯来语、韩语与汉语多音字工作，都把对齐清洗、G2P/变体音素标记、词典增强与确定性提示，视为与声学模型同等关键的瓶颈。

多方言/多语言路线依赖统一 IPA 或罗马化以减少表音歧义，并用 MoE、PEFT、语音 token 预测目标提升语音对齐；日语 SpeechLLM 则用偏好对齐解决“书面语输出不宜合成”的语域错配。

听者侧出现语域可听性研究，以及语境条件重音基准 CAST：文本模型能从话语推断重音，但 TTS 常无法在语音中实现。整体趋势是前端语言表征、提示/对齐策略与评测基准同步细化。

## 论文技术总结

# Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS

- 论文编号：2481
- 报告人：Alexandros Potamianos
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/syllas26_interspeech.pdf

## 问题

现代希腊语缺高质量单说话人语料，低资源 TTS 易损韵律、可懂度与说话人一致性。众包多说话人数据碎片化，全参微调易学成“平均声”；LLM 生成的风格提示在推理时还会引入说话人漂移。

## 方法

数据策展：WhisperX 对齐 + 置信度/时长/声学过滤，整理 CSS10、过滤后 Common Voice（约 15.5 h）与人工核验有声书（约 3.5 h 男声）。在多语言 Parler-TTS（880M）上先全参微调解码器，再用确定性提示（属性分位数分箱、固定拼接）替代 LLM 风格描述，最后在 3.5 h 单说话人数据上做 LoRA（约 25M/5% 参数）锚定身份。推理用统一 canonical 确定性提示与贪心解码。

## 实验与结果

Det.+LoRA：WER 10.7%（人类 ASR 底 7.8%，差 2.9 pp）、CER 3.7%；MOS-I 4.00（人类 4.36）、MOS-C 4.24（人类 4.30）。无 LoRA 时 LLM 提示 WER 更好，加 LoRA 后确定性提示反超（10.7% vs 21.1%）。LLM+LoRA 的 MOS-C 仅 3.56。希腊 VITS 微调未达正式评测质量。失败模式含重音错位、幻觉音节、标点–韵律不匹配。

## 结论

作者认为多语言先验 + 确定性提示 + 说话人 LoRA 是少数据希腊单说话人 TTS 的可行配方；高质量转录比堆时长更重要。局限为单一男声朗读风格与部分主观差异未达显著。

## 点评

把“提示随机性”和“多说话人平均声”拆开治理：确定性提示降条件方差，LoRA 专锚身份，二者协同才稳。客观 SIM-S 仍一般，主观侧重系统内一致性而非严格仿某参考说话人，评价口径需读清。ASR WER 对形态丰富希腊语可能低估/高估感知错误。


# DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization

- 论文编号：2447
- 报告人：Ziqi Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26z_interspeech.pdf

## 问题

统一方言 TTS 面临数据稀缺、正字/拼音跨方言读音歧义、多方言联合训练风格平均与相互干扰；新方言仅有数小时数据时难扩展，高质量方言数据直接续训也不一定稳。

## 方法

基于 F5-TTS 的多阶段流水线：统一 IPA 前端；Stage 1–2 在普通话+多方言 IPA 数据上训练，Stage 2 在文本嵌入后加方言感知 residual MoE，并用方言分类辅助损失引导门控；Stage 3 冻结主干，仅训 LoRA 与 Conditioning Adapter，并用音高/时长微扰增广适配新方言。另用 Flow-GRPO，以 ASR WER 为奖励，在高质量川方言语料上优化 DiT 主干。

## 实验与结果

约 0.7k h 普通话 + 0.4k h 方言。消融：去 MoE 或改用 pinyin 均明显变差（pinyin 时 WER&gt;90%）。相对商业系统 WER/MOS 仍有差距（数据规模差数量级）。对成都高质量数据：Flow-GRPO 将 CD WER 从 29.25% 降至 23.93，并改善 XA/ZZ 等相关方言；直接续训改善有限甚至变差。低资源京剧念白与南京话可经 PEFT 扩展。

## 结论

作者认为 IPA + 方言 MoE + PEFT 构成可扩展统一方言 TTS；GRPO 比直接续训更能利用高质量方言数据并产生跨相关方言增益。

## 点评

IPA 统一拼音歧义、MoE 抗风格平均，问题拆分清楚。客观 WER 绑特定 ASR，方言/戏曲语音上可能偏严；与商业系统对比不公平处作者已指出。奖励仅用 WER，韵律与自然度未直接优化，是当前边界。


# SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis

- 论文编号：2055
- 报告人：Kwangsung Kim
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26p_interspeech.pdf

## 问题

韩语 Hangul 虽偏表音，但正字法形态音位性强，字素≠实际发音；低资源下模型难靠隐式学习消歧。全量音位变体标注会膨胀词表、破坏 token 分布平衡，损害可学性。

## 方法

提出 Selective Allophone-Level Tokenization（SALT）：在 G2P 后的音素上选择性附加音位变体标签（如词首清化 i、腭化 j、韵尾 c）。用 Gini 与 Rényi 效率（α=2.5）筛选标签组合；优选仅区分鼻韵尾的 SALT-N（词表增幅小、效率高）。在预训练 F5-TTS（英/普）上，对文本嵌入与 ConvNeXt 全参微调，其余用 LoRA；数据为 KSS 12.75 h 与极低资源 1 h 子集。

## 实验与结果

12.75 h：SALT-N CER 3.30%、WER 11.24%，优于字素 4.74%/15.26% 与音素 3.74%/14.06%；NMOS 最高 3.10。全标签 SALT-VCP CER 反升至 6.03%。1 h：仅 SALT-N CER 低于 10%（8.19%），字素/音素/VCP 均≥10.78%。人类听感对发音错误更敏感，故 NMOS 更青睐低 CER 的 SALT-N，即便 UTMOS 略低于 VCP。

## 结论

作者认为不必改架构或堆数据，用选择性音位变体输入作归纳偏置即可提升韩语 TTS；关键是在声学消歧与 token 统计效率间取平衡。局限为单说话人小数据，未来将扩到多说话人与其他规则性强的语言。

## 点评

把“语言学先验要注入多少”量化成分布效率指标，再选最小有效标签集，比盲目全规则 G2P 更工程化。低资源增益最大，符合归纳偏置预期。依赖标准发音规则与 G2P 质量；方言/口语变体更自由时，选择性规则可能需重标定。


# G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation

- 论文编号：1064
- 报告人：Feifan Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26i_interspeech.pdf

## 问题

普通话多音字消歧是 TTS 前端关键环节。现有 BERT 类方法参数过大难上端，且闭集分类无法预测训练未见读音；词典增强方案常需存储稠密词向量，占存储。

## 方法

提出 g2pO：用 RoBERTa-tiny（约 3.2M）编码；词典融合模块用 Trie 匹配含目标字的词，对 span 隐状态做 mean+max mix-pooling，动态构造词表示并与拼音嵌入拼接，再经注意力聚合成 lexicon prior 与增强字符状态；辅以 POS 预测；最终用加权 softmax（结合 prior 与合法拼音 mask）输出。词典仅存字–拼音映射（约 100K 词约 3MB），无需预训练词向量。

## 实验与结果

CPP 测试准确率 99.15%（3.99M 参数），优于 g2pW 的 99.08%（约 108M）；RCPP/RCPP(S) 为 99.03%/98.51%。Hard 子集（词典冲突）准确率 93.62%（随机基线 54.26%）。未见读音零样本准确率 70.79%，闭集方法基本为 0。消融显示去 lexicon adapter 掉至 98.55%。

## 结论

作者认为轻量编码器 + 动态词典融合可在极小体积下达到 SOTA，并具备开放词表泛化，适于端侧部署。

## 点评

把“词典知识”从巨大 embedding 表改成隐状态上的 on-the-fly 池化，同时用 prior 打开输出空间，同时解决体积与开放词表。Hard 子集说明模型不是简单查表。未见音依赖词典覆盖与 prior 温度设定；极低频多音字仍可能弱。


# UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction

- 论文编号：909
- 报告人：Sangmin Lee
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26h_interspeech.pdf

## 问题

多语言 TTS 文本编码器常依赖 G2P，可靠工具约仅覆盖百来种语言；纯文本预训练又缺声学线索。需在更大语言覆盖下保持音素保真与文本–语音对齐。

## 方法

提出 UR-BERT：用 Uroman 罗马化统一书写系统；BERT-base 字符级分词；预训练除 MLM 外增加 speech token prediction（STP）：从 omnilingual ASR W2V 中间层提特征，经 MMS-FA CTC 强制对齐到字符，再 k-means（256+静音）离散化为目标。预训练语料约 13K 小时、8M 句、495 语。下游冻结/微调后接 VITS。

## 实验与结果

高资源英/德/普：UR-BERT 的 MOS 分别为 4.35/3.78/3.88，优于 XPhoneBERT 与 m-PLBERT。低资源多语（含 XPhoneBERT 不支持的爪哇语等）MOS 全面最高；未见语巽他语零样本仍优于纯 VITS。消融显示 STP 多数语言提升 MOS。预训练句数仅约 XPhoneBERT 的 2.5%。

## 结论

作者认为罗马化突破 G2P 覆盖瓶颈，STP 补偿罗马化音素粗粒度，可在数据更少时扩展到数百语并保持合成质量。

## 点评

用“共享拉丁书写 + 声学 token 蒸馏”同时扩覆盖与保音素，比堆更大 G2P 更可扩展。罗马化跨语同形异音仍可能混淆，STP 是关键补偿。评测依赖多语 ASR/UTMOS，跨语偏差用相对指标缓解，但仍需留意。


# Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input

- 论文编号：894
- 报告人：Maja Jønck Hjuler
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hjuler26_interspeech.pdf

## 问题

LLM 文本越来越多直接送入 TTS，但其语域是否适合听读未知。既有评测多关注自然度/可懂度，较少测听者加工与记忆负荷；可读性指标也不等于可听性。

## 方法

被试内设计（N=47）：四类输入经同一 Google TTS（澳式口音）合成——ART 对谈广播转写、Wikipedia Simple English（WSiE）、标准维基（WStE）、GPT-4o-mini 生成。测 AIME、NASA TLX 主观努力与线索回忆；并用可读性指标与 Biber MDA 刻画语域。

## 实验与结果

ART 努力显著最高（AIME 62.9、TLX 46.8），书面与 GPT 显著更低且彼此接近（约 25–29 / 15–18）。回忆上 WStE 最高（94.3%），ART 最低（78.7%）。MDA：ART 偏互动口语，WStE 偏正式信息文，GPT 与 WSiE 居中且接近。可读性上 WSiE 最易读，WStE 最难，GPT 居中。

## 结论

作者认为合成语音中，书面/维基源比广播对谈转写更易听；LLM 文本与维基源可听性相当，支持其作为合成输入。研究属初步，语域与话题样本有限。

## 点评

把焦点从“合成器好不好听”转到“输入语域好不好听”，对 agent/播客管线很有现实意义。对谈转写难听可能来自口语纠缠结构经 TTS 朗读后更吃力，而非“口语更自然”的直觉。样本与音色单一，外推需谨慎；也提示“为说话而写”可能比直接喂聊天转写更重要。


# Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine

- 论文编号：887
- 报告人：Heejo You
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/you26_interspeech.pdf

## 问题

韩语 G2P 常用 g2pk 延迟高、词界音变不准，相当于给 TTS 喂标签噪声，拖慢收敛并伤可懂度。需可解释、高速、形态深度整合的规则引擎，并用统计严谨方式验证对下游 TTS 的影响。

## 方法

提出规则 G2P：Kiwi 分析后构建 Sentence→Eojeol→Syllable 层次，音节指针连到语素实现 O(1) 边界判定；规则专用隔离词典；按优先级迭代扫描，命中后重置到 Eojeol 首音节再评估，模拟连锁音变。下游用 96 个 VITS（字素 / g2pk / 所提引擎各 32）训 500k 步，去掉 |z|&gt;1.96 离群后做 ANOVA。

## 实验与结果

G2P：平均 3.14 ms vs g2pk 14.98 ms；句级准确率 85.7% vs 27.2%，CER 0.002 vs 0.021。TTS：Proposed 组 CER 显著优于另两组；g2pk 与字素无显著差异。PESQ/WV-MOS 组间不显著，说明可懂度提升不以牺牲声学自然度为代价。训练曲线显示高质量 G2P 更早收敛。

## 结论

作者认为高精度规则 G2P 同时提升速度、可懂度与训练效率；不准确 G2P 不优于直接用字素。剩余错误多来自同形多义与分析器窗口限制。

## 点评

用大规模重复训练 + ANOVA 把“G2P 准不准有没有用”做成可复现的因果证据，方法学上扎实。规则引擎对连锁音变友好、可调试。同形歧义仍是上界；未覆盖神经 G2P/LLM 前端对比，但作为可引导数据的确定性基线价值高。


# Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech

- 论文编号：604
- 报告人：Morris Alper
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kolani26_interspeech.pdf

## 问题

现代希伯来文书写常省略元音与重音等语音细节，即便加 nikud 仍有重音、shva、不规则词等歧义；现有 TTS/评测用无标音 ASR，对元音与重音错误“看不见”。

## 方法

Phonikud：冻结 DictaBERT 标音器，加轻量头预测增强符号（非末音节重音、发声 shva、不规则词标记），再规则转全规格 IPA。训练用 IsraParlTweet 半自动伪标签 + 人工校正高频词。发布约 2 h 双说话人 ILSpeech（音频–文本–专家 IPA）；训 Whisper-small 作 audio-to-IPA 评测 ASR。下游用 Phonikud IPA 微调 Piper/StyleTTS2。

## 实验与结果

G2P（ILSpeech 子集）：WER 17.4%、CER 3.8%，优于实时标音器与多语 G2P，接近 Gemini。TTS：StyleTTS2 WER/CER 35.2%/8.9%，优于开源基线，接近专有系统；CMOS 相对 Robo-Shaul 自然度 +1.3。重音难例：全方法 WER 3.2%、EM 77.0%，显著优于去重音与 Robo-Shaul。消融：去增强标音或元音均伤性能。

## 结论

作者认为补全语音欠规格说明后，小本地模型可接近大专有系统；框架、数据与评测基准开源。局限继承基座标音器错误与书面对白语体差异。

## 点评

同时修“生成前端”和“评测盲区”：没有 audio-to-IPA，希伯来 TTS 改进难以量化。轻量 adaptor 保留原标音能力再补缺口，工程干净。伪标签+人工校正可扩展，但对口语变体与基座错误仍敏感。


# Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization

- 论文编号：976
- 报告人：Mengjie Zhao
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26d_interspeech.pdf

## 问题

SpeechLLM 常继承书面体输出（markdown、列表、冗长复杂句），日语口语与书面在敬体、句末助词、句法复杂度上差距大，不利于 TTS 与听懂。尚无可靠日语 speech-worthy 评测资源。

## 方法

在 Whisper 编码器 + Sarashina-7B 架构上，预训练对齐模态后，用 DPO+SFT 偏好对齐：偏好口语化、不偏好书面体。偏好数据来自翻译后的 SpeechPref、InstructS2S-200K 滚动采样 + DeepDialogue。构建 SpokenElyza：过滤 ELYZA 中不适口语任务，风格改写并经母语者听测校验。评测用 LLM-as-judge 与词数/依存深度/不可发音字符比例。

## 实验与结果

SpokenElyza：预训练 2.91 → DPO+SFT+口语系统提示 3.44（约 +18%）；Elyza 书面评测从 3.97 微降至 3.78。表面形式：词数约 326→78，NV% 13.46%→3.24%，依存深度降至约 4.97。单独提示可大幅缩短，与偏好训练互补。

## 结论

作者认为偏好对齐可显著提升日语 SpeechLLM 的可听合成友好度，同时大体保留书面指令跟随；SpokenElyza 开源以支持后续研究。

## 点评

把“能听懂的回复”从文本 LLM 对齐迁到 SpeechLLM，并补日语基准，针对语体落差。依赖 LLM 改写与 LLM-as-judge，可能与真实听感不完全一致；书面分略降是风格权衡。偏好数据经翻译，日语特有礼貌策略是否充分覆盖仍待验证。


# Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark

- 论文编号：2743
- 报告人：Avihu Dekel
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/turetzky26_interspeech.pdf

## 问题

同一句子因语篇语境不同需强调不同词（对比焦点），现代 TTS 虽能显式控重音，但能否仅从语境推断并实现恰当词级重音尚不清楚；缺对比控制基准。

## 方法

提出 CAST：对比语境对——相同目标句 + 两种语境，语义上要求不同重音词。用结构化提示生成并由多模型裁判过滤；113 对（226 项），位置与语用类型均衡。评测系统在无语境 / 拼接语境 / 指令语境 / 显式重音下合成，用 WHISTRESS 检测重音，报告 Hit、Pair-Contrast、Pair-Correct。另释放大约 10k 合成训练资源。

## 实验与结果

各系统 Pair-Correct 接近 0；提供语境（拼接或指令）相对无语境无明显提升。显式重音上界更高（如 CosyVoice3 Pair-Contrast 40.3、Pair-Correct 10.6），但仍不可靠。人类校验：标签多数一致率高；检测器与人一致程度落在听者间一致性范围内。文中亦报告文本 LM 能较好从语境恢复目标重音，而 TTS 难落地到声学。

## 结论

作者认为当前 TTS 普遍不能可靠做语篇条件重音；实现能力（显式）与推理能力（语境）之间存在鸿沟。CAST 与流水线开源以推动语境感知韵律。

## 点评

用“同句异境”设计干净隔离语境效应，Pair-Correct 严格卡死句内偏置。结论对下一代对话 TTS 很刺耳但证据清楚。自动检测器 κ 不高反映突显感知本身主观；基准规模中等，扩展合成语料可支撑训练但评测需防污染。

