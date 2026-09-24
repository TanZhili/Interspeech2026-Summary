# TidyVoice2026 Challenge: Cross-Lingual Speaker Verification

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Challenge
- Area：14
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

TidyVoice2026 跨语说话人确认挑战的核心是说话人身份与语言线索纠缠：同说话人跨语接受、同语不同说话人拒绝最难。参赛系统普遍在预训练骨干上叠加语言不变训练——情节原型、对抗/梯度反转、正交投影、层选潜交叉注意力适配器、双 LoRA 语言锚定对抗，以及嵌入/后端/分数级语言补偿。

后端上出现流形约束神经 PLDA 与动态难样本挖掘；数据侧用多语噪声混响增强与零样本 TTS 合成扩语种。排名靠前系统报告约 1.4% 量级 EER，并强调前端去语言后强后端优势可能缩小。

## 论文技术总结

# L-Proto: Language-Aware Episodic Prototypical Training for Multilingual Speaker Verification

- 论文编号：410
- 报告人：Hyung-Seok Oh
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/oh26_interspeech.pdf

## 问题
多语说话人验证中，嵌入常把说话人与语言缠在一起，同说话人形成语言子簇；随机情节采样混语会扭曲原型估计。

## 方法
L-Proto：每情节只从单一语言采样 P 说话人 × K 句，流式缓冲按语构建情节；情节内用支持集均值原型 + 余弦温度 CE。总损失 = 全局分类 + λ·情节原型损失。在 VoxBlink2 预训练骨干上于 TidyVoiceX 微调。

## 实验与结果
TidyVoice 开发集：SimAM-ResNet34 EER 2.88→1.38，ResNet100 3.48→1.18；跨语试验（D/D、D/S）增益最大。ResNet/ECAPA/CAM++ 等多骨干均优于预训练与普通微调。质心分析：跨语同说话人相似度升、同语异说话人降。消融：单语情节优于随机/多语情节；情节采样与原型监督需同用。

## 结论
语言一致情节可稳定多语原型学习、缓解说话人–语言子聚类，在 TidyVoice 上跨骨干一致提升跨语验证。

## 点评
从任务构造而非对抗解耦入手，实现简单且效果清楚。依赖语言标签与语内足够说话人多样性，采样有额外开销；对极端低资源语改进不均匀，自适应情节仍是后续方向。


# Progressive Learning for Robust Speaker Representation

- 论文编号：2097
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/keetha26_interspeech.pdf

## 问题
说话人嵌入在噪声/混响与跨语条件下易编码语言学内容，导致同语异说话人误纳、跨语同说话人误拒。

## 方法
两阶段：Stage1 用 ArcMargin 在 TidyVoice 上微调 ReDimNet-B6，并加大 MUSAN 噪声、RIR、变速增强；Stage2 冻结骨干，训轻量卷积投影网（约 256K 参）用三元组损失拉近同说话人（含跨语正样本）、推开异说话人（含同语负样本）。曾试 GRL 语言对抗但无效故弃用。

## 实验与结果
开发集总体 EER：基线 3.07% → 无适配 ReDimB6 2.70% → Stage1 1.75% → Stage2 1.58%；最难 SS-DL vs DS-SL 由 4.42% 降至 2.52%。盲测 eval-A 9.06%→4.81%，eval-U（未见语）11.60%→7.01%。噪声与混响扰动下 EER 保持较稳；t-SNE 显示跨语同说话人簇更紧、异说话人更分。

## 结论
域内 ArcMargin 适配 + 跨语平衡三元组投影，可在噪声与语言变化下提升说话人表征鲁棒性，并在未见语盲测上显著优于挑战基线。

## 点评
渐进式“先鲁棒分类、再度量塑形”清晰，平衡四类试验对采样很关键。最易条件下有轻微回退；共享多语的说话人簇仍偏近，口音/跨语音素缠结未完全消解。


# Orthogonal Feature Projection and Manifold-Constrained Neural PLDA for the TidyVoice2026 Cross-Lingual Speaker Verification Challenge

- 论文编号：3003
- 报告人：Yuxuan Du
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/du26c_interspeech.pdf

## 问题
跨语种说话人确认中，主流 ASV 训练常忽视语言不平衡，使模型把语言线索与说话人身份纠缠，严重限制跨语种泛化。现有后端把 Neural PLDA 的 P、Q 矩阵当作互不相关的可学习权重，切断了生成式概率约束；而侧重信道补偿的 PLDA-diag 对跨语种仍不足。TidyVoice 2026 正是针对语言无关 ASV 提出的评测。

