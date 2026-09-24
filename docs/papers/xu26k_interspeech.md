# From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

- 论文编号：1160
- 报告人：Yuhao Wang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26k_interspeech.pdf

## 问题
现有语音智能体评测偏反应式问答，缺少对主动介入、条件触发与环境监测的系统基准。

## 方法
提出 ProVoice-Bench（1182 样本）：PIC 隐式意图并工具调用；LTM 潜伏话题监控；CFC 口头与数字上下文矛盾时纠错；ESS 用户定义环境声触发。多阶段 LLM+TTS+声学仿真合成，含数字应用状态。用 Rec/FPR/Acc 与 Response Accuracy 评开源 MLLM。

## 实验与结果
模型普遍过触发（尤其 LTM）；CoT/thinking 在 CFC/LTM/PIC 上明显提升。例：Qwen3-Omni(T) 总体 Acc 0.787、R_acc 0.759；Step-Audio-R1(T) Acc 0.793、R_acc 0.734。去掉数字上下文会显著伤害 CFC 召回与 PIC 准确率。决策是否说话与执行什么任务之间仍有落差。

## 结论
ProVoice-Bench 暴露当前 MLLM 在主动语音交互上的过触发与推理短板，并为数字上下文+音频的主动范式提供评测路线图。

## 点评
把“该不该插话、何时插话”拆成四类可测任务，填补反应式基准空白。合成数据与 TTS 场景可能低估真实噪声与多说话人复杂性；过触发现象本身说明校准比单纯放大模型更急迫。
