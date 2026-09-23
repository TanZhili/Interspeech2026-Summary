# Empathy Omni: Enabling Empathetic Speech Response Generation Through Large Language Models

- 论文编号：984
- 报告人：Guangyan Zhang
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/wang26q_interspeech.pdf

## 问题
端到端语音 LLM 常把回复内容再合成语音，对用户副语言情绪利用不足；同类共情系统又依赖海量情绪对话与大规模训练。需要在数据与算力受限下显式感知情绪并生成共情口语回复。

## 方法
Empathy Omni 为双塔结构：冻结 Whisper large-v3（语义）与 emotion2vec（情绪）编码，经帧堆叠 MLP 下采样到 10 Hz 后融合送入 LLM（Qwen2.5-7B-Instruct + LoRA）。LLM 同步输出文本 token 与 token 级情绪轨迹；用 DTW 将目标波形的帧级情绪特征对齐到 token，联合 CE + MSE/余弦损失监督。语音解码器（6 层因果 Transformer）用门控融合 token 嵌入与 LLM 隐状态，经 AdaLN 注入情绪轨迹，预测 CosyVoice2 声学 token 再流式合成。两阶段训练：先对齐理解与文本共情，再训解码器。配套构建 EmotionalQA-200k（合成+ESD 改写+真实录音，约 135k/15k/50k），并与 VoiceAssistant-400k 联训。

## 实验与结果
VoiceBench 上综合竞争力强：CommonEval 3.47、IFEval 27.89 最佳，UTMOS 4.41 最高；Alpaca/WildVoice 接近 GLM-4-Voice。自建 1k 情绪查询集上 Emotion GPT Score 3.97、Speech Emotion MOS 4.23、ASR-WER 表中为 4.61，优于 OpenS2S 等。消融去掉融合模块后 GPT 分 3.97→3.15、MOS 4.23→3.85、WER 升至 6.42。作者称对悲伤/恐惧等需持续韵律塑造的情绪较有效，细微/混合情绪仍偏泛化。

## 结论
显式 token 同步情绪规划加可扩展合成数据管线，可在无需大规模共情预训练的情况下同时提升指令跟随、音质与共情表达；细粒度情绪与强度控制仍是开放问题。

## 点评
把语义生成与情感轨迹解耦，再用 AdaLN 条件合成，比“隐式从数据学共情”更可控，也解释了音质与共情分同升。DTW 对齐避开非言语发声上的强制对齐失败，设计贴合情绪语音。评测依赖 GPT-4o 与 ASR-WER，且 EmotionalQA 大量合成，真实分布外的细微情绪仍可能是短板。
