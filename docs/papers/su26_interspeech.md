# Robust LLM-based Audio-Visual Speech Recognition with Sparse Modality Alignment and Visual Unit-Guided Refinement

- 论文编号：1277
- 报告人：Fei Su
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/su26_interspeech.pdf

## 问题
LLM 系 AVSR 常独立投影音视频或浅融合，跨模态对齐弱、互补交换不足，且把连续特征喂给 LLM 增加计算与噪声敏感。需要可控的跨模态交互与更稳的 LLM 精炼。

## 方法
提出 **AVUR-LLM** 两阶段：
1. **Sparse Modality Alignment (SMA)**：在 Whisper 音频编码器上层稀疏插入块，视觉作 query、音频作 stop-gradient key/value，校准视觉而不扰动预训练音频通路。
2. **Adaptive Modulated Fusion (AMF)**：解码器中用声学探针注意力熵估计 token 级可靠性，门控视觉注入幅度与方向（tanh）。
3. **Visual Unit-Guided Refinement (VUR)**：对 AV-HuBERT 中层特征 K-means 离散化并 run-length 压缩，作视觉 token 提示；LoRA 微调 LLaMA2-7B 对 N-best 列表打分重排。

## 实验与结果
LRS3（30h/433h）及 +VoxCeleb2（1759h）。AV 干净：433h WER 0.75%，1759h 0.68%，优于 Whisper-Flamingo、Llama-AVSR、MMS-LLaMA 等。0 dB babble 相对 MMS-LLaMA 约 37% 相对降（1.7% vs 2.7%）。消融：AMF+VUR 是噪声鲁棒主因，SMA 再补一截；视觉离散取第 12 层、K=2000 最佳。

## 结论
稀疏对齐 + 置信门控融合 + 视觉离散单元引导的 LLM 重打分，可在干净与噪声下全面提升 LLM-AVSR，并控制对 LLM 的负担。

## 点评
三条线分工清楚：编码器侧稳对齐、解码侧按声学不确定性调视觉、LLM 侧用紧凑视觉单元重排。强在干净 SOTA 与重噪收益；脆弱点在两阶段管线与离线码本、N-best 依赖，以及文中注明各工作 babble 来源不一，跨文绝对数字需谨慎对比。
