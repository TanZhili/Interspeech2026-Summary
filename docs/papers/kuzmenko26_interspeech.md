# GigaAM Multilingual: Foundation Model for Underrepresented Languages

- 论文编号：2483
- 报告人：Andrei Kuzmenko
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kuzmenko26_interspeech.pdf

## 问题
多语 ASR 在中亚长尾语（哈/吉/乌）上因数据极度偏斜表现差；朴素上采样易伤头语种，需可迁移的预训练与微调采样策略。

## 方法
GigaAM Multilingual：600M Conformer，HuBERT 式掩码单元预测，在约 2M 小时音频上预训练。用语言共现图聚类得 5 簇，簇级重加权（最终 E2 提高中亚簇权重）。微调 CTC 共享字符表，数据含开源/众包/弱监督/合成；域感知采样避免合成子集主导。

## 实验与结果
哈/吉/乌在 CV、FLEURS、内部野外集上大幅优于 Whisper-large-v3、Seamless M4T、Omnilingual 1B。匹配 CTC 微调下，即便 240M 变体平均 WER 亦优于 Whisper/Omni。簇重加权 E2 改善目标语且俄语几乎不变；域感知采样尤其抬升内部自发语。极低覆盖巴什基尔/格鲁吉亚适配亦最优。

## 结论
簇级预训练平衡 + 域感知微调是长尾多语 ASR 的有效配方，并开源编码器与 ASR 模型。

## 点评
贡献在数据混合与采样工程，而非新目标函数；受控编码器对比说明“预训练分布匹配目标语族”比盲目用更大通用编码器更重要。合成/弱标签过滤细节决定可复现性。
