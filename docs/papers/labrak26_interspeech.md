# Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization

- 论文编号：2901
- 报告人：Yanis Labrak
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/labrak26_interspeech.pdf

## 问题
长上下文音频推理（>5 分钟）缺少训练与评测资源；开放式摘要/笔记类任务难用自动指标，真实临床音频又受隐私限制。现有公开资源规模小或仅有文本，难以支撑长对话 SOAP 笔记生成。

## 方法
全开源权重流水线三阶段：人格属性采样（724 条主诉等）→ Gemma3-27B 多轮对话生成 → Qwen3-TTS 人格条件声音克隆，再经重叠/停顿、音效、scaper 时间线与 PyRoomacoustics 诊室 RIR、Opus 压缩等声学仿真。参考 SOAP 先抽 grounding 事实 JSON 再生成笔记；评测用两阶段 LLM-as-a-judge（Kimi K2）及 ROUGE/医学概念 F1。释放 Synth-DoPaCo：8,800 对话、1,329 小时音频，均分约 9 分钟。

## 实验与结果
湿音频上 Whisper Large V3 WER 约 2–3%，Qwen3-ASR 约 10–14%。参考笔记 faithfulness 5.0；级联（Whisper/Qwen3-ASR + Qwen3-Thinking）faithfulness 约 3.1–3.3，E2E Omni 约 2.7；逐 claim 幻觉率 E2E 约 32%、级联 22–24%、参考约 1%。表面 ROUGE 上 E2E 可更高，但忠实度与简洁度更差。UTMOS 与真实 mock 接近（1.27 vs 1.28）。

## 结论
合成管道可同时作训练与可控评测资源；当前开源系统中级联因更高忠实度、更低幻觉更可取，瓶颈在长对话临床推理而非近天花板的 ASR。局限包括参考笔记为 LLM 生成、仅英语双人首诊、声学难度可能仍低于真实临床。

## 点评
把隐私受限的临床长音频任务做成可复现的 sim2real 评测床，并强调 faithfulness 优于表面重叠指标，方向对。强在人格多样性、声学仿真与 grounding 笔记流程；弱在参考与裁判都偏 LLM、WER 偏低暗示难度可能不足，外推真实部署需谨慎。
