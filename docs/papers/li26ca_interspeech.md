# Self-supervised Speaker Verification with High-Confidence Pseudo-Label Selection and DINO-Style Self-Distillation Based on Pre-trained Models

- 论文编号：1965
- 报告人：Yishuang Li
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ca_interspeech.pdf

## 问题
无标说话人验证依赖聚类伪标签，噪声标签会拖垮判别；预训练模型（PTM）分层表征如何筛出可靠监督、同时不浪费低置信样本，仍是开放问题。

## 方法
HCPLS：在验证集上按层 EER 选 top-K 说话人判别层，各层独立聚类后经共现矩阵与 Hungarian 对齐，仅跨层一致样本进高置信集 H，其余为无标集 L。学生为 WavLM 前若干层加权和 + ECAPA-TDNN；H 上用 Label Noise Correction 伪监督，L 上 EMA 教师提供置信门控 KD，并加双视图嵌入一致性。迭代中再聚类、离线块级校正与重训。

## 实验与结果
VoxCeleb2-dev 无标训练，评 Vox1-O。K=3 时 H 的 NMI/F1 达 0.9522/0.7571。Iteration-1：HCPLS+蒸馏 EER 2.10%（相对仅 H1 基线 2.64% 降约 20.5%）。4 轮迭代后 EER 1.09%，优于 PTM-LC 的 1.25%（相对降约 12.8%），且迭代轮数少于 IPL。

## 结论
作者认为多层聚类一致性可抬高伪标签纯度，低置信样本宜作无标蒸馏而非硬标签；二者联合可得有竞争力的自监督 SV。

## 点评
“高置信硬监督 + 低置信软蒸馏”分工清晰。层选择依赖验证 trial 上的 EER（虽不更新模型），严格无标场景下该先验需注意；主结果集中在 Vox1-O。
