# CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents

- 论文编号：1273
- 报告人：Wen-Chin Huang
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26f_interspeech.pdf

## 问题
神经音频编解码（NAC）与基于其的 LLM-TTS 基准多偏重建质量与客观指标，少主观、少口音等非标准语音。口音相似度如何评、客观指标是否管用、听者口音是否引入偏差，尚缺大规模证据。

## 方法
构建 CodecMOS-Accent：从 VCTK 选 32 说话人、10 口音、160 真值句；9 个重合成 NAC（含低码率配置）+ 15 个开源 voice cloning TTS，共 4,000 样本。众包 25 听者、19,600 标注，三维 5 分：自然度 S-NAT、说话人相似 S-SPK-SIM、口音相似 S-ACC-SIM；并算 O-WER、O-SPK-SIM、O-ACC-SIM、O-UTMOS。

## 实验与结果
真值在 S-NAT 仅排第 9，但说话人/口音相似最高；低层 SpeechTokenizer 仍保留可感说话人与口音线索。系统级：S-SPK-SIM 与 S-ACC-SIM 相关 0.97（句级 0.75）；O-UTMOS 与 S-NAT 相关 0.96；O-SPK-SIM 对 S-ACC-SIM（0.90）甚至高于 O-ACC-SIM（0.81）；O-WER 与主观相关弱。同口音听者对 SPK/ACC（及全数据上的 NAT）给分更高（同口音偏差）。

## 结论
该数据集是作者所知对口音上 NAC/TTS 主观评估规模最大的工作之一；揭示说话人–口音强耦合、客观指标预测力，以及听者口音偏差。拟公开数据并用于训练更好 SQA、尤其口音相似度直接人标监督。

## 点评
把 ICL 式 voice cloning 的“说话人/口音克隆”拆成独立主观维，并系统对比重合成 vs TTS，填补了编解码基准缺主观、缺口音的空白。UTMOS 对 2020 年后系统仍高度相关，提醒“新架构≠绝对质量跃迁”。同口音偏差与听者以美式为主的构成，限制了“普遍自然”结论；口音嵌入指标未必优于说话人嵌入，说明口音客观度量仍需人标驱动。
