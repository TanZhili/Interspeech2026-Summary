# DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization

- 论文编号：2447
- 报告人：Ziqi Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26z_interspeech.pdf

## 问题

统一方言 TTS 面临数据稀缺、正字/拼音跨方言读音歧义、多方言联合训练风格平均与相互干扰；新方言仅有数小时数据时难扩展，高质量方言数据直接续训也不一定稳。

## 方法

基于 F5-TTS 的多阶段流水线：统一 IPA 前端；Stage 1–2 在普通话+多方言 IPA 数据上训练，Stage 2 在文本嵌入后加方言感知 residual MoE，并用方言分类辅助损失引导门控；Stage 3 冻结主干，仅训 LoRA 与 Conditioning Adapter，并用音高/时长微扰增广适配新方言。另用 Flow-GRPO，以 ASR WER 为奖励，在高质量川方言语料上优化 DiT 主干。

## 实验与结果

约 0.7k h 普通话 + 0.4k h 方言。消融：去 MoE 或改用 pinyin 均明显变差（pinyin 时 WER&gt;90%）。相对商业系统 WER/MOS 仍有差距（数据规模差数量级）。对成都高质量数据：Flow-GRPO 将 CD WER 从 29.25% 降至 23.93，并改善 XA/ZZ 等相关方言；直接续训改善有限甚至变差。低资源京剧念白与南京话可经 PEFT 扩展。

## 结论

作者认为 IPA + 方言 MoE + PEFT 构成可扩展统一方言 TTS；GRPO 比直接续训更能利用高质量方言数据并产生跨相关方言增益。

## 点评

IPA 统一拼音歧义、MoE 抗风格平均，问题拆分清楚。客观 WER 绑特定 ASR，方言/戏曲语音上可能偏严；与商业系统对比不公平处作者已指出。奖励仅用 WER，韵律与自然度未直接优化，是当前边界。
