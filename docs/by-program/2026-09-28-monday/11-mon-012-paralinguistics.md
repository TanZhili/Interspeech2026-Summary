# Paralinguistics

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：3
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

副语言学本场从情绪识别训练策略延伸到 LALM 评测、生理周期、统一副语言理解、韵律可视化、二语口音可理解度，再到关系性情感范式与弱监督情绪日志。CHUCKLE 用众包标注一致性定义样本难度做课程学习，把“对人难”当作对网络也难的先验。

评测与模型能力方面，ParaPairAudioBench 在五维副语言成对比较上显示 LALM-as-a-Judge 仍落后人类且在平局弃权上校准失败；ParA-LLM 以 22 维特征与大规模 Audio-QA、两阶段课程补齐说话人/环境理解，并放出高难度基准。生成侧 NovaDiffusion 把情绪相关韵律注入扩散图像合成；应用侧尝试从朗读语音预测月经周期相位，以及用 Speech LLM 近似人类口音度/可理解度评分。

理论与时序建模上，有工作主张以互动场中的情感共振/活力轮廓替代孤立说话人离散情绪标签；P-SED 用原型度量学习与弱监督做语音情绪日志。瓶颈是主观难度定义、细粒度副语言评测校准、生理信号微弱，以及从话语级标签学帧级情绪边界。

## 论文技术总结

# CHUCKLE - When Humans Teach AI to Learn Emotions the Easy Way

- 论文编号：1591
- 报告人：Ankush Pratap Singh
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/singh26b_interspeech.pdf

## 问题

语音情感识别（SER）标签主观、噪声大，课程学习（CL）从易到难训练有吸引力，但既有难度定义多为启发式、数据驱动或模型驱动，较少对齐人类感知难度。作者认为：对主观任务，众包标注中的一致性与“意图—感知”对齐，才是更自然的难度信号。

## 方法

提出 CHUCKLE：在 CREMA-D（7442 片段、91 演员、6 情感；每段有意图标签与 8–12 名评分者感知标签）上，用两类课程构造难度排序。分数式：意图情感得票比例、标注分布熵，再按四分位分成 Easy / Borderline Easy / Borderline Tough / Tough。规则式：把样本划为 Clear Match、Clear Mismatch、Ambiguous Match、Ambiguous Mismatch，再给出三种由易到难排序（Agreement 1/2/3），分别强调一致性强度、与意图对齐、或二者折中。训练按 bin 递增加入样本；输入为未微调的 HuBERT-Xlarge 帧级表征，分类器为 2 层 BiLSTM 或 2 层 Transformer；对比非课程、随机课程与各类感知课程；评测含 subject-dependent 与 subject-independent，指标为 mean macro accuracy。

## 实验与结果

规则式 Intended-Perceived Agreement 1 在多数设定最优且常达显著：subject-dependent 上 LSTM 0.6623、Transformer 0.6827；subject-independent 上 LSTM 0.6669、Transformer 0.6857。相对非课程基线，规则课程相对准确率提升约 LSTM 0.7%–1.8%、Transformer 0.8%–3.0%；Agreement 1 约少 17% gradient updates，Agreement 2 可少近 40% updates 且准确率仍可比。随机课程往往不升反降。

## 结论

众包中的标注一致性与意图—感知对齐可作为 SER 课程的有效难度信号；规则式课程在准确率与效率上优于非课程与分数式课程，且在跨说话人设定仍有收益。方法在样本排序层工作，模型无关，前提是同时有意图与感知标签；未来拟扩展到多模态与更多数据集。

## 点评

做法抓住的是 SER 特有的“双标签”结构：不仅看 annotator 分歧，还显式建模与演员意图的匹配/错配，尤其把“一致但错配”当作最误导信号之一，比单纯熵排序更贴近主观任务的噪声机制。强项是同时报告准确率与梯度更新成本。脆弱点是依赖 CREMA-D 式 acted 数据与意图标签，真实自发语料往往没有“intended emotion”；绝对增益不大，且难度假设“对人难则对网难”未必处处成立。


# ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge

- 论文编号：2021
- 报告人：Jisu Jeon
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/jeon26d_interspeech.pdf

## 问题

大音频语言模型（LALM）已常被当作生成语音的自动评委，但先前多盯整体自然度，细粒度副语言属性是否判对、能否在模糊时弃权（Tie）、是否依赖文本线索与呈现顺序，仍缺乏可控诊断。自然度总分会掩盖“全局节奏强、局部强调弱”等行为差异。

## 方法

构建 PARAPAIRAUDIOBENCH：5175 对音频，覆盖 Style、Rate、Emphasis、Age、Gender 五维；每例三选一（A / B / Tie）。数据来自 Expresso、Sonos Voice Control Bias Assessment、LibriTTS、EARS 等官方测试切分，并按标签、转录控制与平衡约束筛选。Non-Tie 对比目标/非目标；Tie 在 Style/Age/Gender 上平衡 Both Good / Both Bad，Emphasis 仅 Both Bad，Rate 不含 Tie。约 47% same-transcript、53% cross-transcript，以区分声学依赖与词汇依赖。评测 Gemini 2.5 Flash、GPT-4o Audio、SpeechJudge-7B、Kimi-Audio-7B、Qwen2.5-Omni-7B；交换 A/B 顺序测位置偏置；人类基线为每准则 50 题、6 名评分者（Fleiss’ κ=0.67）。

## 实验与结果

人类平均准确率 79.2%，最强模型 Gemini 2.5 Flash 为 61.5%（平均落后约 17.7%p；摘要亦写相对人类平均落后约 32%p）。Rate 上模型相对较强，Emphasis 等局部韵律更弱。普遍校准失败：Non-Tie 可较高而 Tie 骤降（如 Gemini Emphasis NT 82.3% vs T 19.3%；SpeechJudge 多维 Tie 近乎从不选）。Style 在 same-transcript 明显高于 cross-transcript（Gemini 83.8% vs 36.6%），Emphasis 则相反，显示模型对局部突显敏感不足、对 Style 过度依赖词汇。位置偏置可达约 29.4%p（SpeechJudge）。Age 对人类也难（κ=0.365），Gemini 略超人类约 3.8%p。

## 结论

该基准把副语言评委能力拆成准则区分、Tie 校准、转录敏感性与顺序鲁棒性；现有 LALM 评委整体仍逊于人类，并暴露强制偏好、模态依赖不对称与位置偏置等系统性失效，单看自然度总分看不见这些点。

## 点评

贡献主要在评测协议设计：把“会不会判副语言”变成可分解诊断单元，尤其是 Tie 与 same/cross-transcript 对照，能把“看起来准”拆成真声学能力 vs 文本捷径。对 LALM-as-a-Judge 落地很有用。脆弱点包括 Rate 无 Tie、Emphasis Tie 仅 Both Bad、部分语料与模型可能预训污染虽已尽量用测试切分；人类子集仅 250 题，Age 本身主观噪声大，绝对数字需结合置信区间解读。正文末尾抽取有截断，结论以上述可读部分为准。


# Predicting Menstrual Cycle Phases from Speech: A Paralinguistic Approach

- 论文编号：1878
- 报告人：Anika A. Spiesberger
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/spiesberger26_interspeech.pdf

## 问题

月经周期激素波动可能影响发声，但声学参数研究结论不一致；多数工作用少量预定义特征与群体均值检验，难以捕捉细微、多变量模式，也很少做个体层面相位预测。作者希望用更大规模手工特征与嵌入，检验排卵期与黄体期是否可分，并看说话人级准确率是否与激素水平/变化或年龄相关。

## 方法

