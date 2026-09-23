# Audio-Visual Feature Reconstruction Pretraining for Noise-Robust Emotion Recognition

- 论文编号：605
- 报告人：Ivan Halim Parmonangan
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/parmonangan26_interspeech.pdf

## 问题
音视频情绪识别在背景噪声、混响、丢帧等真实腐蚀下，脏模态可能主导融合并压制干净模态；现有跨模预训练多对齐语义，缺少显式去噪，Transformer 对长序列又二次昂贵。

## 方法
冻结 EAT（音频）与 Timesformer（视频）提特征；两阶段自监督重建：先单模 Mamba2 编码器从腐蚀特征重建干净特征（80 epoch），再冻结编码器训交叉注意力融合 + Mamba2 解码器（200 epoch，MSE + GradNorm 调模态权重）。下游对富化后的单模 token 做 attention pooling + cosine 分类器。预训练用 LRS2+FSDNoisy18K/AIR 等；下游 RAVDESS，噪声集与预训练不重叠。

## 实验与结果
无预训练：干净音频约 77%、视频 93%；噪声音频可落到 39–70%。单模重建预训练改善噪声表现；多模融合预训练在多样噪声/干净视频组合上进一步稳定增益，显著检验优于无预训练与仅编码器预训练。相对可比 Transformer 解码器，Mamba2 方案 FLOPs 略低。

## 结论
显式跨模特征重建预训练可提升噪声下情绪识别鲁棒性，并避免脏模态拖累干净模态，同时保持高效序列建模。

## 点评
把“对齐”换成“从脏重建干净”，直接对准部署噪声。强处是腐蚀类型丰富且预训练/下游噪声源隔离；脆弱处是下游仍分模分类、RAVDESS 表演语料，以及随机划分非说话人独立可能偏乐观。
