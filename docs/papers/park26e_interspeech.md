# Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs

- 论文编号：2005
- 报告人：Taejin Park
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26e_interspeech.pdf

## 问题
流式多说话人 ASR 需同时权衡精度、时延、显存与是否可微调；社区缺少在同一对开源流式 ASR/diarization 骨干上对架构范式的受控对比，且 SOT 短训长推时存在转写–RTTM 标签置换对齐难题。

## 方法
基于 Nemotron Speech streaming ASR 与 streaming Sortformer v2.1，归纳四类架构：Cascaded（词时间戳映射 diarization）、Masked Input（按说话人掩码特征并行解码）、WL-SOT（单实例 + Arrival-Order Speaker Cache / speaker kernel，提出 PI-DTW + 说话频率代价对齐 SOT 与 RTTM）、SSA Diarization Conditioning（多实例条件解码）。在 CH109、Mixer6、AMI IHM/SDM 上报告 cpWER（含 oracle diarization），并在 OpenASR 单说话人集上测退化。

## 实验与结果
多说话人平均 cpWER（oracle diar / 系统 diar）：Cascaded 45.25 / 42.27，Masked 30.06 / 34.77，WL-SOT 28.66 / 33.46，SSA 16.18 / 23.36，SSA 最优。OpenASR：SSA 平均 WER 7.44，接近基座 7.16；WL-SOT 严重退化至 16.95。流式 diarizer DER 在各集约 5–20%。

## 结论
形式化流式多说话人 ASR 的架构权衡；当前 diarization conditioning（SSA）精度领先且单说话人退化小；PI-DTW 为扩展端到端 WL-SOT 扫清标签对齐障碍，但 SOT 路径仍需更大数据与原生说话人标记。

## 点评
同一骨干上的四象限对比，对“无微调 API / 数据稀缺 / 要精度”的选型很实用。WL-SOT 单说话人崩坏说明序列化训练仍伤通用识别；结论偏工程地图而非新 SOTA 叙事，与正文定位一致。
