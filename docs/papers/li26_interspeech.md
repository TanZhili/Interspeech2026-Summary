# XAI-Grounded Explanation Generation for Speech Deepfake Detection with Training-Free Multimodal Large Language Models

- 论文编号：161
- 报告人：Yupei Li
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/li26_interspeech.pdf

## 问题
语音深度伪造检测需要可信解释：传统 XAI 给出难读的低层归因；纯 LLM 解释又易幻觉、缺任务证据与专用数据集。

## 方法
提出训练无关框架 XGEG：用预训练 wav2vec 2.0 / HuBERT / WavLM 检测器生成 IG、LIME、Saliency 谱图归因，经 Qwen2.5-VL-7B 汇总时频异常；另用 openSMILE eGeMAPSv02 + MLP 的 SHAP 取 top 声学特征。将音频与这些证据交给 Qwen3-Omni-30B，按结构化模板（异常时频、自由解释、XAI 聚合说明）生成文本，并强调批判使用 XAI 而非照抄。基于 PartialSpoof 构建约 6.5 万条可解释实例（仅保留四模型均判对的伪造样本）。

## 实验与结果
人工评测（600 条、20 人）：XAI 引导相对纯音频在正确性/证据/特异性上提升明显；三模型聚合 overall preference 最高（1.50 vs 基线 0.35）。时间定位：纯音频 IoU 高但 Inside Accuracy 仅 0.049；单 XAI/聚合可将 IA 提至约 0.48–0.81（摘要称 IA 提升超 45%）。Area-Normalised Local Logit Sensitivity 上 XAI 方法远高于基线（LIME 可达约 327×）。发布数据集采用单模型全 XAI 配置（综合质量最佳）。

## 结论
跨模型/多方法 XAI 证据可引导免训练多模态 LLM 生成更具体、更少幻觉的 SDD 解释，并释放大规模 grounded 解释数据以支持后续研究。

## 点评
把“归因热图可读化 + LLM 叙事”接到同一管线，并用 IoU/IA 与 logit 灵敏度约束 faithfulness，比纯 post-hoc 文案更扎实。代价是流水线重、依赖多检测器与大模型推理；对 bona fide“证明无异常”仍难，正文亦承认。
