# Acoustic Event Detection 2

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：5
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖声音事件检测、异常声检测、开放词汇 SED、跨域小样本增量分类、超声发声检测、短时/事件扰动下的声场景分类，以及谱增强与音乐分类去偏。预训练前端 + 一致性/均值教师、概率化音文对齐、统一扩散异常检测，体现“少标签、多域、重叠事件”下的共同压力。

开放词汇与语义锚点、查询增强，把 SED 从闭集类别推向任意事件描述；跨域 FCAC 与事件注入 ASC 基准则直面分布偏移与前景事件干扰。噪声鲁棒边界引导注意力与 SpecAugment—Patch Merging，分别从边界约束与训练吞吐两侧优化。

音乐分类上的渐进可学习反事实注意力提醒：事件/场景模型同样需要抑制虚假判别区域。整体趋势是：结构化一致性、不确定性建模与鲁棒评测基准并行推进。

## 论文技术总结

# Consistency-Regularized Dual-Branch Network with Performance-Aware Mean Teacher for Sound Event Detection

- 论文编号：353
- 报告人：Lipeng Dai
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dai26_interspeech.pdf

## 问题
预训练模型（如 ATST）用于 SED 时，浅层与深层特征利用不足，半监督 mean teacher 更新幅度固定、易不稳定。需要更好的跨分支一致性与自适应教师更新。

## 方法
ATST 前端 + 双分支后端分别建模浅/深特征；提出时间拓扑一致性损失（TTC）对齐双分支时序结构相似；Performance-Aware Mean Teacher（PA-MT）按学生表现自适应 EMA 更新幅度；跨阶段融合（CSF）合并不同训练阶段优势。在 DCASE 2024 Task 4 上评测。

## 实验与结果
最终 0.541 PSDS1、0.768 mpAUC、Score 1.309，称新 SOTA；消融显示 TTC 主要提 PSDS1，PA-MT 稳定教师更新，CSF 进一步抬分。

## 结论
作者认为双分支一致性正则与表现感知 mean teacher 可提升预训练 SED 的半监督效果。

## 点评
把“浅深特征该一致什么”具体成时间拓扑，比笼统一致性损失更贴 SED 边界任务；PA-MT 针对固定 EMA 的痛点。分数高度依赖 DCASE2024 协议与强预训练前端，迁移到其他标注噪声设定需再验证。


# MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining

- 论文编号：360
- 报告人：Yu Nakagome
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nakagome26_interspeech.pdf

## 问题
真实场景多事件重叠、同一场景可有多种文本描述，音频–文本对齐存在多对多歧义；确定性点嵌入的对比学习难以表达不确定性。掩码式不确定性模拟也不够贴近真实混合。

## 方法
MixProLAP：各模态表示为分布，做不确定性感知跨模态对齐；用音频–文本对混合构造重叠声，捕捉语义包含关系；引入多级 inclusion loss。相对 deterministic CLAP 基线（同数据同预训练权重、InfoNCE）比较。

## 实验与结果
零样本检索：AudioCaps 训练时 A→T R@1 26.85（CLAP 24.23）；Clotho 训练在 Clotho A→T R@1 15.60（CLAP 13.40）。消融显示 mixing + multi-level inclusion 优于谱/词掩码不确定性策略。

## 结论
作者认为混合诱导的概率对齐能更好建模多事件与多样描述歧义，提升检索鲁棒性。

## 点评
用真实感混合代替掩码来造不确定性，切中声学场景本质；概率嵌入也便于解释语义密度。T→A 部分设定提升不均，说明分布建模对检索方向不对称，仍需更细校准。


# UD-ASD: A Unified Diffusion Model for Anomalous Sound Detection

- 论文编号：482
- 报告人：Pengxiang Gao
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26c_interspeech.pdf

## 问题
异常声音检测常为每台机器单独建模，泛化差、异常覆盖窄。扩散模型有条件生成能力，能否用统一模型跨机型监测。

