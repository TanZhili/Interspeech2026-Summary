# Content is What Remains: Invariant Speech Tokenization from Parallel Utterances

- 论文编号：2817
- 报告人：Laurin Wagner
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wagner26b_interspeech.pdf

## 问题
离散语义语音 token 常蒸馏自 HuBERT/WavLM，仍泄漏说话人、韵律与信道，抬高 H(z|c)，损害压缩与下游解耦。

## 方法
PINT：洞察为“同文多说者并行时内容是唯一共享因子”。Stage A 在 HuBERT-base 上用 soft-DTW 对齐并行句、词级对比、音素解码 CE；Stage B 用 EMA 教师生成共享离散目标，学生 CTC 对齐，辅以边际/正交正则（K=200）。并行语料含 ARCTIC/VCTK/ESD 等，非并行靠增强与 Kokoro 合成造伪并行。

## 实验与结果
说话人探针准确率 93.1%→1.2%；ABX 误差约降 42%；离散 WER 12.13 vs HuBERT 21.37。噪声上 token 熵近 0。同规模 LM 困惑度降约 27–30%（约 1.95 vs 2.78/2.67）。压缩：去重后约 12.6 tok/s vs 基线 ~25。消融显示需真实并行；纯合成或仅 AR/CTC 损失更弱。

## 结论
上游把 SSL 表征洗成内容不变 token，可作为编解码器的即插语义目标，比改编解码器架构更正交有效。

## 点评
用并行数据把不变性写进目标函数，比事后对比或投票更干净；情感探针仍约 32% 说明韵律未完全剥离。依赖对齐与（伪）并行语料，低资源语言需合成扩展。
