# Robust ASR: Hallucinations and Biases

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：8
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场主题是稳健 ASR：幻觉检测与缓解、群体偏见、儿童/老年等困难域，以及多说话人场景下的识别与说话人归属。共同背景是大模型 ASR（尤其 Whisper 系）在静音、非语音与长尾实体上仍会“流利地错”，且微调数据配比未必能纠正预训练已固化的偏差。

幻觉研究从内部谱动力学理论（分散→吸引子相变）、解码器中间层探测，到无需改模型的音频锚输入技巧，形成“理论—检测—推理时缓解”链条。专有名词则走 ASR 后处理多视角音素—语义检索接地。偏见与域方面，性别组成实验强调预训练掩盖微调配比效应；儿童零样本 SSL 层误差结构显示问题在声学表征而非可恢复语言不一致；WildElder 提供野外中文老年语料基准。

多说话人侧，端到端 LLM 需在有限真实数据下平衡 ASR 与 diarization；另一工作用说话人切换 token 掩码，使性能不随训练中未见的切换次数崩塌。整体趋势是：稳健性越来越多地被当作可诊断、可接地、可与说话人建模联合优化的系统问题。

## 论文技术总结

# From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales

- 论文编号：1420
- 报告人：Ivan Viakhirev
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/viakhirev26_interspeech.pdf

## 问题
Whisper 等大 ASR 在静音/噪声/对抗下会产生与声学脱节的幻觉；WER 与 token 概率难预警。需从内部表征几何解释尺度依赖的失效机制。

## 方法
提出 Spectral Sensitivity Theorem：层增益 ρ、对齐 κ、谱间隙 ξ 决定语境 Jacobian 进入 Regime I（ρ<1，早期声学注入指数衰减）或 Regime II（对齐+增益导致 rank-1 吸引子）。用 SPI 观测量：有效秩 Neff、谱衰减 α、Kirchhoff 指数 Kf。在 LibriSpeech 构造 Hell 对抗集（3.5× 时伸、6 说话人混、0dB 噪声；仅 WER>0.5），分析 Tiny/Small/Large-v3-Turbo 的 Cross/Self-Attn 与 FFN。

## 实验与结果
Small Cross-Attn 谱尾 Neff 降 13.40%（Regime I）；Large Self-Attn Neff 降 2.34% 且谱硬化（Regime II）。相位图上 Tiny/Small 高秩低 α，Large 低秩高 α。作者强调 Regime II 描述的是自信而非正确，仍需外部标签区分真假。

## 结论
幻觉随尺度从「信号弥散」转向「吸引子锁定」；大模型幻觉更像过度结构化的内部先验投影。未来拟扩展到 Canary/OWSM 并用谱正则做检测/抑制。

## 点评
把幻觉从「文本症状」拉回谱几何，对「越大越稳」直觉是有力修正。κ 未直接测、仅从硬化/压缩反推，理论–实验链条仍有跳跃；但尺度分叉现象本身很清晰。


# Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition

- 论文编号：2666
- 报告人：Abhijit Sinha
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sinha26b_interspeech.pdf

## 问题
成人预训练 SSL 零样本迁到儿童语音时，常只比全局 WER；相近 WER 是否对应相似错误结构、层是否句级最优、错误能否被 LLM 纠正，仍不清楚。

## 方法
冻结 Wav2Vec2/HuBERT/Data2Vec Large 各层，作 Kaldi DNN-HMM 声学特征；仅用成人数据训（英：WSJCAM0；美：Mini LibriSpeech），测 PFSTAR 与 CMU Kids。分析 S/D/I 比例；句级 oracle 选最低 WER 层；用 Mistral-7B-Instruct（零样本与 LoRA 文本微调）做后处理纠错。

## 实验与结果
PFSTAR 最优 WER 约 5.15–5.69%，层间跨度可达 9–13%；CMU Kids 最优约 21–22%，最差可至 86%。PFSTAR 插入相对更多，CMU Kids 替换主导；成人 WSJCAM 几乎无插入。LLM 纠错几乎不改假设；LoRA 文本微调反而恶化。Oracle 增益：PFSTAR 约 1.3–1.6%，CMU Kids 约 5–6%，且不稳定性高 4–6 倍。

## 结论
相近最优 WER 掩盖层间错误结构差异；域差越大层互补越重要；儿童零样本错误主因是声学表征而非可文本修补的语言不一致。

