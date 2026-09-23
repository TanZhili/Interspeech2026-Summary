# Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR

- 论文编号：977
- 报告人：Ryo Magoshi
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/magoshi26_interspeech.pdf

## 问题

LLM-ASR 在新领域常只有文本、无配对语音。仅微调 LLM 缺声学上下文；伪音频提示要么依赖 TTS 难扩展，要么只做文本嵌入上采样/掩码，未对齐音频编码器与投影器输出特性。

## 方法

提出 TE2SL：用可训练 Conformer 精炼模块，把 LLM 文本嵌入映射到真实音频提示潜空间。先在源域配对数据上学习文本嵌入→音频提示对齐；适配时冻结该模块，对目标域文本嵌入随机上采样、精炼并时间掩码，生成样本相关伪音频提示，再与指令一起微调 LLM。对比 text-only FT、Soft Prompt、Upsample-and-Mask。

## 实验与结果

英：LibriSpeech→SPGISpeech/SlideSpeech；日：CSJ SPS→APS（eval1/2）。TE2SL 全面最优：如 SPGISpeech WER 8.5（基线 11.1）、Rec OOV 50.1%；SlideSpeech WER 14.0；CSJ eval1/2 CER 19.6/17.5，OOV 召回亦最高。

## 结论

作者认为伪提示需同时样本相关且感知编码器/投影器特性，才能在纯文本适配中弥合模态差并提升领域词覆盖。

## 点评

把“伪音频提示像不像真提示”当成可学习对齐问题，比启发式上采样更对症。不依赖 TTS，利于多语扩展。精炼模块质量绑死源域配对数据；跨域声学差异极大时，伪提示仍可能偏语言侧。
