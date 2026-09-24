# Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations

- 论文编号：1478
- 报告人：Reo Shimizu
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/takagi26_interspeech.pdf

## 问题
MOS 预测模型常替代听测，但能否捕捉声学保真之外的韵律、口音与说话人特征差异仍不清楚；日语音高口音错误可改词义，尤其需要检验。

## 方法
对语音施加受控扰动并对比人类 MOS 与模型预测：Group A 声学退化（如低码率 MP3）；Group B 用可控音高口音 TTS 故意翻转口音；Group C 操纵平均 F0、F0 变化与语速（自然说话人差异 + 转换）。检验三假设 H1–H3。

## 实验与结果
多数模型能跟随声学退化（支持 H1）；对韵律/口音错误普遍不敏感，尽管主观分大幅下降（支持 H2）；说话人特征上呈双重分离——模型有人类没有的强平均 F0 偏置，却对人类敏感的语速与 F0 变异不敏感（支持 H3）。凸显标量 MOS 预测在声学保真之外的局限。

## 结论
自动 MOS 不宜单独代表「自然度」全维度；韵律与说话人特征需单独评测或改进表征。

## 点评
用正交扰动把「模型听什么」拆开，比相关分析更有因果清晰度。强在日语音高口音设定；脆弱点在扰动未必覆盖全部质量维度，且模型族若未在正文详列完整表时外推需克制。
