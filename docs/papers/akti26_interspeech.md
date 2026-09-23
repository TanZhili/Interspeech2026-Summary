# Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS

- 论文编号：1159
- 报告人：Seymanur Akti
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/akti26_interspeech.pdf

## 问题
Lombard 效应（更大音量、更高音高、更慢语速、更平谱倾斜、更清晰发音）可提升噪声下可懂度，但现代 TTS 多训在非 Lombard 风格，缺少对发声力度与构音的统一、可解耦控制，尤其超构音建模不足。

## 方法
基于 Matcha-TTS（流匹配 + MAS 时长）与 Vocos 声码器。用 Expresso 的 default/enunciated/fast/projected 风格构造构音 β 与发声力度 α 伪标签（并入 LJ Speech 作中性扩充，约 11h+）。各属性映射到 32 维连续嵌入，与说话人嵌入拼接；双注入：编码器侧控时长/语速，解码器 U-Net 侧控谱–韵律。推理 α、β∈[0,1] 连续插值，并可按词赋不同 β 做局部强调。基线为 RMS 增益 + 线性时拉伸。

## 实验与结果
Harvard Sentences 上，提高 β 显著降 WER、升 MVD，α 主要抬谱倾斜；相对基线更有效。噪声实验（餐馆 babble、叠语、白噪，SNR=10/5/1，RMS 归一）：构音持续降 WER；发声力度在固定 SNR 下对 WER 帮助有限但对 SII 有增益；联合缩放在 SNR=1 时尤其有益。CMOS（10 人）：自然度 1.97±0.32、噪声可懂度 1.13±0.24（相对基线/中性）。另支持词级强调。

## 结论
双轴连续控制可模拟 Lombard 相关清晰度与力度变化，并在噪声听感上带来可懂度增益；词级控制可针对性加强片段。

## 点评
把 Lombard 拆成“构音 vs 力度”并分别打进时长与声学通路，比单一风格标签更贴真实适应机制。伪标签依赖 Expresso 离散风格到连续轴的映射，数据规模与说话人数有限，极端 α 还会偏离 ASR 分布；噪声评测做了 RMS 归一以排除简单响度作弊，设计合理。
