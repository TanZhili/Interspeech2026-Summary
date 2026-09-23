# Cross Domain Few-Shot Class-Incremental Audio Classification Via Adversarial Contrastive Learning

- 论文编号：1250
- 报告人：Yanxiong Li
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/si26b_interspeech.pdf

## 问题
既有 Few-shot Class-incremental Audio Classification 假设基类与增量类同域；实际常有域偏移。本文首次系统处理 Cross Domain FCAC（CD-FCAC）：会话间同时存在类增量与域偏移。

## 方法
编码器在 base session 训练后冻结，分类器各会话更新。对抗对比训练：生成多样对抗样本模拟伪目标域，与源域样本一起学域不变嵌入；base session 用监督对比损失促类内紧、类间分。在六对跨域数据集组合上评测 Average Accuracy。

## 实验与结果
六向 AA（%）：Ours 在 FS→NS 46.89、FS→LS 41.67、NS→FS 85.17、NS→LS 79.09、LS→FS 80.05、LS→NS 79.78，均高于 DFSL/CEC/PAN/AMFO 变体与 PCR。N-way K-shot 分析显示 K 增则 AA 升，N=5 时较优。

## 结论
作者认为对抗对比可同时缓解域偏移与类增量遗忘，在 CD-FCAC 上建立新 SOTA。

## 点评
把 FCAC 推到跨域设置填补现实缺口；编码器冻结简化增量但也可能限制对新域声学的适应。对抗样本模拟的“伪目标域”与真实目标域差距仍是主要风险。
