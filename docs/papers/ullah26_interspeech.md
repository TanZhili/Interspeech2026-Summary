# Music Artistic Captioning: Towards Translating Music into Expressive Language

- 论文编号：2618
- 报告人：Ubaid Ullah
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ullah26_interspeech.pdf

## 问题
歌剧等叙事性强、结构演变的长时音乐难以得到既忠于可闻线索又像节目单散文的长文描述；成对音–文数据稀缺，微调易过拟合措辞且难控风格。

## 方法
训练免费框架 MAC：多尺度结构分析（全局等分、MSAF 功能段、局部滑窗）→ MIR 低层声学 + MERT 高层语义/情绪聚成证据字典并口语化 → 分层上下文提示 LLM（GPT-OSS 20B）做槽位约束 JSON 字幕；一次性 Iterative Prompt Optimization 校准风格与忠实度。

## 实验与结果
短基准：MQAD 上 MAC 多项领先；MusicCaps/SongDesc 增益不一（人工标题常含 MIR 难覆盖的文化线索）。无参考艺术设定：Opera/MSD 上 Emo/Art 领先（如 Opera Art 0.55 vs FUTGA 0.35），Sem 逊于 Qwen-Omni。去掉层级上下文伤 Art；去掉 IPO 伤 Emo/Art。

## 结论
用多尺度伪证据约束现成 LLM，可在无任务微调下生成更有叙事连贯与情感对齐的长时音乐描述，跨数据集更稳健。

## 点评
把“长时幻觉”压成可审计的证据槽位，适合节目单式生成。Art/Sem 指标自建、LLM 评判有偏；证据层漏检（罕见乐器/文化语境）时仍会偏短基准上的人工标题。
