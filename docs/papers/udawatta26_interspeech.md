# Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training

- 论文编号：1579
- 报告人：Pasindu Udawatta
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/udawatta26_interspeech.pdf

## 问题
训练中反复做听感测试不现实，损失曲线又缺语言可解释性；需能在训练过程中跟踪口音/元音系统学习的客观指标。

## 方法
提出 Vowel Space Overlap（合成与真值元音空间多边形交面积）与 Procrustes Normalised Disparity（去位姿/尺度后的形状残差）。在 GAE 预训练 Tacotron 2 上分别微调 NZE 与 GIE，多步提取角元音 F1/F2，算两指标；听者评目标口音相似度并与指标做 Pearson 相关。

## 实验与结果
两口音上，Overlap 最大与 Procrustes 最小的步数与视觉最佳形状对齐（NZE≈3000、GIE≈24000）。指标与感知口音相似度显著相关，可作损失曲线的可解释补充。

## 结论
元音空间几何指标可在训练中提供感知相关、语音学可解释的监控信号，并在多口音上稳健。

## 点评
把“看图收敛”落成可复现度量，对口音适应实验很实用。依赖角元音与强制对齐/共振峰估计，噪声与错误切分会扰动；目前仅 Tacotron 2 与两口音，外推到神经声码器端到端系统仍待证。
