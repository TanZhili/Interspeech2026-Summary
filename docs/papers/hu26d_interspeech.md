# TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation

- 论文编号：1307
- 报告人：Chenda Li
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/hu26d_interspeech.pdf

## 问题
边缘部署的语音分离模型参数往往不大，但算力（GMACs/s）很高；简单缩隐藏维度会伤容量。作者要用稀疏 Mixture-of-Experts（MoE）在几乎不增加推理算力的前提下扩大容量。

## 方法
先提出 TF-Conformer：用 mel-band 切分替代 BSRNN 式手工子带，并用 Conformer 替代 RNN，在频率维（F-module）与时间维（T-module）交替建模。再把两侧 Conformer 的 FFN 换成 top-J 稀疏 MoE（默认 J=1）：对均值池化序列描述子做路由，整段共享选中专家；辅以 balance loss。T-MoE 按 mel 子带路由，F-MoE 按时间帧路由，合称 TF-MoE。默认 N=32、R=6、K=80 mel bands，SI-SNR+PIT 训练。

## 实验与结果
Libri2Mix 16 kHz：BSRNN 4.2 G / 13.9 dB SDR；TF-Conformer 4.1 G / 16.4 dB；TF-MoE（E=12）4.1 G / 17.7 dB SDR、17.2 SI-SDR，相对 BSRNN +3.8 dB SDR。消融显示 RNN < Conformer < MoE；E 从 3→12 提升，到 24 反而降约 1.1 dB。路由可视化显示 T-MoE 专家按频带特化、F-MoE 按说话人/发声模式随时间切换。

## 结论
TF-MoE 通过时频双维稀疏专家，在约 4.1 GMACs/s 下把新增参数有效转成分离增益，适合边缘部署；路由分析表明两维专家分别承担频带结构与时变说话人/交叠模式的特化。

## 点评
抓的是“参数便宜、算力贵”的部署错配，用 sequence-level top-1 路由把 MoE 开销压到几乎为零，比只做时域 MoE 的路线更贴合 band-split 分离结构。E=24 退化说明路由可学性是上限；若部署时专家加载/调度有额外开销，论文里的“几乎零算力”还需落到具体硬件实现上验证。
