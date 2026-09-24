# Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions

- 论文编号：930
- 报告人：Junhui Zhang
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26m_interspeech.pdf

## 问题
开放自然语言指令控制细粒度表情仍难，因语料多为中性朗读，且许多零样本系统把参考音频送入 GPT 易与指令风格冲突（style leakage）。

## 方法
从影视媒体构建约 1000 小时指令语料：切分去噪、ASR/说话人分离/副语言标签、字幕对齐，再用多模态 LLM（Gemini）三阶段生成上下文摘要、属性与自然语言指令。模型为 prompt-free GPT（属性型 thinking tokens：性别/强度/风格/口音）+ CosyVoice3 式 FM 仅在声学侧注入音色；另有带 Speaker ID 的指令条件说话人 SFT。扩展 InstructTTSEval 测试集覆盖口音、极端情绪、非主流风格等。

## 实验与结果
相对多开源/闭源基线，RP 等指令指标与 I-MOS 强（基测 I-MOS 3.81 最高）；WER 中等，作者归因于野生声学与标签噪声。去掉 thinking tokens 主观下降；外接指令编码器无增益。SFT 相对基座提高人格一致性 P-MOS，但 I-MOS 略降。

## 结论
野生影视指令数据 + prompt-free GPT/thinking tokens/FM 音色注入可提升开放指令表现力；说话人 SFT 可把控制迁移到指定人设。未来需平衡表达力与稳定，并改进 FM 与参考无关音色。

## 点评
数据管线与“风格走 GPT、音色走 FM”的分工直接针对泄漏问题；扩展评测集有社区价值。原始影视数据因版权未公开，可复现性依赖自建语料；表达力提升伴随 WER 上升也显示指令后训练的稳定性代价。
