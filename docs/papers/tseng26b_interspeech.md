# TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling

- 论文编号：1686
- 报告人：Liang-Hsuan Tseng
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26b_interspeech.pdf

## 问题
文本–语音联合建模受长度不匹配困扰；TASTE 用文本对齐 token 缓解，但依赖外部离线 ASR 与非因果解码，无法流式。

## 方法
提出 TASTE-S：编码器内置 CTC ASR 即时取文本；Aggregator+VQ 生成文本对齐语音 token；解码端因果 Unit decoder（N:M 交错）+ 因果流匹配声码器。两阶段训练：先用金标转写训 Aggregator/Decoder，再联合适配 CTC 预测。数据约 Emilia 400 h + LibriTTS 600 h。

## 实验与结果
与 TASTE 质量相当（CTC 路径 WER≈4.1%、UTMOS≈4.11、说话人相似≈0.88），编码 RTF 从依赖外部 ASR 的约 0.117 降至约 0.002；对转写噪声更稳，支持长篇编解码。交叉注意力仍保持文本–语音对齐。

## 结论
内置 ASR + 因果解码使文本对齐分词可流式落地，且不牺牲重建质量，利于实时 SLM。

## 点评
把“对齐”与“流式”同时做进分词器，比事后 padding/交错更干净。两阶段+联合训练对 CTC 误差鲁棒是关键。重建评测偏 LibriSpeech clean；真实对话噪声与多语仍待验。
