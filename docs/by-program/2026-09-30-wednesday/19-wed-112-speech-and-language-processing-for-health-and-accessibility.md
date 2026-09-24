# Speech and Language Processing for Health and Accessibility

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Show And Tell
- Area：
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以健康与无障碍场景下的可演示系统为主，突出“把评估、采集与处理搬到临床或自然场景”的工程落地。听力学方向出现两条互补路径：一是用游戏化、浏览器端或 VR 沉浸式体验，让听者直观感受噪声中聆听与掩蔽差异；二是面向单侧聋（SSD）等特殊需求定制侧向波束形成硬件，弥补传统助听器前向指向性不足。

儿童语言与发展研究侧则强调开放工具链：从儿童中心音频的标准化、说话人分离与发声指标提取，到头戴相机的可穿戴采集与本地 AI 标注，目标是降低对高级编程与人工标注的依赖，支撑大规模、可复现的自然场景研究。

临床语音分析方面，嵌入式床旁平台试图把采集、分析与报告收拢到同一设备，以服务精神疾病等场景的即时决策；同时出现对“增强后再做临床生物标志物分析”的警惕——可懂度提升并不自动等价于标志物保真，临床感知成为语音增强设计的约束。

构音障碍 ASR 则采用两阶段 Conformer 个性化适配，在数据稀缺与说话人高变异条件下，把通用病理性词汇适应与快速个性化串联到移动端平台，体现无障碍通信从模型到产品的闭环。

## 论文技术总结

# Sound Reactor Mission: Gamified Misophonia Assessment to Bridge the Gap in Audiology and Hearing Care

- 论文编号：3573
- 报告人：Jorge Mejia
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mejia26_interspeech.pdf

## 问题
恐声症（misophonia）常见且影响言语理解，但听力学缺少可扩展、标准化的客观评估路径；现有工具多为问卷，实验室 SIN/ANL 难规模化。

## 方法
浏览器游戏化任务 Sound Reactor Mission（约 6 分钟）：耳机校准 → 自适应估计 VCV 音节 SRT → 从日常声音库自选最恼人“Premium Fuel”掩蔽 → 在个人 SRT 下比较自选/包络合成/标准调幅噪声三种掩蔽的言语识别 → ANL。会场演示可现场完成并看群体仪表盘。

## 实验与结果
试点 N=14，完成率 100%，均时 6.5 分钟；SRT 均值 −9.4 dB SNR（SD 2.2）。六人完整比较：自选掩蔽可懂度 59.2%，合成包络 71.7%，标准噪声 86.3%；ANL 对自选最低。吸吮声等为常见自选掩蔽，个体差异大。

## 结论
游戏化可在非实验室条件下量化个人显著声音对言语理解的额外代价（超纯声学），为听力保健与噪声抑制算法提供可扩展筛查入口。

## 点评
把恐声症从问卷推进到个性化掩蔽 SIN，演示友好。强在三掩蔽对照暗示注意/情感成分；弱在试点极小、部分听者 SRT 触顶，规模化常模与临床效度仍待建立。


# An Immersive VR System for Experiencing Spatial Speech-in-Noise Challenges in Clinical Audiology

- 论文编号：3582
- 报告人：Nicky Chong-White
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chongwhite26_interspeech.pdf

## 问题
临床听阈与言语分数难以让患者/家属体会嘈杂咖啡馆等真实沟通困难，咨询效果受限；现有听力 VR 多偏评估或验配，缺少便携的咨询演示工具。

## 方法
在 Apple Vision Pro 上用 RealityKit 空间音频呈现咖啡馆、火车站、客厅三场景：目标话者、竞争话者与环境噪声空间定位；短对话后做理解选择题。临床者可选 Easy/Medium/Hard（竞争源数量、距离/有效 SNR）。支持语音/注视/手势作答，无需消声室或扬声器阵。定位为演示而非诊断。

## 实验与结果
向 N=8 名临床/业界人士演示完整流程；用户感知难度随预设上升，可用性反馈正面；尚未做听障用户正式评测或预设感知差的量化验证。

## 结论
便携沉浸式演示可为康复咨询提供共享体验参照；后续需听障用户与多平台验证，并可扩展到标准化评估。

## 点评
把“听得见分数”变成“听得到场景”，切中咨询鸿沟。强在无实验室依赖与语音交互适老化；弱在样本极小、非诊断且无听障验证，空间保真度相对真阵列仍未知。


# ELSI: An Interface for Standardizing Child-Centered Datasets, Applying Machine Learning Models, and Extracting Metrics

- 论文编号：3583
- 报告人：Kaveri K. Sheth
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheth26c_interspeech.pdf

## 问题
儿童中心长时录音（LFR）语料目录/元数据不统一，开源模型需编程门槛，商业 LENA 闭源；发展研究者难系统比较发声/轮次等指标可靠性。

## 方法
开源网页界面 ELSI：底层 ChildProject 自动标准化语料；一键跑 VTC（说话人类型切分）与 ALICE（成人音素计数等）；导出儿童/其他儿童/男女成人发声与对话轮次及音素/音节/词计数。重计算在机构服务器，用户浏览器访问，无需本地 GPU。Show and Tell 演示存档→处理→CSV。

## 实验与结果
正文为系统与流程说明，报告经 ERC 资助试点与合作语料试用；未给出大规模基准数字。强调降低技术门槛以支持低资源语言社区参与跨语料比较。

## 结论
ELSI 作为共享基础设施，把标准化、模型与指标串成可复现流水线；计划扩展模型与可持续托管。

## 点评
面向发展心理学而非工程用户，把 ChildProject/VTC/ALICE 包进 GUI，对“一起说话”主题很贴。强在开放与去编程化；弱在依赖中心服务器、指标仍受底层模型质量约束，正文缺定量验证。


# Demonstration of Embedded Systems for Clinical Speech Analysis

- 论文编号：3592
- 报告人：Jeremiah B Joyce
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/joyce26_interspeech.pdf

## 问题
精神/神经科临床语音分析常依赖需上传云端或专用 GPU 的流水线，延迟与 IT/隐私障碍限制床旁决策采用。

## 方法
在 NVIDIA Jetson AGX Orin（ARM CPU + Ampere GPU，约 60 W）上本地跑端到端临床会话分析：pyannote VAD/日志、角色分配、WhisperX ASR、强制对齐、音节核检测、情绪识别等；麦克风采集，显示器展示语速、轮次、词级时间戳与频谱，可用 ELAN 人工校正后重算。演示床旁即时处理。

## 实验与结果
正文为演示与系统能力说明，称可快于实时本地处理；未报告大规模临床准确率新实验（方法细节指向既有工作）。作者称据其知是首次用嵌入式设备做临床语音分析演示。

## 结论
边缘嵌入式可集成采集–计算–显示，降低延迟与数据外传，适合 IT 薄弱门诊与低资源场景；硬件进步使变压器级模型可近实时落地。

## 点评
把“能跑起来的床旁流水线”本身作为贡献，切中临床采用瓶颈。强在隐私与离线；弱在无新的临床效度数字、单设备功耗与噪声环境鲁棒性仍需现场验证。


# The TinyExplorer Ecosystem: Open tools for studying infants’ auditory and visual experiences

- 论文编号：3597
- 报告人：Cátia M Oliveira
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/oliveira26c_interspeech.pdf

## 问题
婴儿日常视听学习环境需 egocentric 头戴摄像，但缺轻量安全硬件，且人工标注视听耗时；长时音频工具难捕捉具身社交交互。

## 方法
开源 TinyExplorer：Gear 用 Insta360 GO 3（1080p/50 fps，水平约 80°、垂直约 116° 视场）采第一人称视频；Detection App 本地跑 AI 标注（敏感数据不上云）。已集成人脸检测（评测 13 种 DeepFace 算法，YOLOv11Face/RetinaFace 优）；手检测（100DOH 等）与 CDI 具体名词关键词 spotting（BabyHuBERT+Whisper）在扩展中。

## 实验与结果
关键词流水线相对人工标注 recall 78%、precision 77%，接近标注者间一致（均值约 82%）。人脸/手检测基准结果指向既有研究 [5,7]；完整多模态一体化仍在推进。

## 结论
硬件+本地 AI 生态旨在可扩展、可复现地研究儿童真实多模态输入；下一步融合姿态/物体与音频，形成“谁在说、做什么、说什么”的整合刻画。

## 点评
把头戴视场（尤其垂直）与本地隐私标注绑成生态，对语言习得具身研究很实用。强在开放与关键词近人类一致；弱在部分模块尚未完全集成进 App，工程成熟度仍演进中。


# Head-Worn Dipole Microphone Array-based Speech Enhancement System for Single-Sided Deafness

- 论文编号：3601
- 报告人：Ken Takaki
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/takaki26_interspeech.pdf

## 问题
单侧聋（SSD）最难听的是聋侧侧向语音，而常规助听器/眼镜阵列多为前向指向，侧向增强硬件与处理不足。

## 方法
眼镜侧梁线性阵：4 全向 MEMS + 4 偶极（开口朝内外，约 11 mm 声程）；假头消声室测传递函数；16 kHz MVDR 波束形成。仿真：TIMIT 目标扫方位，语音形噪声自 ±45°/±135°，比较单麦、三全向 BF、三偶极 BF、2 偶极+1 全向 BF。演示实时 BF 与耳机输出。

## 实验与结果
90° 侧向：三全向 / 三偶极 / 2 偶极+1 全向 SDR 约 2.28 / 3.24 / 3.06 dB，ESTOI 约 0.453 / 0.484 / 0.495；相对共址三全向，2 偶极+1 全向约 +0.78 dB SDR、+0.04 ESTOI（摘要）。偶极相关 BF 在 −45°–0° 亦常优于纯全向 BF。

## 结论
侧向偶极阵列可提升 SSD 关键侧向可懂度相关客观指标；演示用于传播 SSD 需求与偶极麦特性。

## 点评
把阵列指向从“朝前”改到“朝聋侧”，问题定义清楚。强在假头实测+客观指标；弱在仿真用 oracle 噪声协方差、未报告真人 SSD 听力试验。


# BetterSpeak: An Atypical Speech to Typical Speech Platform for Dysarthric Speakers

- 论文编号：3605
- 报告人：Seyed Reza Shahamiri
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shahamiri26_interspeech.pdf

## 问题
构音障碍（尤其儿童）语音变异大、数据稀缺，通用 ASR（如 Whisper）在重度病例上 WER 可很高；需要可手机部署的个性化识别并配合 TTS 辅助沟通。

## 方法
BetterSpeak 移动平台 + 两阶段个性化 Conformer：Phase1 用健康对照（UASpeech/TORGO 等）做词汇域适应；Phase2 用入职少量用户录音仅微调靠近声学输入的编码器层。识别文本可 LLM 润色后 TTS 朗读；支持隐私模式停存录音、监护人纠错反馈持续更新模型。

## 实验与结果
管线前期评估平均 WER：UASpeech 21.5%、TORGO 12.7%，优于先前 Seq2Seq。平台本身尚处伦理批准后的开放试验计划（唐氏/脑瘫等），未在本文报告新的现场儿童试验数字。

## 结论
数据高效个性化适配使构音障碍 ASR 可做成可及辅助技术；计划公开试验后对全体构音障碍用户开放。

## 点评
把已发 Conformer 适配接进儿童可用 App，闭环采集–适应–TTS。强在少样本防过拟合设计；弱在公开儿童构音库缺失、本篇以演示/平台为主，现场效度待试验。


# ClinAware: Speech Enhancement Needs Clinical Awareness

- 论文编号：3611
- 报告人：Pramod H. Kachare
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kachare26_interspeech.pdf

## 问题
远程/居家神经语音评估常先做增强再提生物标志物，但增强为可懂度优化可能扭曲停顿、音高变异、jitter 等临床相关特征，影响下游解读。

## 方法
交互演示 ClinAware：同一噪声语音经保守谱门控、激进平滑、预训练 DEMUCS 等增强；提取 pause ratio、F0 均值/标准差、谱质心标准差、jitter、shimmer、语速等；加权归一化成可解释风险探针（非诊断）。浏览器对比频谱、标志物漂移与风险分变化。

## 实验与结果
示例显示方法依赖的漂移：基线风险升幅有限；激进平滑改变细尺度音高但抬高谱不稳定；DEMUCS 放大音高/能量动态并显著抬高风险分。作者称多条录音趋势类似；无临床诊断效度声明。

## 结论
可懂度提升≠生物标志物稳定；增强需临床感知评估，远程监测流水线应检验处理对标志物的副作用。

## 点评
把“增强副作用”做成可点可比的探针，对可信医疗 AI 很及时。强在多策略对照与透明风险公式；弱在风险分为启发式、非验证诊断，且标志物集较小。

