# DP-VOXLET: Provable Speaker Anonymization for Disentangled Speech Representations

- 论文编号：2910
- 报告人：Christopher Liberatore
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ngong26_interspeech.pdf

## 问题
基于解耦表征的说话人匿名经验效果好，但缺可证明隐私；对说话人嵌入做朴素随机扰动又常落出解码器有效区域，导致音质崩溃。先前对整句特征加噪的 DP 方案效用差。

## 方法
定义 speaker differential privacy（基于 Gaussian DP / 权衡函数）：对同内容、不同说话人的解耦嵌入，机制输出经解码后应满足 \(G_\mu\) 下界。Gaussian speaker mechanism 对 L2-clip 后的说话人嵌入加噪。DP-VOXLET：在 VC 编码器说话人嵌入上训练 VAE，于低维潜空间加噪再解码回有效说话人嵌入，并做 L∞ clamp；可包装 OpenVoice、NaturalSpeech3、vec2wav2.0、ControlVC 等。

## 实验与结果
VoicePrivacy 2024、OpenVoice、librispeech-test、semi-informed。随噪声 σ 增大 EER 升、WER 略升但仍 <4%（如 σ=10 时 EER 41.2%、WER 3.4%；σ=0 时 EER 4.6%、WER 3.0%）。36 个挑战提交中仅 6 个 EER>40%；相对 Shamsabadi 等整特征扰动方案 EER/效用更优。理论：μ→0 时 EER 下界趋近 50%。

## 结论
在解耦语音表征上给出可组合的形式化说话人匿名与对抗下界，并用 VAE 保持高效用。保障依赖内容通道无说话人泄漏的假设。

## 点评
把 DP 落到说话人嵌入而非整句，是相对先前形式化工作的关键效用改进。Assumption 1（完美解耦）不可证，泄漏时保证减弱；实证与理论 EER 下界的对照仍值得读者单独审视。
