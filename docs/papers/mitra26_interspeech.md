# Adaptive Turn-Taking for Real-time Multi-Party Voice Agents

- 论文编号：2493
- 报告人：Soumyajit Mitra
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/mitra26_interspeech.pdf

## 问题
多人语音对话中轮次竞争、重叠与动态 floor 分配使二元静音/句末启发式失效；用户对代理期望从被动听者到主动主持各异，但角色对实时 turn-taking 的影响少被建模。

## 方法
提出 **ModeratorLM**：语音编码器 + LLM，块式流式追加声学嵌入与带说话人标注转写；每块输出「抢轮+回复」控制 token 或空序列（不抢）。**ModeratorLM-Think** 在决策前加 chain-of-thought。构建合成口语多人语料 **RolePlayConv**（约 75k 对话、125 种助手角色，Nova Pro 生成文本 + Zonos TTS）。三阶段训练：ASR 对齐投影 → AMI/Fisher 对话预训练（轮换助手）→ RolePlayConv 角色条件微调（LoRA）。

## 实验与结果
真实会议 NOTSOFAR-1 与 RolePlayConv 零样本角色测试。相对 Moshi、无角色 MP-Baseline：ModeratorLM-Think 在 NSF-1 上 P/R/F1 达 0.81/0.74/0.76，FP 仅 0.01；RolePlayConv F1 0.79。文称相对非角色基线 precision 提升超 40%、recall 超 70%，并大幅降误打断。LLM-as-judge 角色保真更高。消融：无转写性能崩；ASR 假设仅轻微下降；Think 变体对切块策略更稳健，但固定切块评估有伪增益风险。

## 结论
显式角色条件可显著改善多人语音代理的 turn-taking 与回复一致性；推理轨迹进一步抬升召回并降低反应性漏接。

## 点评
把「何时开口」绑到角色义务，切中多人代理与二元对话代理的差异。强在真实会议+合成角色双评与 Think 消融；脆弱点在大量合成数据、评测依赖 teacher-force 与动态切块，以及 NSF-1 助手角色由 LLM/人工事后指定，与真实助手行为仍有差距。
