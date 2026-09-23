# Aligning MusicLLM with Emotion using Instruction Tuning and Feedback-Driven Alignment

- 论文编号：2293
- 报告人：Takuya Hasumi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hasumi26_interspeech.pdf

## 问题
MusicLLM 在 MIR 上强，但情绪回归（arousal/valence）常不优于数据集均值；缺少把连续分数当显式目标的训练。

## 方法
冻结音乐编码器 + 可训投影与 LLM 解码器。先指令微调：GPT-4o 模板生成伪 QA，下一词似然学分数格式。再反馈对齐：GRPO，奖励为解析失败 −200、否则 −(预测−真值)²。数据 DEAM、MERGE；并测与 MusicQA 联合训练是否伤开放问答。

## 实验与结果
仅 IT：回归有限；IT+FDA（无 MusicQA）DEAM R² arousal/valence 达 0.56/0.55，MERGE 0.55/0.29。含 MusicQA 时 IT+FDA：DEAM 0.48/0.35、MERGE 0.50/0.24，同时 BLEU/METEOR/ROUGE 基本保持。开源 Qwen2-Audio/Phi-4-Multimodal 零样本 R² 为负。

## 结论
指令微调可赋予粗回归能力，可验证数值奖励的反馈对齐显著 refinement（尤其 valence），且可与 MusicQA 共存。边界是仍难全面超过专用编码器/探测基线。

## 点评
把 LLM 回归从“会说话”推进到“平方误差可优化”，GRPO 避开评论家网络很务实。强处是保持开放问答；脆弱处是模板填分格式依赖、MERGE 半自动标签噪声，以及相对 MusicFM probing 的绝对差距。
