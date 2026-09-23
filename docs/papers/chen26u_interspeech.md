# Latent-Mark: An Audio Watermark Robust to Neural Codec Compression

- 论文编号：1979
- 报告人：Yen-Shan Chen
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/chen26u_interspeech.pdf

## 问题
AudioSeal 等波形/谱域水印对传统 DSP 稳健，但神经编解码（EnCodec、SNAC 等）把不可感知波形扰动当 off-manifold 残差滤掉，一次 encode–quantize–decode 即可抹除水印。需要在编解码器不变潜空间中嵌入可检测痕迹。

## 方法
Latent-Mark：零比特（只标「有无水印」）。对波形加扰动 δ，经梯度优化在编解码器连续潜表示上沿秘密流形轴 vc 产生可检测方向偏移，并用 SDR 约束 ||δ||∞；扰动对齐码本质心方向以保可听度。引入 Cross-Codec Optimization：同时在多个代理编解码器上优化，捕捉共享潜不变量，以零样本迁移到未见黑盒编解码器。检测对潜序列投影均值做统计检验。

## 实验与结果
摘要称对未见神经编解码有稳健零样本迁移，对传统 DSP（噪声、幅度缩放、滤波、重采样等）仍有竞争力，并保持感知不可闻。正文在方法细节处截断，完整定量表未能读到。

## 结论
可读主张：把水印做成编解码器会保留的潜空间方向偏移，而非会被滤除的波形噪声；跨编解码联合优化是迁移关键。

## 点评
威胁模型切中「神经压缩≈强力去水印」这一新攻击面，零比特+测试时优化与静态编码器训练形成对照。强在流形对齐动机清晰；脆弱点在嵌入需白盒代理与逐条优化成本，以及零比特容量限制。抽取截断，数值从略。
