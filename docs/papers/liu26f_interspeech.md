# A Semantic-Anchor-based Method for Open-Vocabulary Sound Event Detection

- 论文编号：731
- 报告人：Yanfeng Shi
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26f_interspeech.pdf

## 问题
开放词汇 SED 的 query 检索常只把查询当向量匹配，缺乏事件语义理解，新类识别弱。需要语义级参考与更强的 query–特征交互。

## 方法
学习一组 semantic anchor 作为语义参考 token，任意事件通过注意力锚定理解；双向注意力增强 query–特征交互；定制 query 增强提鲁棒。骨干含 HTS-AT；在 AudioSet-Strong 开放词汇设定与 DESED 跨库/零样本评测。

## 实验与结果
开放词汇 novel 类 PSDS 34.9（总体 PSDS 50.5）；DESED 零样本 PSDS1 44.1，甚至超过 DESED 监督基线。称优于既有开放词汇 SED。

## 结论
作者认为语义锚点使模型真正“理解”事件语义，从而提升新类与跨数据集泛化。

## 点评
把开放词汇从纯检索推向有语义参考的注意力机制，对稀有/新类有针对性。锚点数量与初始化、文本query质量会强烈影响上限；零样本超监督基线的结果需结合标签与协议细节解读。
