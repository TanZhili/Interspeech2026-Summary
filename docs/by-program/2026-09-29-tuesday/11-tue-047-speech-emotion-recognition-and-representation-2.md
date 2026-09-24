# Speech Emotion Recognition and Representation 2

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：3
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本海报场覆盖 SER / MER / MERC / CER 的表征与学习策略：高效注意力权衡、多标签基准与 Mamba 融合、混合增强与多损失、图注意力时序聚合、低资源语种轻量双流、对话情感惯性、模态特异标签分布、标注不确定性课程、连续情感时延补偿，以及性别公平迁移与冲突感知伪标签。瓶颈集中在标注歧义、类不平衡、长序列算力、跨模态不一致，以及说话人/评分者偏见与伪标签噪声。

相对“更大预训练编码器”，多篇强调结构与监督形式：分布标签 vs 硬标签、优势加权排序式思想在相关健康场已见、此处则用熵感知分析与对比学习；多任务细粒度对齐可从声学自举伪标签而少依赖转写。公平性工作明确双端（说话人侧与评分者侧）中立，并在属性部分观测下做任务向量式迁移。

效率与容量并存：标准自注意力识别最强但昂贵，RetNet 等高效变体换时延与显存；1.1M 参数双流在孟加拉语说话人无关评测上挑战更大预训练模型——摘要强调先前工作常缺 SI 评测。

## 论文技术总结

# How Attention Shapes Emotion: A Comparative Study of Attention Mechanisms for Speech Emotion Recognition

- 论文编号：1907
- 报告人：Federico Costa
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/casalssalvador26_interspeech.pdf

## 问题
SER 中自注意力能抓长程依赖，但 softmax 注意力相对序列长度二次复杂度，长语音代价高；高效注意力（RetNet、LightNet、GSA、FoX、KDA）在 SER 上缺少统一准确率–效率对标。

## 方法
固定架构：冻结 SSL 语音特征（WavLM / Wav2Vec2 / HuBERT / Wav2Vec2XLSR）与 BERT-large 文本特征，拼接后经可替换 seq2seq 模块，再 attention pooling + 分类头；八类情绪。仅训 seq2seq/池化/分类器（约 20M 可训、总参约 655M）。在 MSP-Podcast v1.0 Dev 与 v2.0 Test1/Test2 上比 Macro F-score；效率只测 seq2seq 的推理延迟与峰值 GPU 显存随序列长度变化。

## 实验与结果
Dev 上 LightNet 均值最高（36.62%），略超 SA（36.39%）；Test1/Test2 上 SA 最稳且最好（均值 36.42% / 27.19%），FoX 次之；GSA 在 T2 最弱（21.73%）。效率：SA 在 400s 延迟 48.59 ms、显存 12.35 GB；KDA 延迟 5.96 ms（约 8.15×）；FoX 显存 0.328 GB（约 37.6× 少于 SA）。全体在 T2 相对 T1 明显掉点。

## 结论
峰值准确率仍偏向标准自注意力（尤其短输入），高效变体提供近线性扩展；T1→T2 掉点显示真实分布与类别不平衡仍是瓶颈。

## 点评
工作把 SER 评测从刷分扩到延迟/显存，设计干净（只换融合层）。强处是多 backbone 与长度扫描；脆弱处是特征提取器冻结且效率只测子模块，端到端系统中 SSL 成本可能淹没 seq2seq 差异，且 T2 弱表现提示架构换注意力 alone 不够鲁棒。


# From Single to Multi-Label SER: Dataset and Mamba-Based Fusion Model

- 论文编号：3458
- 报告人：Thi Thu Trang Nguyen
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tran26c_interspeech.pdf

## 问题
主流 SER 把众包投票压成单标签，抹掉共现与标注歧义；公开大规模多标签语音 SER 基准稀缺。Transformer/SSL 骨干对长音频又偏重。

## 方法
将 MSP-Podcast V2.0 转为多标签：丢弃评分 <3 或 OOS 比 ≥0.5 的样本；多数类必选，次要类需同时满足票数/相对比例/对多数比阈值，L_max=3；训练集上长尾组合剪枝。主基准 n_min=2_final：保留训练样本 ≥1000 的 18 种组合，并做 train-only 右移增强平衡。双分支 Mamba：MFCC（轻量 1D CNN 前缀）与 100 维 log-mel（patch+更深 Mamba）分别编码、masked mean pool，门控缩放后拼接瓶颈头，8 路 sigmoid；二元 focal loss。验证集全局阈值扫描选 checkpoint，测试固定 t=0.45。

