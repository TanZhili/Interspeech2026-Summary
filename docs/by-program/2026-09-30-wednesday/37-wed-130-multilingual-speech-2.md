# Multilingual Speech 2

- 日期：2026年9月30日（周三）
- 时间：14:00-16:00
- 形式：Poster
- Area：12
- 论文数：13
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场覆盖流式语音翻译等待策略、训练数据过滤与跨语对齐、低资源参数共享、离散单元声码器分析、语码混合强制对齐、翻译增强编码器预训练、鲁棒数据增强、副语言表达保留、大规模多语语料，以及 ITN 与视听上下文评测。

翻译系统侧，固定节拍等待易幻觉，学习式等待更贴近真实麦克风场景；S2ST 数据过滤开始直接在成对语音上用 Audio-LLM 做保留/丢弃；最优传输与梯度驱动参数共享用于缩小高低资源差距。

表征与数据侧，离散单元声码器系统分析簇大小与说话人/语言条件；YODAS v3 提供超百万小时高带宽立体声多语数据。鲁棒性议题包括语音学启发的 ASR 错误增强、跨模态对抗鲁棒迁移，以及笑声/哭声等非言语发声的保留。

评测与后处理方面，出现印地—英语语码混合对齐评估、罗马尼亚 ITN 多路线比较，以及用场景视听标签扩展 CXMI 的翻译上下文利用率度量（摘要末尾截断于相关统计）。

## 技术内容

### 流式策略、数据筛选与跨语对齐

**Learning to Wait: Real Streaming Speech-to-Text Translation with an LLM**（论文 1323；Rogier van Dalen）  
指出 Bestow 类固定节拍等待在真实世界易幻觉或滞后。本文学习何时等待更多音频、何时输出 token。摘要称在测试集上质量与/或时延更好，且对真实数据不易幻觉。

**Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data**（论文 1148；Qixu Chen）  
用 Rank→Distill 两阶段从噪声语音对生成伪标签，训练音频大模型直接对成对语音做 keep/drop。摘要称在 CVSS-C 与 SpeechMatrix 上相对未过滤训练最多提升约 +1.4 ASR-BLEU。

**POTSA: A Cross-Lingual Speech Alignment Framework for Speech-to-Text Translation**（论文 695；Xuanchen Li）  
基于平行语音对与最优传输，配合偏置补偿、Q-Former token 级 OT 约束与层调度。摘要称在 FLEURS 上相对五种常用语言 +1.29 BLEU、零样本语言 +2.93 BLEU，每语仅用约 10 小时平行语音。

**Automated Gradient-Driven Parameter Sharing for Low-Resource Multilingual Speech-to-Text Translation**（论文 1292；Ruiyan Sun）  
用语言间梯度行为自动发现参数共享配置（聚类、共享—私有比例、联合 SVD 与正则 CCA）。摘要称在四个低资源语言对与 SeamlessM4T-Medium 上获得一致提升。

### 离散单元、对齐评测与编码器预训练

**Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations**（论文 3330；Naman Kothari）  
分析 BigVGAN 单元声码器在四种印度语言上簇大小与条件策略的交互。摘要称簇大小主导可懂度/音位区分，显式说话人条件对防止身份坍塌不可或缺；语言监督在小簇时更有帮助。

**Evaluation of forced alignment of code-mixed speech: the case of Hindi-English**（论文 2179；Ayushi Pandey）  
评估 Montreal Forced Aligner 在印地—英语语码混合上的表现。摘要称自举词汇策略显著优于未修改词典；句级语码混合数据训练的声学模型平均误差 4.15 ms，远低于单语印地或孤立英语设定。

**Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?**（论文 3241；Tomoya Mizumoto）  
主张翻译目标比转写更能促使编码器捕获语义。摘要称把翻译目标纳入语音编码器预训练可显著改善跨模态整合与下游 Speech LLM 任务。

### 鲁棒增强、表达保留与大规模数据

**PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation**（论文 1963；Xuan Tung Nguyen）  
系统归类越南语级联 ST 中的 ASR 替换错误，并提出用语音学词嵌入替换生成类 ASR 损坏的 PiDA。摘要称在错误 ASR 输出上相对标准微调最多 +2.04 BLEU，并略提升干净文本表现。

**MoVE: Translating Laughter and Tears via Mixture of Vocalization Experts in Speech-to-Speech Translation**（论文 42；Szu-Chi Chen）  
提出可扩展表达数据合成、Mixture-of-LoRA-Experts（MoVE）与软路由，以及约 30 分钟精选数据即可获得强表现的数据效率。摘要称英中 S2ST 上目标非言语发声复现率 76%，而既有系统最多约 14%。

**Cross-Modal Robustness Transfer (CMRT): Training Robust Speech Translation Models Using Adversarial Text**（论文 2278；Gerasimos Spanakis）  
将面向屈折形态的文本对抗攻击适配到语音，并提出无需对抗语音数据即可把文本鲁棒性迁移到语音的 CMRT。摘要称四个语言方向上平均对抗鲁棒性提升超过 3 BLEU，同时保持干净数据性能。

**YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech**（论文 386；William Chen）  
发布逾 110 万小时、48 kHz 多通道、147 语言、CC BY 3.0 的弱标注语料。摘要称 22 种语言超 10K 小时、73 种超 5K 小时，并训练基线 ASR 与神经编解码器以验证有效性。

### 后处理、ITN 与视听上下文评测

**Inverse Text Normalization in Romanian: A Comparative Study of Rule-Based, Neural, and Large Language Model Approaches**（论文 3454；Oana Sirbu）  
在统一区分复制/归一化错误的框架下比较规则、神经、微调多语 Transformer 与 LLM。摘要称规则高精度但覆盖有限，神经模型有预训练收益但数值不稳，少样本 LLM 接近人类且跨域更强但算力成本更高。

**Audiovisual CXMI: Scene-based Context Tagging for Spoken Language Translation Evaluation**（论文 2175；Dayeon Ku）  
将 CXMI 扩展为带场景视听标签的 AV-CXMI，经场景分割与六类上下文标签后条件评估翻译。摘要称在韩英电影翻译上与人类判断相关性更高（Pearson r=0.400；摘要此处截断）。

## 本场要点

- 流式 ST 需要学习式等待，固定节拍在真实静音/语速变化下易失效。
- 数据质量控制从文本侧扩展到成对语音上的 Audio-LLM 过滤。
- 跨语对齐（OT）与梯度驱动参数共享用于低资源多语 ST。
- 离散单元声码器分析强调簇大小与说话人条件的分工；YODAS v3 提供超大规模高保真多语数据。
- 鲁棒议题覆盖语音学错误增强、跨模态对抗迁移与非言语发声保留。

## 覆盖核对

- 1323 | Learning to Wait: Real Streaming Speech-to-Text Translation with an LLM
- 1148 | Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data
- 695 | POTSA: A Cross-Lingual Speech Alignment Framework for Speech-to-Text Translation
- 1292 | Automated Gradient-Driven Parameter Sharing for Low-Resource Multilingual Speech-to-Text Translation
- 3330 | Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations
- 2179 | Evaluation of forced alignment of code-mixed speech: the case of Hindi-English
- 3241 | Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?
- 1963 | PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation
- 42 | MoVE: Translating Laughter and Tears via Mixture of Vocalization Experts in Speech-to-Speech Translation
- 2278 | Cross-Modal Robustness Transfer (CMRT): Training Robust Speech Translation Models Using Adversarial Text
- 386 | YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech
- 3454 | Inverse Text Normalization in Romanian: A Comparative Study of Rule-Based, Neural, and Large Language Model Approaches
- 2175 | Audiovisual CXMI: Scene-based Context Tagging for Spoken Language Translation Evaluation
