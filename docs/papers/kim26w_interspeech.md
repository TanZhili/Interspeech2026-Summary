# Scaling Self-Supervised Speech Models Uncovers Deep Linguistic Relationships: Evidence from the Pacific Cluster

- 论文编号：3205
- 报告人：Minu Kim
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26w_interspeech.pdf

## 问题
既有观察认为 S3M 语言表征主要反映地理邻近或浅层接触，难以恢复深层谱系与长时区域汇聚。问题是：把 LID 覆盖从百级扩到数千语种，是否会非线性地改变嵌入拓扑并显现深层历史结构。

## 方法
比较同骨干 MMS-LID 的 126/256/1K/4K 语种模型；对 49 语（DoReCo+FLEURS）取末层双平均质心，标准化后 Ward 层次聚类，以 ARI/NMI 对照谱系子群，并用文件级 bootstrap（B=1000）估枝置信度。对 POA（Papuan–Oceanic–Australian）簇做维级 t 检验与 30 项声学特征相关，Mann–Whitney 在原始信号上独立验证。1K 与 4K 对 45/49 语 seen/unseen 状态一致，以隔离“覆盖规模”效应。

## 实验与结果
谱系恢复在 126–1K 平台期后，4K 跃升（峰值 ARI 0.74、NMI 0.95，K=18）。4K 树恢复多数家族，并高置信出现早期中华文化圈、波斯区域、达罗毗荼底等接触簇；澳斯特罗尼西亚分裂为未过新几内亚的 A 组与 Oceanic+Papuan+Australian 的 POA 宏簇（bootstrap 约 57%，Oceanic–Papuan 74%）。POA 分离精度 4K 达 1.0（1K 最高约 0.92）。4K 以更少显著维、更集中编码区分 POA；Bonferroni 下 energy dynamic range 最突出（28%），且原始声学上 POA 能量动态范围更高、谱变异更低，与嵌入相关一致。

## 结论
大规模语言覆盖可定性重塑 S3M 几何，恢复深层谱系与长时接触；太平洋宏簇提供声学侧区域汇聚证据。作者视为计算历史语言学与接触研究的新视角。

## 点评
规模效应的“平台期→跃迁”叙事清楚，并用 seen/unseen 控制与声学验证降低“只是看过这些语”的解释。POA 仍是相关性证据，bootstrap 中等、录音条件/语料构成可能混淆；不宜直接当作谱系证明，更适合作为接触与声学共性的计算假说生成器。
