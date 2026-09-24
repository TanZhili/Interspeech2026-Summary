# How do word frequency and syllable surprisal affect response time and acoustic duration in sentence formulation?

- 论文编号：1080
- 报告人：Ivan Yuen
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yuen26_interspeech.pdf

## 问题
词频与音节频率（本文用音节 surprisal）都会影响启动反应时（RT）与声学时长，但多数研究只在单一语言层面上操作；若按 Levelt 式“离散、分阶段、串行”生产模型，应预期跨层加性效应，这一点在真实词的单/双音节材料上尚未厘清。

## 方法
20 名德语被试在句中/句末位置产出控制词频与重读音节 surprisal 的单、双音节词。词频来自 SUBTLEX-DE/CELEX，音节 surprisal 由 deWaC 上训练的语言模型估计。测量问句 onset 到句反应 onset 的 RT，以及重读元音时长；对 log 变换后的 RT 与长元音时长做线性混合效应模型，检验词频×音节 surprisal 等交互。

## 实验与结果
未得到假设的加性效应，而是选择性交互：单音节词 RT 受词频与位置影响（低频反而更快、句中更慢）；双音节词 RT 主要受音节 surprisal 边缘影响，且方向与预期不完全一致。长元音时长上，单音节仅见句末拉长；双音节出现词频×surprisal 交互，高 surprisal 在低频词上反而伴随更短时长，与“高 surprisal→更长”预期相反。

## 结论
词频与音节 surprisal 对 RT 与声学时长的作用因音节类型而异，且两指标不镜像同一过程；结果更支持跨层交互式生产解释，而非严格离散串行阶段模型。

## 点评
把词层与音节层可预测性正交操纵并同时看规划（RT）与实现（时长），直接检验经典串行假设，问题设定扎实。低频单音节更快、高 surprisal 时长更短等反预期结果，提示“心理词库预编译音节”叙事不能简单外推到真实词跨层组合。刺激集合较小、低频单音节 surprisal 范围受限，是解释交互方向时需谨慎的地方。
