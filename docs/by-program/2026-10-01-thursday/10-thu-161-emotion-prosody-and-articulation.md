# Emotion, Prosody, and Articulation

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Long Oral
- Area：跨领域长文口头报告（Cross-area）
- 论文数：5
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场连接副语言感知、多模态情感融合与发音/声学工具：音频讽刺识别强调时间韵律不一致；联邦对抗学习同时护数据隐私与 SER 鲁棒性；多模态情感融合把“单模态精炼”与“跨模态交互”在架构上拆开；另两篇从发音地标库与交互式共振峰校正工具侧支撑可复现的发音与小语种语音学研究。

情感与韵律侧，局部韵律动态与整句情绪基线的错配成为可计算信号；不确定性估计与起终点定位无需帧级标签即可对齐人类感知。隐私与对抗威胁推动联邦学习 + 对抗训练 + 测试随机化的两阶段防御。多模态方面，纠缠式融合被替换为隔离通路、各自精炼、延迟全交互的先验。

发音与资源侧，用物理声道合成器按地标模式生成大规模带精确时间标注的词库，反转“地标标注稀缺”问题；面向少文献语言的交互式共振峰可视化与多算法校正，则把人工核验嵌入可复现工作流。

## 技术内容

### 韵律讽刺、联邦 SER 与多模态情感融合

**ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity**（论文 3451；Prathamjyot Singh）  
纯音频框架建模时间韵律不一致：全局情绪编码器与时间韵律编码器（BiLSTM + 多头注意力）汇入韵律不一致分析器得到标量分数；Monte Carlo dropout 估不确定性，注意力定位讽刺起始而无需帧级标签。MUStARD++ F1=75.3，自发 PodSarc F1=62.9，跨语 MuSaG F1=65.6；十次运行验证不一致建模贡献；人类评测显示不确定性跟踪感知歧义、起终点与人工时间窗对齐。

**A Two-Stage Defence for Robust Federated Speech Emotion Recognition**（论文 1125；Yi Chang）  
针对 IoT 场景语音上传隐私风险与对抗扰动导致情绪误判，提出联邦对抗学习：联邦学习保护本地数据，训练阶段对抗训练、测试阶段随机化提升鲁棒性。实验表明可本地保护语音数据，并对一系列对抗攻击增强模型鲁棒性。

**Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis**（论文 1299；Alexandros Potamianos）  
SeRIn 将单模态精炼与跨模态交互拆为架构先验：各模态沿隔离通路相对各自编码器上下文精炼，专用跨模态通路累积联合演化而不污染单模态流，全交互推迟到最终预测。消融表明结构化交互而非容量驱动增益；视觉损坏下门控分析出现无显式监督的模态再加权。在 CH-SIMS 与 CMU-MOSEI 上达 SOTA 并提升全部指标。

### 发音地标资源与声学测量工具

**An Acoustic Landmark Database of the English Lexicon via Articulatory Synthesis**（论文 1374；Mateo Cámara）  
用 Pink Trombone 物理声道合成器按地标模式生成英语词库（男女成人构型），在口腔闭合/释放等物理事件时刻算法放置地标标签；语料含 >200,000 合成词与时间对齐标注，并用 STOI 测可懂度。支撑词库尺度地标统计、主导线索模式及自动地标检测器训练/评测。

**NewAppVoice: Tools for Visualizing and Correcting Acoustic Measures**（论文 2560；Amélie Elmerich）  
面向少研究语言（复杂音段或类型学罕见特征）的语音学分析，整合多共振峰算法与信号—测量同步可视化，在算法处理中嵌入结构化人工核验，提升可靠性与可复现性。软件与衍生应用以开放获取方式提供。

## 本场要点

- 时间韵律不一致可作为纯音频讽刺检测的核心线索，并支持不确定性与起终点定位。
- 联邦学习与对抗训练/测试随机化可同时服务 SER 隐私与鲁棒性。
- 多模态融合宜在架构上分离单模态精炼与跨模态交互。
- 发音合成可规模化生成精确时间对齐的声学地标资源。
- 交互式多算法共振峰校正工具服务少文献语言的可复现研究。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 3451 | ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity |
| 1125 | A Two-Stage Defence for Robust Federated Speech Emotion Recognition |
| 1299 | Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis |
| 1374 | An Acoustic Landmark Database of the English Lexicon via Articulatory Synthesis |
| 2560 | NewAppVoice: Tools for Visualizing and Correcting Acoustic Measures |