## 实验与结果
Fusion-Gate（3.07M）Test1 miF1/maF1/HL/Jac 为 0.510/0.305/0.179/0.412；Test2 为 0.514/0.258/0.179/0.405，优于单模态 Mamba 与多数复现的韩语融合基线，并接近/超过部分 MulT、WavLM（94.3M）的集合指标。作者强调差异更多体现在 HL/Jaccard/ExactAcc；尾类 Fear/Disgust/Contempt 仍很难。抽取后部讨论略有延续但主表已完整。

## 结论
提供可复现的 MSP-Podcast 多标签构建协议与轻量 Mamba 融合基线，在统一协议下 micro-F1 约 0.50；长尾与稀有情绪仍是限制。代码与划分将公开。

## 点评
贡献重心在标签协议（确定性 multi-hot + 防泄漏剪枝）而非刷大模型。Mamba 线性时序适合长 podcast；脆弱处是固定阈值对尾类不友好、组合空间被压到 18 种牺牲了真实歧义覆盖，以及与 SSL 大模型比参数仍非最轻但准确–效率折中明确。


# Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention

- 论文编号：1219
- 报告人：Yizhong Geng
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26u_interspeech.pdf

## 问题
SER 受情绪复杂与标注稀缺制约；既有 mixup（如 LAM）均匀混合片段、忽略能量动态，可能漏掉与情绪相关的能量线索；简单池化也难突出多帧关键线索。

## 方法
Energy-Adaptive Mixup（EAM）：随机截取短于半长的片段，把干扰段按 SNR∈[−5,10] dB 缩放能量后叠加主段，用能量与时长比构造软标签 λ_mix。特征走预训练 WavLM→CNN/Transformer。Frame-Level Attention Module（FLAM）：多头自注意力后可学习向量加权池化得话语向量。Multi-loss：KL（对齐软标签）+ Focal + Center + 帧级 Context Broadcasting 后的 SupCon，加权求和。说话人/会话独立交叉验证。

## 实验与结果
IEMOCAP：WA/UA 78.47%/79.14%，超 LAM（75.37/76.04）及若干多模态方法。MSP-IMPROV：58.55%/58.34%。RAVDESS：93.40%/92.28%。SAVEE 说话人均 UA 72.3%。消融显示 EAM、FLAM 与各损失逐步抬升；t-SNE 显示 MLL 后类簇更清晰。

## 结论
能量感知混合、帧级注意力与多损失协同可显著提升跨自发/表演数据的 SER，并增强特征可分性。作者称在四个数据集上均超既有 SOTA。

## 点评
相对“只换骨干”，本文把数据增强物理化（SNR 能量）并与软标签、对比/中心损失对齐。强处是四数据集与细消融；脆弱处是超参与损失权重经验设定多、表演集（RAVDESS）高分可能夸大可迁移性，以及 WavLM 冻结/微调细节需读者自行注意域偏移。


# Segment-wise Embedding based Graph Attention Network for Effective Speech Emotion Recognition

- 论文编号：969
- 报告人：Haoyu Song
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26c_interspeech.pdf

## 问题
小规模情绪语料上直接微调大 PTM 易过拟合；话语级 one-hot 标签模糊（多情绪共现、短暂情绪片段），平均/最大池化易稀释；变长序列难做序列到单一标签映射。

## 方法
冻结 HuBERT-large（取第 19 块 1024 维帧特征），其上接 1D Swin-Transformer 段级适配器。后训练：师生 EMA 自蒸馏，联合话语级 KL 一致、块掩码预测（L_MP）与 KoLeo 均匀性正则。微调：把话语切成多段 SSE 作图节点，两层残差 GAT 动态聚合，读出话语向量；损失 CE + 监督对比（SCL）缓解标签歧义。

## 实验与结果
IEMOCAP 5-fold：WA/UA 76.22%/76.84%。MER2023：F1 71.53%，valence MSE 0.9844。作者称相对 SOTA 有显著提升。抽取文本在微调 SCL 公式处附近截断，完整对比表与消融细节部分不可见。

