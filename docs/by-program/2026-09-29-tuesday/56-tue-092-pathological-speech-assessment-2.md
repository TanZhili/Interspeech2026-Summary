# Pathological Speech Assessment 2

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：13
- **论文数**：7
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场聚焦病理/认知相关语音评估：痴呆筛查中用转写分数与 Whisper 嵌入融合降低评分误差并补偿缺失运动子测验；原发性进行性失语则用临床 grounding 的层次仿真缓解标注稀缺。多模态检测整合 ASR 声学嵌入与 LLM 增强语言学特征，或用 LoRA-LLM 对多视角语音派生信号做结构化推理。

表示学习侧提出病理感知神经掩码，迫使编码器学习分布式稳健表征而非捷径；图方法用语义/依存/共现多图与门控融合刻画叙述逻辑偏离。临床嗓音质量客观指标则通过盲去混响减轻房间声学对 CPPS 的扭曲。共同主题是：数据稀缺下的仿真与多视图融合，以及可解释、临床对齐的正则。

## 技术内容

### 认知筛查、失语仿真与痴呆多模态检测

**Mitigating Scoring Errors and Compensating for Nonverbal Subtests in Speech-Based Dementia Assessment**（论文 2806；Franziska Braun）  
面向德语 Syndrom-Kurz-Test：融合各言语子测验的转写分数与 Whisper 嵌入以降低评分误差，并用融合表征近似专家总分以补偿缺失运动子测验。摘要称即使省略子测验仍与专家评分强相关，并能区分认知状态组。

**HASS: Hierarchical Simulation of Logopenic Aphasic Speech for Scalable PPA Detection**（论文 3080；Harrison Li）  
针对 PPA 数据稀缺，提出层次失语语音仿真 HASS，由临床专家系统识别并仿真 lvPPA 在语义、音系与时间维度上的不同严重度缺陷，以支持更准确、可泛化的检测模型。

**Listening Between the Lines: Joint Learning of ASR Embeddings and LLM-Augmented Linguistics for Dementia Detection**（论文 939；Myungwoo Oh）  
Whisper 双通道提取编码器声学表征与 ASR 转写；语言学路径用 LLM 抽取词汇多样性、句法复杂度、语义连贯与话语模式等可解释特征，门控融合。在 ADReSS/ADReSSo 上摘要给出 F1，消融显示多模态优于单模态。

**LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features**（论文 952；Jonghyeon Park）  
在统一提示中编码带停顿标记的 ASR 转写、话题线索、时间流利统计与音系序列四视图，LoRA 微调单一 LLM 学习连贯决策而无模态专用编码器。在 ADReSSo 上摘要给出 F1，消融确认各视图互补。

### 病理掩码、多图融合与嗓音质量去混响

**PAN-Mask: Pathology-Aware Neurological Masking with End-to-End Learnable Weights for Neurological Disorder Detection from Speech**（论文 1006；Qi Sun）  
轻量检测器聚合六种可解释声学描述子估计帧级病理显著性，选择性掩码高显著性段以抑制捷径学习。在三障碍、五语言、六数据集相同超参下摘要称相对随机掩码有准确率增益，并提供可解释临床洞见。

**Gated Multi-graph Fusion via Graph Attention Networks for Alzheimer’s Disease Detection**（论文 2578；Xiao Wei）  
由 ASR 转写构建语义、依存与共现图（共现图用规范语料 PMI 量化叙述逻辑偏离），自适应门控融合应对症状异质性。在 ADReSSo 上摘要给出准确率，消融强调 PMI 图与异质性感知门控。

**From Echo to Accuracy: Robust Voice Quality Assessment Using Blind Unsupervised Diffusion-based Dereverberation**（论文 2608；Sven Franz）  
检验盲扩散去混响能否支持房间无关的 CPPS 嗓音质量评估。摘要称低混响录音去混响不引入系统 CPPS 偏置；混响条件下 CPPS 下降经处理后得到补偿，连续语音质量排序可重建并接近消声参考水平。

## 本场要点

- 语音痴呆筛查可用嵌入融合补偿转写误差与缺失非言语子测验。
- 临床层次仿真为 lvPPA 检测提供可扩展训练数据路径。
- LLM 增强语言学特征或多视图提示推理与声学表征互补。
- 病理感知掩码与多图门控融合提升可解释神经障碍/AD 检测。
- 盲去混响有助于客观嗓音质量指标在真实房间中的稳健性。

## 覆盖核对

| id | title |
|---|---|
| 2806 | Mitigating Scoring Errors and Compensating for Nonverbal Subtests in Speech-Based Dementia Assessment |
| 3080 | HASS: Hierarchical Simulation of Logopenic Aphasic Speech for Scalable PPA Detection |
| 939 | Listening Between the Lines: Joint Learning of ASR Embeddings and LLM-Augmented Linguistics for Dementia Detection |
| 952 | LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features |
| 1006 | PAN-Mask: Pathology-Aware Neurological Masking with End-to-End Learnable Weights for Neurological Disorder Detection from Speech |
| 2578 | Gated Multi-graph Fusion via Graph Attention Networks for Alzheimer’s Disease Detection |
| 2608 | From Echo to Accuracy: Robust Voice Quality Assessment Using Blind Unsupervised Diffusion-based Dereverberation |
