# Brain Studies and Speech

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster
- Area：1
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接神经解码、说话人身份神经表征、认知负荷下的归一化与掩蔽、双语执行功能、屏幕阅读语速能力，以及增强效果的 fMRI 神经评测与 EEG 引导说话人提取。方法光谱从迁移学习、对比对齐、fMRI/MEG/EEG 实验到心理语言学与 IRT 建模。

脑机接口侧强调少数据：MEG 感知预训练可迁移到产出与跨任务；EEG–语音时间对齐用监督对比分类；SAGE 面向试验内注意切换的软门控提取。认知神经侧显示说话人特质并非单一构念，粤语声调归一化在负荷下依赖主动控制，PMBR 或表征构音复杂度。行为与应用侧覆盖掩蔽语言熟悉度、语码转换动机与工作记忆/抑制，以及视障用户语速 IRT；NeuroPAS 则用 fMRI 解码器度量增强是否更接近 Clean 神经模式。

## 论文技术总结

# MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data

- 论文编号：439
- 报告人：Xabier de Zuazo
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zuazo26_interspeech.pdf

## 问题
非侵入式言语 BCI 的 MEG 解码常受单被试数据极少（分钟级）限制，现有做法多为每被试、每任务从零训练；MEG→MEG 预训练及感知–产出跨任务迁移尚未系统验证。

## 方法
在 LibriBrain（单被试约 50 h 听录音书，306 通道，250 Hz）上预训练 MEGConformer，做语音/静音检测；再在 Bourguignon 等 18 名西语被试数据上微调（听、回放、出声朗读各约 5 分钟）。输入为 0.5 s 窗原始传感器；微调引入 RollAugment、软标签（窗内语音占比）等。对比同任务（in-task）与六种跨任务（train→test 不重训）下“从零训练 vs 预训练+微调”，指标 F1-macro、balanced accuracy、AUC-macro，Wilcoxon + Holm 校正与置换检验。

## 实验与结果
In-task：听任务迁移显著（准确率 +3.7%、F1 +2.6%、AUC +7.3%）；回放/产出有小幅提升但不显著；总体置换检验 p<0.001。跨任务从零已全体显著高于机会（准确率约 65.0–73.4%）。迁移后听↔回放增益最大（准确率约 +6.1–6.3%），涉及产出的跨任务也显著受益（约 +4.8–5.3% 准确率）。感知→产出优于产出→感知；多数被试正向迁移但个体差异大（如 Subject 16 产出 F1 −13.3%）。

## 结论
大规模单被试 MEG 预训练可在新被试、分钟级数据上提升语音检测，并增强感知–产出跨任务泛化；产出→听仍可高于机会，说明学到共享言语表征而非仅运动伪迹。局限：仅检测任务、英↔西语、单被试预训练、增益幅度有限且不稳定。

## 点评
工作把“临床标定数据太少”转成 MEG 领域迁移问题，并用跨任务方向性不对称来区分共享听觉表征与产出特有运动成分，比单纯刷同任务准确率更有信息量。脆弱点在帧级随机划分、不同实验室/语言与软标签设定，以及检测任务距音素/合成解码仍远。


# SCANS: Supervised Contrastive Temporal Alignment of Neural Responses and Speech Stimuli

- 论文编号：2651
- 报告人：K M Naimul Hassan
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hassan26_interspeech.pdf

## 问题
EEG 与言语刺激的时间对齐常被形式化为 match–mismatch 分类，但多数模型晚融合、自监督对比又受正负样本稀缺与跨被试噪声限制，难桥接模态差距。

## 方法
SCANS 将任务定义为：给定 EEG 片段与同一语音中的 N 个非重叠候选，找出唯一时间对齐的匹配段。两侧同构编码器：Dilated Convolutional Frontend（EEG 64 通道→128 维空间滤波；语音包络→128；三层膨胀卷积 dilations 1/2/4）+ 对称 Cross-Modal Attention（4 头，互相以对方为 K/V）。全局平均池化得 L2 归一化嵌入；候选与 EEG 拼接后经 MLP 分类。损失 `L = L_CE + λ L_align`（λ=0.5），其中对齐损失为 batch 内严格一一对应的对称 InfoNCE（可学习温度 τ）。

