# Do speech representational spaces encode language family structures?

- 论文编号：2418
- 报告人：Emily Gaughan
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/gaughan26_interspeech.pdf

## 问题
多语语音表示已知含语种信息，但是否编码有意义的语系/谱系结构仍不清晰。现有可视化难以量化，监督 probe 只看固定层级且可能扭曲显著性，而树结构评估在语音域尚未系统开展。

## 方法
用 Common Voice 23.0 测试集中 230 个 languoid（26 语系）各约 100 条，取六类模型中间层隐状态均值后算语种间余弦距离，再以 WPGMC 凝聚聚类建树，与 Glottolog 金标准树比较。评估六种树距离（PARTITION/Robinson–Foulds、PATH、QUARTET、NYE、P-RF、P-QUARTET），并与 ASJP 的 LDND 词典统计上线对照；另用 logistic regression / k-NN / LDA 做顶层语系 probe。模型含 XLS-R、Whisper、XEUS、mHubert-147、ECAPA-LID、Whisper-LID。

## 实验与结果
- 神经表示中 Whisper-LID 平均树距离最好（Avg. Tree Dist −0.80），XEUS 最差（1.14）；均明显弱于 LDND（−1.99）。
- LID 目标整体优于通用编码器；树指标与 probe 对“最佳空间”判断不一致（probe 更看好 mHubert-147）。
- 多数模型在“已见语种比例升高”时树距离变差（如 XLS-R r=0.62）；Whisper / Whisper-LID 相关性弱或无显著相关。

## 结论
树距离比 probe 更适于评估层级谱系结构；宽语种覆盖（如 XEUS）并不自动带来谱系结构。作者建议联合使用 QUARTET、PARTITION、NYE，慎用对树形敏感的 PATH。局限包括只分析单层、架构与数据未严格对照。

## 点评
把历史语言学的谱系树距离迁到语音表示评估，比“看一眼聚类图”或固定层级 probe 更贴合“语言如何分化”的问题。结果暗示 LID 目标比“覆盖尽量多语种”更利于学到家族结构，而未见语种有时反而更接近 Glottolog，点出“已见语种被分得太开”可能破坏谱系几何——这对多语预训练目标设计有直接启发。
