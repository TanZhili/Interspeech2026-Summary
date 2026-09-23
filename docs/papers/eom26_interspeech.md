# Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning

- 论文编号：3190
- 报告人：SooHwan Eom
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/eom26_interspeech.pdf

## 问题
F5-TTS 等 flow-matching 零样本 TTS 推理需参考音频转写（常靠外部 ASR）；对构音障碍、口音等非典型说话人，ASR 易错，且即便用 oracle 转写，文本条件与参考 mel 中非典型声学也可能冲突，把异常模式灌进合成。

## 方法
提出 RTFree-F5：冻结 WavLM-Large 提取参考语音连续特征，经两层 MLP 投影器映射到 F5-TTS 原文本条件空间，与目标文本经文本编码器得到的特征在时间维拼接，替代原先的参考转写条件；参考 mel 仍作 unmasked 声学上下文。两阶段训练：先只训投影器对齐空间，再联合微调投影器与 DiT 骨干；训练用同说话人跨句对。推理无需参考转写。

## 实验与结果
基于 F5-TTS v1 Base，LibriTTS 训练。典型说话人（LibriSpeech-PC / SeedTTS）：Stage 2 的 WER/MOS 不低于或优于 oracle/ASR 基线（如 LibriSpeech-PC：WER 1.77%、MOS 4.13）。非典型：SAP 构音障碍上 WER 从原始 24.62%、oracle 基线 20.71% 降到 10.39%，MOS 2.16→2.85，但 SIM 0.60→0.50；L2-ARCTIC 上 WER 10.75%→1.44%，优于 oracle 2.00%。仅 Stage 1 在 SAP 上几乎失效（WER 90%）。

## 结论
用 SSL“潜在文本”替换参考转写，可复用预训练 F5-TTS，显著提升非典型说话人可懂度与自然度，并去除参考转写依赖；说话人相似度与可懂度之间存在权衡。

## 点评
问题抓得很准：infilling 里参考文本带来的规范音素期望会与病理/口音声学打架。用与参考声学同分布的 SSL 条件化解冲突，同时保住目标文本控制。脆弱处是 SIM 下降、训练仅在健康 LibriTTS 上做跨句对，以及依赖冻结 WavLM 对非典型语音的表示质量。
