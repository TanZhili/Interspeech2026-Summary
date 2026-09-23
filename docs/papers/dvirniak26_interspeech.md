# Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning

- 论文编号：1289
- 报告人：Dmitrii Korzh
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dvirniak26_interspeech.pdf

## 问题
现有 SDD 跨域/跨生成器泛化弱，且缺少人类可感知的推理式解释。需要把 Large Audio Language Model 的链式推理与真人标注理由结合，既抬检测又给可审理由。

## 方法
提出 HIR-SDD：收集人类问卷理由与评论，过滤低准确标注者，经 Qwen-32B 整理为推理轨迹；得到约 124,410 条标注覆盖 41,414 段音频（37 名标注者）。用 SALMONN-7B 等 LALM 在 hard-label 与 reasoning 训练集上微调，并与 Wav2Vec2-AASIST 对照。

## 实验与结果
Test-1-HL 上 SALMONN-7B（Train-2-HL）准确率 94.5、平衡准确率 88.6、F1 85.7，高于 Wav2Vec2-AASIST（约 92.9 / 84.0 / 76.7）。结合 Train-2-R 与 GRPO 等设定可维持相近或略优平衡指标；文中展示推理样本说明可给出可理解理由。

## 结论
作者认为人类启发推理数据能提升 LALM 检测，并提供对真伪判定的自然语言辩护，有助于可解释反欺骗。

## 点评
把“听感理由”系统化成训练信号，是解释性 SDD 的务实路径。风险在于推理轨迹经 LLM 改写可能偏离原始听感，且硬标签过滤已剔除错误类样本，评估可能偏乐观；跨未见生成器的泛化仍需更强协议。