## 点评
把「选一层」拆成错误结构/句级 oracle/可恢复性三条轴，比刷表更有设计含义。LLM 几乎无效强化了「先改声学」的结论；CMU Kids 高不稳定性是自适应层选择的直接动机。


# Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms

- 论文编号：3047
- 报告人：Seshan S
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/s26_interspeech.pdf

## 问题
性别差距常被归因于训练数据失衡，并通过在性别可控子集上微调预训练 ASR 来检验；但预训练语料性别分布未知，微调能否真正暴露「组成→差距」关系存疑。

## 方法
三数据集（LibriSpeech clean、Indic TIMIT、Common Voice v3）× 11 种男:女比例（0–100%，步长 10%）× 四系统：微调 Wav2Vec2、SPRING Wav2Vec2、Whisper Medium，以及从零训 Kaldi TDNN-HMM（LF-MMI）；每配置训练时长上限 71.36h，固定测试集与外部 trigram LM。共 132 条件。用 Demographic Disparity Score DDS=100×(WER_f−WER_m)/WER_m。另在 LibriSpeech 极端比例训 Zipformer 验证。

## 实验与结果
Kaldi：DDS 随组成强且可预测（Indic TIMIT 从 +43.1 到 −37.2）；Zipformer 极端比例亦反转（−9.3→+39.4）。三预训练系统 DDS 波动小且无一致方向（多在约 ±12 内），50:50 近零不等于对组成敏感。微调性别配比无法消除如 LibriSpeech 上 Whisper 持续的女性劣势。

## 结论
组成效应在从零训练中真实存在；预训练表征掩盖了微调阶段的组成信号。仅平衡微调数据不足以缓解预训练 ASR 的性别差距，需表征级干预。

## 点评
用从零系统当阳性对照，方法上干净地拆开「效应是否存在」与「微调能否测到」。对依赖微调性别配比做公平性结论的工作是直接证伪；范围仍限英语与二元性别标注。


# Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition

- 论文编号：1124
- 报告人：Naijun Zheng
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26b_interspeech.pdf

## 问题
多人 ASR 需「谁说了什么」；流水线解耦语义与说话人，端到端 LLM 又常依赖大规模会议标注。重叠区易诱发重复幻觉，ASR 与 diarization 训练难平衡。

## 方法
双编码器：SenseVoice-small（语义，多层拼接+适配器）与冻结 Campplus（多块时长 400/200/100ms 统计后卷积对齐）。特征融合比较语义-only、特征维拼接、时间维拼接、时间交织（每 20 帧/~1.2s）。标签含 `<SC>`+说话人 ID。段长加权说话人 CE；重叠高 CE token 用自适应阈值 Tmask=max(Avg(CE),2.0) 屏蔽。多阶段：ASR→双人对话→拼接至 8 说话人→AliMeeting/Aishell4 微调。后端 Qwen2.5-0.5B-Instruct，总约 0.7B。

## 实验与结果
时间交织 + mask 最优：AliMeeting Test CER/cpCER 23.61/27.16，Aishell4 Eval 17.18/19.98；相对开源流水线约 18%/24% 相对提升（摘要）。mask 相对 cpCER 增益约 8.5%/6.9%。去掉说话人损失、mask 或 ASR 损失均变差。说话人特征可下采样至约 25% 帧仍可接受。

## 结论
有限真实会议数据下，交织融合 + 段感知说话人损失 + 重叠高损屏蔽可平衡 ASR 与归属，减轻幻觉。未来拟做说话人注册与更长时戳。

## 点评
把重叠幻觉归因于「高损 token 主导反传」并做自适应屏蔽，是很具体的训练诊断。0.7B 相对 SpeakerLM 大数据设定的可比性有测试切分差异，但结构消融本身说服力强。


# Multi-Talker ASR Unaffected by Speaker Change Count

- 论文编号：1582
- 报告人：Naoki Makishima
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/makishima26_interspeech.pdf

## 问题
自回归多人 ASR 用说话人切换 token 串接转写；推理时切换次数超过训练分布会漏说话人、CER/SCCA 崩坏。切段过短又损语义连续性。

## 方法
在 Transformer 解码器自注意力中用说话人切换 token mask 替代纯前瞻 mask：对 `[st]`（及 SOMSRED-SVC 中的时间/说话人 token）置 −∞，禁止其他 query 读到已出现的切换计数；训练时另以概率 r 随机 mask 文本 token，阻断从语境推断话轮数。推理只 mask 切换类 token。应用于「ASR+[st]」与联合 diarization 的 SOMSRED-SVC。

