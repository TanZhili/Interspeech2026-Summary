# Tools and Techniques for Phonetic Analysis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 2）
- 论文数：11
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场海报集中在语音学分析工具、弱监督边界/音素标注，以及发音生理与韵律接触现象。弱监督与大模型标注是主线：用停顿、音高重置与能量下降构建高精度韵律边界锚点做 PU 学习；ArtNet 以发音特征预测 + VIB 做零样本跨语音素识别；wav2VOT 把 wav2vec2 用于 VOT、闭塞时长与爆破实现自动估计。

对齐与样本量问题被量化：MFA 在 TIMIT 元音上的可靠声学测量存在特征相关的最小 token 门槛；同音异形词研究用时间归一化频谱图显示音段实现随语境意义分化。韵律与话轮方面，多语料证实话轮末词长时化主要落在末音节；跨语词汇重音检测比较单语/多语/跨语 SSL 特征与 Pre-net/Post-net。

发音侧结合 rtMRI 喉部分割（Mask2Former）与 EGG+喉镜观察澳式英语韵尾清塞音的声门策略；动态分析比较 Legendre 多项式与 GAMM 刻画接触诱发语调变体。监督规模上，G2P 自动音标仅在人类标注少于约 20–30 小时时有益，超过阈值 ASR 预训练更有效。工具化、弱监督与“多少数据才够”是共同关切。

## 技术内容

### 弱监督边界、跨语音素与自动语音学标注

**High-Precision Prosodic Boundary Anchors from Acoustic Cues under Weak Supervision**（论文 209；Hanyu Liao）
在无人工 ToBI 韵律边界时，用长停顿初筛、再以音高重置与能量下降收紧，得到重精度轻覆盖的边界锚点，并以 PU 学习估计连续边界强度。大规模日语语料实验表明可从声学线索恢复有意义的韵律边界模式。

**ArtNet: A JEPA-Like Articulatory Predictive Framework for Robust Zero-Shot Phoneme Recognition**（论文 304；Yaqian Zhou）
针对直接声学—符号映射易受语言特异变异影响，提出 ArtNet：从 SSL 特征预测通用发音表征，并用 VIB 抑制语言特异成分，配合向量空间音位清单对齐（VSIA）。七种未见语言上相对竞争基线显著降低 PER 与 PFER（摘要给出相对降幅 20.56% 与 7.01%）。

**wav2VOT: automatic estimation of voice onset time, closure duration, and burst realisation with wav2vec2**（论文 743；James Tanner）
用 wav2vec2 自动估计 VOT、闭塞时长与爆破实现；在未见数据上可比现有方法，微调后高精度，并跨塞音清浊与调音部位保持高保真，推动大语音模型进入语音学标注流水线。

**Time-normalized spectrograms reveal segmental differences in English heterographic homophones**（论文 793；Yu-Hsiang Tseng）
分析约 14,000 个异形同音词 token 的时间归一化频谱与 phone logits，发现对内音段实现有系统差异，且具体语音实现受话语语境意义塑造，更支持形式—意义在 token 级对齐的词库模型。

**Minimum Token Thresholds and Stabilisation for Reliable Automatic Vowel Alignment: Empirical Study on TIMIT Vowels and MFA**（论文 934；Simon Gonzalez）
以人工边界为金标准，增量采样 MFA 对齐的 TIMIT 元音，考察 Duration/F1/F2 可靠测量所需最小 token。85% 元音—特征组合随 token 增加显著改善；多数在约 50% 可用 token 处稳定，Duration 最早、F2 需最多数据。

### 韵律、话轮与跨语重音

**Word Lengthening as a Function of Utterance Position: A Multi-Corpus Study**（论文 1379；Mateo Cámara）
在英语、西班牙语四语料（>500 说话人）比较话轮末与句中词长：话轮末更长，匹配词、说话人内比较仍显著，效应主要落在末音节，作为地板交接的稳健局部线索。

