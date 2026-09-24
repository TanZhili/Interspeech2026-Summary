# Neural Audio Codec Architectures

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：6
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦神经音频编解码架构，核心矛盾是：下游语音/音频语言模型需要低帧率、语义可分的离散表示，而极端时间压缩又容易损伤可懂度与频谱细节。多篇工作在低码率下同时追求高保真重建与信息解耦（语义、音色、韵律、残差等流）。

解耦成为主线：多流残差、语义–声学分层码本、说话人解耦加基频注入、以及固定长度全局说话人令牌配合动态帧率，都试图降低说话人信息泄漏、减轻下游 SLM 建模负担，并支持变声与可控合成。低帧率方面出现 5 Hz 级超低帧率编解码，以及把固定帧率自编码器转为动态帧率瓶颈的“弹性时间”机制，以适配信息密度不均的区域。

训练策略上，有工作用预训练理解模型编码器做语义引导与自引导提升码本利用率；也有工作强调单阶段优化或相似度驱动的动态帧聚合。总体趋势是：编解码不再只做重建，而是为生成、变声与长上下文建模提供可控、低冗余的离散接口。

## 论文技术总结

# MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement

- 论文编号：301
- 报告人：Jingyu Li
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26c_interspeech.pdf

## 问题
生成用神经编解码常要较高码率；语义/音色/韵律纠缠也限制可控合成与转换。

## 方法
MSR-Codec 将语音编码为四路：semantic、timbre、prosody、residual，多尺度残差逐步融合重建 Mel，再经声码器。基于该 codec 建两阶段轻量 TTS（先语义后韵律细节）。评重建、TTS（WER/SIM）与音色–韵律解耦的声音转换；开源代码与模型。

## 实验与结果
在约 424/524/612 等低码率配置下重建质量有竞争力。两阶段 TTS 相对若干更大模型 WER 更低、说话人相似度更高，且数据需求小、生成更快。VC 实验显示可较独立地迁移音色而不绑死韵律。

## 结论
多流通用残差分解能同时服务低码率高保真与可控生成；解耦能力经 TTS/VC 验证。

## 点评
把 disentanglement 做成显式四流而非事后分析，对 SLM-TTS 管线很实用。码率–质量表与对照系统细节需对照 PDF 完整表；四流设计的训练稳定性与码本利用率是常见风险点。


# OmniCodec: Low Frame Rate Universal Audio Codec with Semantic–Acoustic Disentanglement

- 论文编号：494
- 报告人：Jingbin Hu
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hu26b_interspeech.pdf

## 问题
多数神经 codec 偏语音高保真重建，缺跨语音/音乐/通用声音的低帧率统一建模；高重建质量也不等于语义可信息，限制下游生成。

## 方法
OmniCodec：分层多码本；首批码本注入预训练理解模型（Qwen3-Omni-AuT）音频编码器的语义，其余码本专注声学；self-guidance 提升码本利用率与重建。支持 12.5 Hz 与 6.25 Hz。在 LibriSpeech、GTZAN、AudioSet 子集与下游生成任务相对 Mimi 等对比。

## 实验与结果
同码率下相对 Mimi-16L，OmniCodec-32L（12.5 Hz）PESQ-WB 等多项更优（如约 3.02 vs 2.88），Mel/MCD/主观 MOS 亦有提升；6.25 Hz 变体仍可用。语义侧 PPL 等指标显示表征更利于生成；作者亦指出语音解耦仍有挑战。

## 结论
预训练理解编码器语义注入 + 声学码本分层，可在低帧率全域 codec 上兼顾重建与下游语义效用。

## 点评
把“理解模型编码器当语义教师”接到通用 codec，方向对下游 LM 生成很关键。语音域解耦未完全解决；开源承诺落地后更易复现帧率–码本配置。


# U-Codec: Neural Speech Codec under Extreme Temporal Compression for Fast High-Fidelity Speech Generation

- 论文编号：2398
- 报告人：Xusheng Yang
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26n_interspeech.pdf

## 问题
主流 codec 常 50–75 FPS，自回归 LLM-TTS 每秒需大量前向；极低帧率（如 5 Hz）易损可懂度与频谱细节。

## 方法
U-Codec 目标 5 Hz：Transformer 帧间长依赖（Codecformer）+ 系统扫描 RVQ 深度与码本大小。接入全局–局部层次化 LLM-TTS，在多层 token 上建模依赖。对比高帧率 codec 的重建与 TTS 速度/自然度/相似度。

