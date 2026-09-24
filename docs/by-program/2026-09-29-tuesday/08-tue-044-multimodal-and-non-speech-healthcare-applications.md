# Multimodal and Non-Speech Healthcare Applications

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接呼吸音、构音运动学、帕金森病数字生物标志物、生物声学健康编解码评测，以及视听抑郁检测。非言语/多模态健康信号的共同瓶颈包括：临床语义接地不足、实验室设备难规模化、声学指标纠缠呼吸–喉–构音贡献、试验中安慰剂/霍桑效应，以及压缩传输是否保留诊断信息。

方法上，零样本呼吸音分类用医学 LLM 合成报告做对比对齐；MediaPipe Face Mesh 单摄像头 3D 跟踪对标光学动作捕捉；从 EMA/声学导出构音无力指数以解耦构音成分；临床试验数据检验视听与轻拍数字标志物的被试内稳定性；BACH 系统评测编解码在重建保真与下游任务间的错位；抑郁检测则用优势加权排序损失在潜空间重建潜在序数结构。

## 论文技术总结

# Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment

- 论文编号：2235
- 报告人：Mustafa Talha İlerisoy
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ilerisoy26_interspeech.pdf

## 问题
自监督呼吸音编码器缺临床语义锚定，难零样本诊断；通用音频–文本模型（CLAP 等）缺医学用语，且真实音频–报告配对稀缺。

## 方法
REACH：用医学 LLM 由元数据合成结构化听诊报告作语义锚；冻结医学文本编码器，优化音频投影与骨干；sigmoid 对比损失 + 原生 SSL 重构损失防特征崩坏；FAISS 相似感知负采样拉远病理边界。在 6 数据集 9 任务上评零样本与线性探针。

## 实验与结果
零样本平均 AUC 61.3%，高于 CLAP 51.4% 与 Qwen2-Audio 54.9%；线性探针平均 AUC 71.6% 最高，且仅用全规模基线约 43% 的数据。对齐后仍保持单模态能力。

## 结论
结构化语义对齐可把领域呼吸编码器变为可零样本的多模态工具，效率与效果优于更大通用音频语言模型。

## 点评
关键洞察是“对齐而非从头训医学 CLAP”，LLM 合成报告缓解配对稀缺。强在数据效率与零样本；合成文本质量与元数据覆盖决定上限，临床部署仍需分布外病理与设备变异验证。


# From Lab to Laptop: Validating 3D Speech Kinematics with MediaPipe Face Mesh

- 论文编号：3022
- 报告人：Victoria Sanchez
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sanchez26b_interspeech.pdf

## 问题
发音运动测量依赖 EMA/光学动作捕捉，成本高难临床扩展；已有摄像头方法常缺毫米级、深度可解释的完整轨迹验证。

## 方法
单路笔记本 RGB + MediaPipe Face Mesh；以外眦距做被试校准到毫米，稳定面标做头动刚体校正；与同步 Cortex 光学捕捉对比。任务：DDK、句子重复、最大幅度运动（4 成人，116 段）。评 30/15 fps（匹配滤波带宽）下 3D uRMSE、相对 ROM 的位移误差、速度保真与互相关。

## 实验与结果
3D 位置 uRMSE 均值 2.03±0.59 mm（30 fps），15 fps 相当；归一化位移误差 6.63±1.28%；深度轴可恢复；15 fps 在语音相关频带无明显效用损失。误差沿各标记主运动轴最大。

## 结论
单相机 MediaPipe 流程可达毫米级、深度可解释的发音轨迹，15 fps 仍可用，利于规模化与远程采集。

## 点评
把“是否够临床用”落到轨迹级、毫米单位的金标准对比，比只比摘要特征更硬。样本量小且健康受试者；真实疾病与光照/摄像头变异仍需外推验证。


# Toward an Articulatory Weakness Index for Speech Kinematics in Parkinson’s Disease

- 论文编号：159
- 报告人：Shrishail Baligar
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/baligar26_interspeech.pdf

## 问题
多数 PD 声学指标混杂呼吸–喉–构音贡献，难单独量化构音减弱；EMA 直接但难临床普及，缺可从音频估计、可解释的标量构音指标。

