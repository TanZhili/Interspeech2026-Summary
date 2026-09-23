# Self-adaptive Gradient Conflict Mitigator for Continuous-Time Diffusion Models

- 论文编号：3059
- 报告人：Takumi Hirose
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/hirose26_interspeech.pdf

## 问题
连续时间扩散训练目标是对时间积分的总损失，实际按随机采样的单时刻 \(L_t\) 更新；不同时刻梯度不对齐会导致梯度冲突，拖慢收敛或损害最终性能。

## 方法
提出 DELLBO：对一阶近似的损失下降量取所有概率测度下的最小内积，作为可处理下界。由 Sion 极小极大定理推出最优更新方向为凸包中距原点最近点的单位方向。据此提出 SGCM：用可学习密度 \(m_\alpha(t)=\min\{\lambda s(t),1\}\)（\(s(t)\) 为经验 SNR，\(\lambda=\mathrm{softplus}(\alpha)\)）重加权单时刻梯度，仅增一个可学习参数。

## 实验与结果
在 SGMSE+ 骨干上，WSJ0-CHiME3 与 VoiceBank+DEMAND 对比基线及 SNR / Max-SNR / Min-SNR 加权。训练过程中 SGCM 的 \(\Omega(\mu)\) 最小，最接近理论最优方向。WSJ0-CHiME3 上五项指标均最优（如 PESQ 3.04 vs 基线 2.96）；VBD 上整体最优或接近最优（PESQ 2.85 vs 2.77）。启发式加权往往更差甚至崩溃。

## 结论
作者认为凸包几何刻画了连续时间扩散中的梯度冲突；SGCM 以极低开销逼近最优更新，在语音增强上一致提升质量。

## 点评
贡献偏优化理论：把“时刻间冲突”形式化为 DELLBO 并给出可落地的单参数重加权，与随意 SNR 启发式形成对照。实验排序与 \(\Omega(\mu)\) 一致，论证闭环。局限是经验假设（均值方向近似不变）仅用于动机密度形式；验证主要在 SGMSE+ 增强，向更大曲率感知或非语音扩散任务的推广仍待检验。
