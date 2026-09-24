# Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS

- 论文编号：1613
- 报告人：Jiacheng Shi
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shi26d_interspeech.pdf

## 问题
扩散情感 TTS 的偏好对齐（如 Emo-DPO）通常只强化目标情绪条件轨迹，未显式建模与竞争情绪模式的分离；而 CFG 本质依赖条件对比，这种「单向」优化会削弱细粒度可控性。

## 方法
**Emo-BPO** 在 Grad-TTS 扩散解码器上：
1. 用同文不同情绪的平行对构造双向监督：\((c,a_1,a_2)\) 学情感对齐分支 \(\epsilon_{\theta}^{\mathrm{EA}}\)，颠倒顺序学对比分支 \(\epsilon_{\theta}^{\mathrm{EC}}\)（两套参数，非单网络硬兼两职）。
2. 推理对比引导：\(\epsilon^\omega=(1+\omega(t))\epsilon^{\mathrm{EA}}-\omega(t)\epsilon^{\mathrm{EC}}\)，并用晚步日程 \(\omega(t)=1-t/T\)，早期弱引导保结构、后期加强情绪。
无需额外奖励模型或新标注；冻结文本编码器与时长预测器，只微调 score 网络。

## 实验与结果
数据：ESD + EmoVoiceDB。客观：Emo SIM 99.23、Prosody SIM 3.85、UTMOS 4.52、SER 均值准确 0.87，多项优于 EmoSpeech、CosyVoice(2)、EmoSphere++、EmoVoice；可懂度竞争（WER 3.84，CosyVoice2 更低）。主观 MOS/Emo MOS/MOS EC 与人类情绪识别亦领先；AB 偏好优于 EmoSpeech 与 CosyVoice2。消融：去掉对比分支或晚步日程均伤情绪/韵律/WER。

## 结论
作者认为应在 CFG 框架下同时学习情绪吸引与排斥轨迹；双向偏好 + 渐进引导可提升可控性与感知质量并保持可懂度。

## 点评
洞察贴合扩散机制：CFG 已是对数似然比，把「无条件」换成「竞争情绪条件」并把两条 score 分开学，比只做 DPO 推目标更吃透对比结构。晚步日程也符合「先结构后细节」的去噪直觉。脆弱点：依赖平行同文多情绪对；双分支推理成本更高；骨干是 Grad-TTS，相对现代 LLM-TTS 的绝对 WER 仍可能吃亏。
