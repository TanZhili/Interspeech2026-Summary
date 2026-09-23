# Multi-Source Evidence Fusion for Audio Question Answering

- 论文编号：3297
- 报告人：Aivo Olev
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/olev26_interspeech.pdf

## 问题
Agent 赛道要求推理链事实性、逻辑与完整性，而 LALM 易幻觉、声学工具窄而可靠、ASR 居中；等权集成或把工具当神谕无法处理异质可靠性，且下游推理易锚定于 LALM 的错误最终答案。

## 方法
TalTech 多源流水线：Step-Audio-R1 与 Qwen3-Omni 各对全音频+三段切分只报观察不选题；统一分析做印证/分歧标注。25 工具分四档可靠性（Analytic/Probabilistic/Heuristic/LALM）并设置信度上限与权重；印证、直接作答、域适配性再调分。分歧则多轮取证 + 三阶段矛盾检测 + 定向时段复核。最终分两步 LLM：先选答案、再按七段模板写推理（隐藏源模型答案以防锚定）。推理骨干为 Kimi-K2-Thinking。

## 实验与结果
Agent Track 第 1：Rubrics 69.83，Acc 76.9%。双源相对单源回放消融显著降分（约 −3.2～−4.3 pp）。一致/印证/置信度与准确率正相关；工具推翻双 LALM 预测约 8.5%。音乐理论、时序、音频差分等子类最难；节奏类工具无关率很高。端到端约 8–10 分钟/样本。

## 结论
分层可靠性 + 双源融合 + 矛盾驱动验证可产出稠密可核验推理链，在过程质量上大幅领先，准确率仍具竞争力；架构原则或可推广到其他异质证据推理。

## 点评
与“堆工具”路线不同，本文把可靠性建模与隐藏最终答案当作一等公民，直接对齐 Rubrics 对可检事实句的偏好。代价是极高时延与大量手工阈值；权重非从 MMAR 学得，跨任务迁移需重新标定。
