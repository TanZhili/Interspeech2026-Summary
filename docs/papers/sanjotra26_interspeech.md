# Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech

- 论文编号：2203
- 报告人：Shekhar Nayak
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanjotra26_interspeech.pdf

## 问题
UTMOSv2、DNSMOS 等 O-MOS 多在干净/去噪连续语音上训练；对 in-the-wild 离散 token TTS 的生成伪影（幻觉、韵律倒置）可能“听不清但谱面光滑”，客观分与人工自然度可能脱节。

## 方法
四系统对照（文本与说话人固定）：SYS-A StyleTTS 2（连续干净）、SYS-B MQTTS+语义编码器（原始 ITW）、SYS-C 在 A 上加 MUSAN 泡泡噪声且与 B 的 NISQA 对齐、SYS-D 真录音。耳机筛选听测共 768 条自然度评分；评 UTMOSv2、DNSMOS P.835/Pro、PLC-MOS。

## 实验与结果
人工：D>A>B≈C（B/C ΔMOS=0.10，p=0.14）。文件级相关：A 上 UTMOSv2 r=0.51（p<0.01），B 上跌至 −0.01（n.s.）；Steiger 检验确认崩溃显著。DNSMOS 等对加性噪声惩罚更重（OVRL B 3.06 vs C 2.64），与人工等价相悖。B 中 7/32 文件人工 MOS<2.5 但 UTMOSv2>3.8（acoustic camouflage）。

## 结论
在 MQTTS 类 ITW 离散合成上，现行神经 MOS 不宜单独作自然度代理；建议与 ASR WER 等语义指标组合，并建设针对 ITW 生成伪影的指标。

## 点评
用加性–生成配对把“罚错类失真”钉死，比单纯报 OOD 相关下降更有说服力。结论强度受单架构（MQTTS）限制；camouflage 样本说明表面质量指标会主动误导系统排序。
