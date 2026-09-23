# IACC-HuBERT: Intelligibility-Aware Channel Conditioning of HuBERT Frontend for Dysarthric Speech Conformer ASR

- 论文编号：2375
- 报告人：Hemant Kumar Kathania
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/sapkota26_interspeech.pdf

## 问题
现有语音基础模型多在正常语音上预训练，难以刻画构音障碍（dysarthria）的可懂度差异与说话人变异；全量微调代价高，而仅用 SSL 前端仍不足以适配病理语音。

## 方法
在 TORGO 上按说话人可懂度均值分成 A–D，控制说话人另成一类。用 utterance 级 HuBERT 均值特征训可懂度分类器（LOSO，约 89–95% 验证准确率），取 128 维嵌入。冻结 HuBERT-large，在间隔的 Transformer 层插入 **FiLM** 或 **Gated-FiLM** 通道调制（scale/shift，门控控制强度），仅训 conditioner（约 6.3M / 15.78M 参数）。条件化特征再送入 ESPnet Conformer 编码器 + Transformer 解码器，联合 CTC/注意力训练，LOSO 评估。

## 实验与结果
全体构音障碍说话人平均 WER：FBANK 54.0%、HuBERT 28.9%、FiLM-only 21.3%、Gated-FiLM 21.0%。中重度组增益更大（如 Group B：HuBERT 44.5% → Gated-FiLM 34.8%；Group D：43.6% → FiLM-only 30.3%）。消融显示相对更新 HuBERT 末两层（25.2M），条件化参数更少且常持平或更好。与多篇 LOSO 文献比，平均 WER 最低（21.3%/21.0%）。

## 结论
用可懂度嵌入做通道条件化，能在少训参数下为 Conformer ASR 生成严重度感知的 HuBERT 特征，整体优于裸 HuBERT/FBANK 及部分既有 LOSO 系统。

## 点评
抓的是病理语音“严重度条件分布偏移”，用 FiLM 把旁路可懂度信号注入冻结 SSL，比大面积微调更省参。可能脆弱点：可懂度标签来自说话人级均值、分类器误差会传导；TORGO 说话人极少，LOSO 方差大；重度组有时 FiLM-only 优于门控，说明门控并非普适。
