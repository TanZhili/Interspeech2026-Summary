# Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation

- 论文编号：1902
- 报告人：Eric Bezzam
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/srivastav26_interspeech.pdf

## 问题
ASR 开源与商用模型、数据集激增，开发者难选基线与公平对比方式；多数基准偏英语短音频，跨工具包评测不统一，单 WER、单数据集不足。

## 方法
Open ASR Leaderboard 提供可交互排行榜与开源评测脚本：截至 2026-03-27 覆盖约 86 个系统（26 家机构）、11 个数据集；统一跨 ESPNet / NeMo / SpeechBrain / Transformers 与多家商用 API。三条赛道——英语短音频（<30 s）、多语短音频（德/法/意/西/葡）、英语长音频（>30 s）。报告强归一化后的平均 WER 与 RTFx（音频总时长/转写时间）；社区以 PR 提交评测脚本与自报指标，经维护方复验后上榜。

## 实验与结果
短英：Conformer/FastConformer + LLM 解码整体平均 WER 更优（如表中 Zoom Scribe v1 约 5.80、Cohere Labs Transcribe 5.84、IBM Granite Speech 4.0 1B 5.87 等），但 RTFx 常低于 TDT/CTC；Parakeet TDT 0.6B v2 等吞吐更高但 WER 排名靠后。多语：闭源 ElevenLabs Scribe v2 平均 WER 约 2.67 领先；开源中 Voxtral Small 24B 约 3.70 等。长音频：闭源优势更大（如 ElevenLabs 9.05），开源中 Conformer 系仍较强，CTC/TDT 更适合大批量。约 31% 开源模型沿用 Whisper encoder；扩展语种覆盖有时伴随英语 WER 变差。

## 结论
作者认为标准化归一化与 RTFx 使准确率–效率可比较，并开源代码与数据加载以支持可扩展社区评测；未来拟扩语言/领域、加更多指标与私有评测集，并区分是否需保留不流畅的 verbatim 任务。

## 点评
基础设施型贡献：跨工具包对齐与双指标排序对选型很实用。正文也提醒架构结论与训练数据/规模纠缠；强归一化会抹掉标点/大小写/不流畅差异，不适合测偏好格式能力。
