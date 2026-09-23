# Speaker or Language? Explaining Variance in Charismatic Prosody Across Luxembourgish and French

- 论文编号：26
- 报告人：Nina Hosseini-Kivanani
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/hosseinikivanani26_interspeech.pdf

## 问题
魅力语音的副语言线索多在单语、准备性语料中研究；双语政客在卢森堡语（认同语）与法语（高声望机构语）间切换时，魅力相关韵律由说话人个体还是语言主导，方向如何，尚不清楚。

## 方法
10 名卢森堡政治公众人物（5F/5M），每人各 20 句自发卢森堡语与法语，共 400 句，情境尽量可比。LuxASR 转写、WebMAUS 对齐、ProsodyPro 提取 41 维声学–韵律特征（F0、强度、时长、BID/音质等），z 标准化。PCA 概览；线性混合模型 `feature ~ Language + Gender + Duration + (1|Speaker)`，用 ICCSpeaker 与 Language 边际 \(R^2\) 分解方差；Language×Gender 交互检验 RQ1，FDR 校正。

## 实验与结果
PC1/PC2 解释约 31.4%/16.8% 方差，语言在空间上有系统但重叠的位移。Speaker ICC 中位 0.56，Language 中位仅约 0.5% 方差。41 特征中 18 个 Language 效应 FDR 显著：法语更高 shimmer、句末 F0（\(d=0.90, 0.68\)）；卢森堡语多数中频能量带更高（如 2750 Hz \(d=-1.67\)）。由六维线索合成的魅力指数无可靠语言主效应（\(d=-0.03\)）。

## 结论
说话人身份主导魅力相关韵律方差；语言带来系统但局部的音质/谱与轮廓差异，与社会语言学角色相符，却未形成整体“哪一语更魅力”的优势。局限：仅 10 人政治语体、无听者主观评分、句内容非平行。

## 点评
用 within-speaker 双语设计直接回答“说话人还是语言”，方差分解结论清晰。复合魅力指数无语言效应，提醒勿把单特征差异直接等同全局魅力。脆弱点是声学–感知相关依赖既有文献，且句内容跨语不完全平行可能混入话题效应。
