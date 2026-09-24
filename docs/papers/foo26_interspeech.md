# All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation

- 论文编号：913
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/foo26_interspeech.pdf

## 问题
LALM 基准高分未必等于真听懂：题目可能靠文本先验作答，或仅需局部声学片段，现有“静音替代”等方法有混淆。

## 方法
双轴诊断：Text Prior——对比 Full / 无音频 None / 文本骨干 TB，定义 RTP=Acc_none/Acc_full；Audio Reliance——将音频均分为 N 段独立评测，算保留率 RN，并按 Full/None/片段正确性划分 TS、FS、XS、AH、UN。在 MMAU、MMAR、MMAU-Pro 上评 8 个 LALM。

## 实验与结果
无音频仍保留约 60–72% 满分准确率（模型平均 RTP）。需音频的题目中，仅约 3.0–4.2% 为跨段必需（XS），多数片段已足够。TS 占约 26–39%；语音类 Full–None 差距较大，部分 open/指令类行为不同。多模态训练后 None 常高于 TB，文本先验被强化。

## 结论
当前基准大量混入文本先验与局部线索，不宜直接等同整体听觉理解；建议报告文本先验基线与音频依赖保留率以改进评测。

## 点评
把 VQA/NLI 的“无模态基线”系统迁到音频，对基准可信度是一记清醒剂。片段划分较粗，未覆盖真正长程依赖任务设计；指导原则清晰，落地需基准作者配合重标。
