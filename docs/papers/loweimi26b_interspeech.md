# Phonetic Error Analysis of Raw Waveform Acoustic Models

- 论文编号：798
- 报告人：Zhengjun Yue
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/loweimi26b_interspeech.pdf

## 问题
原始波形声学模型相对 Filterbank 系统的总体 PER 已知，但缺少按宽语音类（BPC）的错误分解与混淆模式分析：可学习前端是否改变混淆结构，BLSTM 与 WSJ 迁移对各 BPC 增益是否不均？

## 方法
在 TIMIT 上用参数化（SincNet、Sinc2Net）或非参数 CNN + BLSTM + FC，双头 CD/CI 输出。按三类分组（8 类音类、辅音/元音+/静音、浊/清/静音）分解 PER，并由替换错误建混淆矩阵。对比仅 CNN、加 BLSTM、以及 WSJ 预训练后仅重训末层的设定，并与 Filterbank 基线对照。

## 实验与结果
从头训练最佳 Test PER 15.3%（Sinc2Net+BLSTM）；WSJ 迁移后 CNN+BLSTM 达 11.3%/12.3%，超过 Filterbank-WSJ。加 BLSTM 对双元音/擦音/半元音相对降错最大（约 28%/19%/18%），元音约 10%。迁移学习辅音相对改善约 30%、元音+约 10%（约 3:1）。混淆主簇（塞音↔擦音；元音↔双元音↔半元音）跨原始波形与 Filterbank 一致，结构由语音学相近性主导。

## 结论
原始波形模型可达当前最佳 TIMIT PER；错误与混淆模式与 Filterbank 相近。时序建模惠及过渡依赖类，跨语料迁移更惠辅音。这些分解可指导类条件增广或损失加权。

## 点评
把“总 PER”拆成可解释的 BPC 诊断，澄清可学习前端并未改写主导混淆。强在与既有 Filterbank 分析对齐。局限：TIMIT 规模小、Affricate 样本极少方差大；尚未延伸到端到端或自监督大模型。
