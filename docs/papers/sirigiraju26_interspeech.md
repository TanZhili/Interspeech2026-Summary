# ALFreeD: Teacher-Guided Few-Shot Pronunciation Assessment via Segmentation-Free Deviation Modeling

- 论文编号：3247
- 报告人：Meenakshi Sirigiraju
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sirigiraju26_interspeech.pdf

## 问题
自动发音评估常依赖规范音素、强制对齐边界与大量标注；非母语偏差大时对齐易错，端到端模型又吃标注。需要少标、无音素分割的教师引导方案。

## 方法
ALFreeD：用 HuBERT 提教师/学习者帧嵌入；余弦距离 + DTW 得学习者对齐的帧级偏差序列；教师–教师偏差训 GMM-UBM，再用 i-vector 把学习者偏差压成句级向量以抑制非发音变异；仅训两层 MLP 预测分数。教师语音由 Google TTS（美音）合成。在 SpeechOcean762 上变化标注量 {300…2500}。

## 实验与结果
300 标样本 PCC 0.68（相对 GOP 0.62 约 +9.7%）；1000 样本达 0.71（可比 GOPT）；2500 样本 0.74（接近 3M 的 0.76，优于 HiPAMA 0.73）。HuBERT 约第 7 层最好；GMM 32 分量、i-vector 维 10 时最佳。

## 结论
教师–学习者表示空间偏差 + i-vector 聚合，可在无规范音素对齐、极少标注下达到接近全监督 E2E 的发音评分相关。

## 点评
用 TTS 教师作参考回避了母语录音成本，但“教师=合成美音”也可能引入风格/音色偏差。中层 HuBERT 最优符合语音学敏感层直觉；方法给的是句级分数，细粒度音素反馈仍待扩展。
