# Paralinguistics

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 3）
- 论文数：8
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

副语言学本场从情绪识别训练策略延伸到 LALM 评测、生理周期、统一副语言理解、韵律可视化、二语口音可理解度，再到关系性情感范式与弱监督情绪日志。CHUCKLE 用众包标注一致性定义样本难度做课程学习，把“对人难”当作对网络也难的先验。

评测与模型能力方面，ParaPairAudioBench 在五维副语言成对比较上显示 LALM-as-a-Judge 仍落后人类且在平局弃权上校准失败；ParA-LLM 以 22 维特征与大规模 Audio-QA、两阶段课程补齐说话人/环境理解，并放出高难度基准。生成侧 NovaDiffusion 把情绪相关韵律注入扩散图像合成；应用侧尝试从朗读语音预测月经周期相位，以及用 Speech LLM 近似人类口音度/可理解度评分。

理论与时序建模上，有工作主张以互动场中的情感共振/活力轮廓替代孤立说话人离散情绪标签；P-SED 用原型度量学习与弱监督做语音情绪日志。瓶颈是主观难度定义、细粒度副语言评测校准、生理信号微弱，以及从话语级标签学帧级情绪边界。

## 技术内容

### 课程学习、LALM 评测与统一副语言理解

**CHUCKLE - When Humans Teach AI to Learn Emotions the Easy Way**（论文 1591；Ankush Pratap Singh）
提出以众包标注者一致性与对齐定义样本难度的感知驱动课程学习 CHUCKLE。实验表明相对无课程基线可提升 LSTM 与 Transformer 情绪识别，并减少梯度更新次数，在被试依赖/独立设定下改善效率与鲁棒。

**ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge**（论文 2021；Jisu Jeon）
构建 5,175 对、五维（Style、Rate、Emphasis、Age、Gender）成对基准，含同转写与跨转写条件。显示当前 LALM 裁判平均落后人类 32%p，并在应判平局时出现严重校准失败，支持多维、校准感知的副语言评测。

**ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding**（论文 3015；Nishit Anand）
设计 22 维副语言特征与逾 1.2M Audio-QA，两阶段课程先单属性再多属性联合推理。发布 ParA-Bench（6,000 道选择题）；前沿模型如 GPT-4o-Audio 仅约 36% 准确率，ParA-LLM 在该基准上超先进 Audio LLM 7.5%，并在 MMAU-Pro/MMAR Speech 有额外增益。

### 韵律可视化、生理与二语评分

**"Say That Again": Visualizing Paralinguistic Cues with Prosody-Aware Diffusion**（论文 2102；Shyamji Tiwari）
NovaDiffusion 在扩散合成中条件于情绪相关韵律：含 Prosody-CLIP、蒸馏 U-Net 与 IP-Adapter 式解耦交叉注意力。在 RAVDESS 上 ECA 71.3%，优于 SonicDiffusion；留出 IEMOCAP 说话人 63.4% vs 41.7%。摘要界定范围限于情绪相关韵律，且 ECA 依赖面部表情分类。

**Predicting Menstrual Cycle Phases from Speech: A Paralinguistic Approach**（论文 1878；Anika A. Spiesberger）
在 76 名德语朗读者排卵/黄体两相位数据上，手工特征达 62.5% 准确率，学习嵌入仅机会水平；响度、共振峰振幅、H1-H2、谱通量效应小且不显著，说话人级准确率与激素水平或年龄无相关。建议未来用更多周期相位与个性化。

**Can Speech LLMs Approximate Human Ratings of Accentedness and Comprehensibility? Evidence from Correlational and Feature-Based Analyses**（论文 1991；Wenwei Dong）
比较 Speech LLM 分数与人类口音度/可理解度评分：中等相关，能捕捉前—后测进步，Lasso 分析显示与人类重叠的音段/超音段线索；仍建议微调并融入语言学知识。

### 关系性情感与弱监督情绪日志

**Shifting Relational Paradigms for Affective Computing: Affective Resonance, Vitality Affects, and Vocal Interaction Fields**（论文 2829；Cy Gorman）
主张情感计算应从个体状态范式转向互动场中的关系单元，并以连续自监督语音表示检测多方会话中的方向性表达耦合；耦合呈体制特异、亚秒尺度，并在独占说话负对照下崩溃。提出 Artificial Affective Resonance Intelligence 设计框架。

**P-SED : Asymmetric Prototype Metric Learning for Weakly Supervised Speech Emotion Diarization**（论文 2388；Nurmemet Yolwas）
P-SED 用可学习情绪原型构造度量空间并正交正则化增强类间可分；Class-aware Prototype Contrastive Loss + Top-K 挖掘显著情绪片段，推理用 TVD 保持陡边界。在 ZED 上 EDER 47.00%，显著优于既有弱监督模型。

## 本场要点

- 感知驱动课程学习把众包一致性当作情绪样本难度信号。
- LALM 作副语言裁判仍明显弱于人类，平局校准是突出失败模式。
- 统一副语言 Audio-QA 课程与专用基准暴露前沿模型的大缺口。
- 韵律条件扩散可将说话情绪相关线索可视化，但评测口径仍偏面部表情。
- Speech LLM 可部分近似人类口音/可理解度评分，但未完全替代。
- 关系性情感共振与弱监督情绪日志推动从话语标签走向互动/时序建模。

## 覆盖核对

- 1591 | CHUCKLE - When Humans Teach AI to Learn Emotions the Easy Way
- 2021 | ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge
- 1878 | Predicting Menstrual Cycle Phases from Speech: A Paralinguistic Approach
- 3015 | ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding
- 2102 | "Say That Again": Visualizing Paralinguistic Cues with Prosody-Aware Diffusion
- 1991 | Can Speech LLMs Approximate Human Ratings of Accentedness and Comprehensibility? Evidence from Correlational and Feature-Based Analyses
- 2829 | Shifting Relational Paradigms for Affective Computing: Affective Resonance, Vitality Affects, and Vocal Interaction Fields
- 2388 | P-SED : Asymmetric Prototype Metric Learning for Weakly Supervised Speech Emotion Diarization
