# MTC-AVSR: Compressed-Token-based Audio-Visual Speech Recognition and Translation with Contrastive Language Alignment

- 论文编号：266
- 报告人：Lusi A
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/a26_interspeech.pdf

## 问题
LLM 系 AVSR 依赖高分辨率多模态 token，计算与延迟高。MMS 等压缩虽有效，但多仅服务识别，未验证压缩 token 能否同时支撑识别与语音翻译，也少有把源语对齐 token 映射到多语言空间而不扩大 LLM 参数。

## 方法
**MTC-AVSR** 三阶段：
1. **多模态压缩**：音视频前端 + AV-QFormer，按约 3.5 token/s 动态分配 query（MMS 式）。
2. **Language Adaptation Module (LAM)**：共享多语言词表 + 两层门控交叉注意力，把压缩 token 重编码为多语言表示；**TCAL** 对比损失把 adapter 输出对齐到词表条目。
3. **任务条件解码**：冻结 LLM（QLoRA）前缀 `<recognize><En>` 或 `<translate><lang>` 切换 ASR/翻译。

分阶段训练：先源语对齐锁定编码器，再在冻结缓存上做跨语适配（\(\lambda\) 从 1.0 anneal 到 0.3）。

## 实验与结果
LRS3+VoxCeleb2（1759h）+ MuAViC En-X。LRS3 干净 WER 0.74%（与 MMS-LLaMA 持平），0 dB babble 2.0%。MuAViC 干净：Es 28.1、Fr 26.3、Pt 21.8 等达文中所称 SOTA；噪声下平均仍强于 Whisper-Flamingo 变体。消融：LAM→词表→TCAL 逐步抬 BLEU/降 WER；3B 较 1B/8B 在干净上更优权衡。LAM 比全量 CMT 更省显存且效果更好。

## 结论
同一超压缩 MMS token 流可同时做 AVSR 与 En-X 翻译；轻量 LAM+TCAL 在冻结编码器下实现多语言切换，说明压缩表示仍保留跨任务语言容量。

## 点评
核心问题「压缩后还剩多少跨任务语义」问得很准，用多任务提示 + 对比词表对齐给出可操作答案。强在单模型多任务与效率；脆弱点在噪声翻译对比因对方噪声文件未公开而不完全对等，以及依赖 Whisper 伪标签 VoxCeleb2。
