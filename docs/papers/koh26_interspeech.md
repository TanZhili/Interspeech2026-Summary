# A Multi-Agent Framework to Automate Feedback Generation for IELTS Speaking Test using Multimodal SpeechLMs

- 论文编号：1417
- 报告人：Hui Xin Koh
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koh26_interspeech.pdf

## 问题
IELTS 口语需在流利连贯、词汇、语法、发音四维上评分并给反馈。手工特征回归覆盖不足、分数向中心靠拢；ASR→LLM 流水线丢掉韵律与时间线索，且识别错误不可逆传播。通用 SpeechLM 又常校准不足、对低质量语音过打分。

## 方法
多代理 + 多模态 SpeechLM（Qwen-Omni）：直接听音频，四个角色代理分别对应官方四项准则，输出分项分数与反馈；元审阅代理对照原音频做跨准则一致性检查，按 IELTS 半档取整汇总总分并合成报告。支持 3B/7B/30B-A3B、单代理 vs 多代理、零样本 vs 九例 few-shot。按 Part1–3 分段评估再与全场平均。对比：手工特征多元线性回归；Whisper 转写 + GPT-5-nano 反馈。

## 实验与结果
新建约 22.63 小时、270 场模拟考，分数 4.0–9.0，考官给分与反馈。评分相关（平均）：Multi+Few-shot r/ρ/τ = 0.480/0.521/0.396，优于单代理与回归（r=0.117）；3B 多代理已显著强于回归。反馈语义相似（SBERT）：多代理约 0.82–0.83，ASR+LLM 仅 0.412。30B MoE 评分相关不如更小稠密模型，作者归因于稀疏激活有效容量约 3B。

## 结论
准则对齐的多代理 + 端到端听音，可提升与人工分数相关性和反馈语义相似度，并绕过 ASR 信息瓶颈；架构分解往往比单纯放大参数更有效。

## 点评
把 IELTS 四维 rubric 显式拆成独立代理，再由元审阅抑制晕轮与重复惩罚，设计与构念效度对齐。语料规模中等且非公开标准集；30B 变弱提示“更大≠更好”，部署时应优先验证多代理结构而非盲目换大模型。
