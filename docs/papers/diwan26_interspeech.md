# ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining

- 论文编号：1437
- 报告人：Anuj Diwan
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/diwan26_interspeech.pdf

## 问题
现有 speech–caption 对齐（如 ParaCLAP）只覆盖窄情态标签；音高、音色、清晰度等 intrinsic 与更广 situational 风格以自然语言描述时，缺少统一嵌入与可用评测/奖励手段。

## 方法
基于 ParaSpeechCaps 训练 CLAP 式双编码器：WavLM-Large 均值池化语音端 + Granite Embedding 278M 文本端，投到 768-D。分别训 Intrinsic、Situational 与两者合并的 Combined；Intrinsic 额外用文本编码器生成的类别嵌入做多标签分类损失，并类均衡采样。下游：风格 caption 检索、属性分类，以及风格提示 TTS 的 best-of-N（N=10）推理时奖励选样。

## 实验与结果
相对 ParaCLAP / ParaCLAP-PSC / VoxProfile 等，多数指标更优。专用模型在对应子集更强（如 Situational R@1 24.79，Intrinsic R@1 18.62）；Combined 在组合评估最好（R@1 14.31）。TTS 引导：CMOS 3.61→3.70，Intrinsic/Situational tag recall 57.9%/69.2%→62.4%/74.3%，NMOS/WER 不降。消融显示新编码器、多任务分类与类均衡均必要。

## 结论
ParaSpeechCLAP 首次较广覆盖 intrinsic+situational 风格对齐，专用与统一策略互补；可用作免训练的 TTS 风格筛选奖励。局限是推理需选对变体，Combined 与专用仍有差距，best-of-N 成本随 N 线性增长。

## 点评
把“宽风格标签空间”落到可发布的双编码器，并把模型当 TTS 奖励用，应用面比纯检索宽。评测仍主要在 ParaSpeechCaps holdout，对外部情感基准覆盖有限；分类提示模板敏感度未深入分析。
