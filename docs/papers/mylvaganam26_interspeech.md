# Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification

- 论文编号：1789
- 报告人：Pravina Mylvaganam
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/mylvaganam26_interspeech.pdf

## 问题
澳大利亚原住民语言（AAL）极度缺数据，从高资源语种迁移做语种识别易灾难性遗忘；单独用 EWC / ER / KD 在长程适应与数据极不平衡下仍不稳，混合持续学习在 LID 上几乎空白。

## 方法
基于 VoxLingua107 预训练 ECAPA-TDNN LID，提出两套混合 CL：(1) **RA-EWC**：新语言 NLL + 回放缓冲 NLL + Fisher 加权 EWC，仅微调分类头；(2) **CG-KD**：新语言 NLL + EWC + 对冻结 teacher 在高资源类上的温度软目标 KLD，学生端编码器与分类头均可训。评测 Warlpiri（~3h）、Dalabon（~40min）、Dharawal（~11min）的单语适应与多语顺序适应，对照 TL、EWC、ER、KD。

## 实验与结果
单语适应（F1%）：CG-KD 总体最优——Warlpiri overall 93.38（HRL 92.89）、Dalabon 85.68、Dharawal 76.41，且目标语多为 100%；TL 严重伤 HRL（如 Dharawal 场景 HRL 仅 31.25）。顺序适应中，联合训练对最稀缺的 Dharawal 仅 50%/66.67%，而顺序任务下两方法均可达 100%；CG-KD 最佳 overall 约 89.43（DH⇒WA⇒DA）。

## 结论
混合 CL 优于朴素微调与单一 CL；CG-KD 在极低资源下最稳，并支持按任务顺序增量纳入多种 AAL 而不依赖数据均衡。面向濒危语种多语 LID 的可扩展适应路径。

## 点评
把“回放/蒸馏 + EWC”对准 AAL 极不平衡场景，问题抓得准；顺序适应相对联合训练在 Dharawal 上的反差，说明任务级容量分配比硬混数据更关键。测试集绝对规模很小（尤其 Dharawal），100% F1 需谨慎解读方差；HRL 只报 33 语子集也限制了遗忘评估的广度。
