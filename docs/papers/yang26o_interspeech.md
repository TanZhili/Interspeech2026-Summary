# Speech Recognition on TV Series with Video-Guided Post-ASR Correction

- 论文编号：2970
- 报告人：John Hansen
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26o_interspeech.pdf

## 问题
TV 剧 ASR 面临多说话人、重叠、专有名词与长程上下文；唇读类 AV-ASR 依赖高分辨率对齐人脸，剧集中常不可用。现有后修较少显式利用视频语义上下文。

## 方法
提出免训练 VPC：先 ASR 得转写；再用 VideoLLaMA2 以 QA 抽取剧名识别与细粒度场景描述；最后用 GPT-4o 据视频上下文仅修正明显识别错误。评估于 Violin 英语 TV 子集（约 90 h，训/验/测 72/9/9 h）。

## 实验与结果
对 Librispeech 预训练再微调的 wav2vec2/HuBERT/WavLM/Conformer：VPC 相对原始 ASR 相对降 WER 约 13.06%/11.86%/20.75%/7.46%（WavLM 29.83→23.64）。无视觉的 GPT-4o  alone 几乎无效甚至变差。初步 AV-HuBERT 达 78.3% WER（人脸条件差）故未作主对比。100 片段消融显示 All-QA（粗+细）优于单一 QA。

## 结论
高层视频语义 + LLM 后修可在复杂多媒体下稳定降 WER，且不必改 ASR 骨干。

## 点评
相对唇读路线，改走语义上下文更贴剧集现实。依赖闭源 GPT-4o/VideoLLaMA2，修正边界靠提示“只改明显错误”，可能引入幻觉；相对提升在弱 ASR（WavLM）上更大，强 Conformer 增益较小。
