# MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data

- 论文编号：1461
- 报告人：Jing Yao Li
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26f_interspeech.pdf

## 问题
神经 TTS 短句质量高，长文易韵律漂移、说话人不一致与句界伪影。压缩序列、加长上下文或朴素分句拼接各有分辨率损失、硬掩码或需改架构/重训的问题。

## 方法
MagpieTTS-LF：纯推理期扩展 MagpieTTS（Koel-TTS 式编解码器 + 神经编解码 token）。(1) 软注意力先验：在上一时刻最高注意力位置邻域赋固定权重，远处给 \(\varepsilon>0\)，以 \(\lambda\log P_t\) 加到 softmax，引导单调对齐且保留远距上下文；(2) 有状态分块：跨句传递历史文本 token、对应编码器隐状态与注意力跟踪 \(\tau\)；(3) 历史文本编码支持篇章级韵律规划。无需长文重训或改结构。

## 实验与结果
自建 Long-Form HifiTTS（约 20 段 3–4 分钟 MLS 拼接）上对比 XTTS、Qwen3-TTS、VibeVoice。WER/CER 最低（0.025/0.012）；WavLM SSIM 最高且最稳；句界能量跳变 14.04 dB，综合 PBD 最优。全程说话人相似与 UTMOSv2 更稳、方差更小。超参：\(\varepsilon=0.1\)，\(w=(0.2,0.8,1.0,0.8,0.2)\)，\(\lambda=1.0\) 等。

## 结论
作者认为推理期软先验 + 跨块状态传递即可在不训练长文数据的情况下显著改善长距可懂度、韵律连贯、说话人一致与边界自然度，并可推广到其他分块编解码 TTS。

## 点评
价值在于“部署即用”：不碰权重，专治分句拼接的边界能量不连续与上下文断裂。软先验相对二值流式掩码更温和。局限是依赖 MagpieTTS 训练期已有的 CTC/注意力先验归纳；对非编解码器或非 AR 架构需再适配；评测长文为拼接构造，真实叙事节奏多样性可能更复杂。
