# ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：8
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕真实约束下的流式 ASR/KWS、持续学习与参数高效适应，以及脉冲网络早退能效。关键词是：开放可复现的流式日语模型、分离前端与干净后端解耦、严格虚警预算下的边缘关键词、无回放持续 ASR，以及口音/说话人流上的 LoRA 变体。

流式与鲁棒性上，CER 分层数据策展对欠表示域有益但多域微调时可能伤性能；在线分离 + 仅干净语音训练的流式 ASR 避免 MCT 对干净语音的损害。KWS 用间隔感知对比正则压低相似伪触发 FRR，并用因果时间关系蒸馏消解非因果教师的因果失配。

持续学习侧从保留方向梯度投影、奇异值尾子空间旋转 LoRA、模块化诊断数据集，到相似度条件有符号正交 LoRA 与按发音方式组织专家的 MoPE-LoRA，共同对抗灾难性遗忘并促进相似说话人/音类迁移。能效方面 First-to-Spike 以输出首峰本身作为决策信号。

## 论文技术总结

# A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR

- 论文编号：3380
- 报告人：Yinchang Yang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26r_interspeech.pdf

## 问题
高性能日语 ASR 常闭源、缺数据细节或仅离线；端侧实时需要流式与可复现的全开放配方，且公开资源偏电视域、讲座/对话覆盖不足。

## 方法
123M FastConformer 混合 RNNT/CTC（CTC 辅助权 0.3）+ cache-aware 多上下文流式（训练采样 [L,R]∈{[70,13]…[70,0]}）。ReazonSpeech ~35K h 预训练，对比全量与 CER 分层策展（丢 CER>20%，三质量带加权）。再在约 507 h 五域渐进微调（含新建 TEDxJP-20h、MSR/BTSJ 过滤等）。

## 实验与结果
五测集平均 RNNT CER 12.4%，优于全开放 OWSM-CTC v4（13.5%）与 ReazonSpeech NeMo-v2（14.1%），参数小 5–8×；RTFx 1220（批）/446（流式）。CER 策展在缺讲座微调时显著帮 TEDx；与多域微调+更深预测 RNN 叠加时反而伤 TEDx。加 TEDx 数据单步可把 TEDxJP-10K CER 从 25.80 降到 13.71；[70,13] 与全句准确率一致，全因果平均升约 1.65 点。

## 结论
首个同时满足权重/数据清单/代码/日志全开放与 cache-aware 流式的日语 ASR；小模型+领域覆盖可打过更大离线开放基线。

## 点评
开放度与流式并重的缺口填得扎实；2×2 策展实验说明“清洗≠总更好”，与解码器容量和微调范围有交互。相对闭源大模型（如 parakeet 10.0%）仍有差距，但在可复现流式赛道上定位清晰。


# Robust Streaming ASR with Decoupled Separation and Recognition

- 论文编号：1503
- 报告人：DeLiang Wang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26h_interspeech.pdf

## 问题
流式 ASR 在噪声、混响与干扰说话人下研究不足；多条件训练（MCT）需大规模含噪数据且常伤干净语音表现。

## 方法
解耦框架：在线分离前端（DPDFNet、因果 oTF-CrossNet；另报全上下文 TF-CrossNet）+ 仅干净语音训练的流式后端。提出 FastMambaformer（FastConformer 中卷积换成 Mamba），并接 NeMo 预训练 FastConformer 与 SimulStreaming。前端与 MCT 基线见相当数据量；推理均零 look-ahead。

## 实验与结果
干净 LibriSpeech 上 FastMambaformer 优于同配置 FastConformer。含噪 LibriSpeech：oTF-CrossNet+干净后端平均 WER 36.1%，优于 noisy-trained MCT（36.9%）；接预训练后端同样受益。CHiME-4 实测：oTF-CrossNet+干净后端 24.56% 优于 MCT 26.17%；大模型+前端可进一步降到约 13.7%。LibriCSS：弱前端 DPDFNet 可伤性能，oTF-CrossNet 降低重叠 WER（如干净后端 26.51→22.93%）。

