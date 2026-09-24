# Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition

- 论文编号：929
- 报告人：Da-Hee Yang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kim26h_interspeech.pdf

## 问题
LLM 系 AVSR 在噪声下仍可能过度依赖受损音频。对比解码（Expert=音视频、Amateur=仅音频）无需训练即可削弱声学偏置，但固定对比强度会在强噪声与干净条件间权衡：强干预利于低 SNR，却可能在干净语音上过纠。

## 方法
在同一 LLM-AVSR 上做训练无关对比解码，用 token 级软门控 \(w_t\) 缩放有效强度 \(\lambda_{\mathrm{eff}}^{(t)}=w_t\lambda\)。\(w_t\) 为三项乘积（保守激活）：
- **相对音频能量 \(E_t\)**：末层末 token 对音频区注意力相对本句运行均值；
- **音频熵 \(H_t\)**：音频区注意力分散度（按头独立算再平均）；
- **JS 散度**：Expert/Amateur 预测分歧，经高斯「甜区」滤波（\(\mu_{\mathrm{sweet}}=0.35\)）抑制过同或过崩塌分歧（防 rank distortion）。

## 实验与结果
LRS3 训练，MUSAN 噪声注入到 0/−5/−10/−15 dB；OOD 到 LRS2。在 Llama-AVSR(8B)、Omni(1B)、Qwen(0.5B) 上相对 AV 基线平均相对改进约 5–10%；干净与噪声均有收益。固定 \(\lambda\) 最优值随 SNR 变化；自适应在各条件更均衡。消融显示 JS 偏稳干净/轻噪，\(E_t/H_t\) 偏助重噪。延迟约 +8.6%。

## 结论
基于注意力与预测分歧的可靠性缩放，可在不改参数的前提下同时改善干净与强噪声 AVSR，避免固定 CD 的鲁棒–干净权衡。

## 点评
把「何时该压音频偏置」做成可观测门控，比一刀切 \(\lambda\) 更贴 SNR 波动。强在即插即用、跨模型尺度可迁移；脆弱点是依赖特定拼接布局提取音频索引、门控超参仍需验证集调，且极端 JS 崩塌时对比项本身就不稳定。
