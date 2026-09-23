# Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition

- 论文编号：683
- 报告人：Benedikt Hilmes
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hilmes26_interspeech.pdf

## 问题
忆阻器可模拟执行 VMM 以降耗，但编程与执行噪声大；相对位置编码（PE）对 ASR 尤其低精度很重要，却发现其线性变换输出幅值易被默认 ADC 裁剪，导致映射到忆阻器后相对无 PE 反而更差。

## 方法
在 SynaptogenML 上仿真 CTC-Conformer（~77M）带相对 PE；LibriSpeech 与 Loquacious 250h；权重 8/4-bit、激活 8-bit；ADC 默认 4 精度+4 量程位。分析 PE 线性层 ADC 裁剪（约 40% 时间），试验：扩大量程/精度、固定 8 bit 预算下移位给量程、仅调 PE 层 ADC、去掉 PE 线性层、学习型 PE、数字域保留 PE（oracle）。

## 实验与结果
数字基线：相对 PE 在 4-bit 权重更稳（dev-other 5.6 vs 无 PE 6.5）。默认忆阻器映射后有 PE 反而更差。将 PE ADC 量程提到 8 或固定预算 1/7（精度/量程）可把相对退化约减半，恢复约 15% 相对优于无 PE。去掉编码相关线性变换时相对退化约降 30%。oracle（PE 留数字）接近最优。

## 结论
PE 层输出动态范围与默认 ADC 不匹配是主要病灶；调 ADC 量程或去掉线性变换可恢复 PE 收益。部署需在硬件可改 ADC 与模型改造间权衡。

## 点评
把硬件量化裁剪与相对 PE 的幅值特性对上号，比笼统报“忆阻器掉点”更有指导性。强在软硬协同建议；弱在纯仿真、且评测子集较小（dev-other/dev）。
