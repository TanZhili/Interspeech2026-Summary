# Aleatoric Style Uncertainty Augmentation with GMM for Domain Generalization in Anti-spoofing

- 论文编号：582
- 报告人：Jin Li
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/li26g_interspeech.pdf

## 问题

反欺骗在未见攻击域上易退化。风格增强（MixStyle/DSU/CSU）用特征均值方差合成新域，但常假设批内风格单峰高斯；多域混合批（不同说话人、编解码、噪声、伪造痕迹）风格多模态，单高斯会低估变差、限制可分性。

## 方法

提出 ASU：在通道风格统计空间建 K 分量对角协方差 GMM，对线 EM 式更新混合权重/均值/方差；将 within-component 方差定义为偶然风格不确定性，与批级 DSU 不确定性相加后做重参数化风格扰动。插入 WavLM + multi-head factorized attentive pooling 管线的训练分支，以概率 p 启用，推理关闭。设定 p=0.5、K=7、λ=0.9。在 ASVspoof5 Track1 open 做反欺骗，Track2 与 ResNet221 ASV 联做 SASV；对比 DSU、CSU 与融合 SOTA。

## 实验与结果

Track1：WavLM+MHFA+ASU 在 Eval 上 minDCF 0.108、EER 3.96%，优于基线 4.99%、DSU 4.77%、CSU 4.64%，且优于若干更大/融合系统中的单模型结果。消融显示批级变差与 GMM 偶然不确定均贡献增益。K 与 λ 敏感曲线在 K=7、λ=0.9 最优。bootstrap 显示 ASU EER 分布显著更低。SASV：ASU 的 min a-DCF 0.118、min t-DCF 0.192、t-EER 4.23，优于基线与 DSU/CSU。

## 结论

用在线 GMM 建模多峰风格偶然不确定性，可在不增加推理成本、无需额外标签下提升反欺骗与 SASV 的域泛化。代码已开源。

## 点评

把“批统计单峰假设”点破，用轻量风格空间混合模型补偶然变差，契合反欺骗训练批天然多域的现实。强项是训练期即插即用、推理零开销。脆弱点是 K/λ 需调、对角协方差忽略通道相关，且增益依赖上游 WavLM+MHFA 与已有强增强配方。