## 实验与结果
5–12.5 Hz 下 PESQ 具竞争力；接入 LLM-TTS 后相对高帧率 codec 推理约快 3×，相似度与自然度大体保持。验证 5 Hz 离散 token 可用于快速高保真合成。

## 结论
帧间 Transformer + 恰当 RVQ 配置使极端时间压缩可行，显著加速 LLM-TTS。

## 点评
把瓶颈从“码率”明确转到“帧率×自回归步数”，对部署延迟很务实。5 Hz 对瞬态辅音/精细韵律仍可能欠采样；质量–速度折中需按语种与场景复核。


# Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding

- 论文编号：3031
- 报告人：Dimitrios Bralios
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bralios26_interspeech.pdf

## 问题
多数神经音频自编码器虽可变码率，但仍固定潜在帧率，对信息密度不均区域均摊时间预算，序列偏长。

## 方法
提出 Elastic Time（ET）：在冻结预训练自编码器上插 Re-Bottleneck；学轻量因果潜在预测器，决定可跳过并稍后重建的帧；推理用贪心边界选择（亦对比精确 DP）。在约 21.5 Hz 基帧率上按保留比例 ρ 做部署期速率控制，跨多域评 mel 距离与 FAD。

## 实验与结果
ρ∈[0.5,0.99] 对应约 10.75–21.29 Hz 平均帧率。贪心与 DP 接近；相对 CodecSlime 等，多数设置效率–质量更好，AudioCaps 上 CodecSlime mel-d 偶有略优。无需外部语义监督即可部署期调速率。

## 结论
内容自适应潜在抽稀可把固定帧率 AE 变成动态帧率，改善长上下文/生成下游的序列效率。

## 点评
把“可变码率”推进到“可变时间分辨率”，对连续潜在尤其关键。插件式设计友好；边界伪影与预测器误差在极低 ρ 时仍需小心。


# SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion

- 论文编号：3108
- 报告人：Hounsu Kim
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26v_interspeech.pdf

## 问题
说话人解耦 codec 可降码率并支持 VC，但强抑制泄漏常靠多阶段/辅助训练，简单设计又易在局部 token 残留说话人信息。

## 方法
SDP-Codec 单阶段训练：局部 token 来自预训练 SSL（vq-wav2vec）连续预量化特征再经紧凑单码本；全局说话人分支；归一化 F0 经 pitch 编解码注入，全局条件反归一化 + soft-label 音高重建损失。评 16/24 kHz 重建、零样本 VC 与说话人探测准确率。

## 实验与结果
可比码率下重建有竞争力；零样本 VC 在说话人相似度、F0 相关与 MOS 上表现强；对比系统中说话人探测准确率最低，暗示泄漏更少。

## 结论
连续预量化 SSL 特征 + 显式 F0 注入与 soft-label 音高损失，可在单阶段管线中兼顾低码率、解耦与 VC。

## 点评
把“解耦 vs 训练复杂度”折中做实，用探测准确率直接量泄漏，比只报 VC-SIM 更硬。内容保真仍是作者自承短板；下游 SLM 尚未实测。


# A Dual-Stream Discrete Neural Codec with Fixed-Length Global Speaker Tokens and Dynamic Frame Rates for Low-Bitrate Speech Tokenization

- 论文编号：3314
- 报告人：Boyang Zhang
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ga_interspeech.pdf

## 问题
单码本 codec 仍常把说话人与内容缠在同一时变流，抬高下游 SLM 负担；固定帧率对冗余段浪费 token。

## 方法
DySTCodec 双流：单码本时变内容流 + 少量定长全局说话人 token（FSQ，约 52 bps 量级开销）；对约 50 Hz SSL 特征做相似度动态帧聚合（阈值 τ 推理可控），自适应反聚合还原基帧率再波形重建；音色扰动减泄漏，轻量 refinement 抑边界伪影。

## 实验与结果
低码率下可懂度与音质强，bitrate–质量优于固定帧率基线，并保持说话人相似度；跨数据集 VC 有效。消融确认音色扰动与 refinement 重要。

## 结论
全局说话人 token + 动态帧聚合可同时降冗余与说话人–内容纠缠，利于低码率分词与转换。

## 点评
把动态帧率与显式全局说话人流绑在一起，比只做 RVQ 降码更贴 SLM 需求。阈值 τ 的跨语料稳定性、聚合边界对节奏的影响仍需细查。

