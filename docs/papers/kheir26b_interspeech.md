# IQRA 2026: Interspeech Challenge on Automatic Assessment Pronunciation for Modern Standard Arabic (MSA)

- 论文编号：2445
- 报告人：Yassine El Kheir
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kheir26b_interspeech.pdf

## 问题
阿拉伯语 MDD 长期缺统一基准与开放标注数据；上一版 IqraEval 无真实人为误读训练数据，最佳 F1 约 0.47。MSA 音位复杂（咽音、强调对立等）且存在双言现象，需要可复现的共享评测与真实误读语料。

## 方法
组织 IQRA 2026：任务给定语音与带元音符号参考文本，预测实际发音音素序列（68 音素 MSA 清单），与规范/verbatim 对齐后算 TA/FR/FA/TR、Precision/Recall/F1（主指标）与 PER。训练资源含 Iqra train（~79h）、Iqra TTS（~52h）及新增真实误读 Iqra Extra IS26（1,333 句，~1.5h）；测试 QuranMB.v2（1,643 句）。基线为冻结 mHuBERT + 加权层和 + BiLSTM-CTC，F1=0.4414。

## 实验与结果
19 队参赛；13 队超基线。榜首 whu-iasp F1=0.7201（相对基线 +0.2787），UTokyo 0.7170，RAM 0.7157；前六均 F1>0.67 且 PER≤0.0445。方法覆盖增强 CTC/时间建模、SSL+LM、生成式 LALM（Kalimat 第 6）。共性发现：真实误读数据对顶名次至关重要；低名次系统常高召回低精确。相对上一版最佳约翻倍。

## 结论
开放训练数据、真实误读语料与多样建模共同推动阿拉伯语 MDD；仍缺音素级诊断到学习者可读字符/变音符反馈的映射，以及面向自然语言反馈的生成式评测。

## 点评
作为挑战综述，价值在数据补齐（尤其 Extra IS26）与全榜诊断，而非单一模型。顶名次方法路径多样却分数接近，说明数据质量与对齐精度比单纯堆模型容量更关键；后续瓶颈明确指向字符级可操作反馈与更大规模真实学习者语料。
