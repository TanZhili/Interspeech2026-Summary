# Tools and Techniques for Phonetic Analysis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：2
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场海报集中在语音学分析工具、弱监督边界/音素标注，以及发音生理与韵律接触现象。弱监督与大模型标注是主线：用停顿、音高重置与能量下降构建高精度韵律边界锚点做 PU 学习；ArtNet 以发音特征预测 + VIB 做零样本跨语音素识别；wav2VOT 把 wav2vec2 用于 VOT、闭塞时长与爆破实现自动估计。

对齐与样本量问题被量化：MFA 在 TIMIT 元音上的可靠声学测量存在特征相关的最小 token 门槛；同音异形词研究用时间归一化频谱图显示音段实现随语境意义分化。韵律与话轮方面，多语料证实话轮末词长时化主要落在末音节；跨语词汇重音检测比较单语/多语/跨语 SSL 特征与 Pre-net/Post-net。

发音侧结合 rtMRI 喉部分割（Mask2Former）与 EGG+喉镜观察澳式英语韵尾清塞音的声门策略；动态分析比较 Legendre 多项式与 GAMM 刻画接触诱发语调变体。监督规模上，G2P 自动音标仅在人类标注少于约 20–30 小时时有益，超过阈值 ASR 预训练更有效。工具化、弱监督与“多少数据才够”是共同关切。

## 论文技术总结

# High-Precision Prosodic Boundary Anchors from Acoustic Cues under Weak Supervision

- 论文编号：209
- 报告人：Hanyu Liao
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/liao26b_interspeech.pdf

## 问题
韵律边界检测多依赖 ToBI 等人工标注，成本高且许多语料缺失。虽有停顿、音高重置、能量变化等声学相关，如何在无人工边界标签下得到高置信正例并推广到全部词接缝，仍困难。

## 方法
弱监督分层锚点 + PU 学习：
1. 长停顿（如 ≥200 ms）得保守候选 B1；
2. 用音高重置与能量下降进一步筛成更严锚点 B2（强调 precision）；
3. 以高置信锚为 **正例**、其余为未标注，用 **nnPU**（\(\pi=0.01\)）训练轻量 MLP，对所有候选接缝输出连续 **boundary strength**。
特征在词接缝处用 Praat/Parselmouth 等提取；在大规模日语语料上验证。

## 实验与结果
摘要：日语大语料上，声学锚点 + PU 可恢复有意义的韵律边界模式，提供可解释、省标注的边界建模。
（抽取偏方法；具体 precision/AUC 表未完整出现在可读段。）

## 结论
优先高精度正锚再 PU 传播，可不依赖人工韵律标签估计边界强度，为后续合成/ASR/标点等提供数据高效路径。

## 点评
把“宁可少而准的正例”写进锚点层级，符合韵律边界感知上长停顿更可靠的语音学直觉。强在可解释声学配方；脆弱在 \(\pi\) 与停顿阈值敏感、且对无明显停顿的弱边界覆盖有限——作者亦以 precision 换 recall。


# ArtNet: A JEPA-Like Articulatory Predictive Framework for Robust Zero-Shot Phoneme Recognition

- 论文编号：304
- 报告人：Yaqian Zhou
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/hu26_interspeech.pdf

## 问题
零样本跨语音素识别中，直接声学→音素映射脆弱：未见语言上替换错误占主导（文中宏观约 84.7% PER 来自 substitution），且大量替换源于已学音素表征不稳而非仅未见音素。

## 方法
**ArtNet**（类 JEPA）：在 SSL 特征上预测结构化 **发音特征**，而非直接符号；**VIB** 抑制语言特异变异。推理配合 **VSIA（vector-space inventory alignment）** 做音素清单对齐。比较 TDNN 等 ArtNet 变体；源语言训练、七种未见语言零样本测 PER / PFER（音素特征错误率）。

## 实验与结果
Table 1（节选）：ArtNet+VSIA 平均 PER **45.54%**（ArtNet 单独 54.94；基线更高），相对竞争基线约 **20.56% 相对 PER 下降**、**7.01% 相对 PFER 下降**；部分语言绝对 PER 降幅约 28 点量级。

## 结论
以发音特征预测为桥梁可增强跨语声学鲁棒性；与清单向量对齐结合后，零样本音素识别显著优于直接映射基线。

