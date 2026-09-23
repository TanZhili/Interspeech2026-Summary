# Back to Ear: Perceptually Driven High Fidelity Music Reconstruction

- 论文编号：219
- 报告人：Kangdi Wang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26d_interspeech.pdf

## 问题
开源音频 VAE 常忽视听觉感知，相位与立体声空间重建差，导致瞬态抹糊与声像不准，难作专业级音乐重建前端。

## 方法
ear-VAE：卷积编码器 + 解码端 Transformer（RoPE）瓶颈；MS-STFT 判别器。损失含多尺度对数幅度、特征匹配、LS-GAN、弱 KL；提出相位相关损失（仅 LR）；重建前加 K-weighting；幅度在 MSLR 全通道监督、相位相关仅用 LR。两阶段训练：公开数据预训练 + 约 1 万小时内部高质量音乐继续训练。

## 实验与结果
相对 DAC、EnCodec、AGC、SAO，在 MuChin 与内部验证上 Mel/STFT 距离、ICPC/CCPC、SI-SDR、dbTP 与 MOS（4.70）全面领先。消融：相关损失、去 CQT 判别、K-weighting、Transformer 块均逐步抬升 SI-SDR；仅 M/S 相位监督反而有害。

## 结论
感知加权、相位相关与 MSLR 分流监督使开源音乐重建 VAE 达更优保真，尤其高频谐波与空间特性。

## 点评
把混音工程里的 K 计权与相关表思路写进重建目标，比单纯加大模型更对症。部分优势来自内部后训练数据，与纯开源基线对比需留意；作者也指出细微空间效果仍可能被衰减。
