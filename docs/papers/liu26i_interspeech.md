# Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input

- 论文编号：1192
- 报告人：Changsong Liu
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26i_interspeech.pdf

## 问题
流式文本输入的 LLM-TTS 缺前瞻导致韵律差，且交错生成历史无限膨胀引发长文崩溃；强对齐标注成本高。

## 方法
对预训练 CosyVoice2 LLM 做韵律边界感知后训练：用 WhisperX 弱时间对齐，随机插入 boundary marker 并截断对应语音目标，教模型在有限未来文本下提前停。推理时每 k 词一块、lookahead f 词，滑动窗口用上一块文本/语音作 prompt，KV 缓存 O(k+f)。流匹配与声码器冻结。

## 实验与结果
Seed-TTS-Eval：标准句 WER 4.03%、长文 4.77%；交错基线长文 WER 70.97%（摘要写 71.0%→4.8%）。说话人/情感相似长文显著更高（SPK-SIM 0.65 vs 交错 0.56；相对摘要称 +16.1%/+1.5%）。主观长文 MOS 4.13 vs 交错 3.18。TTFA 约 1296 ms，RTF 0.782。

## 结论
仅用弱对齐后训练即可让现有 LLM-TTS 在流式文本输入下稳定长文合成并改善韵律，无需改注意力结构。

## 点评
边界标记 + 有界滑动窗口直接对准“韵律缺前瞻”与“长文崩溃”两大痛点，且不改架构，迁移成本低。长文 WER 断崖式改善是最强证据。
