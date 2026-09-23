# Cross-Lingual and Multilingual Speech Recognition 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：9
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场多语/跨语识别与 Speech LLM 聚焦语言干扰、公平性、低资源参数高效适配、编码器融合，以及编解码器 SSL 的语言敏感性。错误分析表明语义保持来自音系–形态–句法–词汇的跨维交互，且不同架构整合语言信息的机制不同。

系统方向包括：语言感知蒸馏查询与门控缓解共享投影器干扰；共享–私有 Fusion-LoRA 与置信门控 Mean-Teacher；多编码器融合；形态感知分词对抗 Indic 形态破碎；SpeechLLM 解码器层冗余剪枝；弱掩码残差可靠度域适应；以及代码切换兴趣点对比训练。公平侧用 MinMaxGAP 正则量化并缩小多语多模态情感识别的性别差距。

## 技术内容

### 错误交互、指令蒸馏与公平性

**How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR**（论文 920；Simon Gonzalez）在 FLEURS 上对 Whisper/Seamless 替换错误，从 ASR 音频与转写直接度量音系、形态、句法与词汇相似度。摘要称语义保持来自系统跨维交互：形态与句法相互依赖，句法保持时音系准确更强；Seamless 基线更好，Whisper 对错误更敏感但更有效利用形态信息。

**Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision**（论文 2446；Shreyas Gopal）用查询库与门控网络选择/混合 Q-Former 查询 token，做语言感知蒸馏。相对匹配多语蒸馏基线指令跟随提升约 14%；合成 Audio-MLQA 口语问答基准，最佳模型相对既有 Speech LLM 基线提升约 32%。

**ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition**（论文 3143；Zi Haur Pang）基于 MELD-ST 构建英/日/德多语多模态基准，发现偏差强依赖语言且多模态融合不必然更公平。ERM-MinMaxGAP 在 Qwen2-Audio 上多语 SER 提升 5.5%/5.0%，总体性别差距分别降 0.1%/1.4%（单模态/多模态）。

### 低资源适配、编码器融合与 SSL 语言敏感性

**Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA**（论文 1183；Jie Liu）SPF-LoRA 共享支学习跨语共性、私有支捕获语种特性并由可学习融合权平衡；MT-CR 用 EMA 教师与可靠性过滤抑制噪声一致性信号。Kathbath 上相对 Whisper-small+LoRA 宏 WER 降 35.4%，并优于所报告 Whisper-medium+LoRA。

**Speech Encoder Fusion for LLM-based Automatic Speech Recognition**（论文 1039；Jakob Poncelet）探索超越简单拼接的学习组合与 Transformer 融合，在单语/多语 ASR 与日记化识别中，仔细融合多并行编码器均可提升下游且开销有限。

**Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens**（论文 3002；Daigo Takizawa）固定 NAC 或 SSL 预训练语言之一做对照。下游表现对 NAC 训练语言不敏感，但强依赖 SSL 预训练语言——单一 NAC 可跨语复用，SSL 语言应对齐目标语。

### 形态分词、解码器冗余、域适应与代码切换

**SᴜTRA: Structurally-Unified Tokenization with Root Awareness**（论文 291；Vaibhav Rathore）形态感知分词保持 akshara 不可分并惩罚跨越形态边界的合并，发布印地/马拉地/古吉拉特形态切分数据。相对 BPE，形态对齐 Boundary F1 峰值 +14.7%，语义可恢复性（印地）+34%，机器翻译平均 +8.08 chrF2。

**Measuring the Redundancy of Decoder Layers in SpeechLLMs**（论文 1873；Adel Moumen）跨两 LLM 族与 1–8B 规模显示解码器冗余多继承自预训练文本模型；7–8B 仅用约 60% 解码层可保持良好 ASR，冗余块跨编码器、任务与语言具全局结构，可支撑单骨干多任务剪枝。

**Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models**（论文 1767；Yuan Li）联合预测置信与残差离散度加权伪标签，弱置信掩码部分遮盖高置信区，并加多扰动一致性。跨域 ASR 相对 WER 降幅：CHiME-4 13.8%、SLURP 25.0%、CORAAL 15.7%，翻译任务亦有改进。

**Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition**（论文 3465；Tung X. Nguyen）在代码切换兴趣点构造声学可信近错假设，经声学/音素/文本约束过滤后，用 POI 加权 CE 与多负对比排序微调 Whisper-small+LoRA。CS-FLEURS 与 ViMedCSS 上相对标准 LoRA，总体与 CS 感知错误率均降逾 2%。

## 本场要点

- 多语 ASR 错误需从跨语言维度交互理解，架构差异显著。
- 语言感知蒸馏与共享–私有 LoRA 缓解多语干扰与负迁移。
- 性别公平需语言/模态特异正则，而非假设融合即公平。
- 编解码器可跨语复用，SSL 预训练语言更关键。
- 形态感知分词与解码器层剪枝分别服务 Indic 与 SpeechLLM 效率。
- 可靠度加权域适应与 POI 对比训练强化跨域与代码切换稳健性。

## 覆盖核对

| id | title |
|---|---|
| 920 | How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR |
| 2446 | Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision |
| 3143 | ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition |
| 1183 | Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA |
| 1039 | Speech Encoder Fusion for LLM-based Automatic Speech Recognition |
| 3002 | Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens |
| 291 | SᴜTRA: Structurally-Unified Tokenization with Root Awareness |
| 1873 | Measuring the Redundancy of Decoder Layers in SpeechLLMs |
| 1767 | Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models |
| 3465 | Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition |
