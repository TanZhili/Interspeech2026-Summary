# Prosody, Pronunciation and Specialized Speech Processing

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：10
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以韵律重音、声调识别与发音评估为核心，并延伸到儿童语音音系过程推断、手语视频生成与日语带声调标记的评估型识别。句子重音检测普遍借助 Whisper 等预训练表征，但强调：单层固定嵌入不足以刻画相对、语境依赖的韵律凸显，因而出现双流显式声学建模、跨层加权融合，以及把词重音作为辅助任务并用词跨度正则约束句重音概率。普通话声调侧则探索仅依赖超音段 F0、多粒度结构化嵌入与可拆卸辅助分支的 Transformer。

儿童与评估场景更强调可解释结构输出：PhonLLM 联合恢复规范音素序列与音系过程标签，并用规则增强规模化注入过程监督；日语口语评估识别器输出带重音标记的音位标签，以多任务音高损失与双估计器融合缓解标注稀缺。手语视频生成则把 LLM 赋能的姿态潜空间扩散规划与运动条件视频扩散结合，并用 Flow-GRPO 多维奖励对齐。整体上，本场从“端到端黑盒分类”转向显式韵律/音系结构、辅助任务与层融合。

## 论文技术总结

# Learning Contextualized Tonal Contours from F0: A Core-Auxiliary Branched Transformer for Mandarin Tone Recognition

- 论文编号：1747
- 报告人：Yi-Fen Liu
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26n_interspeech.pdf

## 问题
普通话声调识别多依赖谱特征；为 CAPT/误发音诊断，希望仅用超音段 F0（及节奏）学上下文声调轮廓，并在推理时保持轻量。

## 方法
核心–辅助分支 Transformer：C-Net 对对数归一 F0 建音节/词/语块级嵌入与交替/内容标记，经多层自注意得轮廓表征；R-Net 用三段时长变异特征建模节奏。训练时辅助分支经 LSAP+交叉注意向核心回传梯度；推理丢弃辅助。损失为三分支交叉熵之和。数据 FCU-VOICE-360（360 说话人朗读）。

## 实验与结果
加词/语块粒度后核心 alone 准确率升至约 96%；辅以 C-Net 或 R-Net 可达 97.5%。v2-m3（Syl+Wrd+辅 R-Net）超单支 TNet-Full（97.2 vs 97.0），且推理延迟与参数更低。双辅助无额外增益。

## 结论
仅超音段信息即可高准确识别五声；可拆辅助分支提升训练稳健且不损推理效率，利于后续 L2 声调诊断迁移。

## 点评
用“训练加通路、推理减通路”把节奏上下文灌进 F0 轮廓学习，设计干净。数据为安静朗读，连读变调/自发语难度未充分覆盖；相对 MFCC 路线的优势在可解释超音段输入，而非绝对 SOTA 竞赛。


# ProWhistress: An Enhanced Dual-Stream Transcription Architecture for Prosody-Aware Sentence Stress Detection

- 论文编号：1303
- 报告人：Hujian Gu
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gu26b_interspeech.pdf

## 问题
无对齐句重音检测中，Whisper 深层表征偏语义、削弱细粒度韵律；普通话重音数据稀缺，现有英语中心方法难直接迁移。

## 方法
ProWhistress：冻结 Whisper 隐式流 + 可训声学编码器（抽中间层）双流；经额外解码块、瓶颈交叉注意与门控残差融合后做 token 级重音分类。另建 SinoStress-Syn（约 12 h，层级 LLM 标注重音+TTS）与 SinoStress-Real（约 3 h 真人）。

## 实验与结果
英语 TinyStress-15k F1 0.959（Whistress 0.909）；零样本 Expresso/EmphAssess 亦显著优于基线。普通话 Syn F1 0.958、Real 监督/零样本约 0.870/0.869，Sim-to-Real 几乎不掉。消融确认双流互补、编码器第 9 层最佳、瓶颈融合优于全维注意。

## 结论
显式声学流缓解语义–韵律权衡，并在中英基准与零样本真实语音上领先；填补普通话句重音数据缺口。

## 点评
门控残差把“补回声学细节”做成可控注入，零样本稳定是亮点。合成重音靠音高/音量/语速规则，复杂对比焦点等仍可能简化；真实集说话人少，泛化边界需更大真人数据验证。


# A Novel Sentence Stress Detection Framework Leveraging Auxiliary Word-Stress Modeling and Loss Optimization

- 论文编号：1494
- 报告人：Tien-Hong Lo
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lo26_interspeech.pdf

