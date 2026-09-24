# MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion

- 论文编号：1961
- 报告人：Guobin Ma
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ma26c_interspeech.pdf

## 问题
MeanVC 的 chunk 自回归去噪训练加倍序列长度、小块质量差，且 MRTE 直接吃参考 Mel，对低质参考敏感；160 ms 块端到端延迟约 211 ms。

## 方法
MeanVC 2：（1）Future-receptive chunking（FRC）按 DiT 层调度 past/future 注意力掩码，去掉 clean-chunk teacher forcing，支持 40 ms 块+有界未来上下文；（2）Universal Timbre Token Encoder（UTTE）由全局说话人嵌入建 UTT key–value，用 BNF 查询经交叉注意力取细粒度音色，降低对参考 Mel 质量依赖。仍用 mean flows 1-NFE。约 18M 参数。

## 实验与结果
Table 1：MeanVC 2 延迟约 109.9 ms，SSIM 0.710、SMOS 3.89、DNSMOS 3.89，全面优于同约 80 ms 输入窗的 MeanVC(80)；相对 MeanVC(160) CER/NMOS 略逊但延迟近半。消融：去掉前向掩码 CER 飙至 20.65%；去掉 UTTE SSIM 降至 0.682。参考鲁棒实验显示 UTTE 优于 MRTE。

## 结论
FRC+UTTE 使流式零样本 VC 在约 110 ms 延迟下显著提升相似与稳健性，优于原 MeanVC。

## 点评
同时打训练友好度、短块上下文与参考质量三个痛点，产品向很强。有界未来上下文是延迟–质量的明确旋钮。