## 结论
足够强的在线分离可使干净训练流式 ASR 超过 MCT，且前端/后端可独立升级，无需任务专用再训。

## 点评
把稳健性外包给模块化前端，避开“为噪声重训 ASR”的代价，对大预训练模型尤其实用。收益高度依赖前端质量（DPDFNet vs oTF-CrossNet 反差大）；全上下文离线 TF-CrossNet 仍明显更好，流式稳健仍是硬问题。


# Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints

- 论文编号：3545
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ha_interspeech.pdf

## 问题
边缘流式 keyword spotting（KWS）需在严格 false-alarm（FA）预算下保持检测灵敏度。标准 CE 训练的轻量因果模型在 ≤0.5 FA/h 等严苛工作点上，面对语音相似 imposters 时 false rejection rate（FRR）显著恶化；直接对 Unknown 做全局对比聚类会扭曲异质非目标流形。

## 方法
提出 Margin-Aware Contrastive Regularization（MACR），仅作离线辅助目标：对因果 1D-CNN 的 penultimate embedding 做 ℓ2 归一化；intra-class pull 仅作用于目标关键词，分母也只含其他目标样本，避免全局聚类 Unknown/Silence。Margin-aware repulsion 对负样本施加 max(0, cos−m)，并对离线挖掘的 hard negatives（EMA 网络上非目标窗口中目标后验 top-K）加权 α>1。总损失 L_CE+λ L_MACR；部署时丢弃 MACR 分支，参数、MACs、算法时延与 CE 基线相同。

## 实验与结果
在 Google Speech Commands V2（12 类）上，约 150K 参数因果 1D-CNN，连续流事件级协议（50 条 2 小时测试流）。MACR 闭集准确率 95.68%（CE 95.82%）；FRR 在 0.5 FA/h 从 16.32%→7.64%，在 0.2 FA/h 从 29.85%→14.80%（相对降幅约 50%）。消融表明去掉 margin、hard-negative 加权或对 Unknown 全局聚类均使 FRR 变差。DS-CNN Tiny 与 BC-ResNet-1 上也有一致 FRR 下降；Raspberry Pi 4B 上推理时延与 CE 同为约 2.15 ms。

## 结论
MACR 通过目标紧致与 hard-imposter 几何边距改善严苛 FA 下的流式 FRR，且零部署开销。证据限于英文多关键词严格 FA 流式设定；更广语言、自定义唤醒词与远场场景留待后续。

## 点评
核心洞察是 Unknown 不是紧致类，对比学习必须把“目标紧致”与“imposter 边距”拆开；这比直接套 SupCon/ArcFace 更贴 always-on FA 约束。脆弱点在于 hard-negative 挖掘依赖 EMA 与合成流协议，真实自然录音与自定义唤醒词上的边距是否仍有效有待验证。


# Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting

- 论文编号：3546
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ia_interspeech.pdf

## 问题
端侧流式 KWS 要求严格因果、零 lookahead 学生模型；从非因果教师（如 AST）做中间层蒸馏时存在 causality mismatch：教师逐步特征已含未来上下文，点式回归会与学生可实现感受野冲突，损害连续长时推理鲁棒性。

## 方法
提出 Causal Temporal Relation Distillation：用无参 Adaptive Average Pooling 将师生时序特征对齐到统一长度 L（默认 24），行内 ℓ2 归一化后构造关系矩阵；对教师关系矩阵施加下三角因果掩码，只蒸馏历史拓扑（Ours）。离线双向变体 Ours-Bi 在保留 L_rel 历史锚点基础上，额外用全矩阵 L_bi 作 privileged prior。联合目标含 CE、logits KD、L_rel 与可选 L_bi；关系匹配仅离线计算，推理仍为因果 1D-CNN。

## 实验与结果
GSC v2 上，冻结 AudioSet 预训练 AST 教师（约 85M），学生约 150K/5.2M MACs。Scratch 95.12%，Vanilla KD 95.74%，Feature KD 95.45%，Relational KD 96.08%，Ours 96.53%，Ours-Bi 96.91%。流式 FRR@1.0 FA/h：Scratch 8.52%→Ours-Bi 4.15%。消融显示仅 L_bi 不如有因果锚点的组合；L=24 优于无 pooling 或过平滑的 L=12。Raspberry Pi 逐步时延约 0.15 ms，各学生变体部署成本相同。

