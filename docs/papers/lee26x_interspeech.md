# AGENT: A Black-box Adversarial Attack Exposing the Achilles' Heel of SASV Systems

- 论文编号：3207
- 报告人：Yowon Lee
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26x_interspeech.pdf

## 问题
SASV 通过 ASV+CM 联合决策缓解欺骗与对单 ASV 的对抗；针对完整管线（级联或分数融合）的黑盒对抗仍不足，既有方法常依赖辅助网络或迁移弱。

## 方法
论文提出 AGENT：在替身 ASV/CM 上联合优化，使输入扰动同时抬高说话人相似度并维持反欺骗通过；用方向选择式梯度融合缓解两目标梯度冲突，再在幅度约束下迭代更新，并将样例迁移到受害 SASV。强调分数最大化以加强跨架构迁移。本文摘要不复述算法逐步更新式与超参配方。

## 实验与结果
作者报告跨多种 SASV 配置攻击成功率最高约 99.62%；在级联结构上相对 FAKEBOB、Double-deceiver 等基线显著更高，并在替身–受害架构不匹配时仍保持较强迁移。

## 结论
作者认为当前 SASV 联合边界仍可被专门设计的黑盒对抗击穿，需更强实战防御。价值在安全评测与风险提示。

## 点评
把攻击目标从单 ASV 扩到 ASV–CM 联合决策，指出梯度冲突是联合攻击难点。防御侧宜关注联合对抗训练、查询限流与决策校准；完整攻击程序细节应留在原文，本总结仅记录研究主张与量级结果。
