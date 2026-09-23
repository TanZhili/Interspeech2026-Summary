# Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR

- 论文编号：877
- 报告人：Abeer Alwan
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26c_interspeech.pdf

## 问题
Speech-LLM 在成人 ASR 上强，但儿童语音差异大、年龄与环境异构；单模型难平衡，且适配儿童常损害成人性能。公开儿童语料上尚缺强 Speech-LLM 结果。

## 方法
基于 Canary-Qwen 的 MoE Speech-LLM：Mixture-of-Projectors (MoP) + Mixture-of-LoRAs (MoL) 为各域专用专家；Classifier-based Domain Router (C-DR) 做粗到细路由（数据集级粗域 + OGI-S 年龄细域）；Entropy-Aware Routing (EAR) 按归一化路由熵插值共享专家。五域：OGI-S 三年龄组、MyST、Libri-Clean。训练时专家用真值硬路由，C-DR 与 MoE 分开训；推理支持硬/软路由。

## 实验与结果
单数据集微调可达新 SOTA（OGI-S Avg WER 10.93 / MyST 8.34）。C-DR MoE（软路由 + EAR）OGI-S Avg 11.08、MyST 8.58、Libri-Clean 1.61，优于 single-expert 与 vanilla-routing MoE，且不伤成人。消融：MoP+MoL 同时最好；仅 MoP 优于仅 MoL。粗到细加权层分类器路由最准。

## 结论
显式域路由 + 双层 MoE + 熵感知共享专家，可在统一 Speech-LLM 中同时服务成人与多域儿童 ASR。据作者称，这是首个在公开儿童语料上给出强结果并联合分析成人/儿童/年龄的 Speech-LLM 框架。

## 点评
把“儿童≠单一域”做成层次路由，并用熵处理年龄边界模糊，比可训练 gate 更可解释。EAR 能超过真值年龄路由，说明声学发展阶段未必对齐生日年龄。参数开销约 +5% 可接受；共享专家单独并不强却能补不确定样本，是实用设计取舍。
