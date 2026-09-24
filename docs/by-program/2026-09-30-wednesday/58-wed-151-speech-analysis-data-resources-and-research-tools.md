# Speech Analysis, Data Resources and Research Tools

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Show And Tell
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为 Show and Tell，侧重可交互研究工具与数据资源：时序标注探索、轻量情感识别演示、模型辅助标注工作台、音素覆盖语料设计工具包、深度表征可视化对比，以及韵律驱动的实时多模态情感演示。共同目标是降低标注与表征验证门槛，并兼顾隐私部署与消费级算力。

工具形态从桌面/跨平台可视化（TSExplorer、Speech Playground）到浏览器实时演示（MER-Live），再到 pip 可装的语料优化库（corpusgen）与可私有化部署的 SpeechBench。功能上强调：高维特征多视图、模型预标注后人修、音素/双音素覆盖优化，以及连续/离散/变长表征并排比较。

效率与可达性并重：Light-DMF 参数少于 65k 且 CPU 实时因子低于 1；MER-Live 音频模型约 6.77M 参数经 TensorRT 加速。整体趋势是把实验室流水线产品化为可演示、可开源、可服务非技术用户的工作台。

## 论文技术总结

# TSExplorer: An interactive data annotation and exploration tool for time-series data

- 论文编号：3572
- 报告人：Einari Vaaras
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/vaaras26_interspeech.pdf

## 问题
时序数据（语音、视频、生理信号等）常用高维特征，但标注与分析往往顺序浏览或静态汇总，难以在特征空间中看清样本关系、比对不同表征或做增量标注。

## 方法
发布跨平台 GUI 工具 TSExplorer：离线提取高维特征后，在交互式 2D 散点图（t-SNE/PCA/UMAP）中浏览整库；点选样本联动音频/视频/波形/谱图等 widget。支持随机、顺序、farthest-first 采样与队列；可切换多种特征表征；标签用下拉或快捷键修改。布局可定制，widget/2DV/采样策略可扩展。Python + PySide6 + PyQtGraph，播放依赖 VLC。

## 实验与结果
正文以系统设计与资源开销为主：如 10 万×160 维 t-SNE 约 1.8 GB RAM、单核约 8 分钟；10 万语音样本预载音频与多特征约 5.1 GB，按需加载可 <0.4 GB；空闲约 0.3 GB。工具已开源，并引用先前工作 [6] 的描述与评估。

## 结论
提供面向时序数据的通用交互标注与探索环境，覆盖无标/半标/全标工作流及特征空间反馈，便于探索分析、标注与标签精修。

## 点评
把“特征空间导航 + 多视图检视”做成可扩展产品，贴合人机协同标注。本文偏工具介绍，量化用户研究细节主要指向此前论文；大库 2DV 预计算仍是使用门槛。


# Lightweight Emotion Recognition with Disjoint Modality Fusion

- 论文编号：3593
- 报告人：Serkan Sulun
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/sulun26_interspeech.pdf

## 问题
多模态语音情感识别常用大模型与重融合，部署成本高；真实场景中音频/文本可缺失或情绪线索冲突（如讽刺），需在轻量设定下同时支持单模态与融合预测。

## 方法
提出 Light-DMF：冻结 Distil-Whisper-large-v3 音频编码器与 MiniLM 文本编码器，用约 64k 可训参数做投影与注意力。四类 sentinel 标记模态有无；文本/音频自注意力各自出头，单向 audio→text 交叉注意力再与融合头拼接，输出 text/audio/fusion 三路预测。混合 IEMOCAP、MELD、CREMA-D、RAVDESS、TESS 与 GoEmotions，统一到 angry/excited/happy/neutral/sad；模态随机丢弃 0.1。推理复用 Whisper 一次前向得到特征与带时间戳转写，再按句并行分类。

## 实验与结果
正文未报告标准 SER 准确率表；强调可训参数 <65k，CPU（i7-5600U）上 1 分钟音频约 0.81 分钟处理（RTF<1）。提供 Colab demo 与开源代码。

## 结论
在极少可训参数与 CPU 实时下实现解耦单模态与融合情感预测，并可混训模态不全/冲突的数据，面向公众可用的轻量 SER 工具。

## 点评
“复用 ASR 内部特征 + 解耦头”对冲突线索与缺模态很务实，工程友好。作为 Show & Tell 向工作，缺系统对比与融合相对单模态的增益数字；情感标签粗映射也可能抹平细类差异。


# SpeechBench: A Unified Speech Annotation and Analysis Tool

- 论文编号：3600
- 报告人：Zheng Nan
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/nan26_interspeech.pdf

## 问题
通用语音模型预标注 + 人工精修可显著提效，但现有工具（Praat、Label Studio 等）或缺模型管线、或缺可视化串联、或强制上传公网，难满足领域数据与隐私需求。

## 方法
SpeechBench 采用 Docker 化前后端：Vue3 + WaveSurfer.js 浏览器前端；Python 后端集成 Parselmouth（类 Praat 分析）及 VAD、说话人分离、ASR、音素识别、强制对齐等预训练模块。用户在画布上拖拽模块组成有向预标注管线，输出直接映射为与波形/谱图对齐的 annotation tiers，再在工作区做人机精修与音高/共振峰/元音三角等分析。支持本地/私有服务器部署，含账号与项目管理。

## 实验与结果
本文为系统与演示描述：展示离线本地运行、会话语音预标注与 tier 编辑全流程；未报告独立定量用户实验。引用 AusKidTalk 等工作说明模型辅助标注可省时降本。

