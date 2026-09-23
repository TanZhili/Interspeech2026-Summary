# Constrained CTC decoding for Efficient Diacritic Restoration

- 论文编号：3220
- 报告人：Rufael Marew
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marew26_interspeech.pdf

## 问题
阿拉伯语文本常缺标音符号，纯文本复原对同形异音仍模糊；已有语音+文本多模态复原有效但计算重、跨域弱。需在保持字母骨架不变的前提下，用语音高效恢复 diacritics。

## 方法
在给定语音与无标音参考 \(u\) 时，用 CTC ASR（Wav2vec2-XLSR 微调）预测含字母与复合标音标签的序列；推理时由 \(u\) 构图字符级 diacritization lattice（字母固定、其后通配符位只允许 diacritic/blank），与 CTC 解码图组合或限制 beam，实现部分强制对齐式约束解码。无标音用 CTC blank 表示。对比 Text-only 与 Text+ASR 基线（后者可额外用 Tashkeela 文本预训练）。

## 实验与结果
数据：ClArTTS（CA，12h 训 / 0.3h 测）、ArVoice 1+3（MSA，6h / 0.9h）。匹配 ClArTTS：Ours WER/DER 11.21 / 3.53，接近 Text+ASR。跨域与联合训练：Ours 明显更稳（如 ClArTTS 训→ArVoice：DER 12.04 vs Text+ASR 19.21；联合训练 ClArTTS DER 3.80、ArVoice 8.69）。bootstrap 95% CI 显示相对 Text+ASR 的 DER 改善显著。

## 结论
约束 CTC 解码在 CA/MSA 上优于或持平多模态基线，且更精简高效，可直接作带标音 ASR 或对无标音标注语音做复原，利于阿拉伯语数据策展。

## 点评
把“字母骨架硬约束”下沉到解码图，避开额外文本编码器与融合训练，效率与跨域表现合理。依赖已有无标音参考；未覆盖方言且基线独享大规模文本预训，公平性上作者已说明。
