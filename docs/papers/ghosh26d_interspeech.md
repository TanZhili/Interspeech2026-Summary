# ASR-Synchronized Speaker-Role Diarization

- 论文编号：880
- 报告人：Bongjun Kim
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ghosh26d_interspeech.pdf

## 问题
医患等场景更需要 doctor/patient 角色日志而非 speaker-1/2；单换能器串行出词+角色会伤 ASR，而角色日志与说话人日志对声学/语言线索依赖不同。

## 方法
冻结 ASR 换能器，训练同步 RD 换能器：分析显示 RD 更依赖语言；故用任务专用预测器（ASR 用 CNN、RD 用 RNN）、更高层 ASR 编码器特征喂 RD，并以 1-best ASR 强制对齐路径上的交叉熵替代 blank-shared RNNT。评私有 DoPaCo 与公开 SiMeCo。

## 实验与结果
DoPaCo 上相对最佳基线相对降 R-WDER 约 6.2%（P3 达 6.1 vs B2 的 7.8）；SiMeCo 相对约 4.5%（微调后 2.1）。相对初始同步 SD 式设置，更高层特征与 1-best CE 带来更大相对降幅（文中累计可达约 19%/54% 量级于中间对比）。ASR WER 因冻结基本不变（约 15.67）。

## 结论
ASR 同步角色日志可行且不必牺牲识别；相对说话人日志，角色任务应注入更多语言上下文并简化对齐损失。

## 点评
先实证“RD≠SD”再改架构，方法叙事干净。强在保 WER 与双库结果；弱在角色集偏医患双角色，出域 SiMeCo 未微调时仍难。
