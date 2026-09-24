# Beyond WER: A Paired Acoustic Stress Test for Ambient Clinical Scribes

- 论文编号：606
- 报告人：Xiao-Hang Jiang
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26c_interspeech.pdf

## 问题
环境临床 scribe（ASR→LLM）用 WER 评稳健性会掩盖安全风险：小词错误可翻转否定、剂量、分诊，而 WER 几乎不动。

## 方法
配对声学压力测试：同一对话注入平稳环境噪声（DEMAND）与非平稳语义干扰（MUSAN 人声）多 SNR，下游 LLM 配置冻结。将否定翻转、数字/单位、非语音污染等原因侧触发映射到分诊漂移、红旗遗漏、Unsafe Rate、SCER、ErrProp 等结果侧安全指标；并测轻量 agent 缓解（无需微调）。

## 实验与结果
干净参考 Unsafe 约 13.6%、WER 16.54%。平稳环境噪声 WER 仅小幅升（摘要称约 +0.71pp）即可使 Unsafe 近翻倍（如 15 dB 环境噪声 Unsafe 27.21%）。语义干扰下 WER 与 Unsafe 同步恶化（5 dB Unsafe 91.54%）。缓解策略在噪声下降低安全劣化。

## 结论
临床不变性应替代纯转写精确度；语义扭曲而非聚合 WER 是下游安全失败主因。轻量缓解可在不微调模型时部分止血。

## 点评
配对设计干净隔离声学因果，对“WER 好看就安全”是有力反例。依赖 LLM 裁判与 claim 抽取，指标本身有噪声；真实诊所噪声分布与合成注入可能有差。结果对部署 ambient scribe 的安全评测清单很实用。