## 结论
段级嵌入图注意力可在变长话语上突出情绪显著段，后训练缓解分布偏移，SCL 提升对模糊标签鲁棒性。边界是依赖强 PTM 与两阶段流程成本。

## 点评
把 SER 当作“稀疏情绪事件检测”而非整句均值分类，用 GAT 替代池化是合理归纳偏置。强处是适配器后训练防过拟合；脆弱处是图全连接对短句可能过度、以及全文截断使相对基线的增益幅度难以逐项核对。


# Dual-Stream DNN-KAN Networks with Bangla-Specific Features for Speech Emotion Recognition

- 论文编号：3374
- 报告人：Kazi Reyazul Hasan
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hasan26_interspeech.pdf

## 问题
孟加拉语 SER 研究不足；多数既往结果为说话人相关（SD），可能只是记住说话人。大 SSL（emotion2vec、wav2vec2-xlsr）参数量大，且缺少针对孟加拉语韵律的归纳偏置。

## 方法
从 OpenSMILE 80 候选中用 η² 与 ANOVA 筛选 15 个高判别特征，三时间窗聚合得 51 维韵律描述子；与 80 维 MFCC 统计拼接为 131 维。双流：MFCC 走因子化 DNN；韵律走共享 B 样条基的轻量 KAN。双向交叉注意力 + 情绪自适应门控（高唤醒偏韵律、低唤醒偏频谱）后瓶颈融合分类。无数据增强；主评说话人独立（SI）：SUBESCO 16/4、BanglaSER 25/9 说话人划分。仅 1.1M 参数。

## 实验与结果
SUBESCO SI 92.12%（SD 95.35%），超 emotion2vec 89.42%、wav2vec2-xlsr 91.05%；BanglaSER SI 82.79%。同管道在 EmoDB 上重选特征达 93.92%。跨语直接测西方集掉点，韵律-only 掉更狠；消融显示加韵律与 KAN/门控逐步增益。McNemar p<0.01。

## 结论
统计特征筛选 + DNN-KAN 双流可在极少参数下达到或超过大 SSL 的孟加拉语 SI 表现；方法可迁移到其他语言重跑筛选，而非声称特征普适。

## 点评
工作同时打“语言适配”和“评测诚实（坚持 SI）”两张牌，用可解释特征工程对抗堆参数。强处是轻量与门控可解释性；脆弱处是表演/会话语料差距大（SUBESCO vs BanglaSER）、η² 阈值极严可能过拟合训练子集，以及无增强的保守设定未必是部署最优。


# EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in Conversation

- 论文编号：3532
- 报告人：Zilong Huang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26p_interspeech.pdf

## 问题
对话多模态情绪识别（MERC）多建模上下文依赖，却常忽略同一说话人情绪的“惯性”——情绪倾向平滑过渡而非剧烈跳变；忽略惯性会使情绪切换处的负样本构造不当，限制特征判别。

## 方法
提出可插拔的 Emotional Inertia-Informed Supervised Contrastive Learning（EII-SCL）。骨干先用模态编码器（RoBERTa/Wav2vec2/CLIP）+ Bi-GRU + Transformer 或 DialogueGCN 式融合得到话语嵌入，再加 CE。对比学习中：同说话人同情绪为正；同说话人异情绪且落在注意力估计的动态惯性窗口内为 hard-negative（动态权重 1−cos/2），窗外或异说话人为 easy-negative。总损失 L=L_CE+α L_eii。

## 实验与结果
IEMOCAP LOSO、MELD 官方划分。MM-TransFormer+EII-SCL：IEMOCAP Acc/w-F1 73.95/74.01，MELD 68.19/67.33；MM-DialogGCN+EII-SCL：IEMOCAP 73.13/73.15，MELD 67.83/66.97，整体超 FEMI、AdaIGN 等。硬负样本平均余弦相似显著高于易负样本（ω=1 时差约 0.3645）；动态窗口优于固定窗口；模糊情绪对误分下降。

## 结论
无需额外标注即可把情绪惯性写入对比目标，提升通用 MERC 骨干表现。边界是依赖说话人标签与局部窗口假设。

## 点评
把心理学“情绪惯性”落成 hard-negative 采样与动态排斥权重，比单纯情绪切换检测更贴近同说话人连续表达。强处是即插即用；脆弱处是窗口依赖注意力估计质量，且离散标签仍强制切分渐变情绪。


