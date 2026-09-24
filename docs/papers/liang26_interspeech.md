# DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning

- 论文编号：342
- 报告人：Xinyu Liang
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26_interspeech.pdf

## 问题
紧凑端到端 MOS 模型（如 DNSMOS Pro）适合实时，但对未见失真/条件泛化不足；SCOREQ 类对比损失有效但依赖重 SSL，难部署。

## 方法
DNSMOS-C：在 DNSMOS Pro 架构上，对中间嵌入施加 MOS 引导的 triplet 对比回归损失（SCOREQ 风格），与 MOS 回归联合单阶段训练；推理与 Pro 相同、无额外开销。在 BVCC、NISQA、Tencent 等上训练，测域内与未见 NISQA 子集；PCA/聚类分析潜空间。

## 实验与结果
10 次运行平均：域内 LCC/SRCC 一致高于 DNSMOS Pro，MSE 相近；未见域相关也更高或持平，标准差更小（更稳）。潜空间两主成分与 MOS 的多重相关升高，呈现质量流形式排序。

## 结论
MOS 引导对比监督可在不增加推理成本的情况下，提升紧凑 SQA 的相关、泛化与训练稳定性。

## 点评
把 SCOREQ 思想压进小 CNN 端到端模型，填补“重模型泛化 vs 轻模型部署”缝隙。增益主要在相关而非 MSE，适合排序/监控场景；与大 SSL SQA 的绝对差距文中未全面对标。
