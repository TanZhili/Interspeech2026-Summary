# Audio Language Models

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：8
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场由一篇面向 ASR 的 speech-LLM 进展邀请报告与四篇系统/评测工作组成。邀请报告在标准 speech-LLM 已于主要榜单成熟的前提下，聚焦释放 LLM 潜力、长时建模、解码加速，以及无编码器 speech-LLM 通向原生多模态。论文侧则分别处理离散化信息损失（混合离散—连续 codec）、流式文本对齐语音分词、Large Audio Language Model 思维链忠实性，以及印度语言情境提示是否真正被 AudioLLM 利用。

方法上，HybridCodec 用时序压缩离散 token 加降维连续残差，离散域自回归与非自回归连续残差上采样结合；TASTE-S 把 CTC ASR 接入编码器并改造单元解码器以支持流式。评测上，忠实性框架定义无幻觉、整体性与专注聆听等音频忠实准则并用音/链干预基准；IndicContextEval 用七级递进提示（含对抗错误实体）检验情境利用。整体趋势是：从“接上 LLM”转向效率、流式、忠实推理与情境是否生效。

## 论文技术总结

# Recent advances in speech language model for ASR

- 论文编号：
- 报告人：Jinyu Li
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
在 LLM 推动下，学界与工业界正把语音模态接入 LLM，形成 speech LLM。本报告聚焦 speech-LLM 用于自动语音识别（ASR）的近期进展，并讨论标准方案成熟之后仍待释放的能力与新架构方向。

## 方法
摘要称标准 speech-LLM 路线已趋成熟，并在主要榜单上取得领先表现；报告将深入：如何更充分释放 LLM 潜力、长语音建模、解码加速，以及无编码器（encoder-free）speech-LLM 的突破——后者通向更接近原生多模态、像处理文本一样处理语音的语言模型。

## 实验与结果
摘要提到主要榜单上的领先结果，但未给出具体榜单名、数据集或 WER 等数字。

## 结论
ASR 向 speech-LLM 整合已进入可用阶段；下一步重点包括长语音、加速，以及向无编码器原生多模态形态演进。

## 点评
问题从「能否做好 ASR」转向「成熟后的能力边界与架构简化」。无 PDF，无法核对「榜单 SOTA」的具体出处与数字。


# HybridCodec: Modeling Discrete and Continuous Representations For Efficient Speech Language Models

- 论文编号：2784
- 报告人：Artem Ploujnikov
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ploujnikov26_interspeech.pdf

## 问题
离散音频表征便于接入 LLM，但量化损失细粒度声学信息，低帧率下说话人与韵律退化明显；纯连续方案又难统一多任务。

## 方法
提出 HybridCodec（扩展 FocalCodec）：离散 BSQ 路径捕语义骨架，连续残差焦点编解码捕量化损失细节，支持 50–6.25 Hz。HybridLM（GPT 式）用 AdaLN 在同骨干上做离散 AR + 连续残差单步 NAR，级联推理减少 AR 步数。ECAPA 说话人嵌入条件化；LibriTTS 上训，覆盖 ASR/TTS。

## 实验与结果
重合成：HybridCodec 在多帧率保持高 UTMOS/SpkSim，6.25 Hz 仍可用。下游：相对离散-only，混合在低帧率大幅恢复 UTMOS/SpkSim（如 6.25 Hz SpkSim 0.707→0.834），并改善 ASR WER；AR 步数约按下采样因子缩减。

## 结论
离散粗骨架 + 连续残差细化可在统一 Transformer 中兼顾 LLM 效率与声学保真，尤其利于超低帧率。

## 点评
把“先粗后细”做成同模型 AR/NAR 多路，工程上干净。强在说话人保持与步数节省；6.25 Hz 上 dWER 仍高，说明极低率语义仍吃紧。证据主要在干净 LibriTTS，噪声域外推待证。


# TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling

- 论文编号：1686
- 报告人：Liang-Hsuan Tseng
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26b_interspeech.pdf

## 问题
文本–语音联合建模受长度不匹配困扰；TASTE 用文本对齐 token 缓解，但依赖外部离线 ASR 与非因果解码，无法流式。

## 方法
提出 TASTE-S：编码器内置 CTC ASR 即时取文本；Aggregator+VQ 生成文本对齐语音 token；解码端因果 Unit decoder（N:M 交错）+ 因果流匹配声码器。两阶段训练：先用金标转写训 Aggregator/Decoder，再联合适配 CTC 预测。数据约 Emilia 400 h + LibriTTS 600 h。

## 实验与结果
与 TASTE 质量相当（CTC 路径 WER≈4.1%、UTMOS≈4.11、说话人相似≈0.88），编码 RTF 从依赖外部 ASR 的约 0.117 降至约 0.002；对转写噪声更稳，支持长篇编解码。交叉注意力仍保持文本–语音对齐。

## 结论
内置 ASR + 因果解码使文本对齐分词可流式落地，且不牺牲重建质量，利于实时 SLM。

## 点评
把“对齐”与“流式”同时做进分词器，比事后 padding/交错更干净。两阶段+联合训练对 CTC 误差鲁棒是关键。重建评测偏 LibriSpeech clean；真实对话噪声与多语仍待验。


# Investigating Faithfulness in Large Audio Language Models

- 论文编号：1533
- 报告人：Pooneh Mousavi
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/mousavi26_interspeech.pdf

## 问题
LALM 可生成 CoT，但相对输入音频与最终答案是否忠实未知；音频条件可能带来幻觉、局部注意或忽视指令等问题。

## 方法
定义音频忠实三准则：无幻觉听、整体听、专注听，外加 CoT–输出忠实。对 Audio Flamingo 3-Think 与 Qwen2.5-Omni，在 SAKURA/MMAR/MMAU 上做音频干预（噪声 SNR、随机/引导掩蔽、对抗语音提示）与 CoT 干预（改写、填充、早答、注入错误）。用答案一致性与 LLM-as-judge 评 CoT 一致性。

## 实验与结果
极端噪声下模型仍常产生看似合理但未接地的推理；掩蔽与对抗提示可大幅改变准确率与一致性，显示对局部线索或注入答案敏感。CoT 常与最终答案一致，但对音频接地较弱，易受扰动。提示存在多模态脱节。

## 结论
LALM 的 CoT 更像与答案对齐的叙述，未必忠实反映音频决策过程；需干预式评测而非仅看准确率。

## 点评
把文本 LLM 忠实性干预迁到音频条件，问题设定重要。依赖 LLM 裁判与自动化解析 CoT，可能引入评判偏差；两模型样本也限制外推到闭源商用系统。


# IndicContextEval: A Benchmark for Evaluating Context Utilisation in Audio Large Language Models Across 8 Indic Languages

- 论文编号：3272
- 报告人：Sakshi Joshi
- 程序：Tuesday 29 September 2026 / Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/joshi26_interspeech.pdf

## 问题
AudioLLM 可用文本提示做语境 ASR，但难分清是真用上下文还是靠预训练参数记忆；既有基准少变提示、少印度语、常合成音。

## 方法
发布 IndicContextEval：约 56 h 自然语音、555 说话人、8 语、23 专业域。七级提示 L0–L6：无语境→语言→域元数据→音频描述→英/本地实体列表→错误实体对抗。评五个模型（含 GPT-4o Transcribe、Gemini 3 Flash、Sarvam Audio、Gemma-3N 等），指标含 WER 与命名实体错误率 NEER。

## 实验与结果
模型间语境利用差异大：本地脚本实体（L5）使 GPT-4o/Gemini/Gemma 的 NEER 显著下降（Gemini L5 最佳约 17.39%）；对抗 L6 回落到接近 L1，显示依赖正确实体。部分模型几乎忽略提示或对提示不稳定。

## 结论
需显式评测 AudioLLM 的语境 grounding；IndicContextEval 的分级与对抗提示可区分记忆与利用。资源已公开。

## 点评
L0–L6 递增与对抗实体设计干净，直接回答“提示有没有用”。自然多语专业域是稀缺点。音频描述由 Gemini 生成，可能对同厂模型偏利；实体列表质量也会影响结论。

