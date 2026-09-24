# Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models

- 论文编号：1737
- 报告人：Liang Cao
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cao26b_interspeech.pdf

## 问题
LALM 音频序列远长于文本，逐 token 自回归延迟高；改 NAR/加 MTP 头或草稿模型有结构或显存开销，且文本低熵与音频高熵导致统一置信阈值会使并行解码退化或伤保真度。

## 方法
Audio-NSP：仅通过数据中心 SFT 激活半自回归块生成——在原序列后追加若干 Anchor-Mask 块（锚点+可学习 mask），位置 ID 对齐逻辑位置；定制注意力（前缀因果、块内双向、块间隔离），损失只算 mask 位。推理为 predict–verify–accept；模态感知动态截断：文本 τ_text=0.8、音频 τ_audio=0.2（Top-1 置信度），按置信度接受变长前缀。骨干 VITA-Audio-Plus-Vanilla，块长 W=4。

## 实验与结果
相对 VITA-Base / VITA-MTP：ASR 平均 WER 劣化约 +1.20（MTP +2.14），TPS 最高约 3.42×（LibriSpeech-clean）；SQA 平均 ACC 劣化约 −1.64（MTP −1.78），约 2.4×；TTS 平均劣化约 +0.29（MTP +0.68），约 1.9×。动态截断 Pareto 优于固定步长；Top-1 / Top-10 sum / Entropy 均可调出可用折中，默认 Top-1>0.2。

## 结论
无结构改动即可把预训练 LALM 变为块级生成，并用模态感知截断缓解文本–音频熵差，相对 MTP 在加速与质量保留上更优（约 1.89×–3.42×）。

## 点评
核心洞见是“同一阈值套在音频上会退化成 AR”，用分模态阈值换速度–保真。仍依赖 SFT 与固定 W；TTS 加速弱于 ASR 是有意保守。未改架构利于落地，但训练序列打包与注意力定制实现成本不低。
