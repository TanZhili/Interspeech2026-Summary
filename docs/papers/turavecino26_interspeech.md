# Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis

- 论文编号：803
- 报告人：Biel Tura-Vecino
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/turavecino26_interspeech.pdf

## 问题
TTS 中 CFG 常用固定零向量作无条件表示，难以区分说话人与文本等正交条件，且可能落在训练分布外，导致大引导尺度下不稳定。需要更稳的无条件基线与可解耦的属性引导。

## 方法
模型：Qwen3-0.6B AR 骨干 + 轻量扩散头预测 64 维 VAE 潜变量，Perceiver 编码说话人，BPE 文本。将固定 ∅ 换为可学习 null 嵌入 ¯s、¯t；训练时各条件独立以 0.1 概率替换。推理可写解耦 CFG：分别对说话人/文本无条件隐藏态施加 ws、wt。对比固定零向量与可学习 null，并与 FishSpeech、Qwen3-TTS、VoxCPM、IndexTTS2 等对比；客观指标含 CER、SECS、PRO、PMR、PQ、UTMOS、Pitch std、SRR；主观多模型 CMOS。

## 实验与结果
耦合 CFG：可学习 null 对 w≥1.0 更稳，说话人相似度平台高于固定零向量峰值；w=0.8 时 SECS 0.817 vs 0.755，CER 相近且 Pitch std 更高。解耦 wt=0.4、ws=1.2 进一步抬 SECS/PRO。CMOS：可学习变体自然度/相似度均为正，固定零为负；解耦版相似度偏好更强、自然度略低于耦合版。文本引导上存在稳定性–表现力权衡，说话人引导存在相似度–绝对质量权衡。

## 结论
可学习 null 提供更稳、有意义的无条件基线，提升相似度与表现力并对大 CFG 更鲁棒；独立 null + 解耦权重可在推理时细粒度控属性。

## 点评
改动小但打在 CFG 实现细节上：把“缺条件”学成域内锚点，比硬塞零向量更合理。解耦引导把相似度与可懂度/表现力的折中显式化，利于产品侧调参；局限是评测说话人偏表现力强，听感上“更像参考”未必总被判为更自然。