## 方法
前端以 ResNet221（瓶颈块分布 [6,16,48,3]）+ MQMHA 池化为主干，AAM-Softmax 配合 sub-center 与 Inter-topK。正交特征投影：冻结 ResNet 与 WavLM Base+，将 WavLM 嵌入线性对齐后，用 Gram-Schmidt 分解为与 ResNet 嵌入平行的冗余分量与严格正交的互补分量；正交分量经零初始化门控的瓶颈网络 Φ（tanh）残差加回 ResNet 嵌入，逐步融入跨语种互补信息。后端提出流形约束 Neural PLDA：不直接学 P、Q，而学 Θ={μ,A,ψ}，由特征值向量 ψ 按对角化 PLDA 公式生成 P、Q，自由度从 O(d²) 降到 O(d)，以 BCE 端到端优化并保持 LLR 可解释性。训练用动态难例挖掘：挑当前分最低的同说话人跨语种对、分最高的异说话人同语种对。再加 AS-Norm（top-200 imposter）与开发集上逻辑回归分数融合。

## 实验与结果
训练分 Base（约 20 万说话人，VoxCeleb/VoxBlink/CN-Celeb 等）、Extended（扩至 60 万）、Multilingual（官方 TidyVoice + 自采 2000 人及方言筛出的约 1 万多语种说话人）。发展阶段：官方基线 Dev EER 3.07%；S1 预训练 ResNet 1.29%；加正交投影 1.07%；加流形 PLDA 0.79%；加难例挖掘 0.72%；加 AS-Norm 0.64（Test1/2：1.55%/2.22%）；最终融合 Dev 0.56%、Test1 1.39%、Test2 1.95%。按语种条件拆分时，跨语种目标/同语种非目标 EER（1.40%/1.87%）反而低于纯同语种条件（1.49%/2.45%），说明语言线索被压制。在 42 支队伍中获第 1。

## 结论
作者认为正交投影可抽取与声学监督特征互补、跨语种更稳的身份线索，流形约束 Neural PLDA 在判别优化时仍守住生成式约束，再配合多语难例挖掘可显著抑制语言干扰；最终两测试集 EER 1.39%/1.95% 夺冠。

## 点评
做法同时打前端“语言纠缠进嵌入”和后端“Neural PLDA 偏离生成流形”两端：几何正交分解比简单 concat 更可控，ψ 驱动的 P/Q 比无约束矩阵更不易过拟合。脆弱点在于依赖大规模私有/扩展数据与多阶段 curriculum，以及难例挖掘对语言标签质量的依赖；正交门控若校准不当也可能把有用声学互补当噪声滤掉。


# LaS-LCA: Layer-Selected Latent Cross-Attention Adapters and Margin-Mixup for Robust Cross-Lingual Speaker Verification

- 论文编号：1255
- 报告人：Xu Shen
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/shen26b_interspeech.pdf

## 问题
跨语种说话人确认因语言失配（enrollment/test 语言不同）性能显著下降。VoxCeleb 偏英语，难以反映多语/跨语条件。大尺度 SSL 前端虽强，但整层堆叠或简单平均会引入大量与身份无关的语言/语音内容；在有限 Tidy-X 数据上微调还易过拟合。

## 方法
提出 LaS-LCA：冻结 w2v-BERT 2.0（及在 VoxCeleb2/VoxBlink2 上经 Adapter MFA 进一步说话人优化的权重），用层选择（LaS）只取连续深层段（实验最优为 19–24）。共享潜在交叉注意力适配器：可学习 latent array A（64×128）在所有选定层间共享，作 Key/Value；各层输出经降维投影为 Query，把多尺度特征压到统一说话人潜空间以滤除可变长语言内容。注意力后再接 Expand-Convolve-Project 的 1D 卷积块捕捉局部时频谱依赖。训练阶段仅更新适配器；并用嵌入级 margin-mixup：在说话人嵌入空间插值，并对 ArcFace 目标角按 λ 缩放 margin，以正则决策边界。框架基于 WeSpeaker，MUSAN/RIR/语速扰动增广，AAM-Softmax（margin 0.2，scale 32）。

