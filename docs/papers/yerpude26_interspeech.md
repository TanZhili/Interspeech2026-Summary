# Attention-Based Multiple Instance Learning with Tabular Stacking for Ambulatory Detection of PVH and NPVH

- 论文编号：2355
- 报告人：Kiran Yerpude
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yerpude26_interspeech.pdf

## 问题
PVH/NPVH 标签只在受试者级，而全日 ACC 切成大量短段，信息段难定位；既往多靠手工汇总+浅层模型，难以同时建模短期突发与跨日持续低效发声。

## 方法
双分支堆叠：预处理保留 voiced、非歌唱、设备开启帧，鲁棒去极值并显式编码缺失。(1) CatBoost：多掩码条件下日级稳健统计（含偏度/峰度/Gini/帧差等）再跨日 mean/min/max；NPVH 另加 CPP/f0 等交互特征。(2) MIL：每受试者最多 24 个 12 s 窗，1D SE-ResNet 编码 + 门控注意力池化到受试者表示，类加权 BCE+focal。(3) 5-fold Stratified GroupKFold 的 OOF 概率经分位数变换后，与差/积组成元特征，逻辑回归 stacking。

## 实验与结果
官方测试：PVH AUC 0.891（第 3），NPVH AUC 0.861（第 1）。OOF：堆叠 PVH 0.886、NPVH 0.757，均优于单分支。消融显示去掉交互特征、日级广播统计、缺失指示或分位数归一化会伤 NPVH；相对 CatBoost-only，完整系统增益很小（约 +0.001–0.002），作者强调互补与校准而非大幅刷分。

## 结论
长时分布统计与注意力 MIL 分别契合 NPVH 弥散低效与 PVH 短暂高强度事件；堆叠与校准对挑战双任务有效。未来可多任务、受试者自适应并做外部验证。

## 点评
病理假设驱动的双尺度设计与挑战榜结果（尤其 NPVH 第 1）对齐得好。诚实报告“深度分支增益有限”是优点；脆弱点在窗数/长度与手工统计空间的超参敏感，以及 NPVH 校准仍偏保守。
