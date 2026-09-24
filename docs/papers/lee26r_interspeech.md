# GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition

- 论文编号：1938
- 报告人：Jiwon Lee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lee26r_interspeech.pdf

## 问题
Silent EMG→语音信息稀疏，仅最小化声学重建误差难保证语义可懂度；现有 ETS 在 silent 测试上 WER 常超 25%。

## 方法
GETS：DiffWave 骨干的 EMG 条件 mel 扩散生成器 + SSR 分类器引导。训练用 voiced EMG 与 DTW 对齐的 silent 特征条件去噪（classifier-free）；推理时 silent EMG 直接编码，并用 MONA-LISA SSR 预测文本 ˆt，以微调 ASR（AVEC 音频变体）的 ∇ log p(ˆt|xt) 做 classifier guidance（ω1=2.5，ω2=1.5，t≤270）。HiFi-GAN 声码。

## 实验与结果
Gaddy & Klein 单说话人：1285 平行对 + 5470 非平行 voiced。Silent 测试 Whisper WER 11.89%（vs Gaddy 25.74、SU-ETS 26.29、diff-ETS 32.1）；DeepSpeech 21.32%。词/停顿起止 MAE 与能量 RMSE 具竞争力；ω1=0 时时间对齐与 WER 明显变差，说明非纯 TTS。打乱实验：EMG-shuff 能量崩坏远重于 Text-shuff。消融：去 ω2 时 WER 升至 32.78%。

## 结论
SSR 语义引导可在不牺牲 EMG 固有韵律线索的前提下大幅提升 silent ETS 可懂度，达到新 SOTA。

## 点评
把 LipVoicer 式 ASR 引导迁到 EMG，直击「编码器容量不够」的旧瓶颈。依赖 SSR/LLM 精修文本质量，引导上限与 MONA-LISA（silent WER 8.93%）绑定；单说话人数据也限制泛化结论。
