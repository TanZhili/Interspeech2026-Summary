# A Closer Look at Failure Modes in Temporal Understanding of Large Audio-Language Models

- 论文编号：3070
- 报告人：Apoorva Kulkarni
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kulkarni26_interspeech.pdf

## 问题
LALM 在时序推理上仍弱，既有基准多报差距却少做机制分析。不清楚失败是单纯“音频注意力不够”，还是音频 token 内部注意力分配不当。

## 方法
基于 TACOS 建 1,657 题三任务基准：Earliest Onset、Latest Offset、Longest Duration（多选，事件间隔/时长差 ≥1s）。行为分析比较 Audio-only / Caption-only / Audio+Caption。因果干预对比：注意力上调（增大音频总注意力）vs ScalingVis 式缩放（重分配音频 token 注意力），从 last / keyword / 两者触发。对开源可复现的 Audio-Flamingo-3、DeSTA2.5 做层定向推理时干预。

## 实验与结果
静音消融近随机，确认需听音频。多数模型 Caption-only 优于 Audio-only，ACQA 增益有限，层注意力偏文本。缩放修复率高于上调（如 AF3 平均约 20.5% vs 15.8%）；Kwd+Last 最好。全层缩放伤性能；单层定向缩放使跨模型任务平均准确率从 55.9% 到 59.1%（无微调）。AF3 偏锐化（α=2），DeSTA 偏平滑（α=0.2）。

## 结论
模态失衡不足以解释时序失败；如何在音频 token 上分配注意力更关键。层定向注意力再分配是有希望的免训练方向。

## 点评
用可控任务 + 因果注意力干预，把“听不够”推进到“听法不对”，对纠偏训练有启发。局限：任务较窄、仅两模型深入、fix rate 只看原本错误样本；作者也承认不能排除弱音频编码器等其他机制。
