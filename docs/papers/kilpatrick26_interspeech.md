# Word Iconicity and Phonological Surprisal as Predictors of Age of Acquisition

- 论文编号：1551
- 报告人：Alexander Kilpatrick
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kilpatrick26_interspeech.pdf

## 问题
象似词跨语言更早习得，但儿童实验显示音系非典型形式更难学；成人加工却偏好高 surprisal/非典型形式。象似性与音系不可预期性对 AoA 与成人加工的相对贡献是否分离，尚缺大规模检验。

## 方法
英语大词表：众包象似性、多源 AoA、以及音位 surprisal/entropy（首/末/最大/平均等）。XGBoost 比较各预测子对 AoA 与成人记忆/语义/词汇判断任务的重要性；线性回归与滑动窗口/四分位模型考察象似性效应随 AoA 的变化，并与平均 surprisal 交互。

## 实验与结果
AoA 主要由频率、具体性、音长主导；surprisal/entropy 对 AoA 贡献弱，却对成人加工任务更重要。回归中象似性显著预测更早 AoA（b=−0.442, t=−17.14, p<.001）；平均 surprisal 对 AoA 为正但相对较弱/不一致。滑动窗显示象似性效应在早期习得更强。

## 结论
发展解离：形式–意义透明性支架早期词汇学习，而音系不可预期性更支持成人加工效率。

## 点评
用同一信息论工具同时对 AoA 与成人加工建模，清晰拆开“象似早学”与“surprisal 利成人”的表面矛盾。AoA 与象似性均为常模/众包估计，因果方向仍可争辩；跨语言推广需谨慎。