德语朗读语料：76 名 18–44 岁自然周期、未用激素避孕的母语者，每人两相位各约 15 句（共 2277 文件，约 84.35 分钟），并有唾液雌二醇、孕酮、睾酮。特征：eGeMAPS（88 维，openSMILE）与 wav2vec2-large-robust 情感微调模型倒数第二层 1024 维嵌入。先对 eGeMAPS 做配对 Wilcoxon + Bonferroni-Holm，并报告 |r|>0.2 的效应量。分类用 XGBoost、SVM、Random Forest、Logistic Regression，嵌套交叉验证（外层 leave-one-group-out，内层 group 3-fold）；说话人级多数投票后报准确率与 bootstrap 95% CI；再用 Pearson 相关分析说话人级准确率与激素及年龄。

## 实验与结果

多重校正后无特征显著；25 个特征有至少小效应（|r|>0.2），黄体期多表现为更高响度、谱通量、H1-H2 及部分共振峰幅度统计量。eGeMAPS 上 RF/LR 准确率最高 62.5%（95% CI 约 [54.6; 69.7]），高于 50% 机会水平；wav2vec2 嵌入各分类器 CI 均与 50% 重叠，未显著超机会。说话人级准确率变异大（eGeMAPS 部分人可达 0%–100%），跨分类器高度相关，但与平均激素、相位间激素差、年龄均无显著相关。

## 结论

排卵—黄体间存在小的声学效应痕迹，手工特征可中等程度预测相位，而所用情感微调 wav2vec2 嵌入未超机会；个体可预测性差异大，且与激素线性指标、年龄无显著相关。作者建议更多周期相位、个性化基线归一、以及直接预测激素水平；局限含响度未严格控录、可能存在无排卵/相位错标、单标注者切分、仅朗读等。

## 点评

问题设定诚实：承认单变量效应弱，转而问“能否预测”与“谁可预测”，并用嵌入对照手工特征，避免只报显著检验。结果提示该生理状态信号可能更贴近可解释声学描述子，而非该情感 SSL 嵌入空间；说话人异质性高也说明群体模型上限有限。脆弱点是效应小、样本量与相位估计噪声、响度可能受录音条件影响，且嵌入模型英/情感预训练可能不匹配德语生理状态任务。


# ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding

- 论文编号：3015
- 报告人：Nishit Anand
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/anand26_interspeech.pdf

## 问题

Audio LLM 在 ASR 等内容理解上已接近人类，但对副语言与声学条件（说话人特质、表达变化、混响噪声等）理解仍弱：作者小样本观察中人类约 78%、GPT-4o-Audio 约 36%。既有系统多为单属性分类，难以对多个交互属性做自由问答与联合推理。

## 方法

定义 22 个属性（10 声学、7 说话人内禀、5 话语级）。声学侧用 EARS/Emilia/Expresso/VoxCeleb 等干净语音，经 RIR 卷积与噪声混合及后处理仿真，度量 DRR、RT60、ERR、DER、SNR、后处理、STOI 质量等并离散分箱。说话人与语音属性映射自多语料元数据（性别、口音、鼻音、音色、响度、平滑度、清晰度；情感、语速、音高、表达性、流畅度等）。生成逾 1.2M Audio-QA：Stage 1 模板生成 688K 单属性问答；Stage 2 用 Qwen2.5-7B ICL 生成 513K 多属性问答。ParA-LLM 自 Qwen2-Audio-7B-Instruct 出发，LoRA（r=128）两阶段各训 1 epoch。另建 ParA-Bench：6000 道多选题（说话人-语音 / 声学 / 混合各 2000），由另一模型族生成以降低自指偏差。

## 实验与结果

ParA-Bench 上 ParA-LLM 总体 43.53%（说话人-语音 55.85%、声学 34.80%、混合 39.95%），高于 GPT-4o-Audio 的 36.03% 与 Voxtral 的 38.80%；声学项 GPT-4o-Audio 仍最高（41.85%）。Omni 与推理型 Audio LLM（Mellow、R1-AQA）整体偏弱。相对 Qwen2-Audio-Instruct，课程后 MMAU-Pro Speech 40.96%→42.09%，MMAR Speech 35.37%→42.86%（+7.49%）。下游展示含自动标注、TTS 控制线索，以及用 ParA-LLM 生成约 150K IR 描述训练 Text2IR。

