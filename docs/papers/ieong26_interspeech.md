# Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models

- 论文编号：554
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ieong26_interspeech.pdf

## 问题
LALM 上 CoT 能引出推理，但再加强常需额外监督或强化学习；能否在推理时无训练地操纵隐状态以提升口语 CoT？

## 方法
从最后 k 层、提示末 token 取隐状态差作为 steering 向量并注入解码全程（α 缩放 + 范数保持）。三种抽取：Vanilla（每样本 CoT 提示 vs 普通提示）；SGS（外部口语集差均值，复用）；TGS（纯文本集差均值，跨模态迁到语音）。外部数据 BeyondAIME（SGS 用 IndexTTS2 口语化）；超参在 spoken GSM8K 上搜。

## 实验与结果
模型：Voxtral-mini-3B、Phi4-mm、Qwen2.5-Omni-7B、Audio Flamingo 3；评测 VoxEval 数学三级 + SpeechR ReveAL-CoT。相对 CoT，多数设定提升，最高 ALL Δ 约 +4.4%（AF3+TGS）、Voxtral+Vanilla +4.3%。TGS 跨模型平均增益最大（约 +2.5%）。同预算下 Vanilla 常优于 self-consistency（三路生成）。Vanilla 对 α 敏感，SGS/TGS 更稳；TGS 少量文本样本即可接近峰值。

## 结论
无训练隐状态引导可普遍加强 LALM 的 CoT；共享向量尤其是文本导出的 TGS 数据高效且可跨模态迁移。

## 点评
把 LLM steering 落到口语推理，并验证文本差向量可迁到语音，实用价值高。增益因模型而异（Qwen 上 Vanilla 几乎无增益）；依赖开发集调 k、α，自动选参仍开放。
