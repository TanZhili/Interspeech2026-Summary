# Two-Sided Fairness Transfer for Gender-Neutral Speech Emotion Recognition with Partially Observed Attributes

- 论文编号：3201
- 报告人：Woan-Shiuan Chien
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chien26c_interspeech.pdf

## 问题
公平 SER 需同时中立说话人侧与标注者侧性别偏见，但多数去偏依赖双侧属性标签；跨数据集时常只有一侧有性别标注，无法直接训练双侧公平模型。

## 方法
两阶段：Stage1 在 CLAP 上对抗去偏（L_FairCLAP=L_CE+L_Adv）分别得到说话人侧/标注者侧 FairCLAP。Stage2 在源域由参数差构造 ATT2Fair 任务向量 τ=θ_RAT^S−θ_SPK^S，按 θ_RAT^T=λτ+θ_SPK^T（可对称）推断目标域缺失侧公平模型。数据：IEMOCAP、MSP-Podcast v1.11、BIIC-Podcast；四类情绪；S1 全说话人集、S2 标注者性别偏置集；指标加权 F1 与统计均等 ∆SP。

## 实验与结果
正文报告 FairCLAP 与 ATT2Fair 跨数据集可保持识别并改善公平；抽取文本在结果讨论前段截断，具体 F1/∆SP 数字表未见完整。

## 结论
任务算术可在部分属性监督下跨数据集迁移双侧性别中立，无需目标域缺失侧标签。边界依赖源域双侧可用与 λ 调参。

## 点评
把“说话人公平 ↔ 标注者公平”写成参数空间向量差，是对缺失属性部署的务实招数。强处是设定贴近真实标注缺口；脆弱处是任务向量线性假设与域移可能不对齐，且全文截断使定量收益难核验。