## 结论

结构化 22 属性数据 + 原子到多属性课程可显著提升统一副语言/声学理解，并外溢到更广音频基准；但相对人类仍有大缺口，多模态 omni 与 CoT 推理并不自动带来该能力。作者释放基准、模型与数据以推动后续研究。

## 点评

路线是“先把 how-it-is-said 做成可监督的结构化属性空间，再用课程从单因素到组合推理”，比继续堆通用 Audio LLM 更对准缺口。强项是同时有大规模训练数据、独立基准与外部基准增益。脆弱点在于大量声学标签来自仿真与离散化，说话人属性依赖映射/主观类别定义，ParA-Bench 仍远低于人类，且声学子项未超 GPT-4o-Audio，说明环境声学理解仍是短板。


# "Say That Again": Visualizing Paralinguistic Cues with Prosody-Aware Diffusion

- 论文编号：2102
- 报告人：Shyamji Tiwari
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/tiwari26_interspeech.pdf

## 问题

文生图忽略副语言：同一句“Are you serious?”因音高、语速、情感语调不同，听者脑中画面不同，但现有音频条件生成常把语音当作单一向量，不分离韵律与环境声/说话人/词汇。作者希望把与情感相关的韵律特征显式抽取出并注入扩散生成。

## 方法

NovaDiffusion 三件套：(1) ProsodyCLIP：在 ESResNeXt 通用音频嵌入上拼接 F0/能量/语速/MFCC 等韵律支路，两阶段 InfoNCE（AudioSet 再 ProsoBench）并加情感辅助 CE；(2) 约 280M 蒸馏 U-Net（BK-SDM + 多尺度融合）；(3) 仿 IP-Adapter 的解耦交叉注意，把韵律嵌入与文本嵌入分开注入（默认权重 α=0.6）。数据管线 ProsoBench：汇合 RAVDESS、IEMOCAP、MSP-Podcast 共约 168K 带标注情感语音，韵律-MLP 校验剔除约 12%，再 CLIP 检索 + 人工核验配图，说话人独立 80/10/10 划分。推理可用 OLSS 少步采样。

## 实验与结果

RAVDESS（8 类，机会 12.5%）上 ECA 71.3%，相对 SonicDiffusion 48.2% 高 23.1pp（同数据重训 SonicDiff.† 仅 52.6%）。ProsoBench 上 ECA 68.5%。IEMOCAP 未见说话人：63.4% vs 41.7%。消融：去掉韵律支路 ECA 跌至 57.2%；仅 hp 仍有 58.9%；去掉 L_CE 为 62.6%。人工评测 Emotion Match 3.82 vs 2.94（p<0.001）。作者强调 ECA 依赖人脸表情分类，不覆盖无脸场景级情感；配图来自 CLIP 检索，学的是文化刻板视觉相关而非物理共现。

## 结论

显式韵律增强 + 解耦适配器可让扩散图更跟随语音情感相关韵律；范围限于与类别情感相关的韵律，完整韵律控制仍开放。局限包括通用音频支路仍含词汇信息、ECA 脸偏、ProsoBench 的 CLIP 配对偏见等。

## 点评

把“音频条件生成”拆成韵律抽取—视听对齐—解耦注入，问题抓得准：同一文本不同说话语气应对应不同画面。用独立 AffectNet 分类器算 ECA、并报告同数据重训基线，有助于说明增益来自韵律而非数据域。脆弱点是评测与训练都高度绑定类别情感与面孔刻板图像，ECA 上限受分类器准确率约束，对场景叙事与细粒度韵律（非情感）外推有限。


# Can Speech LLMs Approximate Human Ratings of Accentedness and Comprehensibility? Evidence from Correlational and Feature-Based Analyses

- 论文编号：1991
- 报告人：Wenwei Dong
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/dong26c_interspeech.pdf

## 问题

