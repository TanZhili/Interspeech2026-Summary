# GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation

- 论文编号：822
- 报告人：Abeer Alwan
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shankar26_interspeech.pdf

## 问题

Whisper 等 Transformer 基础模型在混响、窄带、方言、儿童等声学失配域上掉点；标准 LoRA 调全局注意力，缺局部时序建模，难以补足 Conformer 式局部归纳偏置。

## 方法

提出 GC-LoRA：在 MHSA 输出投影 Wo 的低秩旁路中，嵌入 Conformer 风格门控深度可分离卷积（pointwise+GLU、depthwise、GroupNorm、Swish、再 pointwise），在瓶颈内做局部精炼。相对标准 LoRA 参数更少（如 medium 上 447k vs 829k）。

## 实验与结果

Whisper-medium：AMI/SWBD/CORAAL/MyST WER 11.5/6.3/9.9/8.6，相对 LoRA 显著更优（p&lt;0.05），参数约少 46%。跨 tiny–large-v3 多数设定仍优；tiny+AMI 相对降约 10.9%。消融显示门控深度卷积优于简单 Conv-LoRA / MultiConv-LoRA；推理延迟几乎与 LoRA 相当。

## 结论

作者认为在 LoRA 瓶颈内注入局部卷积，能以极少参数让 Transformer 获得更强声学域适应，缩小与全量微调差距。

## 点评

针对“Transformer 缺局部”的结构补丁放在注意力输出处，不改预训练全局注意，设计克制。增益在失配域一致，但绝对幅度不大；全量微调仍常更强。超参固定跨模型规模，可能解释部分非单调缩放。
