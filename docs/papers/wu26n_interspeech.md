# Quantizer-Aware Hierarchical Neural Codec Modeling for Speech Deepfake Detection

- 论文编号：3212
- 报告人：Jinyang Wu
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wu26n_interspeech.pdf

## 问题
深度伪造语音常带细粒度、局部的合成伪迹，而 SSL 表征偏语义/上下文，可能冲淡这些线索。神经音频编解码器经 RVQ 形成粗到细的残差层次，伪迹未必均匀分布在各 quantizer；现有检测要么只用连续 encoder 特征，要么把 codec 当普通辅助流，缺少对 quantizer 层级结构的显式建模。

## 方法
在冻结 WavLM-Large（前 12 层 + Attentive Merging）的前提下，引入 EnCodec（Q=8、codebook 1024、维 128）离散码的可训练 embedding，再做层次感知聚合后与 SSL 晚期拼接融合。
- Method 1：Quantizer Mean Pooling，对各 RVQ 层均匀平均。
- Method 2（QAF-Static）：学习全局维度级权重矩阵 W∈R^{Q×D}，经温度 Softmax 得到 α_{q,d}，对每个 embedding 维跨 quantizer 加权求和，形成静态、输入无关的层次先验。
时间对齐后与 SSL 特征拼接再线性投影，送入单层 LSTM + 线性分类器。仅更新约 4.4% 额外参数（相对 SSL backbone）；对比 codec 冻结（codecF）与可微调（codecT）。

## 实验与结果
数据：ASVspoof 2019 LA、ASVspoof 5；主指标 EER。另在 CodecFake 上做跨 codec 族鲁棒性探查。
- ASVspoof5：AttM 基线 6.60%；Mean Pooling (codecF) 6.01%；QAF-Static (codecT) 5.68%（相对改进 13.9%）。
- 19LA：AttM 0.65%；QAF-Static (codecF) 0.44%；QAF-Static (codecT) 0.35%（相对改进 46.2%）。
- 所学 quantizer 权重非均匀，第一层贡献最大；CodecFake 上 Group B（紧凑 RVQ/低比特）相对 AttM-LSTM 更明显，其他 codec 族则大体相当，收益呈族依赖。

## 结论
显式建模 RVQ 残差层次、用轻量静态 quantizer 加权做 SSL–codec 融合，在冻结 SSL 时即可稳定提升检测；作者将动态、样本自适应的 quantizer 加权留作未来工作。

## 点评
核心是把“RVQ 粗到细结构”当作取证先验，而不是再堆一个复杂多视图网络；静态维度级加权可解释、训练稳，且与 AttM 的 SSL 层层次正交。脆弱处在于全局先验可能抹平不同生成机制下伪迹所在层的差异（CodecFake 已显示族依赖），且 codec-only 弱、必须依赖 SSL 上下文；跨训练 codec 分布的泛化仍是开放问题。