二语音系评估常用 accentedness 与 comprehensibility 的人工量表，成本高。传统自动发音评估多走预定义维度或 ASR 指标，未必对齐人类感知。作者检验语音大模型能否近似人类评分、是否敏感于 CALL 前后进步，以及打分时依赖的音段/超音段线索是否与人类相近。

## 方法

印尼高中 EFL：33 名完成 36 天 ASR-CALL 练习者，前/后测各 28 句共 1848 句；9 名印尼母语专家用 9 点量表评分（高分=更接近母语/更好懂），ICC 很高。用 Qwen3-Omni-30B-Instruct 做 zero-shot 与 few-shot 提示打分；留出最低/最高各 1 名学习者作样例，其余 31 人（1736 句）测试。另提取 Praat 16 维、eGeMAPS 88 维、Whisper 词距离共 105 特征，经 Lasso 后按与分数的绝对 SPCC 排序，比较人类与 LLM 的线索重叠。线性混合效应模型以 Test（pre/post）为固定效应、说话人与句子为随机效应。

## 实验与结果

与人类相关中等：zero-shot 可懂度 SPCC 最高约 0.419；加朗读文本后两项相关下降。few-shot 中 Exp.6（低/中/高分各 2 例）MSE 最低（accent 0.82、comp 1.37），SPCC 分别为 0.283 与 0.497。LME 显示人类与 LLM 分数均显著 post>pre。句子级平均相关高于说话人级（可懂度句子级 SPCC 0.710）。特征上：人类 accentedness 更偏谱通量/响度等超音段，comprehensibility 以 Whisper Word Distance 居首；LLM 两边都重 duration、词距离、语速与响度，与人类部分重叠但不完全同序。

## 结论

语音 LLM 分数与人类中等相关，能捕捉 CALL 前后进步，并共享部分音段/超音段线索；仍需探索微调与融入语言学知识。提示设计敏感：分开打分优于同时打分，过多示例或附带文本可能干扰。

## 点评

工作价值在“对齐诊断”而不只报相关：用 LME 看发展敏感性，用特征排序看构念是否被误读。结果显示 LLM 更像粗糙的流利度/错误代理，对 accentedness 的超音段重心把握弱于人类。脆弱点是零/少样本未微调、评分者与学习者为同一 L1 背景、few-shot 样例选择可能影响尺度校准，且正文讨论后半有截断。


# Shifting Relational Paradigms for Affective Computing: Affective Resonance, Vitality Affects, and Vocal Interaction Fields

- 论文编号：2829
- 报告人：Cy Gorman
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/gorman26_interspeech.pdf

## 问题

情感计算主流把情感当作孤立说话人的离散类别或唤醒/效价状态；作者认为这对互动不完整。借鉴情感共鸣（affective resonance）与活力情感/轮廓（vitality affects/contours），主张分析单元应是由嗓音动态共同构成的互动场，而非个体内状态。既有声学entrainment多测特征趋同，少见方向性、互动体制分解与场级涌现检验。

## 方法

概念上提出 Affective Resonance Dynamic Ontologies（ARDO）与 Artificial Affective Resonance Intelligence（AARI）：系统应参与并调制关系动态，而非只分类个体情感。实证为概念验证：AMI Meeting Corpus 四说话人近讲话筒，60 s 窗；用 WavLM-Base+ 连续隐状态（不做量化聚类）提取跨层“expressiveness”等代理，并对能量残差化。按 VAD 定义 Tier A（重叠共现）、Tier B（汇合的非重叠单人活动）、Tier C（按谁在说话拆开的非重叠，作语料内负对照）。在体制连续片段上做双变量与四说话人条件 VAR 的 Granger 方向性检验；用循环移位空模型校准短序列假阳性，并以 DSS∈{−1,0,+1} 汇总窗级方向性（微尺度 ≤1 s，宏尺度 >1 s）。

## 实验与结果

