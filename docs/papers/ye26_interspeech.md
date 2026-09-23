# Which Speech Representation Better Matches Text-Native Reasoning? A Study of Speech-Text Alignment on Frame Rate and Representation

- 论文编号：21
- 报告人：Zhen Ye
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/ye26_interspeech.pdf

## 问题
口语对话模型常以文本 LLM 为骨干，但条件于语音时推理能力下降。作者将部分模态差距归因于时间粒度失配：常见 12.5–50 Hz 语音 token 远长于同语义文本（LibriSpeech 上文本约 3.32 Hz），稀释每 token 语义密度。全量微调 LLM 又把“表示好坏”与“骨干适应”缠在一起。

## 方法
冻结文本 LLM（Qwen3-4B）与 Whisper-Large-v3 编码器，固定信息率 600 bits/s，只训输入投影与音频头（约 100M）：
1. **长度对齐**：下采样至 50→2.08 Hz；用 **factorized FSQ**（分组预测）+ 轻量 **NAR audio LM head**（2 层 Transformer + slot embedding）突破低帧率信息瓶颈（可达约 300 bits/frame）；
2. **表示对齐**：在选定中间层对语音/文本隐状态做 utterance 级 InfoNCE（\(\lambda_{\mathrm{align}}=0.1\)）；
3. 三阶段：S2T → T2S → S2S QA（多任务权重）。

## 实验与结果
（全文抽取在 ASR 结果后截断，以下以可读部分与摘要为准。）
- 固定码本下低帧率 ASR 崩溃；factorized FSQ 后 WER 保持窄带（test-other 约 5.97–8.16，test-clean 约 2.39–3.90），呈 **U 形**：过高帧率冗余、过低则压缩损失；中间区 12.5 / 6.25 / 4.17 Hz 较优。
- 摘要结论：语音 QA 最佳制度为 **4.17 Hz + 中间层对齐**；约 2.5k 小时数据下冻结骨干可获有竞争力的 speech-to-speech QA。

## 结论
在冻结 LLM、固定比特率下，帧率与对齐深度共同决定跨模态推理迁移；过密或过疏时间网格均不利，中间帧率配合中层对比对齐更匹配文本原生推理动力学。

## 点评
把“模态差距”可控地拆成帧率与对齐层两个旋钮，并用 factorized FSQ 让低帧率可扫，实验设计干净。强在信息率恒定下的 U 形规律；点评须注明：**PDF 抽取在实验后半（TTS/S2S 细节表）被截断**，S2S 具体数字仅能依摘要，不宜补编未出现的分数。
