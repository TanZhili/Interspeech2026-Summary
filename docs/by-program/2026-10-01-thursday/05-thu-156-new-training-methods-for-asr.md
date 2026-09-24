# New Training Methods for ASR

- 日期：Thursday 1 October 2026
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

本场聚焦 ASR 新训练与架构：统一离线/流式 Transducer、流式 Conformer 卷积感受野、Aligner-Encoder 渐进对齐、三层联合优化、LLM 作 joiner，以及无源域数据的目标中心模型合并。共同目标是在延迟、数据与隐私约束下缩小模式差距并稳定对齐学习。

流式侧，块限注意力 + 动态块卷积统一双模式，并用模式一致性正则拉近离线与流式；BACON 证明块内可安全前看至边界，无需严格因果卷积。对齐侧，中间 Aligner/CTC 目标让对齐沿深度渐进形成；LLM-as-Joiner 把对齐交给编码器、语言建模交给 LLM。优化与迁移侧，三层学习塌缩为可扩展罚函数双层梯度；无源数据时用元学习合并多源模型并强调目标相关源。

## 论文技术总结

# Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization

- 论文编号：1195
- 报告人：Andrei Andrusenko
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/andrusenko26_interspeech.pdf

## 问题
同一 ASR 模型同时做好离线高精度与低延迟流式仍难；Conformer 的 MHA/卷积在 chunk 解码下存在训练–推理失配，低延迟（<0.5 s）时离线/流式模式冲突加剧，大规模数据下的统一训练也欠研究。

## 方法
统一 RNNT：chunk-limited attention（左/当前/右上下文 L,C,R，训练时从预定义集合采样）+ Dynamic Chunk Convolution（DCConv，卷积按 chunk 与核半宽重排，离线共享参数）。训练可用单模式（每步随机 offline/streaming）或双模式（同 batch 两边 RNNT 损失加权）。进一步提出 MCR-RNNT：对离线与流式 joint logits 做对称 KL，用 Triton 融合核在线算 log-softmax/KLD，避免物化巨大 [T,U+1,V] 张量。最终目标 α L_off + (1−α) L_str + λ L_MCR。曾尝试 CR-CTC 扩展，对流式 RNNT 有害，故改为对 Transducer 输出一致性。

## 实验与结果
L-size FastConformer RNNT（~128M）在 Granary ~120k 小时归一化英文上训；Open ASR Leaderboard 平均 WER。Unified DM + MCR-RNNT：离线 6.63，流式在 0.24 s 仍 9.04，显著优于无 MCR 的 SM/DM（低延迟急剧恶化）。XL ~0.6B + 280k 小时含标点大小写：较大右上下文配置离线 AVG WER 5.76（SOTA Unified RNNT），平衡配置低延迟更稳。消融：对称 KL、λ≈0.3、α≈0.5 较优；固定总延迟下增大右上下文降 WER。

## 结论
chunk 限制注意力 + DCConv + MCR-RNNT 可把离线/流式差距压到更低延迟区间，并随模型与数据放大仍有效；框架与英文 checkpoint 开源。

## 点评
关键不是再叠一套编码器，而是在 RNNT joint 输出上显式拉齐两种上下文制度；相对 CTC 一致性，更贴合 Transducer 的对齐灵活性。工程上 Triton 全格点一致性使方法可训练。当前推理仍每步重算左上下文，作者承认速度未充分优化；极低 0.16 s 仍略逊纯流式基线。


# BACON: Boundary-Aware Convolution for Streaming Conformer Models

- 论文编号：1455
- 报告人：Hainan Xu
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26o_interspeech.pdf

## 问题
Chunk-based 流式 Conformer 常把深度卷积改成因果卷积以防未来泄漏；但 chunk 内帧已全部可用，纯因果卷积过度限制右上下文，丢掉安全可用的局部未来信息。

## 方法
提出 BACON：深度卷积通道对半拆分——因果组保留完整历史（仅句首左 pad）；边界感知双向组左上下文可跨 chunk，右上下文用 chunk 末 pad，严格限制在当前 chunk 内。核大小 k 时有效感受野约 [−(k−1),(k−1)/2]，宽于因果 [−(k−1),0]，参数量不变。作为因果卷积的 drop-in 替换。

