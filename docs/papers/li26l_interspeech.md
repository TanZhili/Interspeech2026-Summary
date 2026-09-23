# HFMSE: Harmonic-Guided Speech Enhancement with Flow Matching

- 论文编号：722
- 报告人：Xinhong Li
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/li26l_interspeech.pdf

## 问题
生成式增强依赖条件信息质量：浅层噪声 Mel/波形难以保留谐波等结构，易出伪谱；高层语义条件又假设预训练模型能从噪声中抽准语义，与增强任务前提冲突，形成循环依赖。

## 方法
HFMSE 用显式谐波先验引导 flow matching。条件编码器从随机掩码的干净目标 Mel 与噪声 Mel 提条件；DiT 学习噪声到干净 Mel 的速度场，推理时掩码覆盖全长（无需外部干净参考），配合 CFG 与 BigVGAN 合成。谐波编码器两步：(1) 用 Mel 尺度 Pitch-Harmonic Conversion Matrix（MPCM）做软基频定位；(2) 再与 MPCM 作用生成谐波掩码，经门控聚合后作为持续结构条件注入生成过程，而非仅作后处理或辅助损失。

## 实验与结果
训练约 2000 h（VCTK、LibriTTS、Common Voice、DNS5 干净 + WHAM!/DNS5 噪声，SNR −5~20 dB，40% 加混响），24 kHz 训练、16 kHz 评测。在 DNS Challenge 2020 上对比回归、扩散、离散 token 与 FlowSE 等。HFMSE 在有混响 / 无混响 / 真实录音多数 DNSMOS 与 Spk Sim 上达最优或接近最优（如无混响 OVRL 3.485、Spk Sim 0.958；真实录音 OVRL 3.296）。消融显示去掉谐波编码器比去掉噪声语音条件跌幅更大；去掉门控或掩码训练也会下降。

## 结论
作者认为用物理启发的谐波结构先验作条件，可规避噪声浅层特征与脆弱语义条件的局限，在 DNS 2020 上达到 SOTA 级感知表现。

## 点评
路线选择“低层、噪声相对稳健的结构先验”而非语义 token，直接回应条件不可靠问题，适合重噪/混响下语义提取失败的场景。MPCM + 软基频避免硬 F0 估计的脆性。风险在于强依赖谐波假设：清音/非谐波帧靠扩散掩码缓解，但极端非语音噪声或高度非周期语音上先验可能变弱；相对 FlowSE，收益声称在低 SNR 与混响更明显。
