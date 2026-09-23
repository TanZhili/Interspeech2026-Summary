# The Interspeech 2026 Challenge on Transfer of Pragmatic Intent in Speech-to-Speech Translation

- 论文编号：390
- 报告人：Nigel G. Ward
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/ward26_interspeech.pdf

## 问题
现有语音到语音翻译（S2ST）多评语义与自然度，很少系统评语气、意图等语用保真，难以支撑跨语言对话。

## 方法
挑战设计：英↔西双语者会话重演得到语用对齐测试集（En→Es 240、Es→En 199 句）；主观评“语气/感觉/意图”1–5 分；自动用 Segura 语用相似度量。条件：音频 S2ST（C1）与语用特征向量映射（C2）。报告 4 队正式提交结果。

## 实验与结果
Es→En 音频：人类重演 4.59，最佳系统 CUHK-SZ 3.46，Seamless 2.98；最佳相对人类落后约 1.2 分。Segura 上 CUHK-SZ 亦略优于 Seamless。自动度量与人类相关约 0.51；文中讨论评测优缺与各队系统要点。

## 结论
语用保真仍明显落后人类；挑战建立了数据与评测基线，并暴露自动度量跨条件可比性等问题。

## 点评
把“对话里听起来像不像那个人想表达的”做成可评挑战，填补 S2ST 评测空白。评委少、部分评委参与造数、自动度量局限作者已坦陈；价值在议程设定多于刷榜数字。
