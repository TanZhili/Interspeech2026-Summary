# From Masking to Merging: Rethinking SpecAugment for Efficient Audio Spectrogram Transformer

- 论文编号：3273
- 报告人：Chanwoo Kim
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/park26j_interspeech.pdf

## 问题

AST 训练普遍使用 SpecAugment，被 mask 的谱图区域语义信息少，但仍作为 token 进入 Transformer，带来二次注意力开销。已有 token 削减方法常需额外模块或相似度计算，或随机丢弃而不显式利用增强造成的信息空洞。

## 方法

提出 SpecAugment-Patch Merging：先把 SpecAugment 的时/频 mask 对齐到 16×16、stride 10 的 patch 网格（保证 patch 全掩或全保留），得到全零 patch 的二值候选；在 patch 与位置编码之后、Transformer 之前，随机抽取 2r 个掩码 patch 配成 r 对，按维 max 合并为一枚 token 并压缩序列（保留 [CLS]/[Dist]）。r=0 时与原 SpecAugment 效果接近。合并策略在 max/mean/sum/random drop 中选维 max。

## 实验与结果

在 Balanced AudioSet、ESC-50、Speech Commands V2 上，以 ImageNet 预训练 DeiT-Base distilled 初始化，单卡 RTX 4090。AudioSet 上 r 从 0 增至 100：mAP 几乎不变（34.07→34.08），吞吐 43.3→49.3 samples/sec（约 +13.9%），显存 24.64→21.50 GB。ESC-50：Acc 89.20→88.67，吞吐 127.3→142.9；Speech Commands V2：Acc 98.13→98.06，吞吐 411.1→429.4。同等合并率下相对复现的 PaSST-U，AST 侧吞吐更高（如 16.5% 时 49.3 vs 46.7 S/s）。

## 结论

作者认为把增强产生的掩码区当作合并线索，可在几乎不损精度下加快 AST 训练；因只能合并已掩码 patch，最大削减比受掩码强度限制，但思路可推广到其他使用 SpecAugment 的 patch Transformer。

## 点评

核心洞察是“SpecAugment 已经制造了可丢弃的冗余”，用增强结构做 token 削减，比另加 ToMe 式相似度模块更轻。强依赖“掩码 patch 确实无信息”这一假设；若 mask 未对齐 patch 或掩码过少，可合并候选不足，效率上限就卡住。与 PaSST-U 的对比在统一训练设定下成立，绝对 mAP 不宜直接对照原论文数字。