## 实验与结果
SParrKULee / ICASSP Auditory-EEG Challenge：EEG 0.5 Hz 高通、Wiener、平均参考、64 Hz；gammatone 包络 + x^0.6，64 Hz。窗长 t∈{3,5}s，候选 N∈{2,5}。N=2,t=3：Within MSA 87.09、Held-out 84.12，Total Score 86.1（2023 榜首 Thornton 等为 82.13）。N=5,t=5 Held-out MSA 69.33（HSSTD 4.60），高于 Wang/Thornton 等（约 60–62.8）。更长窗普遍提升准确率并压低被试方差。

## 结论
作者认为扩张卷积前端 + 全程跨模态注意力 + 监督对比多任务目标，可在有限样本下学到更稳的 EEG–言语共享空间，并在 2023/2024 挑战设定上达到新 SOTA，对未见被试泛化更好。

## 点评
相对晚融合余弦匹配，SCANS 把“标签可用的严格时间同步”写进对称对比矩阵，比纯 InfoNCE 自监督更贴合该任务；跨模态注意力直接打通特征提取中的模态缺口。代价是对 challenge 划分与硬负采样依赖强，N=5 held-out 方差仍可能被窗长掩盖个体差异。


# Is Speaker Identity a Unitary Construct? Neural Evidence for Distinct Trait Processing

- 论文编号：1018
- 报告人：Kaile Zhang
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26r_interspeech.pdf

## 问题
说话人身份常被当作单一构念，主要定位于双侧 STG/STS（TVA）；但性别、年龄、口音等特质声学/音系线索不同，是否共享同一机制尚未分清。

## 方法
34 名普通话母语成人做 fMRI（3T Prisma）。刺激为 ChatGPT-4 生成、OpenAI TTS 合成的伪英语词，分性别（2 男 2 女成人）、年龄（儿童/成人）、口音（英式/印度英语）三任务，另有纯音高低基线。Block 设计：听刺激并按键判断特质。DeepPrep 预处理；表面 GLM 对比各特质相对纯音，簇置换检验；三特质 conjunction 定义共享 ROI，再对 ROI 内激活做重复测量 ANOVA。

## 实验与结果
行为：口音最难（准确率 86.76%，RT 约 1087 ms），性别最易（97.70%，约 854 ms），年龄居中。影像：三条件均激活双侧 STG/STS/HG；conjunction 得共享“voice core”。ROI 内口音激活显著强于性别与年龄；年龄额外招募左侧感觉运动/前运动区（PostCG/PreCG），口音额外招募双侧 IFG/MFG/SFG，性别主要停留在颞上听觉区。

## 结论
说话人身份加工非单一：共享听觉核心 + 特质特异扩展区（core-plus-extension）。口音认知负荷最高、额颞网络参与更多；性别依赖低层声学线索。提示未来说话人自适应模型可利用特质分层编码。

## 点评
用伪词弱化语义干扰、再用纯音基线剥离一般声学，设计上适于拆解身份维度；conjunction + ROI 幅度比较把“同一核心、不同负荷”说清楚。局限是合成伪词/固定口音对、任务判断本身引入决策网络，扩展区未必纯属“身份编码”。


# Neural Oscillatory Mechanisms of Speaker Normalization Under Cognitive Load: Evidence from Cantonese Tone Perception

- 论文编号：1940
- 报告人：Kaile Zhang
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ba_interspeech.pdf

## 问题
粤语声调依赖外在说话人归一化（上下文 F0），主动控制假说认为归一化耗认知资源；但双任务下行为常仍稳健，说明大脑可能用振荡机制补偿。何种节律在视觉认知负荷下支撑归一化尚不清楚。

## 方法
32 名粤语母语者（最终 EEG 分析 30 人）听“呢個字係”+ 目标 /ji33/（4 说话人×高/中/低 F0 上下文，Praat 移调 3 半音），判断 /ji55/、/ji33/ 或 /ji22/。次任务为视觉搜索：无负荷（NL）、4×4 低负荷（LL）、8×8 高负荷（HL）。64 通道 EEG，目标锁定 −500–800 ms；ERSP（1–50 Hz）相对基线，置换检验与簇置换比较负荷条件。

