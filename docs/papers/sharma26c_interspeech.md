# LavaSR: Fast and Flexible Audio Bandwidth Extension via Vocos

- 论文编号：2839
- 报告人：Yatharth Sharma
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26c_interspeech.pdf

## 问题
带宽扩展（BWE）要补全低带宽录音缺失的高频。扩散类方法（如 AudioSR）质量高但迭代采样过慢；许多 GAN 方案虽快，却常绑定固定输入/输出采样率对，或引入复杂多尺度管线，难以用单一网络覆盖任意上采样比。

## 方法
LavaSR 基于 Vocos 风格傅里叶域神经声码器：
1. 任意 8–48 kHz 输入先经 sinc 重采样到 48 kHz，得到保低频但无真实高频的基带波形。
2. 从 80-bin mel（n_fft=2048, hop=512）经 8 个 ConvNeXt 残差块（维 512，7×1 深度卷积 + FFN）预测复 STFT，再 iSTFT 得到波形。
3. **Linkwitz-Riley 风格频域 refiner**：用平滑多项式 crossover 掩码把原低频锚点频谱与生成高频线性混合，保证 crossover 附近幅度平坦、减轻相位/幅度尖刺。
训练损失含多分辨率 STFT、mel L1、多分辨率判别器（MRD）对抗损失与特征匹配；AdamW，batch 16。

## 实验与结果
VCTK（约 44 小时）训练；干净 48 kHz 随机下采到 8/12/16 kHz（sinc/ZOH/linear，可加量化噪声）再回采到 48 kHz。相对 Sinc、AudioSR、NVSR、AP-BWE：
- LSD（8/12/16→48）：Proposed 0.85 / 0.80 / 0.74，与 AP-BWE 持平或略优，优于 AudioSR/NVSR。
- ViSQOL 与 AP-BWE 接近（如 8→48 均为 3.51）。
- SI-SDR：Proposed 18.02 dB，介于 NVSR(14.68) 与 AP-BWE(18.77)。
消融显示 LR-inspired refiner（LSD 0.850）优于无 refiner / 砖墙 / Butterworth。效率：约 15M 参数；8 核 CPU RTF 0.0053（约 190×）；A100 batch32 时 RTF≈0.0001（万倍实时吞吐）。OOD 采样率上 LSD 随输入带宽单调下降。

## 结论
作者给出单一网络覆盖任意输入采样率的 Vocos 式 BWE，在频谱/感知指标上接近强 GAN 基线，同时达到极高吞吐；未来工作提到音乐、噪声场景与自适应 refiner。

## 点评
做法本质是把「任意率 BWE」改写成固定 48 kHz 网格上的频谱补全，再靠 crossover 把可靠低频钉死——工程上很聪明，也解释了为何能避开 ratio-specific 架构。相对扩散方法，质量–速度权衡是明确卖点；相对 AP-BWE，用单流复 STFT 头换来巨大 CPU/GPU 加速，但 SI-SDR 仍略逊，说明相位/波形保真仍是单头简化的代价。脆弱点包括：主评测偏干净语音、训练锚点采样率有限，且 refiner 依赖正确的低频锚点——输入低频本身已失真时收益可能下降。
