# WASIL: In-the-Wild Arabic Spoken Interactions with LLMs

- 论文编号：2694
- 报告人：Shammur Absar Chowdhury
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ali26c_interspeech.pdf

## 问题
阿拉伯语语音助手多为 ASR→LLM 级联；用户 dislike 可能来自 ASR 错误、固有不可答、或 LLM 本身，难拆开。缺含音频、转写、回复与显式反馈的野生方言数据。

## 方法
发布 WASIL：收集 9,304 条野生阿拉伯语口语提示（MSA + 方言）；用户 like/dislike 与多标签失败原因。2,573 条金标转写（人工后编辑，按国家匹配标注者），其中 1,777 为测试集；标注方言与可答性（可答/模糊需澄清/不支持/非请求噪声）。用多法官 LLM 对 ASR vs 金标转写下的回复做无参考评分。

## 实验与结果
数据集与标注流程是核心贡献；分析将固有不可答与 ASR 诱发劣化分开，并关联 dislike 与失败类别（指令遵循、事实、风格、文化/宗教等）。公开测试集于 Hugging Face。

## 结论
WASIL 为阿拉伯语语音–LLM 交互提供可拆分误差源的野生评测资源，支持下游导向 ASR 评估与方言覆盖分析。

## 点评
把“用户反馈 + 可答性 + 金标音频”绑在一起，正好打中级联助手评测的混杂因果。方言覆盖与文化/宗教失败标签对阿拉伯语境特别关键。金标子集相对全量仍有限；多法官 LLM 评分需防评判器偏置。