## 结论
用因果可实现的时序拓扑蒸馏替代点式特征回归，可缓解 causality mismatch，并在闭集准确率与连续流 FRR 上取得最佳结果，且无额外部署开销。结论限于 GSC v2、AST→1D-CNN 设定。

## 点评
把“错在绝对特征含未来”转成“只对齐可实现的相对关系，再软用全拓扑”是清晰的因果蒸馏设计。强项是关系构造与推理解耦；风险在于依赖特定教师与合成流协议，且 L 的子音素尺度是否跨域通用需再验证。


# Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR

- 论文编号：2309
- 报告人：Seunghee Ma
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ma26d_interspeech.pdf

## 问题
大规模预训练 ASR（如 Whisper）顺序域适应时会发生灾难性遗忘；严格 rehearsal-free 设定下仅有上一模型参数可用。标准 LwF 对所有 token 等权蒸馏，不确定教师输出会污染保留方向，且监督梯度与蒸馏梯度冲突时会损害保留。

## 方法
以冻结上一模型作教师：用教师分布熵构造 token 级权重 λ_t，抬高低熵（自信）token、压低高熵 token，得到熵引导蒸馏损失。将蒸馏梯度视为 retention direction；当 cos(g_CE, g_distill)<0 时，用系数 η 投影掉监督梯度中与蒸馏方向冲突的分量。基于对角 Fisher 分析冻结 encoder、只微调 decoder。顺序适应 LIB→AMI→TED→SPG。

## 实验与结果
Whisper Large-v3，η=0.75。最终平均 WER 8.12%，相对 LwF decoder-only（8.75%）降 7.2%，相对 FT decoder-only 降 15.9%；BWT 从 LwF 的 −4.63 改善到 −2.82。无 replay 仍优于带 1h TED 缓冲的 GEM/ER。Common Voice 多语退化平均绝对增幅 0.95%，相对 LwF（1.96%）降 51.5%。消融显示投影主推保留与泛化，熵加权在投影下略恢复目标域适应；η 可调保留–适应折中。

## 结论
熵引导 token 蒸馏 + 保留投影 + encoder 冻结，在 rehearsal-free 连续 ASR 适应上优于 LwF，并更好保住多语能力。η 提供显式折中控制。

## 点评
把蒸馏梯度当作可投影的保留方向，比固定 λ 的 LwF 更贴近“冲突时该保什么”的优化问题。代价是投影会牺牲新域适应（AMI WER 上升），且依赖教师在当前域输入上的输出质量；Fisher 仅支撑 encoder 冻结假设，未与 LoRA 等 PEFT 路线直接对比。


# Parameter-Efficient Continual Learning for Automatic Speech Recognition

- 论文编号：3169
- 报告人：Steven Vander Eeckt
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/eeckt26_interspeech.pdf

## 问题
语音基础模型下游适应面临参数量大与顺序微调灾难性遗忘；ASR 上参数高效持续学习（PECL）研究相对 NLP/视觉更少，且不少方法未显式保护相对初始预训练模型的性能。

## 方法
提出 Continual SSVD（CSSVD）：对线性层权重做 SVD，按奇异值分为 head（高能）与 tail（低能）；只在 tail 学习近似旋转 G=I−2K（省略显式 rescaling）。新任务前重算 SVD 以更新 head/tail 划分；多任务时用权重平均（α=1/(i+1)）合并当前解与新任务适应解，保护主导方向并降低共享 tail 内干扰。推理无需任务 ID。

## 实验与结果
OWSM v3.2 small（约 366.7M），约 8.9M 可训参数。实验 1：预训练语 ENG/DEU/ESP 为 T0，再适应 CGN 的 NL→VL；CSSVD 平均 WER 18.33、BWT −1.9，显著优于 LoRA、SSVD、OPLoRA、MiLoRA、BiLoRA、EWC-LoRA、LoRA+FTA 等。实验 2：VL→方言 DVL，CSSVD 平均 24.82、BWT −2.2，仍最佳。消融表明限制在 bottom-k 方向最关键，平均步骤必要，显式 rescaling 几乎无增益。

