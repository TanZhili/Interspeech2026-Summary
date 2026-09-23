# Robust ASR: Uncertainty and Confidence

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：8
- **论文数**：10
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场围绕稳健 ASR 的训练目标、上下文偏置、不确定性与幻觉抑制。CTC/音素识别侧用课程式过渡目标缓解 blank 主导与不稳对齐；非自回归精炼引入一致性正则，并可借快速解码为半监督生成伪标签。热词/实体偏置则结合对比正则、偏置分数估计与不确定性门控的音素级解码时偏置。

另一主线是噪声与低可懂场景：干净—噪声双视角自蒸馏、智通度引导的观测融合（observation addition），以及耳语场景下的自监督不确定性学习与置信融合解码。Speech-LLM ASR 侧用因果中介剖析幻觉来源，并提出小语言模型对齐减轻文本 token 过度注意；置信估计则用基于秩距离的连续目标改进多种架构上的 CEM。

## 技术内容

### 训练目标、一致性与上下文偏置

**Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition**（论文 1040；Izabela Krysińska）  
CTC 音素识别早期易被 blank 主导。TOL 课程学习从粗粒度语音目标逐步过渡到完整音素监督。在英/法/波兰语上摘要称降低 PER、加速收敛并改善训练稳定性。

**Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization**（论文 1471；Wanting Huang）  
将一致性正则扩展到 Align-Refine 非 AR 迭代精炼：全监督下对基座 CTC 与后续精炼步均施加 CR，增益可叠加；半监督下用快速非 AR 解码在线生成伪标签进一步精炼。

**COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation**（论文 1097；Jhih-Rong Guo）  
面向复杂多实体上下文偏置：把 SLM 潜表征映射到判别空间量化音频片段与候选实体匹配强度，并处理多目标话语训练崩塌。在 LibriSpeech 上摘要称跨不同偏置列表规模表现优越。

**UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models**（论文 1577；Yong-Jie Hou）  
免训练解码时框架：熵驱动门控与双模态对比惩罚缓解过偏置与同音误分类。在 Dolphin base 上摘要给出召回/F1 提升及干扰词条件下的召回增益，精度下降受限。

### 适配器对齐、噪声稳健与置信/幻觉

**Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs**（论文 2229；Vinayak Abrol）  
冻结语音编码器与 LLM，仅训练适配器。摘要称扩散 LLM 比自回归模型更能承受适配器瓶颈，在多数据规模划分上 RTF 与 ASR 更优，并避免 AR 在拒绝对骨干调参时的误差传播与漂移。

**DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition**（论文 3232；Jaeeun Baik）  
对干净—噪声成对视角做多层隐表征蒸馏，并用原型分配分布的 KL 稳定训练。在 LibriSpeech 上摘要称多样噪声下识别提升且保持干净准确率，额外开销约为微调时间的约 4%。

**Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition**（论文 879；Gaopeng Xu）  
耳语信号模糊导致漏辨与噪声幻觉两极失败。经自监督任务量化声学物理缺陷，再用置信融合解码向 LLM 解码器提供高层指令与帧级注意调制。摘要称 AISHELL6-Whisper 上相对 CER 下降，幻觉率大幅降低。

**Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models**（论文 1278；Bi-Cheng Yan）  
用因果中介与行为分析探测 SLM ASR 幻觉，提出基于小语言模型的 AudioSLM，以对齐线索与交叉注意增强声学与跨模态交互。摘要称幻觉与对文本 token 过度注意偏置相关，AudioSLM 减轻幻觉并优于部分基于 LLM 的 ASR。

**Rank-Distance Based Confidence Estimation for ASR**（论文 1355；Nagarathna Ravi）  
提出连续目标 RanD 及基于其上的 CEM，覆盖 CTC、RNN-T、TDT、AED；在印地语与英语 ASR 上摘要称优于 SOTA CEM 并向失配域泛化。

**Training-Free Intelligibility-Guided Observation Addition for Noisy ASR**（论文 1096；Haoyang Li）  
用后端 ASR 的可懂度估计导出融合权重，将噪声与增强语音做免训练观测相加，避免改 SE/ASR 参数。跨多种 SE-ASR 组合与数据摘要称相对既有 OA 基线更稳健；并分析切换式替代与帧/话语级 OA。

## 本场要点

- CTC 可用粗到细过渡目标缓解 blank 主导与早期不稳。
- 一致性正则同时服务非 AR 精炼与半监督伪标签。
- 热词偏置结合匹配强度估计、不确定性门控与对比惩罚。
- 扩散 LLM + 仅适配器对齐在参数高效 ASR 上更耐瓶颈。
- 干净—噪声自蒸馏与智通度引导 OA 提升噪声稳健。
- 耳语/SLM 幻觉需不确定性学习与对文本注意偏置的诊断缓解；RanD 改进置信估计。

## 覆盖核对

| id | title |
|---|---|
| 1040 | Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition |
| 1471 | Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization |
| 1097 | COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation |
| 1577 | UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models |
| 2229 | Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs |
| 3232 | DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition |
| 879 | Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition |
| 1278 | Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models |
| 1355 | Rank-Distance Based Confidence Estimation for ASR |
| 1096 | Training-Free Intelligibility-Guided Observation Addition for Noisy ASR |
