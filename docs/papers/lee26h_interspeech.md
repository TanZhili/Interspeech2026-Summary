# UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction

- 论文编号：909
- 报告人：Sangmin Lee
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26h_interspeech.pdf

## 问题

多语言 TTS 文本编码器常依赖 G2P，可靠工具约仅覆盖百来种语言；纯文本预训练又缺声学线索。需在更大语言覆盖下保持音素保真与文本–语音对齐。

## 方法

提出 UR-BERT：用 Uroman 罗马化统一书写系统；BERT-base 字符级分词；预训练除 MLM 外增加 speech token prediction（STP）：从 omnilingual ASR W2V 中间层提特征，经 MMS-FA CTC 强制对齐到字符，再 k-means（256+静音）离散化为目标。预训练语料约 13K 小时、8M 句、495 语。下游冻结/微调后接 VITS。

## 实验与结果

高资源英/德/普：UR-BERT 的 MOS 分别为 4.35/3.78/3.88，优于 XPhoneBERT 与 m-PLBERT。低资源多语（含 XPhoneBERT 不支持的爪哇语等）MOS 全面最高；未见语巽他语零样本仍优于纯 VITS。消融显示 STP 多数语言提升 MOS。预训练句数仅约 XPhoneBERT 的 2.5%。

## 结论

作者认为罗马化突破 G2P 覆盖瓶颈，STP 补偿罗马化音素粗粒度，可在数据更少时扩展到数百语并保持合成质量。

## 点评

用“共享拉丁书写 + 声学 token 蒸馏”同时扩覆盖与保音素，比堆更大 G2P 更可扩展。罗马化跨语同形异音仍可能混淆，STP 是关键补偿。评测依赖多语 ASR/UTMOS，跨语偏差用相对指标缓解，但仍需留意。
