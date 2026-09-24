# Phonetic Aspects of TTS and ASR Systems

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：2
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从语音学角度审视 TTS/ASR：音高抬升伪装、合成语音的语调感知、熟悉度与情感韵律、粤语人机对话中的音位实现、合成嗓音的种族身份感知、多语语音学特征识别，以及发声努力调制策略对噪声稳健性与 ASR 的影响。共同主题是合成与交互系统改变了听者与说话人的语音学行为，并反作用于自动识别。

多篇工作用 AI 克隆/SVC 控制实验材料，比较自然与合成语音在相似度、语调与情感识别上的交互；熟悉度既可能是促进也可能是负担。法医与社会语音学延伸到 ASR 对意志性音高抬升的脆弱性，以及听者对合成嗓音种族标签的刻板印象与可测声学相关。表征侧 PhonoQ-2.0 直接预测帧级语音学特征向量；发声努力聚类显示说话人策略异质并系统影响 Whisper/Wav2Vec2 的 WER。

## 论文技术总结

# Assessing the effect of volitional and synthetic pitch raising in female speakers on automatic speaker recognition

- 论文编号：444
- 报告人：Kirsty McDougall
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/patman26_interspeech.pdf

## 问题
意志性抬高音高是法医常见语音伪装，男性说话人上已显示会严重损害自动说话人识别（ASR），但女性基频更高、抬高策略不同（少用 falsetto、升幅通常更小），其对 ASR 及说话人间变异尚不清楚；亦需检验合成 f0 操纵能否替代真实意志性抬高。

## 方法
(1) PASR 库 3 名女性语音学家：默认与意志性抬高朗读，VOCALISE 2021 spectral x-vector（22 维 MFCC）做非同期 D–D / D–R 同/异说话人比较，报告 EER、x-vector 分数与 zooplot。(2) 声学/听感：Praat 长时 f0、音高 excursion；听感评估喉位等策略。(3) 试点：LMS 库 16 名南方标准英式英语女性，用 Praat 将样本 2 的长时 f0 合成抬高 +1.5 至 +10.5 ST（条件 A–E），同样做 D–D 与 D–合成比较。

## 实验与结果
PASR：D–D EER = 0.0%，D–R EER = 14.4%。退化主要由 P5 驱动（抬高中位 f0 最高约 342 Hz，升幅约 9.8 ST，且音高 excursion 受限）；P8 等同/异分数仍较分离。合成试点：LMS D–D EER = 3.9%；EER 随抬高幅度升至极端 +10.5 ST 时 15.2%。Zooplot 显示中等及以上抬高后“dove”消失，部分说话人变为 chameleon；效应依赖默认 f0 在群体分布中的位置，说话人间不一致。合成无法复现意志性抬高中的多重发音策略。

## 结论
女性抬高 f0 后 ASR 表现高度说话人特异：有人仍可区分，有人变难识别；意志性场景的变异更可能来自策略差异，合成场景则与默认 f0 位置等相关。合成抬高不应视为意志性抬高的代理；需更大规模多说话人意志性数据以区分群体与个体效应，服务法医应用。

## 点评
把“整体 EER 变差”拆到个体策略与 f0 分布位置，对法医 ASR 很有用。强在同一 VOCALISE 管线下对照真实意志性与合成操纵；弱在 PASR 仅 3 人且为训练有素的语音学家，外推到外行伪装需谨慎，合成试点也不能代替真实喉部策略。


# Intonation Perception in Real and Synthetic Speech across Varying Familiarity Levels: A Pilot Study of Equivalence Assessment

- 论文编号：996
- 报告人：Hanrui Zhou
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26b_interspeech.pdf

## 问题
语言训练语料建设成本高，AI 声克隆（此处用 F0 条件的 SVC）可降低成本，但现有评价多基于陈述句；普通话疑问语调依赖句末升/高平 f0，且熟悉度影响加工。需检验自然 vs 合成、熟悉 vs 陌生在说话人相似度感知与语调识别上是否等价。