## 点评
把 JEPA“预测结构化表征”迁到发音特征空间，针对替换错误主导的诊断对症。强在 PER/PFER 双指标与多语零样本；脆弱在发音特征定义与清单映射质量——VSIA 增益大，说明仅预测仍不够，还需目标音系几何对齐。


# wav2VOT: automatic estimation of voice onset time, closure duration, and burst realisation with wav2vec2

- 论文编号：743
- 报告人：James Tanner
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tanner26_interspeech.pdf

## 问题
语音学流水线中 VOT、闭塞时长、爆破实现等标注常需大量人工校正或专用训练数据。大模型如 wav2vec2 在分类任务上表现好，但能否直接服务塞音细粒度声学标注仍待检验。

## 方法
提出 **wav2VOT**：基于 wav2vec2 对塞音片段做帧级分类（闭塞/爆破等状态），经上采样达约 **1 ms** 时间分辨率，再由状态序列推定 VOT、闭塞时长与爆破是否实现。可零样本用于未见语料，也可对目标数据集微调。默认最小区间约 5 ms。

## 实验与结果
- 初始模型：帧准确率约 **96.4%**；爆破实现准确率 **93.3%**（F1 0.96）；微调后更高。
- 未见语料（如 SWB、BB）上，多数 VOT 在 5 ms 容差内的比例与既有工具可比（如约 80% vs 73–79%）；闭塞时长估计容差略宽。
- 贝叶斯对比显示，手动与 wav2VOT 在整体 VOT/闭塞时长及清浊、部位效应上差异可忽略（如浊音对比约 10.76 vs 10.5 ms）。

## 结论
wav2vec2 类大模型可产出接近人工的塞音标注；微调进一步提升，并激励将其用于更多语音学标注任务（如负 VOT、预送气等）。

## 点评
把通用 SSL 表征接到经典语音学测量点，门槛低于专用对齐器再手工改。强在跨语料可比与效应量验证；脆弱在闭塞边界本身就比 VOT 难标，以及不同三向对立/方言实现需额外验证。


# Time-normalized spectrograms reveal segmental differences in English heterographic homophones

- 论文编号：793
- 报告人：Yu-Hsiang Tseng
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26_interspeech.pdf

## 问题
异形同音词常被假定“听起来一样”，但时长已显示与频率相关。段落层面（音段实现）是否也系统性不同、是否受话语语境意义塑造，仍缺大规模声学证据。

## 方法
收集 35 对异形同音词各 200 token（共 **14,000**）：做 **时间归一化频谱图**，并导出 phone logits；用 GPT-2 得上下文嵌入（CE），度量同音对内语义可分性。分析频谱/phone logits 能否区分词型，并回归语义对比、频率、搭配概率等协变量。

## 实验与结果
- 时间归一化频谱已能系统预测同音对内词型；phone logits 显示细微差异（如 *wait* 元音起音慢于 *weight*）。
- CE logits 对 spectral logits 有正向效应：语境语义越可分，语音 token 越易正确分类。
- 时长归一化后，词长效应弱；频率呈 U 形；前后词高概率搭配时 spectral logits 更大（实现更“典型”）。

## 结论
同音词只是近似同音；具体实现受 token 级意义共定。结果更支持形式–意义在 token 层对齐的词库模型（如 Discriminative Lexicon），而非把音段当作纯抽象符号。

## 点评
用时间归一化频谱避开单纯时长解释，把“意义塑形发音”落到可量化的频谱/phone logits，方法干净。强在大样本与 CE 控制；脆弱在 GPT-2 语义代理与英语同音对选取——推广到其他语言需谨慎。


# Minimum Token Thresholds and Stabilisation for Reliable Automatic Vowel Alignment: Empirical Study on TIMIT Vowels and MFA

- 论文编号：934
- 报告人：Simon Gonzalez
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26d_interspeech.pdf

## 问题
强制对齐已成语音学标配，但声学测量要多少 token 才“够稳”、与人工边界可比，仍缺经验阈值。低资源与大规模社会语音学都需要最小样本量指南。

## 方法
在 TIMIT 元音上，以人工音素边界为金标准，用 **MFA** 自动对齐；对 Duration、F1、F2 递增抽样 token，逐步拟合混合效应模型，比较自动 vs 人工测量差异轨迹，定位 **稳定点**（趋势平台）与 Kendall τ。

