# Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition

- 论文编号：3408
- 报告人：Kavya Manohar
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/juvekar26_interspeech.pdf

## 问题
Whisper 等对印地语族微调常在朗读/录音棚语料上变好，却在自发口语上显著退化（studio-bias）；常见保守学习率与 easy-to-hard 课程未必适合低资源音系适应。

## 方法
构建 Vividh-ASR：按声学复杂度分 Tier A（studio）、B（broadcast）、C（spontaneous）、D（合成噪声，仅评测），覆盖 Hindi 与 Malayalam，聚合 Kathbath、Shrutilipi、IndicVoices、FLEURS 等。用 2×2 因子实验解耦学习率时机（递减 vs 递增）与课程方向（easy→hard vs hard→easy）。据此提出 R-MFT：Stage1 自发语高 LR（2e−4）→ Stage2 广播（1e−4）→ Stage3 A+C 混合巩固（1e−5）。并用 CKA、SVD、EMD 等分析 encoder/decoder 表征变化。

## 实验与结果
早期高 LR 是主因：Malayalam 上递减相对递增约有 12–13 点全局 WER 优势；hard-to-easy（R-MFT）再额外改善 Malayalam（39.35% vs Standard MFT 42.25%），Hindi 两课程均收敛约 18.8%。R-MFT Medium 全局 WER：Mal 39.36%、Hi 18.82%；244M Small 达 44.41%/21.41%，优于保守低 LR 的 769M。表征上成功配方主要改动 decoder，encoder CKA≈1；IndicWhisper 则扰动 encoder（CKA 0.775）并扩大有效秩。

## 结论
适应效率由更新时机与复杂度排序共同决定；R-MFT 使小模型在自发 Indic ASR 上可比甚至超过常规大模型微调。后续拟扩展语言与选择性冻结 encoder。

## 点评
把“数据不够”转为“优化轨迹不对”，用分层基准钉住 studio-bias，对法庭听写等真实场景有针对性。强在因子设计与表征证据一致；弱在语言仅两种、Tier D 为合成噪声，且与 IndicWhisper 训练分布不完全可比，因果解释需谨慎。
