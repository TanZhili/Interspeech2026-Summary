# Assistive Technologies 1

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 13）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场覆盖人工耳蜗前端、声码化言语的房间适应、听力损失对话轮次感知、可穿戴无声语音、非规范语音个性化 ASR，以及脑机语音假体的低内存 CTC 解码。共同目标是在严格延迟、功耗与可达性约束下提升感知与交流。

硬件近端：因果卷积前端服务 CI 音素分类并在 STM32 上验证亚 10 ms；声学侧比较不同沉浸年龄对房间条件的适应，瞳孔指标跨组相似。感知侧显示听损老人判断话轮结束时更依赖音高运动而非时长/强度。新界面与解码：SoniSpeech 提供开放词表三模态无声语音数据；VI LoRA 不确定性引导难音素过采样；LightBeam 用延迟融合 LLM 将脑机 CTC 解码内存从约 320 GB 降到约 10 GB。

## 技术内容

### 耳蜗、房间适应与话轮感知

**Lightweight Convolutional Front-ends for Real-time Framewise Phoneme Recognition in Cochlear Implants**（论文 2689；Yuchu Guo）
比较 1D/2D 及标准、膨胀、可变形卷积前端配合序列后端。加卷积前端提升音素分类；STM32 模拟部署中 1D 满足亚 10 ms 延迟与低内存，膨胀卷积可预测扩展感受野。

**Adaptation to Room Acoustics in Understanding Vocoded Speech: A Comparison Between Listeners With Varying Immersion Age**（论文 113；Epri Pratiwi）
分块呈现诱导对房间声学适应。非声码化条件可懂度近天花板；声码化下可懂度随句变化。峰值瞳孔扩张跨沉浸年龄组相似，连续句变化模式也相近，提示房间适应机制或跨背景类似。

**Towards an understanding of prosodic cue weighting for turn-end classification in older adults with varying hearing abilities**（论文 2534；Lorenza Zaira Curetti）
老年听损与正常听力者仅凭韵律判断陈述问句是否结束。两组均高于随机；正常听力更依赖时长与强度，听损更依赖音高运动，提示听损重塑话轮结束线索权重。

### 无声语音、个性化 ASR 与神经假体解码

**SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces**（论文 1625；Ruidong Zhang）
基于声学传感眼镜的开放词表三模态数据：34 小时、18,000 语句，同步超声回波、有声音频与正面视频（有声/无声）。源自 SODA，含 5,356 词与全音素覆盖。CTC ResNet-34 基线无声开放词表 WER 26.3%。

**Data-Efficient ASR Personalization for Non-Normative Speech Using an Uncertainty-Based Phoneme Difficulty Score for Guided Sampling**（论文 776；Niclas Pokel）
用 VI LoRA 估计基础模型认知不确定，构造 PhDScore 驱动定向过采样。英德数据及一年间隔临床报告显示：VI LoRA 不确定比标准熵更对齐专家评估；PhDScore 捕捉稳定构音困难；引导采样显著改善受损语音 ASR。

**Lightbeam: An Accurate and Memory-Efficient CTC Decoder for Speech Neuroprostheses**（论文 2947；Ebrahim Feghhi）
非 WFST 的 CTC 解码器 LightBeam，约 10 GB RAM（相对约 320 GB WFST 方案），经延迟融合将 LLM 接入 beam search，在 Brain-to-Text '24/'25 达领先性能并开源。

## 本场要点

- CI 实时增强受因果与延迟约束，轻量 1D 膨胀卷积前端可部署。
- 声码化条件下房间适应可测，瞳孔努力跨沉浸年龄组模式相近。
- 听损改变话轮结束判断的韵律线索权重，更倚重音高。
- SoniSpeech 推动可穿戴开放词表无声语音基准。
- 音素级不确定性引导采样提升非规范语音个性化数据效率。
- 脑机语音假体解码可用延迟融合 LLM 大幅降低内存门槛。

## 覆盖核对

- 2689 | Lightweight Convolutional Front-ends for Real-time Framewise Phoneme Recognition in Cochlear Implants
- 113 | Adaptation to Room Acoustics in Understanding Vocoded Speech: A Comparison Between Listeners With Varying Immersion Age
- 2534 | Towards an understanding of prosodic cue weighting for turn-end classification in older adults with varying hearing abilities
- 1625 | SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces
- 776 | Data-Efficient ASR Personalization for Non-Normative Speech Using an Uncertainty-Based Phoneme Difficulty Score for Guided Sampling
- 2947 | Lightbeam: An Accurate and Memory-Efficient CTC Decoder for Speech Neuroprostheses