## 实验与结果
数据：TidyVoiceX 训练 3666 人/370h、开发 808 人/87h，共 40 语种；评测 tv26 eval-A（见语种 enroll / 未见语种 test）与 tv26 eval-U（双方均为 38 未见语种）。开发集：SimAM-ResNet34 基线 EER 3.07%；SSL 初始化 Adapter MFA 约 2.1%；说话人初始化后 LCA/LaS-LCA 明显更好；LaS-LCA（19–24）+ mixup 达 EER 1.40%、MinDCF 0.66。消融：深层 19–24 优于全层与浅层；再缩到 4/2 层变差；kernel=3+mixup 最优 EER 1.40%。官方评测：eval-A 3.70% EER / 0.278 minDCF，eval-U 6.41% / 0.329（基线分别为 9.06%/0.658 与 11.60%/0.607）。

## 结论
作者认为不必用满 SSL 深度，聚焦上层表示可得到更干净的说话人信号；共享潜在交叉注意力加局部卷积，再配合嵌入级 margin-mixup，能在冻结 SSL 骨干下提升跨语种验证，TidyVoiceX 开发集 EER 达 1.40%。

## 点评
核心抓的是“SSL 全层聚合噪声大、跨语数据又少”：层选择把说话人相关深层与浅层音素内容拆开，共享 latent 当瓶颈比逐层独立适配更强制统一说话人空间。脆弱点在于层段依赖该骨干与初始化（SV init 远强于 SSL init），且官方 eval-U 仍明显高于开发集，说明未见语种泛化仍是短板；mixup 收益对 kernel 敏感，需按验证集细调。


# Dual-LoRA: Parameter-Efficient Adversarial Disentanglement for Cross-Lingual Speaker Verification

- 论文编号：2274
- 报告人：Qituan Shangguan
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/shangguan26_interspeech.pdf

## 问题
跨语种说话人确认存在严重的语言–说话人纠缠：最难场景是同说话人跨语种需正确接受、异说话人同语种需正确拒绝。标准对抗解耦（盲目语言判别器）会惩罚与语言相关的说话人区分线索，损害身份判别力。全量微调在有限目标数据上还易灾难性遗忘。

## 方法
Dual-LoRA：冻结预训练骨干，全局注入两路并行 LoRA——Speaker Branch（r_spk 较高，ResNet 为 16，w2v-BERT2 为 32）与 Language Branch（r_lang 较低，分别为 4/16），分别提 e_spk 与 e_lang。Language-Anchored Adversary：共享判别器 D；语言锚点流用 e_lang 做语言分类，对抗流经 GRL 把 e_spk 送入同一 D，使对抗梯度对准真实语言线索而非任意相关特征。损失 L_id（Sub-center ArcMargin）+ λ1 L_lang + λ2 L_adv。三阶段课程：先只训语言（λ2=0），再弱对抗，再加强对抗。推理时丢弃语言支路与 D，把 Speaker LoRA 合并进骨干，零额外开销。

## 实验与结果
单系统/消融仅用公开 VoxBlink/VoxCeleb 初始化，在 TidyVoice 上微调 3 epoch。开发集：官方 Full FT ArcFace 3.07% → Sub-center 2.05% → LoRA No Adv 约 1.6%；SamResNet100 Dual-LoRA 0.98%，w2v-BERT2 Dual-LoRA 0.91%。最坏条件 SS-DL vs DS-SL：基线 5.19% → Ours 1.62%。探针 LID：No Adv 72.71%、Std Adv 55.03%、Dual-LoRA 49.02%，同时 EER 最低。跨 ResNet293/SamResNet100/w2v-BERT2，Dual-LoRA 均优于 No Adv 与 Std Adv。最终提交用内部约 18k 小时/396 语种预训练三骨干，1:1:1 校准后融合：eval-A 2.43%、eval-U 2.84%，相对基线降错约 70%，官方第 3。

## 结论
作者认为双路 LoRA 可在冻结骨干上显式因子化说话人与语言；语言锚定对抗比盲目 DANN 更能去语言、保身份；融合系统在见/未见语种评测上均稳健，获挑战第 3。

## 点评
做法针对的是“对抗去语言时误伤说话人”：用独立语言 LoRA 给判别器提供真语言锚点，比直接从 e_spk 猜语言更可控。脆弱点在于课程 λ 与非对称秩需调参，且最终成绩依赖大规模内部多语预训练；若语言支路表征弱，锚定本身会偏，对抗仍可能抹掉有用相关特征。


# Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models