## 方法
17 名普通话成人（相似度任务全员；语调识别 11 人）。4 名女性说话人（2 熟悉、2 陌生）录 10 句中性六字句的陈述/疑问；合成用 seed-vc 类 SVC，客观说话人嵌入余弦相似度陈述约 0.55、疑问约 0.51，再经语音专家筛选。2×2×2 被试内设计（speech type × familiarity × intonation）。任务：(1) 成对同/异说话人判断 + 1–7 相似度评分；(2) 陈述/疑问二分类。PsychoPy；混合效应模型分析 ACC/RT/评分。

## 实验与结果
相似度 ACC：自然–自然对高于自然–合成对（约 0.917 vs 0.851）；speech type × intonation 交互显著——纯自然对中疑问 ACC 高于陈述（0.946 vs 0.875），混入合成后无显著差。熟悉声音 RT 更短（约 0.748 s vs 0.848 s），但相似度评分更低。语调识别整体 ACC 很高（>95%）；Firth 回归显示 familiarity × speech type 交互：自然语上陌生略高于熟悉，合成语上熟悉略高于陌生（简单效应本身未达显著）。疑问 RT 边际更长。

## 结论
疑问语调可能作为说话人识别线索，但受合成特征影响；熟悉度对语调识别的贡献随 speech type 变化。SVC 合成在受控实验中有一定感知可行性，但对复杂韵律与社会线索（熟悉度）仍不足，语料建设仍有挑战。

## 点评
把语调类型与熟悉度同时放进克隆语音评价，比只测自然度/可懂度更贴近训练语料需求。交互效应提示“疑问有助于识人”在合成条件下会打折扣。样本小、语调任务天花板效应明显，主要依赖 RT；试点性质决定外推需更大被试与更广语料。


# A barrier or a booster? Familiarity effects on Mandarin emotion prosody recognition using AI-powered voice cloning

- 论文编号：1038
- 报告人：Feng Xu
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26i_interspeech.pdf

## 问题
情绪韵律识别同时依赖声学线索与说话人身份。AI 克隆可复制熟悉音色，但情绪韵律仍有非自然细节；不清楚熟悉度会补偿合成缺陷，还是因“熟悉身份 + 人工来源”触发 uncanny valley、加重认知负荷。

## 方法
17 名普通话成人。陌生条件：播音专业女性录 14 句中性六字句的喜/怒/惧/悲，作为人类基线与 EPVC 源；熟悉条件：熟悉者只录中性句作目标音色，不做人类情绪基线。基于 F0 条件 SVC（seed-vc），用 \(F_t=c\cdot(F_s-\bar F_s)+\bar F_t\) 做可控唤醒迁移，专家筛选。被试内判断情绪类别；同步 Biopac 采集 HRV（mean HR、RMSSD、LF/HF）。GLMM/LMM；来源分析限陌生声音，熟悉度分析限 AI 声音。

## 实验与结果
人类相对 AI：Source 与 Emotion×Source 显著；除恐惧外，喜/悲/怒准确率与 RT 均显著优于 AI。HRV 各指标无显著来源效应，也无法用逻辑回归区分来源。AI 内熟悉度：Familiarity 与 Emotion×Familiarity 显著；高兴在熟悉音色上准确率更高；恐惧 RT 则陌生显著快于熟悉。HRV 对熟悉度同样无显著区分。全文结论段抽取截断，讨论已给出主要解释。

## 结论
人类情绪韵律识别整体优于当前 AI 克隆；熟悉度对 AI 情绪加工呈情绪特异：积极情绪可作自上而下补偿，恐惧等消极高唤醒可能引发更长的批判性评估。HRV 未反映自主神经层面的系统差；合成情绪解码受社会认知门控。

## 点评
把“音色克隆成功”与“情绪意图传递”拆开，并用熟悉度测试补偿 vs uncanny valley，问题设置清楚。恐惧例外与熟悉恐惧变慢是有信息量的边界发现。弱在熟悉者无人类情绪基线、HRV 全程不敏感，认知负荷主要靠 RT 推断；结论段文本截断，细节以讨论为准。


# Modulation of Phonetic Realizations in Cantonese Dialogue with Human and AI Interlocutors

- 论文编号：1194
- 报告人：Peggy Pik Ki Mok
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26m_interspeech.pdf

