# Audio Language Models

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：8
- 论文数：5
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场由一篇面向 ASR 的 speech-LLM 进展邀请报告与四篇系统/评测工作组成。邀请报告在标准 speech-LLM 已于主要榜单成熟的前提下，聚焦释放 LLM 潜力、长时建模、解码加速，以及无编码器 speech-LLM 通向原生多模态。论文侧则分别处理离散化信息损失（混合离散—连续 codec）、流式文本对齐语音分词、Large Audio Language Model 思维链忠实性，以及印度语言情境提示是否真正被 AudioLLM 利用。

方法上，HybridCodec 用时序压缩离散 token 加降维连续残差，离散域自回归与非自回归连续残差上采样结合；TASTE-S 把 CTC ASR 接入编码器并改造单元解码器以支持流式。评测上，忠实性框架定义无幻觉、整体性与专注聆听等音频忠实准则并用音/链干预基准；IndicContextEval 用七级递进提示（含对抗错误实体）检验情境利用。整体趋势是：从“接上 LLM”转向效率、流式、忠实推理与情境是否生效。

## 技术内容

### 邀请报告与高效/流式语音—文本建模

**Recent advances in speech language model for ASR**（论文 id 未提供；Jinyu Li）邀请报告综述将语音模态接入 LLM 架构的 ASR 向 speech-LLM 进展；在标准路径已成熟的基础上讨论释放 LLM 潜力、长时语音建模、解码加速，以及无编码器 speech-LLM 作为原生多模态方向。

**HybridCodec: Modeling Discrete and Continuous Representations For Efficient Speech Language Models**（论文 2784；Artem Ploujnikov）提出混合离散—连续焦点调制 codec 与混合 Transformer：离散域自回归推理，并耦合非自回归预测与连续残差上采样，以缓解离散化信息损失；摘要称显著改善说话人身份等关键属性保留并提升生成质量。

**TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling**（论文 1686；Liang-Hsuan Tseng）扩展 TASTE 为可流式 TASTE-S：编码器集成 CTC ASR 以即时双模态编码，并重设计单元解码器支持在线解码；联合训练后显示流式约束下仍保持文本对齐分词优势（细节以官方摘要为准）。

### 忠实性与情境利用评测

**Investigating Faithfulness in Large Audio Language Models**（论文 1533；Pooneh Mousavi）提出系统评估 LALM 中 CoT 相对输入音频与最终预测的忠实性框架，定义无幻觉、整体性与专注聆听三类音频忠实准则，并基于音频与 CoT 干预构建基准；在 Audio Flamingo 3 与 Qwen2.5-Omni 上观察到推理常与最终预测对齐，但不总是强锚定于音频，提示潜在多模态脱节。

**IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages**（论文 3272；Sakshi Joshi）发布约 56 小时、555 名说话人、8 种印度语言、23 个专业领域的自然语音基准，设计七级递进提示（元数据、自然语言描述、英/本地文字实体列表及含错误实体的对抗提示），以区分模型是真用情境还是依赖预训练参数知识。

## 本场要点

- Speech-LLM for ASR 进入“成熟路径之外”的长时、加速与无编码器议题。
- 混合离散—连续表示缓解纯离散 token 的信息损失。
- 文本对齐语音分词需要流式改造才能服务实时 SLM。
- LALM 的 CoT 可能与预测一致却未必忠实于音频。
- IndicContextEval 用对抗提示检验情境是否被真正利用。
- 评测从榜单 WER 扩展到忠实性与情境利用率。

## 覆盖核对

| paper_id | title |
|---|---|
| （空） | Recent advances in speech language model for ASR |
| 2784 | HybridCodec: Modeling Discrete and Continuous Representations For Efficient Speech Language Models |
| 1686 | TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling |
| 1533 | Investigating Faithfulness in Large Audio Language Models |
| 3272 | IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages |
