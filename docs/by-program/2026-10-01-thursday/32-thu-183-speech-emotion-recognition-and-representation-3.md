# Speech Emotion Recognition and Representation 3

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：3
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场情感识别与表征从封闭标签走向开放词汇推理、模糊情感分布、边缘–云协作描述，以及说话人不变与跨语泛化。大音频语言模型带来更丰富输出，但细粒度声学时序、模糊性推理与部署隐私仍是短板。

方法上出现 utterance 感知声学 Q-Former、不确定度引导的投机解码、模糊感知目标与思维链、层向任务向量合并融合 ASR 知识、轻量多尺度 SE 块，以及熵对抗去说话人、条件 Transformer U-Net 音视频稳健识别、扩散桥矫正过/欠拟合表征。跨语属性（唤醒/效价/支配）适应所需数据量因任务而异，提示“低资源”阈值依赖目标属性。

## 技术内容

### 开放词汇、描述生成与模糊推理

**AcoustEmo: An Utterance-Aware Acoustic Q-Former for Open-Vocabulary Emotion Reasoning**（论文 2364；Liyun Zhang）提出带时间戳同步滑窗的 Utterance-Aware Acoustic Q-Former，抽取段级音频 token 以追踪微韵律与语调演变。在可解释多模态情感识别（EMER）上增强复杂情感推理，整体优于基线并保持语境准确。

**Edge–Cloud Collaborative Speech Emotion Captioning via Token-Level Speculative Decoding in Audio-Language Models**（论文 901；Ting Dang）提出 Uncertainty-Guided Speculative Decoding：轻量边缘模型本地起草，仅高不确定 token 块升至云端强验证器。MER2024 上 BLEU 最高提升约 62.7%，延迟降约 1.4×、吞吐约 8.5×，刻画质量–效率–隐私权衡。

**Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction**（论文 2031；Jiaheng Dong）将模糊情感识别重塑为分布推理，含对齐人类感知分布的模糊感知目标与结构化模糊感知思维链。在 IEMOCAP 与 CREMA-D 上，SFT/DPO/GRPO 均有一致改进。

### 知识融合、轻量结构与说话人/跨语稳健

**AdaLTM: Adaptive Layer-wise Task Vector Merging for Categorical Speech Emotion Recognition with ASR Knowledge Integration**（论文 80；Chia-Yu Lee）从域内 ASR 与 SER 微调模型提取任务向量，以层向可学习系数并入冻结 WavLM-Large 基座，在无梯度冲突下深度感知平衡语言与副语言知识。MSP-Podcast 上有效缓解 ASR–SER 冲突。

**SETEAB: Multiscale approach with Squeeze-and-Excitation Temporal Enhanced Aware Block for Speech Emotion Recognition**（论文 1208；Kiet Anh Hoang）结合深度可分下采样、SE 通道重标定与 Temporal Enhanced Aware Block，在基准 SER 数据上以更低算力提高准确率并增强跨语料表现。

**How Language-Independent Are Emotional Attributes? A Study on Training Data Scaling and Cross-Lingual Generalization**（论文 2143；Dániel Halmai）在英/普通话上训练与适应，考察唤醒、效价、支配。摘要称唤醒即使两小时适应仍有益；效价需 10–20 小时适应才可匹配约 100 小时单语模型，说明低资源边界因属性而异。

**SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training**（论文 2186；Eunseo Choi）以 wav2vec 2.0 为特征编码器、ECAPA-TDNN 为说话人判别器做熵对抗训练。IEMOCAP 上 UA 60.63%，优于基线 51.15% 与无说话人抑制的 wav2vec 2.0（56.46%）。

**Robust Audio-Visual Emotion Recognition via Conditional Transformer U-Nets with Frequency-Injected Visual Stream**（论文 2770；Hanwook Chung）双路卷积 Transformer U-Net 学习音/视瓶颈，融合解码情感；情感条件辅助解码重建中间特征。音频含逆滤波前端，视觉含频率注入空–谱建模。摘要称噪声混响下优于单/多模态基准。

**Diffusion Bridge Learning Between Overfitted and Underfitted Representations for speech emotion recognition**（论文 2996；Shi-wook Lee）用条件去噪扩散在样本与类原型间学习随机变换，配合配对对齐、循环一致与分类正则，重塑表征几何。英日跨语 SER 上加权平均召回最高分别 +6.42 / +4.00 个百分点。

## 本场要点

- 开放词汇与情感描述需要段级声学时序建模与边缘–云不确定度路由。
- 模糊情感应作为分布推理，并结合思维链监督。
- 任务向量层向合并可融合 ASR 知识而避免多任务梯度冲突。
- 说话人对抗与扩散原型桥接分别抑制说话人泄漏与过拟合域线索。
- 情感属性跨语适应的数据需求显著不同（唤醒 vs 效价）。
- 音视频条件 U-Net 面向噪声混响部署场景。

## 覆盖核对

| id | title |
|---|---|
| 2364 | AcoustEmo: An Utterance-Aware Acoustic Q-Former for Open-Vocabulary Emotion Reasoning |
| 901 | Edge–Cloud Collaborative Speech Emotion Captioning via Token-Level Speculative Decoding in Audio-Language Models |
| 2031 | Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction |
| 80 | AdaLTM: Adaptive Layer-wise Task Vector Merging for Categorical Speech Emotion Recognition with ASR Knowledge Integration |
| 1208 | SETEAB: Multiscale approach with Squeeze-and-Excitation Temporal Enhanced Aware Block for Speech Emotion Recognition |
| 2143 | How Language-Independent Are Emotional Attributes? A Study on Training Data Scaling and Cross-Lingual Generalization |
| 2186 | SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training |
| 2770 | Robust Audio-Visual Emotion Recognition via Conditional Transformer U-Nets with Frequency-Injected Visual Stream |
| 2996 | Diffusion Bridge Learning Between Overfitted and Underfitted Representations for speech emotion recognition |
