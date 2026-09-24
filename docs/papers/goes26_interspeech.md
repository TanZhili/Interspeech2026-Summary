# PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation

- 论文编号：2277
- 报告人：Nina Goes
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/goes26_interspeech.pdf

## 问题
高质量 TTS 内部表征难解释，细粒度音素级编辑（如 /s/–/f/ 插值）常受限于离散音素表示，难以在连续空间平滑变换。需要结构化、可插值的音素潜空间。

## 方法
PhonemeCVAE：β-VAE 为每类音素学习条件高斯先验；编码器用时长感知高斯下采样 + Conformer 得音素 token，解码器上采样 + PostNet；辅以监督对比损失促进类内紧致、类间分离，并含时长预测与对抗/特征匹配损失。推理时在最小对立对的类中心间线性插值替换对应 token，再解码与 HiFi-GAN 声码。

## 实验与结果
在 LJSpeech、LibriSpeech、CMU ARCTIC 等上，先验+对比相对消融显著提升 silhouette 与类间分离（UMAP 更清晰）。听测（N=18）：沿 α 插值可感知音素连续变化；编辑音自然度/质量均值约 3.14/3.22，略低于原音 3.45/3.55。

## 结论
类条件先验与对比正则形成可跨数据集泛化的音素潜拓扑，支持可控插值编辑且大体保持合成质量，有望服务发音清晰与治疗等场景。

## 点评
把音素编辑写成“在先验中心间插值再 patch token”，接口直观。依赖 MFA 对齐与最小对立对听测，对协同发音与跨说话人稳健性仍待更大规模评测；编辑质量略低于原音，说明重建–可编辑性折中仍在。
