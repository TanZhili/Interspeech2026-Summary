# PolyBench: A Benchmark for Compositional Reasoning in Polyphonic Audio

- 论文编号：2466
- 报告人：Yang Xiao
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26aa_interspeech.pdf

## 问题
现有 LALM 评测多关注指令跟随或时序推理，对多声源重叠（复调）场景下的组合关系覆盖不足；重叠导致事件混淆与幻觉，而顺序/时长类基准很少显式测并发组合推理。

## 方法
构建 PolyBench：从 DataSED、DESED、MAESTRO-Real 抽取真实重叠片段（约 169+259+300 条，长音频裁到约 25s），用事件类与时间戳生成五类 MCQA——Counting、Duration、Concurrency、Classification、Detection；问题模板经 Qwen3-Max 改写并由人工质检。Concurrency 额外混入 AudioTime 单声源以平衡正负例。评测开源 LALM（Qwen3-Omni-30B-A3B、R1-AQA、Audio Flamingo 3、TimeAudio+Qwen3-8B、AUDSEMTHINKER-QA GRPO），用 ACC/F1，并以 NV-Embed-v2 做语义匹配；推理模型要求 CoT。

## 实验与结果
难度分层明显：Counting/Detection 最难（Qwen3-Omni 分别约 57.5% / 63.4% ACC；多数模型 Detection 仅约 37%）。Concurrency/Classification 相对更好（Qwen3-Omni 约 83.1% / 77.9%）。TimeAudio 级联在 Detection 上第二（约 51.7%）。Concurrency 在纯复调上可能虚高，混入单声源后正确率大幅下降，暴露捷径学习。

## 结论
作者认为复调组合推理是当前 LALM 瓶颈：感知不稳会在计数与区间定位上放大；需加强底层事件/时序建模与跨模态约束决策。基准已公开。

## 点评
工作把“重叠声学场景”拆成感知→关系→结构决策的五级 MCQA，能暴露纯时序基准看不到的失败。强项是真实数据与捷径诊断；脆弱点在于 MCQA 与选项设计可能低估开放生成难度，且部分指标（如 F1/ACC 差）对模型偏差敏感。