## 方法
UD-ASD：log-Mel 输入；轻量模块把机器 ID 编成条件嵌入，引导扩散重构该机正常数据；用 GMM 拟合重构误差分布判异。统一模型跨机型/域学习；DDIM 采样加速推理（约 24.4M 参数，A40 上约 0.32 s/clip）。在 DCASE2022 Task 2 评测。

## 实验与结果
相对官方基线摘要称 AUC +3.44%、pAUC +2.52%。Table 2：UD-ASD-U 调和平均 AUC/pAUC 约 77.16 / 62.80，优于 Official-AE/CLS 与多种生成式方法；分机型上 Fan/Slider 等较强、Valve 等较弱。

## 结论
作者认为条件扩散统一模型可跨机型 ASD，并用重构误差分布做异常度量。

## 点评
“一小块条件模块 + 统一扩散”降低每机一模型成本，跨域共享特征是卖点。扩散推理延迟与对未见故障模式的覆盖仍是工业落地约束；分机型表现不均提示条件嵌入未必学到同等质量的机型流形。


# A Semantic-Anchor-based Method for Open-Vocabulary Sound Event Detection

- 论文编号：731
- 报告人：Yanfeng Shi
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26f_interspeech.pdf

## 问题
开放词汇 SED 的 query 检索常只把查询当向量匹配，缺乏事件语义理解，新类识别弱。需要语义级参考与更强的 query–特征交互。

## 方法
学习一组 semantic anchor 作为语义参考 token，任意事件通过注意力锚定理解；双向注意力增强 query–特征交互；定制 query 增强提鲁棒。骨干含 HTS-AT；在 AudioSet-Strong 开放词汇设定与 DESED 跨库/零样本评测。

## 实验与结果
开放词汇 novel 类 PSDS 34.9（总体 PSDS 50.5）；DESED 零样本 PSDS1 44.1，甚至超过 DESED 监督基线。称优于既有开放词汇 SED。

## 结论
作者认为语义锚点使模型真正“理解”事件语义，从而提升新类与跨数据集泛化。

## 点评
把开放词汇从纯检索推向有语义参考的注意力机制，对稀有/新类有针对性。锚点数量与初始化、文本query质量会强烈影响上限；零样本超监督基线的结果需结合标签与协议细节解读。


# Cross Domain Few-Shot Class-Incremental Audio Classification Via Adversarial Contrastive Learning

- 论文编号：1250
- 报告人：Yanxiong Li
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/si26b_interspeech.pdf

## 问题
既有 Few-shot Class-incremental Audio Classification 假设基类与增量类同域；实际常有域偏移。本文首次系统处理 Cross Domain FCAC（CD-FCAC）：会话间同时存在类增量与域偏移。

## 方法
编码器在 base session 训练后冻结，分类器各会话更新。对抗对比训练：生成多样对抗样本模拟伪目标域，与源域样本一起学域不变嵌入；base session 用监督对比损失促类内紧、类间分。在六对跨域数据集组合上评测 Average Accuracy。

## 实验与结果
六向 AA（%）：Ours 在 FS→NS 46.89、FS→LS 41.67、NS→FS 85.17、NS→LS 79.09、LS→FS 80.05、LS→NS 79.78，均高于 DFSL/CEC/PAN/AMFO 变体与 PCR。N-way K-shot 分析显示 K 增则 AA 升，N=5 时较优。

## 结论
作者认为对抗对比可同时缓解域偏移与类增量遗忘，在 CD-FCAC 上建立新 SOTA。

## 点评
把 FCAC 推到跨域设置填补现实缺口；编码器冻结简化增量但也可能限制对新域声学的适应。对抗样本模拟的“伪目标域”与真实目标域差距仍是主要风险。


# USV-DETR: High-Resolution and Densely Supervised Detection of Ultrasonic Vocalizations

- 论文编号：1492
- 报告人：Yilan Wei
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wei26d_interspeech.pdf

## 问题
啮齿动物超声发声（USV）在频谱图上尺度小、窄带、稀疏，规则阈值或常规 CNN/检测器难保细节与稳定监督。

