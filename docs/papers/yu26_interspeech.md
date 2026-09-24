# Investigating LLMs Behavior in Depression Severity Prediction

- 论文编号：456
- 报告人：Jiawei Yu
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26_interspeech.pdf

## 问题
LLM 少样本是否为抑郁严重度（PHQ-8）提供有效监督仍不清；示范数量增加是否单调变好、错误示范标签是否被利用、全文转写是否必要，均缺系统检验。

## 方法
E-DAIC（275 访谈，PHQ-8 0–24）；Whisper-Large-V3 重转写；五款 LLM，0–10-shot；矛盾标签干预测标签依赖；GPT-5.1 抽取症状聚焦摘要 vs 全文；多轮预测平均。主指标含 CCC 等。

## 实验与结果
增加 shot 收益有限且非单调；对损坏示范标签大多不敏感，暗示示范更像格式线索而非强监督。症状聚焦摘要一致提升 CCC，约省 80% token；弱模型增益更大。预测平均带来稳定提升且不改提示设计。

## 结论
上下文相关性重于示范数量；临床部署宜优先精炼症状相关文本并配合预测平均，而非堆 shot。

## 点评
矛盾标签与 shot 缩放实验直接拆穿“更多示范=更好临床监督”的假设，对 ICL 医疗应用很有价值。摘要抽取本身用强模型，可能引入抽取器偏置；仅文本通道，忽略声学抑郁线索。E-DAIC 音频质量不均限制外推。
