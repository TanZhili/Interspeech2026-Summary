# Controlled Generation of Synthetic Speaker Vectors for Voice Anonymization

- 论文编号：1464
- 报告人：Ekaterina Kolos
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/kolos26_interspeech.pdf

## 问题
基于重合成的匿名化常用人工说话人向量，但无条件 GAN/扩散难以透明控制性别等属性；反复采样筛选随属性增多代价高，潜空间方向编辑也更偏“改属性”而非按策略保留。

## 方法
在 VPC 2024 基线 B3（STTTS：内容+韵律+说话人向量）上扩展伪说话人生成：（1）复现/条件化 WGAN-QC（cWGAN-QC，标签注入生成器与 critic，按类做二次代价 OT）；（2）无条件扩散（残差 MLP + DDIM）及 classifier guidance 条件采样。向量为 128 维 GST；训练嵌入来自 LibriTTS + ESD(en) + RAVDESS。另提出池级指标（W2、diversity、copying similarity）与哈佛句 TTS wAcc，用于筛选可进管线的生成配置。评测用 VPC 的 EER/WER/UAR，并用 ECAPA 性别分类器检验属性控制。

## 实验与结果
无条件扩散与条件方法的隐私/效用与 B3 相当（如扩散 EER 约 26–28%、WER 约 4.2%、UAR 约 36）。条件控制上，cWGAN-QC 合成音频性别准确率 f/m 达 99.86%/100%；Diffusion+CG 为 99.59%/90.68%。无条件扩散对女声有偏（女 67.3%、男 38.7%）。池评估显示扩散更不易 memorization、WGAN 更接近自然分布且 wAcc 更好；选中的 guidance scale 女 0.72、男 0.22。

## 结论
WGAN 与扩散均可生成高可用合成说话人向量；classifier guidance 更易通过独立分类器扩展到新属性，而 cWGAN 在本文性别控制上更稳。未来拟做多标签/多类属性控制。

## 点评
贡献不在换整条匿名管线，而在给伪说话人采样加上可审计的属性条件与中间诊断指标，便于按政策“保留/改写/标准化”人口属性。cWGAN 控制最强，扩散更灵活但需仔细调 guidance；池级 originality–naturalness 权衡说明仅看下游 EER 可能选到记忆训练身份的生成器。
