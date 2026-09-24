# Unlocking In-Context Learning in Audio-Language Models from Decentralized Medical Audio

- 论文编号：430
- 报告人：Ran Piao
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/piao26_interspeech.pdf

## 问题
临床音频诊断缺大规模中心化标注，机构数据隐私受限；闭集分类难覆盖开放临床概念。需要在联邦设定下让音频–语言模型获得上下文诊断能力。

## 方法
Federated Self-Contextualization (FSC)：无监督聚类伪标签（无语义的任意名称）构造 support–query 片段，训练抽象“声学→上下文标签”映射；三阶段——字幕式预训练对齐音频嵌入与医学 LLM、联邦 episodic ICL 适配、测试时用少量真实标签 support 诊断 query。在留出呼吸与心脏条件上评测。

## 实验与结果
2-way 2-shot 准确率 71.6%，相对最强音频–语言基线高约 9 个百分点（约 62.1%）。跨 shot/设置优势保持；异常心音等子条件亦有报告。消融支持完整流水线。

## 结论
可把 ICL 技能与医学语义知识分源获取：伪标签练推理技能，预训练 LLM 提供概念语义，适配少样本开放词汇临床音频诊断与联邦隐私约束。

## 点评
“无意义伪标签防记疾病–声音映射、只学上下文绑定”是巧妙解耦。联邦 + 少样本叙事贴合医院现实。性能仍依赖测试时真实 support 质量与聚类伪片段是否覆盖声学多样性；开放类别外推边界需更多罕见病验证。
