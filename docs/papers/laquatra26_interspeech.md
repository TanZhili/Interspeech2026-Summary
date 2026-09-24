# Etiology-Aware Speech Language Models for Dysarthric Speech Recognition

- 论文编号：1773
- 报告人：Moreno La Quatra
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/laquatra26_interspeech.pdf

## 问题
标准 ASR 忽略说话人神经病因，难利用病种特异声学–语音模式；如何把病因知识放进语音语言模型仍不清楚。

## 方法
在 SLM 上比较四种策略：标准 SFT；辅助病因分类头（EC，预测不进入解码器）；输入提示给出病因（EH）；自回归先预测病因再转写（EP）。在 Kimi（SAP 上 SFT 最强）上用 LoRA 做 EC/EH/EP；SAP 含 ALS、Parkinson、Stroke、Down Syndrome、Cerebral Palsy；零样本测 TORGO。

## 实验与结果
SAP：Kimi-EP 总体 WER 7.77%、SemScore 91.05，相对 SFT 8.30% 相对降 6.4%（p<0.001）。EC 病因准确率 81% 高于 EP 的 72%，但 WER 8.49% 更差。EH 为 8.22%。EP 在五类条件上均优于 SFT/EC/EH；低资源 Stroke 上 EP 相对 SFT 相对降约 19%。TORGO：EP 总体 15.8% 优于 EH/EC/SFT。EP 误分样本 WER 不差于正确预测，暗示「预测行为」本身迫使模型关注病理声学。

## 结论
病因推理须进入生成流才能惠及转写；自生成临床评估优于被动提示，且推理时无需病因标签。训练仍需病因标注。

## 点评
关键对照是「准确率高但未进解码器的 EC」vs「准确率较低但因果条件化的 EP」，说明放置位置重于分类精度。EH 有 oracle 病因仍逊于 EP，支持主动推理假说。健康说话人无 SAP 标签时 EP 被迫归因，跨域提示设计仍需谨慎。
