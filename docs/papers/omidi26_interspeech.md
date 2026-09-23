# Learning from Annotation Uncertainty: Entropy-Aware Curriculum for Speech Emotion Recognition

- 论文编号：2992
- 报告人：John Hansen
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/omidi26_interspeech.pdf

## 问题
SER 常把多标注者分歧压成硬共识标签；MSP-Podcast 等语料中歧义是结构化感知信息而非纯噪声。需在统一骨干下量化分布监督与熵课程相对硬标签的收益。

## 方法
WavLM-Base + 时序卷积 + 双层 GRU，共享 256 维嵌入，多任务预测 9 类情绪分布与 VAD（异方差 NLL+CCC）。监督：硬 pluralty、主票分布、合并主–次票（0.9P/0.1S 或 0.8P/0.2S）；分类用 CE/CBCE 或 KLD。归一化熵 Hn 作固定歧义属性，用于分层评测与过滤/加权课程（标准从低熵到高熵，反向相反）。渐进解冻 WavLM。

## 实验与结果
相对硬标签，分布目标显著降 JSD/KLD（如 M90 KLD Test1 JSD 0.189 vs Hard CE 0.322）。硬标签 Macro-F1 部分靠 Other 类；分布监督 Other-F1 很低，把不确定性摊到情绪类。M90–Filter Test1 Macro-F1 最高 34.8%；M90–Weight Test2 Macro-F1 31.8% 且 KLD 最低。高熵箱 Macro-F1 全面更差；反向课程不优于标准课程。

## 结论
应超越硬标签，用保留听众分歧的分布目标；熵课程可在决策 F1 与分布对齐间权衡。高歧义话语仍难。

## 点评
控制实验设计干净：同架构只换监督与课程，避免与标签精炼方法纠缠。强处是揭示“刷 Macro-F1 靠 Other”的假象；脆弱处是标注者少时熵代理不完美，且分布监督与硬决策指标不完全同向。
