# VISA: A Visual Information Strengthened Audio-Reasoning System for the Interspeech 2026 ARC Agent Track

- 论文编号：2381
- 报告人：Wenming Tu
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tu26b_interspeech.pdf

## 问题
音频推理需在混源、时变信号上做多步、证据可核验的推断；仅靠单次 LALM 回答易不稳，纯转写式 agent 又易传播识别错误。如何在“LALM as a Tool”范式下注入辅助多模态证据、稳定预测并产出符合 MMAR Rubrics 的推理链。

## 方法
VISA 三模块：(1) 多模态特征抽取——librosa 低层声学描述 + Qwen3-Omni-Captioner 高层描述；Agentic SED（候选事件→FlexSED→VLM 校验热图时间戳）；VLM 解读 Mel/CQT/RMS 等可视化谱图；(2) 模型投票——Qwen3-Omni-Thinking 与 Step-Audio-R1 各随机采样 K=3，多数表决，全不一致则贪心回退；(3) 27 类细粒度路由：LLM 评判选 CoT、VLM 谱推理接管计数/节奏等、或直送更强专家模型。LLM 骨干为 GLM-4.6，VLM 为 Qwen3-VL。

## 实验与结果
MMAR 平均准确率 77.4%，多项模态领先常见 agent / 开源推理模型。去掉细粒度路由后 Acc 降至 73.30、Rubrics 62.63。官方 Agent Track：Rubrics 66.23%（第 2），Acc 77.40%（两赛道总最高之一）。

## 结论
声学—视觉线索 + 一致性投票 + 细粒度路由可同时抬高正确率与 rubric 对齐的推理质量；未来可深化视觉线索机制与自适应协同。

## 点评
核心不是再堆工具，而是把“模型何时听不清、何时该看谱图”做成可路由的专家分工，尤其对计数/时长等数值题用 VLM 读谱，针对性强。系统重度依赖大模型合奏与手工 27 类启发式，可维护性与跨基准迁移成本是主要风险。
