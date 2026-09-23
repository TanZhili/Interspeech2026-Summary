# Medical Dialogue and Conversational Understanding

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：13
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场面向医疗音频与对话理解：联邦少样本临床音频诊断、心理危机热线分级、抑郁症严重度 LLM 行为剖析、环境临床抄写员的噪声安全压测、一线健康对话基准挑战，以及多部位听诊录音的患者级多模态问答。

共性关注标注稀缺、隐私与安全：伪标签情境学习、副语言注入文本证据、提示内容相关性重于 demonstration 数量，以及 WER 无法捕捉的临床不安全输出。评测侧则建设真实噪声重叠的多说话人医疗对话基准，并把听诊从孤立分类推向患者级问答。

## 技术内容

### 联邦少样本诊断、危机热线与抑郁严重度

**Unlocking In-Context Learning in Audio-Language Models from Decentralized Medical Audio**（论文 430；Ran Piao）  
提出联邦自情境化（FSC）：用无监督聚类构造伪标签情境，经字幕预训练对齐与联邦情境微调后，在小支持集上诊断未见查询。摘要称 held-out 呼吸/心脏条件 2-way 2-shot 准确率 71.6%，优于音频—语言基线逾 9%。

**Speech-based Psychological Crisis Assessment using LLMs**（论文 997；Terumi Chiba）  
将非言语声学线索转为显式文本证据（副语言注入），并探索以 LLM 生成诊断理由作辅助监督的推理增强训练。摘要称在分块增强与 5 折交叉验证下 macro F1=0.802、准确率 0.805，优于声学、零样本 LLM 与语音感知 LLM 基线。

**Investigating LLMs Behavior in Depression Severity Prediction**（论文 456；Jiawei Yu）  
在 PHQ-8 预测上评估五种 LLM 的 0–10-shot，并引入矛盾标签干预。摘要称增加 shot 收益有限且非单调，对损坏示范标签不敏感；用症状聚焦摘录替代完整转写持续提升表现并约减 80% token；预测平均化带来稳定增益。

### 临床抄写安全、一线对话基准与听诊问答

**Beyond WER: A Paired Acoustic Stress Test for Ambient Clinical Scribes**（论文 606；Xiao-Hang Jiang）  
对同一对话注入多样噪声并冻结下游配置，隔离噪声对临床推理的因果影响。摘要称平稳环境噪声仅使 WER 上升约 0.71 个百分点，却几乎使不安全输出率翻倍；并提出无需微调的轻量缓解策略。

**Benchmarking Speech Systems for Frontline Health Conversations: The DISPLACE-M Challenge**（论文 3255；Dhanya E）  
发布面向一线健康工作者与求医者自发、噪声、重叠对话的挑战，含约 40 小时开发与 15 小时盲评数据，覆盖说话人日志、ASR、主题识别与对话摘要四项基线，并以 DER、tcpWER、ROUGE-L 评测；本文描述 Phase-I 数据、任务、基线与结果摘要。

**AuscuTSLM: Patient-Level Multimodal Question Answering from Multi-Site Auscultation Recordings**（论文 2037；Fan Wu）  
经门控交叉注意力把多部位听诊录音对齐到冻结 LLM 嵌入空间，做患者级评估。摘要称在 CaReSound 上 F1-macro 0.865、BERTScore 0.952；轻量域特异编码器可媲美大规模 ALM，多部位聚合提供空间冗余以缓解时间截断。

## 本场要点

- 联邦伪标签情境学习使低资源临床音频少样本诊断成为可能。
- 热线危机分级可把副语言证据显式注入文本 LLM。
- 抑郁严重度预测中，上下文相关性与摘录策略重于 few-shot 数量。
- WER 不足以衡量环境临床抄写安全；微小噪声可显著增加不安全输出。
- DISPLACE-M 与 AuscuTSLM 分别推进一线医疗对话基准与患者级听诊问答。

## 覆盖核对

- 430 | Unlocking In-Context Learning in Audio-Language Models from Decentralized Medical Audio
- 997 | Speech-based Psychological Crisis Assessment using LLMs
- 456 | Investigating LLMs Behavior in Depression Severity Prediction
- 606 | Beyond WER: A Paired Acoustic Stress Test for Ambient Clinical Scribes
- 3255 | Benchmarking Speech Systems for Frontline Health Conversations: The DISPLACE-M Challenge
- 2037 | AuscuTSLM: Patient-Level Multimodal Question Answering from Multi-Site Auscultation Recordings
