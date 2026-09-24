# Multi-Speaker Processing, Personalization, and Adaptation

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：9
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖多说话人 ASR/日志、用户自定义关键词、LLM-ASR 的文本域适配与热词定制，以及音频问答的测试时强化学习。级联多说话人系统的说话人泄漏被用日志验证做剪枝校正；统一生成式 Speech-LLM 则用 CoT 先推断说话人数，再用约束感知 GRPO 在未知人数下联合 ASR 与日志。

个性化与适配侧：CTC 引导关键帧融合提升易混淆自定义关键词分辨；文本仅适配用多视角去噪批混合避免破坏 speech–text 投影对齐；热词定制 AFG-Bias 以声学检索+门控注入替代脆弱提示注入。部署后自适应方面，AQA-TTRL 仅用无标注测试数据做多数票伪标签与置信加权强化学习，使较小模型经测试时适应后可超过未适应的更大模型直接推理。

## 论文技术总结

# Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction

- 论文编号：3191
- 报告人：Suresh Singh
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nkouanga26_interspeech.pdf

## 问题
级联多说话人 ASR（分离→单说话人 ASR）受分离说话人泄漏限制；已有纠正多偏词汇重标注，对泄漏伪影的稳健剪除不足。

## 方法
后处理剪枝范式：用预训练说话人日志模型作多模态校验，对已转写片段在满足三方共识时剪除——时间包含（Cac）、词汇交叉验证（Clex）、时间对齐（Ctemp）。不改分离/ASR 骨干，可插在 Sepformer/Mossformer + Universal-2 等级联后面。

## 实验与结果
Libri2Mix、LibriSpeechMix、AMI（SDM/IHM）上相对基线一致降 WER；AMI 上相对改进约 5.8%–10.55%。高泄漏子集（分离源转写相似>0.4）相对 cpWER/WER 降幅最高约 29%（Mossformer AMI IHM 65.58→46.39）。消融：仅文本易过删；声学条件贡献大，三方合用最佳。相对联合 Mossformer-Diar 更跨域稳健。

## 结论
基于日志的三方共识剪枝能有效抑制级联 MT-ASR 中的说话人泄漏，尤其在高泄漏与真实会议场景。

## 点评
把泄漏当“可检测伪影”而非只重标说话人，后处理可复用强基础模型，工程上务实。依赖日志与对齐质量；仅文本条件有害说明多模态约束必要。未改分离前端，上限仍受分离 residual 限制。


# Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts

- 论文编号：2297
- 报告人：Yunrui Cai
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cai26c_interspeech.pdf

## 问题
联合多说话人 ASR（含归因与时间戳）在说话人数未知、输出结构严格时很难；仅 SFT 对齐 Speech-LLM 在高重叠下易突发幻觉与畸形 speaker/timestamp 标签。

## 方法
两阶段生成框架：(1) CoT 增强 SFT：先推断全局说话人数再转写；(2) GRPO 约束探索，用 Multi-dimensional Constraint-Aware Reward（MCAR）直接优化置换不变准确度，并强制计数、时间与结构约束（含 burst 惩罚等）。骨干 Qwen2.5-Omni-7B + LoRA；在高重叠 1 万样本上做 GRPO。

## 实验与结果
Libri2/3Mix 与 Dynamic-Mix(2+3)：SFT+CoT+GRPO 在 3 说话人 cpWER 14.52%、WDER 1.95%；Dynamic-Mix cpWER 9.24%、WDER 1.12%、CoT-Acc 99.72%。相对 SFT+CoT，GRPO 带来约 35%/54% 相对 cpWER 降幅。零样本基线说话人计数仅约 32%。

## 结论
先计数的 CoT + 多维约束 GRPO 使 Speech-LLM 在未知人数、高重叠下联合转写与日志显著更稳，超越仅模仿式 SFT。

## 点评
把“人数未知”显式建成推理前缀，再用 RL 罚结构崩坏，对准生成式多说话人输出的主要失败模式。评测偏合成混合；真实会议噪声/重叠分布外推未充分展开。奖励设计复杂，权重敏感。


# KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting

- 论文编号：1586
- 报告人：Wenbin Jiang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26y_interspeech.pdf

## 问题
用户自定义关键词检测需区分目标词与音近干扰词；全序列匹配易被整体相似淹没局部可辨音素差异。

## 方法
KFC-KWS：利用 CTC 尖峰后验选高置信音素关键帧，对齐音频、音素与文本模态；再经交叉注意力与全句表示融合，兼顾局部判别与全局语境。冻结 XLS-R 音频编码 + G2P 音素 + DistilBERT 文本；可训约 2.0M 参数；模态 dropout。

## 实验与结果
LibriPhrase：无增强时平衡 AUC 98.06%（LPH 96.54%，EER 9.13%），优于 HyperSpotter-c 等且参数更少。带模态 dropout：平衡 AUC 98.73%，LPH AUC 97.65%、EER 7.75%，强于增强版 PLCL 等。易集上 EER 略逊部分全序列模型，偏重难集可辨性。

