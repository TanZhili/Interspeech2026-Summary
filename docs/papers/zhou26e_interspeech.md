# Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces

- 论文编号：1696
- 报告人：Wangzixi Zhou
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26e_interspeech.pdf

## 问题
情感 TTS 即使用 arousal–valence（A–V）连续控制，训练标注常来自单一人群平均，默认「声学线索→感知情绪」映射普适。个体与文化差异会导致模型情绪与听者感知错位；RLHF 类对齐又需大量偏好数据并重训模型，不适于快速人均适配。

## 方法
提出轻量 **训练后个性化层**，不改声学骨干：
1. **情感生成器**：Grad-TTS + Emotion Controller（Emotion Feature Predictor + pitch/energy 预测）。A–V 经 Gaussian Fourier 特征映射后由四层 MLP 预测 SER 衍生的高维情绪特征；训练用 L1 对齐预训练 SER 特征，推理只需 A–V。
2. **交互遗传算法（IGA）**：对目标离散情绪，在 A–V 空间生成候选坐标并合成语音，用户选偏好样本；多亲算术交叉 + 衰减突变强度（\(M_1=0.20,\gamma=0.90,M_{\min}=0.05\)）迭代，通常约三轮收敛，得到个人/文化平均 A–V 映射。

## 实验与结果
数据：约 9 小时美式英语女声（EXPRESSO + EmoV-DB + ESD），A–V 由 SER 估计。相对 Grad-TTS+情绪嵌入，Emotion Controller：MOS 3.37→3.75，WER 21%→17%，CCC(A/V) 0.60/0.64→0.84/0.77。
个性化：中/印尼/日各 10 人共 30 人；个人化 A–V 相对美式数据集均值明显偏移。A/B：亲历个性化者偏好个人映射 76%；新文化听者对文化平均映射偏好约 64.8–69.8%；跨文化排序亦偏好本文化映射（约 65–70%）。

## 结论
作者认为应把情绪感知空间个性化/文化适配，而非一刀切平均 A–V；交互优化可在少量反馈下提升感知对齐。未来工作包括更广语言文化与实时个性化。

## 点评
工作抓住的是「控制空间」而非「声学模型」：把适配限制在 2D A–V，用 IGA 做极少交互的人均搜索，比 RLHF 更贴近产品侧快速定制。Emotion Controller 用 SER 特征桥接低维控制与高维声学，使个性化不必重训扩散解码器。脆弱点：骨干与语料偏英语女声，跨文化听评仍用同一声学模型；A–V 监督本身来自 SER 估计，存在标签噪声；偏好实验规模中等，文化结论更偏初步观察。
