# G-MaP-SE: Guided Speech Enhancement via GMM-Based Prior Matching

- 论文编号：2148
- 报告人：Yike Zhu
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26b_interspeech.pdf

## 问题
说话人嵌入条件可加强增强，但常需干净注册音；若直接从噪声语音抽嵌入，噪声与域偏移会使条件脆弱，甚至伤害增强。

## 方法
G-MaP-SE：离线在干净语音嵌入（冻结 ECAPA-TDNN，192 维，ℓ2 归一化）上拟合对角协方差 GMM 先验；推理时对噪声嵌入做温度 softmax 软匹配，用混合权重加权 GMM 均值得到匹配先验嵌入 \(e_{\mathrm{prior}}\)。经轻量门控融合注入 MP-SENet 编码器后的中间 TF 特征。训练时条件类系统均用干净目标嵌入作 oracle 条件以保证稳定；MaP 无训练参数，换数据集只需重拟合先验而无需重训骨干。默认 \(\tau=0.2\)，\(K=192\)。

## 实验与结果
在 VoiceBank+DEMAND 训练并做域内测试，跨域评 DNS 2020 无混响集。域内各条件变体差距较小；跨域上 G-MaP 相对 Noisy-Cond 全面提升，并明显缩小与 Oracle-Cond 的差距（如 WB-PESQ 2.794 vs Noisy-Cond 2.765，接近 Oracle 2.796）。用 DNS 干净数据重拟合先验可在不重训骨干时进一步适配目标域。余弦相似度分布显示 \(e_{\mathrm{prior}}\) 比 \(e_{\mathrm{noisy}}\) 更靠近干净嵌入。消融：\(\tau\) 约 0.2、\(K\) 约 192 较优。

## 结论
作者认为 GMM 先验匹配能在无注册音条件下 refinement 噪声嵌入，提升噪声与域偏移下的引导增强鲁棒性，并可即插即用换先验。

## 点评
把个性化/引导增强的“干净注册”瓶颈换成“干净嵌入分布先验 + 匹配”，部署负担小，且先验可按域替换。设计克制：冻结提取器防止嵌入空间漂移。局限是匹配可能分到次优原型（部分样本相似度不升）；VBD 规模限制先验多样性，域内增益有限，主要价值体现在跨域。
