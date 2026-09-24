# Interpretable Audio Editing Evaluation via Chain-of-Thought Difference-Commonality Reasoning with Multimodal LLMs

- 论文编号：3176
- 报告人：Yuhang Jia
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jia26b_interspeech.pdf

## 问题
音频编辑需同时衡量“改到了什么”与“保留了什么”；既有自动 MOS/目标指标或缺可解释性，或缺对成对编辑的结构化推理。

## 方法
基于 Qwen2-Audio，用混合/重排构造约 3 万伪成对样本，LoRA 微调 Difference / Commonality 双 caption 任务；再设计 Chain-of-Thought 提示做逐步差同推理，导出 Edit score 与 Faith score。在 AuditScore 上与专家分及 AuditEval-ssl 等相关对比，并用 Qwen2.5-Omni 做 A/B 投票消融。

## 实验与结果
SFT 后 Difference/Commonality caption 从近零跃升（FENSE 约 0.83 / 0.69）。Difference 质量与编辑有效性指标正相关、与保真负相关；Commonality 相反，形成互补模式。Edit score 在编辑有效性上 LCC/SRCC 超 AuditEval-ssl（如 Edit LCC 0.765 vs 0.620）；Faith score 对保真更弱。A/B 显示优化 CoT 流程优于原始提示。

## 结论
差同叙述 + CoT 可给出可解释、与人类更对齐的音频编辑自动评测；代码将开源。

## 点评
把 LLM-as-Judge 落到“改/留”双轴，比单分数 MOS 更贴编辑任务。伪配对与另一 MLLM 当裁判可能引入同族偏差；Faith score 仍明显弱于专用保真模型。
