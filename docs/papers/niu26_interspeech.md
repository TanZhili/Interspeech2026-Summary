# Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis

- 论文编号：533
- 报告人：Zhikang Niu
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/niu26_interspeech.pdf

## 问题
连续潜在 TTS 中，高维潜在重建与说话人相似度好但可懂度差，低维相反，形成信息瓶颈式权衡。

## 方法
提出 Semantic-VAE：在 VAE 潜在上与 SSL 表征做语义对齐（如余弦相似度约束），使高维空间保留声学细节同时结构化语义。编码器将 16 kHz 下采样至约 40 Hz 潜在。用于下游零样本/潜在扩散等 TTS，对照不同潜在维度配置。

## 实验与结果
Semantic-VAE 特征在 LibriSpeech-PC test-clean 上达约 2.10% WER 与 0.64 说话人相似度，缓解高维可懂度崩塌。相对未对齐高维潜在，可懂度提升同时保持较好重建/相似度。

## 结论
SSL 语义对齐可打破“高维好听但听不清”的困境，为连续潜在 TTS 提供更稳表征。

## 点评
把瓶颈诊断清楚并用对齐直接干预潜在几何，比单纯调维度更 principled。主数字集中在单一测试集；与离散 codec-LM 路线的系统对比深度取决于正文完整表。