## 方法
USV-DETR 基于 RT-DETR：引入高分辨率 P2 特征层表征窄带短时信号；采用 DEIM 训练框架（密集 O2O 匹配增强 + 对低质量匹配的自适应加权监督）稳定稀疏小目标学习。损失含 MAL、L1、GIoU、Focal、分布精炼等。数据：SqueakOut（小鼠，12954 图）与自建 USVpic（大鼠，3000 图），7:2:1 划分；指标 AP、AP50、AP75、APs。

## 实验与结果
摘要称跨数据集一致取得最佳检测，时频定位更准。全文较短，细表数字在抽取中覆盖有限。

## 结论
作者认为高分辨率特征与密集监督使端到端检测器更适 USV 小目标，可作为神经行为声学分析工具。

## 点评
把通用小目标检测进展迁到生物声学，P2+DEIM 针对“又小又稀”很贴切。两数据集均为频谱图目标检测设定，对连续长录音流式部署与种系泛化仍需工程化验证。


# Enhancing Temporal Prediction Consistency for Short-Duration Acoustic Scene Classification via Semantic Adversarial Training

- 论文编号：1955
- 报告人：Yiqiang Cai
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cai26b_interspeech.pdf

## 问题
短窗（如 1 s）声学场景分类相对满时长严重掉点。作者归因于时间预测不一致：短窗预测与长时场景语境错位。需迫使特征丢掉“时长依赖语义方差”、保留场景判别信息。

## 方法
提出 Semantic Adversarial Training（SAT）：辅助对抗目标与场景分类竞争，事件判别器（527 类，伪标签来自冻结 BEATs/AudioSet）经 GRL 对抗；用 Local–Global Prediction Discrepancy（LGPD）分层稳定/不稳定测试子集。在 TAU20 上以 10 s 为全局、1 s 为短窗评测。

## 实验与结果
基线随 LGPD 升高准确率由约 95.8% 掉到 34.7%。Table 显示 +SAT 达 76.2 / 50.9（对应分列指标）优于 Mixup、Freq-MixStyle、MTL、KD、JTL 等；不稳定集上缓解掉点更明显。

## 结论
作者认为时间预测一致性与短窗 ASC 精度直接相关，SAT 可提升高差异样本上的稳健性与时序一致性。

## 点评
把短窗崩塌诊断为“与全局语境不一致”而非单纯信息不足，并用事件级对抗去掉时长相关捷径，思路清晰。事件伪标签噪声与对抗权重敏感；LGPD 分层本身依赖满时长语境，部署时短窗系统未必总能拿到 10 s 参考。


# BG-CRNN: Boundary-Guided Dynamic Attention for Sound Event Detection in Complex Scenarios

- 论文编号：2019
- 报告人：Zongmu Lin
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26k_interspeech.pdf

## 问题

复杂噪声环境下 Sound Event Detection（SED）性能会随 SNR 下降而急剧恶化。现有系统虽可用半监督、预训练特征或外部分离模块缓解噪声，但自注意力仍易把目标事件特征与相邻背景噪声混在一起，时间定位不够稳。

## 方法

提出 BG-CRNN：前端用 CNN 与冻结预训练 ATST-Frame 提取并拼接特征，后接 Dynamic Boundary Transformer（DBT）与 Boundary-Guided Attention（BGA），再经 RNN 做帧级预测，半监督训练。

DBT 含双分支共六层 Dynamic Boundary Attention Block：边界分支由强标签差分得到边界标签，用加权边界损失预测边界概率；另一分支将预测边界二值化（阈值 τ=0.7），按类别循环分配到多头，用累积和生成 Segment ID，构造仅允许同段内注意力的动态 mask，注入 scaled dot-product attention。BGA 用边界特征经门控网络得到时域权重，以可学习标量 α（初值 0）残差增强 CNN 特征中的活跃事件区。总损失为监督 SED（BCE）+ Mean Teacher 一致性损失 + 加权边界损失。

## 实验与结果

