# From Awareness to Adherence: Bridging the Context Gap in Spoken Dialogue Systems via Context-Aware Decoding

- 论文编号：1589
- 报告人：Che Hyun Lee
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26m_interspeech.pdf

## 问题
多轮口语对话系统失败常被归因于“忘记历史”；作者指出还存在潜在上下文觉察与生成时主动遵从之间的鸿沟——内部认出关键历史，解码却被参数先验压过。

## 方法
音频适配的 Context-Aware Decoding（CAD）：用内部注意力定位关键历史轮次，推理时对比有/无该关键上下文的输出分布，放大上下文信号（无需额外训练或检索）。在层选择、token–turn–round 聚合与上下文范围上做消融。评测 Audio MultiChallenge 的 Semantic Memory 与 Self Coherence。

## 实验与结果
相对无 CAD：MiMo-Audio 平均 APR 26.01→34.11；Qwen3-Omni 25.78→39.08（Semantic Memory 22.67→39.33，绝对 +13.30pp）；Kimi-Audio 16.19→22.89。整段历史当 key 的 Whole History CAD 反而降至 21.04%，说明需精确选轮。

## 结论
多轮口语对话的上下文失败常是解码遵从问题；基于注意力的 CAD 可在推理期强制上下文忠实，显著提升记忆与自洽子任务。

## 点评
把“记得但没用上”形式化为 awareness–adherence 间隙，干预点放在解码而非再训，部署成本低。依赖注意力作为觉察代理、法官模型与公开榜不一致，绝对分需谨慎解读。
