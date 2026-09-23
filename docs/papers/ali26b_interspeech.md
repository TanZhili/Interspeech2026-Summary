# MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio

- 论文编号：1522
- 报告人：Umberto Cappellazzo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26b_interspeech.pdf

## 问题

微调大语音/音频基础模型成本高，PETL 已普及；Mamba 擅长线性复杂度长序列建模，但尚未作为适配器注入 Transformer 做高效迁移。

## 方法

提出 MambAdapter：在瓶颈适配器低秩空间插入轻量 Mamba，并用可学习缩放 α；跨层共享 down/up 投影以抵消 Mamba 参数开销。用于 AST 音频分类与 Whisper 多语 ASR（仅编码器插适配器，解码器冻结）。

## 实验与结果

分类（Pfeiffer）：MambAdapter 约 0.06M 参数，平均准确率 89.72，接近 Conformer 适配器（0.27M，90.07）且远超 LoRA/Bottleneck。ASR（五语）：平均 WER 优于 Bottleneck/Conformer/LoRA（同参预算下约降 0.8–7.4%）。低参预算（&lt;500k）优势更大；去 Mamba 则 FSC 等任务大幅掉点；共享投影以约 4× 参数换不到 1% 平均收益。

## 结论

作者认为把 Mamba 放进共享投影瓶颈，可在更少可训参数下匹配或超过强 PETL 基线，是首个将 Mamba 用于语音/音频 PETL 的工作。

## 点评

用 SSM 的时间压缩特性匹配低秩瓶颈，理论动机清楚。分类上与 Conformer 适配器接近但更省参；ASR 增益更明显。超参（expand、d_state、kernel）对结果敏感，文中有网格分析。未探索解码器侧适配。
