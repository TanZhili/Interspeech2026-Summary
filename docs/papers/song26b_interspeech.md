# MSMC: Multi-Scale Masked Convolution network for Robust Speech Emotion Recognition

- 论文编号：951
- 报告人：Haoyu Song
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/song26b_interspeech.pdf

## 问题
大型 SSL（HuBERT/WavLM）SER 效果好但参数与算力难边端实时；Mel 谱 + 传统 CNN 又难建模长程情感依赖，且对掩码谱直接卷积会泄漏。

## 方法
MSMC：学生分支对时—频掩码 Mel 谱做泄漏无关的 Masked Convolution Encoder（按可见掩码重归一化卷积）；教师为 EMA，看完整谱。条件位置编码 + 轻量 Transformer（学生仅保留可见 token）。多尺度一致性：MCE 中间层掩码区重建 + 全局向量余弦蒸馏；学生先自监督/蒸馏更新，再结合分类 CE；教师 EMA。

## 实验与结果
IEMOCAP 10-fold LOSO：全模型 WA 76.0%、UA 68.8%。消融显示 MCE、CPE、多尺度蒸馏逐步抬升。复杂度约 6.77M 参数、0.9G MACs/3s，相对文中 SSL 基线约少 16× 参数、23× MACs，同时逼近其准确率。

## 结论
泄漏无关掩码卷积 + 多尺度 mean-teacher 蒸馏，可在轻量谱图模型上逼近重 SSL 的 SER 表现，适合实时/边端。

## 点评
把视觉 MCMAE 思路改成“整频带时间掩码 + 按掩码重归一”，贴合谱图各向异性。双分支与 EMA 训练更复杂，部署可只留学生；与 SSL 对比的具体基线配置需对照原文表 2 解读，但效率叙事清晰。
