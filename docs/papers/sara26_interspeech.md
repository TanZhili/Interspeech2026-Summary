# Light-weight Pronunciation Assessment via Discrete Speech Token Surprisal

- 论文编号：1153
- 报告人：Shammur Absar Chowdhury
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sara26_interspeech.pdf

## 问题
发音评估常依赖强制对齐、音素清单或昂贵的标注非母语数据，低资源/无学习者语料场景难落地。需要主要用母语资源即可工作的轻量方案。

## 方法
仅用母语（LibriSpeech）训练：HuBERT Layer9 + K-means（K=512）得离散单元；3-gram Token LM 算 surprisal（用标准差/尖峰率等描述，避免均值抹平稀疏错误）。可选 Text2DUnit（CANINE+LoRA 解码器）由参考文本预测规范单元，与学习者声学单元做质心 L2 代价的 DTW，得到距离、失配率、失配 surprisal 等。Ridge 融合为分数；也可无监督直接用特征当质量指标。

## 实验与结果
SpeechOcean762：Audio+transcript 轻监督 Acc/Flu/Pros PCC 0.661/0.763/0.753；无监督 DTW 距离 Acc −0.633。音频 alone 约匹配 aMRT（0.60）。100h vs 960h 母语训练差异很小。L2-ARCTIC 零样本迁移 Ridge(SO-train) Acc/Flu/Pron 0.506/0.492/0.526，本地轻校准可再升。

## 结论
母语离散单元 surprisal + 文本引导 DTW 可在少标或无标学习者数据下做发音评估，并跨库迁移；转写引导带来明显增益。

## 点评
把“不像母语音位配列”操作化为 token surprisal，避开 GOP 管线依赖，对零资源场景很实用。强依赖朗读参考文本时增益最大；无文本时 surprisal 相关较弱，更适合做粗筛而非细诊断。
