# Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio

- 论文编号：1748
- 报告人：Phillip Long
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/long26_interspeech.pdf

## 问题
自回归语言模型可经算术编码做无损压缩，但既往多限于 8-bit/16 kHz；16/24-bit 全保真下词表爆炸（65K/16.7M），能否实用并与 FLAC 竞争未知。

## 方法
系统基准音乐/语音/生物声学、16–48 kHz、8/16/24-bit。提出 Trilobyte：将每样本拆成字节交错，词表恒为 256（O(1) vs O(2^b)），序列长度增约 ⌈b/8⌉ 倍，使 24-bit LM 压缩首次可训。用 GPT-2 类 AR + 算术编码；亦可用 NLL 估计码率。

## 实验与结果
LM 在 8-bit 与 16-bit 上持续优于 FLAC 并达 SOTA 量级；随 bit depth 升高相对增益变小。Trilobyte 改善 16-bit 并首次使 24-bit 可处理。作者指出 bit depth（相对采样率或领域）是限制可学压缩增益的关键因素。

## 结论
字节级分词让全保真无损 LM 压缩可行；高 bit depth 下相对传统编解码器的优势收窄。

## 点评
把“LM 无损压缩”从玩具 8-bit 推到 CD/专业位深，工程贡献清楚。上下文窗口与算力仍远高于 FLAC；随深度升高收益递减提示与线性预测的信息论重叠。
