# Grounding Spoken LLMs in Multi-Speaker Audio via Diarization Conditioning

- 论文编号：445
- 报告人：Alexander Polok
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polok26b_interspeech.pdf

## 问题
Spoken LLM 用 SOT 扩展到多说话人时需改词表并微调解码器，易灾难性遗忘推理/摘要/问答能力；多说话人远场 grounding 与任务泛化仍弱。

## 方法
提出 diarization-conditioned SLM：用 DiCoW 的 STNO 掩码经 FDDT 在 Whisper 编码器各层调制表示，抽取目标说话人声学特征；经 modality adapter 送入冻结的 Ministral 解码器（实例化为 Dixtral = DiCoW 编码器 + Voxtral Mini 3B）。仅训练编码器与 FDDT；全局模式可将 \(p_T=1\)。Diarization 前端用 DiariZen。另构建 NSF-QA（内容/情感/性别问答与摘要），用 Gemini 评判准确率与 ROUGE-L。

## 实验与结果
转写（cpWER）：Dixtral macro 15.4，优于 Gemini 3.0 Flash（44.4）、VibeVoice（35.2）、Voxtral MTv2（31.4），接近专用 DiCoW v3.3（14.0）。消融：FDDT swap / 无全量 encoder swap 更稳；LoRA 解码器 ASR 最好（NSF-1 21.3）但伤指令跟随；QA+Summ 微调损害 Mixer6 转写。NSF-QA：zero-shot 远场内容 QA 54.6≈Gemini 55.1；微调后内容 73.0、情感 47.6、性别 95.5、ROUGE-L 41.4，超过近讲 Voxtral/Gemini。

## 结论
在编码器侧做 diarization 条件、冻结解码器，可在保留 SLM 通用能力的同时显著提升说话人归因转写；有任务数据时远场 Dixtral 可超过近讲基线，包括级联 ASR+LLM 难以回答的副语言问题。

## 点评
把多说话人问题压成“单说话人式”输入分布，避开 SOT 对 LLM 的结构性破坏，与独立按说话人解码的复杂度论证一致。强依赖外部 diarization 质量；QA 裁判与参考均用 Gemini，作者自认可能偏保守。ASR 与下游任务联合训练仍留作未来工作。
