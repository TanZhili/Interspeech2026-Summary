# Inverse Text Normalization in Romanian: A Comparative Study of Rule-Based, Neural, and Large Language Model Approaches

- 论文编号：3454
- 报告人：Oana Sirbu
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/sirbu26_interspeech.pdf

## 问题
罗马尼亚语 ITN（口语数字/日期等→书面形式）此前缺乏系统研究；需处理性数一致、罗马数字、机构命名等，且缺少统一评测与跨域证据。

## 方法
制定罗马尼亚 ITN 指南与 24,753 条手工口语–书面对（新闻为主，另含 400 条 OOD：有声书/童话/影视/播客）。统一指标：Global / Copy / Norm WER 及 Mean WER。比较 NeMo/Pynini 文法、微调 mT5、few-shot LLM（o4-mini）、agentic 工具调用、微调 RoLlama3.1-8B。

## 实验与结果
域内 Mean WER：LLM 提示 1.21%、RoLlama 1.75%、NeMo 1.92%、Agentic 2.84%、mT5-small 8.38%。OOD：LLM 2.57%（接近人工 2.45%）、RoLlama 3.97%、NeMo 4.56%。文法高效无 GPU；few-shot 约 $0.0073/句，agentic 更便宜但更弱；mT5 多种规模均偏高误差。

## 结论
罗马尼亚 ITN 存在清晰精度–成本权衡：LLM few-shot 最准且跨域强，确定性文法在隐私/边缘场景仍具竞争力；纯小神经模型数值不稳定、覆盖不足。

## 点评
把 Copy/Norm 拆开评测很适合 ITN（既要改对数字又不能乱改上下文）。资源与指南开源便于复现。脆弱处是新闻域主导标注、API 模型版本漂移，以及 agentic 未跑赢强文法说明工具编排未必优于精心规则。
