# Causal Redundancy in Speech Representations: The Hydra Effect and Limits of Sparse Disentanglement in WavLM

- 论文编号：3316
- 报告人：Patalee Narasinghe
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/narasinghe26_interspeech.pdf

## 问题
WavLM 等 SSL 语音模型如何编码低层声学属性仍不清晰；线性探针只给相关证据，原始神经元又高度多义（polysemantic），稀疏自编码器在语音连续冗余域能否真正因果解耦尚待检验。

## 方法
在 WavLM-Base+ 上：用线性探针与 SHAP 做层/神经元定位；训练 JumpReLU SAE（8192 latents）试图解耦；对 top 重要 latent 做消融测因果；再用 INLP 擦除整段线性子空间。声学标签为 openSMILE GeMAPS（F0、Loudness、AlphaRatio 等），数据为 RAVDESS + CREMA-D + TIMIT，说话人无关划分。

## 实验与结果
声学特征在早期层（尤其 Layer 1）线性可解，打乱标签基线很低。原始神经元与 SAE 均见 Hydra 效应：去掉 top-50 重要维后 Pitch/Loudness 的相对 R² 仍约 97–99%。INLP 子空间擦除可对目标特征造成 >94% 的 R² 下降；Loudness 擦除高度选择性（旁路跌 <1.5%），而 spectral 特征之间交叉跌幅 >75%，说明共享子空间。

## 结论
连续声学特征在 SSL 中呈分布式但可在子空间层分离；离散 neuron/latent 消融不够，需要子空间级干预做机制解释。

## 点评
把 LLM 式 SAE 可解释性搬到语音后，用 Hydra 效应点出连续声学流形的冗余本质，再用 INLP 证明“可分离≠可单点消融”。强在因果干预设计清晰；脆弱在主要看 Layer 1 与线性探针可读性，非线性纠缠与更高层语义未充分覆盖。
