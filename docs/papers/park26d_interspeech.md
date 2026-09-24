# Countering Neural Audio Codec Distortions in Watermarking with Adaptive Restoration

- 论文编号：953
- 报告人：Sungho Park
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/park26d_interspeech.pdf

## 问题
神经音频编解码器（EnCodec、DAC 等）带来结构化、非线性失真，常把水印提取准确率打到近随机；各编解码器失真模式不同，单一恢复网络难以泛化。现有深度水印对经典失真较稳，但对神经编解码仍脆弱。

## 方法
在不动 Timbre 水印嵌入/解码器的前提下，于编解码输出与提取器之间插入频谱恢复：STFT 幅度谱 → 轻量编解码器分类器 → 按类选择专用 ConvNeXt U-Net 恢复 → 送入原提取器。用 L1 重建损失对齐编解码前水印谱。VQ 失真具空间相关，故用 7×7 depthwise ConvNeXt 扩大感受野。按编解码器各训专家模型，推理时动态路由。

## 实验与结果
LJSpeech 8:1:1，评估 11 种神经编解码器。编解码器分类器测试准确率 100%。RVQ 多码本场景恢复后 bitwise accuracy 常超 98%（如 EnCodec 24 kbps：72.91%→98.75%；DAC 8 kbps：86.56%→99.58%）；单码本极低码率（WavTokenizer、StableCodec 等）提升有限、近随机。自适应优于单一共享模型。消融：无恢复 59.01%，无自适应 60.54%，Basic CNN+自适应 70.44%，完整方案 84.05%（EnCodec 6 kbps）。

## 结论
作者认为后处理恢复可显著提升对 RVQ 神经编解码的水印稳健性，且易于扩展新编解码器；单码本信息瓶颈下后验恢复能力有限，未来水印设计宜考虑量化机制本身。

## 点评
把问题定为“编解码感知的谱恢复”而非重训水印，工程上易插拔。自适应专家路由对异构失真很关键。边界清晰：单码本/极低码率几乎不可恢复；训练依赖已知编解码器配对，开放未知编解码仍待验证。
