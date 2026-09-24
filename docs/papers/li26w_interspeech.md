# Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization

- 论文编号：1340
- 报告人：Yudong Li
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/li26w_interspeech.pdf

## 问题
流式零样本 VC 中，信息瓶颈去音色常丢掉韵律，被迫注入 \(f_0\) 等并缓存未来帧（如 StreamVC 约 60 ms 算法前瞻）；既有说话人扰动又难在“音色泄漏 vs 效用保留”间取得优平衡。

## 方法
Zero-VC：训练时用现成 Speaker Anonymization（SA）扰动源语音以压泄漏、保语言/韵律，再经严格因果流式编码器（20 ms 帧移、零前瞻）提内容；WavLM-large 第 7 层 + 可学习注意力池化提参考音色；因果卷积 HiFi-GAN 式解码器注入全局音色。对抗训练后推理丢弃 SA 与判别器，chunk-by-chunk 缓存因果状态。

## 实验与结果
相对 LSCodec/Seed-VC 扰动，SA 中间音频 SS-S 最低（0.119）且 FPC 较好；训成 VC 后更近“低泄漏高目标相似度”理想区。零前瞻系统相对非流式开源模型：SS-S 0.171、SS-R 0.521、SMOS 最高，WER 3.96%、FPC 0.688，CPU RTF 0.063；算法延迟 20 ms，低于 DualVC3/StreamVC/RT-VC 报告值。无 SA 时对 40–60 ms 前瞻依赖更强。

## 结论
SA 作扰动可同时改善泄漏–效用权衡，并支撑真正零前瞻流式架构，把算法延迟压到单帧下限。

## 点评
把匿名化目标显式对接流式 VC 的核心权衡，延迟叙事有力。训练仍依赖外部 SA 预处理；端到端并入 SA、跨语与总系统延迟仍是后续点。
