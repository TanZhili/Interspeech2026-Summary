# Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs

- 论文编号：110
- 报告人：Minh Duc Pham
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26_interspeech.pdf

## 问题
多语 Audio LLM 在英–汉码切换转写上仍系统失败：漏掉一种语言、整段翻译、幻觉重复；即使含 CS 监督数据的模型也可能如此。

## 方法
用 DPO 对齐：chosen 为真值混合转写，rejected 由 Qwen3-32B 对真值做全局翻译（80%）或部分片段翻译（20%）以模仿失败模式。约 100K 对 / ~570h，来自 CS-Dialogue（自然对话）与 EMILIA（英汉拼接）。训练 MERaLiON-2-3B、Phi-4-MM（全参）与 Qwen2-Audio-7B（LoRA，全参易幻觉）；训练时从 20 英 + 20 中提示池随机采样，评测固定英文转写提示。

## 实验与结果
相对基线 MER：Phi-4 在 EMILIA 70.98→7.38（相对 −89.6%）；Qwen2-Audio SEAME dev man 72.89→58.30（−20.0%）；MERaLiON 因已有 CS SFT，SEAME 增益较小（0.7–2.0%），CS-Dialogue −11.1%。定性显示翻译、幻觉、漏语等三种失败模式均被纠正。SEAME 为分布外。

## 结论
偏好对可把已具备多语能力的 Audio LLM 引出正确的“原样混合转写”行为，分布内与分布外均有一致改善。

## 点评
核心是行为对齐而非重训声学：用可控合成 rejected 放大“翻译≠转写”信号。未显式构造幻觉/漏语 rejected，但三类错误仍下降。局限：仅英汉、rejected 非模型自身采样、未测对其它音频能力的副作用。
