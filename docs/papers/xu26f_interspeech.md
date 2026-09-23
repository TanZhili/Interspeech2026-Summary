# Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations

- 论文编号：858
- 报告人：Tianze Xu
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/xu26f_interspeech.pdf

## 问题
说话人嵌入的跨语种泛化（如英粤）对合成与识别重要，但相对人类感知与声学结构的对齐研究不足；既有工作多停留在较早 MFCC 系统或单语相似度相关。

## 方法
基于 SpiCE 语料 10 名粤英双语女性说话人的节日问候短句，沿用既有 40 名听者（20 双语 / 20 英语单语）的 9 点声纹相似度评分（同/异说话人 × 粤/英/混合语言，共 220 对）。从 18 个 Wespeaker 预训练模型（ResNet、SimAM、ECAPA、CAM++ 等）及粤语微调版本提取嵌入，用余弦相似度；声学侧提取 29 个变量（语速、f0、共振峰、谐波/噪声等）。用线性混合模型预测机器相似度；用 RSA 将机器 RDM 与感知/声学 RDM 相关。

## 实验与结果
机器相似度同说话人显著高于异说话人（0.78 vs 0.60）；混合语言条件同–异对比减弱；粤语微调未提升相似度，预训练略高于微调。机器–感知 RSA 中等相关（均值 ρ≈0.44）；听者语言背景与刺激语言有交互，但微调状态无显著效应。机器–声学相关最强多为语速、F1–F4 均值与 SHR；粤语更偏 F2/F4 与高频谐波差，英语更偏 f0、FD、CPP。

## 结论
深度说话人嵌入在跨语种声纹相似度上与人类行为大体平行：能区分身份、对语言切换敏感，并依赖部分语言敏感、大体共享的声学线索；小规模粤语微调未见收益。局限含粤语微调数据量、短句样本与说话人数。

## 点评
把 LMM 身份/语言效应与 RSA–声学拆解绑在一起，证据链比单纯“跨语识别准确率”更贴近认知对齐问题。微调无增益与人类“语言背景不显著”平行，值得注意；若微调数据过小导致表征扰动而非增益，外推到大规模粤语适应仍需验证。
