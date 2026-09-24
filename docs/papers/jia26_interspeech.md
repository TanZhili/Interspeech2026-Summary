# Augmenting Dysarthric Speech Severity Assessment with MOS Supervision

- 论文编号：1300
- 报告人：Zengrui Jin
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jia26_interspeech.pdf

## 问题
构音障碍严重度评估依赖临床标注，数据稀缺；生成式增强缺乏感知级重标注，难直接服务严重度回归。合成语音伪影与构音障碍在可懂度/自然度上有感知共性，能否用 TTS MOS 语料作增强。

## 方法
SSL（wav2vec 2.0 / HuBERT）均值池化 + 两层回归头，端到端微调。目标：SAP 开放域构音障碍语料的 Intelligibility / Naturalness（1–7）。辅助：QualiSpeech 的 Overall / Naturalness MOS（1–5），线性映射到 SAP 尺度。两种范式：JT（1:1 混合联合回归）；FT（先 QualiSpeech 再 SAP）。

## 实验与结果
开发集作测试（说话人未见）。FT 在两维上稳定优于仅域内训练；JT 对自然度有效，对可懂度常负迁移。维度匹配增强（QualiSpeech Naturalness→SAP Naturalness）MSE 相对降幅最大（如 wav2vec Base 约 36.4%）。小编码器在仅域内时更稳，大模型更吃增强。

## 结论
TTS 评估语料可作标签高效增强；可懂度更适合顺序微调而非联合优化。合成失败与构音障碍共享感知/声学共性。

## 点评
把“感知 MOS”直接接到临床严重度，绕过无标注合成。可懂度与 Overall/Naturalness 语义错位解释了 JT 失败，论证清楚；SAP 可懂度标签严重偏斜（多为 1）仍限制上限。