在 DESED 与 WildDESED（16 kHz）上评估，指标为 PSDS1/PSDS2。在干净 DESED 上训练时，各 SNR 下 BG-CRNN 均优于复现的 ATST-CRNN；在噪声 WildDESED 上训练并 fine-tune 后，-5 dB 时 PSDS1 达 0.191、PSDS2 0.417，优于 EADSED 与 LLM-based 方法。DESED 消融中，完整流水线 PSDS1/PSDS2 为 0.566/0.791，高于基线 0.502/0.750。

## 结论

作者认为边界引导的段内注意力与 BGA 能抑制噪声干扰、提升低 SNR 下的检测与定位，具有实际部署潜力。边界帧稀疏需加权损失；单独加 BGA 可能过度聚焦边界，需与动态 mask 联用才最优。

## 点评

做法抓住的是“噪声与目标事件在时序上耦合、自注意力跨段泄漏”这一类问题：用显式边界把注意力硬限制在事件段内，再软增强活跃区，比单纯数据增强或外部分离更贴近 SED 的定位目标。强依赖边界预测质量与阈值设定；在极低 SNR 下边界本身难估，动态 mask 可能切错，这是设计上的脆弱点。


# Towards Event-Robust Acoustic Scene Classification

- 论文编号：2350
- 报告人：Bohan Hu
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/cai26d_interspeech.pdf

## 问题

真实声学场景中前景事件会随时空、季节变化（event shift），而现有 ASC 数据集多为相对干净、事件构成稳定的录音，难以评估模型对未知前景事件的鲁棒性。跨城、跨设备、时变等基准也未专门覆盖这一因素。

## 方法

提出 Event-Shifted Acoustic Scene（ESAS）基准：以 CochlScene 为背景、FSD50K 为事件池，用 BEATs 检测背景中已有事件并过滤，再以 GPT-4 做场景–事件语义分组，将候选事件分为 Known / Unknown；训练与验证仅含背景与 Known 混合，Unknown 仅出现在测试集。混合协议：10 s、44.1 kHz、每段 1–10 个事件类、时间位置随机、时间拉伸 [0.8,1.15]、音高移位 [-3,3]、场景–事件 SNR ∈ [-15,+15] dB。评估按 background-only / known-event / unknown-event 三档准确率，以分离“混合本身”与“分布外事件”两类失效。

## 实验与结果

ESAS 约 211 h、13 场景类、76,081 段；测试集三类样本约 1:1:1。基线含 TF-SepNet、BC-ResNet、GRU-CNN、CP-Mobile、BEATs、PaSST。背景准确率约 78–84%；引入 Known 事件后明显下降（如 TF-SepNet 降约 14.7%）；Unknown 条件下轻量 CNN 可降最多约 22 个百分点，预训练 Transformer 仍降约 7–9 点。事件数增至 10 时轻量模型可跌至 50% 以下，BEATs/PaSST 仍约 68–70%。低 SNR 下 TF-SepNet/BC-ResNet 可至 37.42%/43.21%，Transformer 约 67%。

## 结论

作者认为现有 ASC 对未知前景事件与密集多声部干扰脆弱，轻量 CNN 尤甚；ESAS 旨在推动面向 event-robust ASC 的研究，尤其是能应对不可预测噪声的轻量结构。

## 点评

贡献主要在问题定义与可控合成基准，而非新分类器：用 Known/Unknown 拆分把“声学混合难”和“事件分布外”分开测，比单一整体准确率更有诊断价值。合成依赖 LLM 语义过滤与固定混合协议，真实场景中事件–场景耦合与录音条件更复杂，外推时需谨慎；预训练大模型相对更稳，也提示轻量部署路线仍缺针对性防御机制。


# From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer

- 论文编号：3273
- 报告人：Chanwoo Kim
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/park26j_interspeech.pdf

## 问题

AST 训练普遍使用 SpecAugment，被 mask 的谱图区域语义信息少，但仍作为 token 进入 Transformer，带来二次注意力开销。已有 token 削减方法常需额外模块或相似度计算，或随机丢弃而不显式利用增强造成的信息空洞。

## 方法

