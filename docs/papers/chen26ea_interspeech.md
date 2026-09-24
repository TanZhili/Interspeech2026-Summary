# SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding

- 论文编号：3369
- 报告人：Po-Yen Chen
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26ea_interspeech.pdf

## 问题
Prompt-based 多意图 SLU 因解码随机性，多路径预测的 intent–slot 语义帧常冲突；输出级多数投票难以细粒度剔除虚假意图与噪声槽位。

## 方法
SFL-MTSC：对同一 utterance 采样 K 条路径，聚合成帧池 \(F=(d,i,s)\)。先按 (domain,intent) 分桶，桶内用 Hybrid Jaccard（key-value 与 value Jaccard 插值，\(\alpha=0.3\)）建阈值图做槽聚类；以跨路径 support 过滤（\(\mathrm{supp}\ge\lceil K/2\rceil\)），再 Value-First 重积成最终多意图预测。零样本后处理，无需微调。

## 实验与结果
MAC-SLU（中文车载多意图）。配置：Qwen3-4B 文本、Whisper+Qwen3 管线、Qwen2.5-Omni-7B。K=5，温度 {0,0.3,0.5,0.7,1.0}。Vanilla Prompting 上 Overall Acc. 分别 +1.23/+0.4/+1.45，Slot F1 最大 +28.86；Intent Acc. 常略降。消融显示槽级 support 过滤是主增益源；\(\alpha\) 在 [0,0.7] 对 Overall Acc. 较稳。

## 结论
帧级自洽聚合可稳定提升 Overall Acc. 与 Slot F1；局限包括 Intent Acc. 偶降、LALM 高方差时增益有限、仅单数据集评估。

## 点评
把 self-consistency 做到语义帧与槽簇，比整句投票更贴合多意图结构。Hybrid Jaccard 针对槽键命名漂移合理；Overall Acc. 绝对值仍很低，说明零样本多意图本身很难，该方法更像稳健后处理而非端到端突破。
