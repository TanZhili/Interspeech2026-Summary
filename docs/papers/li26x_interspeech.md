# What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study

- 论文编号：1487
- 报告人：Shekhar Nayak
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26x_interspeech.pdf

## 问题
讽刺感知依赖韵律，但自然语料中音高、语速、响度共变，难分离各维度因果贡献；需可控合成刺激做因果检验，并对照模型是否与人类权重一致。

## 方法
用 Qwen3-TTS 单说话人生成，对语速（快/慢）× 音高变化（动态/平坦）× 响度（响/轻）做 2×2×2 全交叉；经 Cohen’s d 正交筛选得 192 刺激（24 句×8 条件）。66 名英语近母语者评 5 点讽刺与自然度；同刺激喂给 Qwen3-Omni（多 seed 平均）。LME 分析主效应与交互。

## 实验与结果
正交验证：目标维度 d 大（音高 1.14、响度 0.81、时长 1.76），非目标 |d|<0.25。人类：响度主效应显著（更响更讽刺），语速与音高主效应不显著。模型：讽刺评分更由语速驱动（更慢更高分），与人类权重不一致。自然度方面人类偏好更快、更轻；模型更偏好动态音高。

## 结论
可控神经 TTS 可构造正交韵律刺激；人类主要靠响度听讽刺，而该基础模型更偏重语速，行为对齐有限。

## 点评
方法贡献大于单一“响度重要”结论：用生成+效应量筛选逼近因果独立。无语境的最小设置抬高韵律权重；模型用同一家族 TTS/Omni，对齐差距可能部分来自训练目标差异，不宜外推到所有系统。
