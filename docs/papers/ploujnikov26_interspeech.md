# HybridCodec: Modeling Discrete and Continuous Representations For Efficient Speech Language Models

- 论文编号：2784
- 报告人：Artem Ploujnikov
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ploujnikov26_interspeech.pdf

## 问题
离散音频表征便于接入 LLM，但量化损失细粒度声学信息，低帧率下说话人与韵律退化明显；纯连续方案又难统一多任务。

## 方法
提出 HybridCodec（扩展 FocalCodec）：离散 BSQ 路径捕语义骨架，连续残差焦点编解码捕量化损失细节，支持 50–6.25 Hz。HybridLM（GPT 式）用 AdaLN 在同骨干上做离散 AR + 连续残差单步 NAR，级联推理减少 AR 步数。ECAPA 说话人嵌入条件化；LibriTTS 上训，覆盖 ASR/TTS。

## 实验与结果
重合成：HybridCodec 在多帧率保持高 UTMOS/SpkSim，6.25 Hz 仍可用。下游：相对离散-only，混合在低帧率大幅恢复 UTMOS/SpkSim（如 6.25 Hz SpkSim 0.707→0.834），并改善 ASR WER；AR 步数约按下采样因子缩减。

## 结论
离散粗骨架 + 连续残差细化可在统一 Transformer 中兼顾 LLM 效率与声学保真，尤其利于超低帧率。

## 点评
把“先粗后细”做成同模型 AR/NAR 多路，工程上干净。强在说话人保持与步数节省；6.25 Hz 上 dWER 仍高，说明极低率语义仍吃紧。证据主要在干净 LibriTTS，噪声域外推待证。
