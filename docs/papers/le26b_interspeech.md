# ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning

- 论文编号：1077
- 报告人：Kiet Anh Hoang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/le26b_interspeech.pdf

## 问题
越南语标注稀缺，需要公开、可部署的 SSL；既有 wav2vec2-Vi 延迟高，大规模工作权重未公开。BEST-RQ 搭配 8× 下采样易因 mask 与编码器不同步而掉点。

## 方法
ViP-VL：BEST-RQ + ChunkFormer，78M 参数，8× 时间下采样。用声学堆叠（15 帧窗、步长 8，拼接优于平均）与感受野对齐同步 mask 流形；在 10 ms filterbank 上先 mask，再按“至少 80% 组成帧被 mask”判定下采样帧是否 mask，有效时间 mask 约 45%。在约 17,000 小时无标注越南语上预训练。下游：ASR（VLSP 等）、情感（ViSEC）、方言（ViMD）、说话人验证（VoxVietnam）。

## 实验与结果
LibriSpeech 验证：ViP-VL 平均 WER 9.7，优于未对齐的 8× BEST-RQ（11.9），对齐 2× 量级。越南 ASR 平均 WER 13.76，优于 Wav2vec2-Large-Vi（17.89）与 PhoWhisper-Large（14.09）等（同范式比较）。SER UA 74.45%；方言区域/省级 F1 93.24% / 57.17%。低资源 ASR 曲线显示预训练相对从零训练优势随标注减少而增大。权重与实现开源。

## 结论
在高压缩 SSL 中，mask–下采样同步与感受野对齐和数据规模同等重要；按此训出的公开 ViP-VL 在多项越南语任务上达 SOTA 级表现。

## 点评
把“8× 掉点”归因到同步错误并用堆叠/阈值 mask 修掉，比一味堆数据更有方法贡献。公开权重填补社区缺口。与用远更大数据/监督的系统对比时需注意设定差异；省级方言仍难，说明细粒度变体仍是瓶颈。