## 实验与结果
- **85%**（33/39）元音–特征组合随 token 增加显著改进；F1 对所有元音均改进。
- 多数约在可用 token 的 **50%** 附近稳定；Duration 最早（约 **24% / ~30 tokens**），F1 约 36% / ~1088，F2 最晚（约 **56% / ~1335**）。
- 元音间差异大：如 IH 较早稳定（约 31%），AW/AO 更晚（约 82–86%）。

## 结论
给出按特征分化的最小 token 经验阈值：时长最省数、F2 最耗数；增大自动对齐样本通常使测量更接近人工金标准。

## 点评
把“对齐够不够”做成可操作的稳定点曲线，对社会语音学抽样设计很实用。强在特征分层；脆弱在仅 TIMIT+MFA——其他对齐器/语体/语言的阈值可能平移，不宜直接外推绝对数字。


# Word Lengthening as a Function of Utterance Position: A Multi-Corpus Study

- 论文编号：1379
- 报告人：Mateo Cámara
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/camara26b_interspeech.pdf

## 问题
话轮转换需在数百毫秒内预测话轮结束；边界前延长是重要韵律线索。需检验：话轮末词是否更长、是否仅为词汇选择、延长集中在词内何处，以及跨语体/语言是否稳健。

## 方法
四语料、英西双语（Switchboard、Columbia Games、BU Radio、Glissando）：>500 说话人，约 **39,470** 话轮末 + **206,268** 句中词。比较话轮末 vs 句中时长；同说话人–同词配对；音节定位；对照 ToBI 式 break index。

## 实验与结果
- 基线：话轮末均长约 0.44 s vs 句中 0.24 s（差约 203 ms；\(d\approx1.22\)）；摘要池化约 **+91 ms**（\(d=1.14\)）。
- 严格配对：约 **+80 ms**（\(p<0.001\)；77% 配对为正）；约 92.8% 词型呈正效应。
- 效应主要在 **末音节**（话轮位置对比末音节 \(d=0.09\)，非末音节 ≈0）；高 break 词更长（高 vs 低约 +215 ms）。
- 朗读语料英西均见一致方向。

## 结论
话轮末延长是稳健、局部（末音节）的地板移交线索，与韵律边界强度并行，而非单纯选更长词。

## 点评
多样本、配对与音节定位把“话轮末更长”钉成边界 contr ol 而非词汇混杂，对对话系统与转写对齐都有用。强在跨语料一致；少数反转集中在截短的 backchannel 类词，提示范畴边界仍需小心定义。


# Larynx segmentation in mid-sagittal speech production real-time MRI

- 论文编号：1402
- 报告人：Xuan Shi
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26v_interspeech.pdf

## 问题
喉部时空动态与协调在言语产生中仍刻画不足。中矢状面实时 MRI 可观察喉结构，但小结构分割难、标注贵，需要可复现的分割管线与标注量指南。

## 方法
基于 **Mask2Former** 的喉部分割管线：监督学习 + 半监督精炼。在多说话人中矢状 rt-MRI 上评估不同标注比例的 AP/DSC；以 5% 边际收益阈值估计够用标注量。再用分割结果做普通话声调的喉部动态个案分析（声带长度、喉高、甲状软骨倾角等）。

## 实验与结果
- 低标注区 AP/DSC 上升快；按 5% 边际收益，约 **25–60%** 标注后收益递减，对应约 **3–9 标注/人**（约 5–50% of 794 训练样本 / 6 人，依摘要区间）。
- 半监督在中低标注量有小幅提升，但有时退化，达不到全监督上界。
- 大结构（杓状软骨、会厌、声带）DSC 更高（如杓状 ~0.86）；甲状腺等更难（DSC ~0.66）。
- 声调分析：声带长度与 F0 共变；喉高、甲状倾角呈调型差异；25% vs 100% 标注轨迹大体相似。

## 结论
少量高质量标注即可支撑语音学可用的喉部分割；rt-MRI 能同时捕捉内在与外在音高控制及喉收紧机制。代码已开源。

## 点评
把分割“标多少够用”做成边际收益曲线，对 rt-MRI 语音学很务实。强在结构难度分层与声调应用演示；半监督不稳定与甲状腺难标是明确边界。