## 实验与结果
NeMo FastConformer（17 层，d=512，k=9，chunk C=14≈1120 ms）上对比因果 vs BACON，架构含 RNN-T 与 CHAT。LibriSpeech：CHAT test-other WER 8.47→7.68（相对约 9.3%，p<0.001）；test-clean 也有显著改善。En→De AST：两族模型在 MuST-C/CoVoST 上 BLEU 均显著提升（如 CHAT CoVoST 36.40→37.72）。双说话人 Fisher cpWER 27.41→27.14（方向一致，p=0.19）。消融：全通道 boundary-aware（all-bidir）常弱于 BACON，甚至在 RNN-T test-other 上差于因果；因果组起边界稳定作用。全注意力设定下非因果卷积仍比因果低 0.93 WER，说明卷积右上下文与注意力互补。平均发射 chunk 索引略降，未增延迟。

## 结论
在 chunk 流式约束下用通道拆分安全引入 chunk 内右上下文，可在多任务、多架构上提准且不增加参数与延迟。

## 点评
洞察很具体：流式约束是“不看未来 chunk”，不是“永远不看未来帧”。双组设计避免 chunk 右缘全通道有效感受野同时塌缩。收益在困难集与翻译上更明显；多说话人增益较小，可能被重叠/说话人归因噪声淹没。


# Progressive Alignment Objectives for Aligner-Encoder based ASR

- 论文编号：2132
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26t_interspeech.pdf

## 问题
Aligner-Encoder 用编码器第 u 个位置直接预测第 u 个 token，无 cross-attention / Transducer 格点；对齐多在深层突然出现，长句上训练脆、性能差。

## 方法
提出 InterAligner：在中间层 ℓ_int（主实验第 15 层）对更长、更细粒度 BPE 序列加中间 Aligner 损失（独立 predictor/joiner）；在更早层 ℓ_ctc=12 加 InterCTC；顶层仍对较粗短序列做最终 Aligner。总损失加权 λ_final L_final + λ_int L_int + λ_ctc L_ctc，形成由早到晚、由细到粗的对齐课程。

## 实验与结果
17 层 Conformer-L（~118M），LibriSpeech 960h：Final-only 5.0/7.8 → +InterCTC 3.4/6.0 → +InterAligner 3.1/5.6（test-clean/other）。Common Voice EN：12.4→11.2→10.9。按时长分层，>21 s 句 clean/other 从 InterCTC 的 17.0/18.0 再到 InterAligner 的 11.6/13.5。消融：中间与 CTC 目标同用较小词表（如 256）优于不匹配；λ_final/λ_int=0.5/1.0 优于 1.0/0.5；InterAligner 挂在第 15 层优于第 16/13；仅缩小最终词表不够，需要层级监督。注意力可视化显示层 14 出现细粒度对角、层 16 再到粗粒度。

## 结论
中间 CTC + 中间细粒度 Aligner 可让对齐在深度上渐进形成，稳定 Aligner-Encoder 训练，并在长句上带来最大收益。

## 点评
针对“对齐瓶颈挤在顶层”的结构问题，用多粒度中间监督做课程，比单纯加深或换解码器更对症。挂层位置与词表粒度敏感（需留出至少约两层做细→粗转换）。收益主要在长句；短句上相对 InterCTC 提升有限。


# From Bilevel to Trilevel: Joint Training for Speech Recognition

- 论文编号：1738
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26b_interspeech.pdf

## 问题
ASR 常用“无监督预训练 + 监督蒸馏微调”两阶段流程，预训练损失在微调时被丢弃，易遗忘或负迁移；既有双层优化（如 BL-JUST）联合监督与无监督，但仍缺少知识蒸馏这一层。

## 方法
提出 TL-SUD：三层嵌套优化——上层监督损失 L_sup（标注数据）、中层无监督 L_unsup、下层蒸馏 L_KD（标注+无标注，蒸馏时不用真标签）。将中下两层折叠成双层子问题，用惩罚型双层梯度下降（PBGD）两次，得到共享骨干 θ 与各任务头 ϕ/η/ψ 的嵌套更新；惩罚系数 γ1、γ2 随 epoch 从 0 退火升至最大值。实现上 FastConformer 学生（115M，17 块）用 CTC 监督、对比无监督、特征级蒸馏；教师更大 FastConformer（616M）。

## 实验与结果
LibriSpeech：unlabeled=train-other-500，labeled=train-clean-100 时，TL-SUD test-clean/other 6.7/15.9，优于 PT(U)+FT(SD) 7.4/19.5、加权求和 7.4/19.1、监督基线 8.7/23.0。相对 BL-JUST（无 KD）在 100/200/360h 标注上均更低 WER（如 100h：6.7/15.9 vs 7.0/17.1）。惩罚日程敏感，最佳约 γ1 max=180、γ2 max=0.005。解码为无外部 LM 的 greedy。

