# VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition

- 论文编号：1903
- 报告人：Umberto Cappellazzo
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/arora26b_interspeech.pdf

## 问题
LLM 系 AVSR（如 Llama-AVSR）多在干净声学上优化，LoRA 微调无法让文本预训练 LLM 骨干学会对噪声音频隐状态稳定表征；噪声鲁棒压力几乎全压在编码器上，噪声下性能下降明显。

## 方法
**VIB-AVSR**：在 LLM 中间层对**音频**隐状态插入变分信息瓶颈（视频/文本不压）。位置相关两层 MLP 参数化对角高斯后验，相对可学习先验做 KL；重参数采样后与原表示插值 \(\hat{Z}=\alpha H+(1-\alpha)\tilde{Z}\)（\(\alpha=0.5\)）再传入下层。推理用均值。骨干：Whisper-medium + AV-HuBERT + Llama-3.2-1B（LoRA）。最优配置：层 4 与 8 双瓶颈，\(\beta=0.1/H\)。

## 实验与结果
LRS2；MUSAN babble/speech 噪声。噪声训练与干净训练两种范式下，相对 Llama-AVSR 在多数 SNR 降 WER，极端噪声 Avg(N>S) 收益更大；干净训练时瓶颈仍能泛化到未见噪声。干净语音（∞）基本持平或略优。消融：单层不足，双层 (4,8) 最佳，三层过正则；\(\alpha=0\) 过损，固定 0.5 优于日程调度。

## 结论
对 LLM 骨干音频表示做轻量 VIB 正则，无需改架构或加数据，即可在多 SNR/噪声类型上提升鲁棒性，且与噪声增强机制不同，干净训练也可受益。

## 点评
把噪声鲁棒从「编码器/数据增强」推到「LLM 内部表征压缩」，问题定位清楚。强在开销小、消融完整；脆弱点在仅压音频通道、\(\beta/\alpha\)/层位敏感，以及实验集中在 LRS2 + 特定噪声，跨域外推仍待验证。
