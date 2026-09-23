# Energy Redistribution in the Spectro-Temporal Modulation Domain for Near-End Listening Enhancement

- 论文编号：319
- 报告人：Amin Edraki
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/edraki26_interspeech.pdf

## 问题

Near-End Listening Enhancement（NELE）需在总能量不变下重分配语音能量以提升嘈杂回放可懂度。多数方法在时–频域加权，难以显式操控对感知重要的 Spectro-Temporal Modulation（STM）结构（如共振峰过渡）。

## 方法

在 Modulation Power Spectrum（MPS）上乘以可学习非负 STM mask，再逆 2D FFT 回谱图（复用原相位），加高斯带通强调后 iSTFT，最后能量归一化到与干净语音相同。mask 为段无关全局参数，用 −ESTOI(干净参考, 处理后+噪声) 做梯度优化。消融比较 temporal-only、spectral-only、separable、joint 四种参数化，最终选用参数更少且效果接近 joint 的 separable mask（约 260 vs 16K 参数）。

## 实验与结果

训练：LibriSpeech train-clean-100 的 5 s 段 + AudioSet 噪声，SNR −15–0 dB。客观评测：dev-clean 100 句，DEMAND（restaurant/living room/station）与 SSN，SNR −10/−5 dB；指标 ESTOI、wSTMI、STGI、Whisper-small WER。相对未处理基线，所提方法平均增益通常高于 SSDRC、OptimalSII、iMetricGAN；−5 dB 下多数条件显著最优。主观：5 名正常听力普通话听者、中文矩阵句、餐厅噪声 −5 dB，句正确率 STM 0.92，高于 Noisy 0.46 及 OptimalSII/iMetricGAN，与 SSDRC（0.90）接近。

## 结论

作者认为在 STM 域联合调控谱/时调制比单维 mask 更稳；可分 mask 在参数量与效果间折中较好。主观实验规模小、条件单一，需更大验证；学到的 mask 远离调制 DC、偏向更高调制频率，反映能量从极慢包络再分配。

## 点评

把 NELE 从时–频“哪段能量重要”转到“哪类调制重要”，与可懂度文献中 STM 角色一致，且用可微 ESTOI 直接优化全局 mask，实现简单。脆弱点在于：优化目标绑死 ESTOI，其他指标/ASR/主观不完全同序；全局固定 mask 不随内容自适应；主观样本少，对声调语言的泛化仍属初步证据。
