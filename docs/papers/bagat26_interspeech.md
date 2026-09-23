# Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition

- 论文编号：2422
- 报告人：Zhe Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bagat26_interspeech.pdf

## 问题
ATC 语音噪声大、L2 口音重、真实标注稀缺，通用 ASR 退化；传统增强难覆盖口音/说话人多样性，L1→L2 口音转换尤缺。

## 方法
合成管线：先分离语音/噪声并 AudioSR 超分，再经 F5-TTS、kNN-VC、TokAN 式 L2→L1，以及重用 TokAN 的可控 L1→L2（微调 token 转换与 token-to-Mel，条件目标口音）；最后 AAS（8 kHz 重采样、200 Hz 高通、注入原句噪声）。L1→L2 幻觉用 Whisper WER>50% 过滤。下游微调 Whisper-small，4 折交叉验证 ATCO2 约 4 h。

## 实验与结果
OOB Whisper 63.32% WER；仅真实微调 22.69%。仅合成中 VC+AAS 最佳约 24.18%。真实+合成时 L1→L2 AC 最优达 21.64%，显著优于仅真实；L2→L1 混训反而变差（25.92%）。AAS 对 TTS 等增益很大；口音多样性比单纯说话人多样性更关键。

## 结论
面向 ATC 的生成式增强（含可控 L1→L2）能在极少真实数据下提升识别，真实+L1→L2 合成优于仅真实微调。

## 点评
问题抓的是 ATC 的“信道+口音”双缺口，把 L1→L2 当多样性源而非归一化预处理。评测严谨（配对手测）；合成过滤丢约 35% 样本，且数据量仍小，扩展到更大 ASR 与细粒度流利度控制是自然下一步。
