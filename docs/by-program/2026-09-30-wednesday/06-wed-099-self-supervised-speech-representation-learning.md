# Self-supervised Speech Representation Learning

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：8
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦自监督语音表示的可解释性、任务适配与部署效率。一方面深入剖析 WavLM 等模型中声学特征的冗余与多义性，说明稀疏神经元消融不足，需要子空间级干预；另一方面把韵律、口吃等多任务信号显式注入或联合建模，强化情感与流畅性相关下游能力。

联邦与边缘场景推动自适应微调：早期退出与按深度部分聚合应对算力异构与任务所需表示深度差异。离散令牌路径则在推理阶段用软分配缓解硬量化信息损失，训练仍可保持硬离散效率。低资源域适配方面，出现可端到端训练的硬 Gumbel-Softmax 层选择器，结合 BEST-RQ 目标自动挑选 Whisper 编码器层。

总体趋势是：SSL 骨干仍是通用底座，但研究重心转向“表示里到底编码了什么、如何在隐私/算力约束下高效适配、以及离散接口如何在推理时更表达力强”。

## 论文技术总结

# Causal Redundancy in Speech Representations: The Hydra Effect and Limits of Sparse Disentanglement in WavLM

- 论文编号：3316
- 报告人：Patalee Narasinghe
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/narasinghe26_interspeech.pdf

## 问题
WavLM 等 SSL 语音模型如何编码低层声学属性仍不清晰；线性探针只给相关证据，原始神经元又高度多义（polysemantic），稀疏自编码器在语音连续冗余域能否真正因果解耦尚待检验。

## 方法
在 WavLM-Base+ 上：用线性探针与 SHAP 做层/神经元定位；训练 JumpReLU SAE（8192 latents）试图解耦；对 top 重要 latent 做消融测因果；再用 INLP 擦除整段线性子空间。声学标签为 openSMILE GeMAPS（F0、Loudness、AlphaRatio 等），数据为 RAVDESS + CREMA-D + TIMIT，说话人无关划分。

## 实验与结果
声学特征在早期层（尤其 Layer 1）线性可解，打乱标签基线很低。原始神经元与 SAE 均见 Hydra 效应：去掉 top-50 重要维后 Pitch/Loudness 的相对 R² 仍约 97–99%。INLP 子空间擦除可对目标特征造成 >94% 的 R² 下降；Loudness 擦除高度选择性（旁路跌 <1.5%），而 spectral 特征之间交叉跌幅 >75%，说明共享子空间。

## 结论
连续声学特征在 SSL 中呈分布式但可在子空间层分离；离散 neuron/latent 消融不够，需要子空间级干预做机制解释。

## 点评
把 LLM 式 SAE 可解释性搬到语音后，用 Hydra 效应点出连续声学流形的冗余本质，再用 INLP 证明“可分离≠可单点消融”。强在因果干预设计清晰；脆弱在主要看 Layer 1 与线性探针可读性，非线性纠缠与更高层语义未充分覆盖。


# Prosody-Aware Speech Representations for Emotion Recognition under Pragmatic Ambiguity

- 论文编号：3486
- 报告人：Yeonwoo Park
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/park26l_interspeech.pdf

## 问题
SER 常用 STT 取向编码器（如 Whisper）学语义/频谱表示，却未显式保留韵律；在语用歧义（如同句“Geurae”可因语调表同意/讽刺等）下，Hamming 等粗指标会掩盖模型真实差距。

## 方法
冻结 whisper-large-v3-turbo，提取帧级隐表示；用 Parselmouth/Librosa 得到阈值化 F0 与能量，时间对齐后与编码器输出拼接并投影，再经两层 Transformer + 线性头做 59 类多标签情感分类。另建未见过的 Pragmatic Ambiguity Resolution（PAR）评测：从韩语对话视频中筛出多模态标签与文本单模态不一致、且与音频一致的 1000 句。对比文本/SSL/融合模型及同骨干有无韵律、有无上下文（±5 句）。