## 问题
人机语音互动中的语音调节多在语调语言、偏积极表达系统上研究；粤语等声调语言、以及面对负面/对抗性 AI 时，对话者身份（人 vs AI）如何改变精细语音实现仍不清楚。

## 方法
17 名香港粤语母语者，被试内 2×2：Interlocutor（Human vs AI）× Emotion（Neutral vs Negative）。Wizard-of-Oz 脚本对话 20 段；人类条件为同一女性母语者音视频，AI 条件为同说话人约 3000 句训练的 DurIAN 定制 TTS + Memoji，音色/内容可比。测目标词时长、六声调时正则化 F0（GAMM）、三角元音 VSA（情绪主效应因数据平衡仅在情绪上分析）。MFA 强制对齐后人工校正。

## 实验与结果
目标双音节词时长：AI 条件显著更短（β = −10.891, p = .04）；音节时长边际更短；话语语速无显著差。F0：相对人类，中性下 AI 上 Tone 1、Tone 4 升高、Tone 5 降低；负面下 Tone 4 亦升高；Tone 2 在负面情绪下相对中性升高（两种 interlocutor）。VSA 在负面下边际更大（β = 1.07, p = .057）。全文讨论后半截断，引言/结果中的主要发现已可读。

## 结论
与 AI 对话时目标词更短、部分声调 F0 呈声调特异而非整体抬高/压低；情绪效应较弱且偏局部（Tone 2、边际 VSA）。表明声调语言中 interlocutor 效应比先前报告的更细粒度。

## 点评
用同一说话人定制 TTS 控制音色/语速混淆，比直接用 Alexa 类助手更干净，也解释了为何与“对 AI 说话更慢更长”的文献相反。时长效应落在反复出现的目标词而非全局语速，设计上便于定位。截断限制了对完整讨论与局限的核对；样本量 17、脚本对话外推到自然对抗性交互仍需谨慎。


# Perceptual and Acoustic Correlates of Racial Identity in Text-to-Speech Voices

- 论文编号：1479
- 报告人：Noah Khaloo
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khaloo26_interspeech.pdf

## 问题
TTS 日益像人，听者能否从全合成语音感知种族身份、是否伴随人格刻板印象，以及 Black/White 标签对应的声学相关物是什么；既往对合成语音存在偏“听成白人”的报告。

## 方法
EasyPeasy AI 合成 32 个英语音色（平台标注 Black/White × Male/Female 各 8）。144 名美国英语听者（Prolific）：人格块对 16 个声音评 6 维人格 + 像人程度；种族块对另 16 个声音做种族等多选（刺激避开 AAE 形态音系线索，只留音质/元音质量）。用 %Reported Black 的 k-means 得感知标签（White / Black / Ambiguous）。VoiceSauce 提 F0、F1–F4、Residual H1*、谱倾斜谐波、CPP 等，XGBoost 在男性感知标签上做 Black vs White 分类。

## 实验与结果
性别平台标签与听者一致很高（男 98.6%、女 93.6%）。种族聚类显示偏 White 的评定偏向；Ambiguous 中多数为平台 Black Female。男性感知为 Black 的声音在愉快、专业、可信、能力上显著更低；女性无显著种族效应。像人程度正向预测各人格维。声学：全特征 CV 准确率约 65%，顶 15 特征约 66%；Black 评定声音 Residual H1*、CPP、部分高/低频谐波倾斜更低，F4 更高；F1/F2 在部分元音上有局部差。

## 结论
听者能从合成语音中形成种族感知，但偏向评成 White；稳定评成 Black 的男性声音人格评分更低。现代 TTS 可编码与 MAE/AAE 相关的细粒度声学差异；开发与部署需警惕刻板印象的社会后果。

## 点评
感知标签（非平台标签）+ 可解释声学特征 + 人格联动，比只问“像不像某一种族”更完整。65% 分类准确率不算高，但 top 特征与 Residual H1* 主导模式仍有语音学解释。女性效应弱、Ambiguous 偏 Black Female，说明性别×种族交互是部署合成语音时的敏感点。


# Multilingual Phonological Feature Recognition with Self-Supervised Speech Models

- 论文编号：2735
- 报告人：Abner Hernandez
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hernandez26b_interspeech.pdf

