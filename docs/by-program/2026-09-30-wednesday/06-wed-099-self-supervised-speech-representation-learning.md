# Self-supervised Speech Representation Learning

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：8
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场聚焦自监督语音表示的可解释性、任务适配与部署效率。一方面深入剖析 WavLM 等模型中声学特征的冗余与多义性，说明稀疏神经元消融不足，需要子空间级干预；另一方面把韵律、口吃等多任务信号显式注入或联合建模，强化情感与流畅性相关下游能力。

联邦与边缘场景推动自适应微调：早期退出与按深度部分聚合应对算力异构与任务所需表示深度差异。离散令牌路径则在推理阶段用软分配缓解硬量化信息损失，训练仍可保持硬离散效率。低资源域适配方面，出现可端到端训练的硬 Gumbel-Softmax 层选择器，结合 BEST-RQ 目标自动挑选 Whisper 编码器层。

总体趋势是：SSL 骨干仍是通用底座，但研究重心转向“表示里到底编码了什么、如何在隐私/算力约束下高效适配、以及离散接口如何在推理时更表达力强”。

## 技术内容

### 表示可解释性与韵律感知

**Causal Redundancy in Speech Representations: The Hydra Effect and Limits of Sparse Disentanglement in WavLM**（论文 3316；Patalee Narasinghe）  
用线性探测、JumpReLU SAE 与 INLP 分析 WavLM。早期层可定位声学特征，但原始神经元多义性强；潜变量消融出现 Hydra 效应——离散移除因大规模冗余无法抑制声学特征。INLP 擦除整个声学线性子空间可选择性去除如基频等特征并保留其他探测。在 RAVDESS、CREMA-D、TIMIT 上表明需子空间级而非神经元级干预。

**Prosody-Aware Speech Representations for Emotion Recognition under Pragmatic Ambiguity**（论文 3486；Yeonwoo Park）  
向预训练 Whisper 编码器共享隐表示注入音高与能量，构建韵律感知表示。在 59 类情感分类与语用歧义消解（PAR）任务上，摘要称相对无韵律 Whisper 最高分别提升 13.93 与 11.6 个百分点，且 PAR 上优于基于文本的 GPT-4o mini 推理。

### 多任务流畅性、联邦微调与软令牌推理

**DysfluentNet: Joint Stuttering Event Detection and Dysfluency-Aware Transcription via Hierarchical Self-Supervised Learning**（论文 696；Mohankumar Muthu）  
冻结 WavLM-Large 配合轻量不流畅条件解码器，在 SA-CTC 目标下联合细粒度口吃事件检测与不流畅感知转写；辅以课程学习与基于标注者一致性的 SEP-28k 难度划分。摘要报告 SEP-28k/FluencyBank 上宏 F1 72.4、DI-WER 18.3，分别优于最佳已发表基线 6.8 与 4.1 点。

**Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations**（论文 2122；Xin Guo）  
在 SSL 骨干中间层插入轻量预测头实现早期退出，按本地约束与任务需求终止计算；并提出按层、深度感知的部分聚合。摘要称降低边缘开销、支持异构硬件，并在资源受限联邦环境保持有竞争力的性能。

**Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference**（论文 1668；Kentaro Onda）  
仅在下游推理使用软令牌分配，训练仍硬离散。摘要称在 ASR 与语音合成上优于硬分配，对域外数据泛化更强；非母语 ASR 甚至超过连续 SSL 特征；且表示与音素对齐更准。

**Gumbel-BEARD: Automatic Layer Selection for Self-Supervised Adaptation of Whisper in Low-Resource Domains**（论文 825；Abeer Alwan）  
端到端可训练硬 Gumbel-Softmax 选择器自动选择 Whisper 编码器层，并以 BEST-RQ 目标做自监督域适配。在 MyST 儿童语音上，摘要称用 10 小时标注微调即可匹配全量 133 小时全监督基线；MyST 上 Whisper-medium WER 8.21%，OGI Spontaneous 上 Whisper-small 11.06%；CORAAL 上相对 WER 最高降约 6%。

## 本场要点

- WavLM 声学信息高度冗余，子空间擦除比稀疏消融更有效。
- 显式注入音高/能量提升语用歧义下的情感识别。
- DysfluentNet 联合口吃事件检测与不流畅感知转写。
- 联邦早期退出与按深度聚合适配异构客户端。
- 推理期软令牌分配可弥补硬量化损失。
- Gumbel 层选择 + BEST-RQ 高效适配低资源儿童/方言域。

## 覆盖核对

| id | title |
|---|---|
| 3316 | Causal Redundancy in Speech Representations: The Hydra Effect and Limits of Sparse Disentanglement in WavLM |
| 3486 | Prosody-Aware Speech Representations for Emotion Recognition under Pragmatic Ambiguity |
| 696 | DysfluentNet: Joint Stuttering Event Detection and Dysfluency-Aware Transcription via Hierarchical Self-Supervised Learning |
| 2122 | Adaptive Federated Fine-Tuning of Self-Supervised Speech Representations |
| 1668 | Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference |
| 825 | Gumbel-BEARD: Automatic Layer Selection for Self-Supervised Adaptation of Whisper in Low-Resource Domains |
