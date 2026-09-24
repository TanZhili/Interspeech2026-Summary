# Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising

- 论文编号：3422
- 报告人：Sergio Burdisso
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/burdisso26_interspeech.pdf

## 问题
仅用目标域文本微调 LLM-ASR 的 LLM 会破坏 projector 学到的语音–文本对齐，引发灾难性遗忘。文本比配对音频更易得，需要不改结构、不增参的纯文本适应。

## 方法
把适应建成去噪任务，并用 multi-view noise-driven batching：每个 mini-batch 混合 (1) 源域配对音频–文本、(2) projector 诱导的噪声转写、(3) 合成破坏的源转写、(4) 破坏的目标转写。合成噪声含随机字符替换与重复，模拟 projector 噪声模式。冻结编码器与 LLM 骨干训 projector 得基座后，用该混合做文本适应；无架构改动。

## 实验与结果
SLAM-ASR（WavLM-Large + Llama 3.2 系）上 DefinedAI / SlideSpeech。域内/域外/跨域三档：相对 Fang et al.、Ma et al. 文本适应更优；跨域相对基座相对 WER 改进最高约 25.4%（An），仍低于有音频适应上界。SlideSpeech 域外相对改进约 4.2%–7.0%。

## 结论
多视角噪声混合可在纯文本适应时保持语音–文本对齐，显著优于近期文本适应法，且不增参数。

## 点评
关键洞察是“别让 LLM 只见干净目标文本”，用源音频与噪声视图当锚防遗忘。工程上轻、可插。上界仍逊真音频适应；噪声配方需调，跨声学域差距仍大。