- 论文编号：1799
- 报告人：Jinghan Peng
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/peng26f_interspeech.pdf

## 问题
说话人确认在语言失配时性能下降：身份线索与语言相关声学特性纠缠。相对在有限、偏语种数据上从头训 SV，利用大规模多语 SSL 预训练模型学到的泛化声学/语音表示，有望得到更语言无关的说话人嵌入；但如何聚合多层、如何稳定训练仍需系统验证。

## 方法
主系统：w2v-BERT 2.0 前端，每层经两层 MLP Adapter 投到 256 维，再做 Multi-scale Feature Aggregation（比较 Mean、层/通道加权、通道/时间拼接、Hierarchical Cross-Attention 等六种），Attentive Statistics Pooling 后投影为 256 维嵌入，AAM-Softmax 训练。三阶段训练：Stage1 冻骨干训下游（全数据、2s、margin 0→0.2）；Stage2 解冻全模型微调；Stage3 仅在 TidyVoiceX Train 上做大间隔微调（6s、margin 0.5）。辅系统：轻量 ReDimNet-B5/B6，SphereFace2-C，两阶段预训练+LM-FT。训练数据含 TidyVoiceX Train、VoxCeleb2、VoxBlink2、CN-Celeb、WenetSpeech 清洗子集、3D-Speaker，及 RIR/MUSAN 等在线增广。开发集做选模与 QMF 校准，分数级平均融合。

## 实验与结果
指标 EER / minDCF（P_target=0.01）。主系统 w2v-BERT 2.0：Dev 1.03%、eval-A 3.34%、eval-U 4.59%；+QMF 后 eval-A/U 为 2.73%/2.84%。ReDimNet-B6+QMF：2.52%/3.43%。融合+QMF：eval-A 2.21%、eval-U 2.99%。PTM 对比（仅 TidyVoiceX Train 微调）：w2v-BERT 2.0 Dev EER 2.09% 优于 Whisper Large-v3、XLS-R、MMS 等。聚合消融：Channel Concatenation EER 最低（2.09%），HCAF minDCF 最好；最终提交选 CC。训练阶段消融：冻前端 1.54% → 全微调 1.14% → +LM-FT 1.03%。

## 结论
作者认为用 w2v-BERT 2.0 作前端加多层聚合与三阶段适配，可构建更可泛化、偏语言无关的 SV；同数据下 PTM 系统在未见语种 eval-U 上强于轻量 ReDimNet；最终融合在 TidyVoice2026 达 2.21%/2.99% EER。

## 点评
路线偏“强 SSL 前端 + 工程化训练课表”，贡献更在系统对比（PTM 选型、聚合策略、三阶段）而非新解耦机制。Channel Concatenation 无额外参数却 EER 最好，说明有时简单融合够用。脆弱点在于 580M+ 骨干算力与大规模多源数据门槛；未见语种仍明显高于开发集，语言纠缠问题主要靠预训练覆盖而非显式对抗压制。


# Language-Invariant Multilingual Speaker Verification for the TidyVoice 2026 Challenge

- 论文编号：2437
- 报告人：Xiaoxiao Miao
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/li26fa_interspeech.pdf

## 问题
多语说话人确认受跨语数据不足与嵌入中语言相关信息拖累。官方 TidyVoiceX 虽多语，但每说话人通常只有两三种语言，语言多样性不够，易学到身份–语言纠缠的表示，削弱跨语泛化。

## 方法
骨干为 w2v-BERT 2.0：各 Conformer 层经 Layer Adapter 降维适配，拼接后 ASP + 线性得到说话人嵌入，LoRA 高效微调。语言不变学习：在嵌入上接语言分类器，经 GRL 做对抗（λ_GRL=λ_lang=0.1），先单独训语言头再联合对抗。合成增广：用 Qwen3-TTS 零样本多语克隆，对最多约 3495 条 >3s 参考音各合成 10 语种×10 句，共约 34.95 万条；文本来自 LibriTTS 经 M2M100 翻译，参考转写用 Whisper-large-v3。训练两阶段：先在 VoxCeleb2/VoxBlink2/3D-Speaker/KeSpeech/CN-Celeb 上大规模说话人预训练（冻→解冻）；再在 TidyVoiceX 上域适应并开 GRL。比较 ArcFace 与 SphereFace2-A/C；推理用 QMF（时长、嵌入范数、SNR、原分等）逻辑回归校准。

