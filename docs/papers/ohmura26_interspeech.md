# LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control

- 论文编号：2231
- 报告人：Junki Ohmura
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ohmura26_interspeech.pdf

## 问题
数值化语音印象（VI，如明亮度等 11 维 1–7 分）可控 TTS 缺公开语料；且易出现印象泄漏——合成被参考音频自身 VI 拉偏。单参考同时供说话人与 VI 条件可能造成纠缠。

## 方法
发布 LibriTTS-VI：在 LibriTTS-R 上人工标注 130 句×10 维（+语速由 ASR WPM），训练 VIE 并按音高/能量/WavLM 相似句扩充到全库。骨干 VIC：HuBERT+BiLSTM 参考编码器、Control Module、STL，接 VITS。提出 VIC-dis：同说话人另一句 r′ 作说话人条件、VI 仍来自目标句；VIC-srf：用高斯噪声替换参考分支，纯 VI 控制。对比 VIC-base 与 Qwen3-TTS VoiceDesign（VI→NL 提示，零样本/微调）。

## 实验与结果
客观：VIC-srf 将 RVI-MSE 从 base 的 0.61 降到 0.41，∆V 从 0.22 到 0.05（泄漏近消失）；调制斜率平均 0.199>dis 0.159>base 0.121。QVD 数值控制弱（斜率 0.068），且文本语义与 VI 纠缠。主观多维调制 MSE：srf 0.92 vs base 1.15。质量 MOS 大多保持，部分极端调制略降。

## 结论
公开 VI 语料使可复现；双话语解耦与无参考生成显著减轻印象泄漏并提升数值可控性，优于基于 NL 提示的 LLM-TTS 在精细 VI 上的表现。

## 点评
问题定义清楚：泄漏来自“同一句既当身份又当印象”。解耦与无参考两条路互补；公开语料是社区价值。标注一致性中等、VIE 代理误差会传导到评测；部分维（如 Powerful–Weak）仍难学，极端调制可能伤自然度。
