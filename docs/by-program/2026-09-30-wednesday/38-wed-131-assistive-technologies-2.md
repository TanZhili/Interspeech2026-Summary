# Assistive Technologies 2

- 日期：2026年9月30日（周三）
- 时间：14:00-16:00
- 形式：Poster
- Area：13
- 论文数：10
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场围绕听力辅助、人工耳蜗仿真、耳语转换、聋人/重听用户视角、EMG 无声语音、构音障碍 ASR、双参考评测、个性化联邦学习，以及听声/想象语音的共享神经表征。

听力技术从“适应声学环境”走向用可穿戴设备估计现实世界聆听努力与疲劳；耳蜗侧既有随机神经响应的 DNN 近似，也有共振峰对声码语音可懂度相对重要性的实验。

无障碍与病理语音侧，耳语到正常语音强调低资源下对齐与生成解耦；构音障碍 ASR 在重度低可懂度、联邦个性化与“字面 vs 意图”双参考评测上同时推进。立场论文则强调聋人口音与可验证、公平的设计框架。

脑—机与无声接口方面，EMG 静默语音会自发形成音位表征；单被试 EEG 语料用于检验听觉感知与“内心语音”在音素级的对应。

## 技术内容

### 聆听努力、耳蜗模型与 CI 可懂度

**Steps toward a wearable-informed model of real-world listening effort and fatigue among adults with hearing loss**（论文 2022；David Meng）  
46 名听力损失成人完成 7–10 天现场研究，结合 Apple Watch EMA、被动心率与声音监测及每日手机问卷。摘要称用可穿戴特征分类高聆听努力与高疲劳准确率分别为 68% 与 76%，提示未来实时自适应助听与纵向监测的可行性。

**Towards a Stochastic DNN Approximation of Cochlear Implant Auditory Models**（论文 1872；Theresa Hartmann）  
用层级 VQ-VAE 将 Greenwood 型频谱图映射到 Gamma 分布参数，再采样得到概率均值率神经图，以逼近电刺激听觉模型的随机特性。摘要称在 JS 散度与神经图相似度指标下能捕捉全局时频谱结构与关键随机性质，尤在中低频。

**Relative Importance of Formants to the Intelligibility of Vocoded Speech in Cochlear Implant Simulation**（论文 143；Ying Cai）  
用保留前三共振峰轨迹的正弦波语音，并分别去掉其一。摘要称第二共振峰轨迹对可懂度贡献最大、第三最小，与宽带语音一致；但声码器包络截止频率与频带数会调节该相对重要性。

### 耳语转换、DHH 立场与 EMG 静默语音

**WhisperVC: Decoupled Cross-Domain Alignment and Speech Generation for Low-Resource Whisper-to-Normal Conversion**（论文 2002；Dong Liu）  
三阶段框架：有限成对数据学域不变语义；仅用正常语音学长度—通道对齐与说话人条件 mel 生成；再微调 HiFi-GAN。摘要称在 AISHELL6-Whisper 上 DNSMOS 3.07、UTMOS 2.83、CER 16.93%、WavLM 说话人相似度 0.95，并可用于隐私通信与术后康复等场景。

**Bridging the Speech AI Accessibility Gap for Deaf and Hard of Hearing People**（论文 3001；Christian Vogler）  
立场论文指出当前语音 AI 对聋口音与 DHH 使用场景关注不足，提出 UVG 与 FATE 设计框架，讨论非听觉核验、个性化声音身份保留，以及缺少 DHH 参与时的隐私与边缘化风险。

**Emergence of Phonetic Representations in EMG-based Silent Speech Interfaces**（论文 2499；Guillaume Toussaint）  
比较合成、识别、音素分类与无监督预训练等任务下的 EMG 表征。摘要称即使无显式监督也会形成音位表征；对声学目标的回归损失对可懂合成至关重要；仅对比自监督并不能在合成或音素分类上带来可测改进。

### 构音障碍 ASR、评测与个性化联邦学习

**Investigating ASR for Low-Intelligibility Dysarthric Speech**（论文 1326；Jun Wang）  
在单人大量低可懂度数据上，说话人依赖 BLSTM-HMM 与微调 Whisper 均达到 WER < 14%；将微调 Whisper 泛化到其他患者时，对重度构音障碍相对未微调模型改善 6.4 个百分点，且不损伤轻中度表现。

**What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR**（论文 750；Hawau Olamide Toyin）  
指出非典型语音存在字面转写与意图转写两种有效参考，多数评测混为一谈并奖励删除不流畅。摘要称在 11 个 ASR 模型上用双参考评估口吃语音，排名与表现显著分歧，强调应按用例选择参考。

**Towards Personalized Federated Learning for Dysarthric Speech Recognition**（论文 1559；Tao Zhong）  
探索参数平均与嵌入平均两类个性化聚合。摘要称在 UASpeech 与 TORGO 上相对正则化 FedAvg，WER 绝对最多降低 0.99%（相对 3.15%）与 0.56%（相对 4.73%）。

**Shared Phone-Level Neural Representations of Auditory Perception and ‘Inner Voice’ Production: One-to-One Mapping using a Single-Subject EEG Corpus of Heard and Imagined Natural Speech**（论文 2683；Scott Wellington）  
发布逾 22 小时单被试、时间对齐的听声与想象自然语言 EEG。摘要称想象语音诱发的音素 ERP 在向量空间上最接近对应听声音素 ERP，并可用凸二次优化加权子带改善一对一映射，为想象语音 BCI 提供方向。

## 本场要点

- 可穿戴 EMA 使现实世界聆听努力/疲劳建模成为可能。
- 耳蜗相关工作覆盖随机模型近似与共振峰相对重要性实验。
- 耳语转换强调对齐与生成解耦；DHH 立场强调可验证与公平设计。
- 重度构音障碍 ASR 在充足说话人依赖数据下可达较低 WER，并需双参考评测。
- EMG 与 EEG 工作分别揭示无声接口音位表征与听—想音素级对应。

## 覆盖核对

- 2022 | Steps toward a wearable-informed model of real-world listening effort and fatigue among adults with hearing loss
- 1872 | Towards a Stochastic DNN Approximation of Cochlear Implant Auditory Models
- 2002 | WhisperVC: Decoupled Cross-Domain Alignment and Speech Generation for Low-Resource Whisper-to-Normal Conversion
- 3001 | Bridging the Speech AI Accessibility Gap for Deaf and Hard of Hearing People
- 2499 | Emergence of Phonetic Representations in EMG-based Silent Speech Interfaces
- 1326 | Investigating ASR for Low-Intelligibility Dysarthric Speech
- 750 | What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR
- 143 | Relative Importance of Formants to the Intelligibility of Vocoded Speech in Cochlear Implant Simulation
- 1559 | Towards Personalized Federated Learning for Dysarthric Speech Recognition
- 2683 | Shared Phone-Level Neural Representations of Auditory Perception and ‘Inner Voice’ Production: One-to-One Mapping using a Single-Subject EEG Corpus of Heard and Imagined Natural Speech
