# Acoustic Event Detection 1

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从异常声音检测的局部密度归一化，到呼吸音分类的 SSM 骨干，再到大规模自动标注管线、语音声学 landmark 检测，以及生物声学的任务向量合成与嵌入可解释性。共同主题是：在密度不均、标注稀缺、分类体系分散的条件下，如何让嵌入距离、频谱敏感性与生态约束真正服务检测/分类。

方法分歧清晰。距离法 ASD 用 cluster exit 自适应邻域，避免跨簇破坏局部密度假设；呼吸音工作用光谱响应分析论证 SSM 相对 AST 的中高频保持，并加谱感知正则与 Dual-Axis Patch-Mix；TriA 则把场景音频自动变成带事件标注的训练数据。Landmark 检测强调软标签时间展宽与冻结 HuBERT 特征。生物声学两篇分别回答“机构不共享原始数据时如何合成多类群分类器”和“预训练嵌入编码了哪些类语音特征、对任务是否有用”。

瓶颈包括邻域大小敏感、全局自注意力低通行为、标注成本、landmark 元音类难度，以及任务向量合成在 domain negation 等边界条件失效。

## 论文技术总结

# Mind the Gap: Detecting Cluster Exits for Robust Local Density-Based Score Normalization in Anomalous Sound Detection

- 论文编号：177
- 报告人：Kevin Wilkinghoff
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wilkinghoff26_interspeech.pdf

## 问题
嵌入空间异常声检测中，局部密度归一化（LDN）对邻域大小 K 敏感：K 增大常因越过簇边界破坏局部性而变差，固定小 K 又欠稳。

## 方法
分析排序距离与距离比 r_k=d_k/d_{k+1}，用尖锐跳变定义 cluster exit。提出训练无关的 CED：对每个参考样本根据距离比（可邻比平滑）检测退出点，自适应选取邻域大小再做 LDN（可叠加 VarMin）。即插即用替换固定 K。

## 实验与结果
五类嵌入（含 Direct-ACT、OpenL3、BEATs、EAT 等）× 多基准：相对固定小邻域，LDN+CED（及 +VarMin）在宽 K 扫描上相对性能更稳、整体增益一致（文中相对性能曲线约 1.0–1.07 量级）。目标域常更早出现簇退出，解释固定大 K 失效。

## 结论
邻域应随局部性是否保持而自适应，而非先验固定；CED 轻量且无训练，提升 LDN 对 K 的鲁棒性。

## 点评
把“大邻域不稳”归因于结构上的簇退出而非单纯统计噪声，诊断清晰。阈值固定、无标签设定适合工业监测；对极度重叠或连续流形嵌入，距离比启发式可能误触发，需场景校验。


# Lung-SRAD: Spectral-Aware Regularized Audio DASS with Dual-Axis Patch-Mix Contrastive Learning for Respiratory Sound Classification

- 论文编号：550
- 报告人：June-Woo Kim
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shridhar26_interspeech.pdf

## 问题
呼吸音分类（RSC）中 crackle/wheeze 等异常是短时局部谱–时结构；AST 等 CLS 自注意力理论与实证上可能呈低通，削弱高频空间变异，且二次复杂度高。

## 方法
以 AudioSet 蒸馏的 DASS（状态空间）为骨干；用谱响应曲线分析中间层，对选定层施高斯卷积谱感知正则。提出 Dual-Axis Patch-Mix 监督对比学习：沿时间与频率轴混合谱图块，适配 SSM 扫描。ICBHI 官方 60/40 病人无关划分，8 s/16 kHz，SpecAugment，Adam 5e-5，五随机种子。

## 实验与结果
四类 Score：(Se+Sp)/2。纯微调 DASS 61.06%；加谱正则与 Dual-Axis Patch-Mix 的 Lung-SRAD 达 64.48%±0.25（Sp 79.53%、Se 49.42%），相对 AST 基线约 +5%。二分类可达 72.57%。消融显示双轴混合优于单轴；高斯核大小与 σ 过大会降分。

## 结论
SSM 更保中高频空间成分，配合谱正则与双轴混合对比可提升 ICBHI RSC；开源代码公开。

## 点评
把“局部异常=空间高频”接到骨干频谱行为分析，动机强于单纯换模型。Score 仍略低于部分 BEATs SOTA（如 64.84%），敏感性仍偏低；正则层选择依赖响应曲线，跨设备泛化待验。


# TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios

- 论文编号：995
- 报告人：Hong Lyu
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lyu26_interspeech.pdf

## 问题
面向家庭等特定场景的音频分类（AC）标注数据稀缺：通用集（AudioSet、FSD50K、ESC-50）对特定声学场景覆盖不足，专用集（DESED、Kitchen20、CHiMe-Home 等）规模有限。已有自动标注流水线（Emilia-Pipe、NVSpeech-Pipe、NonVerbalSpeech-Pipe）依赖 ASR 或只做副语言标注，难以覆盖广义音频事件。

