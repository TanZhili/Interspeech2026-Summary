# Speaker Separation via Audio Language Modeling

- 论文编号：2864
- 报告人：Luca Lanzendörfer
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lanzendoerfer26b_interspeech.pdf

## 问题
传统分离依赖连续时频表示、掩码/PIT 与任务专用结构；离散编解码令牌虽已支撑 TTS 等生成，盲多说话人分离能否用因果语言模型从混合令牌一次解码出各说话人流仍少探索。

## 方法
LlaSep：XCodec2 将混合与各源编为 50Hz 离散令牌；Whisper-small 语义特征线性投影作条件；在 LLaSA-1B 骨干上监督微调，自回归生成最多 4 路说话人令牌流（特殊说话人分隔符）。构建 MLSEE-Conversation：MLS/Emilia/EuroSpeech 合成约 15k 小时、7 语、多种重叠模式。推理采样多次取均值。

## 实验与结果
LibriCSS：平均 DER 23.43%（PixIT 32.65%；掩码基线因固定两路输出 DER 极高）；DNSMOS-OVRL 3.13、ScoreQ-NR 3.95、ScoreQ-Ref 0.37，均优于对比。MLSEE 2 说话人 DER 28.11%、4 说话人 43.79%，仍优于 PixIT。CallHome 英/德：DER 24.84 vs PixIT 30.20，感知质量明显更高。生成流感知干净，但非字面复现源波形，内容保真依赖编解码与令牌准确率。

## 结论
令牌级语言模型可作为多说话人分离/日志化的可行范式；音质优势明显，说话人数增多时自回归误差累积。代码、检查点与数据开源。

## 点评
把分离写成“从混合前缀生成多流”，与掩码路线形成清晰对照：音质换可逆性。DER 仍不算低，且与固定两输出基线对比时对方吃亏。对真实电话场景零样本仍有效，说明合成对话预训练有迁移；4 说话人退化提示序列长度是瓶颈。
