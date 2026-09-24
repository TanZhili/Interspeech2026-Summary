# VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion

- 论文编号：2712
- 报告人：Aastha Sharma
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26b_interspeech.pdf

## 问题
多数 spoofing/deepfake 基准仍依赖 2024 年前合成系统，与 LLM 时代 TTS/VC 及真实传输后处理产生的伪迹分布不匹配，导致在旧数据上很好的检测器在部署时被高估。需要能刻画这种时间漂移与后处理偏移的评测基准。

## 方法
构建双语（英/西）基准 VoxENES 2026：真实语音来自 LibriSpeech（EN）与 VoxPopuli（ES），统一 16 kHz mono、截断/补零至 4 秒；合成侧含 7 种 TTS（如 VoxCPM 1.5、Qwen3-TTS、GLM-TTS、Chroma、VibeVoice、CosyVoice 3、Chatterbox）与 3 种 VC（Seed-VC、OpenVoice v2、RVC v2），共 4,600 条原始合成，再经 10 种后处理（MP3/AAC、白噪/babble、重采样、变速、响度归一等）扩至 46,000 条增强合成，总 53,628 条。在不微调的前提下评测 8 个预训练检测器（AASIST2、RawNet2、多种 Wav2Vec2 变体、AST-ASVspoof5、ECAPA-TDNN 异常打分等），报告 EER/准确率及按合成方法、后处理的分解结果。

## 实验与结果
- 整体最优为 AST-ASVspoof5：EER 28.98%、Acc 75.94%；多数模型接近或差于随机（如 AASIST2 EER 57.86%，存在预测反转）。
- 后处理影响不均：白噪可降低部分模型 EER（如 AST 从 26.7%→17.4%），MP3 则使 AST 升至 48.4%。
- Seed-VC 最难：无一检测器 EER 低于 41%；ECAPA 在部分 TTS 上较好（如 GLM-TTS 10.2%）但在 VC 上大幅退化。

## 结论
作者认为现有反欺骗对策高度依赖脆弱、基准特异伪迹，面对 LLM 时代生成器与常规后处理仍远不够；VoxENES 2026 可作为持续跟踪合成前沿的测试床。

## 点评
工作本质是补齐“时间漂移评测”，用固定预训练、零微调暴露 OOD 落差，比只报旧基准 SOTA 更贴近部署。解读时需注意各检测器训练语料不同，绝对 EER 不宜当严格 head-to-head；后处理偶发“变好”也说明模型可能在换一套捷径线索而非真正学会真伪判别。
