# Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation

- 论文编号：2414
- 报告人：Shengfan Shen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shen26d_interspeech.pdf

## 问题
零样本 TTS 客观指标（WER/SIM/预测 MOS）在 SOTA 区间易饱和、与人类排序相关弱；主观评测贵且难复现。

## 方法
I2D：对每个模型做多轮自条件合成——上一轮输出作下一轮参考，最多 10 轮；强模型退化慢、弱模型快，从而拉开差距。跨轮聚合（均值/加权）客观分。在 LibriTTS、Seed-TTS-Eval、CV3-Eval 上评 11 个 AR/NAR/混合系统，并做人机相关分析。

## 实验与结果
第 1 轮分数高度拥挤、UTMOSv2 等系统级 SRCC 弱（摘要称约 0.118）；迭代聚合后 UTMOSv2 系统级 SRCC 升至约 0.464。第 10 轮 utterance/system 级相关整体增强。可观察内容/说话人/自然度/情感克隆轨迹差异。

## 结论
作者认为迭代自条件退化可放大模型差、提升客观指标可区分性与人机对齐，适合自动化零样本 TTS 评测。

## 点评
评测协议创新：用误差累积当“压力测试”。代价是算力×迭代次数，且强依赖首轮参考质量；可能偏爱“抗自条件”而非单次生成最优的系统。与 VoiceMOS “zoomed-in”问题直接对话。
