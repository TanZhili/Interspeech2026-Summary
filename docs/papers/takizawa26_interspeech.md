# Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

- 论文编号：3002
- 报告人：Daigo Takizawa
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/takizawa26_interspeech.pdf

## 问题
基于神经音频编解码器（NAC）离散 token 的 SSL 更省存储与算力，但语言敏感性来自 NAC 还是 SSL 预训练尚不清楚；若每语需重训 NAC 则削弱效率优势。

## 方法
控制实验解耦：RQ1 在 NAC 重建波形上做 ASR/SER；RQ2 固定 NAC、变 SSL 预训练语；RQ3 固定 SSL 与下游语一致、变 NAC 训练语。英/日/中，DAC 等公开 NAC；codec-based HuBERT（冻结 NAC 码本嵌入求和作输入）。用相对波形基线的 CoV 度量跨语变异。

## 实验与结果
RQ1：DAC 最稳，重训语（EN+/JP/ZH/All）对重建下游影响有限（ASR CoV 约 2%）。RQ2：SSL 预训练语与下游对齐显著更好，错配则 ASR/SER 大幅变差（CoV 可达 37–43%）。RQ3：SSL 对齐后更换 NAC 训练语差异小，不必按目标语重训声学 NAC。

## 结论
下游主要敏感于 SSL 预训练语言，而非 NAC 训练语言；可跨语复用单一声学 NAC，但 SSL 预训练语应与目标语对齐。

## 点评
把编解码器与 SSL 阶段拆开做因果式对照，结论对工程选路很清晰。范围限于英日中与声学型 DAC；语义型编解码器、更多语种与任务是否同样不敏感仍待验证。
