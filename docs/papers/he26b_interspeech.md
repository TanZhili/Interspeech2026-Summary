# Spec2Spatial: A Time-Frequency Spatial Attention Network for Binaural Audio Synthesis

- 论文编号：607
- 报告人：Changjun He
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/he26b_interspeech.pdf

## 问题
深度学习单声道到双耳合成仍难忠实再现 ITD/ILD 等耳间线索，与真实录音存在明显差距。作者希望在时频域显式建模耳间关系并注入声源位姿条件。

## 方法
Spec2Spatial：先用 Time-Domain Warping（TDW）按几何延迟粗造左右通道，再 STFT；编码器堆叠 Interaural Spatial Attention Network（ISAN，含能量分析模块 EAM 的时–频门控）与 Conv2D；解码器用 Condition Fusion Residual Network（CFRN，FiLM 注入 7 维位姿）与上采样，预测复数掩码后乘到 warped 谱并 iSTFT。损失为波形 L2、相位损失与多分辨率 STFT 损失。

## 实验与结果
Binaural Speech（约 2 小时 KEMAR 配对录音）上：DILD 1.250、DITD 0.034、MRSTFT 1.174，均为对比中最优；Wave-L2 等次优。主观 MOS / Spatialization / Similarity 均最高（如 MOS 4.21）。消融：仅 TDW 时 DILD 极差；去掉 TDW、EAM 或 CFRN 均损害耳间与谱指标。作者称对音乐等 OOD 音频也有效。

## 结论
时频耳间注意力 + 位姿条件残差融合可显著改善 ILD/ITD 与感知质量；未来需更大双耳数据与更广听测以提升跨数据集泛化。

## 点评
相对纯时域/扩散基线，把优化目标对齐到 DILD/DITD/MRSTFT 更贴近空间听感。TDW 提供粗 ITD、ISAN/CFRN 补 ILD 与频相关线索的分工清晰。局限仍是单一小数据集与固定分裂；Wave-L2 并非最优也说明波形全局误差与耳间保真不完全一致。