## 方法
提出 TriA Pipeline 四阶段：Standardization（转 24 kHz 单声道 WAV、响度 -20 dBFS 等）、Audio Activity Detection（auditok 按能量切分，domestic 场景最小 ECT 1.2 s、最大 SCT 2.0 s）、Audio Event Detection（AS-2M 微调的 BEATs iter3+，本地窗 5 s/移 3 s、置信度阈 0.6，再全局检测并拼接）、Filtering（audiobox-aesthetics 的 PC/PQ 与 CLAP 相似度过滤）。用流水线从 Bilibili、Douyin 等构建 TriA（>2130 小时、431 类），并按场景先验切出 TriAGK 子集（TriADESED、TriAKitchen20、TriANonspeech7k）。下游用 BEATs 骨干 + 线性分类头，在人工标注、仅 TriAGK、先 TriAGK 再人工标注三种设定上微调，指标为 Accuracy 与 Macro-F1。

## 实验与结果
小批量验证：约 284.7 小时原始音频、RTX 3090 上约 10 小时、RTF 0.03；Filtering2 后剩 80.08 小时、258 类，主观听测标注准确率约 93.67%。TriA 的 PC/PQ 优于 DESEDreal、Kitchen20、Nonspeech7k。三任务结果（Table 4）：DESED AC 上 TriADESED+DESEDreal 达 Acc 0.8258 / F1 0.8256（相对仅人工约 +5.37% Acc、+3.94% F1）；Kitchen20 序贯微调到 0.9813 / 0.9812；Nonspeech7k 仅 TriA 子集弱于人工，但序贯仍略升。相对仅人工标注，平均相对提升 Acc 3.97%、Macro-F1 3.35%。

## 结论
TriA Pipeline 能把流媒体原始音频转成带事件标注的训练数据；TriAGK 在家庭 AC 任务上可与人工标注相当甚至更好，与人工序贯微调带来稳定增益。代码与数据已开源。

## 点评
核心是把“特定场景缺标注”转成可重复的 AED+美学/CLAP 过滤流水线，并用场景先验子集对接下游任务，而不是只堆大规模无平衡数据。强度在于流水线可扩展、且序贯微调把自动数据当预热。脆弱点在于标注依赖 BEATs 与 AudioSet 本体，对人工集未覆盖或分布偏移的类可能系统偏差；过滤阈值越高类多样性越低，质量与覆盖需权衡。


# Acoustic Landmark Detector based on Conformer and HuBERT

- 论文编号：1386
- 报告人：Mateo Cámara
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/camara26c_interspeech.pdf

## 问题
声学 landmark 是与发音事件绑定的突变点（元音、滑音、塞音/擦音/鼻音的闭开），是连接声学与音系特征的表示，但传统检测多为手工特征与规则；深度学习在音素边界上进步明显，在稀疏 landmark 上的系统能力仍不清楚。

## 方法
在 1839 条人工标注语料（3 说话人；678 VCV + 1161 词；8 类共 8428 个 landmark，90/10 分层划分）上，用 Conformer 编码器（dmodel=256、12 层）做帧级 9 类（背景+8 landmark）分类。关键设计：按事件类型设 Gaussian soft labels（σV=20 ms、σG=15 ms、擦音  soft 12 ms、塞/鼻 10 ms）以建模标注时间不确定性；特征对比 mel、冻结 wav2vec2、冻结 HuBERT、mel+wav2vec2 混合；峰值后处理（高度 0.5、峰间距≥5 帧等）。共 14 组配置，涵盖损失（加权 CE / focal / 无权重）、容量、按类分模型、数据子集与增强；主指标 F1@20 ms（辅 F1@30 ms），并报告本语料 LER。

## 实验与结果
冻结 HuBERT 最好：F1@20 ms=0.77、F1@30 ms=0.84；soft 相对 hard 绝对 +0.070（元音从 0.54 跌至 hard 的 0.18）。塞音/擦音 release 与塞音 closure 较易（F1>0.80），元音与鼻音 release 较难（元音约 0.55）。本语料 LER 13.8%；与 Auto-Landmark（TIMIT、5 类、31.3% LER）因语料/标签/指标不同不可直接比。零样本到 Auto-Landmark 对应子集 LER 63.0%。消融：focal、按类分模型、仅 VCV 训练伤害最大；词子集略优；增强与合成预训练几乎无增益。

## 结论
Conformer+冻结 HuBERT 与按类 σ 的 soft label 可在本语料上达到较强的时序定位 landmark 检测；可检测性随事件突变程度升高，与 Stevens 理论一致。局限为语料小（3 说话人）、单次划分，以及对 TIMIT 的零样本迁移有限。

## 点评
抓的是“稀疏、需时间容差对齐的音系事件检测”，把标注时间模糊显式写进 soft label，比单纯换更大模型更对症。HuBERT 优于 mel/wav2vec2 说明 SSL 表征对 manner 相关突变有用，但帧移与峰值后处理仍约束极限。数据域窄（孤立音节/词）是主要脆弱点，跨语料与连续自发语音仍待验证。


# Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data

- 论文编号：2629
- 报告人：Ragib Amin Nihal
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nihal26_interspeech.pdf

