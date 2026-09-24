# Audio-Based Understanding of Audiobook Narration Appeal

- 论文编号：453
- 报告人：Shahar Elisha
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/elisha26_interspeech.pdf

## 问题
有声书吸引力受叙述风格影响，但大规模计算研究少；同一书目多版本、体裁差异与稀疏消费数据使“哪些声学特征驱动吸引力”难解。

## 方法
LibriVox 单叙述者英语有声书 8,854 本（1,206 叙述者、65 体裁）；每本最多采样约 10 分钟音频。特征：eGeMAPS、YAMNet 事件、whisper-tiny 语速等共 129 维汇总。以 view-rate（浏览量/上线天数）为公开代理；GLM / 分体裁 GLM / 书目随机截距 LME；四分位分类与同书目内排序；并用 Spotify 子集的 return-rate 复核。

## 实验与结果
全局 GLM 伪 R²≈0.09，31 个特征显著但效应小；同书不同叙述变异（0.52）接近跨书目变异（0.54）。LME 相对 GLM 大幅降 AIC。分类：声学 alone 准确率约 0.29–0.32（随机 0.25），结合体裁可达 0.35。排序在 view-rate 上弱，改用 return-rate 后 Kendall’s τ 升至约 0.26–0.28。

## 结论
在控制书目后，叙述声学仍与消费相关且体裁依赖；声学信息可用于分类/排序，但粗代理指标限制强度。属首批系统连接叙述声学与大规模真实消费的研究。

## 点评
把推荐/选角问题落到可解释声学特征与同书对照，工程价值清楚。view-rate 噪声大、对短书有偏，Spotify return-rate 补强是关键；效应分散提示“组合风格”比单特征更重要。