# Reconciling Dynamic Data Analysis with Linguistic Reality: Comparing Legendre Polynomial Modelling and GAMM Applied to Prosodic Contact

- 论文编号：2585
- 报告人：Angelo Dian
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/dian26_interspeech.pdf

## 问题
接触引发的语调变异是动态轮廓问题；单点音高分析不足。Legendre 多项式与 GAMM 都能建模非线性 F0，但各自揭示的语音学信息、如何对接音系解释，需在同一接触语料上对照。

## 方法
以塞浦路斯希腊语（CYG）与雅典希腊语（ATG）年轻人延续升调为案例：在兴趣区（RoI）上分别做 **Legendre 多项式系数**（再 LMER）与 **GAMM** 平滑比较。CYG 按听感核高/核低分为 CYG-nh / CYG-nl。

## 实验与结果
- 两法一致：CYG-nh 与 CYG-nl、ATG 不同——整体斜率更小、曲率更大、更 N 形；ATG 与 CYG-nl 相近。
- 多项式：variety×tone 对 c1–c3 均显著（如 c1 \(F(2,21.41)=74.872,p<.001\)）；CYG-nh 在三维系数空间独立成簇。
- GAMM：形状差异显著、整体高度不显著；CYG-nh vs ATG 在归一化 RoI 约 **29–50%** 核高目标附近显著偏高，并与 CYG-nl 在更大区间有差异。

## 结论
多项式抓全局几何，GAMM 定位相对时间上的局部差异；互补使用更利于接触语调的语音实现与音系解释。

## 点评
方法论文色彩强：同一语言事实上展示两种动态分析各擅长什么。强在收敛结论 + 时间定位互补；样本年轻说话人、听感预分类可能影响类别边界，但作者以档案研究为先验支撑。


# Achieving voicelessness in coda stop contexts: Insights from combined electroglottography and laryngoscopy

- 论文编号：2610
- 报告人：Joshua Penney
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/penney26_interspeech.pdf

## 问题
英语韵尾清塞音可通过声门张开或收缩实现清音，并影响前接元音音质。EGG 显示澳英 /t/ 偏收缩、/k/ 偏张开、/p/ 不一；但 EGG 只间接反映声门阻抗，无法直接看声门上构型。

## 方法
联合 **EGG（开商 OQ 轨迹）** 与 **喉镜成像**，观察韵尾 /p,t,k/ 前元音上的声门/会厌喉收紧，对照短语末与鼻音前位置，检验 EGG 推断与可见喉行为是否一致。

## 实验与结果
- **短语末**：各部位 OQ 随元音推进下降（收缩增加），CI 大量重叠——收紧是共同策略。
- **鼻音前**：/t/ 仍明显收缩；/k/ 末段 OQ 上升（张开/气声）；/p/ 轨迹平坦略降，模式不清。喉镜图像与上述部位差异一致（/t/ 维持收紧，/k/ 声门开、会厌喉收紧减弱）。
- 个体与条目变异大；部分条目末尾突然释放收紧，喉镜可见会厌喉开度突变。

## 结论
支持近期 EGG 发现，并显示短语末位置各部位清塞音更偏好 **收紧** 策略；鼻音前则保留部位分化。EGG 与喉镜大体对齐，后者补充声门上信息。

## 点评
双模态验证把“间接电生理”钉到可见喉状态，对韵尾声门化文献很关键。强在位置×部位交互；变异大提示不能把平均轨迹当成单一说话人策略。


# Multilingual and Cross-lingual Lexical Stress Detection Using SSL Feature Vectors

- 论文编号：2914
- 报告人：Abdulrahman Alhabshi
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/alhabshi26_interspeech.pdf

## 问题
词重音对可懂度重要，但阿语与英语实现不同，多语与跨语检测困难。需检验固定 SSL 特征 + 轻量分类器在单语、联合多语与跨语迁移上的表现差异。

## 方法
冻结 SSL 编码器（HuBERT、WavLM、XLS-R）提特征；两阶段分类：**音节级 Pre-net（DNN）** + **词内音节依赖 Post-net（TDNN）**。比较单语、阿–英联合多语、双向跨语迁移。

