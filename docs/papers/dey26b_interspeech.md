# Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition

- 论文编号：3115
- 报告人：Spandan Dey
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/dey26b_interspeech.pdf

## 问题
端到端声学 NER 中，组织名因多词跨度、缩写、OOV 与跨度内非实体词，比人名/地名更难；常规交叉熵不显式建模实体起止结构依赖，边界易截断或外扩。

## 方法
基于 Whisper-small（编码器冻结，解码器前九层冻结）：(1) LLM（Phi-3-medium）针对性语义增强——缩写展开与词汇改写，再经规则清理，XTTS-2 多说话人合成语音；(2) 训练期专用 `<org end>` 边界标记；(3) Structure-Constrained Entity Learning（SCEL）：在 LCE 上叠加实体差分、标签抑制、跨度覆盖、边界一致性，以及熵正则与置信度标定。数据为 Yadav 等英文声学 NER 库（约 150h，LibriSpeech+Common Voice，90:5:5）。

## 实验与结果
相对纯 LCE（Org-F1 30.35），SCEL 将 Org-F1 提到 40.00、WER 8.27；SCEL+TSA+`<org end>` 达 Org-F1 51.40（相对 SCEL +11.40）、WER 9.53。优于 ASR+Flair 流水线（Org-F1 19.04）与 WhisperNER（约 30–31）。合成单跨/多跨测集上，提议框架多跨 Org-F1 明显高于 CE 基线。

## 结论
组织类弱点可通过对数据增强、类别边界标记与结构损失组合显著改善，同时保持 ASR 与其他实体类别可用；未来扩展多语声学 NER。

## 点评
诊断（多词、缩写、跨度内虚词）与解法（TSA、org end、SCEL）一一对应，比单纯放大 Whisper 更可解释。Org-F1 提升伴随整体 F1/WER 小幅回退，说明类别特化存在权衡；LLM-TTS 增强对真实录音分布的外推仍是主要风险点。
