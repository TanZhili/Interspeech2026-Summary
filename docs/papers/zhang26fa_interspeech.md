# MPA-KWS: Multi-Modal Phoneme-Level Alignment for Streaming Open-Vocabulary Keyword Spotting

- 论文编号：2485
- 报告人：Jue Zhang
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26fa_interspeech.pdf

## 问题
音素级对齐有助于区分易混词，但多数非流式；现有流式 CTC 对齐多仅支持文本注册，且训练/推理对齐策略不一致、跨模态 InfoNCE 未利用音–文非对称性。

## 方法
MPA-KWS：因果 Conv1dNet + 交叉注意力偏置注入关键词音素先验；W-CTC 强制对齐聚合音素级声学嵌入（训练推理一致）；音–文用 AsyP 损失、音–音用对称 InfoNCE；验证器交互特征 + BiGRU。支持文本-only 与文本–音频注册（训练 50% 掩码支持音频）。CTC beam-search 动态挖硬负文本。推理滑窗对齐，复杂度 \(O(W\times L_p)\)。

## 实验与结果
LibriPhrase（4.0M 参数）：文本-only AUC LPH/LPE 96.04/99.95，EER 9.53/0.77；文本–音频 97.30/99.98，EER 8.21/0.45，优于所列 CMCD、W-CTC、MM-KWS、PLCL。消融：去音素损失、去增强、去偏置、仅 InfoNCE 均掉点。

## 结论
作者认为统一 W-CTC 流式音素对齐 + 非对称跨模态对比与硬负挖掘，可在流式开放词表 KWS 上达到最佳结果并支持多模态注册。

## 点评
同时解决流式、多模态注册与训练–推理一致三个痛点，LPH 提升说明针对易混词设计有效。模型约 4M，相对超轻流式方案更重；依赖 g2p 与 CTC 对齐质量。
