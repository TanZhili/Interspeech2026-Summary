# TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation

- 论文编号：218
- 报告人：Shengkui Zhao
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26_interspeech.pdf

## 问题
单声道分离既需短时谱连续性（谐波、音素过渡），也需长程说话人一致性。全局 Transformer 注意力易忽略局部细节，静态卷积感受野又不够灵活；时域分块方法未能充分利用二维频谱的时–频几何结构。

## 方法
TF-MossFormer 在 STFT 域预测复谱实部/虚部：Conv2D+gLN 编码后，堆叠 B 个交替频率/时间建模块，每块含 Conv-SwiGLU、RMSGroupNorm 与卷积门控的局部–全局 MHSA。局部注意力为滑动窗（时间窗 wT、频率窗 wF），全局为标准 MHSA；门控为 Conv1D+Swish。消融比较三种布局（V1：局部→全局最优；V2 反向；V3 并行）及去掉门控的 V4。S/M/L 三档：D∈{96,128,128}，B∈{4,6,9}，参数约 6.0/16.9/25.4M。训练用 SI-SDR、AdamW、4 s 片段、16 ms 窗 / 8 ms hop。

## 实验与结果
在 WSJ0-2Mix（8 kHz）上，窗口 (wT,wF)=(31,7) 最佳，S 模型 SI-SDRi 22.61 dB。V1 优于 V2/V3/V4。与同规模对比：S 为 22.6 SI-SDRi（优于 TF-Locoformer(S*) 22.2、SPMamba 22.5）；M 为 24.0（优于 TF-GridNet 23.5、TF-Locoformer(M) 23.6）；L 为 24.4（优于 TF-Locoformer(L) 24.2、MossFormer2(L)+DM 24.1）。

## 结论
内容感知滑动窗局部注意力、局部先于全局的布局，以及卷积门控，共同带来多尺度上的 SOTA 分离表现，并保持相对有利的参数与算力。

## 点评
工作把“局部连续性 + 全局分组”落到 TF 双路径上，用可调窗替代固定卷积局部建模，门控再做特征筛选。强项是尺度扩展一致且相对 TF-GridNet 更省算力；评测仍集中在两说话人完全重叠的 WSJ0-2Mix，对更复杂噪声/混响场景的外推需另证。
