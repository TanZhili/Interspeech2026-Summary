# MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis

- 论文编号：1031
- 报告人：Tan Dat Nguyen
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26c_interspeech.pdf

## 问题
LLM-TTS 依赖自回归 Transformer，长序列下自注意力二次复杂度与 KV cache 膨胀，限制播客/有声书/边缘部署。纯 Mamba 线性高效但全局上下文与表达力不足；已有混合方案多需昂贵从头预训练且细节不公开。

## 方法
提出 MamTra：在预训练 CosyVoice 2 上按多种策略（Interleaved BlockBeg/End、Contiguous Front/Middle/Back/Sandwich、数据驱动 Importance）把部分 Transformer 换成 Mamba，比例 1:1 到 1:11。用注意力线性化与 SSM 的结构对应，把教师 Q/K/V 投影初始化到 Mamba 的 C/B/x。再用多层蒸馏恢复性能：L = LCE + Llogits（skew KL）+ Lemb（token embedding MSE）。训练只用约 0.5k 小时 LibriTTS（约为教师英语数据的 2%）。

## 实验与结果
评测 Seed-TTS-eval test-en 与 LibriTTS test-clean。MamTra 1:1（BlockBeg）相对 CosyVoice 2：VRAM 可降约 34%，每 token FLOPs 在上下文 2048 时最多省约 1.4×10^11；WER 仅绝对升约 0.25%（2.03→2.28），NMOS/UTMOS/SSIM 接近教师。更激进 1:11 时可懂度明显下降。BlockBeg 在低成本扫描中 CE/WER 更稳；高替换比时 WER 重要性选层更有效。消融显示去掉 LCE/Llogits/Lemb 都会抬高 WER；重用预训练权重收敛远快于 Xavier/Kaiming。

## 结论
通过结构化替换、权重迁移与多层蒸馏，MamTra 可在很少数据上恢复教师级质量，并显著降低推理显存与计算，适合内存受限的长上下文 TTS。

## 点评
价值在“转换预训练 Transformer→混合骨干”而非从零训 SSM：把二次注意力瓶颈换成局部线性状态，同时保留少量全局层。BlockBeg + 适度替换比是效率–质量甜点；过度替换（1:11）会跌破可懂度底线。脆弱点包括蒸馏对教师分布的依赖，以及 Importance/WER 选层在新域是否可迁移。
