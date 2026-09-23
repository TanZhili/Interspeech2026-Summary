# Pathological Speech Assessment 4

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：13
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场病理语音评估从“单层 SSL 特征 + 私有协议”转向层偏好分析、跨语检索增强、统一可复现基准，以及与临床量表对齐的音素级评分与可解释声学关联。数据稀缺与协议碎片化是共同瓶颈；公开基准（PathBench、EarlyPD）试图让方法可横向比较。

表示学习上，Wav2Vec2 等模型经域适应后呈现维度特异的层偏好，可学习标量混合利用互补线索；跨语检索把另一语言的严重度锚定嵌入库融入分类。临床落地侧强调阿拉伯语音素评分与专家相关、早期帕金森检测的说话人独立划分，以及用典型相关分析揭示模型嵌入与 eGeMAPS 特征的对应关系。

## 技术内容

### SSL 层融合与跨语检索

**Uncovering Dimension-Specific Layer Preferences in Wav2Vec2 for Fine-Grained Perceptual Assessment of Dysarthric Speech**（论文 692；Zihan Zhong）先对 Wav2Vec2-Large 做无监督域适应，再在 Speech Accessibility Project 上对 25 个 Darley-Aronson-Brown 感知维度做逐层分析。最优层因维度而异，故用可学习标量混合融合所有层并超越单层基线；学到的权重显示与言语子系统分组一致的维度偏好。

**Cross-lingual Retrieval-Augmented Classification for Dysarthria Severity Assessment**（论文 2697；Taeyoung Jeong）提出 CRAC：监督对比学习塑造严重度聚焦嵌入空间，用对侧语言语料建向量库，训练与推理时检索 top-k 参考并以交叉注意力融合。在韩语卒中后与意大利语 ALS 构音障碍、说话人独立三分类协议下，摘要称平衡准确率分别为 87.3%/86.7%，相对单语基线提升 8.4/20.0 个百分点。

### 统一基准与临床对齐评分

**PathBench: Speech Intelligibility Benchmark for Automatic Pathological Speech Assessment**（论文 946；Bence Mark Halpern）发布基于公开数据集的统一病理可懂度基准，比较无参考、参考文本与参考音频方法，并设 Matched Content / Extended / Full 三种协议以对应语言学对照刺激与机器学习最大数据用法。建立六数据集基线，并提出 Dual-ASR Articulatory Precision（DArtP），摘要称在无参考方法中平均相关最高。

**A Benchmark for Early-stage Parkinson's Disease Detection from Speech**（论文 1057；Khiet P. Truong）针对 EarlyPD 定义、数据与协议不一导致结果难比，提出首个言语 EarlyPD 检测基准：说话人独立划分、覆盖三种常见言语任务与不同训练资源设定，并按数据集、聚合层级、性别与疾病阶段给出多维分解。摘要强调可复现参考与公开采用以推进临床有意义检测。

**Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment**（论文 3472；Ehsan Hoque）构建模块化阿拉伯语音素级发音评分：MSA 音素化、微调语音到音素模型、Levenshtein 对齐，以及最长公共子序列与编辑距离混合的评分器。最佳 OmniASR-CTC-1B-v2 音素错误率 8.92%；三位认证言语治疗师对 40 条话语独立评分，Harf-Speech 与专家均分 Pearson 0.791、ICC(2,1) 0.659，摘要称优于现有端到端评估框架。

**What Does a Pathological Speech Assessment Model Know about Acoustic Features? A Case Study on Oral and Oropharyngeal Cancer Patients**（论文 3343；Tuan Nguyen）对基于 Wav2Vec 2.0 的口/口咽癌患者可懂度评估模型做典型相关分析，度量嵌入与 eGeMAPS 低层描述符的相关。摘要称与频谱与韵律特征相关最强，第一 MFCC 系数在各层相关最高；组级频谱/韵律/音质相关分别为 0.77/0.71/0.65，并为病理评估的声学特征选择提供实践指引。

## 本场要点

- 细粒度构音障碍评估需要按感知维度选择或融合 SSL 层，而非默认单层。
- 跨语检索增强可在标签稀缺下借用另一语言严重度参考。
- PathBench 与 EarlyPD 基准推动公开、可复现的协议统一。
- Harf-Speech 展示与专家评分相关的阿拉伯语音素级临床对齐框架。
- CCA 解释表明病理评估模型更贴频谱与韵律类可解释特征。
- 说话人独立与多任务/多资源设定是临床迁移评测的关键设计。

## 覆盖核对

| id | title |
|---|---|
| 692 | Uncovering Dimension-Specific Layer Preferences in Wav2Vec2 for Fine-Grained Perceptual Assessment of Dysarthric Speech |
| 2697 | Cross-lingual Retrieval-Augmented Classification for Dysarthria Severity Assessment |
| 946 | PathBench: Speech Intelligibility Benchmark for Automatic Pathological Speech Assessment |
| 1057 | A Benchmark for Early-stage Parkinson's Disease Detection from Speech |
| 3472 | Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment |
| 3343 | What Does a Pathological Speech Assessment Model Know about Acoustic Features? A Case Study on Oral and Oropharyngeal Cancer Patients |
