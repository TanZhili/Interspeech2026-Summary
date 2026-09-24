# Assessing True Generalisability of Audio-Visual Speech Recognisers

- 论文编号：2583
- 报告人：Zhaofeng Lin
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lin26m_interspeech.pdf

## 问题
AVSR 在 LRS3 上已近饱和（干净 WER <1%），但测试集仅约 0.9h，疑似对 LRS3 分布过拟合。WildVSR 等未见集缺音频，无法评 AVSR。需要严格匹配分布的未见评测来检验真泛化。

## 方法
从 MultiVSR 子采样构建 MV2LRS3：在声学、视觉与人口统计七因子（时长、年龄、性别、肤色、头姿、SNR、语速）上对齐 LRS3 test。评五个 SoTA（含 AV-HuBERT、Auto-AVSR、Llama-AVSR 等）；做属性分析、词表内外对比、A/V/AV 三设定与错误类型分析；发布数据与元数据。

## 实验与结果
五模型在 LRS3 上 WER 约 0.77–1.50%，在 MV2LRS3 上崩至约 14.0–23.5%（如 Llama-AVSR 0.77→16.5，Auto-AVSR 0.95→14.0）。扩大匹配集仍稳健。存在词表偏置：限制到 LRS3 共享词汇可相对改善（如 Whisper-Flamingo 至 9.9%，约 47% 相对提升）。多数模型 AV 甚至差于 audio-only；替换/删除/插入模式因模型而异。

## 结论
对齐分布仍崩溃→近完美 LRS3 分数不等于真泛化；词表与模态融合是关键短板。作者释放 MV2LRS3 作未来基准。

## 点评
用「匹配分布的未见集」区分分布漂移与记忆过拟合，比随意 OOD 更有说服力。强在七因子与词表隔离；脆弱点在 Whisper 生成转写可能引入标签噪声，以及 MultiVSR 来源与 TED 风格差异仍可能残留。