## 实验与结果
行为：对比性上下文效应显著，预期准确率随 Context F0 变化；负荷主效应与交互不显著——归一化行为不受视觉负荷影响。视觉任务 LL 准确率（0.91）显著高于 HL（0.7）。EEG：NL 早期 alpha 抑制（约 0–415 ms，前额+顶枕）；负荷条件转为顶枕 alpha 激活（LL 约 246–800 ms，HL 约 159–800 ms），HL 在 428–707 ms 强于 LL；HL 独有前额 delta 抑制（303–565 ms）。未见显著 beta。LL 条件下 alpha 功率与次任务准确率负相关（r=−0.38）。全文讨论后半略有截断。

## 结论
行为稳健不代表自动：负荷下通过顶枕 alpha 抑制视觉干扰、高负荷下前额 delta 把注意拨向外部听觉，支持主动控制假说。Beta 未参与上下文维持（至少在头皮 EEG 上）。

## 点评
用行为恒常 vs 振荡重配的对照，直接回应“双任务下归一化仍成功”的悖论；alpha/delta 拓扑与次任务相关使“抑制分心、改向注意”解释可检验。抽取文本末尾截断，且无负荷对比只靠视觉网格，泛化到听觉负荷需另证。


# Beta Rebound as a Neural Signature for Speech Movement: Preliminary Evidence Using Magnetoencephalography

- 论文编号：2995
- 报告人：Keerthana Stanley
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanley26_interspeech.pdf

## 问题
运动后 beta 回弹（PMBR，约 13–30 Hz）在肢体任务中研究充分，可反映力度、时长与复杂度，并被讨论为 ALS 等生物标志；自然言语产出中 PMBR 是否稳健、是否随发音复杂度调制尚不清楚。

## 方法
5 名健康英语右利成人。刺激为 AAC 常用五句，按 WCM、音节数、平均时长排序复杂度（最高 “Do you understand me?”，最低 “Goodbye.”）。延迟出声朗读：基线→静读 1 s→想象→出声；每句 100 次。Elekta Triux MEG（306 通道）+ 下颌气压传感器标定运动终点；SAM beamformer 定位口腔运动皮层 beta，相对基线 −3 至 −2.5 s；ROI 约运动后 0.25–1.25 s、15–30 Hz。

## 实验与结果
五句均在下颌运动结束后出现清晰 PMBR。高复杂度两句平均的 TFR 调制强于低复杂度两句。表面定位显示双侧运动区（BA4/BA6）PMBR，左侧（语言优势）更强、更早、更久。未报告正式推断统计。

## 结论
作者认为 PMBR 可作为自然言语发音的可测皮层特征，并初步提示发音复杂度与优势半球偏侧调制；样本小、基线可能受残留 beta 污染，结论需谨慎。未来拟扩大样本并纳入 ALS/帕金森等临床群体。

## 点评
把肢体运动文献中的 PMBR 迁到真实词句与 AAC 刺激，并用下颌偏移对齐，抓住“言语运动复杂度能否写进 beta 回弹”这一具体问题。n=5、无统计检验、基线窗口短，是典型试点证据，临床生物标志主张尚早。


# Effects of listener language experience, masker language, and cognitive load on word monitoring accuracy and response time

- 论文编号：2950
- 报告人：Jessica Chin
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chin26_interspeech.pdf

## 问题
言语–言语掩蔽中，目标与掩蔽语相似度（语言相似假说）与听者对掩蔽语熟悉度都会损害识别；认知负荷是否进一步恶化尚待厘清。匹配语言效应到底来自类型学相似还是熟悉度，证据混杂。

## 方法
澳英单语（分析 n=78）与阿–英双语（n=27）做英语词监测 + 数字预负荷双任务。目标为高频双音节英语词序列（SNR −5 dB），掩蔽为英/瑞典语/阿拉伯语/西班牙语双说话人 babble；预负荷记 1 或 3 个两位数（低/高负荷）。贝叶斯多层模型比较 d′ 与命中 RT；预负荷用 Levenshtein 距离验证负荷操纵。

