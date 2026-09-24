# From Noisy Speech to Accurate APIs: LLM-driven Embedding Steering for Resilient Tool Retrieval

- 论文编号：3291
- 报告人：Rama Doddipatla
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zorila26_interspeech.pdf

## 问题
语音驱动 tool/API 检索中，API 描述风格混乱且与嵌入训练分布错位，ASR 噪声进一步放大查询–描述失配，微调嵌入成本高。

## 方法
训练无关离线 embedding steering：用 Qwen3-8B 为每个工具生成至多 10 条用户风格用例/查询，嵌入平均得 ellm，与原描述嵌入混合 e′=α e_api+(1−α)ellm（验证取 α=0.5）。查询侧：WhisperSpeech TTS + 混响与 speech-shaped noise（SNR∼U(−5,5) dB）后 Whisper ASR，得到干净/噪声转写。

## 实验与结果
数据集 Gorilla-HF、Ultratool、ToolACE；嵌入 BERT-base、ToolRetriever、bge-base/large。K=10 时各模型/数据集 NDCG 普遍提升；如 bge-large 平均 N@1 在参考查询约 52.7→60.5，噪声查询约 19.3→20.5。弱编码器相对增益最大。K=1 已有收益，K=5/10 更稳；α∈[0.25,0.5] 最优。

## 结论
LLM 合成查询平均嵌入可无重训地增强 speech-to-API 检索，对描述噪声与 ASR 错误均有韧性，易接入现有流水线。

## 点评
把查询扩展做成工具侧表示精炼，模型无关、部署轻。噪声条件 WER 极高时绝对分仍低，steering 是缓解而非根治。语音为 TTS 仿真，真实口语意图分布可能更散。
