# SpAArSIST: Sparsified AASIST for Efficient and Reliable Anti-Spoofing

- 论文编号：2430
- 报告人：Anton Firc
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/firc26b_interspeech.pdf

## 问题
SSL+AASIST 图池化反欺骗常用但公开实现含冗余操作，算力偏高；需在不牺牲判别力下简化后端，并兼顾域外稳健与校准。

## 方法
SpAArSIST：保留 XLS-R 前端与 AASIST 图交互骨架，改三点——训练/推理分离的 top-k 保留比 (k_tr, k_inf)；用节点特征幅度（L2）替代可学习打分；用均值聚合替代高温 softmax 的 stack-node 注意力（或降温度对照）。在 ASVspoof 5 两阶段训练，并在 In-the-Wild 测域外。用判别+校准+算力的双轨复合分排序配置。

## 实验与结果
最佳配置后端 MACs 195.045M→154.706M（约 −20.7%），参数 611.8k→586.4k（−4.1%）；ITW EER 4.64%→2.82%、minDCF 0.133→0.078；ASVspoof 5 上仍具竞争力。幅度打分 + 更激进剪枝（如 k_tr=0.3, k_inf=0.1）常居复合分前列。

## 结论
简化图池化与读出可在降算力同时提升域外稳健；训练–推理分离稀疏比为部署提供旋钮。复合分便于在准确、校准与算力间选模型。

## 点评
相对“加模块刷分”路线，做减法并量化每项贡献，工程价值高。幅度代理可解释但未必普适；结论依赖固定 XLS-R 配方，跨前端迁移需再验证。