## 方法
在健康 USC-TIMIT EMA 上从六线圈运动特征学 PCA 轴 Za（越大=运动更小更慢）；汇总为 AWI 等标量。临床侧用音频→EMA 反演（Wu et al.）得代理轨迹：PD 21 人连读、9 对年龄性别匹配对照（PVQD）、398 人声带过度功能语料测特异性。与 UPDRS 等量表相关。

## 实验与结果
USC-TIMIT 上音频推导 Za 与 EMA 一致（Pearson r=0.839）。AWI 在 PD 升高并与运动严重度相关；健康与声带过度功能群体相对稳定，对性别/响度较不敏感。定位为连续描述量而非诊断分类器。

## 结论
提出 EMA 落地、可纯音频估计的构音减弱指数，为未来呼吸–喉–构音子系统分解奠基。

## 点评
把“子系统可分离指标”落到可部署的标量，方向正确。健康参考空间与反演模型误差会传导；PD 样本量有限，且与声学混杂指标的相对增益需更大队列确认。


# Speech and Video Biomarkers Exhibit Reduced Within-Subject Variability in Early Parkinson’s Disease and Resistance to Placebo and Hawthorne Effects

- 论文编号：2850
- 报告人：Vikram Ramanarayanan
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kothare26b_interspeech.pdf

## 问题
PD 临床试验中安慰剂与霍桑（被观察）效应使 MDS-UPDRS 等主观量表噪声大；早期 PD 尤其敏感度不足。需检验语音/视频数字生物标志相对量表的稳定性与抗上下文干扰能力。

## 方法
ASCEND Phase 2（NCT06006247）早期未治疗 PD：50 人远程每两周完成语音、面部、指敲任务至 12 周。试验未达主要终点、无明显运动改善，故合并组分析“纯噪声”。基线看数字指标与 UPDRS Part III 相关子项的 Spearman 相关；纵向用混合效应模型看相对基线变化。

## 实验与结果
基线若干客观指标与对应 UPDRS 项相关（如自发语音 F0 SD 与 Speech ρ=−0.36；眨眼率与 Facial ρ=−0.46）。相对 MDS-UPDRS，语音/视频/指敲指标显示更低被试内变异，并对安慰剂/霍桑效应更不敏感。作者主张其作更稳健的试验终点候选。

## 结论
在无真实疗效的早期 PD 试验中，视听数字生物标志比 UPDRS 子分更稳、更抗安慰剂与观察效应，利于灵敏检测进展或疗效。

## 点评
巧妙利用“阴性试验=噪声显微镜”比较量表与数字指标，证据设计强。相关量级中等，且任务与 UPDRS 构念仅部分对齐；推广到有真实疗效的试验仍需验证灵敏度–特异度权衡。


# BACH: Benchmarking Audio Codecs for Bio-Acoustic Health

- 论文编号：1588
- 报告人：Zixing Zhang
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26w_interspeech.pdf

## 问题
远程医疗依赖心音、鼾声、肺音等生物声学信号的传输与分类，但信号量大、维度高，压缩时能否保住诊断线索尚不清楚。通用音频 codec 在语音/音乐上保真度高，却未必保留生物声学中的短促、稀疏、不规则临床线索；现有 Codec-SUPERB、ARCH、AudioCodecBench 等评测也未系统覆盖健康声学任务。

## 方法
提出 BACH，在统一管线中评测八个约 1 kbps 的神经音频 codec（DAC、EnCodec、WavTokenizer、BigCodec、SpeechTokenizer、FACodec、UniCodec、SemantiCodec），覆盖多码本、单码本、解耦与语义类设计。评测分三条路径：Original（原始音频+预训练 HuBERT 特征）、Compressed（直接用 quantizer 表示）、Reconstructed（codec 重建后再经 HuBERT）。下游分类器统一为线性投影 + Transformer Encoder + 前馈头；分类报 Acc/F1，重建报 UTMOS、PESQ、STOI。五个数据集：Snoring、HeartSound、ICBHI、MSTI、VocalSound。

