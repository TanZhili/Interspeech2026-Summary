# Speech Emotion Recognition and Representation 1

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 3）
- 论文数：5
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场从可泛化 SER 综述切入，再到弱监督训练动态、轻量谱图架构、二阶几何聚合，以及音义冲突下的解耦。主线是：固定类别判别已成熟，但真实情绪理解要求跨语言/域/标签体系泛化，并处理声学与文本语义矛盾。

综述强调 foundation models 与 Speech LLMs 可能把 SER 推向开放式、零样本推理。实证研究则分别打在：早期硬标签强迫提交导致的不确定；SSL 过大难以上边缘而 mel CNN 表示不足；一阶池化丢掉特征相关；以及语义先验压倒矛盾声调（Semantic Dominance）。

方法上呈现“软化监督—蒸馏一致性—几何相关—对比解耦”光谱：PWS 逐步收紧 top-k 软监督；MSMC 用掩码卷积与 mean teacher 逼近 SSL；SOC 把协方差描述子映到切空间；ACR-Net 用跨模态注意力与对比解耦对抗 ASPIRE 冲突基准。

## 技术内容

### 可泛化范式与训练动态

**Generalizable Speech Emotion Recognition: Strategies and Trends**（论文 （无编号）；Chi-Chun Lee）
Survey Talk 回顾 SER 从固定情绪类别判别走向跨语言、跨域、跨标签体系与多样数据的可泛化学习，并讨论 foundation models / Speech LLMs 如何推动超越固定标签空间的情绪推理，以及向灵活、多语、潜在零样本开放式理解过渡。

**Progressive Weak Supervision for Speech Emotion Recognition**（论文 1587；Bao Thang Ta）
针对标签歧义与早期训练高不确定，提出 Progressive Weak Supervision：早期若真标签落在 top-k 即视为正确并赋软分布，k 线性衰减至 1。WavLM-Base 在 IEMOCAP（英语四类）与 ViSEC（越南语四类）上，k=3 时分别达 78.08% 与 85.70% 未加权准确率。

### 轻量表示、二阶聚合与音义冲突

**MSMC: Multi-Scale Masked Convolution network for Robust Speech Emotion Recognition**（论文 951；Haoyu Song）
为在谱图上逼近 SSL 表示质量，提出 MSMC：掩码卷积编码器提取稀疏谱特征，mean teacher 强制多尺度一致性以蒸馏全局语义与微韵律。IEMOCAP 上轻量模型中 WA 76.0%，与重 SSL 基线相当且参数与计算更低。

**Geometric Second-Order Feature Correlation Learning for Self-Supervised Speech Emotion Recognition**（论文 1210；Shuanglin Li）
指出一阶聚合默认特征独立、丢弃高阶关系。SOC 层以协方差描述子建模相关，经 Log-Euclidean 映射到欧氏切空间再线性判别。在 ESD 与 RAVDESS 上称恢复一阶池化丢失的判别信息。

**ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling**（论文 2134；Mengke Zhang）
当声调与文本语义矛盾时，模型易被语义先验支配。引入含四类冲突的 ASPIRE 基准及 SOP、LDD 指标；ACR-Net 用跨模态注意力与对比解耦损失将矛盾表示拆到正交潜空间。实验称极性冲突下既有模型语义过度自信严重，ACR-Net 保持高 LDD、SOP 近零并提升 Acoustic Accuracy。

## 本场要点

- 可泛化 SER 正从固定类别转向跨域迁移与 Speech LLM 开放式理解。
- 渐进弱监督可缓解早期硬标签强迫提交。
- 掩码卷积+多尺度一致性使轻量谱图模型逼近 SSL 精度。
- 二阶相关聚合补回 SSL 特征的协同共现信息。
- 音义冲突需显式解耦；新基准暴露语义主导失败模式。

## 覆盖核对

- （无编号） | Generalizable Speech Emotion Recognition: Strategies and Trends
- 1587 | Progressive Weak Supervision for Speech Emotion Recognition
- 951 | MSMC: Multi-Scale Masked Convolution network for Robust Speech Emotion Recognition
- 1210 | Geometric Second-Order Feature Correlation Learning for Self-Supervised Speech Emotion Recognition
- 2134 | ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling
