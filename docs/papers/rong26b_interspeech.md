# Beyond Symmetric Interaction: Capability-Aware Asymmetric Multi-Agent Collaboration for Audio Deep Reasoning

- 论文编号：2273
- 报告人：Chenxing Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/rong26b_interspeech.pdf

## 问题
音频深度推理需要专家级感知与多步推理。朴素多智能体对称投票/辩论难以利用不同 LALM 的互补能力，忽略角色与能力偏差（弱者拖累强者的“木桶效应”、强模型的“文本补偿”导致协同幻觉），且忽略单智能体采样不稳定性。

## 方法
AsymAudio 三阶段：(1) Intra-Agent Consistency Refinement——决策智能体对同一题重采样，不一致则由 LLM 生成客观内部引导并自校正；(2) Inter-Agent Collaborative Interaction——角色分层：强/中为决策智能体，弱为仅供证据、可挂工具的辅助智能体；反馈非对称：强者收隐式客观声学引导（不暴露对方答案），较弱者收显式同伴上下文；(3) 共识则输出，否则最多 T_max=3 轮，达上限取更强决策智能体答案，再汇总与终答一致的推理路径。实现：Qwen3-Omni Instruct/Thinking 为决策，Captioner+大 LLM 为证据，Whisper-large 作工具。

## 实验与结果
MMAR 平均 74.80（多模态多项领先，如 So-Mu 100%）；MMAU-mini 平均 79.10。消融：对称角色+对称交互 69.80 → 非对称角色 71.60 → 角色+非对称交互 72.30（两轮、无 intra 模块设定）。重采样显示弱模型更不稳定；在答案曾变的子集上，intra 精炼优于首跑与多数投票。交互轮数在 3 轮附近最优，再增略降。挑战 Agent Track 排名第 3。

## 结论
能力感知的非对称协作 + 智能体内一致性精炼，能更好利用异质 LALM 并抑制木桶效应与协同幻觉，在音频深度推理基准上显著优于单模型与常规多智能体范式。

## 点评
核心洞见是“不要让弱智能体和强智能体平权投票”，并用隐式/显式反馈分别防文本补偿与借力校准，问题诊断与机制设计对齐得好。系统重度依赖超大 Qwen3-Omni 家族，成本与可复现门槛高；终局仍偏向最强智能体，需分清增益来自协作协议还是底座规模。
