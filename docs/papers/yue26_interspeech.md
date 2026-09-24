# G2C-NET: A Grid-to-Continuous Neural Network for Sound Source Localization in Distributed Microphone Arrays

- 论文编号：1733
- 报告人：Zhiyuan Yue
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yue26_interspeech.pdf

## 问题
分布式麦阵网格化 SSL 把回归改成分类，但粗网格量化误差大、细网格算力高；均匀聚合麦对特征也忽略各对可靠性差异。

## 方法
G2C-NET：在 pairwise 特征（GCC/SLF）上用 Adaptive Pairwise Feature Aggregator（可学习 query 注意力）得到全局网格似然 h；Continuous Position Estimation 对峰值邻域（窗口 R）做似然加权质心得到连续坐标。损失 Ld（与高斯目标分布 MAE）+ λLc（坐标 L2），CPE 可微以提供亚网格监督。

## 实验与结果
仿真与 Libri-adhoc40 微调：Ours RMSE/ACC 仿真 25.52 cm / 78.63%，真实 23.35 / 81.15，优于 SRP、GNN、LMSL。少节点时优势更大（如 SLF、M=4：33.09 vs GNN 46.22）。消融显示 APFA 在稀疏阵更关键、CPE 在多节点更关键；λ=10 最优。

## 结论
注意力聚合 + 网格到连续细化可在固定分辨率下降低量化误差并提升鲁棒性，无需更密网格。

## 点评
在保持 pairwise/可变麦数框架的前提下补“可靠性”与“亚网格”，问题切得准。注意力权重与特征质量正相关的分析有说服力；仍偏单源 2D，多源与未知高度需扩展。
