# New Training Methods for ASR

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：8
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场聚焦 ASR 新训练与架构：统一离线/流式 Transducer、流式 Conformer 卷积感受野、Aligner-Encoder 渐进对齐、三层联合优化、LLM 作 joiner，以及无源域数据的目标中心模型合并。共同目标是在延迟、数据与隐私约束下缩小模式差距并稳定对齐学习。

流式侧，块限注意力 + 动态块卷积统一双模式，并用模式一致性正则拉近离线与流式；BACON 证明块内可安全前看至边界，无需严格因果卷积。对齐侧，中间 Aligner/CTC 目标让对齐沿深度渐进形成；LLM-as-Joiner 把对齐交给编码器、语言建模交给 LLM。优化与迁移侧，三层学习塌缩为可扩展罚函数双层梯度；无源数据时用元学习合并多源模型并强调目标相关源。

## 技术内容

### 统一流式训练与块内卷积

**Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization**（论文 1195；Andrei Andrusenko）  
统一 RNNT 框架用带右上下文的块限注意力与动态块卷积同时支持离线与流式解码；提出高效 Triton 实现的模式一致性正则 MCR-RNNT，促使训练模式间一致。实验称提升低延迟流式准确率、保持离线性能并可扩展到更大模型与数据；框架与英语检查点开源。

**BACON: Boundary-Aware Convolution for Streaming Conformer Models**（论文 1455；Hainan Xu）  
指出块内帧已全部可用，卷积可前看至块边界而不违流式约束。BACON 将深度卷积通道拆为因果组与边界感知双向组，参数量不变、有效感受野更宽。在单/多说话人 ASR 与语音翻译两架构上提升准确率且时延可比。

### 对齐目标、三层优化与 LLM Joiner

**Progressive Alignment Objectives for Aligner-Encoder based ASR**（论文 2132；Jaeyoung Lee）  
Aligner-Encoder 无交叉注意力/Transducer 格，对齐常在上层突然形成、长句脆弱。InterAligner 加中间 Aligner 目标使对齐沿深度渐进，并配 InterCTC。LibriSpeech 17 层 Conformer 上，最终仅 Aligner 为 5.0/7.8 WER，InterCTC 至 3.4/6.0，InterAligner 至 3.1/5.6，长句增益最大。

**From Bilevel to Trilevel: Joint Training for Speech Recognition**（论文 1738；Jen-Tzung Chien）  
将双层学习扩展为三层：联合监督、无监督与蒸馏目标。用序贯罚函数双层梯度下降把下两层塌成子问题再与上层集成，单循环利用未标注结构、标注对齐与教师迁移。FastConformer + LibriSpeech 上优于两阶段预训练微调与先前双层方法。

**LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR**（论文 2149；Jaeyoung Lee）  
编码器按 Aligner-Encoder 将 T 帧变为 U 个 token 级语音状态；预训练 LLM 从这些状态预测转写，语音注入选定层，上层用 LoRA。相对语音前缀解码，上下文从 T+U 缩短为 U。LibriSpeech 与多语 Common Voice 上优于同规模基线；与轻量识别头联合训练可隐式向编码器迁移语言知识。

### 无源域目标中心合并

**Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging**（论文 371；Ka Hyun Park）  
在无法访问源数据、仅有预训练源模型与有限目标数据时，提出 Mᴏᴄʜᴇᴇ：用元学习解决表示错位并强调目标相关源，做目标中心模型合并。实验称 Macro-F1 最高优于基线 14.5 分。

## 本场要点

- 统一离线/流式 Transducer 需模式一致性正则缩小差距。
- 流式块内卷积可边界感知前看，扩大感受野。
- Aligner 对齐宜沿深度渐进，辅以中间 CTC。
- 三层联合优化可在单环融合监督、无监督与蒸馏。
- LLM 可作对齐后的语言建模 joiner，缩短上下文。
- 无源域场景可用元学习目标中心合并多源模型。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 371 | Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging |
| 1195 | Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization |
| 1455 | BACON: Boundary-Aware Convolution for Streaming Conformer Models |
| 1738 | From Bilevel to Trilevel: Joint Training for Speech Recognition |
| 2132 | Progressive Alignment Objectives for Aligner-Encoder based ASR |
| 2149 | LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR |
