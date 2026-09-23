# ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching

- 论文编号：185
- 报告人：Jihwan Kim
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26_interspeech.pdf

## 问题
零样本对话 TTS 的 flow matching 在密集 Mel 上做分钟级单次生成时显存爆炸，常被迫切块，损害长程一致性。

## 方法
ZipL-Dialog：确定性 Mel 自编码器将 100 Hz Mel 压到 25 Hz（\(r=4\)，\(D=100\)）连续潜空间；在潜空间做掩码条件 flow matching（前缀上下文干净、目标区线性插值噪声）；辅助 Mel 域重建损失 \(\lambda=0.5\)。ZipFormer 下采样改为较温和的 [1,1,2,1,1]，避免默认激进层级在压缩后损害短音素分辨率。预训练后在 OpenDialog 英语子集微调。

## 实验与结果
相对 ZipVoice-Dialog：最大峰值显存最多降 11.22×（CoVoMix2：36.21→3.23 GB），推理最多快约 2.23×。UTMOS 最优或并列最优；WER/cpSIM 略逊未压缩基线。消融：确定性 AE 优于 VAE（WER 3.634 vs 6.535）；加 \(L_{\mathrm{mel}}\) 全面提升；默认 [1,2,4,2,1] 与无下采样均严重损害质量。

## 结论
作者认为 25 Hz 潜空间 CFM + 适配层级可大幅降低长对话合成的显存与时延，并保持有竞争力的感知自然度。

## 点评
把“长序列显存”问题落到时间压缩，并用确定性瓶颈 + Mel 监督对抗 VAE 过平滑，针对性强。效率收益清晰；代价是客观可懂度与说话人相似的小幅回退，说明压缩仍损局部细节。
