# Contrastive Regularization for Accent-Robust ASR

- 论文编号：949
- 报告人：Van-Phat Thai
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/thai26_interspeech.pdf

## 问题
SSL 预训练 + CTC 微调在母语语音上强，但对口音变异敏感。口音特定方法需显式口音监督/结构改动；口音不变方法仍缺轻量、与通用 CTC 微调无缝结合的正则。

## 方法
在 CTC 微调时加 utterance 级 Supervised Contrastive（SupCon）辅助损失：对编码器隐状态均值池化后投影，以同一转写为正相关、不同转写为负相关，促进内容紧致、跨口音更稳的几何结构。训练期用、推理不加参；无架构修改、无口音标签。

## 实验与结果
L2-ARCTIC，未见转写（UT）/未见口音（UA）评测。wav2vec2-Large+4-gram：UT WER 10.47→9.14（相对约 −12.7%），UA 9.98→7.41（相对约 −25.8%）。在 W2V2/WavLM base/large、greedy 与 LM 解码上均一致降 WER；对 wav2vec2 增益通常大于 WavLM。within-transcript 余弦离散度均值 0.0518→0.0430（相对约 −17%），t-SNE 显示转写簇更紧。

## 结论
SupCon 是模型无关的轻量正则，能提升多口音 ASR 并收紧同转写跨说话人表示，尤其利于未见口音泛化。

## 点评
用“同一句不同口音应靠近”把口音不变做成对比几何，比口音分类头更少负迁移风险。增益在 UA 最大，符合不变性叙事。依赖基准中重复转写构正样本；无自然重复时需相似度分组或合成变体，外推仍待验证。
