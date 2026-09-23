# IPA-Guided Dual Transcription for Data-Centric Speech Corpus Refinement

- 论文编号：2221
- 报告人：Jeong-Ju Choi
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/choi26f_interspeech.pdf

## 问题
口语实现与正字法之间是多对多映射（日期、数字、缩写等），导致语料转写不一致，拖累下游 ASR/合成。纯文本 TN 看不到实际发音；已有双文本 STT 也未把识别器输出的音素流直接喂给下游消歧模型。

## 方法
数据中心框架两段：(1) Phoneme Intermediate Conditional（PIC）音频编码器——Conformer N=12，中间层 k=9 用 CTC 预测 IPA，末层 CTC 预测 subword，两损失等权；(2) Gemma-3-27B 经 LoRA/SFT + GRPO，以原始正字法与 IPA 为条件生成 (Written)/(Spoken) 双文本。IPA 来自 STT 而非仅文本 phonemizer，作为消歧主条件。

## 实验与结果
英语 TN（GoogleTN，TTS 合成评测语音）：Proposed 相对 Duplex 等，SA 88.7、WER 2.73、F1 0.981、DER 4.7（Duplex DER 10.2），数字类相对 Duplex 错误约降 53.9%。韩语牙科领域：由 YouTube 半自动建 100h KDSC，双转录得 KDSC V2；PIC+KDSC V2 在 KDent CER 5.1、KDigit WER 12.2，相对基线错误降约 69.8%/18.1%；原 KDSC 微调反而在领域集严重退化。

## 结论
IPA 引导双转录可缓解口语–书面歧义并支撑领域语料迭代精炼；作者承认英语 TN 评测用 TTS 而非自然语音，计划扩展到自然语料与更多语言/任务。

## 点评
把语料精炼做成「音素条件的双文本生成」，比纯文本 TN 多了声学落地。强在领域脏语料上 V1→V2 对比鲜明；脆弱点在 TN 诊断协议依赖参考 spoken 形式的 TTS，以及 LLM 规模与迭代环成本。