## 实验与结果
- 多语训练接近单语：英约 **97%**、阿约 **90%**（摘要）；实测多语均值阿 87.87%、英 95.24%；最高如 HuBERT Post-net 英 **97.08%**、WavLM Post-net 阿 **89.77%**。单语基准约英 97.49%、阿 90.56%，优于先前约 91%/82%。
- Post-net 相对 Pre-net 有稳定小幅增益。
- 跨语明显下降且方向不对称：英→阿均值约 **68%**（最佳 XLS-R Post-net 79.17%）；阿→英约 **76%**（最佳 86.69%）。跨语时多语预训练的 XLS-R + Post-net 最稳。

## 结论
SSL 特征支撑高准确阿/英重音检测；联合多语几乎不损单语，跨语则依赖方向与时序建模；Post-net 与多语预训练有助于迁移。

## 点评
把重音检测做成可控的训练体制对比，突出类型学差异（阿语量敏感 vs 英语元音弱化）解释迁移不对称。强在三编码器×两阶段网格；跨语仍远低于单语，说明“共享韵律特征”不能替代目标语音系约束。


# Scaling Human and G2P Supervision for Robust Phonetic Transcription

- 论文编号：3271
- 报告人：Alexander Metzger
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/metzger26_interspeech.pdf

## 问题

精细语音转写（IPA）对临床评估、发音训练等很关键，但专家标注昂贵，非母语与非典型语音更难标。常见做法是用 G2P 从正字法转录大规模生成音素标签，隐含假设“标签数量可弥补噪声”。作者指出 G2P 反映的是某一方言的规范发音，难以刻画说话人特异、误读与非典型实现，可能把模型偏向标准发音、削弱对声学变异的敏感度。本文不提新架构，而是系统研究人类标注与 G2P 监督在质量与数量上的交互，问清“多少专家标注之后大规模 G2P 开始边际收益递减”。

## 方法

整理约 80 小时带专家音素标注的英语语料（TIMIT、L2-ARCTIC、EpaDB、Speech Ocean、Buckeye、PSST、DoReCo、ISLE 等），覆盖多种母语方言、8 种 L1 背景的 L2 语音及卒中后失语；预处理后约 54.75 小时干净语音（训练约 40.81、测试约 13.94）。ISLE（意/德）作未见方言测试，TIMIT/EpaDB/PSST/Speech Ocean 作已知方言未见说话人测试。指标为 PanPhon 的加权 Phone Feature Error Rate（WPFER），按发音特征差异给替换部分分数。

课程分四阶段对比：自监督预训练（Wav2Vec2-XLSR / HuBERT / WavLM 等）、多语 ASR 微调、G2P 机器音素标签微调、人类专家音素微调。在固定音频上按比例把人类标签换成 G2P 标签做缩放实验，并检验是否叠加约 5.3K 小时 G2P 数据。

## 实验与结果

最优课程（XLSR 预训练 + ASR 微调 + 约 40 小时人类音素监督）平均 WPFER 约 3.5%，相对先前系统约 2.3× 降低，在非母语与失语（PSST）上提升明显。消融显示：有人类微调时再加 G2P 对未见方言（ISLE）无显著收益甚至略伤泛化；ASR 预训练则无论微调数据如何都能显著降错。缩放曲线表明：人类数据增加显著降错；G2P 预训练仅在人类标注少于约 20–30 小时时有帮助，超过该阈值后常无显著收益甚至变差。全人类标签均值 WPFER 约 3.4%，全 G2P 约 5.5%。

## 结论

在英语设定下，一旦约有 20–30 小时多样人类音素标注，额外 G2P 监督通常不再显著有益，甚至可能略损跨方言与非典型语音；ASR 预训练则持续改善域外泛化且不引入 G2P 式规范发音偏置。局限为仅英语与所覆盖方言；未来需检验其他语言与更极端低资源条件是否存在类似阈值。

## 点评

核心贡献是把“G2P 大规模是否总是更好”做成可控缩放与课程消融，而不是再堆一个转写网络。阈值现象与“ASR 中介带来说话人/方言多样性但不锁死规范音素”的解释，对临床与方言鲁棒转写路线有直接启示：中等规模高质量人类标注可能比盲目扩 G2P 更划算。脆弱点在于阈值依赖其清洗后的 40 小时人类训练集构成与 WPFER 定义；若目标语言或标注粒度不同，阈值位置可能移动，且结论外推需谨慎。

