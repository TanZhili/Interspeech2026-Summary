# Mixture of Spectral Experts for Audio Deepfake Detection

- 论文编号：661
- 报告人：Zhe Li
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/qiu26_interspeech.pdf

## 问题
神经语音合成越来越自然，伪造痕迹更难察觉；SSL 预训练模型虽有强表征，但对幅度不规则、相位失真等低层物理线索利用不足；现有频域特征或波形编码器与 PTM 融合时，相位建模不够，且与高层上下文存在表征鸿沟；全量微调成本高，常规 PEFT 也未显式控制预训练奇异方向的贡献。

## 方法
框架由 Frequency Audio Encoder（FAE）与 Mixture of Spectral Experts（MoSE）组成，骨干为冻结的 WavLM-Large。FAE 对 STFT 取对数幅度，并以 sin/cos 表示相位（训练时加随机相位扰动），经 1D 卷积与 depthwise separable convolution 得到与 PTM 同维的谱表征 P。MoSE 作用于 Transformer FFN 权重：对 W_l 做 SVD 后冻结奇异基 U、V，仅用 K 个专家对中间矩阵 Σ 做低秩更新（I+BA），组内共享可训参数（G=2，K=4）；路由按时间平均池化后的门控加权专家输出。各层输出可学习加权得到 Z_final，再与 P 做 cross-attention 融合后分类。训练用加权交叉熵（bonafide 0.9 / spoof 0.1），约 4.8M 可训参数。

## 实验与结果
在 ASVspoof 2019 LA 训练，评测含 2019 LA 与跨集 2021 LA/DF、In-the-Wild。2019 LA：EER 0.29%、min t-DCF 0.0081，优于表中对比系统。跨集 EER：2021 LA 2.68%、2021 DF 3.89%、ITW 9.25%。消融：去掉 FAE→0.51%，去掉 MoSE→0.45%，两者都去→0.72%，纯 WavLM 基线 1.46%。K=4、G=2 最优；可学习路由温度约 0.9831 时 21 LA EER 最低。

## 结论
FAE 提供显式幅度–相位线索，MoSE 在 SVD 域对冻结 WavLM 的 FFN 做专家化低秩适配，在 ASVspoof 2019/2021 与 In-the-Wild 上取得有竞争力的表现与较强跨集泛化；在对比系统中于 2021 LA 与 ITW 上 EER 最优，2021 DF 上仍具竞争力。

## 点评
抓的是“合成/声码器留下的谱与相位物理痕迹 + 如何在不破坏 SSL 先验下把骨干拧向这些痕迹”两类问题。相对只堆 LFCC/CQT 或普通 LoRA/MoE，把 PEFT 放进 SVD 中间矩阵并按组共享，更直接对准频谱奇异方向上的伪造偏移。强依赖 ASVspoof 类分布与固定 4 秒裁剪；跨集 DF 上略逊于 MoLEx，说明对压缩/深度伪造变体仍可能脆弱。
