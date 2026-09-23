# Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR

- 论文编号：2080
- 报告人：Henri-Leon Kordt
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kordt26_interspeech.pdf

## 问题
主流 ASR 常被训练为省略不流畅，导致信息丢失与幻觉；在小规模带标注不流畅数据上直接微调易灾难性遗忘，而全量联合重训不现实。

## 方法
在 whisper-small.en 上引入四类不流畅标记（FILLER、REP、DISRUPT、PAUSE），用 EWC、ER、A-GEM、Weight Averaging（WA）做持续学习。两阶段：(1) 在 SME 上引入标记并保留 LibriSpeech；(2) 从选定检查点顺序适应 Pitt 与 Delaware。用 pWER、标记 micro/macro-F1 及 BWT/FM/FWT/IM 等 CL 指标；用可学习门控的 head-attribution 与零掩码消融分析解码器交叉注意力头。

## 实验与结果
标记引入：WA 在 SME pWER 最低（9.64%）且 LS 最好，但标记 F1≈0；FT/ER/A-GEM 标记 micro-F1 约 0.73–0.75，SME pWER 约 12%。成功发标记时，少数交叉注意力头跨方法一致；掩蔽 Top-5 FILLER 相关头可减少约 57% FILLER 发射而 pWER 变化小。顺序适应：WA A-WER 最好（18.90%），ER 标记 A-F1 最好（0.49）；PAUSE 最难，ER 优势明显。LS 保留同样 WA 最优（4.68%）。

## 结论
CL 可在不联合重训下提升不流畅 ASR 与标记保持，但最优方法取决于目标：标记引入与保留偏 ER，ASR/干净语音稳定性偏 WA；标记学习对应稳定的交叉注意机制。局限为单一骨干与单一任务顺序。

## 点评
把「发出不流畅标记」与「保干净 ASR」拆开用 CL 权衡，比单纯微调更贴近真实增量部署。注意力头消融给出机制线索：强正则/权重平均可能压住标记专用回路。PAUSE 与 REP 的方法敏感性说明不流畅类型并非同等可学，部署时需按临床目标选 CL 策略。
