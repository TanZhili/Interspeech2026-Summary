# Speech and Language Technologies for Health Applications 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 13 - Oral 4）
- Area：13
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。健康应用数字仅出自摘要。

## 技术趋势

本场聚焦认知障碍与精神健康相关的言语技术：零样本跨语阿尔茨海默检测、认知状态条件 TTS 增强、临床知情加权言语图、病因感知构音障碍 ASR、半监督老年 ASR，以及弱监督抑郁检测。

跨语与数据稀缺是主轴：ORBIT 用多模态双几何对抗学习语言不变表示；CoSTA 用 CS 条件 TTS 与 ASR 转写池扩增 AD 检测数据。可解释性方面，WSG 把临床动机属性写入言语图，少数特征即可接近全基线表现。构音障碍识别强调把病因推理嵌入自回归生成流，而非仅作辅助分类。老年与抑郁场景则分别用置信引导增量伪标签与标签校正双流多示例学习应对弱/半监督噪声标签。

## 技术内容

### 阿尔茨海默检测：跨语、增强与言语图

**Synergizing Zero-Shot Cross-Lingual Alzheimer Detection with Language-Invariant Multimodal Bi-Geometric Adversarial Learning**（论文 2756；presenter：Muskaan Singh）  
假设融合多语语音与文本预训练并经对抗抑制语言特异混淆，可支撑未见语可靠迁移。提出 ORBIT：交叉注意融合、多抽头语言对抗者，以及球形—双曲几何学习与共识聚类。零样本跨语评估中多模态融合持续优于单模态；相对单模态与简单拼接融合，ORBIT 表现最强。

**CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer’s Disease Detection**（论文 88；presenter：Yin-Long Liu）  
适配 CosyVoice2 与 F5-TTS 为认知状态条件 TTS 以合成 AD/健康对照特征言语；转写池含人工转写与 36 路 ASR 转写，并分析增强倍数与测试时增强。ADReSS 上 CS 条件 TTS 提升合成效用，ASR 驱动增强常优于人工转写；CoSTA 相对基线提升 4.16%，测试集仅音频准确率 85.83%。

**WSG: Clinically-Informed Weighted Speech Graphs for Dementia Detection**（论文 2266；presenter：Yao Xiao）  
加权言语图把词义、发音等临床动机属性融入图结构，并提出新图衍生特征集。摘要称仅一两个特征即可达到接近完整基线特征集的表现，且解释与临床观察对齐；并开源图构建、特征提取与可视化 Python 框架。

### 构音障碍、老年 ASR 与弱监督抑郁

**Etiology-Aware Speech Language Models for Dysarthric Speech Recognition**（论文 1773；presenter：Moreno La Quatra）  
比较标准微调、辅助病因分类、输入提示病因，以及在同一自回归流中先预测病因再转写。后者最有效：Speech Accessibility Project 上 WER 7.77%，相对标准微调相对降 6.4%，且推理无需临床标签。辅助分类病因准确更高却不降 WER，说明临床推理需嵌入生成流。TORGO 跨集评价一致获益。

**Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition**（论文 1611；presenter：Chengxi Deng）  
置信估计模块对未转写数据可靠性排序，按高→低置信课程式纳入；可学习提示做说话人自适应训练。DementiaBank Pitt 与粤语 JCCOCC MoCA 上，相对无置信引导增量/说话人自适应伪标签的半监督基线，WER/CER 绝对降 1.45%/2.27%（相对 6.21%/6.98%）。

**Label Correction Enhanced Dual-Stream Multiple Instance Learning for Weakly-Supervised Depression Detection in Speech**（论文 1716；presenter：Xinzhou Xu）  
LC-DMIL 用融合似然比与原型策略校正不准确标签，并以双流多示例学习处理不精确标签。弱监督抑郁语音实验显示方法有效（摘要未列具体准确率数字）。

## 本场要点

- 零样本跨语 AD 检测依赖多模态语言不变表示与几何/对抗约束。
- 认知状态条件 TTS + ASR 转写增强可显著提升 AD 检测数据效用。
- 临床知情加权言语图兼顾可解释性与特征效率。
- 病因需在生成流内先推理再转写，辅助分类不足以降 WER。
- 老年半监督 ASR 受益于置信课程与说话人提示自适应。
- 弱监督抑郁检测需同时校正不准确与不精确标签。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 2756 | Synergizing Zero-Shot Cross-Lingual Alzheimer Detection with Language-Invariant Multimodal Bi-Geometric Adversarial Learning |
| 88 | CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer’s Disease Detection |
| 2266 | WSG: Clinically-Informed Weighted Speech Graphs for Dementia Detection |
| 1773 | Etiology-Aware Speech Language Models for Dysarthric Speech Recognition |
| 1611 | Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition |
| 1716 | Label Correction Enhanced Dual-Stream Multiple Instance Learning for Weakly-Supervised Depression Detection in Speech |