# Leveraging Modality-Specific Label Distributions for Enhanced Multimodal Emotion Recognition

- 论文编号：2076
- 报告人：Xiaohan Shi
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26e_interspeech.pdf

## 问题
多模态情绪识别（MER）多设计复杂融合，却常用统一多模态标签，忽略各模态自身标签分布；EmotionTalk 上仅 24.5% 样本三模态标签完全一致，跨模态情绪倾向差异被浪费。

## 方法
提出 MoLD：HuBERT/RoBERTa/DINOv2 提特征后经 Mamba 精炼；各模态经池化+FC 预测模态特异标签分布 E⋆_m；Cross-Modality Fusion 用两次交叉注意力聚合另两模态得 H^(fus)_m，再与 E⋆_m 拼接。三模态表征拼接后分类。损失：CE + 各模态 KL（分布学习）+ InfoNCE 模态相似损失，权重为可学 softmax。

## 实验与结果
EmotionTalk 七类。多模态 MoLD UAR/F1 58.96%/59.67%，超 Cross-Attention（56.05/57.25）与 MLP（54.08/53.66）。消融去 LD/MS/CMF 均掉点。单模态设定下语音/文本/视频亦优于 MLP。Oracle 分布上界约 66.56% UAR。

## 结论
显式建模模态特异标签分布并约束跨模态一致性，可同时提升单模与多模 MER。边界依赖提供模态级标签的语料。

## 点评
抓住“统一标签掩盖模态分歧”这一数据事实，把 LDL 从单模扩展到跨模交互。强处是分析与消融清晰；脆弱处是视频编码器冻结、中文语料特定，以及分布标签质量决定上限。


# Learning from Annotation Uncertainty: Entropy-Aware Curriculum for Speech Emotion Recognition

- 论文编号：2992
- 报告人：John Hansen
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/omidi26_interspeech.pdf

## 问题
SER 常把多标注者分歧压成硬共识标签；MSP-Podcast 等语料中歧义是结构化感知信息而非纯噪声。需在统一骨干下量化分布监督与熵课程相对硬标签的收益。

## 方法
WavLM-Base + 时序卷积 + 双层 GRU，共享 256 维嵌入，多任务预测 9 类情绪分布与 VAD（异方差 NLL+CCC）。监督：硬 pluralty、主票分布、合并主–次票（0.9P/0.1S 或 0.8P/0.2S）；分类用 CE/CBCE 或 KLD。归一化熵 Hn 作固定歧义属性，用于分层评测与过滤/加权课程（标准从低熵到高熵，反向相反）。渐进解冻 WavLM。

## 实验与结果
相对硬标签，分布目标显著降 JSD/KLD（如 M90 KLD Test1 JSD 0.189 vs Hard CE 0.322）。硬标签 Macro-F1 部分靠 Other 类；分布监督 Other-F1 很低，把不确定性摊到情绪类。M90–Filter Test1 Macro-F1 最高 34.8%；M90–Weight Test2 Macro-F1 31.8% 且 KLD 最低。高熵箱 Macro-F1 全面更差；反向课程不优于标准课程。

## 结论
应超越硬标签，用保留听众分歧的分布目标；熵课程可在决策 F1 与分布对齐间权衡。高歧义话语仍难。

## 点评
控制实验设计干净：同架构只换监督与课程，避免与标签精炼方法纠缠。强处是揭示“刷 Macro-F1 靠 Other”的假象；脆弱处是标注者少时熵代理不完美，且分布监督与硬决策指标不完全同向。


# Revisiting Delay Compensation via Feature-Level Temporal Accumulation in Continuous Emotion Recognition

- 论文编号：3030
- 报告人：Jian Xiang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiang26b_interspeech.pdf

## 问题
连续情绪识别（CER）标注常滞后于信号；主流做法是对标签做固定时移的 shift-based delay compensation（SDC），需截断边界且对延迟参数敏感。作者认为标注更像在时间窗上累积证据，而非瞬时判断的延迟报告。

## 方法
提出 accumulated delay compensation（ADC）：对冻结 wav2vec2.0 特征各维做因果滑动均值滤波，群延迟 τ=(N−1)/2，不改输入–标签对齐。后端用 Constrained Neural ODE。RECOLA 官方划分；CCC 评测。对比实践级 RA-SDC（训练/评测截断对齐）与公平设定（同扩展序列上 ADC 均值滤波 vs 纯延迟）。