## 问题
自动发音评估（APA）中的韵律重音包含句重音检测（SSD）与词重音检测（WSD），二者都依赖音高、时长、强度等线索，但多数工作把它们当独立任务。SSD 在 Whisper 子词分词下还会出现同一重读词内多个 token 概率弥散的问题；现有对齐式管线依赖时间戳质量，对齐无关的 WhiStress 又未引入词级重音约束。

## 方法
提出 STRAW：冻结 Whisper-small 骨干，仅训练任务头与 phone embedding。SSD 以 decoder 状态为 query、encoder 状态为 key/value，经 Transformer decoder 块与 FCNN 做 token 级二分类；评测时任一 token 判为重读则该词判为重读。WSD 用 G2P（CMU 式带 stress digit）得到 phone 序列，经可训 phone embedding 与 encoder 交叉注意力做 phone 级二分类（仅 digit “1” 标为重读）。另加词跨度重音正则器 WSR：对每个真值重读词的子词跨度，鼓励唯一优势 token 概率接近 1、其余接近 0，并用跨度内概率总和偏离 1 的程度加权。总损失为 α·L_SSD + β·L_WSD + λ·L_WSR（默认均为 1）。朗读 APA 设定下用参考转写提供 token/phone，不必额外 ASR。

## 实验与结果
数据为 TinyStress-15K（合成、词级重音标注）：Train/Valid/Test 各 13.5k/1.5k/1k 条。SSD F1：GT alignment 0.858、MFA 0.815、WhiStress 0.909、STRAW 0.934；去掉 WSD/WSR/二者分别为 0.922/0.929/0.915。WSD 上 STRAW F1 约 0.920，去 WSR 几乎不变。POS 误差分析显示功能词（PART、DET 等）假阴性有所下降，SCONJ 因样本少仍偏高。

## 结论
在统一冻结 Whisper 框架内同时做 SSD/WSD，并用 WSR 缓解子词跨度内重音弥散，完整配置在 TinyStress-15K 上取得最高 SSD F1。作者指出局限：词重音简化为每词单一主重音、两头无直接交互、评测仅限合成语音；计划扩展到自发/真人录音并加强跨任务耦合。

## 点评
做法把共享韵律线索拆成“辅助监督 + 语言学正则”，而不是硬共享隐状态，消融也承认 WSD 消融不能证明向 SSD 的知识迁移。WSR 直接针对 Whisper 子词分词的标注模糊，设计动机清楚；主要脆弱点是合成数据上的表观增益能否迁移到自然重音，以及两头分离导致无法强制句/词重音一致性。


# WhiSSDapt: Adaptive Fusion of Whisper Layer Embeddings for Sentence Stress Detection

- 论文编号：3236
- 报告人：Jhansi Mallela
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/murugaiyan26_interspeech.pdf

## 问题
句重音检测需要同时捕捉局部声学与词间相对关系，现有 Whisper 方案常固定取某一 encoder/decoder 层（如 WhiStress 选 Layer 9），默认重音信息集中在单层；而分层分析表明声学、语音、词级信息分布在多层，固定层可能次优。

## 方法
WhiSSDapt：冻结 Whisper-small（English-only），对全部 encoder/decoder 隐状态各学一组标量权重，经温度缩放 softmax 归一化后加权求和得到 ˜h_enc、˜h_dec；再经额外 decoder 块（˜h_dec 对 ˜h_enc 做交叉注意力）与两层 FFN（768→1536→2）做 token 级二分类，再对齐到词级。仅训练融合权重、额外 decoder 与分类头；加权交叉熵类别权重 [1.0, 2.33]。τ 在 GER/ITA/EmphAsses 上取 0.1，TinyStress-15k 上取 0.01。基线为固定 Layer 9 的 WhiStress，以及 ISLE 上的 SupraDoRAL。

## 实验与结果
数据：ISLE（德/意非母语英语，人工词级显著度）、TinyStress-15k（合成）、EmphAsses（Expresso TTS 强调）。词级 F1：WhiSSDapt 在 TinyStress/EmphAsses/GER/ITA 分别为 0.9131/0.9811/0.853/0.8930，优于 WhiStress（0.909/0.939/0.804/0.870），相对提升最高约自然语音 4.48%、合成 6.09%；相对 SupraDoRAL（GER 0.7817、ITA 0.8656）也有提升。层权重分析：decoder 普遍偏好 Layer 9，encoder 偏好 Layer 12、中层受抑；固定融合 E(1,12)–D9 接近全自适应，换深层 decoder（D12）明显变差。

