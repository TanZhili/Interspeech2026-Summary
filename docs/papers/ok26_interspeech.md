# Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning

- 论文编号：2458
- 报告人：Seaone Ok
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/ok26_interspeech.pdf

## 问题
ASR 虽面向说话人无关转写，但 SSL 编码器仍编码说话人痕迹，带来成员推断风险；直接遗忘易伤转写，且既往语音遗忘少见“抹身份却仍能正常转写该说话人”的设定。

## 方法
在 VCTK 上微调 HuBERT-base+CTC 得 Original；Gold 仅用 retain。冻结编码器先训第 6 层辅助说话人头；用 K-Means 估 forget 说话人质心，再解冻编码器，以 CTC(Dr)+λ SAID 做遗忘：softplus 推开 forget 嵌入与质心的余弦相似度（Speech-Aware Identity Dispersion）。对比 Gradient Ascent、Random Label、Bad-T、SCRUB、DUCK 等。评 WER（Dr/Df/Dt）与表征级 logistic MIA。

## 实验与结果
层分析：第 6 层上 Gold 对 Df 的 MIA≈0.52（近随机），Original≈0.75，选为干预点。SAID：Dr WER 7.60、Df 9.55、Dt 7.30；Df MIA 52.6（对齐 Gold 52.7），Dr MIA 74.8。相对 Gradient Ascent（Df WER 飙至 21.77）等，更能同时贴近 Gold 的隐私与效用。

## 结论
针对中间层身份簇的表征级发散可实现说话人级遗忘，同时保持对遗忘/未见说话人的转写能力；框架可扩展到其他敏感属性。

## 点评
把目标从“让模型听不懂某人”纠正为“像从未见过该身份但仍能听写”，更贴合 ASR 产品约束。质心发散比破坏性梯度上升更可控。评测依赖线性 MIA 与 VCTK 朗读设定，对更强黑盒攻击与自发语音的稳健性仍待验证。
