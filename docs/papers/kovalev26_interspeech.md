# SEAM: Shortcut-Aware Real-Time Detection of Scripted vs. Spontaneous Speech for Interview Guardrails

- 论文编号：1480
- 报告人：Pranay Manocha
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kovalev26_interspeech.pdf

## 问题
稿读/自发语音分类可用于面试护栏，但标签常与语料身份、信道、录音伪迹纠缠，内部持出高分可能是捷径学习，外域一移即崩。

## 方法
SEAM：统一波形预处理（去直流、70 Hz 高通、−23 LUFS、限幅）；溯源一致的 seam-aware 采样禁止跨录音拼接；约 14 h 非语音噪声库按 40–70% 窗长混入破“干净=稿读”启发式。训练语料：People’s Speech/PodcastFillers（自发）与 LibriSpeech/Spoken Wikipedia（稿读）。DistilHuBERT + 均值池化 + MLP，仅解冻顶层 Transformer，8 s 窗。另设对抗性外部面试评测集（720 片段，风格×信道交叉）。

## 实验与结果
全量训练：内部 test Acc/AUC 0.962/0.977，外部 Acc/AUC 0.952/0.971。消融去掉噪声库与 seam 后内部 AUC 升、外部 AUC 从约 0.90 降至 0.73。8 s 窗优于 2/4/12 s；顶层解冻优于仅头或更深解冻。INT4 量化至 41.8 MB，外部性能几乎不降。多语零样本抽取文本末尾截断。

## 结论
稳健的实时稿读检测依赖捷径感知的数据与评测设计，而非更大骨干；压缩后仍可部署为人工复核的窄护栏信号，非独立裁决器。

## 点评
用“内部升、外部降”的消融直接证明捷径学习，评测设计比刷榜更有价值。外部集专有、英文为主，风格与语体/信道仍部分纠缠，护栏用途需保持人工在环。
