# Adaptive AVSR: Integrating Speaker and Environmental Embeddings for Robust Audio-Visual Speech Recognition

- 论文编号：2081
- 报告人：Tobias Bocklet
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/simic26_interspeech.pdf

## 问题
AVSR 虽在噪声下优于纯 ASR，但大规模泛化训练未必充分用上「当前说话人」与「当前环境噪声」信息；说话人嵌入用于 ASR 个性化较成熟，环境嵌入在 AVSR 中探索较少。

## 方法
以 Whisper 为骨干，上游自注意力 AV 融合（音视频拼接后分块）。从音频提取：
- **噪声嵌入**：四层注意力编码器联合回归 SNR + 四类噪声分类（babble/music/natural/sidespeaker），取编码器输出作嵌入，注入融合模块；
- **说话人嵌入**：X-Vector（优于 ECAPA），注入解码器前级。

比较三种注入：前缀拼接、额外交叉注意力、门控通道加权。噪声用门控最好，说话人用前缀最好。

## 实验与结果
LRS3 + VoxCeleb2 预训练/微调。相对无自适应基线，噪声门控平均相对降 WER 约 3.5%（∅ 4.42→4.26），说话人前缀约 3.2%；-5 dB 收益更大。联合噪声+说话人无额外收益——X-Vector 本身可约 90% 准确分类噪声，与专用噪声嵌入冗余。相对 AV-HuBERT base 平均相对降约 13.4%（∅ 4.92→4.26），多数噪声类优于 AV-Fusion / Whisper-Flamingo。

## 结论
噪声与说话人嵌入可显著提升 Whisper 系 AVSR，且最佳注入策略依嵌入类型而异；二者信息有重叠，简单叠加未必更强。

## 点评
系统比较三种注入位点/方式很实用，门控「按噪声调音视频权重」直觉清晰。有趣发现是 X-Vector 携带噪声线索，解释了说话人自适应在重噪也有效。局限：增益绝对值不大、依赖外部噪声/说话人嵌入质量，以及与 AV-HuBERT 的训练 SNR/目标差异可能影响公平性。
