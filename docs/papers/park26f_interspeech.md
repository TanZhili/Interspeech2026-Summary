# LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations

- 论文编号：2225
- 报告人：Hoyeon Lee
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26f_interspeech.pdf

## 问题
短语停顿标注存在一对多合法切分；单参考评测会拒掉与金标不同但仍合理的标注，人工评测又难扩展；直接用 LLM 当裁判捕捉细微韵律差异也有限。

## 方法
提出 LMRE：用 LLM 从少量 few-shot 演示池（与评测参考 disjoint）多次采样生成多参考查找表，保留出现次数超过 Niter/10 的标注；假设标注与任一参考相似度（EM 或 F1）超阈值即接受。韩语测试床含 1356 条标注、五种策略（AP-Only、Comma-IP、音频驱动、文本驱动、合成）与十一配置。

## 实验与结果
可接受组（人工分 4–5）上，单参考相对人工欠接受约 13–27%，LMRE Combined 将差距压到约 7%（分 5 组仅 1.75%）。与人工分相关：Combined† 多参考 F1 达 r=0.621、ρ=0.626，高于单参考（约 0.50）。F1 普遍优于 EM；长句上 EM 增益更明显。小演示池（|PFS|=128）即可泛化到未见句。

## 结论
LMRE 在可扩展自动评测与多参考容忍之间取得折中，比单参考更贴近人工接受行为。

## 点评
把“一对多韵律”落到可复用查找表而非黑盒裁判，确定性与可复现性更好。参考质量仍依赖演示池与 LLM 生成分布；目前验证集中在韩语，跨语迁移需另证。
