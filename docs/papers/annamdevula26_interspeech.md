# CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations

- 论文编号：1744
- 报告人：Nirmesh J. Shah
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/annamdevula26_interspeech.pdf

## 问题
跨语 TTS（尤其低资源、音系多样的印度语）中口音与说话人属性纠缠，LLM-codec TTS 虽有跨语能力却难显式控制口音强度；过强口音伤可懂度，需要转换与连续强度调制。

## 方法
Neucodec（50 token/s）离散化；Perceiver Resampler（Ns=32）从参考声学 token 得说话人/风格嵌入；GRL 对抗分类器抑制嵌入中的口音/语言信息；可学习语言嵌入扩展到所有 latent slot 并相加，推理用 λ e_lang1+(1−λ)e_lang2 插值口音强度。Qwen2.5-0.5B AR 预测声学 token。数据：Indic 多语约 986 小时 + L2-ARCTIC 微调。指标：口音相似度/泄漏、UTMOS、SpkSim；20 人 MOS。

## 实验与结果
Indic：Proposed UTMOS 3.181、AccLeak 0.203、AccSim 0.371、SpkSim 0.842，优于 IndicF5、XTTS-v2。L2-ARCTIC：UTMOS 4.001、AccLeak 0.439、AccSim 0.686，口音控制度优于 CVAE/GST。主观口音相似度 MOS 高于基线；强度 0→1.0 时 AccSim 单调上升。

## 结论
对抗解耦 + 加权语言嵌入可在保留说话人的同时做跨语口音转换与连续强度控制，适用于低资源多语设定。

## 点评
核心是把“口音当可加条件、说话人当需洗掉的泄漏”，用 GRL+语言嵌入插值实现强度旋钮，工程清晰。强度分析与泄漏指标对齐目标；脆弱点是口音评测依赖 GenAID/微调口音嵌入的代理质量，且 SpkSim 在 L2 上略低于部分 GST 基线，解耦仍有折中。
