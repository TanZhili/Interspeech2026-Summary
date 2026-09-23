# Temporal Partitioning of Vocal Activity for Detecting Vocal Hyperfunction from Neck-Surface Accelerometer Data

- 论文编号：1435
- 报告人：Władysław Średniawa
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azarski26_interspeech.pdf

## 问题
用长期颈表 ACC 检测 PVH/NPVH 时，仅靠全日汇总统计可能抹掉日内用嗓变异；既往基线 AUC 约 PVH 0.82、NPVH 0.78，需更好的时间切分与特征工程以提升区分度。

## 方法
在 NeckVibe 数据上分任务建模。PVH：策略1——将日切为 10 个部分重叠时间窗，对 CPP、H1–H2、spectral tilt、L/H、ACC 幅度、SPL 等在 voiced 帧上取 mean/median/SD/10th/90th 及 voiced 比例，并全日汇总 IBIF；用强正则 XGBoost。策略2——语音/歌唱分开聚合、减为 4 个非重叠时段，用逻辑回归。最终对两模型概率平均做集成。NPVH：在 Cortés 式短窗上网格搜索窗长与 voiced 比例阈值，最佳为 300 s 且至少 10% 语音+歌唱，再聚合到受试者级，用另一套正则 XGBoost。严格 LOGO（按受试者）验证。

## 实验与结果
训练集聚成：PVH 集成 LOGO AUC 0.891（单模型约 0.871/0.881）。官方测试：PVH 集成 AUC 0.925（第 1）；NPVH AUC 0.820（第 4），均超基线。SHAP 显示下午/晚间 H1–H2 低变异、高 IBIF CQ 等指向 PVH；NPVH 更依赖短窗高分位统计而非宽时段模式。经典 MLP/CNN/LSTM 易过拟合。

## 结论
按日切分与语音–歌唱分离能提升 ambulatory VH 检测；PVH 与 NPVH 最优时间尺度不同（宽窗日内结构 vs 短窗瞬态）。集成与特征工程优于浅层神经网络在该受试者规模下的表现。

## 点评
把挑战组织文里的“日内变异”落到可复现的切窗与双模型集成，并用 SHAP 把预测接到声门闭合相关生理解释，工程与可解释性兼顾。脆弱处在任务特定超参与手工特征空间，换设备/人群时窗设置可能需重搜；NPVH 召回仍偏低，反映该类异质性更大。
