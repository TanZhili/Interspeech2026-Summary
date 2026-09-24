# Modeling Overlapped Speech with Shuffles

- 论文编号：2462
- 报告人：Matthew Wiesner
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/wiesner26_interspeech.pdf

## 问题
重叠语音的说话人归属转写中，跨说话人 token 交错顺序未知；PIT 扩展差、SOT/tSOT 对时间对齐假设强，缺少在单通道重叠上做一次通过对齐的统一框架。

## 方法
用 shuffle 积 FSA 表示保留各说话人内部顺序的所有合法交错；在 CTC 前向中对 shuffle 图边缘化（shuffle loss）。用近似 token 起始时间（utterance 起止线性插值）加 collar κ 做偏序剪枝，κ→0 退化为 tSOT，κ→∞ 为全 shuffle，SOT 为说话人级全序特例。说话人归属：输出 (token, speaker) 元组，可用因式分解（类 SD-CTC）或直接联合 softmax。解码：1-pass 贪心元组 CTC，或 N-pass 目标说话人掩码后接标准 TLG。采用 compact selfless CTC 拓扑以控图规模。实现基于 k2/Icefall。

## 实验与结果
在合成 LibriSpeech 重叠上评估训练、解码与对齐（摘要声明）。正文实验表与具体 WER/cpWER 数字在抽取全文中于方法段截断，未能完整读到。

## 结论
Shuffle + 偏序约束为重叠多说话人 ASR 提供可统一看待 SOT/tSOT/SD-CTC 的形式化；Viterbi 路径可做单遍对齐，并支持说话人标记元组建模。框架原则上可扩展到 transducer/HMM 及其他交错过程。

## 点评
把并发交错写成可组合 FSA，理论清晰，且指出 tSOT/SOT/SD-CTC 是偏序特例，贡献偏框架性。图规模对说话人数敏感，偏序 collar 是关键工程旋钮。因抽取截断未见实验表，定量结论仅能依据摘要“在合成 LibriSpeech 重叠上评估”，具体数字从略并在此说明。
