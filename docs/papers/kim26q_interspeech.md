# A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers

- 论文编号：2154
- 报告人：Inho Kim
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kim26q_interspeech.pdf

## 问题
RAG 知识库同时含语音与文本时，联合嵌入有模态鸿沟与分数失衡；分模态检索后需能跨模态比较的重排器，但缺少跨模态相关性标注。

## 方法
STEREO：文本检索器用 e5-mistral-7b-instruct，语音用 HuBERT 基 SpeechRAG；分数 Z-score 归一后融合取 top-k。用 gpt-4o-audio-preview（纯文本候选用 gpt-4o）打统一相关性分构图。重排器在 ULTRAVOX / Qwen-Audio-Chat / Qwen2-Audio 上 LoRA，以 Yes−No logit 差打分，支持 pointwise/pairwise/listwise；长音频切窗，训练随机窗、推理 mean/max 聚合。

## 实验与结果
Spoken SQuAD（TTS 段落）+ MS MARCO 混合池。Pointwise 最稳：混合域 Spoken SQuAD 上 ULTRAVOX Hit@1 约 0.76 vs Z-score 0.53。下游 QA EM 普遍高于 Z-score（如 Spoken SQuAD mixed 上 ULTRAVOX 生成约 0.36→0.48）。无 Z-score 时语音候选易被淹没；Max 池化在语音占比较高时更好；30s×4 窗在 Spoken SQuAD 上略优。

## 结论
跨模态标注 + ALM 重排可在单模态与混合池中提升证据排序与下游 QA；pointwise 在异构设定更稳，Z-score 对保持语音可见性关键。

## 点评
late fusion + 重排避开联合空间鸿沟，路径清晰。标签依赖专有 ALM，质量有上限（相对 oracle Hit@1 仍有差距）。Spoken SQuAD 为 TTS，作者亦指出自然口语有待验证。