## 实验与结果
高负荷显著降低数字回忆，但不影响词监测。单语：西班牙语掩蔽 d′ 高于英语与瑞典语；RT 在瑞典语、阿拉伯语快于英语。双语：西班牙语 d′ 高于英语；RT 在瑞典/阿/西均快于英语；整体 RT 慢于单语，但准确率相当；阿拉伯语掩蔽未额外损害双语者。类型学梯度（瑞典≈英、西/阿更远）证据不足。全文讨论末句抽取截断。

## 结论
同语掩蔽最难；类型学相似度与熟悉度（阿语掩蔽对双语者）未按预测系统损害监测；认知负荷未传到主任务，可能因被试放弃记数字。词监测难度低于句子识别，可能削弱熟悉度效应。

## 点评
用同语 vs 类型学相近 vs 熟悉掩蔽的三向对照，直接拆语言相似假说与熟悉度混淆；贝叶斯单侧假设与 d′ 设计清晰。任务偏简单、远程自助耳机、负荷条件试次数不均，可能削弱效应，解释上需克制。


# Not all language switching is equal: Language brokering and code-switching are associated with working memory and inhibitory control in young adults

- 论文编号：3404
- 报告人：Sarah M. Wright
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wright26_interspeech.pdf

## 问题
双语优势证据在年轻人中不稳定；把语码转换当作单一频率指标可能掩盖不同交际功能（词汇检索、身份表达、语言掮客/口译）对执行功能（EF）的差异需求。

## 方法
大学生样本；完整 EF 任务者 N=375，语码转换分析（至少 Rarely）中有协变量完整个案 N=176。九项任务经 CFA 建 shifting/updating/inhibition 三个相关潜变量（拟合可接受）。总体转换频率与语言掮客频率为 7 点自评；ACSES 14 项动机做 polychoric EFA，得身份、语用、词汇、享受四因子。回归控制年龄、优势度、口语水平、SES。

## 实验与结果
总体转换频率与三域 EF 均无显著关联（ps>.30）。词汇动机与 updating、inhibition 正相关（ps=.007；综合模型仍 ≤.004）。掮客频率与 updating（p<.001）、inhibition（p=.007）负相关。身份/享受/语用动机及 shifting 无可靠关联。综合模型 R² 约 0.068–0.174。全文结论段抽取截断。

## 结论
作者认为 EF 关联取决于交际功能而非转换次数：词汇驱动转换与更新/抑制正相关，语言掮客则负相关；日常会话转换本身无线性“练脑”效应，符合 Adaptive Control 等情境依赖框架。

## 点评
把“转换频率”拆成动机因子与掮客角色，并用潜变量降低任务杂质，正中双语优势测量问题。截面自评与单题掮客指标无法因果推断，负相关也可能反映负担/选择偏差而非“转换伤 EF”。


# Profiling Speech Rate Abilities of Visually Impaired Screen Reader Users by Bayesian Item Response Theory

- 论文编号：3096
- 报告人：Takahiro Miura
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miura26_interspeech.pdf

## 问题
读屏 TTS 语速配置缺乏证据：简单正确率把题目难度与个人能力混为一谈，且日语研究不足；传统 IRT 需大样本，视障小样本难用。

## 方法
11 名日语视障读屏用户（全盲 6、低视力 5）。ITA 语料 42 句×5 语速（150–500 WPM）用 macOS Kyoko 合成；复述算 mora 正确率，另评可懂度/可听性 Likert。贝叶斯累积 probit（等级反应）与 beta 回归分离题目难度与个人能力；弱信息先验，brms HMC。并回归盲视状态与相对听速经验。

## 实验与结果
模型收敛（最大 R̂=1.004）。能力个体差大（可懂度 SD 0.91，可听性 1.10）。相对 150 WPM，≥300 WPM 可懂度显著下降（β≈−1.23 至 −2.00）；中长句反而更易。全盲能力高于低视力；盲视状态与听速经验独立预测理解，但听速经验对可听性为负。全文局限讨论有截断。

