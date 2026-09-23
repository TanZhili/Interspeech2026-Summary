# From Black-Box to Clinical Insight: A Multi-Stage Explainable Framework for Speech-Based Cognitive Impairment Detection

- 论文编号：1252
- 报告人：Maryam Zolnoori
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/haghbin26_interspeech.pdf

## 问题
基于 transformer 的认知障碍筛查性能提升，但黑盒难临床落地；现有 SHAP/LIME 多停在 token 重要性，缺少与认知–语言机制及可读叙述的衔接。

## 方法
在 SpeechCARE-AGF（mGTE 语言 + mHuBERT 声学 + 年龄门控融合，NIA PREPARE F1=72.11%）上建四级可解释管线：子词 SHAP 聚合到词；词汇丰富度/句法/不流畅/语义连贯等理论特征；LLaMA-3.1-70B-Instruct 四阶段推理，把归因与特征译成结构化临床叙述。数据 PREPARE（英/西/普，2,058 人）。

## 实验与结果
医生在 70 例分层英语样本上评估，解释与患者级认知画像对齐良好；系统可用性 SUS 82/100，提示工作流集成潜力。筛查模型本身为 PREPARE 挑战获奖架构。

## 结论
作者认为多阶段 XAI 可将黑盒预测转为临床可理解叙事，有助于筛查模型的可解释部署。

## 点评
重点不在抬分类分数，而在临床可沟通性；LLM 叙事层是差异化。局限：医生评测规模有限且偏英语；解释质量依赖 ASR 转写与 LLM 忠实度，幻觉风险需临床把关。
