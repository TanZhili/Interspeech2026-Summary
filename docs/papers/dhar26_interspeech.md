# Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS

- 论文编号：1655
- 报告人：Nirmesh J. Shah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dhar26_interspeech.pdf

## 问题
扩散 TTS（如 StyleTTS2）音质已较强，但对表情语音中的尖锐韵律转折、快速基频变化仍难稳。解码器里常用 Snake 等固定周期激活来拟合谐波结构，但对突变幅度/频率与清浊边界的适应性不足。

## 方法
在 StyleTTS2 框架上提出 **OscillaTTS**：整体两阶段训练与模块布局不变，核心是把解码器（iSTFT-Net 声码器）中的非线性换成自适应振荡激活
\[
x + \tanh(\alpha\sin^2(x)),
\]
其中 \(\sin^2(x)\) 提供周期归纳偏置，可学习 \(\alpha\) 调节振荡强度，线性旁路保持稳定性。Stage1 用重建损失训练解码器相关组件；Stage2 联合训练（含 style diffusion、SLM 判别器等），推理时从文本侧预测风格嵌入。作者从梯度/Taylor 展开对比 Snake、HOSC，说明 Oscilla 具有输入依赖的门控式振荡响应。

## 实验与结果
数据：LJSpeech（单说话人）与 ESD 英语子集（Happy/Angry/Sad）；80/10/10 划分；24 kHz；stage1 200 epoch、stage2 120 epoch。
- LJSpeech：主观 Speech Quality 86.67（StyleTTS2 81.48）；MCD 6.59、F0-RMSE 0.35；AutoPCP 4.05、WER 1.85（优于 StyleTTS2 的 3.92 / 2.86）。
- ESD：Angry/Happy/Sad 的 ES MOS、MCD 等多项优于 StyleTTS2；AutoPCP/WER 亦改善（如 Angry WER 9.21→4.05）。
- 激活消融：可学习 α 的 Oscilla 在 MCD/F0-RMSE 上优于固定 α、Snake1D、ReLU、tanh 等变体。

## 结论
作者认为在扩散 TTS 解码器中引入自适应振荡归纳偏置，能更好建模快速韵律变化；在 LJSpeech 与 ESD 上主客观均有一致提升。局限/展望：多说话人表情 TTS 与歌声合成。

## 点评
这是一篇「只改激活函数」却对准真实痛点的工作：表情语音的尖锐转折往往卡在解码器局部非线性的表达能力，而不是再加一套韵律预测器。Oscilla 相对 Snake 的可学习幅度 + tanh 阻尼 + 线性旁路，设计动机能从梯度分析直接看出来，消融也支撑了「自适应 α」的必要性。脆弱点在于：改进高度绑定 StyleTTS2/iSTFT-Net 解码路径；主观样本与情绪类别有限；与更大系统级改动相比，增益幅度中等，外推到更复杂多说话人设定仍待验证。
