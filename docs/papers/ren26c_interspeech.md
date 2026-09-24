# Adapting Audio Large Language Models for Speaker Verification

- 论文编号：1117
- 报告人：Shuai Wang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26c_interspeech.pdf

## 问题
Audio LLM（ALLM）泛化强，零样本能否做说话人确认，以及轻量微调能否缩小与专用 SV 模型差距，尚缺系统评估。

## 方法
将 SV 重写为音频问答；先零样本测公开基准，再在 VoxCeleb2、CN-Celeb、3D-Speaker 等约 900 万对上 LoRA（r=16，约 18M 可训参）微调，用规则硬负样本采样。分数取 “One” token 概率。并扩展为文本相关 SV：同时核验说话人与文本内容。

## 实验与结果
Kimi-Audio 零样本 EER 多在 30–50%；微调后性别/语言条件降至 4.87%/2.93%，仍整体落后 ResNet34/ECAPA/CAM+，但短时长等难条件更具竞争力；硬采样优于随机。多骨干微调均提升 SV。文本相关 LibriSpeech：微调后综合准确率 98.87%，接近 Whisper+ECAPA（98.83%）。

## 结论
适当适配后 ALLM 可作为统一 SV 框架并保留通用音频理解；零样本不足，与专用模型仍有差距。

## 点评
把 ALLM 当问答式验证器并系统扫声学条件，清楚标出“语义强、身份弱”。统一文本相关任务有吸引力；算力与仍存的 EER 差距限制替代专用骨干的短期可行性。
