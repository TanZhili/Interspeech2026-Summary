# Evaluation of Speech and Audio Analysis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 5）
- 论文数：14
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场评测主题从语音质量 MOS 预测扩展到 LALM 审计、歌唱/文本—音频对齐、音频问答与对抗攻击。质量评估正从标量 MOS 转向成对偏好（PrefSQA、AnimeScore）、多维可解释描述（校准—推理框架）以及事件级文本—音频对齐（ELSA），以降低评分噪声并提高与人类相关。

基础模型如何用于 SQA 被系统审视：CAL-MOS 显示最佳层强烈依赖骨干与数据集，朴素跨层加权不稳，层校准 adapter 更鲁棒；另有面向细粒度声学细节（噪声、混响）的预训练编码器，纠正许多 SSL 对背景声学过度不变的偏向。神经音频编解码器的客观指标与 MUSHRA 相关性被专门检验。

更广的能力基准包括 UG-Bench（感知+生成解耦）、AURA/AQEval（开放 AQA）、VoxEffects（效果链监督）与 LALM 成员推断攻击协议（控制分布偏移混淆）。生成侧有 RLHF 偏好对齐音频描述；安全侧则有神经编解码器潜空间的快速对抗波形生成。评测可信度、偏好标签与跨任务统一框架是共同方向。

## 技术内容

### 隐私审计、歌唱与文本—音频评测

**Membership Inference Attacks against Large Audio Language Models**（论文 514；Jia-Kai Dong）
首次系统评估 LALM 成员推断。多模态盲基线显示常见音频数据即使无模型推理也可近乎完美分隔训练/测试，故 MIA 可能主要检测分布偏移；提出盲基线协议与分布匹配数据。结果表明 LALM 记忆呈跨模态，源于说话人声音身份与文本绑定。

**Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation**（论文 912；Sourav Ghosh）
MUSICJUDGE 将歌词正确性与音高—节奏保真在块对齐多模态分析中耦合，并用语义/词汇/语音多信号匹配检测歌词块；以 Modality-Guided LoRA 微调 ASR 改善歌唱转写。跨数据集与人类专家判断一致性强。

**ELSA: Acoustic Event-Level Semantic Alignment for Fine-Grained Reference-Free Text-to-Audio Evaluation**（论文 914；Shuntaro Suzuki）
针对 CLAP 类粗粒度相似度与人类相关弱，ELSA 按文本导出的声学事件分解生成音频并评估事件级对齐。四 TTA 基准上与人类主观评分相关高于先前指标。

### 偏好学习、综合基准与面向质量的表征

**PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets**（论文 1512；Junyi Fan）
研究无 MOS 的偏好预测，PrefSQA 含不确定度感知 logits、损伤注意力头与非匹配参考比较模块。MOS 派生数据增益小，高质量偏好/仿真集上相对基线提升更清晰，强调偏好数据质量。

**UG-Bench: A Comprehensive Benchmark for Evaluating Large Audio-Language Models**（论文 1517；Hui Wang）
在语音感知、音频感知、语音生成与口语理解四能力上系统评估 11 个 LALM 与 5 个专用生成模型，发现指令遵循与生成质量缺口显著。

**A Fine-Grained Acoustically-Aware Pre-training Encoder for Speech Quality Assessment**（论文 1607；Donald S. Williamson）
提出融合局部谱—时建模、帧级谱关系聚合与显式噪声/混响信息的编码器，避免 SSL 对背景声学过度不变；多数据集 SQA 上以更小模型达到与大得多模型可比性能。

**VoxEffects: A Speech-Oriented Audio Effects Dataset and Benchmark**（论文 1621；Zhe Zhang）
提供带精确效果链监督的语音效果数据与识别基准（存在检测、预设分类、活跃效果数、强度），含采集端/平台端退化鲁棒协议，并给 AudioMAE 多任务基线。

### 编解码器指标、可解释 SQA 与风格偏好

