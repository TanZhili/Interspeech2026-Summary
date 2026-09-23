# Spoofing and Deepfake Detection 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 4）
- 论文数：10
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场反欺骗/深度伪造检测同时覆盖被动检测、主动防御、数据集多样性与攻击面扩展。数据侧共识是“多样性重于盲目扩规模”：固定生成方法下过度扩容可能损害跨域泛化；SEA-Spoof、LRLspoof、MultiAPI Spoof 分别补东南亚六语、66 语（含低资源）与约 30 个商业/开源 API 的覆盖，并暴露高资源训练模型的跨语退化与语言作为独立域移来源。

方法上，韵律监督掩码预测（ProSDD）提升对表情/情感伪造的泛化；域不变韵律特征在真实诈骗电话零样本/少样本设定提供轻量替代，而 HuBERT/wav2vec2.0 在有真实样本时更高。域泛化用 GMM 式偶然风格不确定性增强；主动防御 FreqGuard 以频域先验生成不可感知扰动干扰合成。

攻击面不限于分类器：Ouroboros 展示语音增强模型可被干净音频自触发后门；KEYAC 评估语音表征学习在键盘声学侧信道与 VoIP 编解码下的泛化，并用 KAN 微调。瓶颈是真实犯罪/低资源数据稀缺、表情攻击、API 异构与前端模块新威胁。

## 技术内容

### 跨域特征、数据规模与表情鲁棒检测

**Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection**（论文 1975；Jeongmin Lee）
在演员情景录音训练、真实犯罪来电测试的跨域设定比较域不变韵律特征与 HuBERT/wav2vec2.0。韵律特征零样本 F1 69.5%、5-shot 71.0%；HuBERT 5-shot 最高 94.2% F1；wav2vec2.0 呈高精度取向。结论：无真实数据时域不变特征可部署，SSL 更高但需真实样本与算力。

**Exploring the Scale and Diversity of Speech Anti-spoofing Datasets: Experiments and Analysis**（论文 157；Zhuolin Yi）
解耦训练数据规模与多样性：固定生成方法下过度扩规模收益可忽略甚至损害跨域泛化；含多样攻击的较小复合集在跨数据集评估上显著优于大规模低多样性集。主张未来数据集优先生成方法多样性。

**ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks**（论文 831；Aurosweta Mahapatra）
两阶段框架：先在真实语音上做说话人条件韵律（音高、VAD、能量）监督掩码预测，再与欺骗分类联合优化。ASVspoof 2019/2024 训练下均降低 2024 EER，并在 EmoFake 与 EmoSpoof-TTS 上相对降幅达 50%。

### 侧信道、后门与主动防御

**Impact Analysis of Speech Representation Learning Models for Acoustic Side-Channel Attack**（论文 3500；Orchid Chetia Phukan）
发布 KEYAC 数据集，在标准与 VoIP 编解码下评估六种表征模型零样本/部分微调。部分微调有提升但跨编解码泛化困难；改用 Kolmogorov-Arnold Networks 微调持续优于基线并刷新 KEYAC。

**Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers**（论文 455；Yunjie Zhou）
针对语音增强被动处理特性，提出以理想干净输出为自然触发、无需外部注入的后门框架。多样模型/数据上攻击成功率近完美且性能退化极小；物理世界未改干净录音可激活，并可推广到内容篡改，对常见过滤与微调防御仍有效。

**FreqGuard: Leveraging Frequency-Domain Feature Priors for Universal Proactive Voice Defense**（论文 2069；Yankai Wang）
用可学习频域特征先验生成不可感知扰动，破坏说话人嵌入并干扰合成系统；联合多损失追求高不可感知性与低说话人相似度。黑盒 TTS 上降低攻击成功率，并称跨模型泛化与感知质量优于既有方法。

### 多语/多 API 数据与域泛化

**SEA-Spoof: Bridging the Gap in Multilingual Audio Deepfake Detection for South-East Asia**（论文 3019；Jinyang Wu）
首个面向泰米尔、印地、泰、印尼、马来、越南六语的大规模音频深度伪造检测集（>700 小时成对真实/伪造）。基准显示高资源训练模型跨语严重退化，在 SEA-Spoof 上微调可恢复跨语与跨合成源性能。

**When Spoof Detectors Travel: Evaluation Across 66 Languages in the Low-Resource Language Spoofing Corpus**（论文 345；Kirill Borodin）
LRLspoof 含 24 个开源 TTS、66 语共 2,732 小时。对 11 种公开对抗措施做阈值迁移并报告 spoof rejection rate，显示跨语拒绝率差异显著，语言本身是欺骗检测域移来源。

**MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection**（论文 1187；Xueping Zhang）
Multi-API Spoof 约 230 小时、30 个 API（商业/开源/在线平台）；提出 Nes2Net-LA 增强局部上下文，并定义 API tracing 任务。Nes2Net-LA 在多样未见欺骗条件下更鲁棒。

**Aleatoric Style Uncertainty Augmentation with GMM for Domain Generalization in Anti-spoofing**（论文 582；Jin Li）
用 GMM 建模风格分布多峰，提出基于分量内变异的偶然风格不确定性增强及端到端在线 EM 式更新。在反欺骗与 SASV 上显著优于既有方法。

## 本场要点

- 反欺骗数据建设优先级从“更大”转向“攻击/语言/API 更多样”。
- 表情与情感伪造需要显式学习真实语音韵律变异，而非只拟合数据集伪影。
- 真实诈骗场景下，轻量域不变韵律特征与重型 SSL 存在可部署性—精度权衡。
- 东南亚与低资源多语语料揭示高资源检测器的跨语脆弱性。
- 语音增强等前端可成为干净音频触发的后门载体，威胁面扩大。
- 主动频域扰动防御与 GMM 风格不确定性增强分别从攻防与泛化两端补强。

## 覆盖核对

- 1975 | Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection
- 157 | Exploring the Scale and Diversity of Speech Anti-spoofing Datasets: Experiments and Analysis
- 831 | ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks
- 3500 | Impact Analysis of Speech Representation Learning Models for Acoustic Side-Channel Attack
- 455 | Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers
- 2069 | FreqGuard: Leveraging Frequency-Domain Feature Priors for Universal Proactive Voice Defense
- 3019 | SEA-Spoof: Bridging the Gap in Multilingual Audio Deepfake Detection for South-East Asia
- 345 | When Spoof Detectors Travel: Evaluation Across 66 Languages in the Low-Resource Language Spoofing Corpus
- 1187 | MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection
- 582 | Aleatoric Style Uncertainty Augmentation with GMM for Domain Generalization in Anti-spoofing
