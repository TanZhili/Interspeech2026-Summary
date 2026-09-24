# EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis

- 论文编号：1834
- 报告人：Ganjun Liu
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26f_interspeech.pdf

## 问题
自然语言指令可控 TTS 灵活，但常依赖粗糙情绪标签，缺少细粒度类别与强度的显式建模；仅靠语言指令也难稳定捕捉情绪的声学对应。参考音频条件则易受说话人/音色绑定。

## 方法
**EmoInstruct-TTS** 双路径框架：
1. **Emotion2embed**：Sentence-BERT 文本特征与 ECAPA-TDNN 声学特征拼接投影为 896 维；多任务分类 + 序数强度排序损失，覆盖 48 态（27 细粒度类别 + 7 主情绪×3 强度）。
2. **ICE-Flow**：MiniLM 编码指令，流/回归生成声学接地的 Emotion2embed；样本级 L2 + 协方差分布正则；推理可 CFG 调节指令遵从。
3. **合成**：指令进 LLM（Qwen2.5-0.5B+LoRA）做语义规划，Emotion2embed + 说话人嵌入条件 CFM 生成 mel，BigVGAN 声码。

## 实验与结果
ESD + CNCED；弱标注字幕集 + 人工细粒度标注集。相对 CosyVoice2/3：21 强度任务与 27 细粒度任务上 Dual-Path 的 MOS/ESMOS 整体更优；去掉任一路径均下降。48 类客观 ECS 0.870（最高），WER 2.59%（CosyVoice3 更低 1.97%）。ICE-Flow 增加端到端延迟约 <1–2%。分布一致性消融显示 Sample+Dist 最优（IOA 0.91）。

## 结论
作者认为语义指令与结构化情绪嵌入应分工：前者规划语言、后者调制声学；双路径提升细粒度/强度可控与自然度。未来拟支持无预定义类别的开放描述。

## 点评
「双路径」直接回应指令 TTS 的常见失败：文本能描述情绪，却不一定能驱动正确声学。Emotion2embed 用序数几何把强度做成可排序方向，ICE-Flow 再把自由指令接到该空间，工程上完整。脆弱点：48 态标签体系仍是封闭集；部分字幕来自 Gemini 自动生成，噪声可能影响表示；相对 CosyVoice3 在 WER 上仍有差距。
