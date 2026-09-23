# MATA: A Training-Free Approach to Mitigate Cross-Modal Attention Imbalance in Large Audio Language Models

- 论文编号：1212
- 报告人：Junyu Wang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/wang26t_interspeech.pdf

## 问题
LALM 在自注意力中系统偏向文本 token、低估音频 token（尤其中层融合层），导致声学线索利用不足、推理与幻觉变差；视觉域已有类似研究，音频—文本注意力失衡尚缺系统干预。

## 方法
训练无关的 MATA（More Attention To Audio）：在 softmax 前、仅对序列最后一 token 的 query，把音频 key 区间的原始注意力分乘以 (1+α)。默认 α=0.1，干预解码器约第 10–20 层；无新增参数、开销可忽略。可挂到 Qwen2-Audio、Qwen2.5-Omni、Ke-Omni-R、Qwen3-Omni-Thinking 等。

## 实验与结果
MMAU Test-mini：Qwen2-Audio 59.4→64.8；Qwen2.5-Omni 71.1→73.6。MMAR：Qwen2.5-Omni 56.6→61.2；Ke-Omni-R 64.1→66.8。挑战 Single Model：Thinking + MATA 达 Acc 71.0 / Rubrics 62.6（相对基线 68.6 / 58.7），赛道第 2，且为前列中唯一训练无关方案。消融显示中等 α 与中层干预最佳。

## 结论
在中层直接抬高末 token 对音频的注意力，可无训练提升答案正确率与 CoT 过程质量，是高效缓解跨模态注意力失衡的手段。

## 点评
诊断（中层音频注意力偏低）与干预点（softmax 前、末 token、音频 span）对齐干净，工程上极轻。α 过大可能破坏模态平衡；对已很强的模型增益收窄，且不改变权重本身，复杂场景仍可能需数据或 RL 补齐。
