# ALARM: Audio–Language Alignment for Reasoning Models

- 论文编号：759
- 报告人：Hassan Shahmohammadi
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/grinberg26_interspeech.pdf

## 问题
冻结 LLM、仅训适配器的自生成目标可避免输出分布偏移，但不适用于内置思维链的推理 LLM（RLM）：推理轨迹会暴露文本替身输入，导致不自然回复。依赖 ASR/VAD 的输入对非语音与低 SNR 也脆弱；单编码器（如 Whisper）难兼顾语音/音乐/环境声。

## 方法
ALARM：
1. **数据**：约 6M 实例 / 2.5M 独特提示 / 19K 小时（语音、音乐、声音、指令）；用大指令模型生成并过滤与元数据对齐的提示；用同骨干 RLM **self-rephrasing** 把自生成回复改写成音频理解风格（思考预算 \(B=1536\)），避免暴露“元数据/文本输入”。
2. **多编码器**：Whisper、W2V-BERT-2.0、MuQ、SSLAM；层加权平均后适配；融合变体：
   - **ALARM-CA**：以 Whisper 为主、串行 cross-attention 融合（25 Hz）；
   - **ALARM-P**：Whisper 主序列 + 三路 Perceiver 前缀（各 20 latent）；
   - **ALARM-E**：推理时拼接 CA 融合特征与 Whisper 适配特征（50 Hz，无需再训）。
冻结 RLM（Qwen3-4B-Thinking），只训适配/融合。

## 实验与结果
（抽取在 Experimental Setup 开头截断；指标取自摘要。）
- 4B ALARM 在同类规模上更优，并在多数更大 ALM 之上的音频推理基准表现突出；**保留文本能力、训练成本较低**。
- **MMAU-speech** 开源最佳；含闭源时整体约第三；**MMSU** 亦强。

## 结论
Self-rephrasing 使自生成范式兼容 RLM；多编码器压缩融合去除 ASR 依赖，在较少数据与算力下得到有竞争力的音频推理 ALM，并开源代码与权重。

## 点评
核心洞察是：对 RLM，对齐问题不只在输入侧，还在“目标回复是否像听音频”。Self-rephrasing + 多域编码器是务实组合。**实验数字表未进入抽取**，具体分数与消融需回 PDF；点评不编造未写明的绝对分。
