# Delayed-Commitment Online Speaker Tracking for Robust Many-Speaker Diarization

- 论文编号：898
- 报告人：Youngki Kwon
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kwon26_interspeech.pdf

## 问题
在线说话人日志在多人场景易假注册/坏质心；固定容量模型说话人数封顶，聚类法虽开放但随人数增常劣化，且既有基准偏双人。

## 方法
DC-OST：每条嵌入立刻出标签，但新说话人质心延后至缓冲攒满 K 条再 medoid 提交；距离阈值随已注册人数自适应升高（有上限）抑制虚假注册；配套系统 VAD 与 1.5 s/0.5 s 步长嵌入，延迟 0.5 s。在 VoxConverse、VoxSRC-23（最多约 21/28 人）评 DER，并按说话人数分层。

## 实验与结果
系统 VAD 下 0.5 s 延迟 DER：VoxConverse 9.53%、VoxSRC-23 9.12%，优于 DIART 与 Sortformer；按人数分析显示误差更平稳（Std(∆) 一致性更好），基线随人数上升更易崩。消融称延后提交贡献大于自适应阈值。

## 结论
延迟提交质心 + 自适应阈值可在无人数上限的在线聚类中维持多人稳健性，适合真实会议流式转写。

## 点评
把“立刻出标签”与“晚点建质心”解耦，直接打多人在线痛点。强在多人基准与分层分析；弱在仍依赖嵌入与系统 VAD 质量，重叠话者处理非本文重点。
