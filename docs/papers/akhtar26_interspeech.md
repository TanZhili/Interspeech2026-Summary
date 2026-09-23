# From Signals to Patterns: Non-Invasive Tuberculosis Detection from Cough Audio using Bandit Weighted Hyperbolic Prototypes

- 论文编号：2704
- 报告人：Muskaan Singh
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/akhtar26_interspeech.pdf

## 问题
咳嗽音频结核筛查中，频谱描述子与预训练基础表示各有优劣，但简单拼接难利用互补性，且易受设备/环境伪迹影响。

## 方法
提出 COBALT：双流（如 MFCC 与 PaSST 等）经轻量适配与 tokenization，映射到共享 Poincaré 双曲原型码本；用 bandit 式可靠性权重融合原型，再接 MLP 分类。对比单流、拼接、欧氏变体与 Möbius 加法融合。

## 实验与结果
CODA TB DREAM Challenge 受试者无关五折。单流以 PaSST+CNN 最强（ACC≈79.3%）。完整 COBALT 在 MF+PST 达 ACC 88.93、F1 87.26、AUC 89.07，优于拼接与仅 Möbius 组成；COBALT-E 亦稳定优于拼接，说明结构化融合本身有益。

## 结论
双曲原型对齐 + 样本相关可靠性加权能有效融合频谱细节与基础模型时序模式，在基准上刷新报告指标。

## 点评
融合设计针对“异构表示不对齐 + 伪迹不稳定”很贴切。临床外推仍受挑战赛协议与多国设备异质性制约；可解释性主要停留在消融，未深入验证模型是否真正依赖病理声学而非通道伪迹。
