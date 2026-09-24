# A Novel Transfer Learning Approach for Room Impulse Response Estimation and Speech Dereverberation Across Geometrically Diverse and Data-Scarce Environments

- 论文编号：31
- 报告人：Christian Ritz
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pasha26_interspeech.pdf

## 问题
RIR 估计对回声消除与去混响关键，但跨房间形状（矩形→L 形/不规则）泛化差，目标几何标注稀缺。

## 方法
迁移学习：几何感知编码器提形状不变特征，物理信息解码器施加回声稀疏与能量衰减先验；LSTM 将房间参数映射为时域 RIR。微调时冻结编码器只更新解码器。源域 500 矩形房 25k 对；目标仅用 10 房微调、40 房测试。

## 实验与结果
未见目标几何上 MSE 降 56%、LSD 降 37%（相对未迁移设定）。下游去混响：PESQ 3.24 vs GAN 基线 2.78，STOI 0.89 vs 0.79。

## 结论
选择性冻结 + 物理正则可在极少目标房数据下完成跨几何 RIR 迁移，并改善去混响实用指标。

## 点评
“编码器冻、解码器适”把跨几何不变性与房间特异声学拆开，样本效率高。依赖仿真/参数化几何输入；真实测量噪声与不规则材料分布可能削弱物理先验假设。
