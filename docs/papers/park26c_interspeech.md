# LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features

- 论文编号：952
- 报告人：Jonghyeon Park
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26c_interspeech.pdf

## 问题
痴呆相关言语改变跨声学、时间、音系与语篇多维；既有方法常单视角或晚融合，限制跨症状综合推理。

## 方法
将四类语音衍生信号写入统一提示：Whisper ASR 转写+对齐停顿标记、语篇主题/聚类线索、时间流利统计、不流畅感知音素序列；对 LLM（最佳 Qwen3-14B）做 LoRA（r=8）微调做 AD/CN 分类，无需模态专用编码器。评测 ADReSSo。

## 实验与结果
最佳多视角 LoRA 模型说话人级 F1 90.14%。逐步消融显示各视角互补；仅转写基线约 81.48%，加入停顿、主题、音素等逐步提升至满分配置。

## 结论
结构化多视角提示 + 参数高效 LLM 适配可统一整合异质言语线索，在 ADReSSo 上达到强判别性能。

## 点评
用单一 LLM 做跨视角推理，避免复杂多编码器融合工程。性能与 jung26 同数，属同一团队互补路线；对对齐与音素识别前端质量依赖高，低资源语言可迁移性待验。