## 结论
把监督、无监督与蒸馏纳入可训练的三层优化，能比两阶段与双层 JUST 更一致地利用三类信号，并在低资源标注设定下降低 WER。

## 点评
做法把“遗忘预训练语义”的管线问题改成嵌套可行集约束，KD 放最底层注入教师先验。工程关键是惩罚调度；调不好会破坏三目标平衡。评价刻意去掉 LM，突出优化本身，但绝对数字与带 LM 系统不可直接比。


# LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR

- 论文编号：2149
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26u_interspeech.pdf

## 问题
把 LLM 当 speech-as-prefix 解码器时，模型既要学对齐又要做语言建模，上下文长达 T+U，内存与计算重；对齐本可由语音编码器更好承担。

## 方法
LLM-as-Joiner：Aligner-Encoder 产出 U 个 label-synchronous 语音状态（监督前 U 个编码器位置）；预训练 Llama-3.2-3B 在选定层 ℓ 注入语音（门控残差融合），下层当 predictor、上层当 joiner，仅上层 LoRA（rank 16），tokenizer/嵌入/LM head 不变、无 blank。同编码器并行训练轻量 LSTM+FFN 头以便无 LLM 部署。总损失：λ_llm L_llm + λ_lite L_lite + λ_ctc L_ctc（1.0/0.5/0.1）。

## 实验与结果
Conformer-L 从零训练。LibriSpeech：LLM head 3.2/5.6，优于 decoder-only 基线 3.7/7.1；Lite head 3.8/6.4，接近从零 Aligner 3.9/6.5。cv-5langs（de/en/es/fr/it）：LLM head 均 11.5，Lite 12.5，显著优于从零 Aligner 14.4；decoder-only 在多语未收敛。RTF：Lite 0.02，LLM head 0.65 vs decoder-only 0.90。消融：注入层 0/7 相近，14 变差；门控用 speech+text 对 Lite 更有利。

## 结论
用 Aligner 管对齐、LLM 管语言建模，可在更短上下文下提升识别，并让联合训练的轻量头隐式受益于 LLM。

## 点评
接口设计清晰：U 长度对齐面让 LLM 不必吞长语音前缀。对照实验刻意不用预训练语音编码器，突出架构差异。多语上 Lite 头收益更大，说明知识迁移对低资源语言更关键；晚注入失败提示融合仍需足够上层容量。


# Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging

- 论文编号：371
- 报告人：Ka Hyun Park
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/park26b_interspeech.pdf

## 问题
无源域数据、仅有多个预训练源分类器与少量目标标注时，如何适配未见目标域；常规迁移/数据选择不可用，现有模型合并易在少样本目标上过拟合。

## 方法
提出 MOCHEE：冻结 wav2vec2 等共享嵌入，只合并各源 MLP 分类头。用 Sinkhorn 软置换矩阵对齐隐单元（消除置换对称性），再学源权重 α 做对齐参数空间加权平均。α 不直接拟合目标训练集，而用 meta-reweighting：内环在目标 train 上虚更新置换参数 p，外环用目标 val 损失对 α 取元梯度（非负后 softmax）。源参数本身不更新。

## 实验与结果
CAMEO 情感跨语料：源 CREMA-D/SubESCO/RAVDESS/MESD，目标 CAFÉ、Oréau（六类情绪）。MOCHEE 在 CAFÉ Acc/Macro-F1 50.85/49.40，Oréau 35.30/34.85，优于 Uniform、Greedy Soup、Re-basin、TIES 等；相对最差基线 Macro-F1 可高约 14.5 点。即便基线再在目标上微调，MOCHEE（不微调）仍最好。消融：去置换对齐掉点大；去 α 学习也一致变差。权重演化显示目标英源时逐步抬高英语源 CREMA-D。

## 结论
在源自由、少目标标签设定下，对齐 + 元学习源重要性的目标中心合并，可比启发式合并更好泛化到未见目标样本。

## 点评
抓住“能共享模型不能共享数据”的现实约束，把合并权重当元学习对象而非验证集挑模型。软置换让异构训练头可平均；内环改 p 而非 θ 保留合并效率。局限在分类头合并与共享冻结前端假设，且效果依赖目标 train/val 划分质量。

