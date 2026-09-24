# HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec

- 论文编号：3393
- 报告人：Arjun Gangwar
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/gangwar26_interspeech.pdf

## 问题
语义–声学解耦编解码有两路：蒸馏进 RVQ-1（快但语义弱）与双流+推理时 SSL（语义强但慢）。需要兼得解耦强度与推理速度。

## 方法
HybridCodec：公共因果 CNN 编码器（24 kHz→25 Hz）分语义/声学支路；语义 VQ（16384）经轻量 ConvNeXt 解码蒸馏 w2v-BERT-2.0 第 16 层（训练时冻结，推理去掉 SSL）；声学支路对“公共潜变量−语义解码”做 RVQ。GAN+谱重建+蒸馏训练。对比 DAC、DAC(Distill)、DualCodec。

## 实验与结果
60k 更新 LibriSpeech：HC-SED-AED RVQ-1 WER 15.36% 最优；高码本层重建具竞争力。跨语/零样本（SeedTTS-en、CV-French）语义仍强。相对 DualCodec 约 3× 加速（RTF 约从 0.042 量级降至约 1/3）。消融显示双流+蒸馏组合对 RVQ-1 最关键。

## 结论
双流结构加语义蒸馏可在无推理 SSL 下保持强 RVQ-1 语义与快速推理，适合下游语音 LLM tokenize。

## 点评
把 DualCodec 的解耦与 Mimi 式蒸馏拼成“训练重、推理轻”的折中，工程动机清楚。25 Hz 低帧率有利于长上下文 LM；声学质量与纯 DAC 仍有取舍。
