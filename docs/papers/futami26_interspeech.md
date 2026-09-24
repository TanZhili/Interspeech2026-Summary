# Merging the Knowledge of LLMs for Automatic Speech Recognition

- 论文编号：2561
- 报告人：Hayato Futami
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/futami26_interspeech.pdf

## 问题
LLM 基 ASR 域适应常靠浅融合/密度比在解码时调用外部 LM，大模型每步推理成本高；需把目标域文本知识并入参数、推理零额外开销。

## 方法
同一预训练 LLM 上：ASR 用 LoRA，目标/源域 LM 亦用 LoRA。域扩展合并（对应浅融合）：θ = θ_pre + Δasr + λα Δlm,tgt；域迁移合并（对应密度比）：再减 λβ Δlm,src。可用 TIES（按幅度剪枝、选符号、只合同号参数）减轻任务干扰。推理仍单次 ASR 前向，无额外模块。

## 实验与结果
CSJ-SPS→CSJ-APS（LLM-jp-3-980M+Conformer）：基线 eval1 CER 13.9；TIESmerge-T 13.3，参数与 RTF 不变（1.1B / 0.45）；浅融合/密度比更低（12.8/12.5）但参数与 RTF 上升。合并可再与 SF/DR/rescoring 组合进一步降 CER。LibriSpeech→SPGISpeech（LLaMA3.2-1B）：基线 WER 11.2→TIESmerge 10.6；SF/DR 约 9.1/9.0。贪心解码下合并仍有效，CSJ 上甚至可优于 DR。

## 结论
跨模态 LoRA 算术合并能稳定提升目标域 ASR，且不增显存与延迟；绝对增益弱于逐步 LM 融合，但可与之叠加，并便于单模型部署。

## 点评
把浅融合/密度比“搬进权重空间”，切中大 LM 融合的成本痛点。跨模态对齐脆弱——加大 λα 易崩 ASR，故增益有限。无目标域配对数据、只需文本时很实用；源域文本缺失则只能做扩展合并。
