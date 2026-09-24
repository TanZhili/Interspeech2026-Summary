# Benchmarking Speech Systems for Frontline Health Conversations: The DISPLACE-M Challenge

- 论文编号：3255
- 报告人：Dhanya E
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/e26_interspeech.pdf

## 问题
一线社区健康对话（印地语、自发、嘈杂、重叠、语码混合）与医院受控英语临床语料差异大，缺统一基准覆盖说话人日志、ASR、主题识别与摘要的端到端链路。

## 方法
DISPLACE-M Phase-I：发布约 40h 开发 + 15h 盲测印地语一线健康会话；四赛道——说话人日志（DER）、ASR（tcpWER 等）、主题识别、对话摘要（ROUGE-L）；提供基线（IndicConformer、ASR–LLM 主题/摘要等）。12 国际队参赛；参考 Gemini 2.5 Pro、Sarvam Saaras v3。

## 实验与结果
ASR：最佳队 CER/WER/tcpWER 10.59/18.15/18.63，优于微调 IndicConformer 基线（tcpWER 20.23）与 Gemini；日志赛道前四队超 Baseline-2。主题识别 ROUGE-1/L 最佳约 0.46/0.44（基线约 0.15/0.14）；摘要 ROUGE-L 最佳约 0.20（基线 0.18，Gemini 0.21）。域内微调与医学术语后处理是 ASR 关键。

## 结论
挑战建立了印地语一线健康会话的可复现基准与排行榜；Phase-I 显示 ASR/日志有明显提升空间，高层理解任务仍难。后续阶段将延续。

## 点评
把社区一线、语码混合与多任务串成统一评测，填补印度健康语音空白。摘要/主题绝对分仍低，反映上游 ASR 误差与任务定义难度；发布数据规模相对会议语料仍有限，但对催生域适配研究已够用。
