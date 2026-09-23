# Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding

- 论文编号：3058
- 报告人：Hoseong Ahn
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ahn26b_interspeech.pdf

## 问题
Whisper 等长音频编解码 ASR 易产生静音幻觉、跨段重复环与内容漏识；启用上一段转写作上下文时错误会放大，beam search 也难纠正高置信幻觉。

## 方法
提出训练无关的 Whisper-CD：每步用干净音频 logits 与三种声学扰动负样本对比——高斯噪声（SNR 10 dB）、全零 silence、波形左移 \(\Delta_s=7\) s；用 log-sum-exp（\(\tau=1\)）聚合负 logits，\(\ell^{CD}=(1+\alpha\tau)\ell^{pos}-\alpha\tau\log(\frac{1}{K}\sum\exp(\ell^{neg}/\tau))\)。编码器与解码器路径批并行；保持语言识别与时间戳等能力。默认开 previous-context、greedy。

## 实验与结果
五集长音频：Large-v3-Turbo 上 CORAAL 38.75→14.43（最多约 24.3 pp 降幅），Earnings22 33.25→16.16 等全面下降；Large-v3 基线因重复环 WER 可 >100%，CD 后大幅收敛但仍高于 Turbo。吞吐高于 beam=5（如 Turbo CORAAL 147 vs 99 tokens/s）。消融：单扰动不如多负样本；\(\alpha\) 过大伤干净集（TED-LIUM）。

## 结论
多负样本对比解码可在无重训条件下抑制长音频幻觉与重复，相对 greedy 开销有限、显著快于 beam search，可作已部署 Whisper 的即插替换。

## 点评
把对比解码从视觉/文本迁到 ASR，用声学退化暴露模型先验，直接打在上下文传递放大错误的链路。\(\alpha\) 与模型尺度敏感，Large-v3 深重复环仍难完全拉回；decoder-only ASR 如何注入扰动路径仍开放。
