# Noise-Aware In-Context Learning for Hallucination Mitigation in ALLMs

- 论文编号：1610
- 报告人：Qixuan Huang
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/huang26k_interspeech.pdf

## 问题
听觉大模型在重叠事件、噪声与声学不确定时易靠语言先验“补全”，产生幻觉。既有评测多二元分类，难刻画生成式细粒度幻觉；缓解又常需昂贵微调。

## 方法
构建 **Clotho-1K**：从 Clotho 人工筛选修订 1,000 条多事件参考，定义四类幻觉（声学属性、声源/材质、先验驱动、虚构事件），用 LLM-as-Judge 对生成字幕打标。提出免训练 **NAICL**：建宽带噪声–保守描述先验库，用 BEATs 检索 Top-K 声学相似噪声对作上下文，引导证据不足时降低语义承诺、多用声学层表述。

## 实验与结果
多款 ALLM 幻觉率普遍偏高（约 19–40%），Source/Fabricated 为主。Qwen2.5-Omni-7B 上 NAICL 将 HR 从 26.53% 降至 16.98%，四类均降。消融：真实音频 ICL 无效甚至更差；无检索固定噪声仍降 HR 但偏过度保守；2s、结构化描述、检索 3-shot 最佳；Event/Definite 词频降、Acoustic 词频升。

## 结论
噪声可作为弱语义声学下界先验，经检索式 ICL 在推理时校准生成，显著抑制幻觉且无需微调。

## 点评
把噪声从“干扰”反转为“保守生成模板”，思路轻巧、即插即用。脆弱处：依赖 LLM 评判与人工修订参考的主观性；过度保守可能牺牲信息量；目前主测单一底座与 captioning 设定。