## 实验与结果
CSJ 伪多人混合/拼接；训练最多 2 次切换。3 SC 非重叠：基线 CER 13.5%/SCCA 59.5%，Ours(r=0.6) 5.9%/96.3%，接近含 3 SC 的 oracle。4–5 SC 时基线大量少报切换（CER 22–28%），Ours 多数正确。SOMSRED-SVC 上 r=0.4 时 3 SC CER/SCCA 亦明显改善，TER/EER 几乎不降。

## 结论
屏蔽切换计数语境可使自回归多人 ASR 外推到训练未见的切换次数，而无需为更长话轮重造数据。

## 点评
针对「从历史 `[st]` 计数」这一捷径做结构性封堵，比数据扩容更干净。r 过大伤训练；带时间/说话人 token 时与 oracle 差距仍大，说明被 mask 的结构信号越多越难逼近。


# WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations

- 论文编号：102
- 报告人：Hui Wang
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26_interspeech.pdf

## 问题
中文老年语音多在受控环境采集，话题/自发度/信道多样性不足；野外自动管线对老年声又易出错，缺带细粒度人工标注的真实场景语料。

## 方法
WildElder：从在线视频（关键词检索 + 老年创作者频道）收集，人工切分、转写与元数据标注（年龄段、性别、口音强度轻/中/重）。质检要求抽检准确率 ≥95% 等。最终 23,701 句、33.7 小时（619 视频）；说话人级划分训/开/测 18,835/2,465/2,400 句。基线含从零 Transformer/Conformer/Branchformer/Paraformer，以及 CW（WenetSpeech）与 Whisper Tiny–Medium 零样本/微调。

## 实验与结果
从零最优约 Conformer attention rescoring CER 31.74%。CW 零样本/微调 16.43%/13.54%；Whisper-Medium 23.41%/16.14%。微调后女/男 CER 约 10.44%/16.89%；随年龄上升，85+ 明显变差（90–95 约 24.41%）。

## 结论
野外老年普通话仍难；预训练+领域微调必要。数据集可作为 ASR 与说话人画像等任务的挑战基准。

## 点评
「野外来源 + 人工细标」补上现有中文老年库的空白。人口学分解（性别/高龄）把难点落到可行动的采集与适配方向，而不只是报一个总 CER。


# Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval

- 论文编号：907
- 报告人：Pranshu Nema
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nema26_interspeech.pdf

## 问题
端到端 ASR 对专有名词/长尾词常产出音近但词错的替换，伤下游实体理解；微调代价高，单信号后编辑又弱。

## 方法
后处理专名 grounding：GLiNER 抽实体；对预定义词表做多视图检索——G2P 音素编辑距离、Soundex 粗语音编码、上下文嵌入余弦；min-max 归一化后加权融合排序，不改 ASR 也不用声学特征。在 United-MedSyn 药物名闭集词表上评 Whisper-large-v3 与 Qwen3-ASR-1.7B。

## 实验与结果
原 ASR 实体精确匹配约 38.27%/36.27%。融合（+text-embedding-3-large）Recall@1 达 74.67%/59.82%（相对精确匹配 +36.4/+23.6 pp），R@10 最高 87.36%。单视图中 G2P 略优于 Soundex；语义视图单独较弱但在高 K 互补。近同音与语义近邻仍是残差错误主因。

## 结论
ASR 专名错误具结构化音近性，多粒度语音+语义检索可显著提升实体级 Recall@K，且 ASR 无关。可扩展到其他专名词表；未来拟做自适应权重与解码约束。

## 点评
把「纠错」改成「排序候选供下游/人工」，产品形态更务实。评估条件在 NER 对齐成功样本上，抽取失败被排除，报告的是 grounding 上限而非端到端流水线。


# From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection

- 论文编号：338
- 报告人：Jan Jasiński
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/jasinski26_interspeech.pdf

## 问题
ASR 幻觉（流畅但与音频无关的转录）会拖垮下游系统，但传统 WER 等指标难以把它与普通误听区分开。现有文本指标多依赖参考转写，参考无关指标与 LLM 检测在部署场景下效果有限；真实语音上的人工标注数据也长期不足。