**Evaluating Objective Speech Quality Metrics for Neural Audio Codecs**（论文 1809；Luca A. Lanzendöerfer）
对高保真语音做 MUSHRA，分析主观分与常用客观指标相关：部分指标与人类感知一致，另一些难以捕捉相关失真，为神经编解码器语音评测提供选型指引。

**Calibration-Reasoning Framework for Descriptive Speech Quality Assessment**（论文 2362；Milos Cernak）
后训练 Audio LLM：先校准预测预定义感知维度，再用 GRPO 与维度特异奖励强化描述准确性与质量问题时间定位。QualiSpeech 多维平均 PCC 0.71，RL 推理带动 MOS 预测提升 13%。

**CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models**（论文 2960；Alef Iury Ferreira）
在十个 SFM、四 MOS 数据集上比较全微调、末层探测与朴素跨层加权；最佳层强依赖设置，朴素融合不稳。层校准 adapter 再池化可提升多融合鲁棒并缩小与全微调差距。

**AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style**（论文 3025；Joonyong Park）
用成对排序评估“二次元感”：15,000 对偏好显示其由受控共振塑造、韵律连续性与刻意发音驱动而非简单高音高。手工特征 AUC 上限 69.3%，SSL 排序模型可达 90.8% AUC。

### 对抗攻击、AQA 指标与描述对齐

**Exploiting Neural Audio Codec Latents for Adversarial Audio Attacks**（论文 3055；Ajita Rattani）
在神经音频编解码器连续潜空间用条件生成器单次前向合成类特异扰动并解码为对抗波形；定向攻击成功率最高 99%，推理亚 7 ms，相对生成基线延迟降 24×。

**AURA Score: A Metric for Holistic Audio Question Answering Evaluation**（论文 3185；Satvik Dixit）
发布 AQEval（约 10k 模型回答的人类正确性/相关性标注），显示 BLEU/METEOR/BERTScore 等与人类相关弱；提出 AURA，在 AQEval 上与人类评分相关达先进水平。

**Aligning Audio Captions with Human Preferences**（论文 2052；Kartik Hegde）
用人类成对偏好训练 CLAP 奖励模型，经 RLHF 微调任意基线描述系统而无需真值标注；人类评估显示相对基线更受偏好，并可比有监督真值方法。

## 本场要点

- 质量评测正从标量 MOS 转向偏好、事件级对齐与多维可解释描述。
- LALM 审计需先排除数据分布偏移，否则成员推断可能测到伪相关。
- SFM 用于 MOS 时层选择与融合策略高度依赖骨干/数据，需层校准。
- 面向 SQA 的预训练应保留噪声/混响等细粒度声学线索。
- 开放 AQA 需要专度量（AURA）与人类标注基准（AQEval）。
- 评测生态同时扩展到歌唱、音效链、二次元风格、编解码器与对抗鲁棒。

## 覆盖核对

- 514 | Membership Inference Attacks against Large Audio Language Models
- 912 | Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation
- 914 | ELSA: Acoustic Event-Level Semantic Alignment for Fine-Grained Reference-Free Text-to-Audio Evaluation
- 1512 | PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets
- 1517 | UG-Bench: A Comprehensive Benchmark for Evaluating Large Audio-Language Models
- 1607 | A Fine-Grained Acoustically-Aware Pre-training Encoder for Speech Quality Assessment
- 1621 | VoxEffects: A Speech-Oriented Audio Effects Dataset and Benchmark
- 1809 | Evaluating Objective Speech Quality Metrics for Neural Audio Codecs
- 2362 | Calibration-Reasoning Framework for Descriptive Speech Quality Assessment
- 2960 | CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models
- 3025 | AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style
- 3055 | Exploiting Neural Audio Codec Latents for Adversarial Audio Attacks
- 3185 | AURA Score: A Metric for Holistic Audio Question Answering Evaluation
- 2052 | Aligning Audio Captions with Human Preferences
