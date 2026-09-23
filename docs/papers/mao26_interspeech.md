# Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior

- 论文编号：1248
- 报告人：Sicheng Mao
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/mao26_interspeech.pdf

## 问题
远场说话人日志（distant speaker diarization）受噪声、混响、说话人数变化与重叠语音影响，难度大。数据驱动方法依赖增强与大规模训练；模型驱动方法可利用多通道空间信息。neural FCASA 已对分离部分做贝叶斯建模，但对日志活动仍用非贝叶斯的交叉熵监督，未能把说话倾向先验纳入训练。

## 方法
在 neural FCASA 的多通道混合生成模型上，对说话人活动倾向 η_nt 引入 Beta(α,β) 先验，再由 Bernoulli(η_nt) 生成二值活动掩码 u_nt，与潜在谱特征、PSD 与空间协方差矩阵共同生成 STFT 域混合。推理端用编码器输出 PERT 参数化的 (m,λ)（模式与集中度）得到后验 Beta，替代原先对 η 的 Bernoulli 后验。分离与日志统一用变分推断最大化 ELBO：分离项与原模型相同；日志项含 E[log p(u|η)] 与两个 Beta 的 KL，均可闭式计算（digamma），从而用连续活动分数的正则化 ELBO 替代原始交叉熵。训练目标为加权和 L_sep^(1)+γ1 L_sep^(2)+γ2 L_diar^(1)+γ3 L_diar^(2)。推理时对 η 做 11 帧中值滤波并以 0.5 阈值二值化；分离仍用多通道 Wiener 滤波。

## 实验与结果
在 AMI（约 100 小时、8 麦圆阵、官方 train/dev/eval）上复现与对比 neural FCASA。WPE 去混响；STFT 窗 512、hop 160；N=6（5 说话人+1 噪声）；γ 均取 1.0。在 m∈{0.3,0.5,0.7}、λ∈{4,10} 等设置下，相对 baseline，DER 绝对降约 3%–4%（相对约 16%–30%），JER 绝对降约 4%–6%（相对约 20%–27%）；m=0.3, λ=4 总体最好（如 Forgiving DER 10.11 vs baseline 14.48）。参数仅多约 257，对速度影响可忽略。未评分离客观指标（AMI 无孤立参考）。

## 结论
用 Beta 说话人活动先验把 neural FCASA 的日志部分也纳入全贝叶斯变分训练，日志 ELBO 可闭式求，PERT 便于学超参，显著降低 AMI 上的 DER/JER。未来工作包括先验超参估计、更复杂对话活动模型，以及更好的分离以进一步助推日志。

## 点评
做法抓住的是“活动掩码二值监督过硬、缺少说话倾向/对话氛围先验”这一建模缺口，用共轭 Beta–Bernoulli 把日志损失改成带 KL 正则的连续倾向学习，与分离端 VAE 风格统一。相对常见 EEND 式交叉熵或多通道特征工程，强在先验可解释且几乎不加参。脆弱点在于先验形状被限制为单峰（α,β≥1）、超参需调，且评测按 10 秒块、与全录音 Pyannote 基线不完全可比；分离质量未量化，日志增益是否部分依赖分离仍不清晰。
