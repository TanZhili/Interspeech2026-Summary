# UFL-GAN: A Multi-Discriminator GAN for Unsupervised Speech Enhancement

- 论文编号：2565
- 报告人：Satvik Bejugam
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/bejugam26_interspeech.pdf

## 问题
多数深度增强需成对噪声–干净数据，真实场景难获得。现有无监督 GAN（如 MetricGAN-U、UnSE）或全局判别器收敛慢、难抓局部，或高噪下生成器信息不足。

## 方法
UFL-GAN：生成器为 NTVF，在对数幅度谱上估计幅度掩码并用噪声相位 ISTFT 重建；将预训练 APC（LibriSpeech 960h）表示经线性层拼入 CDF 块以补长时上下文。判别器双路：句级（时间池化后出单一分数）与帧级（每帧打分），采用 CMGAN 风格卷积头与 LSGAN（干净→1，噪声/增强→0）。训练仅用非成对干净与噪声，无参考重建损失。

## 实验与结果
VoiceBank+DEMAND：PESQ-WB 2.64、eSTOI 0.82、CSIG 3.99、CBAK 3.27、COVL 3.35、SI-SNR 15.95、DNSMOS 3.30；eSTOI/CSIG/CBAK/COVL 优于所列无监督基线，PESQ/DNSMOS 接近 QMixCAT，SI-SNR 接近 UnSE。消融：帧级略优于句级；双判别器 + APC 全面最优。

## 结论
作者认为句级与帧级对抗互补，外加 APC 辅助可在无成对数据下达到均衡的侵入/非侵入指标；未来拟扩展到混响与削波。

## 点评
针对“全局打分粗糙、局部打分易整段静音”的张力做双尺度判别，并用 APC 预测未来帧的归纳偏置抗噪，设计动机清楚。仍依赖非成对干净语料而非纯噪声域适应；与 QMixCAT 等伪标签路线比，GAN 先验路线在 PESQ 上未全面领先，优势在复合 MOS 与可懂度。
