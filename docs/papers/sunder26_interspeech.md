# Parameter-Efficient Adaptation of Speech-Aware LLMs for Timestamp Prediction

- 论文编号：2441
- 报告人：Avihu Dekel
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sunder26_interspeech.pdf

## 问题
词级时间戳对字幕、检索等重要，但 one-pass 交错生成会伤转写质量；独立对齐模型又难并入 speech LLM。需在单一 speech LLM 内做 SRWT，且参数高效、不破坏已有 ASR/AST 能力。

## 方法
两步：先 ASR 转写，再在转录条件上再生带词末时间戳与静音标记 的序列（10 ms 单位）。三种适配：Non-Mod 持续微调 projector+LoRAA；Mod-LoRA 冻结合并后的基座 LoRA，另训时间戳 LoRA（两 pass，需重算 KV）；Mod-aLoRA 用 activated LoRA，遇 `<|timestamp|>` 才激活适配器，可复用第一步 KV cache。基座为 Conformer 编码器 + Q-Former + 1B LLM。

## 实验与结果
训练数据含 LibriSpeech、MLS、CommonVoice、VoxPopuli 等，时间戳经 MFA 并按 CTC AAS 过滤。英文平均 AAS：Non-Mod 27.1 ms（相对最佳基线 Qwen3-FA 41.8 ms 降约 35%）；多语 Mod-aLoRA 21.2 ms 最佳。SRWT WER 与基座 ASR 同为英文 7.3%、多语约 5.3%。仅英语 SRWT 训练时，Mod-aLoRA 零样本多语 AAS 37.3 ms，远优于 Non-Mod 的 339.5 ms。

## 结论
两步 SRWT 保转写质量；Mod-aLoRA 兼顾模块化与 KV 复用，对齐误差达 SOTA，并具跨语零样本迁移。

## 点评
把“写什么”与“何时”拆开，再靠 aLoRA 复用基座 KV，切中 speech LLM 多任务扩展痛点。时间戳监督强依赖 MFA/过滤质量；Non-Mod 对齐更好但破坏模块化，实际选型需权衡。
