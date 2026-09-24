# SGAD: A State-Guided Adaptive Decision Framework for Robust EEG-Based Auditory Attention Switch Decoding

- 论文编号：1815
- 报告人：Yuting Ding
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ding26d_interspeech.pdf

## 问题
EEG 听觉注意切换解码（AASD）需在稳定与切换间兼顾准确与低延迟；固定时序平滑难两全。数据划分若未控制音频/说话人混淆会高估泛化。

## 方法
SGAD：因果状态检测推断注意转移态，再以状态引导自适应门控调节时序平滑强度；编码器先预训练再冻结，SGAD 用 L_dec+λ1 L_state+λ2 L_smooth 训练。提出六层评测协议（跨音频、说话人、被试等，含 LOSO/LOSSO）。数据 MS-AASD，男女讲者 0 dB 双耳混合，约 1 s 重叠窗。

## 实验与结果
指标：Acc、Sw-F1、切换检测延迟 SDL。摘要称 SGAD 在多协议下提升准确与稳定性并保持低延迟；不同协议表现差异提示划分相关偏差。具体数值表依正文实验段。

## 结论
状态依赖决策可打破固定平滑权衡；多协议评测对可靠 AASD 必不可少。

## 点评
同时改「怎么决策」与「怎么评」，对神经助听落地更务实。强在混淆控制意识；脆弱点在状态检测误差会传导到门控，且实验室 0 dB 双讲与真实噪声场仍有差距。