## 结论
在统一环境中接通“可视化多步预标注管线 + 交互精修 + 声学分析”，降低非技术用户门槛，并兼顾隐私敏感数据的本地部署。

## 点评
把管道编排与 tier 编辑做成一体，对准真实标注瓶颈。价值取决于内置模型质量与领域适配；正文未给出相对基线工具的效率对比数字。


# corpusgen: An Open-Source Toolkit for Phoneme-Coverage-Optimized Speech Corpus Design Across Languages

- 论文编号：3603
- 报告人：Fariha Jaigirdar
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/syed26_interspeech.pdf

## 问题
为 TTS/ASR 设计音素覆盖充分的语料仍常依赖语言特定、临时脚本；低资源语言尤缺统一的评估–选择–生成工具链。

## 方法
开源 Python 包 corpusgen：espeak-ng/Phonemizer 做 G2P，PHOIBLE 提供多语音素清单（文称覆盖 2186 语），CoverageTracker 维护音素/双音素/三音素计数。命令分为 evaluate（覆盖率、JSD/熵/PCD、饱和曲线）、select（greedy、CELF、stochastic greedy、ILP、分布感知、NSGA-II）与 generate（仓库检索 / LLM API / 本地模型 + 音位控制评分）。提供 pip、CLI、Python API，Apache-2.0。

## 实验与结果
演示跨英语、孟加拉语、阿拉伯语等流程，比较达 95%/100% 音素覆盖所需句数及 CELF 相对 greedy 的加速。正文称在 12 语系共 40 种语言上验证；强调覆盖优化选择可用显著少于随机基线的句子接近最优音素覆盖（具体数字以演示/视频为主）。

## 结论
把音素覆盖评估、集合覆盖式选择与缺口补全生成收成语言无关工具包，降低低资源语料设计门槛。

## 点评
算法菜单完整、基础设施（PHOIBLE+espeak）务实，对“一起说话”主题友好。G2P/清单映射误差与生成句自然度仍是风险；正文定量对比偏演示叙述，复现需依赖开源包与配套材料。


# Speech Playground: An Interactive Tool for Speech Analysis and Comparison

- 论文编号：3604
- 报告人：Stephen McIntosh
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/mcintosh26_interspeech.pdf

## 问题
Praat 等工具难方便接入现代深度学习表征并做句对比较；研究者常需拼编码器、对齐与临时可视化脚本。

## 方法
Speech Playground：SvelteKit 前端（Analysis 单轨 / Diff 双轨）+ FastAPI Python 后端懒加载模型。统一 encoder 接口覆盖 SSL、发音、音系特征、段级及 ZeroSyl 等可变长表征，可离散化；Diff 模式用 DTW 或段/离散对齐，可切换距离与全局/半全局匹配。支持 TextGrid、可选 MFA 强制对齐、录制与同步听对比。IndexedDB 管理本地样本库。

## 实验与结果
本文为工具介绍与 UI/工作流演示（含音系向量层、帧级 DTW 距离层、发音反演特征对齐等截图）；未报告独立基准实验数字。开源仓库与可选 mfa-service 已给出。

## 结论
在同一交互界面比较多种连续/离散/变长表征与对齐设定，服务语音研究、表征校验与 CAPT 向实验。

## 点评
Diff 模式把“听哪里不同、表征哪里不同”绑在一起，对 CAPT 与表征调试很贴切。扩展性依赖 encoder 插件生态；大模型加载与实时性权衡正文未量化。


# MER-Live: An Interactive Browser Demo of Prosody-Driven Multimodal Emotion Recognition

- 论文编号：3607
- 报告人：Haoyu Song
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26h_interspeech.pdf

## 问题
多数 SER 系统按离线、已知边界的段级 logit 平均评估；实时部署需要滑动窗、低延迟，并在不同速率下融合语音、视频与文本。现有演示也容易被误解为关键词分类。

## 方法
MER-Live 以语音为主、视频与文本为辅的浏览器实时多模态情感识别演示。声学分支 MSMC（约 6.77M 参数）输入最近 3 秒的 128×300 log-mel，经 Masked Auto-Encoder 在约 17.7k IEMOCAP 段上无标签预训练后四类微调；文本仅为 ASR 软概率的置信度加权 tie-breaker。各模态权重 \(w_m=2\max(0,(1-p^{neu}_m)-0.15)\)，经归一化与 EMA（α=0.20）及 0.10 滞后平滑。模型导出 TensorRT FP16；UI 每 250 ms 更新，支持十折 hold-out 热切换、5 秒录制平均、与开源 wav2vec 2.0 SER 基线并排对比。

## 实验与结果
10-fold IEMOCAP 上部署用音频 MSMC：74.03% WA、66.39% UA；多模态合成评估可超 83%。H200 上 batch 5 时 TensorRT FP16 0.24 ms，相对 PyTorch FP32 约 14×。合成视听文本概率下，音频相对 vision+text 基线约提升 6–9%。

## 结论
演示了轻量韵律主导的端到端实时多模态情感管线。局限包括：实时模式因 3 秒感受野准确率上限约 60%；ASR 文本分支依赖 Chrome/Edge；当前经明文 WebSocket，getUserMedia 需 localhost 或 TLS。

## 点评
把“同词不同调”做成可当场验证的交互，切中韵律主导主张。融合规则透明但多模态数字来自合成概率流而非真视频标注；实时与离线协议差距也说明部署评估需单独报告。