## 实验与结果
AI-Hub 韩语情感风格数据（约 457h）训练验证。Hamming 各模型都约 96–98，差距被压缩；注入 F0+能量后 Subset 准确率 12.46→26.39（+13.93%p），PAR 21.00→32.60（+11.6%p），超过多数基线并略优于 GPT-4o mini（31.10）。同骨干下上下文增益小于韵律（Subset +4.83%p、PAR +1.6%p）。较小 Whisper-base 上韵律收益有限。

## 结论
语用歧义下瓶颈在表示是否保留韵律，而非单纯模型规模；显式注入 F0/能量可显著缓解 STT 编码器的韵律抑制，且粗粒度指标不足以诊断该问题。

## 点评
贡献主要在诊断设定（PAR）与同骨干对照，方法本身是冻结编码器后的韵律拼接，简单但能直接暴露 STT 表示缺口。结论依赖韩语数据与特定歧义定义；韵律只进分类头、不改 Whisper 内部注意力，上限仍受冻结骨干约束。


# DysfluentNet: Joint Stuttering Event Detection and Dysfluency-Aware Transcription via Hierarchical Self-Supervised Learning

- 论文编号：696
- 报告人：Mohankumar Muthu
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/muthu26_interspeech.pdf

## 问题
口吃检测与转写常拆成独立系统；标准 WER 用流畅参考会惩罚忠实保留不流畅的系统；多任务耦合与困难样本课程策略在口吃场景仍不足。

## 方法
DysfluentNet：冻结 WavLM-Large，学层加权和；检测头用 attentive pooling + 六类多标签 focal loss（BLK/PRO/SR/WR/INT/FLU）；转写头为 BiLSTM + 扩展词汇的 SA-CTC，经 cross-attention gate 用检测 logits 条件化解码，并加对齐一致性项。按 SEP-28k 标注者 Fleiss’ κ 分五档课程，由易到难扩展训练集。联合损失 `L_det + β L*_CTC`。

## 实验与结果
SEP-28k 检测 macro F1 72.4（相对最佳公开基线 LLM-Dys +6.8）；FluencyBank 二分类 F1 81.5。转写 DI-WER 18.3（相对 SSDM 2.0 −4.1），标准 WER 13.8。消融：无课程 −3.3 F1；无 SA-CTC 条件/对齐损害 DI-WER；换 wav2vec 2.0 骨干亦下降。少数类 BLK/SR 提升最大。

## 结论
共享冻结 SSL、检测条件化 SA-CTC 与标注一致性课程，使检测与不流畅感知转写互相增益，并在 SEP-28k/FluencyBank 上刷新报告指标；目前仅英语。

## 点评
把检测当 soft prior 注入 CTC、并用 DI-WER 对齐“保留不流畅”目标，系统设计闭环清楚。脆弱点是对齐窗固定、编码器全冻、评测说话人规模有限，以及课程依赖众包 κ 分层质量。


# Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations

- 论文编号：2122
- 报告人：Xin Guo
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/guo26c_interspeech.pdf

## 问题
联邦学习下微调 SSL 语音模型时，客户端算力差异会造成掉队，而不同下游任务所需表示深度也不同；全模型统一更新既低效又难在弱设备上跑通。

## 方法
以 Wav2Vec 2.0 Base 为骨干，在 Transformer 第 3/6/9/12 层挂早期出口预测头。客户端按本地资源与任务复杂度选最大训练深度 `L_max`，只前向/反向到该层。服务器做层向、深度加权的部分聚合：仅对训练过该层的客户端加权平均（权重含本地数据量与深度），使浅层由更多客户端更新、深层由高资源客户端精炼。

## 实验与结果
在 SUPERB 式五任务（KWS、ASR、ER、SID、ASV）上评测。同构联邦与集中式均显示最优出口因任务而异（如 ASR 偏好第 9 层，KWS 常偏好第 6 层）。异构深度设定下，层向部分聚合优于普通 FedAvg，部分任务甚至超过同构最优深度联邦（如 ASR test-clean 8.79 vs FedAvg 9.21；SID 15.30 vs 17.50）。深度从 12 降到 3 层可显著降低客户端显存（如 KWS 约 −43%）。

