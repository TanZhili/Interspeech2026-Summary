# FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing

- 论文编号：1121
- 报告人：Yuxuan Jiang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/jiang26d_interspeech.pdf

## 问题
文本条件音频编辑需同时满足时间一致性（只改目标段）与背景保持（重叠声源下非编辑区不变）。现有反演/全局条件方法改一处常牵动整段；训练式方法依赖复杂三元组与专用结构，成本高、灵活性差。

## 方法
基于 TangoFlux（Rectified Flow + MM-DiT）的免训练框架 FreeSonic。(1) 优化 RF 反演–重建，为后续编辑提供稳定结构。(2) 反演前 5 步聚合 double blocks 的 text–audio attention，阈值+膨胀平滑得时间掩码 M，定位待编辑段。(3) 在 single blocks 做三阶段 Scheduled Attention Decoupling：早期按 δ（0.85→1.0）混合源/目标 KV，并用 M 在非编辑区强制注入源 KV；中期 δ=1 且保持掩码；后期去掉约束做全局协调。(4) Task-Oriented Noise Injection：仅在 M 内对潜变量加可调度噪声，便于删除与非刚性替换。推理用 RF-Solver、25 步；噪声强度按 Add/Remove/Replace 分别为 0.1/0.4/0.25，截止步 t1=5。

## 实验与结果
基准：AudioCaps / AudioSet Strong 等构建的 Add(1300)、Remove(1300)、Replace(750)。对比 SDEdit、AudioEditor、ZETA、训练式 SAO-Instruct。FreeSonic 多数客观指标领先（如 Add FAD 1.55、Remove FAD 1.95、Replace CLAP 0.424）；主观 Quality/Relevance/Faithfulness 整体强。消融去掉掩码、改全量 KV 替换或去掉噪声注入均变差。固定 NFE=150 时 RTF 约 0.854，优于多数训练无关基线。

## 结论
免训练下用 RF 反演 + 注意力时间定位 + 调度解耦 + 任务噪声，在保背景与局部编辑间取得更好平衡，并在多种编辑任务上达到高保真与较高效率。

## 点评
抓住音频“可加性/重叠”导致全局反演难局部改的本质，把 MM-DiT 的跨模态注意力当作时间定位器，再用掩码约束 KV，比纯改文本条件更可控。相对训练式编辑省数据与微调。风险在于掩码依赖早期注意力质量与阈值、强依赖 TangoFlux 骨干，复杂重叠或弱对齐文本时定位可能漂移。