## 结论
CTC 引导关键帧融合能有效提升音近关键词判别，在 LibriPhrase 难集与平衡指标上达到强结果且参数紧凑。

## 点评
抓住“混淆发生在少数音素位置”，用 CTC 峰定位再融合，比纯全局嵌入更对症。参数效率好。易集略牺牲、依赖 CTC 对齐质量；开放域口语噪声下峰检测是否稳仍待验。


# Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising

- 论文编号：3422
- 报告人：Sergio Burdisso
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/burdisso26_interspeech.pdf

## 问题
仅用目标域文本微调 LLM-ASR 的 LLM 会破坏 projector 学到的语音–文本对齐，引发灾难性遗忘。文本比配对音频更易得，需要不改结构、不增参的纯文本适应。

## 方法
把适应建成去噪任务，并用 multi-view noise-driven batching：每个 mini-batch 混合 (1) 源域配对音频–文本、(2) projector 诱导的噪声转写、(3) 合成破坏的源转写、(4) 破坏的目标转写。合成噪声含随机字符替换与重复，模拟 projector 噪声模式。冻结编码器与 LLM 骨干训 projector 得基座后，用该混合做文本适应；无架构改动。

## 实验与结果
SLAM-ASR（WavLM-Large + Llama 3.2 系）上 DefinedAI / SlideSpeech。域内/域外/跨域三档：相对 Fang et al.、Ma et al. 文本适应更优；跨域相对基座相对 WER 改进最高约 25.4%（An），仍低于有音频适应上界。SlideSpeech 域外相对改进约 4.2%–7.0%。

## 结论
多视角噪声混合可在纯文本适应时保持语音–文本对齐，显著优于近期文本适应法，且不增参数。

## 点评
关键洞察是“别让 LLM 只见干净目标文本”，用源音频与噪声视图当锚防遗忘。工程上轻、可插。上界仍逊真音频适应；噪声配方需调，跨声学域差距仍大。


# AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning

- 论文编号：288
- 报告人：Haoyu Zhang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26c_interspeech.pdf

## 问题
LALM 部署后静态，难适应真实测试分布；有监督更新需标注。需在无标签测试数据上自进化做 Audio Question Answering。

## 方法
AQA-TTRL：对测试题多数投票（如 64 次）得伪标签，再以 GRPO 做测试时强化学习。置信度加权优势缓解伪标签噪声；multiple-attempt sampling 抑制 advantage collapse。全参微调（AdamW），小数据集约 100 步、大数据集约 500 步。对比 DI、DIMV、同伪标签 SFT。

## 实验与结果
MMAU / MMAR / MMSU：Qwen2.5-Omni 7B 平均 +4.42%（64.39→68.81），3B +11.04%（53.82→64.86）；适配后 3B 平均超过未适配 7B 的 DI。优于 DIMV 与伪标签 SFT。消融显示置信度加权与多次尝试互补。按音频类型适配时 music-only 平均最高。

## 结论
无标签测试时 RL 自适应可使 LALM 在 AQA 上显著自提升，小模型经适应可逼近更大模型直推。

## 点评
把数学域 TTRL 迁到音频，用多数票伪奖励 + 抗噪机制形成闭环。RL 比同标签 SFT 更能“忍错标签”。成本是测试时大量前向与更新；伪标签系统性偏差仍可能固化。


# AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR

- 论文编号：2029
- 报告人：Long Wu
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26i_interspeech.pdf

## 问题
LLM-ASR 难识别稀有领域实体；浅层融合不适生成式解码，深度上下文化多为传统 E2E，提示注入易规模崩塌与幻觉。需不改 LLM 参数的可插拔热词偏置。

## 方法
AFG-Bias：Cross-Modal Acoustic Retrieval（CAR）用滑窗跨模态相似度从大规模候选中取相关热词；Acoustic-Fusion Gating 把经验证偏置注入解码并抑制无声学依据的幻觉。训练时冻结骨干 LLM；HotwordModule（内维 256、单层单向 LSTM）等轻量模块可训。推理 K=5、τ=3、偏置权重约 0.4。

## 实验与结果
AISHELL-1/KeSpeech 训，SeACo 与金融/医疗集评。三骨干 FireRedASR/OSUM/Kimi：相对直推，金融/医疗 CER 相对降最高约 74.1%（OSUM 10.93→2.83）；AISHELL 热词 F1 最高约 +5.4。无门控 CER 飙至约 20%；候选扩到上千仍较稳。纯提示注入常崩至 >30% CER。

## 结论
声学检索 + 门控融合可在冻结 LLM-ASR 上实现可扩展、低幻觉热词定制，显著优于提示注入。

## 点评
把“先声学证据再偏置”做对，直接打消提示列表淹没注意力的失败模式。可插拔性强。依赖 CAR 召回质量；极短/同音热词与跨语实体仍可能漏检或误门控。