## 方法
在 HALAS 数据集上对 Whisper large v3 做话语级幻觉检测，比较三类范式并做融合：
1. **文本指标**：oracle（WER/CER/IER、BERTScore、SeMaScore、CHP 等）与 reference-free（CPS、PPL、对齐置信度、NCHP 等），用 Logistic Regression / Random Forest / XGBoost 分类。
2. **LLM**：以 GPT-4o mini、Gemini 系列零样本提示为基线，逐步加入更强推理模型、Whisper 非语音幻觉病理、few-shot，并尝试去掉参考转写。
3. **解码器内部状态**：对 Whisper 各层解码序列做 mean/max pooling 与 BLSTM 探测（自注意力 / 交叉注意力 / 最终输出，可加序列差分）。
4. **晚融合**：用 XGBoost 与 BLSTM 的 OOF 概率加音频时长，训练 Logistic Regression 元分类器。

## 实验与结果
数据为 HALAS（Earnings-22 上 Whisper large v3：858/3611 为幻觉）。主要数字：
- 单特征 AUC：oracle BERT 82.3%、CER 81.9%；reference-free 最强 CPS 68.2%。
- 文本分类：XGBoost 全特征 F1 62.8%；仅 reference-free 降至 37.7%。
- LLM：最佳 oracle 配置 F1 58.7%；reference-free 降至 32.8%，仍不如轻量 XGBoost。
- 内部状态：中间层线性可分性约 AUC 81–82%；最优 BLSTM（参考无关）AUC 87.6%、F1 65.5%。
- 晚融合：Acc 90.7%、F1 68.3%、AUC 90.0%，优于单一范式。

## 结论
幻觉信号在 Whisper 解码中间层被编码；参考无关的内部状态探测可超过依赖参考的文本/LLM 方法。文本与内部状态部分互补，晚融合达到最佳整体检测效果。三类方法对单功能词插入类幻觉仍普遍失效。

## 点评
工作把“有没有参考转写”这一部署约束放在中心：oracle 文本特征看起来强，但一旦去掉参考就崩；内部状态探测绕开了这一瓶颈，且不引入 LLM 的延迟。晚融合说明两类错误不完全重叠，但元分类器仍依赖音频时长等弱路由信号，单字幻觉仍需声学侧信息。


# Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR

- 论文编号：1314
- 报告人：Saurabh Kumar
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/agarwal26_interspeech.pdf

## 问题
Whisper 在静音与非语音上易产生虚假转录，现有 VAD、置信度、抑制或改模型等方法缓解有限。同时短对话轮次无法填满 Whisper 固定 30 秒窗口，吞吐浪费。需要不改模型、可落地的幻觉检测与安全批处理方案。

## 方法
提出 **anchor audio**：在输入前拼接一段领域内几乎不出现的短提示音频（优选 TTS 合成的 “Mongolia”），用能否正确识别该前缀作为可信度标记；锚点也作多段拼接的分隔符。
五种推理：A1 原版 Whisper；A2 仅 Silero VAD；A3 VAD+锚点前缀，匹配失败则回退整段输出；A4 朴素批拼接后按锚点切分；A5 批处理校验锚点个数，不匹配则回退到单条 A3。推理用 int8 whisper-turbo。

## 实验与结果
1–5 秒片段共约 33k：零售客服私有集、UrbanSound8K（6614，排除 children playing）、AMI、LibriSpeech。
- 整体 WER：A1 32.18% → A5 13.23%；Urban8k HER：A1 72.2% → A3 0.12% / A5 0.14%。
- A4 有 8.45% 切分失败；A5 失败率为 0。
- 并发 32 时 P95 延迟：A3 579ms、A5 566ms，与 A2（570ms）接近。
- 文本 prompt 消融（Ab1/Ab2）HER 仍高于音频锚点，且零售 WER 变差。
- LibriSpeech 上锚点略升 WER（如 clean 2.87%→3.03%），作者归因于专有名词拼写表面差异。

## 结论
输入级锚点音频可在不修改 Whisper 的情况下几乎消除非语音幻觉，并支持带校验的批拼接。A3 适合延迟敏感，A5 适合吞吐；局限包括锚点需领域调参、长句收益下降、仅评 Whisper/英语。

## 点评
做法本质是给自回归解码一个“声学 grounding token”，比纯文本 prompt 更强，且复用同一机制做批分隔，工程上很实用。风险在锚点与真实语音重叠、噪声掩蔽导致匹配失败，以及批校验回退带来的尾延迟；跨领域与跨架构是否成立仍需验证。

