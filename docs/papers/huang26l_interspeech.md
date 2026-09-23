# Unified Neural Speech Coding for Multiple Sampling Rates

- 论文编号：1641
- 报告人：Jiankai Huang
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26l_interspeech.pdf

## 问题
多数神经语音编解码器绑定单一采样率；跨 16/24/48 kHz 需外权重采样或多模型，感受野物理时长与频谱统计不一致导致共享量化困难。

## 方法
统一模型：共享 SEANet+LSTM 骨干与单一 RVQ；Sampling-Rate Adapter（SRAT）在波形端可学习对齐到内部 16 kHz 网格；Sampling-Rate Modulator（SRMT）做率条件仿射校准中间特征。三阶段渐进训练（单率→混合等）。

## 实验与结果
1.5 kbps：16 kHz ViSQOL/STOI/PESQ 约 4.21/0.920/2.369；24 kHz 4.22/0.919/2.353；48 kHz 4.14/0.889/2.750，与专用模型可比且单权重。去掉 SRAT/SRMT 或渐进训练均降质。MACs 约 2.1–2.6G，参数 19.65M。

## 结论
轻量率感知适配与调制可使一套权重原生服务多采样率，质量接近专用模型并简化部署。

## 点评
相对“外权重采样或分模型”，把时间网格与特征校准内化进网络，部署更干净。内部锚定 16 kHz 可能对最高频细节仍有折中；消融显示两组件缺一不可。
