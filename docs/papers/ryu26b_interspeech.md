# Segment-level Tree Search for Long Meeting Document Summarization

- 论文编号：3011
- 报告人：Sangwon Ryu
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/ryu26b_interspeech.pdf

## 问题
长会议转写信息稀疏、话题跳变，多阶段 extract-then-summarize 易累积误差且缺中间校验；参考摘要过短又诱导过度压缩。即便 LLM 上下文超过 100K，仅靠加长输入仍难充分覆盖全局分散要点。

## 方法
提出免训练框架 S3：滑窗切段（w=2048，r=256）并对每段采样 k=5 候选摘要（nucleus 或 DBS），离线建树；用自奖励引导的 MCTS（UCT，c=1.0，30 次模拟）选路径，奖励为 Coherence/Consistency/Fluency/Relevance 的 Likert 归一化均值；最后 refinement 去掉跨段冗余套话。对比整篇摘要基线、Refine、以及每段单候选的 S2。

## 实验与结果
数据 QMSum；骨干含 Qwen2.5-7B/72B、Gemma-3-12B。G-Eval 上 S3-7B 平均 4.56，超过同骨干基线与 72B 摘要级基线（4.54）；S3-12B 达 4.74。按长度分箱时 Base 在长文上相关性下降且摘要占比 <1%，S3 更稳、摘要约占原文 4.66%（参考仅 0.62%）。nucleus 采样优于 DBS（Avg 4.56 vs 4.51）。ROUGE-1 反而偏低，与参考过短、惩罚信息丰富输出一致。

## 结论
结构化段级组合优于单纯放大模型或依赖超长上下文；S3 能生成更合适长度、覆盖更全的会议摘要。

## 点评
把长文摘要写成「段候选组合搜索」，用自评估奖励绕开短参考监督，方向清晰。强在 7B 逼近/超过 72B 整篇生成，且长度分箱证据扎实；脆弱点在自奖励与生成模型同源可能自我偏好，以及计算开销（每段多候选 + MCTS），且 ROUGE 与 G-Eval 背离时需依赖人类/裁判模型校准。
