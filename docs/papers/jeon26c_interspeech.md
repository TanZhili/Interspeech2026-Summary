# Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR

- 论文编号：1569
- 报告人：Woori Jeon
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeon26c_interspeech.pdf

## 问题
将 GPTQ/AWQ 等 PTQ 直接用于 Whisper 在 2–3 bit 时严重退化甚至幻觉循环。语音激活在稳态与零填充区高度相关，在音素边界变化剧烈；帧均等进 Hessian 会使静态/填充主导校准，掩盖关键过渡。

## 方法
DiffAQ：用帧间激活差 ∆xt=xt−xt−1 的 L2 范数作时间密度，归一化后得权重 wt=α+(1−α)d̄t（α=0.2），缩放 Hessian 累加。仅改编码器线性层；解码器仍用标准 GPTQ。训练无关，校准 128 条 LibriSpeech train-other，评 Whisper base/small/medium、LibriSpeech 与 FLEURS。

## 实验与结果
3-bit 全配置最低或近最低 WER；2-bit 增益最大：Medium test-other 17.53%→12.93%，FLEURS 18.05%→12.07%；Small FLEURS 3-bit 11.37%→8.69%。RTN/AWQ 常 WER>100%。Base 在 2-bit 仍崩坏，属容量瓶颈。α 不敏感。

## 结论
按声学变化率加权 Hessian 可改善超低比特 ASR 的 PTQ；2-bit Medium 权重大约从 1.5 GB 压到 <200 MB。局限：噪声瞬态也可能获高权重；未验证其他编码器架构。

## 点评
抓住语音相对文本的“时间冗余/填充陷阱”，把 PTQ 校准偏到音素过渡，改动小、解释清楚。强在无需重训；弱在 Base 2-bit 仍不可救，且差分对非语音瞬态不具选择性。
