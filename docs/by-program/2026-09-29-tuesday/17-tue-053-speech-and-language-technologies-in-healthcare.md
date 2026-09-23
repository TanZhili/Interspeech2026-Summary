# Speech and Language Technologies in Healthcare

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：13
- 论文数：9
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场覆盖急诊分诊对话仿真、临床访谈转写隐私与角色归因、急救电话情感分诊假设检验、手术机器人语音指令安全识别，以及构音障碍修复/评估、口吃检测与老年语音零样本在线自适应。共同主题是：医疗场景不能只看通用 WER，而要保全否定、情态与时间线索，控制误识别导致的不安全动作，并在数据受监管限制时用结构化 EHR 驱动对话仿真。

临床可及性方面，构音障碍工作引入共振峰引导的显式谱空间校正再合成；口吃则用多实例学习从片段级标签推断帧级，或以自注意力权重特征做跨语零样本检测；老年 ASR 用跨话语音—文提示实现零样本在线说话人自适应。评估上，DIALOG-DeID 提出 speaker-attributed WER 与 Qualifier/Temporal Preservation 等超越 WER 的指标；法语急救电话研究则提示元数据可能比情感特征更能预测优先级。整体上，本场强调安全、可审计语义线索与跨说话人/跨语鲁棒。

## 技术内容

### 临床对话、分诊仿真与情感假设

**TriageSim: A Conversational Emergency Triage Simulation Framework from Structured Electronic Health Records**（论文 819；Dipankar Srirag）从结构化 EHR 生成带人设条件的多轮护患分诊对话，可控不流畅与决策行为，产出约 800 条合成转写及对应音频；结合自动语言/行为/声学保真分析与 50 条随机对话的人工医学保真评估，并用于会话式分诊分类效用检验。

**DIALOG DeID: Role and Privacy Aware Transcription for Clinical Interviews Beyond WER**（论文 1489；Dominic Dwyer）给出长时临床对话可配置管线，统一 ASR、日记化、角色映射与去标识；在 PSYCHS-Bench 上报告最佳聚合 WER 为 13.3±1.4，而角色归因 sWER 仍为 33.1±6.7，语义审计发现 20–24% 片段存在线索丢失。

**Revisiting Emotion-Based Triage: Evidence from French Emergency Call Data**（论文 1265；Elio Stasica）在 250 通法语急救电话、四级优先级标注及年龄/性别/说话人角色元数据上，比较离散情感与维量（唤醒度/效价）SER 接入有序逻辑回归；摘要称纳入元数据后类别情感不再改进预测，维量情感与说话人角色存在交互但效应依赖说话人，总体元数据优于情感特征。

### 手术指令安全与构音障碍修复/评估

**Surgical-Robot Command Spotting: Safety-Aware Learning for Compositional Commands**（论文 3372；Jaewon Lee）将口罩与手术室噪声下的短指令分解为方向、模式与幅度（1–5），用共享编码器上头级时间注意力池化，并以序数回归、逐样本损失掩码与训练期辅助头学习步进幅度；在韩语 OR 指令集留一说话人、干净/噪声与口罩/无口罩条件下，联合指令成功率为 95.36%，步进 MAE 为 0.0338，灾难性步进错误率（|Δ|≥3）为 0.60%。

**Formant-Guided Speech Repair for Enhanced Comprehension of Dysarthric Speech**（论文 1217；Xin-Yu Chen）提出含 formant-aligned spectral transformation（FAST）的模块化框架，在合成前显式校正扭曲共振峰，并与构音障碍适配 ASR 与说话人自适应 TTS 结合；在主要语料上 CER 相对降低 72.4%，主观评测显示可懂度/理解/流畅性增益逾 90%，聆听负担降低 60.9%，并在普通话与英语数据上展现泛化。

**Phoneme Error and Uncertainty Features for Interpretable Dysarthric Speech Assessment**（论文 1138；Zihan Zhong）用冻结 CTC 音素识别器的后验不确定性作构音扭曲代理，结合音素错误率构成 Phoneme Error Decomposition（PED）特征族；在 Speech Accessibility Project 语料上以逻辑回归探测，完整 PED 在四个主要维度上平均 AUROC 为 0.80。

### 口吃检测与老年语音自适应

**Stuttering Classification and Segmentation with Attention-Based Multiple Instance Learning**（论文 1091；Petar Sušac）基于微调 wav2vec 2.0、WavLM 与 Whisper 编码器的多实例网络，在片段级标签上同时服务片段级与帧级口吃分类；摘要报告帧级 F1 提升 23%，片段级 F1 提升约 2%–9%。

**Evaluating Zero-Shot Cross-Lingual Stuttering Detection Based on Self-Attention Weights of Temporal Acoustic Vector Sequence**（论文 1886；Genzo Miyahara）以时间声学向量序列的自注意力权重（SAWF）作为可跨语迁移特征，面向重复与延长等声学相似模式，并在口吃语料上进行零样本跨语评测（具体语言对与分数以官方摘要为准）。

**Decoding while Adapting: Zero-Shot Online Speaker Adaptation via Audio-Textual Prompts for Elderly Speech Recognition**（论文 620；Chengxi Deng）从当前及若干先前话语提取音—文嵌入并跨模态融合为紧凑说话人提示；在 DementiaBank Pitt 与 JCCOCC MoCA 上相对说话人无关模型，WER/CER 绝对下降 0.61% 与 1.22%（相对 2.99% 与 4.48%），并报告 RTF 加速。

## 本场要点

- 医疗 ASR/对话强调角色归因、否定/情态/时间线索保全，而非仅看整体 WER。
- 分诊相关：EHR 驱动对话仿真与“情感即紧急度”假设的实证检验并存。
- 手术语音控制把组合指令因子化，并以序数回归服务安全幅度预测。
- 构音障碍路径包括共振峰显式修复与不确定性可解释评估。
- 口吃检测推进帧级分割与跨语零样本特征。
- 老年语音用跨话语音文提示做零样本在线自适应。

## 覆盖核对

| paper_id | title |
|---|---|
| 819 | TriageSim: A Conversational Emergency Triage Simulation Framework from Structured Electronic Health Records |
| 1489 | DIALOG DeID: Role and Privacy Aware Transcription for Clinical Interviews Beyond WER |
| 1265 | Revisiting Emotion-Based Triage: Evidence from French Emergency Call Data |
| 3372 | Surgical-Robot Command Spotting: Safety-Aware Learning for Compositional Commands |
| 1217 | Formant-Guided Speech Repair for Enhanced Comprehension of Dysarthric Speech |
| 1091 | Stuttering Classification and Segmentation with Attention-Based Multiple Instance Learning |
| 1886 | Evaluating Zero-Shot Cross-Lingual Stuttering Detection Based on Self-Attention Weights of Temporal Acoustic Vector Sequence |
| 1138 | Phoneme Error and Uncertainty Features for Interpretable Dysarthric Speech Assessment |
| 620 | Decoding while Adapting: Zero-Shot Online Speaker Adaptation via Audio-Textual Prompts for Elderly Speech Recognition |
