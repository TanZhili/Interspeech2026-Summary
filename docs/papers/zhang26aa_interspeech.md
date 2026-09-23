# PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs

- 论文编号：1734
- 报告人：Pei Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26aa_interspeech.pdf

## 问题
多语 SLM 常冻住 LLM、混训多语多任务，易把各语音频表示压到共享空间，损失细粒度语言差异，且任务级对齐粗糙。

## 方法
PART 三阶段：① 仅训 adapter 做语内 ASR 粗对齐；② 渐进解冻编码器（先末 8 层再全量）+adapter，仍仅 ASR；③ 解冻 LLM，联合 ASR+S2TT。SenseVoice-large 编码器 + Qwen2.5（1.5B/7B）→ PART-2B/8B。数据：ASR 810k h（10 语）、S2TT 434k h。

## 实验与结果
FLEURS/Common Voice：PART-2B 平均 WER 4.7/7.4，优于同规模 Baseline-2stage（6.4/9.2）与 Whisper-large-v3；PART-8B 更优。CoVoST2 xx→en：PART-8B 平均 BLEU 39.1。消融显示去 ASR→S2TT 分阶段、去 LLM LoRA、去渐进解冻均降点；梯度相似分析显示语内对齐增强且跨语边界仍可区分。

## 结论
分阶段语内再跨语、任务依赖启用 LLM，可在保留语言特异性的同时提升多语 ASR 与翻译。

## 点评
抓住“过早混语混任务导致表示坍缩”的训练病，用进度表强迫先学语内映射再借 LLM 跨语。强在同数据预算对比清晰；大规模商购数据细节不可复现，方法迁移价值大于具体分数。
