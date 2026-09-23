# Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR

- 论文编号：1837
- 报告人：Pravina Mylvaganam
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mylvaganam26b_interspeech.pdf

## 问题
澳大利亚原住民语言 Warlpiri 转写语音极少（本文约 1.5 小时、18 说话人），跨语迁移关键，但源语常按语系/地理启发式选取，未必反映声学或语言类型相似度。

## 方法
先用 VoxLingua107 上 ECAPA-TDNN LID 预筛近邻语；再以 ECAPA、wav2vec 2.0、XLSR-53 层间嵌入余弦测声学相似度，并以 WALS/SSWL/PHOIBLE/Grambank 等算句法、音位清单、语法与总体类型距离。Whisper-small：先在各高资源源语微调，再微调 Warlpiri；对照单语、原多语 Whisper/XLSR-53 与最不相似源语。Spearman 相关分析相似度与零样本/微调 WER、CER。

## 实验与结果
近邻含 Assamese、Hindi、Tamil 等，非 Pama–Nyungan、亦非地理邻近；英语/日语声学最远。Assamese 微调最佳：WER 32.6%、CER 12.3%（单语 86.9%/41.3%，多语 Whisper 41.0%/15.1%）。Hindi/Telugu/Tamil 约 37.6–40.7% WER；日语/爪哇语更差。零样本：音位清单与类型相似度相关更强；微调后声学相似度相关最强（ρ_WER≈−0.67）。

## 结论
系统相似度排序可改进 Warlpiri ASR 迁移；声学近邻主导微调收益，音位/类型更解释零样本。语系或地理亲近不是充分标准。

## 点评
把“选谁做源语”做成可检验的相似度–下游链路，对极低资源原住民 ASR 实用。强在多维相似度与相关分析；弱在 Warlpiri 数据仍极短、仅 Whisper-small，且部分语缺完整语言特征。
