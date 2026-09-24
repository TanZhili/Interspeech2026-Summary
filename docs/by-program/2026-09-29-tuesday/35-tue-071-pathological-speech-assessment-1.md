# Pathological Speech Assessment 1

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：13
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从心衰、呼吸音、感冒到抑郁与帕金森构音障碍、痴呆预测，共同主题是：生理/病理状态如何改变语音或呼吸声学，以及模型是否学到疾病线索还是说话人身份等捷径。

自监督对比时间邻近、无缓冲持续学习、听诊部位特异相关，以及感冒语料上的说话人嵌入位移，强调生态有效数据与跨中心/跨域泛化。抑郁检测则同时出现免训练辩证推理引擎与严格说话人独立评测的警示。

跨语帕金森构音障碍检测用表征级语言平移削弱语言身份；多语痴呆预测评估基础模型零样本能力。趋势是：数字生物标志物必须经受说话人泄漏、域偏移与跨语混淆的压力测试。

## 论文技术总结

# Contrastive Time-Proximity Pre-Training for Speech-Based Heart Failure Monitoring

- 论文编号：424
- 报告人：Nicholas Cummins
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fiedler26_interspeech.pdf

## 问题
心衰（HF）急性失代偿（ADHF）需尽早发现；液体潴留可改变声道，但既往声学生物标志多依赖持续元音与患者主动配合，难以用于日常自然语音监测。手工声学特征对内容、时间与录音条件敏感，且缺乏直接刻画 HF 状态的特征。

## 方法
提出对比时间邻近（CTP）自监督预训练：在同一患者纵向录音上，≤3 天对拉近嵌入、≥100 天对推远（余弦 embedding loss，margin=0）。骨干改编 d-vector：mel 谱切 160 帧段，双向 LSTM + 帧注意力得段嵌入，再经段注意力聚成 256 维录音表示（约 4.5M 参数）。评估三档输入：A(16 kHz, 40 mel，可从说话人验证 checkpoint 初始化)、B/C 更高采样率与 mel 维。下游将入院（wet）相对出院（dry）作排序任务，用冻结特征的 XGBoost Ranker 或联合微调的 Neural Ranker；Level 1 为 Charité 留一患者交叉验证，Level 2 将 Level 1 集成测 Mayo。预训练数据为 Noah Labs 远程监测约 5.2 万条德语自然语音（392 人）；临床评估为 VAMP-HF 两中心共 68 名 ADHF 患者。

## 实验与结果
CTP 预训练上近端相似度明显高于远端。Level 1：经典 29 维声学特征 XGBoost 准确率最高 0.62，CTP-A 约 0.58–0.61，人类标注约 0.55。Level 2 跨中心跨语言：经典特征跌至 0.34，CTP-A 仍约 0.59–0.61；无 CTP 的 d-vector 接近随机。Level 2 差异因样本量小未达统计显著。注意力峰值常落在呼吸相关停顿，与人类“呼吸”线索一致。

## 结论
CTP 能从弱标注纵向自然语音学到对 ADHF 有预测力的表示，并较经典特征更利于跨中心泛化；注意力指向呼吸段，提示生理相关性。局限：N=68、探索性比较、无连续失代偿度量、代码未公开。

## 点评
用疾病渐进性把时间邻近变成对比监督，避开对临床终点的强依赖，抓的是“同人纵向状态变化”而非说话人不变性。强在跨语言诊所仍稳住、且段注意力可解释；弱在临床队列小、阈值未系统扫、预训练目标与下游最优配置不一致（B/C 预训练更好但下游更差）。


# Lung-CL: Spectrum-aware Distillation and Generative Replay for Continual Learning based buffer-free Respiratory Sound Classification

- 论文编号：1199
- 报告人：Qinben Lai
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lai26_interspeech.pdf

## 问题
跨医院、设备与人群部署呼吸音分类时，域增量学习易灾难遗忘；存真实样本的 replay 触碰隐私（GDPR/HIPAA），而通用 buffer-free 蒸馏又忽略呼吸音时频稀疏、病理线索集中在高能量窄带的特点，易把设备噪声当不变特征。

## 方法
Lung-CL：Teacher–Student、固定容量。AST 前 6 层冻结为特征提取器 G、后 6 层+分类头为可训 H。Class-Specific Latent Replay（CSLR）：每域结束后用对角 CS-GMM（BIC 选分量数，Kmax=10）拟合各类潜特征，新域训练时采样伪特征注入 H，无需缓存音频。Multi-Level Spectrum-Aware Distillation（MLSAD）：Energy-Gated Distillation 按谱能量加权中间特征差、全局余弦对齐语义方向、KL 蒸馏 soft logits。联合优化分类、LEGD、LCosine、LKD。输入 16 kHz、8 s mel（50–2000 Hz）；三数据集映射统一四类 Normal/Crackle/Wheeze/Both。

