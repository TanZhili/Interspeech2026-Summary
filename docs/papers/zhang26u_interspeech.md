# Learning to Wait: Real Streaming Speech-to-Text Translation with an LLM

- 论文编号：1323
- 报告人：Rogier van Dalen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26u_interspeech.pdf

## 问题
LLM 流式语音翻译的 SOTA（Bestow）用固定 wait-k：按固定音频块节奏吐 token。标准测试集短、静音规整时看起来还行，但真实场景麦克风早开、说话犹豫或过快时，会幻觉或越落越远。

## 方法
在 Bestow 架构（Conformer 语音编码器 + 条件网络交叉注意力 + 冻结 3B LLM+LoRA）上，用可学习 wait policy 替代固定节奏：每步根据已见音频与已输出文本，输出 Wait/Emit 二分类分布；Emit 时再跑 LLM 生成下一 token。训练时用强制对齐得到参考 Wait/Emit 序列，对 wait policy 与 LLM 多任务联合损失，一次算齐所有 (t,u) 组合。解码时交错执行 wait/emit。

## 实验与结果
英→法/韩，训练约 3700h（LibriSpeech+CommonVoice+MuST-C，目标文与对齐由 GPT-4/QWEN 等生成）。评测 Fleurs；另构 SilFleurs（句首加 5s −20dB 噪声）暴露早开麦问题。英→法：Learned 在 Fleurs 上 COMET 0.767、延迟 1.72s（Fixed 3.57s）；SilFleurs 上 Learned 0.745，Fixed 跌到 0.593。英→韩：Learned Fleurs/SilFleurs 均为 0.820，Fixed 从 0.814 崩到 0.486。AlignAtt 基线对静音也明显更差。

## 结论
内容条件的可学习等待策略在保持质量的同时降低延迟，且对句首静音不敏感；固定 wait-k 在真实开麦条件下会灾难性幻觉。

## 点评
抓住了“评测分布 ≠ 真实开麦/语速”这一部署痛点，用 SilFleurs 把固定节奏的失败模式钉死。Wait policy 条件于已输出文本，相对 continuous integrate-and-fire 更合理。脆弱处是对齐与目标翻译依赖外部 LLM/强制对齐，且长句、快语速下的追赶行为正文未充分量化。