## 结论
早期出口 + 深度感知部分聚合可在异构联邦中协同训练 SSL 语音模型，兼顾效率与性能，并缓解掉队。

## 点评
抓住的是联邦里“设备异构 × 任务所需深度不同”的交叉约束，用弹性深度比单纯压缩参数更贴合 SSL 层级结构。脆弱点在于出口集合与任务最优深度仍需经验配置，ASV 依赖 SID 全局模型间接评估，真实边缘端通信/能耗未充分展开。


# Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference

- 论文编号：1668
- 报告人：Kentaro Onda
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/onda26_interspeech.pdf

## 问题
SSL 离散 token 压缩好、训练省，但硬量化丢信息，下游相对连续特征常变差；HuBERT-Soft 等虽软化表示却失去离散压缩优势且需额外微调 SSL。

## 方法
训练下游模型时仍用 k-means 硬离散；推理时按特征到各质心距离做 softmax 后验，对 token 嵌入做期望加权求和再送入下游。温度 `τ` 可按任务调、无需重训。可与多层码本加权叠加。

## 实验与结果
HuBERT/WavLM large 第 21 层，`K∈{128,1024,4096}`。ASR（LibriSpeech-100h 训）：hard/soft 全面优于 hard/hard；ERJ 非母语上甚至可超过连续特征（如 WavLM K=4096：38.8 vs cont. 38.9）。合成（LJSpeech HiFi-GAN）：重建与 TIMIT→LJ 的 VC 多数指标改善，SpkSim 仍保持离散去说话人优势。嵌入分析显示音素类内方差下降、可分性比（inter/intra）上升。`τ` 过小近硬分配、过大近均匀，均损害 WER。

## 结论
仅在推理做软分配，可在保留训练压缩的同时提升 ASR/合成，并改善跨域与音素可分性。

## 点评
改动极轻但抓住“训练压缩 vs 推理信息量”的不对称；对域外与非母语尤其有用。脆弱在于最优 `τ` 依赖验证集搜索，训练仍是硬标签，分布偏移大时软后验质量受质心与 SSL 层选择制约。


# Gumbel-BEARD: Automatic Layer Selection for Self-Supervised Adaptation of Whisper in Low-Resource Domains

- 论文编号：825
- 报告人：Abeer Alwan
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26o_interspeech.pdf

## 问题
Whisper 等基础模型在低资源域（儿童语音、方言）因域偏移与标注稀缺而退化。BEARD 用 BEST-RQ 自监督适配编码器，但预测层需人工穷举搜索，大模型代价高且固定层未必跨域最优。

## 方法
Gumbel-BEARD：在 BEARD 两阶段流程上，用可学习 logits + hard Gumbel-Softmax（STE）每步离散选择编码器预测层；温度从 5.0 退火到 0.1 以先探索后集中。无标注阶段做 BEST-RQ 量化损失与师生蒸馏（内层+输出）；再与解码器在有限标注上联合微调。硬选择优于对各层软加权。

## 实验与结果
MyST：Whisper-small 上 10h 标注达 9.35% WER，接近全量 133h SFT（9.34%）；全量达 8.51%。Whisper-medium 全量 8.21%（报告优于先前 8.50%）。OGI Spontaneous 域内 11.06%；用 MyST 跨域适配后 11.15%。CORAAL 方言：small/medium 相对 SFT 有显著相对下降（如 medium test 9.81→9.25）。适配约 1 GPU-hour，远低于 BEARD 穷举层搜索。PWCCA 显示相对原编码器知识保持更好。

## 结论
可训练的硬层选择使无标注 Whisper 域适配自动化且更省算力，在儿童与方言低资源设定上刷新/逼近 SOTA，并具跨域迁移能力。

## 点评
把“选哪一层做 SSL”从超参搜索变成可微离散路由，切中 BEARD 痛点。硬选择避免不同抽象层梯度混杂是关键设计。脆弱点是仍依赖 BEST-RQ 超参默认配置、温度退火日程固定，且主要验证 Whisper 编码器–解码器结构。

