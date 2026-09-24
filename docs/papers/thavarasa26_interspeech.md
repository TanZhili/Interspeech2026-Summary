# KuralHub: Exposing Typological Capability Frontiers in Multilingual Speech Emotion Recognition

- 论文编号：3502
- 报告人：Jubeerathan Thevakumar
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/thavarasa26_interspeech.pdf

## 问题
SER 进展受高资源语言偏置；跨语迁移是否主要由预训练数据量决定，还是受语言结构类型约束，缺乏大规模系统证据。

## 方法
KuralHub：在 29 语、33 个公开数据集上评测 11 个冻结自监督骨干（HuBERT、Wav2Vec2、WavLM、Whisper 等变体）+ 轻量分类头，统一五类情绪设定；报告跨语与语系差异。

## 实验与结果
跨语可迁移性更受类型结构约束而非预训练数据量：对汉语、阿姆哈拉语等可较好适应，但对达罗毗荼语族（如泰米尔、卡纳达）系统失败，模型间方差很小（泰米尔均值 UAR 约 0.31）。单纯放大参数无法消除该瓶颈。

## 结论
暴露类型能力边界，呼吁类型感知预训练与公平 SER 路线图；开源基准服务低资源语言。

## 点评
把「数据多少」与「结构远近」对照，比只报平均 UAR 更有诊断价值。数据集在 elicitation、标签体系与样本量上异质，语系失败也可能混入录音/标注质量；但仍提供强信号：达罗毗荼语需专门表征策略。
