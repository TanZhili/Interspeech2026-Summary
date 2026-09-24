# On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models

- 论文编号：999
- 报告人：Shunsuke Kando
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kando26_interspeech.pdf

## 问题
GSLM 的离散单元序列远长于文本，训练成本高；常规 N=20 ms 设定对语音生成是否冗余、降低码率会否伤重合成与续写，尚缺系统扫描。

## 方法
HuBERT-base 第 9 层特征按 N∈{20…280} ms 分段均值池化，再 K∈{128…16384} 做 K-means（64 种码率）。uLM 为 OPT，训于 LibriSpeech 960 h；u2s 分别为 Tacotron2+PWG 与 VITS（LJSpeech）。评重合成（WER、UTMOS、MCD、LogF0 RMSE）与续写（PPL/VERT、GPT-4.1-mini 成对裁判、MMOS、AB）。

## 实验与结果
重合成：中等 N（40/80）在更低码率下接近 N=20；Tacotron2 更可懂，VITS 声学更好。续写：在 WER<5 且 UTMOS>4 的设定中，N=80–120 大 K 的 LLM 裁判常优于基线；人工 AB 显示 (20,256) 与 (80,4096) 等可竞争。LLM 裁判与 MMOS 的 SRCC 仅 0.323，高于 PPL/VERT 但仍偏低。

## 结论
更低码率仍可支撑可懂重合成与高质量续写，常规高码率对生成任务可能冗余；续写自动指标与人工对齐仍弱。

## 点评
把“理解向”的 N/K 扫描延伸到生成任务，并点出任务最优码率不同（音素保真 vs 语义建模）。评价瓶颈在续写指标——LLM-as-judge 相关性仍低，结论对温度选择与归一化方式敏感。
