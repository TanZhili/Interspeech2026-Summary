# Formant-Guided Speech Repair for Enhanced Comprehension of Dysarthric Speech

- 论文编号：1217
- 报告人：Xin-Yu Chen
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26n_interspeech.pdf

## 问题
构音障碍严重损害可懂度；VC 对重度病例可懂度提升有限，TTS 管线又常损失韵律/身份。多数神经重建黑箱忽略元音共振峰等感知关键线索，且多在英语孤立词上评测，对汉语与跨病理泛化不足。

## 方法
模块化修复：构音障碍适配 ASR（冻结 Wav2Vec2.0 + Conformer + RNN 解码，CTC/CE 混合）→ FAST（共振峰对齐频谱变换）→ 说话人自适应 TTS（XTTS v2，仅微调 speaker encoder）。FAST：MFA 得 phone 边界，Praat 估 F1/F2，相对 AISHELL-1（汉语）或 TORGO 健康对照（英语）按元音类与性别参考计算偏差，用 α 控制高斯加权频谱扭曲幅度，再 iSTFT 与后处理。TTS 以 FAST 校正语音作条件与音色参考，并结合 ASR 文本。

## 实验与结果
数据：CDSD、MDSC、MSDM（汉语）、TORGO（英语）。主库 CDSD 上 CER 由输入 80.97% 降至 Full 22.33%（相对降约 72.4%）；MDSC/MSDM/TORGO Full 分别为 38.44/34.50/15.42。优于 DiffDSR、RnV、Liu 等基线，并在 CDSD/MDSC 上优于 Oracle TTS（真值文本）。消融去掉 FAST 或 SPK 约恶化 4–7 个绝对点。主观（18 听者，CDSD）：可懂度/理解/流畅约 2.3→4.4+，听努力 3.81→1.49（降约 60.9%）。κ=2.0 时 VSA 约升 10.6%、FCR 降低。

## 结论
显式共振峰校正再合成可同时提升可懂度与自然度，且文本正确 alone 不足以修复塌缩的声学实现。局限包括级联 ASR 错误传播与说话人相似度相对输入略降的可懂度–身份权衡。

## 点评
把临床“元音空间塌缩”写成可解释的频谱扭曲，并与 ASR–TTS 级联衔接，消融与 VSA/FCR 证据链较完整。脆弱处在于依赖 ASR/对齐质量与健康语料参考均值，重度非典型共振峰或对齐失败时 α 校正可能错向；跨语言泛化仍依赖语言特定参考。
