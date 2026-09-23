# Audio-Visual and Multimodal Perception

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Long Oral（跨领域长文口头）
- **Area**：程序标注为 Cross-area long papers（本场 JSON 中 area 字段为空）
- **论文数**：5
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场从“多模态是否有效”转向“多模态如何贡献、是否真正泛化、是否像人一样感知”。音视频语音识别侧用 Shapley 归因拆解模态贡献，并在严格匹配分布的未见集上检验 LRS3 近乎完美分数是否反映真实泛化；视觉语音识别则对比模型与人类唇读在词/视位层的成功失败模式。

情感分析侧批评优化式模态平衡方法混淆拟合速度与判别贡献，主张用留出判别效用重新定义模态价值。听觉注意解码则发布面向移动对话场景的大规模多模态数据集，把生态效度与多生理通道纳入注意力与聆听努力研究。

共同主题是：诊断与评测协议优先于再堆叠架构；泛化、类人感知与模态效用估计成为下一阶段瓶颈。

## 技术内容

### AVSR 贡献归因与真实泛化

**Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition**（论文 417；Umberto Cappellazzo）  
AVSR 在噪声下利用声视觉信息，但模型如何平衡模态仍不清楚。提出 Dr. SHAP-AV，用 Shapley 值分析模态贡献，含 Global / Generative / Temporal Alignment 三类分析，覆盖六模型、两基准与不同 SNR。摘要称噪声下模型更依赖视觉，但即使严重退化仍保持高音频贡献；模态平衡在生成过程中演化，时间对齐在噪声下仍成立，SNR 主导模态加权；暴露持续音频偏置，并主张把 Shapley 归因作为标准诊断。

**Assessing True Generalisability of Audio-Visual Speech Recognisers**（论文 2583；Zhaofeng Lin）  
当前 AVSR 在 LRS3 上近乎完美，引发适应过拟合疑虑。从大规模 MultiVSR 子采样构建高度受控、未见评测集，严格匹配 LRS3 测试集的声学、视觉与人口统计分布。评估五种 SOTA 架构出现普遍性能崩溃；细粒度属性分析定位退化驱动因素，并揭示词汇偏置与音频视觉甚至落后于仅音频等现象。发布匹配测试集供后续基准使用。

### 类人唇读、MSA 模态平衡与移动场景 AAD 数据

**The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders?**（论文 2498；Rishabh Jain）  
VSR 在基准上超越人类唇读，但是否建立类人视觉语音感知仍存疑。在 MaFI 词级唇读数据上用词/字/音素/视位指标对比三系统与人类。摘要称模型虽总体更准，但成功/失败的词与人类不同；仅给少量起始音素的文本 n-gram 基线可媲美人类；词级错误更可由训练词频解释而非视觉信息量；模型在人类最难视位上获益最多，对视觉清晰度依赖更弱，表明更依赖训练语言线索而非视觉绑定。

**The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods**（论文 2556；Alexandros Potamianos）  
MSA 受模态不平衡制约，但领域仍依赖承诺过多的优化式平衡方法。给出统一评测框架、失败的理论诊断（混淆拟合速度与判别贡献），以及面向留出判别模态估值的研究议程。在 CMU-MOSI/MOSEI 上摘要称：无策略可靠优于 Late Concatenation；对超参敏感；比值校准亦难带来一致增益。核心论点是损失≠效用、梯度≠重要性。

**MOV-AAD: A Large-Scale Multimodal Dataset for Auditory Attention Decoding During Moving Conversations**（论文 3556；Nima Mesgarani）  
AAD 常在静态简化语音场景评测，与日常聆听差距大。MOV-AAD 面向移动、自然对话中的听觉注意：64 通道 EEG 与眼动、呼吸、皮电、心率、血氧、体温、体动、PPG 等同步生理记录，支持跨模态神经与生理标记分析。采用动态移动会话声源与注意参与行为测量，服务现实空间动态下的稳健 AAD、多模态注意建模、聆听努力与被试间神经响应等研究。

## 本场要点

- Shapley 归因显示 AVSR 在噪声下仍有持续音频偏置，SNR 主导模态加权。
- 分布匹配的未见集上 AVSR 普遍崩溃，质疑 LRS3 近完美分数的泛化含义。
- VSR 成功模式更贴近训练语言线索，而非人类式视觉感知。
- 优化式 MSA 模态平衡方法未可靠超越简单晚融合，需改用判别效用估值。
- MOV-AAD 为移动会话场景提供 EEG+多生理同步的大规模 AAD 资源。

## 覆盖核对

| id | title |
|---|---|
| 417 | Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition |
| 2583 | Assessing True Generalisability of Audio-Visual Speech Recognisers |
| 2498 | The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders? |
| 2556 | The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods |
| 3556 | MOV-AAD: A Large-Scale Multimodal Dataset for Auditory Attention Decoding During Moving Conversations |
