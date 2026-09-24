# I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance

- 论文编号：2807
- 报告人：Ritvik Shrivastava
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yadav26b_interspeech.pdf

## 问题
现有 AudioLLM 只在被查询时响应；面向听障辅助等可穿戴场景，需要根据单一自然语言意图持续监听并自主决定何时打断用户。

## 方法
Interrupt and Silent Modeling（ISM）：在 LLM 解码中引入 `<interrupt>` / `<silent>` 特殊词元，覆盖四态——起振检测、持续相关触发、无关抑制、去重。模型无关，应用于 Qwen2-Audio-7B。定义主动辅助评测指标与流式协议。

## 实验与结果
ESC-50：interrupt F1 99.6%，去重 recall 完美。噪声厨房 Epic-Sounds：无域特训仍获最高 interrupt F1，且不过度触发/抑制。流式评估平均延迟约 3.5 秒，显示实时可行性。

## 结论
用两个特殊词元即可把主动监听嵌进标准 AudioLLM 解码，近完美完成环境声主动辅助原型任务。

## 点评
任务形式化清楚，评测覆盖起振与去重，比单纯分类更贴辅助场景。延迟 3.5 s 对紧急告警可能偏慢；开放环境误报代价与意图表述鲁棒性仍待现场验证。
