# U-Codec: Neural Speech Codec under Extreme Temporal Compression for Fast High-Fidelity Speech Generation

- 论文编号：2398
- 报告人：Xusheng Yang
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26n_interspeech.pdf

## 问题
主流 codec 常 50–75 FPS，自回归 LLM-TTS 每秒需大量前向；极低帧率（如 5 Hz）易损可懂度与频谱细节。

## 方法
U-Codec 目标 5 Hz：Transformer 帧间长依赖（Codecformer）+ 系统扫描 RVQ 深度与码本大小。接入全局–局部层次化 LLM-TTS，在多层 token 上建模依赖。对比高帧率 codec 的重建与 TTS 速度/自然度/相似度。

## 实验与结果
5–12.5 Hz 下 PESQ 具竞争力；接入 LLM-TTS 后相对高帧率 codec 推理约快 3×，相似度与自然度大体保持。验证 5 Hz 离散 token 可用于快速高保真合成。

## 结论
帧间 Transformer + 恰当 RVQ 配置使极端时间压缩可行，显著加速 LLM-TTS。

## 点评
把瓶颈从“码率”明确转到“帧率×自回归步数”，对部署延迟很务实。5 Hz 对瞬态辅音/精细韵律仍可能欠采样；质量–速度折中需按语种与场景复核。
