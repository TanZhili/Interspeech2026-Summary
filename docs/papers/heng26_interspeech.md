# Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech

- 论文编号：642
- 报告人：Yue Heng Yeo
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/heng26_interspeech.pdf

## 问题
码切换 ASR 缺高质量 CS 语料；用 TTS 增广时多优化重建保真度，未显式约束语言边界一致性，合成数据对下游未必有用。

## 方法
提出声学级 CMI_speech：用带 Language Alignment Loss 的 Whisper 解码器交叉注意力得到帧级伪语言标签，再按非主导语言帧占比定义混合度；与真值语音的 |ΔCMI| 衡量结构保真。对 CosyVoice2 先做 SEAME CS 微调，再以 DPO 对齐：同文本随机采样多样本，用归一化 UTMOS、MER、ΔCMI 打分构造偏好对（最优 vs 最差，并过滤 MER>20%、UTMOS<2.5、ΔCMI>20%）。合成语音与真实数据按等时长混合微调下游 ASR。

## 实验与结果
SEAME 约 192h。TTS 上加 ΔCMI 使 ΔCMI 28.1→16.1、MER 16.2→10.3，UTMOS 维持约 3.8。Whisper-large v3：Real 100h MER 12.1/17.8；+CosyVoice 10.1/16.0；+DPO(UTMOS,MER) 9.6/15.1；+ΔCMI 8.9/14.2（DevMAN/DevSGE）。CTC Conformer 同步改善至 15.4/21.9。定性显示 ΔCMI 更能稳住跨语边界与英文段发音。

## 结论
用声学码混指标引导 DPO，可让合成 CS 语音更贴近真实混合结构，从而更有效地提升下游码切换 ASR。

## 点评
关键是把“文本 CMI”落到帧级声学，直接进偏好学习，补上仅 MER/MOS 管不了的边界问题。依赖伪标签 LID 质量与过滤阈值；合成与真实等时长设定保证公平，但未展开更大规模合成比。
