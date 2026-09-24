# Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades

- 论文编号：1821
- 报告人：Shinyoung Sun
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26f_interspeech.pdf

## 问题
实时字幕需低延迟与稳定译文。段级云端级联中，激进端点检测抬高请求率，可超出服务容量形成 backlog avalanche——排队延迟主导，使“更快”设置在稳态下更慢。系统评测常只报单一端到端延迟，混淆首字延迟与稳定字幕延迟。

## 方法
提出 RST：可复现 KO→EN 字幕流水线，区分 time-to-first-text（latency first）与 time-to-stable-text（latency stable）。在完整 FLEURS KO→EN（2851 clips）上回放评测；2×2 级联（whisper-1 / gpt-4o-transcribe × gpt-4.1-mini / grok-4-fast）；对比 fast vs stable 端点预设并扫 hangover/min 时长；定义运营阈值为 median RTF≤1 的最激进设置。另做 Whisper 提示消融。

## 实验与结果
fast 预设 median RTF≫1（如约 24–52），latency stable 可数十秒并随时间累积；stable 预设 RTF 可 ≤1，首字/稳定延迟约 1–3 s 量级且质量更高（BLEU/chrF）。Whisper 滚动/静态提示在短块流式下 CER +14–17 pp，并可泄漏指令。吞吐稳定是低延迟 LLM 级联的必要条件。

## 结论
端点粒度–吞吐稳定–上下文完整构成三难；应优先保证 median RTF≤1 的稳定区，再追求激进延迟。提示条件在短块流式 ASR 上可能有害。

## 点评
把“快设置变慢”量化成 backlog 机制，并拆分 first/stable 延迟，对工程运维直接可用。评测绑定特定云 API 与 KO→EN，外推需重标定阈值。
