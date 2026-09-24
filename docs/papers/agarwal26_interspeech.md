# Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR

- 论文编号：1314
- 报告人：Saurabh Kumar
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/agarwal26_interspeech.pdf

## 问题
Whisper 在静音与非语音上易产生虚假转录，现有 VAD、置信度、抑制或改模型等方法缓解有限。同时短对话轮次无法填满 Whisper 固定 30 秒窗口，吞吐浪费。需要不改模型、可落地的幻觉检测与安全批处理方案。

## 方法
提出 **anchor audio**：在输入前拼接一段领域内几乎不出现的短提示音频（优选 TTS 合成的 “Mongolia”），用能否正确识别该前缀作为可信度标记；锚点也作多段拼接的分隔符。
五种推理：A1 原版 Whisper；A2 仅 Silero VAD；A3 VAD+锚点前缀，匹配失败则回退整段输出；A4 朴素批拼接后按锚点切分；A5 批处理校验锚点个数，不匹配则回退到单条 A3。推理用 int8 whisper-turbo。

## 实验与结果
1–5 秒片段共约 33k：零售客服私有集、UrbanSound8K（6614，排除 children playing）、AMI、LibriSpeech。
- 整体 WER：A1 32.18% → A5 13.23%；Urban8k HER：A1 72.2% → A3 0.12% / A5 0.14%。
- A4 有 8.45% 切分失败；A5 失败率为 0。
- 并发 32 时 P95 延迟：A3 579ms、A5 566ms，与 A2（570ms）接近。
- 文本 prompt 消融（Ab1/Ab2）HER 仍高于音频锚点，且零售 WER 变差。
- LibriSpeech 上锚点略升 WER（如 clean 2.87%→3.03%），作者归因于专有名词拼写表面差异。

## 结论
输入级锚点音频可在不修改 Whisper 的情况下几乎消除非语音幻觉，并支持带校验的批拼接。A3 适合延迟敏感，A5 适合吞吐；局限包括锚点需领域调参、长句收益下降、仅评 Whisper/英语。

## 点评
做法本质是给自回归解码一个“声学 grounding token”，比纯文本 prompt 更强，且复用同一机制做批分隔，工程上很实用。风险在锚点与真实语音重叠、噪声掩蔽导致匹配失败，以及批校验回退带来的尾延迟；跨领域与跨架构是否成立仍需验证。