## 实验与结果
ICBHI→SPRSound→HF 等三条序列（S1–S3）。相对 buffer-free 基线（EWC/SI/LwF），Lung-CL 在 S1/S3 取得最佳或接近最佳 ACC（约 61.81%）与最强 BWT（S1 −4.0%，S3 −5.05%）；S2 严苛域移下 BWT −9.6%，仍优于 EWC/SI。消融：CSLR 将 BWT 从 −14.11% 提到 −8.20%；再加 LEGD 至 −4.0%。t-SNE 显示生成伪样本能复现原域流形。

## 结论
在无真实缓冲下，CS-GMM 潜空间重放加能量门控谱蒸馏可缓解呼吸音域增量遗忘，并兼顾隐私与稳定性–可塑性权衡。

## 点评
问题切在“医疗音频不能存样本 + 病理在高能量带”，CSLR 与 EGD 分别对准隐私与谱稀疏。强在 buffer-free 仍可比部分有缓冲方法；弱在依赖冻结底层假设分布不漂、三类映射与序列设计可能影响可复现泛化，且 HF 类重叠严重时伪样本质量仍需依赖可视化佐证。


# An auscultation location specific study on the relationship between expiratory-to-inspiratory acoustic patterns and spirometric airflow limitation across age and gender in asthmatic patients

- 论文编号：2602
- 报告人：Dheeraj Harish Kumar
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26g_interspeech.pdf

## 问题
哮喘气流受限以呼气为主，临床靠努力依赖的 FEV1/FVC；既往 E/I 谱功率比与肺功能相关，但听诊部位、年龄与性别如何调制该相关仍欠系统研究。

## 方法
141 名确诊哮喘（20–60 岁，66 男 75 女；FEV1/FVC 51%–99%）。Littmann CORE、4 kHz，四后壁部位（LL/LU/RU/RL）各 5 个呼吸周期，专家标注吸呼段。STFT（Hanning N=2048, H=512）算带限谱功率，E/I = P(E)_B / P(I)_B，频带 0–800、100–200、200–400、400–800 Hz；部位级取五次中位数。Spearman 相关检验 E/I 与 FEV1/FVC，分年龄组与性别；α=0.05。

## 实验与结果
100–200 Hz 与 200–400 Hz 相关更强且常显著，400–800 与宽带 0–800 较弱。全体上左下（LL）在多带更强。年龄：年轻组（如 20–30）下部尤其 LL 更强；50–60 组左上（LU）各带最高且部分显著。性别：男性 LL、女性 LU 跨带更强且显著。作者报告相关多为中等（约 r=0.2–0.4），宜作探索性证据。

## 结论
E/I 与 FEV1/FVC 的关联具部位、频带、年龄与性别依赖；中低频与下后壁总体更敏感，但不同人口子群最优听诊位不同，不能直接替代肺量计。

## 点评
把“呼气受限—声学 E/I—肺功能”对齐到部位与人口学分层，设计清晰、统计直白。强在与老化弹性回缩/关闭容积等生理叙事一致；弱在组间未做正式比较、相关中等、单中心且 RU 有一例缺失，离临床替代仍远。


# Common Cold Corpus: Health-aware robustness study of modern speaker embeddings under physiological domain shift

- 论文编号：1188
- 报告人：Anabell Hacker
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hacker26_interspeech.pdf

## 问题
中度上呼吸道感染（URTI）会改变发音器官，但现代说话人嵌入在生态有效录音下对短期生理域移的稳定性仍不清楚；既往冷语音语料多为高症状、实验室条件，不利于同人健康–患病对照。

## 方法
发布 Common Cold Corpus：85 名德语者经个人设备远程采集，患病（WURSS 均值约 3.25/7）与健康各一场（≥7 天间隔），朗读 NWS 与 Butter Story，共约 431 分钟。声学：openSMILE eGeMAPS（90 参量），配对 t/Wilcoxon + BH 校正。嵌入：ECAPA-TDNN、TitaNet、ECAPA2、ReDimNet，16 kHz、截断至 15 s，文本受控闭集验证（genuine 188、imposter 15792），报告 EER/AUC、条件内距离、Zshift、身份 crossover margin。

