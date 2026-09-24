# DGS-MLDG: Domain Gradient Surgery Guided Meta-Learning for Domain Generalization in Speech Deepfake Detection

- 论文编号：1042
- 报告人：Youzhi TU
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qin26_interspeech.pdf

## 问题
语音深度伪造检测在未见域上易失效。MLDG 通过元训练/元测试模拟域偏移，但两目标梯度常冲突（余弦相似为负），朴素聚合会抵消更新。

## 方法
提出 Domain Gradient Surgery (DGS)：不对称地把冲突的元测试梯度投影到元训练梯度的法平面，去掉破坏性分量。Layer-wise DGS (LW-DGS) 按实时余弦相似度只对冲突层做手术。骨干为 XLSR-Mamba 类检测器；与 ERM、标准 MLDG、PCGrad/GradVac/CAGrad 对比。

## 实验与结果
跨数据集平均相对 ERM：DGS-MLDG +5.29%，LW-DGS-MLDG +4.04%。In-the-wild / CodecFake 上 DGS 达 5.23% / 6.76% EER，优于对称梯度手术。反向投影或只手术 SSL 骨干会变差；冲突负比例由约 33% 降至约 23.5%。

## 结论
针对元学习双层结构的不对称梯度手术可稳定 MLDG，提升跨编码与真实场景泛化；层选择版在效率与收益间折中。

## 点评
抓住“元训练应主导、元测试只纠偏”的双层不对称性，比把两任务当对等 MTL 更贴合 MLDG。增益在难集更明显；平均相对提升约 5% 不算革命性，但是干净的优化向改进。
