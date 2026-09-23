# Consistency-Regularized Dual-Branch Network with Performance-Aware Mean Teacher for Sound Event Detection

- 论文编号：353
- 报告人：Lipeng Dai
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dai26_interspeech.pdf

## 问题
预训练模型（如 ATST）用于 SED 时，浅层与深层特征利用不足，半监督 mean teacher 更新幅度固定、易不稳定。需要更好的跨分支一致性与自适应教师更新。

## 方法
ATST 前端 + 双分支后端分别建模浅/深特征；提出时间拓扑一致性损失（TTC）对齐双分支时序结构相似；Performance-Aware Mean Teacher（PA-MT）按学生表现自适应 EMA 更新幅度；跨阶段融合（CSF）合并不同训练阶段优势。在 DCASE 2024 Task 4 上评测。

## 实验与结果
最终 0.541 PSDS1、0.768 mpAUC、Score 1.309，称新 SOTA；消融显示 TTC 主要提 PSDS1，PA-MT 稳定教师更新，CSF 进一步抬分。

## 结论
作者认为双分支一致性正则与表现感知 mean teacher 可提升预训练 SED 的半监督效果。

## 点评
把“浅深特征该一致什么”具体成时间拓扑，比笼统一致性损失更贴 SED 边界任务；PA-MT 针对固定 EMA 的痛点。分数高度依赖 DCASE2024 协议与强预训练前端，迁移到其他标注噪声设定需再验证。
