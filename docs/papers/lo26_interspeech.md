# A Novel Sentence Stress Detection Framework Leveraging Auxiliary Word-Stress Modeling and Loss Optimization

- 论文编号：1494
- 报告人：Tien-Hong Lo
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lo26_interspeech.pdf

## 问题
自动发音评估（APA）中的韵律重音包含句重音检测（SSD）与词重音检测（WSD），二者都依赖音高、时长、强度等线索，但多数工作把它们当独立任务。SSD 在 Whisper 子词分词下还会出现同一重读词内多个 token 概率弥散的问题；现有对齐式管线依赖时间戳质量，对齐无关的 WhiStress 又未引入词级重音约束。

## 方法
提出 STRAW：冻结 Whisper-small 骨干，仅训练任务头与 phone embedding。SSD 以 decoder 状态为 query、encoder 状态为 key/value，经 Transformer decoder 块与 FCNN 做 token 级二分类；评测时任一 token 判为重读则该词判为重读。WSD 用 G2P（CMU 式带 stress digit）得到 phone 序列，经可训 phone embedding 与 encoder 交叉注意力做 phone 级二分类（仅 digit “1” 标为重读）。另加词跨度重音正则器 WSR：对每个真值重读词的子词跨度，鼓励唯一优势 token 概率接近 1、其余接近 0，并用跨度内概率总和偏离 1 的程度加权。总损失为 α·L_SSD + β·L_WSD + λ·L_WSR（默认均为 1）。朗读 APA 设定下用参考转写提供 token/phone，不必额外 ASR。

## 实验与结果
数据为 TinyStress-15K（合成、词级重音标注）：Train/Valid/Test 各 13.5k/1.5k/1k 条。SSD F1：GT alignment 0.858、MFA 0.815、WhiStress 0.909、STRAW 0.934；去掉 WSD/WSR/二者分别为 0.922/0.929/0.915。WSD 上 STRAW F1 约 0.920，去 WSR 几乎不变。POS 误差分析显示功能词（PART、DET 等）假阴性有所下降，SCONJ 因样本少仍偏高。

## 结论
在统一冻结 Whisper 框架内同时做 SSD/WSD，并用 WSR 缓解子词跨度内重音弥散，完整配置在 TinyStress-15K 上取得最高 SSD F1。作者指出局限：词重音简化为每词单一主重音、两头无直接交互、评测仅限合成语音；计划扩展到自发/真人录音并加强跨任务耦合。

## 点评
做法把共享韵律线索拆成“辅助监督 + 语言学正则”，而不是硬共享隐状态，消融也承认 WSD 消融不能证明向 SSD 的知识迁移。WSR 直接针对 Whisper 子词分词的标注模糊，设计动机清楚；主要脆弱点是合成数据上的表观增益能否迁移到自然重音，以及两头分离导致无法强制句/词重音一致性。
