# Acoustic Landmark Detector based on Conformer and HuBERT

- 论文编号：1386
- 报告人：Mateo Cámara
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/camara26c_interspeech.pdf

## 问题
声学 landmark 是与发音事件绑定的突变点（元音、滑音、塞音/擦音/鼻音的闭开），是连接声学与音系特征的表示，但传统检测多为手工特征与规则；深度学习在音素边界上进步明显，在稀疏 landmark 上的系统能力仍不清楚。

## 方法
在 1839 条人工标注语料（3 说话人；678 VCV + 1161 词；8 类共 8428 个 landmark，90/10 分层划分）上，用 Conformer 编码器（dmodel=256、12 层）做帧级 9 类（背景+8 landmark）分类。关键设计：按事件类型设 Gaussian soft labels（σV=20 ms、σG=15 ms、擦音  soft 12 ms、塞/鼻 10 ms）以建模标注时间不确定性；特征对比 mel、冻结 wav2vec2、冻结 HuBERT、mel+wav2vec2 混合；峰值后处理（高度 0.5、峰间距≥5 帧等）。共 14 组配置，涵盖损失（加权 CE / focal / 无权重）、容量、按类分模型、数据子集与增强；主指标 F1@20 ms（辅 F1@30 ms），并报告本语料 LER。

## 实验与结果
冻结 HuBERT 最好：F1@20 ms=0.77、F1@30 ms=0.84；soft 相对 hard 绝对 +0.070（元音从 0.54 跌至 hard 的 0.18）。塞音/擦音 release 与塞音 closure 较易（F1>0.80），元音与鼻音 release 较难（元音约 0.55）。本语料 LER 13.8%；与 Auto-Landmark（TIMIT、5 类、31.3% LER）因语料/标签/指标不同不可直接比。零样本到 Auto-Landmark 对应子集 LER 63.0%。消融：focal、按类分模型、仅 VCV 训练伤害最大；词子集略优；增强与合成预训练几乎无增益。

## 结论
Conformer+冻结 HuBERT 与按类 σ 的 soft label 可在本语料上达到较强的时序定位 landmark 检测；可检测性随事件突变程度升高，与 Stevens 理论一致。局限为语料小（3 说话人）、单次划分，以及对 TIMIT 的零样本迁移有限。

## 点评
抓的是“稀疏、需时间容差对齐的音系事件检测”，把标注时间模糊显式写进 soft label，比单纯换更大模型更对症。HuBERT 优于 mel/wav2vec2 说明 SSL 表征对 manner 相关突变有用，但帧移与峰值后处理仍约束极限。数据域窄（孤立音节/词）是主要脆弱点，跨语料与连续自发语音仍待验证。