## 实验与结果
官方基线 Dev 3.07%、eval-A 9.06%、eval-U 11.59%。仅预训练数据微调已 Dev 2.74%。SphereFace2-C 明显优于 ArcFace；仅 TidyVoiceX 微调的 SF2-C：Dev 0.95%，+GRL 0.937，++QMF 达 Dev 0.893、eval-A 2.458、eval-U 4.451。混入大规模预训练数据对未见语种 eval-U 更有利，对见语种子集更偏域特化。合成数据：t-SNE 显示同说话人合成与真实嵌入接近；但在本设置下加合成未再提升，仅用合成约 1.022% Dev EER，接近真实数据 0.95%，作者认为数据充足时合成–真实域差可能伤性能，低资源时更有价值。

## 结论
作者认为微调大规模 SSL、用 SphereFace2、语言对抗与（低资源下）ZS-TTS 增广可提升多语 SV；GRL 带来适度去语言收益，合成增广在数据受限时更有意义。

## 点评
三条线并列：强 PTM+MFA、GRL 去语言、TTS 扩语种。GRL 与 QMF 的增益清晰但幅度不大；SphereFace2 相对 ArcFace 的提升更醒目。脆弱点在于合成增广在充足真实数据下未兑现收益，说明“更多语种”不等于更好——域匹配与标签噪声同样关键；eval-U 仍明显高于 eval-A，未见语种泛化仍未彻底解决。


# Effectiveness of Language Variability Compensation in Speaker Verification

- 论文编号：3367
- 报告人：Oldřich Plchot
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/mosner26_interspeech.pdf

## 问题
说话人确认研究长期受单语宽带宽数据主导，语言变异对试验分数的影响常被信道/源失配掩盖。TidyVoice 2026 把语言多样性推到前景：同一说话人多语、评测含 38 未见语种。需要系统比较在嵌入端、后端与分数端分别做语言补偿是否有效，以及它们如何交互。

## 方法
嵌入端：（1）在池化后分支加语言分类头与 GRL，多任务 L=L_s(ArcFace)+L_l，迫使共享骨干抑制语言信息；（2）DSU 在卷积特征上扰动通道均值/方差以模拟未见域偏移。后端：PSVM、球形高斯变体 SG-TPSDA，以及用 LDA 投掉主导语言方向（维数在开发集调）。分数端：ResNet18 语言分类器得语言相似度作质量度量，经逻辑回归校准说话人分数。前端含 w2v-BERT 2.0+层适配器+MFA，以及更大的 SimAM-ResNet100；微调数据试 TidyVoiceX、VoxCeleb2、NIST SRE CTS Superset（上采样至 16 kHz）等组合。

## 实验与结果
微调数据：SimAM-ResNet100 在 T+V+C 上 Dev EER 1.50% 最佳；w2v-BERT MFA 仅 T 即 1.50%，加英语主导的 V 反而变差。嵌入端：ResNet 上 GRL+DSU 达 Dev 1.20%；w2v-BERT+GRL 达 0.99%。子列表显示最难的跨语目标/同语非目标（tgt≠, imp=）在 GRL 后显著改善（如 MFA：2.83%→1.58%），最易同语目标/异语非目标则略变差，符合“语言线索被削弱”。后端：非语言补偿嵌入上 PSVM/SG-TPSDA+LDA 很强；但对已 GRL 的嵌入，后端补偿效果变弱，需大幅减小 LDA 维数。提交为 SimAM+PSVM-LN 与 w2v-BERT+SG-TPSDA 的先验加权逻辑回归融合：Dev 0.81%、eval-A 2.53%、eval-U 3.40%。分数端语言质量度量对无补偿系统有帮助（1.28%→1.10%），对已 GRL 系统几乎无增益。

## 结论
作者认为在语言多样场景下显式补偿语言变异至关重要；嵌入端 GRL/DSU、强后端与分数端质量度量可各自带来相近收益，但前端已去语言后，后端/分数端优势会减弱。提交系统 eval-A EER 2.53%。

## 点评
价值在于“整条流水线对照实验”而非单点技巧：证明语言纠缠可在前端净化，也可留给能拆说话人/非说话人子空间的后端消化；两者不可简单叠加。脆弱点在于子列表分析主要基于见语种开发集，未见语种行为未充分展开；MinDCF 在同语非目标子列表上逼近 1 也被作者怀疑部分标签问题，解读需谨慎。

