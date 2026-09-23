# PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement

- 论文编号：916
- 报告人：Jun Gao
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gao26e_interspeech.pdf

## 问题
现有 flow matching 增强多在 Mel/STFT 域建模，SSL 仅作外部条件。Mel 缺相位、STFT 分布重尾且声学属性缠绕，生成难度大；未充分利用 SSL 低层声学与高层语音层的层级结构。

## 方法
PhASE-Flow 全程在 WavLM-Large SSL 空间工作：第一层 Transformer 作声学表示（生成目标流形），最后一层作语音（phonetic）条件。冻结 WavLM 从噪声输入提两路表示；DiT-based FM 用 OT 路径与 x-pred 目标学习干净声学表示分布，训练时以概率丢弃噪声声学条件以强化语音条件；推理用 4 步 Euler ODE。增强声学表示由独立训练的 Vocos 风格声码器（注意力 + ConvNeXt + iSTFT）还原波形。

## 实验与结果
干净数据约 1021 h（DNS5 LibriVox、VCTK、EARS、LibriSpeech，经 DNSMOS/UTMOS 过滤），噪声与 RIR 在线混合（SNR −5~15 dB，50% 混响）。在 DNS 2020 no-reverb / with-reverb 上对比 TF-GridNet、StoRM、LLaSE-G1、AnyEnhance、FlowSE。no-reverb：UTMOS 4.11、SBS 0.93、LPS 0.97、dWER 2.79%（最低），DNSMOS 3.40。with-reverb：非侵入指标领先生成基线，SpkSim 0.75、dWER 13.19%。消融表明声学 SSL 域优于 Mel/STFT；语音条件在 SSL 域带来全面增益，在 Mel 域则主要改善内容相关指标。

## 结论
作者认为在 SSL 域做 phonetic 条件的声学 flow matching，比频谱域更结构化，能提升感知质量与说话人相似性并抑制幻觉，且仅需四步采样即可高效推理。

## 点评
把“条件 SSL”升级为“在 SSL 流形上生成”，利用层间解耦对齐语义与声学，针对频谱缠绕与表示失配。四步采样是实用卖点。脆弱处：依赖 WavLM 层选择与声码器先验；混响集上生成式方法 SpkSim/dWER 仍可能差于噪声或判别式 TF-GridNet，幻觉问题未完全消除。
