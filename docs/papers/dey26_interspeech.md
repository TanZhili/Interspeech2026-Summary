# Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation

- 论文编号：3091
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/dey26_interspeech.pdf

## 问题
对抗攻击在 ASV/ASR 中研究较多，但独立 LID 前端被攻击可拖垮多语后端，文献中系统分析与防御不足。需在白盒梯度攻击下评估 SOTA LID 并构建主动防御。

## 方法
提出 Self-Defensive Adversarial Re-Training（SDART）：在对抗重训（ART）上叠加 (1) 对抗样本挖掘 ASM（随 epoch 提高攻击比例，PGD 步长在 [0.010,0.035] 均匀采样）；(2) 无教师、基于在线标签平滑（OLS）的防御蒸馏，用上一 epoch 按语言聚合的软标签；(3) 动态 α 与按预测熵加权的软标签；(4) 仅用正确分类的干净样本更新语言软标签矩阵。主干主要为 ECAPA-TDNN，输入 80 维 log Mel；攻击含 FGSM/PGD。

## 实验与结果
VoxLingua-10（十大语）与 Common Voice 同语种；评测 EER 与 \(C_{avg}\)。基线 ECAPA 在 PGD（0.03, 5 步）上显著变差。VoxLingua-10 上 SDART：干净 EER 2.801、FGSM 3.666、PGD 3.544，优于 ART、TRADES、DD、MART。Conformer 与 Common Voice 上多数设置亦最优；从 Conformer 迁移攻击到 ECAPA 的黑盒场景中 SDART 仍低于基线 EER。

## 结论
SDART 在多种架构与语料上同时改善干净与对抗 LID 表现，优于常见主动防御；未来拟扩展到更多攻击与其他语音任务。

## 点评
把 ASM 的渐进域暴露、语言条件软标签与“只用干净正确样本引导”串成 teacher-free 蒸馏，针对 LID 的跨语一致性而非通用 logit pairing。脆弱点是攻击设定集中于白盒 FGSM/PGD 与固定步长区间，更强或自适应攻击下的外推未充分验证。
