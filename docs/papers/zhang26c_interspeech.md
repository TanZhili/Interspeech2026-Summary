# AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning

- 论文编号：288
- 报告人：Haoyu Zhang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26c_interspeech.pdf

## 问题
LALM 部署后静态，难适应真实测试分布；有监督更新需标注。需在无标签测试数据上自进化做 Audio Question Answering。

## 方法
AQA-TTRL：对测试题多数投票（如 64 次）得伪标签，再以 GRPO 做测试时强化学习。置信度加权优势缓解伪标签噪声；multiple-attempt sampling 抑制 advantage collapse。全参微调（AdamW），小数据集约 100 步、大数据集约 500 步。对比 DI、DIMV、同伪标签 SFT。

## 实验与结果
MMAU / MMAR / MMSU：Qwen2.5-Omni 7B 平均 +4.42%（64.39→68.81），3B +11.04%（53.82→64.86）；适配后 3B 平均超过未适配 7B 的 DI。优于 DIMV 与伪标签 SFT。消融显示置信度加权与多次尝试互补。按音频类型适配时 music-only 平均最高。

## 结论
无标签测试时 RL 自适应可使 LALM 在 AQA 上显著自提升，小模型经适应可逼近更大模型直推。

## 点评
把数学域 TTRL 迁到音频，用多数票伪奖励 + 抗噪机制形成闭环。RL 比同标签 SFT 更能“忍错标签”。成本是测试时大量前向与更新；伪标签系统性偏差仍可能固化。
