# Search-GRT: Guided Retrieval Training of Search Agents to Optimize for Complex Question Answering

- 论文编号：2006
- 报告人：Aounon Kumar
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26d_interspeech.pdf

## 问题
搜索智能体做多跳 QA 时早期差查询导致检索失败、奖励稀疏，错误级联。Search-R1 等纯结果 RL 在 MHQA 上仍弱。

## 方法
**Guided Retrieval Training (GRT)**：RL（PPO）训练时用 ground-truth 信息把检索语料限制到与 GT 最相似的文档子集（E5 嵌入 top-\(\kappa=300\)）；HotpotQA 用给定段落，NQ 用 query+answer 拼接。推理时仍用完整 Wikipedia 搜索。奖励为答案精确匹配。底座 Qwen2.5-3B。

## 实验与结果
相对 Search-R1 等基线，All QA 平均 EM 0.375 vs 0.318；MHQA 平均 0.297 vs 0.206（文称超 40% 提升）。检索准确率与“检索正确条件下的答题准确率”均更高；训练奖励更强、可用更少步达到更好表现。

## 结论
训练期用 GT 引导检索可缓解稀疏奖励，提升子查询与综合答题，且推理可接真实搜索引擎。

## 点评
本质是把“课程式检索约束”写入 RL 环，专治多跳早期失败。注意：本文是文本搜索智能体，与音频模态无直接关系（虽排在 audio-llm 会场）。局限：训练依赖 GT 相关文档、\(\kappa\) 固定、EM 字符串匹配偏严。
