# A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction

- 论文编号：3610
- 报告人：Shiva Shankar Arumugam
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/arumugam26_interspeech.pdf

## 问题
联络中心通话密集包含客户名、账号、SKU、药名等命名实体，流式 ASR 易错，错误会传到 agent companion 界面，造成 CRM 错录与返工。人工在 UI 上的实体纠正本是高质量监督，却很少回灌到 ASR/抽取栈；且通常不能预先备好完整实体表，也不宜做声学重训。

## 方法
演示 MACE（Multi-Agent Companion Environment）闭环：ASR（带偏置列表 B）→ 词替规则 R → 抽取子代理 → companion UI 建议；reflection 子代理在音频路径外消费 UI 纠正 Δ，将误识/漏抽实体写入 B，对跨对话复发（阈值 τ）的误识模式生成替换规则 R。按对话批更新，B/R 存 KV、按 agent 作用域隔离；不改声学模型。实验用 ContextASR-Bench 英对话子集、Whisper-large-v3，确定性代理抽取器 + oracle 编辑器模拟人在环，K=100 批、τ=2，|B|≤500、|R|≤200。

## 实验与结果
相对无偏置基线，MACE Adaptive 将 NE-WER 从 0.178 降至 0.147（约 −17.1%），EditRate 从 0.304 降至 0.247（约 −18.6%），分别闭合至 oracle 偏置差距的 23.6% / 22.0%；32 批配对 bootstrap 的 95% CI 与基线不重叠。|B| 约在第 3 批饱和至 500，|R| 约第 28 批饱和至 200。

## 结论
作者认为把 companion UI 纠正闭环回写成偏置与替换规则，可在无先验实体表、无声学重训下持续降低实体错误与人工编辑率，并向 oracle 偏置靠拢。

## 点评
抓的是“人在环纠正→上下文偏置/后处理规则”的运营反馈回路，多智能体分工让更新离线于实时转写路径，工程上很贴联络中心。评测用 oracle 编辑与代理抽取，真实 LLM 抽取与真人编辑噪声下的增益可能打折；B/R 容量封顶后增益饱和，跨租户/跨域迁移也依赖作用域隔离设计。