## 实验与结果
声学：NWS 上 F0 80 百分位与 HNR 在 BH 后仍显著下降；多数特征仅名义显著；TBS 趋势同向但校正后不显著。验证：患病–健康仍高可分（TitaNet EER 1.51%，AUC 0.9893 等），相对健康–健康跨文本基线 EER 约升 1–2 个百分点。条件内距离 ill 更大；Zshift 模型依赖（TitaNet 8.826，ECAPA2 1.177）。ECAPA-TDNN 约 6.38% 样本身份 margin>0；位移方向有显著全局对齐。

## 结论
中度感冒在真实场景下即可引起说话人嵌入可测、部分有向的位移，而多数经典声学标记校正后消失；身份大体可保，但对生物特征与数字生物标志应用有双重含义。语料仍在扩大。

## 点评
用同人配对 + 生态录音把“生理域移”从通道失配里拆出来，并同时看声学显著性与嵌入几何。强在多架构对照与 Zshift/crossover 指标；弱在设备/环境等混杂难彻底排除、样本相对 ComParE 仍小，位移是否特异于感冒需更大规模与症状分层验证。


# Moot-Court: Training-Free Dialectical Reasoning for Depression Detection

- 论文编号：3099
- 报告人：Yuqing Sun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26i_interspeech.pdf

## 问题
自动抑郁检测需要可解释、可扩展方案；向 LLM 注入语音多依赖微调/P-tuning，临床小数据易过拟合且“模型锁定”。纯文本 LLM 又丢掉声学生物标志。

## 方法
Moot-Court：冻结 LLM 的训练免费辩证推理。先将声学指标（latency、语速、F0、能量、jitter、shimmer 等）文本化，建多层蓝图 VL/VS/VP，并按精神病理网络抽出 Vext/Vint/Vevid 事实节点。Prosecutor 建致病图 GP、Defense 建情境图 GD（指示、强化、矛盾、排除等边类型）。k=5 法官多样温度裁决，Reflector 据对错场景写入正规则/负陷阱 Codex；奖励 S=α×β×W+δnew 驱动检索与 MODIFY/MERGE/ADD。骨干如 DeepSeek V3.2、Qwen3；音频描述用 Qwen-Audio。数据 DAIC-WOZ 官方划分，ZipEnhancer 降噪。

## 实验与结果
DeepSeek V3.2：F1 0.8856，Recall 0.9394，Precision 0.8378，优于多项全训/微调/指令微调基线（如 DepressInstruct F1 0.8235）。跨骨干仍高召回（≥0.9394）；Qwen3-30b F1 0.8234。消融：纯直接推理 F1 0.6296；加辩证无 Codex 0.7020；全框架 0.8856。文本+音频相对纯文本 F1 0.7890→0.8856。

## 结论
在不更新权重下，将多模态抑郁判定组织为对抗图辩论 + 自演化 Codex，可在 DAIC-WOZ 上超过微调模型并提升可追溯性。

## 点评
把 GRPO 式“经验蒸馏”搬到临床辩证结构，避开小样本微调过拟合，问题意识清楚。强在模块消融显示 Codex 能同时拉回召回与精度；弱在依赖强闭源 LLM API、声学仅符号化入 prompt，以及对 DAIC-WOZ 官方划分的外部泛化未测。


# Who is Speaking or Who is Depressed? A Controlled Study of Speaker Leakage in Speech-Based Depression Detection

- 论文编号：1394
- 报告人：Hsiang-Chen Yeh
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yeh26_interspeech.pdf

## 问题
语音抑郁检测在 DAIC-WOZ 等基准上常报极高准确率，但未见患者时近随机；疑因说话人泄漏使模型走身份捷径而非抑郁声学标志。需在训练规模固定下系统量化重叠说话人效应。

## 方法
DAIC-WOZ 189 人、PHQ-8≥10 为抑郁，切出 6545 段。规模匹配划分：控制组 151 人 / 目标组 38 人；测试固定为目标组一半片段，训练 A 无说话人重叠（5117 段）、训练 B 同等规模但含目标组另一半（重叠）。三族模型：Wav2Vec-Linear Probing、XLSR-eGeMAPS 拼接、Wav2Vec-SLS；编码器冻结/微调，并加 DANN（说话人作域）对抗。报告抑郁 Macro F1、准确率与说话人识别准确率。

## 实验与结果
重叠设定下微调 Wav2Vec 可至准确率 97.65%（SLS 约 98%），说话人识别常 >90%；严格独立时跌至约 58.74% 等，DANN 仅有限回升（如 62.36%）。XLSR-eGeMAPS 说话人识别近随机（约 6–10%），抑郁准确率中等（约 54–67%），重叠–独立差距较小。高抑郁性能总伴随强身份可分性。

## 结论
当前语音表示中抑郁信号与说话人身份高度纠缠；重叠划分会高估泛化与临床效用，应强制说话人独立评估。