## 结论
可学习多层融合可替代手工选层，并稳定优于固定层基线；分析给出可解释的锚点层（decoder 9、encoder 12）。未来拟扩展到其他韵律任务。

## 点评
核心贡献是把“哪一层有韵律”从离线试错变成端到端可学习融合，层权重分布与消融互相印证，比单纯刷分更有解释力。弱点是骨干仍冻结、合成数据上权重会塌到单层，说明自适应优势在自然变异更大时更明显；且与 WhiStress 同属参考转写条件下的 token 分类设定。


# PhonLLM: Joint Phone Recognition and Phonological Process Inference for Child Speech

- 论文编号：3378
- 报告人：Ilja Baumann
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/baumann26_interspeech.pdf

## 问题
儿童言语临床筛查需要音位级诊断反馈，ASR 转写 alone 不够；传统 MDD/CAPT 多针对 L2 或独立错误分类，缺少把期望发音与实现发音之间的音韵过程（如 fronting、backing、deletion）显式标出的结构化预测，且过程标注昂贵。

## 方法
提出 phonological process inference：输入声学 a 与由正字法经 eSpeak G2P 得到的期望 phone 序列 x，输出带过程标签的规范 phone 序列 y。PhonLLM：wav2vec 2.0（OmniASR，300M）音频帧每 r=5 帧下采样投影后，与期望 phone embedding 拼接，送入冻结 LLaMA-1B，仅训 LoRA（r=16, α=32）与音频投影。两阶段：先在成人多语数据（CommonVoice、MLS 等，约 9.8k 小时）做跨语种 phone 识别；再在儿童数据上联合预测 phone+过程标签。规则增强：对规范 IPA 施加 fronting/backing/deletion 改写得到训练用“期望”序列，目标仍为规范 phone 加过程 tag；采样概率 fronting 0.30、backing 0.60、deletion 0.12、仅识别 0.30。临床 PhonBank 数据仅用于评测。

## 实验与结果
基线平均：冻结 LLM 上下文 F1 50.2；精调文本 oracle F1 89.0；XLSR-53→精调 LLM 级联 F1 48.5（XLSR PER/AW-PER 58.0/26.2）。PhonLLM 平均 tagging F1 75.9（chance 19.2），PER/AW-PER 23.5/12.6，相对 XLSR PER/AW-PER 降约 59.5%/51.9%。Fronting 最稳（多数据集 F1 约 80+），backing/deletion 更难。去掉期望序列条件后模型不再输出过程标签。Másdóttir 按年龄分层：AW-PER 从约 18.83（2y）降至 9.54（7y），tagging F1 约稳定在 74 附近。

## 结论
轻量 speech–LLM 可联合恢复规范发音与音韵过程标签，规则增强可规模化注入监督；联合建模相对 ASR 级联提升 tagging 与降低 PER。局限包括过程库存仍窄（计划加 deaffrication、cluster reduction、stopping 等），backing/deletion 仍弱。

## 点评
把“纠错”改写成“相对期望发音的过程变换”，并用期望序列作触发条件，消融清楚说明过程标签不是无从声学无条件学出的。规则改写解决标注瓶颈，但训练过程分布与临床自然过程可能错位；临床集规模小、德语 recall 偏低，部署前需警惕增强规则与真实病理过程的覆盖差。


# SignMatch: Aligning Pose Latent Diffusion via Multi-dimensional Rewards for Sign Language Video Generation

- 论文编号：1546
- 报告人：Rongjie Huang
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26j_interspeech.pdf

## 问题
手语视频生成（SLVG）要从口语文本与参考签名者图像合成写实签名视频，但文本与细粒度时空动作对齐弱；似然训练往往同时兼顾不好语义忠实与视觉真实，RL/偏好优化在手语生成中尚未充分利用。

## 方法
SignMatch 两阶段：(1) LLM 赋能的 pose latent 扩散（flow-matching），文本骨干默认 T5-Large（也试过 Qwen3-8B），将句子映射为运动条件潜变量 C（身体+手部）；(2) 参考引导的签名视频扩散（参考 SignViP：SD v1.5 U-Net + AnimateDiff 时序，条件编码器注入运动、参考编码器保身份）。随后仅对 pose latent 规划器用 LoRA（rank 64）做 Flow-GRPO 后训练，冻结视频渲染器；对每句采样 G=8 候选，在潜变量上计算多维奖励：语义 R_BLEU（pose→text 回译 BLEU）与视觉 R_SSIM（相对真值 pose），组内标准化后加权（λ_sem=λ_vis=0.5）得 advantage，随机单步做 clipped GRPO+KL（β≈0.04）。回译奖励模型与评测用 BLEU 评估器来自不同训练 run，以减轻 reward hacking。

