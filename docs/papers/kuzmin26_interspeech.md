# StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation

- 论文编号：3105
- 报告人：Nikita Kuzmin
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/kuzmin26_interspeech.pdf

## 问题
基于神经音频编解码语言模型的流式说话人匿名化常损害情感：续写训练范式与 VQ 瓶颈使模型偏向主导声学风格，而非保留源情感；多情感提示虽能部分缓解，却损可懂度且难获取。

## 方法
在 StreamVoiceAnon 上做监督微调（仅 Slow/Fast AR）：用同说话人中性–情感对（CREMA-D，约 2.5 万对）迫使情感来自源内容而非提示；加语义/声学 [SEP]；并用 Emotion2Vec+ 帧级特征对 Slow AR 声学隐状态做蒸馏（Lemo，w=0.01），推理时去掉蒸馏头，延迟仍约 180 ms。VPC 2024 评 EER/WER/UAR。

## 实验与结果
frame-distill：UAR 49.2%、WER 5.77%、EER-L 48.98%；相对中性提示基线 UAR 39.7% 相对提升约 +24%，相对情感提示变体 44.6% 约 +10%。消融显示中性–情感配对增益最大（+4.2 UAR），声学支路蒸馏优于语义支路；sad 由 8.0%→42.6%，happy 过预测被纠正。相对其他流式方法情感保留最高，但仍低于离线 EASY（63.8% UAR）。

## 结论
情感退化主要是训练范式问题；配对重构加声学帧级蒸馏可在零推理开销下显著提升情感保留并略改善隐私。局限包括单 SER 评测器、无主观听测、仅表演情感语料。

## 点评
把“提示复制情感”拆成可验证的训练信号，比堆推理提示更干净。蒸馏落在无内容监督的声学支路，避免与 LM loss 抢梯度，设计合理。流式与离线差距仍大，且 IEMOCAP/CREMA-D 表演情感外推到自发场景需谨慎。
