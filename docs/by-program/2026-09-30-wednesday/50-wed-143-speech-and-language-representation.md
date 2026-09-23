# Speech and Language Representation

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Poster
- Area：4
- 论文数：9
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场涵盖模仿语音说话人嵌入、语音表征是否编码语系结构、维度独立性的信息论度量、非言语发声上的说话人验证、声—脸关联图挖掘、神经转码后的传统编解码器溯源、阿联酋阿拉伯语人工标注语料、法证子带倒谱分析，以及低资源澳大利亚原住民语言识别的混合持续学习。

主线是表征中“身份—语言—情感/病理—编解码痕迹”如何纠缠与解耦，以及低资源方言/濒危语言如何获得可用资源与防遗忘适应。

## 技术内容

### 说话人嵌入、语系结构与维度独立性

**ECAPA-TDNN-based Speaker Embedding Framework for Voice Mimicry Assessment**（论文 1535；Bhasi K.C.）  
从频谱与韵律特征提取说话人嵌入评估模仿语音质量，并以感知测试最佳模仿艺人为目标做 DNN 预测（命中=模型输出匹配 MOS 最高艺人）。摘要称在 MIMICz 上基于增强 ECAPA 嵌入的方案优于其他嵌入方法。

**Do speech representational spaces encode language family structures?**（论文 2418；Emily Gaughan）  
比较六种树比较方法与探测分类器，评估六种常见语音编码器/LID 模型表征是否编码语系系统发育结构。摘要称树方法比探测分类器更能解释语系结构，不同表征对训练未见语言表现有差异。

**Quantifying Dimensional Independence in Speech: An Information-Theoretic Framework for Disentangled Representation Learning**（论文 1654；Bipasha Kashyap）  
用有界神经互信息估计量化手工声学特征跨维度统计依赖。摘要称六个语料上跨维度 MI 较低（估计界 <0.15 nats），而源—滤波器 MI 更高（0.47 nats）；归因分析显示情绪维度源主导（约 80%），语言与病理维度滤波器主导（约 60%/58%）。

### 非言语发声、声—脸关联与编解码取证

**Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach**（论文 77；Yi-Cheng Lin）  
冻结 Data2Vec + ECAPA-TDNN，并以域感知路由 MoE、条件蒸馏与对比损失桥接言语/NVV。摘要称覆盖 10 类 NVV，语音—NVV EER 从 38.93% 降至 22.66%，语音 EER 从 13.17% 降至 9.24%。

**GMOD: Voice-Face Association Learning via Graph Mining and Orthogonal Disentanglement**（论文 432；Ju Zhang）  
用全局相似图与课程引导挖掘发现潜在正样本，做多正样本对比学习，并以正交解耦提取跨模态共享身份特征。摘要称在 VoxCeleb 上显著优于 SOTA 无监督声—脸关联基线。

**Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding**（论文 2354；Shinee Youn）  
针对 RVQ 神经编解码转码掩盖传统压缩痕迹的问题，用 Transformer 建模 RVQ 层间因果与时序依赖以识别遗留编解码器。摘要称编解码器识别准确率超过 97%，并在 32–128 kbps 上保持稳健联合识别，说明传统痕迹在神经转码后仍可保留。

### 低资源语料、法证子带与持续学习

**Hamsa: A Manually Annotated Emirati Arabic Corpus for Speech and Language Technologies**（论文 1049；Shaikha Alsuwaidi）  
发布约 11 小时跨酋长国会话录音、母语者转写校验的迪拜/阿联酋阿拉伯语语料。摘要称微调多语 ASR 后 Whisper-v2 WER 从逾 40% 降至 25% 以下，可支持方言 ASR、翻译、字幕与呼叫中心等应用。

**Sub-band Cepstral Analysis of Speaker-Specific Information: A Case Study of Japanese Word /saN/**（论文 303；Shunichi Ishihara）  
用带限倒谱系数（BLCC）在 306 名男性日语 /s/、/a/、/N/ 上定位说话人敏感子带。摘要称元音与鼻音优于擦音，7–8 kHz 说话人信息弱；敏感子带随音段变化且不完全可由调音/声学特性预测。

**Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification**（论文 1789；Pravina Mylvaganam）  
提出回放增强 EWC 与约束引导知识蒸馏两类混合持续学习，以适应 Warlpiri、Dalabon、Dharawal 等低资源 AAL 语言识别。摘要称优于微调与既有 CL 基线，在适应多 AAL 同时保持先前高资源语言表现。

## 本场要点

- 模仿评估、NVV 说话人验证与声—脸关联都在推动身份表征跨域稳健。
- 语系结构与维度互信息分析提供表征几何/统计可解释性工具。
- 神经转码后仍可溯源传统编解码痕迹，拓展音频取证。
- Hamsa 等人工标注方言资源显著降低 Emirati ASR 错误率。
- 混合持续学习缓解濒危/低资源语言适应中的灾难性遗忘。

## 覆盖核对

- 1535 | ECAPA-TDNN-based Speaker Embedding Framework for Voice Mimicry Assessment
- 2418 | Do speech representational spaces encode language family structures?
- 1654 | Quantifying Dimensional Independence in Speech: An Information-Theoretic Framework for Disentangled Representation Learning
- 77 | Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach
- 432 | GMOD: Voice-Face Association Learning via Graph Mining and Orthogonal Disentanglement
- 2354 | Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding
- 1049 | Hamsa: A Manually Annotated Emirati Arabic Corpus for Speech and Language Technologies
- 303 | Sub-band Cepstral Analysis of Speaker-Specific Information: A Case Study of Japanese Word /saN/
- 1789 | Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification
