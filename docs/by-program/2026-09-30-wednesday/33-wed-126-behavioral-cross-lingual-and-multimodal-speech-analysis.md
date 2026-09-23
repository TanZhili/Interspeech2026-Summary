# Behavioral, Cross-lingual, and Multimodal Speech Analysis

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster（Area 3 - Poster 2）
- Area：3
- 论文数：11
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。行为与跨语数字仅引自摘要。

## 技术趋势

本场海报把行为状态（压力、情感、填充停顿）、跨语/低资源情感与语用，以及视听/多模态反讽与讽刺检测串在一起。压力检测从实验室 TSST 声学—韵律预测，扩展到医院工作者的语音+轨迹晚融合；情感侧同时追问声学相对文本的贡献（芬兰自发语）、填充停顿的大规模斯拉夫议会建模，以及微笑言语在嘈杂人群噪声下的决策偏置变化。

跨语资源建设密集：MMEE 多语多情感强调检测基准、KuralHub 暴露类型学能力边界、YUE-PUB-Speech 粤语语用多模态、TIMBRE 对 49 层×26 语料做层间跨语 SER 大图。视听与多模态则用眼动揭示普通话反讽的眼/口注意不对称，以及文本锚定正交残差校正分离讽刺中的共鸣与失调。

## 技术内容

### 压力、情感与会话标记

**Automatic Detection of Stress from Speech in the Trier Social Stress Test**（论文 671；presenter：Wieland R. Cremer）  
50 名被试完成 TSST 或非压力对照；经说话人日志与机器学习，压力情境检测显著高于均值基线，部分生理与情感压力反应可由声学—韵律特征预测，并报告特征重要性。

**Looking for Affect in Spontaneous Finnish Speech through Linguistic Interpretability**（论文 2452；presenter：Kalle Lahtinen）  
在新发布的芬兰自发情感语料上系统组合文本与音频特征：效价回归上多模态优于单模态，唤醒度上互补有限，支持其他语言先验并补充芬兰证据。

**Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments**（论文 3262；presenter：Ivan Porupski）  
约 4000 小时克罗地亚/捷克/波兰/塞尔维亚议会语音；Transformer 检测填充停顿，GEE+Mundlak 区分说话人内/间效应。复制年龄与语速与 FP 率负相关，但性别效应语言特异且方向常与既往文献相反；情感与 FP 率正相关，反对派相对执政联盟倾向更低 FP 率。

**Hearing Smiles in the Crowd: How Babble Noise Shapes Smiled Speech Perception**（论文 1178；presenter：Rong Li）  
多说话人嘈杂噪声降低微笑样言语检测与类型（愉悦 vs 展唇）分类敏感度，并系统性改变响应偏置：噪声增大时更不愿报告“听到微笑”，强噪声下安静时偏“愉悦”的倾向可反转。

**Stress Detection Across Daily Activities: A Context-Aware Multimodal Framework with Trajectory and Ambient Speech**（论文 1262；presenter：Wei-Heng Huang）  
医院工作者数据上，语音与移动轨迹特征晚融合相对纯音频基线，F1 提升 9.32%、MCC 提升 0.038。

### 跨语资源、层间 SER 与语用基准

**Do Speech Emphasis Models Generalize across Languages and Emotions?**（论文 2783；presenter：Megan Wei）  
MMEE：7 语、34 情感/风格、10000 句（14.13 h）三级感知标注。单语零样本迁移有限，多语训练显著更稳健；高低唤醒情感间迁移稳健；合成与感知基准双向迁移提示共享韵律结构。

**KuralHub: Exposing Typological Capability Frontiers in Multilingual Speech Emotion Recognition**（论文 3502；presenter：Jubeerathan Thevakumar）  
11 个自监督模型×33 数据集×29 语；跨语可迁移性更受结构类型学而非预训练数据量支配，德拉维达语系系统性失败，单纯放大参数不能消除瓶颈。

**YUE-PUB-Speech: A Speech-based Pragmatic Understanding Benchmark for Cantonese**（论文 289；presenter：Ziwei Gong）  
首个粤语多模态语用数据集：语用丰富文本由训练标注者录音配对，无需细粒度音系/词级对齐；基线显示加入语音相对纯文本提升语用理解。

**TIMBRE: Layer-Wise Cross-Lingual Speech Emotion Recognition Across 49 Layers and 26 Corpora**（论文 579；presenter：Anatoly Marchenko）  
xls-r-1b 的 49 层×26 语料共 31850 次线性探针实验；跨语料迁移在第 15 层（约 31% 深度）达峰（F1=0.392），第 45 层相对塌缩 24.6%。罗曼语呈 U 型相对优势，声调优势随深度增强；均池化 wav2vec2 相对 27 维声学特征 F1 高约 41%，但声学特征复杂度低得多。整体可迁移性更受语料表达性与诱发方式驱动。

### 视听反讽与多模态讽刺

**Eye and Mouth Cues in Audiovisual Perception of Mandarin Irony: Evidence from Eye-tracking and Facial Masking**（论文 1544；presenter：Shifeng Xia）  
44 名母语者在纯视觉、视听安静/噪声条件下听讽责与讽赞及其字面对照。讽责更长注视眼部；讽赞更多注意口部，安静视听下注视眼部时瞳孔更大，显示反讽类型间非对称视觉策略。

**T-ORR: Text-Anchored Orthogonal Residual Rectification for Robust Multimodal Sarcasm Detection**（论文 2222；presenter：Qi Chen）  
动态局部约束对齐使非语言流聚焦所修饰词；结构保持几何分解经 QR 投影拆成语义共鸣与模态失调；对比失调路由建模字面与失调状态距离。MUStARD / MUStARD++ 达 SOTA。

## 本场要点

- 言语可无创侵入地指示压力情境与部分生理/情感反应；日常场景需加空间轨迹上下文。
- 芬兰自发语上文本对效价贡献更大，唤醒度更依赖声学。
- 大规模议会填充停顿显示情感与权力地位调制，性别效应不可跨语一概而论。
- 多语多情感强调与 SER 基准暴露类型学能力边界，层深选择对跨语迁移关键。
- 粤语语用与普通话反讽强调语音/面部多模态对意图理解的必要性。
- 嘈杂噪声改变微笑感知的决策偏置；几何解耦利于捕捉讽刺失调线索。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 671 | Automatic Detection of Stress from Speech in the Trier Social Stress Test |
| 2452 | Looking for Affect in Spontaneous Finnish Speech through Linguistic Interpretability |
| 3262 | Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments |
| 1544 | Eye and Mouth Cues in Audiovisual Perception of Mandarin Irony: Evidence from Eye-tracking and Facial Masking |
| 2783 | Do Speech Emphasis Models Generalize across Languages and Emotions? |
| 3502 | KuralHub: Exposing Typological Capability Frontiers in Multilingual Speech Emotion Recognition |
| 289 | YUE-PUB-Speech: A Speech-based Pragmatic Understanding Benchmark for Cantonese |
| 579 | TIMBRE: Layer-Wise Cross-Lingual Speech Emotion Recognition Across 49 Layers and 26 Corpora |
| 1178 | Hearing Smiles in the Crowd: How Babble Noise Shapes Smiled Speech Perception |
| 1262 | Stress Detection Across Daily Activities: A Context-Aware Multimodal Framework with Trajectory and Ambient Speech |
| 2222 | T-ORR: Text-Anchored Orthogonal Residual Rectification for Robust Multimodal Sarcasm Detection |
