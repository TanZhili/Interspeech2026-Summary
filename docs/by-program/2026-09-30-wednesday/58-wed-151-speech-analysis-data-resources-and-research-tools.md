# Speech Analysis, Data Resources and Research Tools

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Show And Tell
- Area：未标注
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场为 Show and Tell，侧重可交互研究工具与数据资源：时序标注探索、轻量情感识别演示、模型辅助标注工作台、音素覆盖语料设计工具包、深度表征可视化对比，以及韵律驱动的实时多模态情感演示。共同目标是降低标注与表征验证门槛，并兼顾隐私部署与消费级算力。

工具形态从桌面/跨平台可视化（TSExplorer、Speech Playground）到浏览器实时演示（MER-Live），再到 pip 可装的语料优化库（corpusgen）与可私有化部署的 SpeechBench。功能上强调：高维特征多视图、模型预标注后人修、音素/双音素覆盖优化，以及连续/离散/变长表征并排比较。

效率与可达性并重：Light-DMF 参数少于 65k 且 CPU 实时因子低于 1；MER-Live 音频模型约 6.77M 参数经 TensorRT 加速。整体趋势是把实验室流水线产品化为可演示、可开源、可服务非技术用户的工作台。

## 技术内容

### 标注、探索与语料设计

**TSExplorer: An interactive data annotation and exploration tool for time-series data**（论文 3572；Einari Vaaras）  
跨平台时序数据交互标注与探索工具，由高维特征导出多类互补 2D 可视化，支持探索分析、无标/半标标注、特征表示比较，以及已有标签的事后检查与交互精修。

**SpeechBench: A Unified Speech Annotation and Analysis Tool**（论文 3600；Zheng Nan）  
面向“通用模型预标注 + 人工精修”的领域数据工作流，集成多类语音处理模型与图形化多步预标注管线，降低非技术用户门槛，并支持私有服务器部署以满足隐私要求。

**corpusgen: An Open-Source Toolkit for Phoneme-Coverage-Optimized Speech Corpus Design Across Languages**（论文 3603；Fariha Jaigirdar）  
开源 Python 工具包：espeak-ng G2P、PHOIBLE（2,186 语种）音素清单，以及 CELF 加速贪心集合覆盖、整数线性规划、分布感知选择与 NSGA-II 等多目标优化；可接 LLM API/本地 transformer 做音位控制造句，并报告音素/双音素/三音素覆盖。Apache-2.0，pip 安装，含 API 与 CLI；演示称覆盖优化可用显著更少句子接近最优覆盖。

### 轻量识别、可视化与实时演示

**Lightweight Emotion Recognition with Disjoint Modality Fusion**（论文 3593；Serkan Sulun）  
Light-DMF 以少于 65k 可训参数在音频与文本上独立分类并走融合通路，支持模态缺失或冲突标签的混合模态数据；CPU 推理实时因子低于 1，并开源代码与面向公众的演示。

**Speech Playground: An Interactive Tool for Speech Analysis and Comparison**（论文 3604；Stephen McIntosh）  
Python 后端 + Web 前端交互工具，探索连续、离散与变长等多种深度特征，含 TextGrid、强制对齐及可配置距离/对齐设置，支持视听对比，面向研究、表征验证与 CAPT 实验。

**MER-Live: An Interactive Browser Demo of Prosody-Driven Multimodal Emotion Recognition**（论文 3607；Haoyu Song）  
浏览器实时多模态情感演示，语音为主、视频与词汇辅助；声学支路为 log-mel 上轻量掩码自编码 SER（MSMC），文本仅作辅助决胜而非关键词触发。约 4 次/秒更新；可热切换十个说话人留出检查点、录 5 秒或上传对比。6.77M 音频模型 TensorRT FP16 下五句批 0.24 ms（H200），相对 PyTorch FP32 约 14×；IEMOCAP 10 折音频 MSMC 达 74.03% WA / 66.39% UA，多模态逾 83%。

## 本场要点

- 时序与语音标注工具强调多视图探索与“模型预标 + 人修”管线。
- corpusgen 把跨语种音素覆盖优化做成可安装工具包。
- 轻量情感与实时演示面向 CPU/浏览器部署与公众可达。
- Speech Playground 补齐深度表征与 Praat 类工具的交互对比缺口。
- 隐私敏感场景需要可私有化部署的标注分析一体工具。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 3572 | TSExplorer: An interactive data annotation and exploration tool for time-series data |
| 3593 | Lightweight Emotion Recognition with Disjoint Modality Fusion |
| 3600 | SpeechBench: A Unified Speech Annotation and Analysis Tool |
| 3603 | corpusgen: An Open-Source Toolkit for Phoneme-Coverage-Optimized Speech Corpus Design Across Languages |
| 3604 | Speech Playground: An Interactive Tool for Speech Analysis and Comparison |
| 3607 | MER-Live: An Interactive Browser Demo of Prosody-Driven Multimodal Emotion Recognition |
