# Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data

- 论文编号：2629
- 报告人：Ragib Amin Nihal
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nihal26_interspeech.pdf

## 问题
生物声学训练数据按类群、地区与机构碎片化，难以集中；各自微调的专家模型无法无数据联合或会遗忘。现有 BirdNET/Perch 类单体模型扩展需全量重训。任务算术在视觉中有效，但在生物声学中尚未系统检验，也不清楚生态声学结构能否预测权重空间几何。

## 方法
从同一预训练 BEATs（iter3+ AS2M）独立微调 5 个类群专家（661 种：Passerines 336、非雀形目 157、猛禽/水鸟 84、海洋哺乳动物 21、两栖类 63），只共享任务向量 τ=θ−θ0（编码器权重、不含分类头）。合并策略对比 simple avg、task arithmetic、DARE，以及 TIES / DARE+TIES / DELLA 等符号冲突方法。评估用冻结合并编码器上的线性探针与 k-NN；以相对联合训练的 composition gap 为主。另做地区组成（BirdCLEF 东西非/南亚/新热带 + BirdSet POW）与 focal→soundscape 的 domain negation。用谱分布 JSD 与任务向量余弦相关检验“声学生态位”假说。

## 实验与结果
全部类群对满足线性模式连通、无 loss barrier。任务向量近正交：跨类群余弦 0.01–0.04，鸟类内 0.08–0.09；与谱 JSD 强负相关（Spearman ρ=−0.915）。661 类上 DARE+avg 达 59.2%（联合 68.3%，约 86% 相对；gap≈9.1–9.5），TIES 等冲突方法差 1–6 个百分点。合并使多数类群（雀形目等）掉点、少数类群获益（海洋哺乳 +3.9%、两栖 +1.9%）。地区合并准确率 60.8%（联合 67.2%）；三区合并对留出区达单区模型约 90.8% 准确率。focal 任务向量减法单调损害焦点与声景准确率，域否定失败。

## 结论
独立微调的生物声学专家可通过任务算术组成多类群分类器且无需共享数据；近正交几何使简单平均最优、符号冲突方法有害；合并对少数类群更友好。域否定因录音风格与物种身份纠缠而失效。作者主张机构只共享任务向量即可协作组装分类器。

## 点评
把“声学生态位→近正交任务向量→简单平均最优”串成可检验预测，比盲目套用视觉合并更有解释力。实用价值在隐私友好的一射式联邦式组装；脆弱点包括必须统一基座与超参、线性探针 gap 仍约 9%、以及更细分类阶时正交性可能减弱（正文亦提示）。