## 实验与结果
数据：RWTH-2014T（德语手语）、How2Sign（ASL）。视频回译语义（Table 1）：SignMatch 在 RWTH 上 BLEU-4 11.3、ROUGE 27.1、COMET 0.62，优于最强基线 SignViP（7.9/25.4/0.54）；How2Sign BLEU-4 5.1 vs 4.5。视频质量（Table 2）：RWTH FVD 914、IDS 0.60、SSIM 0.70；How2Sign FVD 2009、IDS 0.61、SSIM 0.65，均优于 SignViP 等。消融：无 RL BLEU-4/FVD=9.2/936；仅 BLEU→10.7/978；仅 SSIM→9.7/901；组合→11.3/914。T5-Large 优于 Qwen3-8B（pose 级 BLEU-4 14.26 vs 11.04）。

## 结论
在中间运动潜空间做多维 RL 对齐可同时提升语义与视觉，且不必更新视频渲染器。作者称在两基准上达到语义与视频质量的 SOTA；正文未展开更多失败模式边界。

## 点评
把对齐点压到 pose latent、奖励也算在潜变量上，避免每步渲染多视频，工程上合理；BLEU 与 SSIM 互补的消融也支持“语义奖励 alone 会伤 FVD”。脆弱处在于回译 BLEU 与 SSIM 相对真值 pose 是否覆盖手语语言学正确性，以及冻结渲染器时潜空间对齐对最终手形细节的上限。


# Building Tailored Speech Recognizers for Japanese Speaking Assessment

- 论文编号：1672
- 报告人：Yotaro Kubo
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kubo26_interspeech.pdf

## 问题
日语口语评估需要带音高重音标记的音位转写，以保留误重音、误读等说话人错误；通用 ASR/多语语音转写会因语言模型“规范化”抹掉这些错误。CSJ core 中带手标重音的数据仅约 45 小时（训练约 2.3 万句），远小于全量 CSJ，数据稀疏。

## 方法
流式可部署架构：去掉量化的预训练 Mimi 语音编码器 + 随机初始化因果 Llama-2 风格 Transformer（d=512，24 层，8 头）上的多任务 CTC。(1) 音位字母（PA，片假名+重音撇号，243 token）；(2) 正字法字符 TT（2309 token，可用无重音的 noncore）；(3) Harvest 估计的 fo 轨迹 10 类分类。任务权重 PA/TT/fo=0.3/0.6/0.1。解码用 lattice fusion：由 PA/TT 的 CTC 混淆网络经 blank 去除得格子；TT 格子经 UniDic 发音词典 FST 转为 PA 格子并与 PA 格子按发音权重归一化后取并，再最短路径。对比显式 conditioning、Whisper/TT-only 作外部 TT 源等变体。选用 CTC 以尽量少做错误纠正。

## 实验与结果
主评测 CSJ core eval1/2/3，外加 JSUT basic5000。含重音的平均 mora-label 错误率：从 PA-only 约 12.3% 量级降到完整方法约 7.1%（摘要）；Table 1 中 MT+LF 在 eval1–3 含重音分别为 7.0/7.7/9.1，优于 Whisper†、Multipa† 与 PA-only。多任务主要得益于 TT+noncore；单独 fo 帮助有限，与 TT 合用有增益。JSUT 上 TT 不准时 fusion 帮助变弱，换 Whisper 作 TT 源可改善。Whisper 在 CSJ 上 CER 高、倾向忽略说话人错误，在无错误朗读 JSUT 上则很强。

## 结论
多任务利用廉价正字法标注与 fo，再经 FST 融合 PA 与词典诱导的 PA 分布，可在稀疏重音标注下做出更准确的日语音位+重音识别，优于通用多语系统。相对优势取决于 TT 源质量与领域是否匹配。

## 点评
问题设定抓住了“评估向 ASR 不能规范化”这一关键冲突，CTC+多任务+词典融合是针对小标注、要保留错误的务实组合。脆弱点在于词典路径会把 TT 错误或规范发音偏好注入 PA，自发语与朗读外域表现分化；fo 辅助本身弱，说明音高重音仍主要靠稀缺 PA 监督。

