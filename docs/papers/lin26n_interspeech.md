# WQ-Fusion: Dynamic Gated Attention for Cross-Domain Audio Representation

- 论文编号：3228
- 报告人：Gongping Huang
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/lin26n_interspeech.pdf

## 问题
单编码器难以同时覆盖语音精细结构与非语音/高层语义；静态拼接 Whisper 与 Qwen 虽已强，但不能按任务动态取舍。

## 方法
**WQ-Fusion**：冻结 Whisper-large 与 Qwen2-Audio 双骨干 → Adaptive Feature Modulation 对齐 → 位置编码 → 元素级门控 Transformer 动态路由。面向 Interspeech 2026 Audio Encoder Capability Challenge Track A（XARES-LLM 类评测）。

## 实验与结果
总体分 0.836，高于最强单编码器（如 Qwen 约 0.796）与简单拼接（约 0.832）；消融显示 AFM + 门控逐步抬升至 0.836。Whisper 偏语音、Qwen 偏非语音/语义，融合后互补。

## 结论
动态门控融合异构编码器可提升跨域通用表示，优于静态拼接。

## 点评
挑战赛系统文：核心洞察是“互补 inductive bias + 可学路由”。依赖两大冻结骨干，部署重；门控是否真正按任务解释仍需更多诊断。