## 结论
在尾空间做近似旋转并跨任务平均，可在 ASR PECL 上同时降低遗忘与平均 WER。局限是各层均匀分配适应容量，未来可按层选择性分配。

## 点评
相对“改 top-k”（SSVD）改为“只动低能尾并平均”，直接对准保护预训练主方向；实验覆盖多类从 NLP/视觉迁来的 PECL 基线，证据较全。脆弱处在于困难方言任务上新任务 WER 仍高于无正则 LoRA，且 head/tail 重划分依赖每任务后完整 SVD。


# MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition

- 论文编号：2111
- 报告人：Theresa Pekarek Rosin
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pekarekrosin26_interspeech.pdf

## 问题
现有 ASR 鲁棒性数据集/基准常孤立考察噪声、口音或障碍等因素，难以反映真实共现与随时间累积的分布漂移；也缺少用持续学习诊断预训练 ASR 在何处遗忘的可控资源。

## 方法
发布 MoDiCoL：用 Taguchi L27 正交阵与 foldover 得 108 种因子配置×75 样本=8100 条（约 18.79 h，其中合成 14.08 h）。三因子族为语言内容（域/风格）、说话人（年龄/口音/健康/停顿/不流畅）、声学环境（噪声类型/SNR/距离）。真实与 XTTS-v2 合成语音经去噪、不流畅/损伤/停顿、混响距离与噪声注入管线对齐配置。CL 课程：t0=LibriSpeech 控制设定，再依次 Acoustic、Speaker、Linguistic、Compound 漂移；评估 ER、RLR、OGD 三种策略（whisper-small.en，online/streaming）。

## 实验与结果
未适应时 t0 A-WER 7.42，t1/t2/t3 分别升至 47.62/87.28/141.73，t4 为 43.37；合成子集整体好于真实。课程上 ER-10% 最稳：A-WER 17.31±0.48，优于 JOINT（27.24）与 FT（34.14），FM 接近 0；RLR 遗忘大，OGD 的 AI-WER 最好（21.19）且任务梯度近正交。顺序引入漂移提升可塑性，但除 ER-10% 外 FM/BWT 方差大，任务顺序敏感。

## 结论
MoDiCoL 支持对多因子漂移下 ASR 适应与遗忘做诊断；适度 replay 最利于跨漂移保持鲁棒性，梯度子空间干扰是遗忘因素之一。数据与管线已放 Hugging Face。

## 点评
价值在“可控共现因子 + CL 课程当诊断工具”，而非再堆单一噪声/口音集。合成占比高、部分配置靠损伤仿真，外推到真实共现分布时需谨慎；ER 优于 JOINT 的结果有启发，但强依赖缓冲与任务顺序。


# SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation

- 论文编号：3243
- 报告人：Ye-Eun Ko
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ko26b_interspeech.pdf

## 问题
部署 ASR 面临说话人流式到达、无可回顾历史数据的 rehearsal-free 持续说话人适应；O-LoRA 等任务无关正交分离可抑干扰，但会阻断声学相近说话人之间的正迁移。

## 方法
提出 SCOLoRA：每说话人学新 LoRA 分支并合并进骨干；用 ECAPA-TDNN 嵌入余弦相似度 S_{i,t}，经 sigmoid 先验与轻量 router 映射为有符号系数 λ(S)：相似时 λ<0 鼓励子空间对齐，不相似时 λ>0 强制正交。对 LoRA 基做单位 Frobenius 投影以稳定有符号重叠目标。总损失为 ASR 损失 + Σ λ(S)∥A_i^⊤ A_t∥_F²。

## 实验与结果
Whisper small + LoRA（r=4）于 TEDLIUM2/3 与 CHiME3。TEDLIUM3 上 SCOLoRA 测试平均 WER 4.11%、dev 4.41%、forgetting 0.05，优于 SeqLoRA（4.35/0.10）、O-LoRA（4.33/0.19）及 EWC/L2P/InfLoRA/GainLoRA。跨库一致改进；CHiME3 平均 WER 22.59（SeqLoRA 29.32，O-LoRA 28.09）。消融显示有符号加权与 router 优于仅正向相似度条件，对 τ∈{0.20,0.25} 不敏感。

