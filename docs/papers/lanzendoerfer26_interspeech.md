# Evaluating Objective Speech Quality Metrics for Neural Audio Codecs

- 论文编号：1809
- 报告人：Luca A. Lanzendöerfer
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/lanzendoerfer26_interspeech.pdf

## 问题

神经音频编解码（NAC）在低码率高保真上进展快，但客观指标能否反映其特有失真、尤其立体声分通道编解码场景，仍不清楚。主观 MUSHRA 昂贵，需要可靠客观代理。

## 方法

用 ODAQ 的 11 条干净语音与 11 条语音+背景样本，经 EnCodec、MBD、Vocos、DAC、SNAC、Mimi 等编解码（分通道处理），做众包 MUSHRA（过滤后语音 13 人、混合 17 人）。计算大量侵入式/非侵入式指标（PESQ、PEAQ、STOI、ViSQOL、DNSMOS、NISQA、SCOREQ、WARP-Q、各类 SDR/SNR 等）与平均 MUSHRA 的 Pearson/Kendall 相关，并公开评分。

## 实验与结果

语音子集：SCOREQ（ρ=0.937）、PESQ（0.886）、STOI（0.885）等与主观最对齐；PEAQ、NORESQA 近零相关。混合语音+背景：PESQ 仍最可靠，若干语音子集上表现好的指标相关性下降（SCOREQ no-ref 等明显变差）。码率—MUSHRA 曲线显示不同编解码主观差距。

## 结论

对 NAC 语音评测，PESQ 与 SCOREQ 总体最可靠；域（纯语音 vs 含背景）会改变指标排序，选择指标需匹配内容类型。作者建议据此指导后续 NAC 语音评测并释放 MUSHRA 数据。

## 点评

务实的“指标选型指南”：用当代 NAC 重测经典客观指标，避免沿用过时假设。样本数有限（各 11 条）、仅分通道立体声、模型清单非穷尽，外推需谨慎；但对开发迭代仍有直接参考价值。
