# Audio Understanding and Representation Learning

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Poster（Area 5）
- 论文数：11
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场覆盖视听 VAD、长会话目标说话人提取、脚本化检测护栏、多通道分离–日志统一、长音频层次活动语法、说话人归属副语言事件、音乐艺术字幕、并行不变语音分词，以及 AAC/少样本提示学习。共同主题是：理解任务要从“能分类”走向“抗捷径、可归因、层级一致、语义不变”。

会议/多说话人前端强调空间先验：DOA 引导免日志归因，空间信息同时进入系统与自适应仿真以降低重叠区混淆。事件理解则走向联合帧级预测与语法引导层次解析。表示学习侧，并行话语对齐把说话人探测准确率压到近随机；字幕与分类侧则用双 MoE 动态奖励路由或音频侧提示补文本提示不足。评测意识突出：SEAM 显示去掉防捷径组件会使外部泛化骤降。

## 技术内容

### 检测、会议前端与护栏

**MAC-VAD: A Modality-Aligned Cross-Attentive Framework for Robust Voice Activity Detection**（论文 384；Bruhanth Mallik）
音频编码器自适应学谱–时表示，视觉编码器用人脸/唇特征预测语音 onset，模态对齐双交叉注意力融合，并以教师网络蒸馏。MMVAD 评估称优于基线，验证对齐交叉注意力与自监督蒸馏。

**Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR**（论文 787；Yichi Wang）
PATSE 用 DOA 空间先验直接提取各目标说话人流，简单 VAD 后处理即可推断活动而无需显式日志。重放与真实会话上 ASR 增益优于 CSS 与基于日志流水线。

**SEAM: Shortcut-Aware Real-Time Detection of Scripted vs. Spontaneous Speech for Interview Guardrails**（论文 1480；Pranay Manocha）
用统一预处理、seam-aware 采样、非语音增强与 DistilHuBERT 抑制语料/信道捷径。8 s 窗外部面试域 ROC-AUC 0.971±0.004；去掉防捷径组件内部指标升而外部骤降。量化后约 41.8 MB。

**MCA-DCF-DS: An Adaptive Framework for Unified Diarization and Separation with Spatial Information**（论文 1539；Shutong Niu）
将 DCF-DS 扩展为多通道并在自适应仿真中引入空间信息，处理日志漏检与混淆权衡。空间信息在系统与数据两侧均改善下游 ASR；同 ASR 后端下优于 CHiME-8 Task 2 冠军。

### 层次活动、联合事件与音乐字幕

**Grammar-Guided Hierarchical Parsing for Long-form Audio Activity Recognition**（论文 2157；Peng Zhang）
由事件证据推断顺序一致的 Act-Sub-Event 树；Hierarchical Activity Grammar 编码组成与时序约束。无需子活动/活动标签训练；MultiAct 上提升 Edit score 并给出可解释层次。

**SA-UAED: Joint Frame-Level Detection of Audio Events, Speaker Activities, and Speaker-Attributed Paralinguistic Events**（论文 2486；Zekun Lan）
仿真管线生成帧级精细标注，联合预测声音事件、说话人活动与归属副语言（笑、咳等）。显著改善说话人归属副语言检测且不牺牲通用 SED/SD。

**Music Artistic Captioning: Towards Translating Music into Expressive Language**（论文 2618；Ubaid Ullah）
训练无关 MAC：聚合帧/段/曲级描述子为约束伪证据，驱动指令 LLM 分层长字幕，并用一次性迭代提示优化平衡叙事与忠实度。歌剧语料与字幕基准上相对强基线一致提升。

### 不变分词、字幕 RL 与少样本提示

**Content is What Remains: Invariant Speech Tokenization from Parallel Utterances**（论文 2817；Laurin Wagner）
PINT 在并行话语与增强上用对齐损失微调 SSL，蒸馏共享语言残差。相对基线：说话人探测准确率相对降 98.7%（93.1%→1.2%），ABX 错误率降 42%，LM 困惑度降 27–30%。

**Context-Adaptive Automated Audio Captioning with Symmetric Dual-MoE and Dynamic Reward Routing**（论文 2897；Seyun Ahn）
对称双 MoE：策略侧 LoRA 专家经声学上下文路由；奖励侧并行评估语义、语法、词汇多样与音文对齐并由上下文路由器加权，用 GRPO 优化。Clotho 与 AudioCaps 上字幕质量与人类偏好提升。

**Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models**（论文 885；Hyebin Cho）
在音频编码器引入可训练提示以捕获任务声学特征，并与文本提示结合。11 数据集上作为即插即用模块通常提升少样本表现。

**Audio-Language Prompt Learning for Few-Shot Audio Classification**（论文 1173；Qisheng Xu）
MALP 联合优化音频专用、文本专用与共享提示。11 基准平均相对 CoOp/CoCoOp/PALM 分别 +7.21%/+4.80%/+1.77%。

## 本场要点

- 视听对齐与教师蒸馏提升稳健 VAD；会议场景可用 DOA 先验免日志归因。
- 脚本化检测必须显式防捷径，否则外部泛化崩溃。
- 空间信息同时进入分离–日志系统与自适应数据可改善重叠区 ASR。
- 长音频理解走向语法引导层次解析与说话人归属副语言联合检测。
- 并行不变分词显著剥离说话人泄漏；双 MoE 动态奖励改善 AAC 上下文适应。
- 少样本 ALM 需音频侧提示与共享跨模态提示，不能只调文本。

## 覆盖核对

- 384 | MAC-VAD: A Modality-Aligned Cross-Attentive Framework for Robust Voice Activity Detection
- 787 | Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR
- 1480 | SEAM: Shortcut-Aware Real-Time Detection of Scripted vs. Spontaneous Speech for Interview Guardrails
- 1539 | MCA-DCF-DS: An Adaptive Framework for Unified Diarization and Separation with Spatial Information
- 2157 | Grammar-Guided Hierarchical Parsing for Long-form Audio Activity Recognition
- 2486 | SA-UAED: Joint Frame-Level Detection of Audio Events, Speaker Activities, and Speaker-Attributed Paralinguistic Events
- 2618 | Music Artistic Captioning: Towards Translating Music into Expressive Language
- 2817 | Content is What Remains: Invariant Speech Tokenization from Parallel Utterances
- 2897 | Context-Adaptive Automated Audio Captioning with Symmetric Dual-MoE and Dynamic Reward Routing
- 885 | Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models
- 1173 | Audio-Language Prompt Learning for Few-Shot Audio Classification
