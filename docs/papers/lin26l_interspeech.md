# Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment

- 论文编号：2408
- 报告人：Zhiyu Lin
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26l_interspeech.pdf

## 问题
语音到语音（S2S）模型可懂但常缺表现力；主观评分贵，低层声学特征又抓不住感知细微差别。需要把人类对 expressiveness 的偏好对齐成可扩展客观指标，并用于数据筛选与模型改进。

## 方法
DeEAR 四阶段：将表现力拆为 Emotion（wav2vec2 细调 arousal，CNSCED+IEMOCAP）、Prosody（Gemini-2.5-Pro CoT 评分，SRCC=0.73）、Spontaneity（DNSMOS 启发的伪标签 + 对“过干净但朗读感”惩罚，再蒸馏到 wav2vec2）；用约 480 条人工标注、XGBoost 非线性融合三子分；再蒸馏为单一 DeEAR-Base（wav2vec2-xlsr-53 多任务）。应用：按 DeEAR 从开源情感对话语料筛出约 14K 句 ExpressiveSpeech（约 51h），微调 S2S 基座。

## 实验与结果
与专家 MOS：总体 expressiveness PCC/SRCC 0.91/0.85；DNSMOS/UTMOS 反而与表现力负相关。七个 SOTA S2S 基准：DeEAR 与人类排序 SRCC=0.93，Doubao 最高、Qwen2.5-Omni/Gemini 靠后。S2S-FT vs Base：盲听偏好 78.5% vs 10.0%；客观 S_expr 从 2.0 升到 23.4，情绪与自发维度增益最大。

## 结论
少量标注即可得到与人类偏好对齐的多维表现力指标；用其做评估驱动数据策展，能显著提升 S2S 感知表现力。未来拟接入强化学习做端到端优化。

## 点评
把“表现力”拆成可学子任务再非线性融合，比直接回归抽象 MOS 更贴感知瓶颈（一文指出单维短板会卡死总分）。Prosody 依赖 Gemini、Spontaneity 依赖启发式伪标签，可扩展但外部模型与阈值选择会进指标本身；ExpressiveSpeech 顶 15% 阈值经人工审计，说明指标仍需人校准。DNSMOS/UTMOS 与表现力负相关，提醒“干净度指标”不能当表现力代理。
