# An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation

- 论文编号：1244
- 报告人：Haoran Wang
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26w_interspeech.pdf

## 问题
高吞吐推理引擎面向单流文本自回归，难原生支持 SpeechLM 的多码本 delay-pattern 交织采样、波形解码，以及 CFG 双路前向带来的吞吐腰斩与调度同步开销。

## 方法
基于 vLLM 连续批处理：主–辅分解，仅一条码本流走引擎标准管线，其余 S−1 流在模型内采样并缓存；请求结束后 delay 解交织，GPU 内嵌声学解码器直接出波形。用每请求相位状态机（text / transition / audio / drain）与动态词表掩码管理文–音混合输出。CFG 采用 Paired Request Co-Scheduling：条件与无条件 companion 同批共享一次 backbone 前向，仅在音频相位合并 logits，采样 token 同步写回 companion。在 Bagpiper、OpusLM、OpusLM-Dialogue 上验证。

## 实验与结果
单卡 H100 80GB、FlashAttention-3。相对顺序 PyTorch：Bagpiper decode 约 52.7→5694.5 tok/s，OpusLM 36.5→4582.9，OpusLM-Dial. 53.9→5870.5；MFU 最高约 9.95%。FP32 下与参考实现 token 序列一致；BF16+FA3 有精度漂移但不伤聚合质量（MMAU-mini、LibriSpeech ASR/TTS、Eval2000 UTMOS 与基线接近）。Bagpiper CFG：decode 约 4952→3960 tok/s，约保持非 CFG 吞吐的 80%。

## 结论
在连续批处理引擎内原生支持多流音频生成与端到端合成，并用成对共调度吸收 CFG 开销；跨多种 SpeechLM 最高约 108× 生成吞吐，修改主要落在模型与 logit 层，便于复用。

## 点评
把 delay-pattern 与 CFG 嵌进现有调度/KV 基础设施，而不是另起一套服务，务实可落地。吞吐数字依赖高并发与 H100；质量表中个别指标（如对话 UTMOS）略降，说明精度与批处理路径仍需任务侧核对。开源分支便于复现。
