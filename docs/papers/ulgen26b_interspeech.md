# DiffAnon: Diffusion-based Prosody Control for Voice Anonymization

- 论文编号：1331
- 报告人：Ismail Rasim Ulgen
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ulgen26b_interspeech.pdf

## 问题
韵律兼具表达效用与说话人身份线索；现有匿名方法多固定抑制/保留/扰动韵律，缺少单模型内连续、推理时可调的效用–隐私折中机制。

## 方法
DiffAnon 在 SpeechTokenizer RVQ 空间做条件扩散：以 Q1 为语义条件、MPM 帧级潜变量为韵律、FreeVC 说话人嵌入为说话人条件，x-prediction 重建全层 Q1:8。训练随机丢弃条件；推理用伪说话人替换身份，经 classifier-free guidance 调节 \(w_{pro}\) 控制源韵律保留强度，并可选用伪说话人 CFG。DDIM 100 步；训练于 LibriTTS。

## 实验与结果
VoicePrivacy 2024：\(w_{pro}\) 从 1→0 时 F0 相关与 UAR 单调下降、EER 上升（如 libri-test lazy EER 33.09→42.43），WER 约 4.62→5.61。\(w_{pro}=1\) 时 F0-corr 达 75.58（test），UAR 约 50.80；伪说话人 CFG（\(w_{spk}=3\)）lazy EER 可达 48.16，接近强基线。单模型覆盖多工作点。

## 结论
扩散 + CFG 首次在语音匿名中提供可插值的推理时韵律控制，实证韵律是效用–隐私折中的主轴之一。

## 点评
把折中从“换系统”变成“调权重”，对部署选点很实用。内容靠 Q1 锚定较稳，但强匿名仍损情绪 UAR；semi-informed 下 EER 明显低于 lazy，说明攻击者适应仍挑战形式化“可控”叙事。
