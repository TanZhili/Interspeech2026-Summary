# Screening Matters: A Comparative Study of Conventional and Crowdsourced Listening Tests

- 论文编号：1387
- 报告人：Anika Treffehn
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/treffehn26_interspeech.pdf

## 问题

主观听测仍是评估经典与神经语音/音频编解码质量的可靠手段，但实验室 P.800 成本高；众包 P.808 更快更便宜，却难控环境与设备，结果常更差（评分跨度收缩、方差变大）。需要弄清哪些筛选能有效把众包结果拉近实验室基准。

## 方法

对同一套 20 条件 DCR（含参考、MNRU、低通、Codec2/AMR/EVS 及 FlowDec、Lyra、DAC、Mimi、SNAC、WavTokenizer 等），分别做实验室 P.800（27 人）与 MTurk P.808（33 人）。系统比较三类筛选：预筛选（MJNDQ 式 pretest、问卷）、中筛选（traps、参考金标准最低分阈值）、后筛选（评分跨度、MNRU 锚点排序）。以相对 P.800 条件均值的 MAE/RMSE 与 Pearson/Spearman 相关衡量对齐度。

## 实验与结果

无筛选时两测相关高（r=ρ=0.929）但绝对误差大（MAE 0.573、RMSE 0.659），参考分降 1.11、最差锚点升 0.88。Pretest/问卷几乎无效。Gold standard（最低参考≥4）+ 剔除 trap 离群后：MAE 0.327、RMSE 0.401、r=ρ=0.963（留 14 人）。评分跨度≥2.5：MAE 0.284、RMSE 0.325。完美锚点排序：MAE 0.376、RMSE 0.428。联合后筛选（跨度 2.5 + 完美排序）达 MAE 0.230、RMSE 0.259、r=0.974（留 7 人）；通过后筛选者亦通过中筛选。

## 结论

作者认为众包听测可通过 traps、最低参考分、评分跨度与锚点排序显著贴近 P.800；预筛选在本文设定下无效。建议用预设阈值做被试级筛选以替代仅靠条件内标准化离群规则，并多招 3–5 倍被试以抵消淘汰。适用于早期原型评估等需快、省的场景。

## 点评

把“众包差在哪”具体化成未用满量表与条件内方差过大，再按预/中/后筛选做可复现的消融，对实际听测协议很实用。后筛选越严越准但有效人数骤减，统计功效与偏差风险上升；结论依赖本测试集与 DMOS 设定，换语言/立体声/一般音频时阈值需重标定。相对盲目用标准化 outlier，被试级跨度与锚点排序更不易把真实感知差异误判为离群。
