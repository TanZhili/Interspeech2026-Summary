# Scalable Keyword Spotting via Modular Network Expansion

- 论文编号：987
- 报告人：Viktor Khaymonenko
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/khaymonenko26_interspeech.pdf

## 问题
嵌入式固定词表 KWS 部署后常需加新关键词，但原训练数据不可用，全量微调会灾难性遗忘且破坏已上线阈值与行为。

## 方法
参数封顶的模块化扩展：冻结整条基座（含 BN 统计）与核心分类头；挂接 ≤10k 参数的 Expanded Blocks（拼接冻结层激活 + Conv1D/BN/hard-swish）与独立 New Head。推理用 core-first：先按原阈值判核心词，仅拒绝时再看新头。保证核心 logits/决策规则对任意输入与出厂模型完全一致。基座约 150k 的 SVDF 风格网络。

## 实验与结果
GSC v2 五组 held-out 词对扩展，FAR 在 Common Voice 上标定 1%。新词宏平均 FRR：提出方法 4.37%，优于 Ensemble 6.46%、LoRA 6.41%、Adapters 8.05%；全微调新词好但核心 FRR 从 2.71% 飙到 69.08%。同预算下 MACs 16.34M，低于 Adapters/LoRA。消融显示扩展深度约 4 块最优。

## 结论
作者认为在无原数据与严格不回退约束下，模块化扩展可有效加入新关键词并保持出厂核心检测器不变。

## 点评
把“不回归”做成构造性保证（冻住路径），比 EWC/适配器的软约束更贴合产品安全。代价是新词依赖轻量旁路容量；扩展深度过深时基座最深层对核心词过专、迁移变差。