方向性耦合在亚秒滞后、互向共现体制下更可检：Tier A 微尺度非零 DSS 质量最高且近对称；Tier B/C 更偏向零支持。移位空模型显示短序列显著性膨胀（如 Tier A 微尺度名义 p<.05 拒绝率约 11.9%，膨胀约 2.4×）。校准后 q=5% 时 Tier A 微尺度相对空模型约有 +6.6pp（双变量）与 +7.4pp（能量控制条件模型）超额拒绝；更严 q=1% 时效应减弱但仍呈体制特异：A 最强、B 弱、C 近空。作者称耦合不能只还原为能量同步，且跨特征有小而结构化效应。

## 结论

互动配置本身构成可测的表达耦合痕迹，个体状态管线难以利用；这支持把 ARDO/AARI 作为面向场级活力动态的设计约束。局限：expressiveness 非效价/离散情感；Granger 仅线性预测依赖；结果目前仅 AMI；Tier B 宏尺度样本不足；跨语料完整结果留待后续。

## 点评

这篇主要是范式转移论文：用体制分解 + 空校准方向性耦合，证明“关系结构在，个体独占说话时耦合塌缩”，从而反对只做说话人情感标签。对社交机器人/共情对话设计有启发。脆弱点是实证仍 prelim、特征代理抽象、统计管线复杂（FDR、窗门控、滞后网格），效应幅度不大且依赖 AMI 会议场景；从可测耦合到真正 AARI 生成闭环仍有很长距离。正文末尾抽取截断，以上述可读部分为准。


# P-SED : Asymmetric Prototype Metric Learning for Weakly Supervised Speech Emotion Diarization

- 论文编号：2388
- 报告人：Nurmemet Yolwas
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/liu26r_interspeech.pdf

## 问题

Speech Emotion Diarization（SED）要对连续语音中情感事件的起止与类别做细粒度定位，但帧级标注极稀缺（公开 ZED 仅约 17 分钟），难以全监督训练。弱监督常用 MIL：极端池化监督过稀，把句级标签铺到全帧又易在静音/过渡段引入噪声。需要在仅有句级标签时仍能定位连续情感片段。

## 方法

P-SED：WavLM 提帧特征，投影并 L2 归一化到单位超球面，与可学习情感原型（含 Neutral）做温度缩放余弦相似度得帧 logits。正交正则 L_orth 抑制“中性主导坍缩”。弱监督用非对称优化：Class-aware Prototype Contrastive Loss（CPCL）对中性袋用多类 CE，对情感袋仅对比目标情感相对中性的响应并动态伪标；Top-K ranking loss 在情感袋上对 top-p% 显著帧施 margin 约束。另有句级加权池化辅助分类。推理对各类概率序列做 Total Variation Denoising（TVD）再归一化，抑噪同时保锐利边界。

## 实验与结果

IEMOCAP（Happy/Angry/Sad/Neutral，Session 1–4 训、5 验）作弱监督训练，ZED 作帧级测试。同 WavLM 骨干下，P-SED+TVD 的 EDER 为 47.00%，优于 frame-wise CE（56.52%）、ENT/FENT（55.16%/54.37%）及 MA/GEP 后处理；无后处理 RAW 为 50.67%。消融去掉原型、正交、CPCL 或 Top-K 均升高 EDER；Top-K 比例约 0.6 较好。配对 t 检验相对基线显著（p<0.05）。

## 结论

正交原型空间 + 非对称显著实例挖掘 + TVD，可在仅句级标签下做连续情感定位，并在 ZED 上优于对比弱监督基线。局限：固定比例挖掘难适应快速多变情绪转换；测试集规模小，泛化评估受限。未来拟自适应挖掘、上下文序列建模与更大帧标注集。

## 点评

抓住 SED 的结构难点：中性背景占时长、情感局部连续、弱标签易确认偏置。把“目标情感 vs 中性”做成袋级二元对比，再用 Top-K 补局部边界，比单纯 max-pool 更贴合情感事件形态。脆弱点是依赖 IEMOCAP→ZED 的跨语料迁移与固定 p，真实对话情绪更碎时可能漏检；EDER 仍较高，说明弱监督 SED 距离可用仍远。

