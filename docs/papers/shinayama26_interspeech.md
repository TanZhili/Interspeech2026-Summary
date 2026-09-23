# Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition

- 论文编号：1630
- 报告人：Kentaro Shinayama
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shinayama26_interspeech.pdf

## 问题

多语联合微调大预训练 ASR 时，共享容量不足易负迁移，甚至不如分语种模型。LoRA-MoE 等轻量专家容量有限，难充分表达语种差异。

## 方法

将 Whisper 解码器 FFN 上循环（复制预训练参数）为稀疏 MoE，每 token 仅激活 1 个专家，活跃参数与稠密模型相同。路由：按语言身份硬路由，或基于隐状态（±语言嵌入）的 soft top-1。编码器保持共享。在 CommonVoice 10 语与亚洲 4 语上评测。

## 实验与结果

CommonVoice：硬路由 10 专家平均优于 MultiFT 与 LoRA-MoE，甚至优于 MonoFT 上界（西欧 5 语 WER 12.3 vs MultiFT 13.6）。亚洲 4 语硬路由平均 CER 5.2 vs MultiFT 6.2（约相对降 16%）。上层解码器放置 MoE 即可接近全层效果且参数更少。对 medium/large-v2 仍有效。Soft 路由更省专家数但弱于硬路由。

## 结论

作者认为直接扩容 FFN 专家比低秩专家更利于多语微调；硬路由强制语种分工，减轻负迁移；语言依赖主要在解码器上层。

## 点评

“上循环=复制 FFN 成专家”简单可落地，推理成本几乎不变。硬路由需可靠语言 ID；soft 路由因专家同初始化难分化是文中坦承的局限。对书写体系差异大的语种集合尤其有说服力。
