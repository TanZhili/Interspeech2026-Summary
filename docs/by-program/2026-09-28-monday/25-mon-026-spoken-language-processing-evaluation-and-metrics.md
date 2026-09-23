# Spoken Language Processing: Evaluation and Metrics

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 12）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场专攻口语处理评测：无参考假设质量、非标准语音上的榜单泛化、多书写系统临床 ASR、SpeechLLM 交叉偏见、可弃权可靠性，以及长上下文情绪字幕评估。共同命题是：WER 等传统指标既可能低估（正字变体）、也可能高估（幻觉爆发下的“标准榜”），且无法刻画可靠性与社会偏见。

技术路径包括：用 TTS 条件似然度量语音–文本声学差异；在 FluencyBank/SEP-28k/UIUC 等子集上重评开放榜模型；MultiClin 多参考与脚本统一；语音克隆控制内容后测口音×性别交叉偏见；弃权感知 ASR 与 RAS 指标；把情绪字幕拆成原子感知单元再音频锚定核验。

方向上，评测体系正从单一错误率走向声学接地、可达性、公平性与可靠性的多维协议。

## 技术内容

### 无参考与可达性评测

**Read What You Hear: Reference-Free Hypotheses Evaluation with Acoustic Discrepancy**（论文 3434；Zhihan Li）
READ 用预训练自回归 TTS 计算给定文本假设下语音 token 的条件似然，度量声学差异，无需额外训练即可做假设精炼。实验称与特定识别错误相关，并可将 ASR 输出相对错误率至多降约 20%，噪声条件收益更强。

**WER Are We (Really): How Well Do Top Open ASR Leaderboard Models Generalize to Nonstandard Speech?**（论文 3522；Nihar Mahapatra）
在口吃与构音障碍子集上评估 Whisper、CrisperWhisper、Parakeet、Canary、Granite 等。平均 WER 相对榜单升高 2–5×，极端幻觉可达 24×。整体 Whisper-Large-v3 泛化最稳健，Parakeet 对构音障碍有互补优势，凸显可达性评测缺口。

**When Multiple Script Matters: Evaluating ASR in Clinical Settings**（论文 1126；Minkyu Kim）
提出 MultiClin 以应对非英语临床多书写变体。多脚本感知评测比单参考更公平；训练脚本不一致会升高正字不确定并阻碍收敛，50% 映射比熵最高，脚本统一效果最佳。

### 偏见、可靠性与长字幕

**The Voice Behind the Words: Quantifying Intersectional Bias in SpeechLLMs**（论文 1918；Shree Harsha Bokkahalli Satish）
对三款 SpeechLLM 做 2,880 次受控交互（六种英语口音×两种性别呈现，语音克隆固定内容）。东欧口音尤其女性呈现帮助性评分更低；礼貌度相近但帮助性不同。LLM 评判能抓方向趋势，人类对口音对比更敏感。

**RAS: a Reliability Oriented Metric for Automatic Speech Recognition**（论文 1409；Wenbin Huang）
引入允许对不确定片段弃权的转写框架与 RAS 指标（信息量与避错权衡，参数由人类偏好校准），并以监督自举+强化学习训练。实验称可靠性显著提升且准确率仍具竞争力。

**EmoSURA: Towards Accurate Evaluation of Detailed and Long-Context Emotional Speech Captions**（论文 1046；Xin Jing）
将复杂字幕拆为 Atomic Perceptual Units，并以音频锚定核验；同时发布分层平衡的 SURABench。EmoSURA 与人类判断正相关，而传统指标因对长度敏感呈负相关。

## 本场要点

- 无参考评测可用 TTS 条件似然做声学接地与假设精炼。
- 开放 ASR 榜在非标准语音上 WER 可膨胀数倍，可达性评测紧迫。
- 临床多书写变体要求多参考评测与训练脚本统一。
- SpeechLLM 存在口音×性别交叉偏见，人类比 LLM 评判更敏感。
- 弃权机制与 RAS 把可靠性纳入 ASR 目标。
- 长情绪字幕宜原子核验，忌整体 N-gram/不稳定 LLM 打分。

## 覆盖核对

- 3434 | Read What You Hear: Reference-Free Hypotheses Evaluation with Acoustic Discrepancy
- 3522 | WER Are We (Really): How Well Do Top Open ASR Leaderboard Models Generalize to Nonstandard Speech?
- 1126 | When Multiple Script Matters: Evaluating ASR in Clinical Settings
- 1918 | The Voice Behind the Words: Quantifying Intersectional Bias in SpeechLLMs
- 1409 | RAS: a Reliability Oriented Metric for Automatic Speech Recognition
- 1046 | EmoSURA: Towards Accurate Evaluation of Detailed and Long-Context Emotional Speech Captions
