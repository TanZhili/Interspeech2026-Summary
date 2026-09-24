# Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?

- 论文编号：2436
- 报告人：Wangjin Zhou
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26i_interspeech.pdf

## 问题
下游分类上常把单一预训练 checkpoint 下的小幅 SFT 增益解读为“方法更好、天花板更高”，却默认 SFT 相对优劣在同类预训练实例间稳定。实际上骨干、预训练数据与配方交互强烈，单 checkpoint 结论可能缺乏外部效度。

## 方法
把 SFT 视为 capacity elicitation：配方差异主要反映对特定 checkpoint 的 elicitation match（激活可靠性），而非普遍抬高上限。在 FEATURE MODE（末层 / 倒数第 4 层 / 层加权和）与 FREEZE MODE（全微调 / 冻 CNN / 冻 CNN+前 N=4 层）上构造 8 种配置，作用于 wav2vec 2.0、HuBERT、WavLM 共 9 个 checkpoint；在 SUPERB 的 IC、ER、SID 上评测。用 McNemar 检验定义相对最优的 top-group；全矩阵默认 seed 1337，并对三个 base 模型额外用 seed 2048/7395。

## 实验与结果
表 2/3 显示 top-group 配方随 checkpoint 变化，同架构同规模但预训练数据不同时排序可翻转；部分“常进 top-group”的配方在个别 checkpoint 上严重 under-activation（异常低分仍完成训练）。多 seed 下同一配置可在 fully activated 与 under-activated 间双向切换。hubert-large 在 ER 上八种配方统计不可分，说明有时配方边际效应很小。约一万 GPU 小时（H20）。

## 结论
统计上“最优/同组最优”的 SFT 配方依赖预训练实例与 seed；表观增益常是激活匹配，而非普适更高天花板。应跨多 checkpoint 与多种子评估。

## 点评
把“方法进步”与“碰巧激活某 checkpoint”拆开，用 top-group 不稳定性与 seed 双向翻转直接打穿单点对比的外部效度，对 SUPERB 式对比实验很有警示意义。局限是配置空间仍沿特征层/冻结轴离散采样，未覆盖学习率等更广超参；结论偏方法论，不给出新 SOTA 配方。