## 问题
生物声学训练数据按类群、地区与机构碎片化，难以集中；各自微调的专家模型无法无数据联合或会遗忘。现有 BirdNET/Perch 类单体模型扩展需全量重训。任务算术在视觉中有效，但在生物声学中尚未系统检验，也不清楚生态声学结构能否预测权重空间几何。

## 方法
从同一预训练 BEATs（iter3+ AS2M）独立微调 5 个类群专家（661 种：Passerines 336、非雀形目 157、猛禽/水鸟 84、海洋哺乳动物 21、两栖类 63），只共享任务向量 τ=θ−θ0（编码器权重、不含分类头）。合并策略对比 simple avg、task arithmetic、DARE，以及 TIES / DARE+TIES / DELLA 等符号冲突方法。评估用冻结合并编码器上的线性探针与 k-NN；以相对联合训练的 composition gap 为主。另做地区组成（BirdCLEF 东西非/南亚/新热带 + BirdSet POW）与 focal→soundscape 的 domain negation。用谱分布 JSD 与任务向量余弦相关检验“声学生态位”假说。

## 实验与结果
全部类群对满足线性模式连通、无 loss barrier。任务向量近正交：跨类群余弦 0.01–0.04，鸟类内 0.08–0.09；与谱 JSD 强负相关（Spearman ρ=−0.915）。661 类上 DARE+avg 达 59.2%（联合 68.3%，约 86% 相对；gap≈9.1–9.5），TIES 等冲突方法差 1–6 个百分点。合并使多数类群（雀形目等）掉点、少数类群获益（海洋哺乳 +3.9%、两栖 +1.9%）。地区合并准确率 60.8%（联合 67.2%）；三区合并对留出区达单区模型约 90.8% 准确率。focal 任务向量减法单调损害焦点与声景准确率，域否定失败。

## 结论
独立微调的生物声学专家可通过任务算术组成多类群分类器且无需共享数据；近正交几何使简单平均最优、符号冲突方法有害；合并对少数类群更友好。域否定因录音风格与物种身份纠缠而失效。作者主张机构只共享任务向量即可协作组装分类器。

## 点评
把“声学生态位→近正交任务向量→简单平均最优”串成可检验预测，比盲目套用视觉合并更有解释力。实用价值在隐私友好的一射式联邦式组装；脆弱点包括必须统一基座与超参、线性探针 gap 仍约 9%、以及更细分类阶时正交性可能减弱（正文亦提示）。


# Beyond task performance: Decoding bioacoustic embeddings with speech features

- 论文编号：2759
- 报告人：Ines Nolasco
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nolasco26_interspeech.pdf

## 问题
预训练音频嵌入在生物声学中已成为标配，但很少知道它们编码了哪些声学属性、以及这些属性对具体任务是否有用；仅靠下游分类榜单难以做透明、可解释的模型选择，尤其对稀有种与数据稀缺场景。

## 方法
从 BEANS 训练划分取 6 个数据集（狗个体、蝙蝠个体、鸟种、海洋哺乳动物种、蚊子种、语音词；共约 34054 条）。用 OpenSmile eGeMAPS 提取 88 维可解释特征（F0、Loudness、Harmonicity、SpectralShape、Formants、MFCC、Temporal）。对 6 个冻结编码器末层时间平均嵌入（BEATS base、NatureLM、BirdMAE、BirdNET、EffNet all、Perch）做：Emb2Feat——线性 ridge 与浅层 MLP（256 隐层）回归探针，报 R²；Emb2Emb——用 ridge 预测模型间嵌入重叠；FeatImportance——特征与标签的 NMI，再与 R² 交叉对照任务显著性与可恢复性。

## 实验与结果
BirdMAE 与 BEATS base 在多数特征类别上可解码性最好；全模型拼接通常最好，显示互补。非线性相对线性最大约 +0.08 R²，故主分析用线性。Loudness 整体最好（文摘 R²=0.76），F0 最难（R²=0.33）；谱形状也好于 F0。Emb2Emb 显示无单一模型可预测全部其他模型，BirdNET 最难被预测。任务显著特征因类群而异：鸟/狗偏 F0，蚊/蝙蝠偏 loudness，海兽/语音命令偏 MFCC；不少任务显著特征在单模型末层线性不可恢复，拼接也未必总最优（高维易伤回归）。

## 结论
模型编码互补而非冗余；loudness 易恢复、F0 难；任务相关特征因分类群而变且未必被任一单模型编码。框架用声学内容而非仅榜分指导选型。局限：eGeMAPS 为人声优化、F0 提取可能不可靠；时间池化丢时序；未做分层探测。

## 点评
把“选哪个生物声学嵌入”从黑盒榜分化为可检验的特征可恢复性与任务显著性对齐，方向正确。强在跨模型/跨类群的系统探针与互补性证据；弱在 ground-truth 特征本身可能偏置（尤其超声/非声道发声），且末层+均值池化可能低估时变信息，结论应视为选型假说生成器而非因果解释。

