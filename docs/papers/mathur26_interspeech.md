# How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech

- 论文编号：2805
- 报告人：Nityanand Mathur
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mathur26_interspeech.pdf

## 问题
风格字幕 TTS 用自然语言控音色，但单个词如何影响声学仍不清楚，妨碍诊断失败与改进可控性。图像域有 DAAM，语音尚缺等价框架。

## 方法
将 DAAM 适配到 CapSpeech（T5 风格字幕 + 流匹配 DiT）：在 25 层×24 ODE 步钩取交叉注意力，聚合为每 token 时序热图。对 120 风格字幕×30 文本约 3600 组合分析，分 Style/Content/Function 类，度量时序方差、峰均比、熵，以及与 F0/能量相关，并看层–步重要性。

## 实验与结果
风格词时序方差显著低于内容/功能词（p≪0.001，d=−1.16），呈全局调制；风格注意力与 F0/能量相关且语义一致（如 “loud”–能量 r=+0.64）。风格条件在早期 ODE 步与深层更强（早期相对后期约 5.2× 衰减）；注意力熵在第 17 层最低并与风格重要性峰重合。

## 结论
首次显示风格字幕在语音扩散/流匹配中的交叉注意力机制：风格全局、内容更局部，条件作用呈层–步层次。可为诊断与可控编辑提供归因工具。

## 点评
把 DAAM 迁到时序 mel latent，并做大规模 token 统计，解释性强。归因基于注意力作为忠实代理的假设，未做因果干预（如遮挡/改写 token）验证；仅针对 CapSpeech 架构，换其他条件注入方式时模式可能不同。
