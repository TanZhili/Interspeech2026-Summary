# From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales

- 论文编号：1420
- 报告人：Ivan Viakhirev
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/viakhirev26_interspeech.pdf

## 问题
Whisper 等大 ASR 在静音/噪声/对抗下会产生与声学脱节的幻觉；WER 与 token 概率难预警。需从内部表征几何解释尺度依赖的失效机制。

## 方法
提出 Spectral Sensitivity Theorem：层增益 ρ、对齐 κ、谱间隙 ξ 决定语境 Jacobian 进入 Regime I（ρ<1，早期声学注入指数衰减）或 Regime II（对齐+增益导致 rank-1 吸引子）。用 SPI 观测量：有效秩 Neff、谱衰减 α、Kirchhoff 指数 Kf。在 LibriSpeech 构造 Hell 对抗集（3.5× 时伸、6 说话人混、0dB 噪声；仅 WER>0.5），分析 Tiny/Small/Large-v3-Turbo 的 Cross/Self-Attn 与 FFN。

## 实验与结果
Small Cross-Attn 谱尾 Neff 降 13.40%（Regime I）；Large Self-Attn Neff 降 2.34% 且谱硬化（Regime II）。相位图上 Tiny/Small 高秩低 α，Large 低秩高 α。作者强调 Regime II 描述的是自信而非正确，仍需外部标签区分真假。

## 结论
幻觉随尺度从「信号弥散」转向「吸引子锁定」；大模型幻觉更像过度结构化的内部先验投影。未来拟扩展到 Canary/OWSM 并用谱正则做检测/抑制。

## 点评
把幻觉从「文本症状」拉回谱几何，对「越大越稳」直觉是有力修正。κ 未直接测、仅从硬化/压缩反推，理论–实验链条仍有跳跃；但尺度分叉现象本身很清晰。
