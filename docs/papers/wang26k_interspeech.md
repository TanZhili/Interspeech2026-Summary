# Does Fine-tuning by Reinforcement Learning Improve Generalization in Binary Speech Deepfake Detection?

- 论文编号：589
- 报告人：Xin Wang
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26k_interspeech.pdf

## 问题
主流 SSL 深度伪造检测多用监督微调（SFT），易对目标域过拟合。受 LLM 启发，问 Group Relative Policy Optimization (GRPO) 能否改善未见攻击/域泛化。

## 方法
在 AntiDeepfake 多阶段管线（预训练 SSL + 后训练 + 微调）上，对 XLS-R-2B / MMS-1B / MMS-300M 等二分类检测器试纯 GRPO、SFT、SFT→GRPO 及简化/无负样本/不同 β 变体。目标域 DFE24；域外 ADD23、FoR、DEEP-VOICE、In-the-Wild。消融负奖励与正则项。

## 实验与结果
XLS-R-2B：纯 GRPO 域内平均 EER 约 9.93，域外平均 2.69，优于 SFT（10.26 / 6.28）与多数混合设置。去掉负样本后域外变差；过大 β 严重损害域内。无后训练时 GRPO 域外仍差，说明后训练表征是前提。分布漂移测量支持上述发现。

## 结论
纯 GRPO 微调可在保持目标域性能的同时显著提升域外泛化；负奖励可能是关键因素。面向 SSL 前端二分类检测器的结果据作者称属新发现。

## 点评
把 LLM 对齐工具迁到反欺骗，问题设定清楚。纯 RL 优于 SFT→RL 暗示过强监督会锁死决策边界；依赖大规模后训练与算力，落地成本不低。