## 结论
按说话人相似度调节对齐/分离，可在无回放持续说话人适应中同时降低 WER 与遗忘。

## 点评
把 O-LoRA 的硬正交改成相似度调制的有符号正则，切中说话人流“有的该共享、有的该隔离”。依赖说话人编码器质量与合并后单模型容量；长流上存储全部历史 A 基的开销与干扰累积正文未充分展开。


# Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition

- 论文编号：322
- 报告人：Anmol Guragain
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dahal26_interspeech.pdf

## 问题
口音英语 ASR 性能易降；按口音分配 MoE/适配器会使专家数随口音增长，且忽略口音差异常体现为系统的音素实现扭曲这一共享结构。

## 方法
提出 MoPE-LoRA：固定 6 个按发音方式划分的 LoRA 专家（元音、塞音、擦音、塞擦音、鼻音、流音/滑音），插入 Conformer 自注意力 Q/K/V。帧级混合路由：冻结音素 CTC（LibriSpeech 训练）提供监督硬分配，与可学习门控混合（β），top-2 激活。专家跨口音共享，测试无需口音标签。辅助 load-balancing 与 router Z-loss；主损失 CTC。

## 实验与结果
L2-ARCTIC（约 24 h，6 口音），说话人与句子双重 disjoint。NeMo Conformer CTC Small。最佳 MoPE-QKV（层 6–16）WER 10.43%，优于 Full FT 12.80%、Single LoRA-QKV 11.33%、MAS-LoRA 11.77%。零样本留一口音：平均 WER 9.98%，相对 Single LoRA（11.38%）相对改进 12.3%。TIMIT MI/t-SNE 支持中层最富音素信息，故聚焦 6–16 层；跨域音素 top-1 仅 36.04%，故用 top-2 补偿。

## 结论
按音素范畴分解适配、混合路由，可在固定专家数下提升多口音与未见口音识别，且参数高效。

## 点评
用发音方式归纳口音变异，比“一口音一专家”更可扩展；音素监督在口音上不准时靠学习门控补偿是务实设计。边界在于依赖额外音素模型与英语发音学分类，对更强口音或非英语音系的迁移仍需验证。


# First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks

- 论文编号：1858
- 报告人：Siqi Cai
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26j_interspeech.pdf

## 问题
SNN 本具事件驱动低时延潜力，但常跑满整段序列；现有 early-exit 多用 softmax 置信阈值等非脉冲准则，偏离纯事件范式并增加部署复杂度。

## 方法
提出 First-to-Spike（F2S）：输出层每类一个 LIF 神经元，首个发放脉冲的类即为预测并立即停算；无脉冲则回退到最终膜电位 argmax。加入可学习侧向抑制 WTA 电路加速竞争。Hybrid Temporal Training（HTT）含加权 TET 分类损失、时间间隔 margin 损失与正确类发放时刻效率正则。

## 实验与结果
GSC V2：F2S Acc 92.89%、ADT 63.68、能耗 2.75 µJ，优于 ED-sKWS（90.14%/66.07/2.85 µJ）。SEED：79.35% Acc、ADT 3.06；SEED-IV：71.60%、ADT 5.45，均高于 Sparch 与 ED-sKWS 且更低时延。消融：仅 F2S 规则已有 early-exit；WTA 大幅提准，HTT 进一步降 ADT，二者合用最佳。

## 结论
脉冲本身可作为可靠决策信号；F2S+WTA+HTT 在语音指令与 EEG 情感识别上同时提升准确率并降低时延/能耗。未来需考察 SNR 鲁棒性及与异步神经形态传感器耦合。

## 点评
把 early-exit 内化为输出层“赛跑发脉冲”，比外挂置信阈值更贴 SNN 硬件。强项是跨语音与 EEG 一致；脆弱点包括无脉冲回退仍依赖满时序、以及能耗按 CMOS MAC/AC 估算，真实神经形态芯片开销可能不同。

