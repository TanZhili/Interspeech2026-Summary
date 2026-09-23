# Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS

- 论文编号：2730
- 报告人：Rong Wang
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26ea_interspeech.pdf

## 问题
MOS 与谱距离只给全局分，无法定位合成相对自然语音的偏离层级：是韵律垮了、音段垮了，还是两者独立？

## 方法
在 LJ-TTS（13,100 句配对）上分析四系统（Tacotron2-DDC、FastSpeech2、Glow-TTS、MixerTTS），共享 HiFi-GAN。韵律：21 个句级 F0/强度/时间特征 + LASSO 分类。音段：元音空间面积、按发音部位的 F2 轨迹、locus equation。人–机边界经 MFA 迁移并抽查校验。

## 实验与结果
韵律呈跨时间尺度解离：全局 F0 变异压缩（\(d=-0.55\)），局部 pitch inflection 升高（\(d=+0.82\)）；语速/浊音比等时间指标无显著差。元音三角形面积仅剩人类 9–30%；齿龈/软腭处 F2 条件运动减弱，齿龈 locus 斜率系统偏高。韵律与音段偏差 Spearman 近零。LASSO AUC≈0.851。架构上 FastSpeech2 韵律偏差小但元音塌缩最重，Glow-TTS 局部变调过量等。

## 结论
作者认为神经 TTS 并非“单调平坦”，而是全局–局部 F0 协调与音段目标/协同发音各自偏离；二者基本不相关，应作为独立质量维度，补充 MOS。

## 点评
用语音学可解释指标拆开 MOS 黑盒，结论“解离而非平坦”有说服力。局限在单说话人朗读英语、两阶段声学模型；作者也承认在更口语/端到端系统上差距可能更大。
