# Dynamic Time Warping Reveals Prosodic Alignment in Caregiver–Child Interactions across Languages

- 论文编号：2356
- 报告人：Olivier Rüst
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rust26_interspeech.pdf

## 问题
偶发 CDS（紧跟儿童话轮的照料者话语）在结构上更简化，但其韵律对齐机制不明：是短时 priming，还是随儿童年龄变化的社会 accommodation？

## 方法
ACQDIV 中英、日、俄语料（纵向自然互动，主要母子对）。取儿童话轮 offset 后 2s 内的非重叠照料者跟随话轮，计算 Δt；用 Praat/parselmouth 提 F0，均值中心化后 DTW 归一化距离度量音高轮廓相似度。分语言 Bayesian 多层 LogNormal 回归：Norm DTW Dist ~ Δt + Age + (1|child)。用证据比（ER）比较 priming（仅短时对齐、无年龄效应）与 accommodation（短时对齐 + 年龄增大相似度下降）。

## 实验与结果
Δt：俄语正相关（更近更相似，ER≈284.7）；英语无可信效应；日语反而反向。儿童年龄：英、日、俄均与距离正相关（年龄越大越不相似；英/俄 ER=Inf，日 ER≈299），支持跨语言的 accommodation。

## 结论
CDS 的部分韵律特征可由照料者–儿童互动中的对齐产生，并以年龄相关的 accommodation 为主；短时效应受文化/语言调节。局限：仅 F0、语种与文化有限。

## 点评
用 DTW + 发展时间尺度把“CDS 是否只是一般对齐”操作化，并清晰对立 priming vs accommodation。跨语言不一致的短时效应提醒不要把英语模式外推；整句 DTW 可能稀释局部模仿，后续宜做亚话轮尺度分析。
