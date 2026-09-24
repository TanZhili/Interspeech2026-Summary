# A System-Agnostic Approach to Modelling Interaction Quality in Spoken Dialogue Systems

- 论文编号：1152
- 报告人：Paul Gering
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gering26_interspeech.pdf

## 问题
交互质量（IQ）分类以往多用系统日志等系统依赖（SD）特征，难以跨系统泛化。系统无关（SA）路线缺少声学线索验证；能否用声学+文本+时间特征替代日志特征。

## 方法
在 LEGO（公交电话对话，229 对话/5477 exchange，中位 IQ 1–5）上对比 SD 与 SA。SA：Silero VAD + Whisper 转写（人工校正）、eGeMAPS、HuBERT/WavLM/Wav2Vec2 池化、RoBERTa/SBERT/TOD-BERT 文本嵌入及话轮时长/延迟/重叠等。两阶段：静态冻结编码器 + LSTM；端到端微调编码器与后端。

## 实验与结果
调参 Macro-F1：静态 SD 0.557 vs SA 0.498；微调后 SD 0.593 vs SA 0.530。测试集最终：微调 SA MF1/UAR 0.454/0.453，接近 SD 0.462/0.471，优于多数类；相对 Ultes UAR 0.540，微调 SD UAR 0.471、SA 0.453。微调提升 SA 但计算与延迟更高。

## 结论
端到端微调时，声学–文本–时间 SA 特征可接近 SD 日志特征，成为可跨系统的 IQ 建模替代；静态管道下 SD 仍更优。

## 点评
把“可迁移评估”落到有音频的 LEGO 上，填补了先前纯文本 SA 工作。标签偏斜与电话噪声削弱声学嵌入；半自动转写校正使 SA 并非完全自动，作者也指出需更新语料与全自动流水线。