## 问题
多数系统先识别音素再映射音韵特征，未显式建模音韵结构；单语或辅助目标设定下，结构化音韵预测相对强音素基线在多语/跨域/未见语上的优势尚缺系统比较。

## 方法
PhonoQ-2.0：冻结 XLSR-ft（wav2vec 2.0 音素微调版）+ 共享投影与 2 层 Conformer，四头预测 22 维特征（manner 9、元音高低/前后 6、place 5、voicing 2）；manner 条件门控只在相容类别上激活元音/部位头。基线 CTC-Phoneme 同骨干，预测后用统一 phone→feature 表映射到同一 22 维空间。训练语：英、德、西、捷（各约 52–56 h）；MFA 对齐；段级 macro-F1 评估。

## 实验与结果
域内（CP 等）平均 macro-F1：PhonoQ-2.0 91.3% vs CTC 映射 82.5%（+8.8），英语增益最大（+11.6）。OOD（FLEURS / VoxPopuli）仍优约 +9.3 / +7.8。相对旧版 PhonoQ，在共享 12 维上德国/西语大幅提升。零样本法/意/俄：平均 73.6% vs 66.9%（+6.7），意大利语最高 +10.8。逐特征分析显示 manner/元音/部位/浊音普遍提升，非单靠某一难类。

## 结论
直接结构化音韵特征预测优于“音素优先再映射”，跨域与未见语更稳；可用于发音评估、语言学习与低资源场景。局限：22 维未覆盖法语鼻化元音、俄语腭化、意大利语长辅音等，需扩展特征清单与更远类型学迁移。

## 点评
同骨干、同特征空间的公平对照很关键，说明低 PER 并不自动等于好音韵特征。Manner 门控把语言学约束写进解码，比独立多标签更干净。未见语仍掉到七十出头，说明 articulatory grounding 有帮助但非万能；特征库存缺口会直接限制临床/跨语用途。


# Vocal Effort Modulation Strategies: A Cross-Corpus Taxonomy with Noise Robustness and ASR Implications

- 论文编号：2747
- 报告人：Lubos Marcinek
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marcinek26_interspeech.pdf

## 问题
Lombard/发声努力下说话人会改 F0、能量、谱倾斜、语速，但个体策略长期被当成均值附近的噪声；尚无对多维声学剖面的正式聚类分类，effort 可控 TTS 也多做统一变换、忽略策略类型。

## 方法
AVID 50 人（25F/25M）四档努力（soft→very loud）：对每人拟合 F0、RMS、谱倾斜、语速相对努力等级的 OLS 斜率，z-score 后 K-means；以稳定性选 k=3。校正 LOSO 多项逻辑回归评估可预测性。验证：(1) 84 万含噪句、12 类噪声、多 SNR 上重聚类 ARI；(2) 法语 FLombard 同流程余弦对应；(3) Whisper-base / Wav2Vec2-base 按簇分层 WER。

## 实验与结果
三簇：C1 High Modulators（高 F0/RMS 斜率，男偏）；C2 Spectro-Temporal（正倾斜斜率、最强减速，女偏）；C3 Conservative（各维变化最小）。ANOVA 各特征 p<10⁻⁵，η²=0.25–0.55。性别关联方向性但不显著（χ²=4.37, p=0.113）。校正 LOSO 准确率 96–98%，macro-F1=0.97。噪声：SNR≥+10 dB 时 ARI≈0.86 可恢复。FLombard Conservative 与 AVID C3 余弦 0.873。ASR：各 SNR 上 WER 次序 C3<C2<C1（大调制反而更差）。

## 结论
发声努力存在三种稳定、可预测的策略类型；高 SNR 下可稳健恢复，跨语料有部分对应；当前 ASR 更惩罚 High Modulator 的大声学偏离。可为簇条件、说话人自适应 TTS/数据增强提供结构。

## 点评
把“努力调节个体差”做成可解释分类法，并对噪声、跨语料、ASR 做三角验证，工程指向明确。轮廓系数一般、GMM 分区不一致，说明策略本质连续；性别效应未显著却常被叙述，需更大样本再谈机制。WER 反序对“越 Lombard 越好识别”的直觉是有力纠偏。

