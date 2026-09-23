# Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation

- 论文编号：446
- 报告人：Korin Richmond
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/valentinibotinhao26_interspeech.pdf

## 问题
偏好类听测（AB、BWS）比 MOS 方差更小、更少量表偏差，但因“必须测全对”的误解采用不足。在听者少、时长紧（如濒危语言 TTS）场景下，需要更高效的系统对采样策略。

## 方法
用 Blizzard 2013 刺激（自然音 + 5 个旧系统 + 4 个神经系统，共 10 系统）先做覆盖尽可能多对/元组的 AB 与 BWS 听测（Prolific，排除后 AB 54 / BWS 57 人）。再从已收集答案库中回放三种采样：随机、merge-rank（MR，含随机/正确初始排序与不同每对最大请求数）、ASAP（信息增益 + batch，每轮 9 对）。BWS 侧对请求对做贪心检索以覆盖 batch。用 TrueSkill 估计分数，报告显著成对差异数与对全量排序的 Kendall 相关。

## 实验与结果
AB 与 BWS 上 ASAP 在显著差分数与排序相关上均最好；MR 因逐对深挖、中间覆盖不全，收敛前显著差更少。按估计听测时长（AB 约 16.9s/题、BWS 约 36.6s/题）对比：同等时长下 BWS 优于 AB，ASAP 再放大差距。实践对照：约 10 人、20 分钟 ASAP-BWS（约 200 听测分钟）约等于 40 人同等时长 AB（约 800 分钟）。

## 结论
ASAP 主动采样能更快揭示系统差异并逼近全量排序；BWS 比 AB 更省时长效率；二者组合适合听者/时长受限的评估设计。

## 点评
用“全覆盖听测作答案银行 + 离线回放采样”干净地比较算法，避开了在线听测噪声。结论对濒危语言等少听者场景很实用。需注意：刺激含明显强弱系统，小间距 SOTA 场景下 ASAP 优势可能更关键（文中亦引用 ASAP 原作者小范围条件结果）；且 BWS 检索不保证请求对一定被 best/worst 命中，信息增益实现依赖工程细节。
