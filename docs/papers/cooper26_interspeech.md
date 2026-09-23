# A Large-Scale Dataset of Listener Impressions of Emotional TTS

- 论文编号：1521
- 报告人：Erica Cooper
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/cooper26_interspeech.pdf

## 问题
自动语音质量评估（如 VoiceMOS/UTMOS）主要基于中性合成语料（BVCC、SOMOS），难泛化到情感 TTS。情感系统除自然度外还需评情绪匹配度，但公开情感听评结果稀缺，自然情感语料（IEMOCAP、MSP-Podcast）又无合成样本。

## 方法
构建大规模听评数据集：18,208 条五类情绪样本，来自 13 套 SOTA 合成系统与自然情感语音；262 名美式英语母语听者，每条约 4–9 分（多数 7 分）。材料覆盖 ESD 自然/合成、DailyTalk 对话合成、开源克隆与文本提示 TTS、API（Gemini）等；音量统一用 sv56。收集 QMOS、EMOS、自由感知情绪类别，以及 valence/arousal/dominance（SAM）。测试分三部分以降低疲劳。

## 实验与结果
组内系统排名给出 QMOS/EMOS（跨组不宜直接比）。感知目标情绪比例与 EMOS 相关达 0.92；VAD 分布相对 ESD 自然语音的 EMD 与 EMOS 强相关。零样本预测：UTMOS 对 QMOS 系统级 SRCC 总体 0.80（Angry 较弱）；Emotion2vec 概率对 EMOS 总体约 0.81–0.82；Gemini-as-judge 对 EMOS 总体 0.84。VAD 零样本相关仅中等（valence 0.45、dominance 0.42、arousal 0.58）。

## 结论
作者给出首个面向情感合成语音的大规模多维听评数据集，并将公开以支持自动评估模型；现有 MOS/情绪/LLM 预测器有一定相关，但仍有明显改进空间且随情绪类别波动。

## 点评
贡献在「评测基础设施」而非新合成器：把质量、类别匹配与 VAD 放在同一批合成+自然样本上，正好填补情感 TTS 客观指标训练数据的空白。分析也提醒跨系统公平比较受文本/说话人条件限制。脆弱点：听者与语种偏美式英语；部分合成条件不一致使「系统排行」只宜作资源而非严格 SOTA 榜；零样本预测结果说明 Angry 等类别仍是难点。
