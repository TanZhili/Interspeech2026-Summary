# A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus

- 论文编号：2096
- 报告人：Yuan-Fu Liao
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cho26b_interspeech.pdf

## 问题
台语（Taigi）标注稀缺；大量在线视频是台语语音 + 画面硬编码繁中字幕、无独立字幕文件，常规 ASR/OCR 难以自动建库。

## 方法
多模态半监督：预处理用 PaddleOCR 抽字幕并按时码切成（文本、帧、语音）三元组；trimodal AVLM（SigLIP + Whisper Large-V2 台语微调 + Qwen2.5，早期融合，LoRA）与 OCR 各出候选；CER 过滤共识对后，用 Qwen2.5-VL 按错误模式提示并参照原图融合伪标签，迭代微调 AVLM；强制对齐精修边界。下游用所得语料微调 Whisper 与 Qwen2.5-14B 翻译。

## 实验与结果
PTS-Taigi 监督：AVLM CER 7.46%，优于 VLM 10.26%、ALM 35.29%，对模糊/噪声更稳。Golden Set 迭代：AVLM CER 36.8%→9.3%（融合约 9.4%），提取量升至池中约 87%（434h）。再扩得约 860h 语料：Whisper 台语→中文 CER 57.8%→37.8%；约 590k 平行句微调后 BLEU 0.2016→0.4033。

## 结论
音视频语言融合 + VLM 共识伪标签可规模化构建跨语言台语–中文字幕语料，并显著提升下游转写与翻译；方法可迁移其他低资源场景。

## 点评
针对“语音语言≠字幕语言”的硬编码设定，用音频作视觉识别约束、用 VLM 化解 OCR/幻觉，工程闭环完整。Golden Set 域外起分很差、迭代后逼近监督，说明半监督主要在修域移。伪标签仍依赖 OCR–AVLM 共识阈值，极端视觉损坏时召回会掉；台语 ASR 再对齐中文建 MT 语料会引入二次误差。
