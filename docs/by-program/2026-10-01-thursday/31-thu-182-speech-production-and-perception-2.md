# Speech Production and Perception 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：1
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场海报连接语音产生/感知的声学线索、超声/MRI 发音成像、统一 ASR–TTS 连续表征，以及二语重音与肌肉动力学测量。一端是低资源语言的分类与音素发现，另一端是物理声道模型与深度学习自动化测量，共同强调“可观测发音证据”如何支撑识别、合成与教学。

声学上，辅音分类可受益于邻接元音中点共振峰等外在线索；发音侧则探索超声静默识别的物理一致性增强、清洁语音上的声学–发音反演，以及颏舌骨肌厚度的自动量化。学习系统侧出现统一 LLM（自回归 ASR + 流匹配 TTS）与极低资源类型学迁移音素发现。心理语言学与二语研究则检验词频/音节惊讶度与词重音时空手势协调。

## 技术内容

### 声学线索、超声与 MRI 反演

**Vowel Allophony Improves Maximum-Likelihood Classification of Warlpiri Consonants**（论文 3107；Coralie Cram）研究 Warlpiri（五部位塞音）说话人可用的声学线索。最大似然分类显示仅辅音内在线索不足；加入邻接元音的外在线索可提升 CV 与 VC 分类，且邻接元音中点共振峰的异音信息贡献最大。摘要讨论其对低资源语言基于概率感知模型生成预测的潜力。

**Towards Robust Ultrasound-based Silent Speech Recognition Learning Physics-Aware and Context-Rich Representations**（论文 2646；Qisheng Xu）针对超声舌成像伪影与复杂时序依赖，提出物理感知与上下文丰富表征：时间聚类下采样保关键上下文、物理感知增强对抗成像扰动，并以时间掩码与 3D 卷积+双向循环混合结构学习时空表征。摘要称显著优于基线，强调物理一致性与结构完整性。

**Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model**（论文 734；Sofiane Azzouz）比较同说话人、同句经语音切分对齐的去噪 MRI 语音与清洁环境录音。在去噪 MRI 上训练的模型于两类语音上评估，并另训仅清洁语音模型。摘要称清洁语音可有效支持发音反演，RMSE 1.56 mm，接近 MRI 表现。

**Automated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and UltrasoundAutomated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and Ultrasound**（论文 1664；Alisher Myrgyyassov）提出 SMMA：深度学习分割+骨架厚度量化自动分析颏舌骨肌动态。验证 Dice 0.9037、MAE 0.53 mm、r=0.901。粤语元音（N=11）显示 /a:/ 厚度显著大于 /i:/（7.29 vs 5.95 mm），与下颌下压作用一致；性别差异约 5–8%。

### 统一模型、低资源音素与韵律产生

**UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models**（论文 2194；Wenhao Guan）用连续表征统一 ASR 与 TTS，避免离散分词信息损失；双注意力掩码在 ASR 因果与 TTS 双向间切换，并以文本前缀引导的语音填补支持零样本克隆。摘要称相对 SOTA 单任务模型具竞争力或更优。

**How do word frequency and syllable surprisal affect response time and acoustic duration in sentence formulation?**（论文 1080；Ivan Yuen）在德语中考察词频与音节惊讶度对反应时与元音时长的跨层交互。假设加性效应，但结果呈选择性交互，取决于词为单/双音节，挑战离散、分阶段、串行跨层加工假设。

**Extreme Few-Shot Phoneme Discovery for Indigenous Australian and Pacific Languages via Typological Transfer Learning**（论文 284；Prasanth Yadla）在不足一小时音频上，经语音清单重叠选择源语言的 Typological Anchor Selection，从高资源南岛语做 VQ-VAE 类型学迁移。三语濒危数据上相对多语自监督基线，NMI 提升 18.8%，簇纯度提升 15.6%。

**Lexical stress-conditioned spatiotemporal gestural coordination in L2 English**（论文 3116；Paul McGuire）用电磁发音仪与多元函数主成分及地标时间对齐，分析台湾华语说话人 L2 英语词重音的时空手势协调。六人中四人在 FPCA 分数空间显示重音条件可分，口音最重的两人则否。

**Articulatory Dynamics using Physical Vocal-tract Models**（论文 840；Takayuki Arai）用可改变构型的物理动态声道模型，以不同发音 timing 集合产出给定词，从发音音系学视角展示言语动态方面，服务语音学教学与病理等相关场景。

## 本场要点

- 低资源辅音对比分类可显式利用邻接元音异音线索。
- 超声 SSR 与颏舌骨肌自动测量把成像物理约束带进学习与临床量化。
- 清洁语音可接近 MRI 训练模型的发音反演精度。
- UniVoice 展示连续表征下 ASR/TTS 统一与掩码切换。
- 极低资源音素发现依赖类型学锚定迁移。
- 二语重音与跨层可预测性效应提供产生机制的实证约束。

## 覆盖核对

| id | title |
|---|---|
| 3107 | Vowel Allophony Improves Maximum-Likelihood Classification of Warlpiri Consonants |
| 2646 | Towards Robust Ultrasound-based Silent Speech Recognition Learning Physics-Aware and Context-Rich Representations |
| 734 | Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model |
| 2194 | UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models |
| 1080 | How do word frequency and syllable surprisal affect response time and acoustic duration in sentence formulation? |
| 284 | Extreme Few-Shot Phoneme Discovery for Indigenous Australian and Pacific Languages via Typological Transfer Learning |
| 3116 | Lexical stress-conditioned spatiotemporal gestural coordination in L2 English |
| 1664 | Automated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and UltrasoundAutomated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and Ultrasound |
| 840 | Articulatory Dynamics using Physical Vocal-tract Models |