提出 SpecAugment-Patch Merging：先把 SpecAugment 的时/频 mask 对齐到 16×16、stride 10 的 patch 网格（保证 patch 全掩或全保留），得到全零 patch 的二值候选；在 patch 与位置编码之后、Transformer 之前，随机抽取 2r 个掩码 patch 配成 r 对，按维 max 合并为一枚 token 并压缩序列（保留 [CLS]/[Dist]）。r=0 时与原 SpecAugment 效果接近。合并策略在 max/mean/sum/random drop 中选维 max。

## 实验与结果

在 Balanced AudioSet、ESC-50、Speech Commands V2 上，以 ImageNet 预训练 DeiT-Base distilled 初始化，单卡 RTX 4090。AudioSet 上 r 从 0 增至 100：mAP 几乎不变（34.07→34.08），吞吐 43.3→49.3 samples/sec（约 +13.9%），显存 24.64→21.50 GB。ESC-50：Acc 89.20→88.67，吞吐 127.3→142.9；Speech Commands V2：Acc 98.13→98.06，吞吐 411.1→429.4。同等合并率下相对复现的 PaSST-U，AST 侧吞吐更高（如 16.5% 时 49.3 vs 46.7 S/s）。

## 结论

作者认为把增强产生的掩码区当作合并线索，可在几乎不损精度下加快 AST 训练；因只能合并已掩码 patch，最大削减比受掩码强度限制，但思路可推广到其他使用 SpecAugment 的 patch Transformer。

## 点评

核心洞察是“SpecAugment 已经制造了可丢弃的冗余”，用增强结构做 token 削减，比另加 ToMe 式相似度模块更轻。强依赖“掩码 patch 确实无信息”这一假设；若 mask 未对齐 patch 或掩码过少，可合并候选不足，效率上限就卡住。与 PaSST-U 的对比在统一训练设定下成立，绝对 mAP 不宜直接对照原论文数字。


# Progressive Learnable Counterfactual Attention for Music Classification

- 论文编号：147
- 报告人：Yi-Xing Lin
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26_interspeech.pdf

## 问题

音乐分类中注意力常只靠分类损失弱监督，易被伪相关与数据集偏差带偏。LCA 用可学习反事实分支暴露误导性区域，但在单一表示空间中残余偏差仍可能与主注意力纠缠，难以彻底解耦。

## 方法

提出 Progressive Learnable Counterfactual Attention（P-LCA）：在 genreMERT（或 Short-chunk ResNet）的 LCA 之上做 K 阶段精炼。每阶段在当前表示上跑主分支与反事实分支，用与 LCA 相同的一组损失；阶段结束后把主分支注意力条件特征经共享的 stage-wise representation projection 投影到新潜空间，作为下一阶段输入，并用正弦 stage embedding 区分阶段、共享注意力参数。推理时丢弃反事实分支。总损失为各阶段损失加权求和。

## 实验与结果

任务：Artist20 歌手识别（SID）、GTZAN 流派（MGC）、EMOPIA 情感（MER）。SID 消融中 K=3 最佳；genreMERT(w/ P-LCA) 帧级 F1 Avg/Best 0.70/0.73、歌曲级 0.88/0.94，优于 LCA。去投影模块或仅增大 LCA 容量均无明显增益。MGC：帧/歌曲 Acc 0.91/0.94（LCA 为 0.89/0.92）。MER（Short-chunk ResNet）：4Q/Arousal/Valence Acc 0.78/0.92/0.84，高于 LCA 的 0.76/0.92/0.82。可视化显示主注意力更聚焦，反事实更弥散。

## 结论

作者认为分阶段投影能从不同表示视角反复暴露并抑制残余注意力偏差，在多种音乐分类任务上稳定优于单阶段 LCA，且增益来自结构而非单纯参数量。

## 点评

做法针对的是“偏差与任务线索在同一特征空间不可分”：用投影换视角再做一轮反事实竞争，比加深单阶段 LCA 更对症。阶段数有最优值（文中 K=3），过多可能过拟合或稀释监督；目标与超参基本沿用 LCA，跨架构适用性已在 ResNet 上验证，但训练目标组合较重，落地时调参成本不低。

