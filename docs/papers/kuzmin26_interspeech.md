# StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation

- 论文编号：3105
- 报告人：Nikita Kuzmin
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/kuzmin26_interspeech.pdf

## 问题
流式神经音频编解码（NAC）语言模型做说话人匿名化时，continuation 训练会让模型默认主导声学模式，VQ 瓶颈也丢情感细节；用多样情感 prompt 虽能部分提 UAR，却伤可懂度且难获取。

## 方法
在 StreamVoiceAnon 上监督微调：同说话人中性–情感成对（含中性–中性），迫使情感来自 source 而非 prompt；语义/声学分支加可学习 [SEP]；对 Slow AR 声学隐状态做帧级 Emotion2Vec+ 蒸馏（Lemo），总损失 LLM + w·Lemo（w=0.01）。推理去掉蒸馏头，延迟仍约 180 ms。在 CREMA-D 构约 25k 对微调 5 epoch；按 VPC 2024 评 EER/WER/UAR。

## 实验与结果
frame-distill：UAR 49.2%、WER 5.77%、EER-L 48.98%（semi 18.30%）；相对中性 prompt 基线 UAR 39.7% 约 +24% 相对提升，优于情感 prompt 变体 44.6%。消融：仅情感数据 +1.4 UAR，中性–情感对 +4.2，[SEP] 再 +2.1；声学分支蒸馏优于语义分支（WER 更低）。sad 由 8.0%→42.6%，happy 过预测被纠正。微调 <2 小时、推理零额外延迟。

## 结论
情感退化主要是训练范式而非容量问题；声学帧级蒸馏可在流式约束下显著提升情感保留并略增隐私。仍落后离线 EASY（63.8% UAR）；局限含单一 SER 评测器与表演语料。

## 点评
把“从 prompt 抄风格”改成“从 source 还原情感”，并用声学支路避开与 LM 损失的梯度冲突，设计干净且零延迟开销。相对其他流式方法在隐私–情感平面领先，但离线全句建模仍有明显差距；表演情感与 VPC SER 协议下的数字外推到自发情感需谨慎。
