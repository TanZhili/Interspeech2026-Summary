# Temporal Ensembling Threshold and Neighbor-Aware Label Mixup for Speaker Verification with Open-Set Noisy Labels

- 论文编号：11
- 报告人：Liang He
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fang26_interspeech.pdf

## 问题
大规模说话人数据噪声标签难免；开集噪声（真说话人不在标签集）经硬标签纠正仍错，软标签又学不稳，现有选样/纠正方法对此不足。

## 方法
提出 TET-LM：每轮用嵌入–原型余弦相似度拟合双成分 GMM 得阈值，EMA 集成得 ¯τ 划分 clean/noisy；mean-teacher 对 noisy 取 top-K 邻类（高置信则 K=1），归一化权重做邻域标签 mixup 损失。三阶段：全量 warmup → 仅 clean → clean + mixup。ECAPA-TDNN1024 + AM-Softmax；在 VoxCeleb1/2 注入 10–50% 同性别对称/非对称噪声。

## 实验与结果
消融表明去掉 TET 或 LM 均变差，高噪声下 LM 更关键；K=10、μ=0.4 最优。相对 Standard，平均 EER/minDCF 约降 54%/42%（最佳基线 ES-GMM 约 52%/40%）。Vox1 Sym-50%：Standard EER 13.71 → TET-LM 4.04；Vox2 各评测列表上多数噪声设置亦最优或近最优，干净数据表现稳定。

## 结论
时间集成阈值稳选样，邻域 mixup 更适配开集纠正；多阶段训练提升不同噪声场景鲁棒性。

## 点评
把开集噪声显式当成“邻域混合”而非硬翻标签，比只丢弃 noisy 更贴真实爬取数据。噪声为同性别人工翻转的受控设置；真实网页噪声分布与跨数据集迁移仍待验证。
