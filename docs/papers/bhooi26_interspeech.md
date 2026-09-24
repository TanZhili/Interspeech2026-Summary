# Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs

- 论文编号：2229
- 报告人：Vinayak Abrol
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bhooi26_interspeech.pdf

## 问题
Speech-LLM ASR 常更新骨干；严格仅训 adapter 时，自回归 LLM 易漂移，而扩散 LLM 的全局精炼是否更耐 adapter-only 瓶颈仍待验证。

## 方法
冻结语音编码器与 LLaDA 等扩散 LLM，仅训练深度 MLP adapter（帧堆叠 + LayerNorm/SiLU）做跨模态投影；对比同设定下的自回归 Llama 等。在 LibriSpeech 多数据量划分评 WER 与 RTFx。

## 实验与结果
960h：test-clean WER 2.807%，相对同设定 AR 约 54% 相对改进，RTFx 约 12.3×（吞吐约 +45%）。低资源多 100h 子集上 dLLM 方差更低、更稳。消融：归一化与手工帧堆叠优于可学习卷积时序；过强 SpecAugment 略伤精度。

## 结论
在严格 adapter-only 协议下，扩散 LLM 比 AR 更可扩展、更快，适合多模态 ASR 集成。

## 点评
把“只训桥”作为硬约束来对比 AR vs 扩散，结论有部署意义。SOTA 数字需放在同冻结协议下理解，未必优于全参微调大系统；adapter 设计消融扎实，但编码器/LLM 选型固定时外推有限。
