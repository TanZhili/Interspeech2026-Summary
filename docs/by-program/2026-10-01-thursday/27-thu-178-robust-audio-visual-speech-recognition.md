# Robust Audio-Visual Speech Recognition

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：10
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述；Survey Talk 条目无技术摘要时不臆造结果。

## 技术趋势

本场聚焦噪声与复杂环境下的音视频语音识别（AVSR），尤其是 LLM 骨干接入后的稳健表示、跨模态对齐与压缩 token 多任务能力。共同问题是：干净条件优化的 LLM-AVSR 在噪声下表示不稳；独立投影或浅融合限制互补交换并加重 LLM 计算负担。

技术路径包括：向 Whisper 类骨干注入说话人与噪声场景嵌入；在 LLM 内部关键位置加入变分信息瓶颈以正则化表示；稀疏模态对齐与视觉单元引导细化；以及压缩多模态语音 token 同时支撑识别与翻译，并用对比对齐保留语言容量。场次以 Survey Talk 开场，但程序单未给出技术摘要，正式方法贡献集中在后续四篇 Oral。

## 技术内容

### Survey Talk（程序未提供摘要）

**To be announced (Survey Talk, 40 mins)**（论文 id 未给出；presenter 未给出）安排在 14:00–14:40，类型为 Survey Talk。官方程序单未提供技术摘要、题目亦标注待公布，故本处仅记录场次形式与时长，不臆造综述内容或结论。

### 自适应嵌入与 LLM 内正则

**Adaptive AVSR: Integrating Speaker and Environmental Embeddings for Robust Audio-Visual Speech Recognition**（论文 2081；Tobias Bocklet）在 Whisper ASR 上扩展 AV 融合，并从音频提取说话人与噪声场景嵌入。噪声嵌入用自定义注意力模型生成并注入 AV 融合模块；说话人用 X-Vector，在解码前缀拼接、额外交叉注意力与门控加权三种策略间比较，于 pre-decoder 注入。摘要称 LRS3 多噪声条件下相对基线噪声/说话人自适应分别提升 3.5%/3.2%，相对 AV-HuBERT 相对 WER 降幅最高达 13.4%。

**VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition**（论文 1903；Umberto Cappellazzo）指出 LLM-AVSR 多在干净声学上优化，缺少稳定噪声表示机制。提出 VIB-AVSR：在 LLM 骨干目标位置插入变分信息瓶颈层以正则化表示，无需改架构或额外训练数据。摘要称可降低多种 SNR 与噪声类型下的性能退化。

### 稀疏对齐、视觉细化与压缩多任务

**Robust LLM-based Audio-Visual Speech Recognition with Sparse Modality Alignment and Visual Unit-Guided Refinement**（论文 1277；Fei Su）认为独立投影或浅融合限制跨模态对齐并增加 LLM 负载。提出 AVUR-LLM：稀疏模态对齐与视觉单元引导细化。摘要称 LRS3 达 SOTA，0 dB SNR 加性噪声下相对基线相对改进 37%，并释放代码与相关资源。

**MTC-AVSR: Compressed-Token-based Audio-Visual Speech Recognition and Translation with Contrastive Language Alignment**（论文 266；Lusi A）针对高分辨率多模态序列对 LLM 的计算成本，以及 token 压缩多局限于单任务识别的问题，提出基于 minimal multimodal speech（MMS）token 的多任务模型：MMS 式压缩器 + 提示条件 LLM 单流推理，轻量语言适配器（LAM）将压缩、源对齐 token 映射为多语表示，并以 token-contrastive alignment loss（TCAL）与多语词表对比对齐。摘要称 LRS3 WER 0.74%（与 SOTA 相当），MuAViC En-X 上英–西/法/葡 BLEU 分别为 28.1/26.3/21.8，均为所述 SOTA。

## 本场要点

- Survey Talk 占 40 分钟但程序无标题与摘要细节，技术结论不可从本批 JSON 推断。
- 说话人/环境嵌入与 VIB 分别从输入适配与 LLM 内部表示两侧提升噪声稳健性。
- 稀疏对齐与视觉单元细化针对浅融合瓶颈，并报告强噪声相对增益。
- 压缩 token 可在识别与翻译间复用，对比语言对齐用于保留残差语言容量。
- 评测主轴仍是 LRS3，并延伸到 MuAViC 翻译任务。

## 覆盖核对

| id | title |
|---|---|
| （空） | To be announced (Survey Talk, 40 mins) |
| 2081 | Adaptive AVSR: Integrating Speaker and Environmental Embeddings for Robust Audio-Visual Speech Recognition |
| 1903 | VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition |
| 1277 | Robust LLM-based Audio-Visual Speech Recognition with Sparse Modality Alignment and Visual Unit-Guided Refinement |
| 266 | MTC-AVSR: Compressed-Token-based Audio-Visual Speech Recognition and Translation with Contrastive Language Alignment |
