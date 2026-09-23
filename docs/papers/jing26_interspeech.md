# EmoSURA: Towards Accurate Evaluation of Detailed and Long-Context Emotional Speech Captions

- 论文编号：1046
- 报告人：Xin Jing
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/jing26_interspeech.pdf

## 问题
情感语音长描述字幕难评：N-gram/嵌入度量对长度敏感且难捕感知细节；LLM 整体打分在长文上易推理不一与上下文崩塌；与音频脱钩的标签分解又无法声学接地。

## 方法
EmoSURA：用 LLM 将候选/参考字幕拆成原子感知单元（APU）；用 Qwen2-Audio 对每条 APU 做相对原音频的 Yes/No 验证得精度；再用 LLM 做 APU 级语义匹配得召回（奖励参考外但音频支持的正确细节）；综合 F1 与描述性 F1。发布 SURABench（MSP-Podcast 分层抽样约 1018 句，GPT-4.1 辅助字幕）。

## 实验与结果
14 人 MOS：BLEU/ROUGE/METEOR/CIDEr 等与人类负相关；EmoSURA PCC≈0.44，秩相关优于 MACE。扰动检测：声学特征/性别幻觉检出率高（约 93%/97%），情绪翻转约 82%，虚构发声事件仅约 60%。作者指出长度膨胀严重惩罚 N-gram。

## 结论
作者认为原子分解 + 音频接地验证比传统度量更可靠地评估长情感字幕，并提供分层基准。

## 点评
“拆原子再验声学”正面打中幻觉与长度惩罚。PCC 仍中等，人类评判方差未完全解释；参考字幕含 LLM 生成成分，可能与评测 LLM 同分布偏置。发声事件短板说明时序事件仍难。
