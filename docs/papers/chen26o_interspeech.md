# CE-CoT: A Contrastive Empathetic Chain-of-Thought Training Strategy for Improving Emotion Consensus in Empathetic Speech LLMs

- 论文编号：1271
- 报告人：Jing-Han Chen
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chen26o_interspeech.pdf

## 问题
共情语音 LLM 常用 SER 准确率、Emotional Reaction（ER）、Exploration（Ex）等指标，但它们不保证回复情绪方向与用户一致。Emotion Consensus（EC）衡量这种方向正确性，在语音 LLM 中仍少被显式建模；仅靠识别正确情绪并不能保证回复共情对齐。

## 方法
提出 Contrastive Empathetic Chain-of-Thought（CE-CoT）：把目标回复拆成情绪识别 e、忽略情绪的中性回复 r_neu、再经情感反应与探索性提问修订的 r_rev，形成隐式对比（r−=r_neu，r+=r_rev）。训练两步：(1) 用文本 LLM（Qwen-7B-Chat）结合转写与含真值情绪的 CE-CoT prompt 生成期望 CoT 回复 R；(2) 语音 LLM 仅见语音与不含真值情绪的同一 prompt，用 KL 散度对齐到 R。推理沿用同一结构。EC 由 LLM 裁判（Gemini Flash 2.0）判断 r_rev 主情绪是否匹配标签。

## 实验与结果
在 IEMOCAP、ESD（英）、MSP-Podcast 子集、MESC 上评估 BLSP-Emo、RE-LLM、Qwen2Audio。预训练通用模型多数 EC 低于 0.5；vanilla 行为对齐增益有限或不稳。CE-CoT 对齐相对预训练/vanilla 在多数据集显著提升，例如 BLSP-Emo 在 MSP-Podcast 上相对 vanilla 约 +19.1%，在 MESC 上相对预训练约 +35.2%。条件评估中，CE-CoT 使因 EC 失败而清零的 ER/Ex 掉幅约减半。案例显示 vanilla 易把开心用户回成悲伤，CE-CoT 可对齐。局限：单轮、未深挖内部推理与 EC 度量变体。

## 结论
结构化对比式 CoT 对齐可提升共情语音 LLM 的情绪一致性，超越表面模仿式微调；作者认为这为多轮与更细 EC 度量奠定基础。

## 点评
把“识别对了却回错情绪”拆成可监督的中性 vs 修订对比链，训练目标直接对准 EC，比只追 ER/Ex 更对准部署风险。依赖文本 LLM 造监督与 LLM 裁判 EC，增益对裁判与 prompt 敏感；单轮设定下尚未检验多轮情绪漂移时对比结构是否仍稳。