## 点评
用“等规模、只动是否重叠”的对照把泄漏从模型复杂度里剥离，证据链清晰。强在跨架构一致、并同时报 Spk ID Acc；弱在 DANN 未能真正抹平差距，说明简单对抗不够，且结论主要锚定 DAIC-WOZ 一种切段协议。


# Adapting Self-Supervised Speech Representations for Cross-Lingual Dysarthria Detection in Parkinson’s Disease

- 论文编号：773
- 报告人：Abner Hernandez
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hernandez26_interspeech.pdf

## 问题
帕金森构音障碍数据稀缺，跨语检测重要；自监督语音表示仍编码语言结构，即使固定 /pa-ta-ka/ DDK 任务也会与病理线索混淆。需在不重训 S3M、且尽量只用目标语健康对照的前提下做表示级对齐。

## 方法
语言平移（LS）：˜x = x_src − μ_src + μ_tgt，质心仅由各语健康对照（HC）在交叉验证折内估计。提取 HuBERT-Large、WavLM-Large、XLS-R-300M 说话人级向量；逻辑回归分类 PD vs HC，嵌套 CV 选阈使灵敏度≥0.9。数据：捷克、德语、西班牙语（PC-GITA）PD/HC 队列。设定：(1) 跨语——训练含源语 PD+HC 与目标语 HC，无目标语 PD；(2) 多语——含目标语 PD。

## 实验与结果
跨语无 LS：极高特异、低灵敏（如 HuBERT CZ Spec 0.98 / Sens 0.35）。加 LS 后灵敏与 F1 大幅上升（HuBERT F1：CZ 0.74、DE 0.61、ES 0.74）。多语设定下差距缩小，LS 常提高特异而灵敏大致持平。UMAP 显示源语 PD 点移向目标质心；HC 上语言 SVM 探针准确率由约 96% 降至近随机（约 29–34%）。德语与捷克/西语质心距离更大，跨语增益相对较小。

## 结论
DDK 上的 S3M 仍含强语言身份；HC 质心平移可削弱该结构并显著改善无目标语 PD 时的跨语检测，多语有目标语 PD 时收益更温和。

## 点评
把跨语失配压成一次向量算术，临床可部署性强。强在探针与可视化支撑“去语言”解释、阈值统一灵敏约束；弱在每种语言来自不同语料，语言效应与语料效应难彻底拆开，且任务高度受控，向自然语音推广待证。


# Foundational speech models evaluation on multilingual dementia prediction

- 论文编号：2587
- 报告人：Bartłomiej Eljasiak
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/eljasiak26_interspeech.pdf

## 问题
痴呆早期筛查需要可扩展语音生物标志；主流基础语音编码器在多语、跨语与零样本认知障碍检测上的系统比较不足，且临床标签数据稀疏。

## 方法
SUPERB 式管线：冻结或微调编码器 → 可学习层加权 → 下游头（轻量 ECAPA-TDNN 或前馈/注意力池化）→ 段级概率平均到被试。语料：DementiaBank 系 ADReSS/ADReSSo/ADReSSM/TAUKADIAL/Dem@Care/Ivanova，加波兰 DiagNeuro；统一痴呆 vs 健康（非健康一律映射为痴呆）。说话人分离用时间戳或 pyannote；段长约 ≥6 s 参与者语音，训练随机 30 s。比较 Wav2Vec2、HuBERT、WavLM、Whisper 等；单语、多语预训练再微调、及未见语迁移。

## 实验与结果
多语设定 WavLM-Base+ 整体 F1 0.761；WavLM-Large 英语子集 F1 0.854。单库上冻结编码器 ADReSSo F1 0.916、DiagNeuro 0.943 等，部分可比或超公开 SOTA。跨语：如 EN+SP 训测 PL 可达 F1 0.929；向 PL 逐步加语种可抬 F1（0.692→0.840）。Whisper-tiny：非目标语预训练再微调普遍优于纯单语基线；西语上仅跨语 transfer 即可 F1 0.678 超单语 0.648。作者因官方 TAUKADIAL 测分不具代表性而自建分层划分，并剔除重复文件以防泄漏。

## 结论
在多语料统一管线下，基础语音模型可做稳健多语痴呆检测；增加训练语种常提升单语表现，并存在一定零样本迁移。注意切分与去重对可比性至关重要。

## 点评
贡献偏“大规模对照与数据卫生”而非新架构，对领域很实用。强在多编码器×多语设定与“加语种反而帮单语”的经验；弱在病因标签被压成二类、任务与录音时长异质、以及自建 TAUKADIAL 划分使与挑战榜直接对比需谨慎。