## 实验与结果
Compressed 域 Acc/F1 普遍低于 Original（如 Original 在 Snoring/HeartSound/ICBHI/MSTI/VocalSound 上 Rec 基线约 96.0/100.0/94.5/78.2/90.6）。语义/解耦类 codec 在 Compressed 域更强：SpeechTokenizer、FACodec 总体最优（如 FACodec HeartSound Com. 99.5/99.5，SpeechTokenizer MSTI Com. 41.5/41.8 显著高于多数模型个位数 Acc）。重建保真与下游任务不对齐：DAC/EnCodec 重建指标较好但任务相对弱；SpeechTokenizer 重建偏低但任务强。增加码本深度主要抬升 PESQ，对下游 F1 增益有限。

## 结论
BACH 表明现有 codec 难以同时兼顾重建保真与诊断语义保留；面向医疗应用的 codec 需联合优化感知质量与任务相关信息。作者计划扩展更多生物声学任务与真实场景鲁棒性评估。

## 点评
工作把“codec 好不好”从听感指标拆成 original / compressed / reconstructed 三视图，直接打在健康声学分类上，抓的是医疗传输场景里真正要保的是语义而非 MOS。强处是暴露重建–任务错位，以及语义引导 quantizer（SpeechTokenizer/FACodec）的相对优势；脆弱处在于下游仍依赖 HuBERT+小分类头、码率统一到约 1 kbps、且部分数据集很短（如鼾声约 1 秒），对 codec 泛化结论需谨慎外推。


# Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking

- 论文编号：535
- 报告人：Manning Gao
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26d_interspeech.pdf

## 问题
基于音视频的自动抑郁检测（ADD）中，抑郁与非抑郁样本特征高度重叠，点式 BCE 把二者当独立名义类，忽略抑郁严重度的潜在序结构；vlog 数据集又只有二值标签，标准成对损失对所有 pair 均等加权，难以在模糊边界处拉开决策面。

## 方法
双流时间编码：1D Conv 投影 + Seq-TDNN，得到音/视表示后经模态 Transformer，再用 Mutual Transformer（a→v、v→a 与联合自注意力）融合，mean-pool + MLP 输出抑郁分数 s 与概率 p=σ(s)。核心是 Binary Advantage-weighting Ranking (BAR) Loss：由正负分数差构造难度矩阵，对难 pair 做 advantage 加权的 hinge 间隔分离（Lsep），并对类内分数做加权紧致（Lcom），再加概率分布正则（Lreg），总损失为 L_BCE + λ_BAR(Lsep+λ_com Lcom+λ_reg Lreg)。推理在验证集上网格搜索动态阈值 τ* 以最大化 F1。

## 实验与结果
数据：D-vlog（961 条，555 抑郁/406 非抑郁）、LMVD（1823 条，908/915）。Ours 在 LMVD 上 Acc/P/R/F1/Avg 为 76.50/75.00/79.12/77.01/76.91；在 D-vlog 上 F1 77.66、Avg 76.44，整体优于 Bi-LSTM、DepTrans、DepMamba、CAF-Mamba 等；DepMamba 在 D-vlog 上 Recall 略高但 F1 略低。消融：去掉 mutual transformer 或 advantage-weighting 均明显掉点（如 D-vlog Avg 从 76.44 落到 73.38/70.23）。训练中 active hard pairs 从 4184 降到 2463，剩余 hard pairs 平均余弦相似从 0.77 降到 0.57；LMVD 上间隔 m=1.15 最优。

## 结论
BAR Loss 用成对排序与难样本加权，从二值标签中恢复潜在序结构并缓解特征重叠，在野外 vlog 数据上达到或接近 SOTA。局限是目前仅评野外数据，作者计划扩展到 DAIC-WoZ 等临床集以验证域迁移。

## 点评
做法的关键不是再堆一个融合模块，而是把“抑郁程度是连续谱、标签却是二值”写成几何约束：难 pair 驱动间隔、类内方差压缩、再配动态阈值。与常见 BCE/简单 ranking 比，优势在显式打模糊重叠区；风险是超参多（Optuna 搜出的 m、β、λ 等）、依赖验证集调阈值，以及野外自报/志愿者标注与临床标准的鸿沟。

