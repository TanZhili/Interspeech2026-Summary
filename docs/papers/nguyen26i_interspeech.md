# Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition

- 论文编号：3465
- 报告人：Tung X. Nguyen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26i_interspeech.pdf

## 问题
语码转换（CS）错误集中在嵌入语与切换边界（POI）；标准微调缺少针对这些易混片段的显式信号。

## 方法
CS-NMG：用冻结种子 ASR 的 N-best 定位 POI，仅替换 POI 构造 near-miss，并用 LLM（Gemini）离线扩展替换候选；经声学边际、音素距离、文本距离三层门控保留“难但合理”负例。Whisper-small + LoRA：POI 加权 CE（WCE）锚损失 + 多负例 InfoNCE 式对比排序（长度归一化分数）。推理仍为标准 ASR。

## 实验与结果
CS-FLEURS cmn-eng 与 ViMedCSS vie-eng：WCE+CL（tri-level）相对 CE 约降 2+ 点 WER/PIER（如 cmn-eng 16.67/17.25→14.06/15.10；vie-eng 24.72/21.95→21.87/18.74），优于 WCE、MWER 与仅 N-best 负例。消融：LLM 扩候选需门控才稳定；三层门控整体最优（约 3.8 NM/utt）。

## 结论
面向 POI 的 near-miss 对比训练比单纯上权 POI token 更能抑制跨语混淆，在总体 WER 与 PIER 上一致改进且无增推理模块。

## 点评
把偏好对齐落到声学合理的局部负例，切中 CS 错误分布。依赖外部 LLM API 与 prompt，离线成本与可复现性是短板；目前两语对、单骨干，门控阈值跨脚本迁移需谨慎。