## 实验与结果
实践级：唤醒 ADC 峰值 CCC 0.816（τ=2s）vs RA-SDC 0.808（1.5s）；效价 ADC 0.485（τ=6s，一 seed 无效）或有效最佳 0.484（4.5s）vs RA-SDC 0.473（3s）；均超无补偿基线（0.746/0.385）。唤醒偏好较短积分窗，效价偏好较长窗；ADC 对延迟参数更稳健。

## 结论
特征级时间累积可同时平滑与内生延迟补偿，是比标准时移更优的 CER 延迟处理方式，且维度依赖窗口长度。

## 点评
把延迟补偿从“挪标签”改成“积特征”，物理上对应标注者累积证据，并自然低通。强处是公平对比与唤醒/效价差异分析；脆弱处是仅 RECOLA、短块拼接与常数填充边界，以及效价不稳定 seed。


# Two-Sided Fairness Transfer for Gender-Neutral Speech Emotion Recognition with Partially Observed Attributes

- 论文编号：3201
- 报告人：Woan-Shiuan Chien
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chien26c_interspeech.pdf

## 问题
公平 SER 需同时中立说话人侧与标注者侧性别偏见，但多数去偏依赖双侧属性标签；跨数据集时常只有一侧有性别标注，无法直接训练双侧公平模型。

## 方法
两阶段：Stage1 在 CLAP 上对抗去偏（L_FairCLAP=L_CE+L_Adv）分别得到说话人侧/标注者侧 FairCLAP。Stage2 在源域由参数差构造 ATT2Fair 任务向量 τ=θ_RAT^S−θ_SPK^S，按 θ_RAT^T=λτ+θ_SPK^T（可对称）推断目标域缺失侧公平模型。数据：IEMOCAP、MSP-Podcast v1.11、BIIC-Podcast；四类情绪；S1 全说话人集、S2 标注者性别偏置集；指标加权 F1 与统计均等 ∆SP。

## 实验与结果
正文报告 FairCLAP 与 ATT2Fair 跨数据集可保持识别并改善公平；抽取文本在结果讨论前段截断，具体 F1/∆SP 数字表未见完整。

## 结论
任务算术可在部分属性监督下跨数据集迁移双侧性别中立，无需目标域缺失侧标签。边界依赖源域双侧可用与 λ 调参。

## 点评
把“说话人公平 ↔ 标注者公平”写成参数空间向量差，是对缺失属性部署的务实招数。强处是设定贴近真实标注缺口；脆弱处是任务向量线性假设与域移可能不对齐，且全文截断使定量收益难核验。


# Conflict-Aware Pseudo-Labeling via Acoustic Signals for Multi-Task Speech Emotion Recognition

- 论文编号：2118
- 报告人：Shunfei Liang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26f_interspeech.pdf

## 问题
话语级 SER 标签抹掉帧内情绪动态；用 ASR 转写做细粒度对齐成本高。朴素伪标签在模糊帧上噪声大。

## 方法
冲突感知伪标签：训练数据分 K 折训 K 个冻结 emotion2vec 子模型；去掉池化后对帧做协同推断。多数票（>K/2）帧赋硬伪标签（共识区）；无共识帧用话语级真值回填（冲突区）。下游共享 HuBERT 编码器，话语分支 attention pooling + CE，帧分支对共识/回填分别 CE，L_total=L_utt+λ(L_cons+α L_rect)。推理丢弃帧头。

## 实验与结果
IEMOCAP（4 类 LOSO）、EmoDB（7 类）、MELD 官方划分。作者称三集均达 SOTA 且无需辅助文本；抽取文本在实现细节处截断，完整 WA/UA 对比表未见。

## 结论
仅用声学协同共识与全局回填即可构造帧级辅监督，提升表示而不增加推理开销。边界是伪标签仍依赖话语级真值先验与子模型多样性。

## 点评
用“多视角共识 vs 冲突回填”处理伪标签噪声，比单纯稠密伪标更稳，并避开 ASR 依赖。强处是训练期多粒度、推理零附加；脆弱处是 emotion2vec→HuBERT 骨干切换与 K 折成本，以及截断导致 SOTA 数字不可核对。

