# MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion

- 论文编号：1596
- 报告人：Takuhiro Kaneko
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/kaneko26_interspeech.pdf

## 问题
MeanVoiceFlow 等一步流匹配 VC 推理快，但固定重型内容编码器（如 Conformer 瓶颈特征）耗时约为一流步的 10 倍，成为瓶颈；需在无额外预训练声码器条件下联合压缩内容编码与转换模块。

## 方法
MeanVoiceFlow2：用轻量可训内容编码器 \(c_\phi\) 替换教师固定内容编码器，并联合训学生平均速度网 \(u_\phi\)。训练含：(1) 相对教师 MeanVoiceFlow 的转换蒸馏 + 真实数据重建；(2) diffusion-GAN + 样本混合的对抗，提升真实感且不依赖外部声码器判别器；(3) 教师引导条件增强（用教师在打乱说话人条件下生成样本喂内容编码器）促内容–说话人解耦。推理仅用 \(c_\phi\) 与 \(u_\phi\)。

## 实验与结果
VCTK 零样本：相对教师 MVF，nMOS 3.93 vs 3.76，UT/DNSP 更好，CER/SECS 相近，RTF 约降 9×（0.00084 vs 0.0072）。对比 FasterVoiceGrad 主观/客观更优或持平且训练无需预训练声码器。消融显示转换+重建、扩散+混合、CondAug 均有贡献。LibriTTS 上同样约 9× 加速且质量提升。

## 结论
联合蒸馏轻量内容编码器与 Mean Flow，可在保持说话人相似度下明显提速并改善感知质量。

## 点评
抓住“一步流已快、编码仍慢”的真实瓶颈，蒸馏设计完整。仍依赖同数据训好的教师；波形合成用 HiFi-GAN，端到端一步波形未完全打通。