**Multilingual and Cross-lingual Lexical Stress Detection Using SSL Feature Vectors**（论文 2914；Abdulrahman Alhabshi）
以固定 SSL 特征 + 音节级 Pre-net 与词语境 Post-net（TDNN）做阿拉伯语/英语词汇重音检测。多语训练接近单语准确率（英 97%、阿 90%）；跨语迁移有方向性；Post-net 提升鲁棒，多语预训练迁移最强。

**Reconciling Dynamic Data Analysis with Linguistic Reality: Comparing Legendre Polynomial Modelling and GAMM Applied to Prosodic Contact**（论文 2585；Angelo Dian）
以塞浦路斯希腊语与雅典希腊语延续升调为案例，比较 Legendre 多项式与 GAMM。两者都识别低核 ATG 样与高核曲率更大的 CYG 变体；多项式抓全局几何，GAMM 细相对时间（尤其核高目标），互补解释接触情境语调。

### 发音生理成像与音标监督规模

**Larynx segmentation in mid-sagittal speech production real-time MRI**（论文 1402；Xuan Shi）
提出基于 Mask2Former 的中矢状面 rtMRI 喉部分割管线，结合监督与半监督。约每被试 33–79 标注即可在 5% 边际增益阈值下足够；半监督有时反而下降。普通话声调样例研究展示捕捉内/外在音高控制与喉部收缩的能力。

**Achieving voicelessness in coda stop contexts: Insights from combined electroglottography and laryngoscopy**（论文 2610；Joshua Penney）
联合 EGG 与喉镜观察澳式英语韵尾清塞音的声门/喉设置。结果支持近期发现，并显示在短语末位置，所有调音部位清塞音更偏好收紧策略以实现清音。

**Scaling Human and G2P Supervision for Robust Phonetic Transcription**（论文 3271；Alexander Metzger）
在约 80 小时涵盖母语、非母语与中风后言语的英语基准上发现：G2P 监督仅在人类标注少于约 20–30 小时时有帮助；超过后无显著收益甚至损害跨方言鲁棒，而 ASR 预训练可大幅降低加权音素特征错误率。

## 本场要点

- 韵律边界与音素标注正大量转向弱监督锚点、PU 学习与 SSL/wav2vec2 工具化。
- 可靠自动对齐存在特征相关的最小 token 门槛，对低资源与社会语音学设计有直接含义。
- 同音词音段实现可随语境意义分化，挑战纯抽象音段符号观。
- 话轮末加长是跨语料稳健、主要位于末音节的韵律线索。
- rtMRI 分割与 EGG+喉镜把发音生理测量推向可复现管线。
- G2P 规模化有质量阈值；过阈值后应转向人类标注质量与 ASR 预训练。

## 覆盖核对

- 209 | High-Precision Prosodic Boundary Anchors from Acoustic Cues under Weak Supervision
- 304 | ArtNet: A JEPA-Like Articulatory Predictive Framework for Robust Zero-Shot Phoneme Recognition
- 743 | wav2VOT: automatic estimation of voice onset time, closure duration, and burst realisation with wav2vec2
- 793 | Time-normalized spectrograms reveal segmental differences in English heterographic homophones
- 934 | Minimum Token Thresholds and Stabilisation for Reliable Automatic Vowel Alignment: Empirical Study on TIMIT Vowels and MFA
- 1379 | Word Lengthening as a Function of Utterance Position: A Multi-Corpus Study
- 1402 | Larynx segmentation in mid-sagittal speech production real-time MRI
- 2585 | Reconciling Dynamic Data Analysis with Linguistic Reality: Comparing Legendre Polynomial Modelling and GAMM Applied to Prosodic Contact
- 2610 | Achieving voicelessness in coda stop contexts: Insights from combined electroglottography and laryngoscopy
- 2914 | Multilingual and Cross-lingual Lexical Stress Detection Using SSL Feature Vectors
- 3271 | Scaling Human and G2P Supervision for Robust Phonetic Transcription