## 结论
贝叶斯 IRT 可在 N=11 下为 TTS 语速评测分离难度与能力；约 250–300 WPM 为该经验群体门槛，个性化需同时考虑盲视类型与习惯语速。证明概念，需更大样本。

## 点评
把无障碍读屏评测从“平均正确率”推进到可解释的人–题潜变量尺度，适合小样本特殊人群。弱先验与宽可信区间是诚实代价；有效响应仅 2310/6930、经验用户偏多，外推新手与默认语速设计需谨慎。


# fMRI Decoding of Speech Conditions Across Brain Regions of Interest for Neural Evaluation of Speech Enhancement

- 论文编号：1947
- 报告人：Ching-Chih Sung
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sung26_interspeech.pdf

## 问题
噪声下 Clean vs Noisy 的 fMRI 多体素模式高维且跨被试变异大；深度解码是否优于 SVM，以及如何把解码输出变成可比较增强系统的神经指标，尚不清楚。

## 方法
NeuroPAS-Net 三阶段：掩码重构 SSL → 重放增量学习 → 目标被试监督微调，同一 CNN 编码器迁移。25 名听力正常普通话听者听 Clean、Noisy（SSN −3 dB）、DNN-SE（SEMamba）、Classic-SE（MMSE）四条件句子，12 个言语相关 ROI（AAL）。在 R PreCG Clean–Noisy 解码器上取 sigmoid 输出作 NeuroPAS，增强试次仅推理。

## 实验与结果
各 ROI 均高于 50% 机会；NeuroPAS-Net 全面优于 SVM/CNN，R PreCG 峰值 79.3%。消融显示 P1+P2+P3 单调提升（R PreCG 77.46→79.30）。归一化 NeuroPAS：DNN-SE 0.60 > Classic-SE 0.41。与主观可懂度 Spearman ρ=0.43（校正后 p≈0.17）。

## 结论
框架可稳健解码声学清晰度，并给出与主观相关的连续神经增强分数；DNN-SE 比经典增强更接近 Clean 神经模式。未来拟扩展到听力损失与 EEG/MEG。

## 点评
把 SE 评测从听感分数接到“是否更像 Clean 的多体素模式”，思路直接；三阶段迁移针对跨被试难题。NeuroPAS–可懂度相关未达严格显著、ROI 解码不等于因果，且仅正常听力，神经指标宜作行为评测的补充而非替代。


# SAGE: Switch-Aware EEG-Guided Soft Gating for Target Speaker Extraction with In-Trial Switching

- 论文编号：864
- 报告人：Xuefei Wang
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26p_interspeech.pdf

## 问题
EEG 引导目标说话人提取多假设注意在试次内固定；自发切换时 EEG 噪声与神经延迟会造成硬切换断续与错误说话人泄漏。

## 方法
SAGE：Conv-TasNet 式前端分离出两路候选；EEG 模块预测注意偏置 α(t) 与切换概率 p_sw(t)，温度 τ(t)=τ0+λ p_sw 软门控并局部平滑得 g(t)，输出 g·s1+(1−g)·s2。可微分局部时移补偿延迟；dropout 方差估计不确定性并加权平滑正则。损失 −SI-SDR + 切换感知 TV + 不确定性平滑；三阶段训分离器再联合微调。

## 实验与结果
自建 18 人普通话自发注意切换数据（64 导 EEG，±90° 男女混合）。SAGE：SI-SDR 8.67 dB、STOI 88.24%、平均切换延迟 2.04 s，优于 BASEN/NeuroHeed/NeuroSpex+/M3ANet。消融去掉软门控、延迟对齐或不确定性策略均降 SI-SDR/STOI/ACC；去掉对齐延迟升至约 2.58 s。

## 结论
把试次内切换当作动态软选择，并显式处理延迟与不可靠 EEG，可同时提升提取质量与切换时延。未来关注跨被试与更复杂声学。

## 点评
相对“先 AAD 再硬选音轨”，SAGE 在波形融合层做切换感知平滑，对准听感断续这一痛点。自建数据与按钮标注延迟、双说话人设定，跨被试泛化与多说话人仍待验证。

