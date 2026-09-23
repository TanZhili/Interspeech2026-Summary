# Daily Affect Inference from Longitudinal Speech-based Journals: A Comparison of Acoustic and Linguistic Models

- 论文编号：2383
- 报告人：Michelle D Schlicher
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/schlicher26_interspeech.pdf

## 问题
日常语音日记兼具声学与语义，能否在群体与个体层面推断当日 arousal/valence/stress；声学与语言学哪条更有效，尚缺可比纵向语料与系统对照。

## 方法
德国大学生 2 周晚间日记：“今日亮点与低点？”+ MDBF（V/A/C）与 PSS-4；仅分析口语组：61 人、769 段（约 90% 女性）。Whisper 转写后对比：微调 GBERT-large、零样本 Mistral-7B-Instruct；声学侧 eGeMAPS+节奏/停顿特征随机森林，以及微调 wav2vec2 情感回归。说话人独立 5 折 CCC/RMSE；并用说话人中心化 LME 看日间声学与情绪。

## 实验与结果
群体层：语言远强于声学。Mistral 对 valence CCC .466、stress .360；GBERT 对 arousal CCC .122 最优；eGeMAPS/w2v2 多数近零或负。说话人层：Mistral 更像抓特质而非日间状态，RMSE 随个体均值系统变化。LME 在 FDR 后仅 valence 上停顿数（负）与预训练情感模型预测 valence（正）显著；arousal/stress 无显著声学日间关联。

## 结论
自由叙说语义更适合追踪日回顾式情绪/压力；全局声学模型难监控个体日波动，需个性化。日记反映的是当日总结而非瞬时状态，亦限制预测。

## 点评
把“日记是回顾而非瞬时”说清楚，并同时报群体 CCC 与说话人内 LME，避免被表面上的 LLM 分数误导。样本小、性别极偏、自我报告偏差大；声学近零与经典 SER 文献冲突，外推临床需谨慎。
