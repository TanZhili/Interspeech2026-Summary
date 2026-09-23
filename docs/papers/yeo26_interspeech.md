# Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition

- 论文编号：2063
- 报告人：Jinsu Yeo
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yeo26_interspeech.pdf

## 问题
Conformer-Transducer 端侧内存受限；整数量化有 1 bit/参数硬下界。解码器对误差敏感需高精，编码器冗余多，若解码器不能再压，只能把编码器压到亚 1-bit，但标准量化做不到。

## 方法
LittleASR：用 LittleBit 式变秩二值分解 ˜W=diag(h)Ub diag(ℓ) Vb⊤ diag(g)，以秩 r 准连续控制有效 bpw。梯度敏感度 Ω(l) 引导可微预算搜索，编码器压到亚 1-bit、解码器/联合网保留更高秩，再 QAT。目标含点卷积、LSTM 投影与线性层；Conv2d 用 INT4 RTN。NeMo Conformer-Transducer Large（120M），LibriSpeech。

## 实验与结果
混合秩 1.0 bpw：dev-other WER 6.01%（AbsMean tensor 6.30%，尺寸约 18.8 MB）。可到 0.2 bpw（7.1 MB），整数基线无法进入。同尺寸下混合秩优于均匀秩（如 0.4 bpw：8.78 vs 10.82）。分配显示浅层编码器约 0.3–0.4 bpw、深层与 Value 投影更高、联合网约 2.0 bpw。

## 结论
变秩二值分解打破 1-bit 地板，敏感度分配在极端压缩下拓宽 Pareto 前沿，适合超紧内存 ASR。

## 点评
把“编码器可狠压、解码器要护”落到连续秩预算，而非死守离散比特档，问题意识准。强在亚 1-bit 可达与层内（如 Wv vs Wq）细粒度；弱在依赖 QAT、二值 GEMM 真机收益未测，且极端 0.2 bpw WER 仍明显抬升。
