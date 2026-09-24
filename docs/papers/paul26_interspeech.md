# PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent

- 论文编号：2760
- 报告人：Aounon Kumar
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/paul26_interspeech.pdf

## 问题
搜索增强 LLM agent 常用 outcome 级奖励（如 exact match）做 RL，对中间搜索查询质量监督不足，易产生粗粒度复合查询、检索低效，尤其在小模型上。

## 方法
PROGRESS 在 Search-R1 / PPO 框架上加入轨迹级 coverage reward。冻结教师（Qwen2.5-72B-Instruct）离线生成 essential search queries；策略 rollout 提取搜索查询后，由 LLM judge 按语义与粒度匹配，算 precision/recall 的 F1 作为 \(r_{cov}\)。总奖励为 \(r_{ans}+r_{format}+\lambda_{cov}r_{cov}\)（\(\lambda_{cov}=0.2\)）。检索用 2018 Wikipedia + E5，每查询 top-3。

## 实验与结果
策略为 Qwen2.5-3B Base，主训 NQ+HotpotQA。多跳平均 EM：PROGRESS 30.19，优于 Search-R1 (EM,FR) 28.64 与 Zero-search 27.13；仅 HotpotQA 训练时多跳平均 31.28。检索准确率平均 44.96 vs Search-R1 38.66。查询质量（Completeness/Granularity）在 2wiki、MuSiQue 上均提升。1.5B 上亦有小幅增益。

## 结论
教师引导的 coverage 监督可在不需逐步标注的情况下改善查询分解与检索，带来约 2–5% 绝对 EM 提升；作者强调中间搜索行为塑形对 agentic LLM 很重要。

## 点评
把“查什么”从 outcome RL 中拆出，用 F1 式覆盖奖励做轻量过程偏置，方向清楚。依赖强教师与 LLM judge，匹配误差与 \(\lambda\) 设定会传导到策略；文中也承认仍有直接用复杂查询搜索的失败例。
