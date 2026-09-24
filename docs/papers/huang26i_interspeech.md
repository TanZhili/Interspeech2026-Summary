# Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization

- 论文编号：1471
- 报告人：Wanting Huang
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26i_interspeech.pdf

## 问题
一致性正则（CR）已提升 CTC，但在 Align-Refine 等非自回归迭代对齐精炼及半监督伪标签场景中如何系统结合仍不足。

## 方法
Align-Consistency：对 Align-Refine（CTC 初对齐 + S=2 步 Transformer 精炼）的 base 与各精炼步，在 SpecAugment 双视图上施加 CR；半监督时用非 AR 解码在线生成伪标签并继续训练。ESPnet Conformer，评 LibriSpeech LS-100/960 与 Libri-Light 无标数据。

## 实验与结果
监督：相对 CR-CTC，test WER LS-100 约 12.2/26.7→10.0/22.9，LS-960 4.3/9.9→3.3/7.4；CR 作用于 CTC 与精炼步可叠加。半监督：从 LS-100 模型用 960h 无标可至约 4.3/9.6，再加 LL-6000 至 3.8/9.1；Align-Consistency 伪标签优于纯 CTC。

## 结论
非 AR 精炼与 CR 互相增益；快速并行解码适合在线伪标签，半监督下 CR 对噪声监督仍稳健。

## 点评
把 CR 从纯 CTC 扩到对齐精炼全链路，并证明伪标签质量受益于非 AR，逻辑闭环。超参（α、λ、S）依赖验证调参；未与强 AR 自训练主流路线同协议全面对比。
