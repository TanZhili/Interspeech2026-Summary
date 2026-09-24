# Measuring the Redundancy of Decoder Layers in SpeechLLMs

- 论文编号：1873
- 报告人：Adel Moumen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/moumen26_interspeech.pdf

## 问题
SpeechLLM 中 LLM 解码器常占 >90% 参数，语音任务是否真需要全部深度？冗余能否跨任务复用尚未系统刻画。

## 方法
SLAM 框架：WavLM Large + MLP 投影 + Qwen2.5 / Llama 系列（1–8B）。用层间角距离找最优连续可删块；剪枝后对接收层 MLP 加 LoRA，并可选解冻投影做 healing。在 ASR（LibriSpeech、Loquacious）上量化可剪比例（相对 WER≤0.25），再迁移到 CoVoST2 AST（En→De、Fr→En，Whisper 编码器）。

## 实验与结果
文本与语音角距离热图几乎一致，冗余主要继承自预训练 LLM；深层更可删。联合 decoder+projector healing 远优于只修一侧。7–8B 可删约 28–44% 层仍保持可接受 ASR（约保留 ~60% 解码层）；更小模型可删比例更低。AST 可删约 32%，且 ASR 最优剪枝路径几乎可直接用于 AST。Llama3.1-8B 删 40% 层约 35% 加速、显存 15.72→10.37 GiB。

## 结论
解码器冗余大体模态与任务无关；可基于文本前向定剪枝路径，用单剪枝骨干加适配器服务多任务，降低计算成本。

## 点评
用角距离 + 局部 healing 把“多余容量”测清楚，并显示跨 ASR/AST 路径可迁移，对压缩部署很有启发。阈值依赖相对退化阈值；LoRA 微调解码器反降可剪性；更多家族、语种与推理类任务仍待覆盖。
