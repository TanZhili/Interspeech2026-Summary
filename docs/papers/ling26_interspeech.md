# TGTSE: Token-Guided Target Speaker Extraction with Visual Cue

- 论文编号：1710
- 报告人：Zhong-Qiu Wang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ling26_interspeech.pdf

## 问题
音视 TSE 常用唇部连续嵌入条件化，但视觉与声学模态异构、对齐不稳，嵌入只是相关特征而非生成必要变量；希望用与语音生成更紧耦合的离散语义 token 作时序对齐线索。

## 方法
TGTSE 两阶段：token predictor（DNN1）以冻结 3D-ResNet18 唇特征 + 混合物 STFT 幅度，经 Transformer 预测 WavLM-KM 伪标签（WavLM-Large，K-means）；再将预测 token 经可训练码本嵌入，条件化 extractor（DNN2）——TF-GridNet 或 MossFormer2，损失为负 SI-SDR。伪标签用 LibriSpeech 子集重做；提取网络与码本端到端训练。

## 实验与结果
VoxCeleb2-2Mix / LRS2-2Mix（SNR −10–10 dB）。Oracle token 消融：K=128 最佳；token 准确率约 60% 已有合理提取。TGTSE(MossFormer2) 在两集上 SDR 15.2/16.2、SI-SDR 14.8/15.7；相对 AV-TFGridNet，TGTSE(TFGridNet) SDR/SI-SDR 分别提升约 0.7/0.9 dB。跨域 LRS3、TCD-TIMIT、Grid 上亦全面优于同骨干 AV 基线。

## 结论
将唇动映射为离散语义 token 再引导提取，可缩小跨模态鸿沟，在基准与跨域集上持续优于常规 AV-TSE。

## 点评
做法把 AV 条件从“相关视觉嵌入”换成“语音侧离散语义”，对齐与监督都更像 ASR/生成式序列问题。强在对 backbone 可插拔且跨域仍涨；弱点是依赖伪标签质量与 token 预测准确率——K 增大预测变难，而真实噪声视觉下 token 错误会直接传导到提取。
