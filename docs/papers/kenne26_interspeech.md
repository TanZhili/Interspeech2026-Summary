# Multi-Level Privacy-Preserving Dementia Detection from Speech via Targeted Adversarial Obfuscation and Representation Learning

- 论文编号：2868
- 报告人：Henriette Flore Kenne
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/kenne26_interspeech.pdf

## 问题
痴呆检测语音同时暴露说话人身份与转写内容；既有隐私方法常只防单一威胁，或牺牲诊断效用。

## 方法
双层框架：(1) 信号级 Cumulative Signal Attack（CSA）：在关键词对齐片段用 PGD+CTC 把波形推向语义偏离目标转写，累计整形扰动以保韵律；(2) 特征级：共享编码器 + GRL 压制说话人支路，并用互信息引导噪声注入保护与痴呆相关的韵律维、破坏说话人维。在 DementiaBank Pitt 上评测 ASR WER、说话人 F1/EER 与痴呆 F1/AUC。

## 实验与结果
摘要报告 WER=1.00、说话人 EER=0.59、说话人 F1=0.003、痴呆 F1=0.78、AUC=0.86。相对噪声等基线，双层在保持较高痴呆 F1（约 0.79 vs 原 0.83）同时更强压制说话人；白盒窃听下说话人 F1 约 0.003、EER≈0.50、Whisper WER=1.00。

## 结论
信号语义混淆与特征层说话人对抗可同时抵御机器转写与说话人再识别，并保留可用诊断性能。

## 点评
把威胁拆成「听懂内容」与「认出是谁」两路分别打，比单点匿名更贴临床共享场景。关键词对齐扰动依赖转写质量；不可逆扰动利于隐私但不利于事后审计。效用仍用宏 F1/AUC，临床部署还需校准阈值与可解释性。
