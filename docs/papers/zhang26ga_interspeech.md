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
