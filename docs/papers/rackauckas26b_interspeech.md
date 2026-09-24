# A Speech-First Character Interface for Stylized Japanese Dialogue Practice

- 论文编号：3599
- 报告人：Zackary Rackauckas
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rackauckas26b_interspeech.pdf

## 问题
日语练习需同时体验文字、发音、语体与句末助词；多数中性导师聊天把语音当附加，难感受角色语体差异。

## 方法
Jouzu 移动演示：选虚构角色 → 打字或说话 → 人设条件 LLM 生成日语 → Style-BERT-VITS2（专业演员微调）合成角色声；多角色同 prompt 对比；点击词显示假名/罗马字/英义。框定角色语为表达性练习，非正式场合万能模板。用户研究结果另文。

## 实验与结果
演示系统；引用 Style-BERT-VITS2 JP Extra 与母语真值平均无显著差异的先前评测。本文不重复学习成效数字。

## 结论
以语音为主通道展示人设、情感与语体对比，并嵌入轻量词汇支架，形成可展台运行的日语口语练习环。

## 点评
“同句多角色听差”教学设计清楚；依赖角色语，需防学习者误用到正式场景（作者已声明）。
