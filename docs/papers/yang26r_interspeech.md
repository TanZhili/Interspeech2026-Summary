# A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR

- 论文编号：3380
- 报告人：Yinchang Yang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26r_interspeech.pdf

## 问题
高性能日语 ASR 常闭源、缺数据细节或仅离线；端侧实时需要流式与可复现的全开放配方，且公开资源偏电视域、讲座/对话覆盖不足。

## 方法
123M FastConformer 混合 RNNT/CTC（CTC 辅助权 0.3）+ cache-aware 多上下文流式（训练采样 [L,R]∈{[70,13]…[70,0]}）。ReazonSpeech ~35K h 预训练，对比全量与 CER 分层策展（丢 CER>20%，三质量带加权）。再在约 507 h 五域渐进微调（含新建 TEDxJP-20h、MSR/BTSJ 过滤等）。

## 实验与结果
五测集平均 RNNT CER 12.4%，优于全开放 OWSM-CTC v4（13.5%）与 ReazonSpeech NeMo-v2（14.1%），参数小 5–8×；RTFx 1220（批）/446（流式）。CER 策展在缺讲座微调时显著帮 TEDx；与多域微调+更深预测 RNN 叠加时反而伤 TEDx。加 TEDx 数据单步可把 TEDxJP-10K CER 从 25.80 降到 13.71；[70,13] 与全句准确率一致，全因果平均升约 1.65 点。

## 结论
首个同时满足权重/数据清单/代码/日志全开放与 cache-aware 流式的日语 ASR；小模型+领域覆盖可打过更大离线开放基线。

## 点评
开放度与流式并重的缺口填得扎实；2×2 策展实验说明“清洗≠总更好”，与解码器容量和微调范围有交互。相对闭源大模型（如 parakeet 10.0%）仍有差距，但在可复现流式赛道上定位清晰。
