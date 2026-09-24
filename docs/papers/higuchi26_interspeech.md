# Incremental End-to-End Spoken Dialogue State Tracking with a Multimodal LLM and Reinforcement Learning

- 论文编号：592
- 报告人：Tomoya Higuchi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/higuchi26_interspeech.pdf

## 问题
口语 DST 的 ASR→文本 DST 级联易传播错误；端到端多模态 LLM 可直接从音频推断状态，但现有口语 DST 仍常每轮重生完整信念状态，输出冗长且易污染未变槽。增量更新在文本 DST 已复兴，却尚未系统用于端到端口语 DST。

## 方法
基于 Qwen2.5-Omni-7B + QLoRA：输入对话历史、上一信念状态与当前音频，输出转写与符号编辑（set/update/delete），确定性应用到 \(B_{t-1}\)。两阶段训练：SFT 学格式与对齐；再 GRPO，组内相对优化奖励 \(r=\alpha r_{\mathrm{WER}}+\beta r_{\mathrm{diff\text{-}F1}}+\gamma r_{\mathrm{exact}}+\delta r_{\mathrm{format}}\)（权重 0.3/0.5/0.1/0.1）。对比级联 SPACE+WavLM、Gemma-2-9B 全状态、同骨干全状态 SFT。

## 实验与结果
SpokenWOZ predicted mode：增量 SFT JGA 48.52（全状态同骨干 45.36，+3.16）；+GRPO 达 49.20，SER 18.03；WER 21.61（全状态 23.01）。Oracle 下增量 JGA 约 88–90，predicted 掉约 40 点，显示误差传播是主瓶颈。去掉 WER 奖励后 JGA 与 WER 双降。中后期轮次增量仍优于全状态。

## 结论
增量编辑 + GRPO 在 SpokenWOZ 达到正文报告的最佳结果；训练用金标上一状态，部署时自预测状态易级联出错。局限：单模型单数据集、GRPO 采样成本高。

## 点评
把文本 DST 的差分更新搬到语音端到端，并用 GRPO 同时拉转写与编辑质量，针对增量路径的“错一次、错全程”很对症。Oracle/predicted 鸿沟说明下一步应做带噪声历史的训练或恢复机制，否则增益难完全落到真实对话。
