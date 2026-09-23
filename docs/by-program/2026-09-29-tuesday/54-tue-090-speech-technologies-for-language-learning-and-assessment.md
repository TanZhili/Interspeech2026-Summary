# Speech Technologies for Language Learning & Assessment

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：10
- **论文数**：12
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场面向语言学习与口语评测：口音会话 ASR 强调实体与填充停顿召回而非仅 WER；口语语法纠错把犹豫视为不确定信号而非噪声。水平评估从英语中级扩展到低资源巴斯克语 C1 判别，并比较多语言 SSL。

评分与反馈侧出现多代理多模态 SpeechLM 直接分析音频对齐 IELTS 构念、带自然语言理由的多粒度 SpeechLLM，以及用序数原型对齐替代大规模 MLLM 微调。发音检测诊断则从音系特征分解、语言特定混淆图、离散 token surprisal 到教师引导少样本无切分偏差建模，并转向以可懂度为中心的音段错误排序。

## 技术内容

### 口音 ASR、犹豫感知 GEC 与水平判别

**Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR**（论文 786；Fiza Husain）  
三阶段管线：启发式筛选高实体密度数据、区域 LoRA 适配器一次前向输出逐字与纠正转写、六类错误分类并由 LLM 裁判验证。摘要称印度/印尼/拉美口音测试上实体与填充召回显著提升，并匹配远更大零样本模型的实体表现。

**Exploring Hesitation as a Signal for Spoken Grammatical Error Correction**（论文 1869；Seunghoon Han）  
用特殊标记与犹豫类型嵌入保留不流畅信息。在 Speak & Improve Corpus 2025 上摘要称优于规则去不流畅与人工流利转写，犹豫邻近处增益更大。

**Discriminating Proficiency Levels in L2 Speech: A Comparative Study of Self-Supervised Models in Basque**（论文 1948；Christoforos Souganidis）  
检验多语言 SSL 能否判别低资源巴斯克语 C1；摘要称 mHuBERT-147 相对 wav2vec 2.0 xlsr 有统计显著提升，并在 ICNALE L2 英语上复现以示可重复。

### 多代理/可解释评分与序数对齐

**A Multi-Agent Framework to Automate Feedback Generation for IELTS Speaking Test using Multimodal SpeechLMs**（论文 1417；Hui Xin Koh）  
四角色代理对应评分准则，直接分析音频而无中间转写瓶颈。新建 IELTS 模拟考基准上摘要称与考官相关更高，反馈与专家语义更相似。

**A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales**（论文 2335；Aditya Kamlesh Parikh）  
量规引导 SpeechLLM，混合 SFT 与 Bounded DPO，联合预测句级准确/流利/韵律、词/音素准确并生成理由。在 SpeechOcean762 上摘要称可比单粒度模型；理由句级似真，词/音素级忠实度较弱。

**LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment**（论文 1346；Hong-Yun Lin）  
用潜空间序数原型对齐正则，配合从冻结 Whisper 自适应收割多层表征的 SALR。摘要给出 RMSE，称可媲美十亿级系统而无需 LLM 微调，并提供可解释准则对齐偏好。

**Adaptive Multimodal Expert Specialization by Meta-Learning for Spoken English Assessment**（论文 1650；Cong-Thanh Vu）  
元学习混合专家使子网络适配多样声纹剖面，以在少样本与隐私约束下个性化评分。摘要给出分类 F1 与回归 MSE。

### 发音检测诊断与可懂度导向

**Using Phonological-Level Wav2Vec2 for Mandarin Automatic Mispronunciation Detection and Diagnosis**（论文 869；Jinghao Chen）  
在统一 Wav2Vec2-CTC 中建模音段与声调属性。摘要称相对仅音素基线 FAR 与 DER 下降，并支持更细可解释反馈。

**Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs**（论文 3239；Hanh Nguyen）  
构建有向统计图学习音素混淆模式，并用语言特定策略捕捉不同 L1 系统差异。在 L2-ARCTIC 上摘要给出 F1。

**Light-weight Pronunciation Assessment via Discrete Speech Token Surprisal**（论文 1153；Shammur Absar Chowdhury）  
仅用母语资源训练：SSL+K-means 离散化，母语 token LM 算 surprisal，辅以 Text2DUnit–DTW 对齐特征。在 SpeechOcean762 与跨库 L2-ARCTIC 上摘要称接近监督基线。

**ALFreeD: Teacher-Guided Few-Shot Pronunciation Assessment via Segmentation-Free Deviation Modeling**（论文 3247；Meenakshi Sirigiraju）  
无需规范音素与边界：HuBERT 帧嵌入经 DTW 算学习者—教师偏差，i-vector 抑制非发音变异后 MLP 预测。在 SpeechOcean762 上摘要称以极少标注可比近期 E2E。

**Automatic Assessment of L2 Speech Intelligibility: Segmental Error Ranking**（论文 2522；Agnieszka Pludra）  
基于音素替换错误的回归与 AdaBoost 特征重要性，给出影响可懂度的音段错误排序，在多数据集人类评分上验证，强调可懂度优先于母语性。

## 本场要点

- 语言学习 ASR 需实体与填充召回，数据策展贡献可量化。
- 犹豫可作为口语 GEC 的有用信号而非应删除噪声。
- 低资源水平评估可借助多语言 SSL；IELTS 反馈走向多模态多代理。
- 可解释多粒度评分需兼顾理由似真与忠实；序数几何对齐可替代大规模微调。
- MDD/APA 从音系分解、L1 混淆图到无切分教师偏差与 surprisal 等多路径并行。
- 可懂度中心音段错误排序引导 CAPT 优先关键音素。

## 覆盖核对

| id | title |
|---|---|
| 786 | Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR |
| 1869 | Exploring Hesitation as a Signal for Spoken Grammatical Error Correction |
| 1948 | Discriminating Proficiency Levels in L2 Speech: A Comparative Study of Self-Supervised Models in Basque |
| 1417 | A Multi-Agent Framework to Automate Feedback Generation for IELTS Speaking Test using Multimodal SpeechLMs |
| 2335 | A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales |
| 1346 | LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment |
| 1650 | Adaptive Multimodal Expert Specialization by Meta-Learning for Spoken English Assessment |
| 869 | Using Phonological-Level Wav2Vec2 for Mandarin Automatic Mispronunciation Detection and Diagnosis |
| 3239 | Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs |
| 1153 | Light-weight Pronunciation Assessment via Discrete Speech Token Surprisal |
| 3247 | ALFreeD: Teacher-Guided Few-Shot Pronunciation Assessment via Segmentation-Free Deviation Modeling |
| 2522 | Automatic Assessment of L2 Speech Intelligibility: Segmental Error Ranking |
