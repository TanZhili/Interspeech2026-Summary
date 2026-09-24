# Revisiting Active Speaker Detection: An In-the-Wild Benchmark for Generalization and Robustness

- 论文编号：581
- 报告人：Tuan Khai Nguyen
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26b_interspeech.pdf

## 问题
ASD 基准 AVA 几乎全来自老电影，SOTA 近饱和（mAP>95%）易让人误以为任务已解决；真实场景含少见语言、噪声、拥挤与复杂镜头，泛化不清。

## 方法
提出 UniTalk：规模可比 AVA、覆盖多样野生视频与难度子类（语言/噪声/视觉复杂度）。评测现有 SOTA 在 AVA vs UniTalk，以及 UniTalk 训练后向 AVA、Talkies、ASW 的跨域泛化与少样本适应。

## 实验与结果
AVA 近完美模型在 UniTalk 最强仅约 83.2 mAP，Hard 子集约 77.9。UniTalk 训练模型跨域更好：AVA/Talkies/ASW 约 88.0/91.4/90.4 mAP。预训练后快速适应可达约 92.4 mAP，接近全数据。

## 结论
ASD 在真实条件下仍未饱和；UniTalk 提供更现实的稳健性与泛化基准。

## 点评
用“电影饱和 ≠ 野生解决”直接打醒领域，Hard 子集设计有诊断价值。跨域数字显示数据域比架构口号更决定表现。标注噪声与类别定义细节会影响绝对 mAP；与 AVA 协议对齐仍是公平对比关键。
