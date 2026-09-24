# Hallucination Benchmark for Speech Foundation Models

- 论文编号：2347
- 报告人：Alkis Koudounas
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koudounas26b_interspeech.pdf

## 问题
现代 ASR 会产生看似流利却未锚定于音频的幻觉；WER 把所有错误等权对待，无法区分音似替换与语义颠倒等危害程度不同的现象，也缺少标准化分类与度量。

## 方法
提出 SHALLOW（SpeechHALL-ucinationOvervieW），从四维分解 ASR 错误：(1) Lexical Fabrications：插入/替换/删除比加权（插入权最高，全插入非 fillers 记 1）；(2) Phonetic Fabrications：metaphone 编码上 Hamming、Levenshtein、Jaro-Winkler 平均；(3) Morphological Errors：依存结构 Jaccard 发散 + LanguageTool 语法/拼写/标点加权；(4) Semantic Errors：滑窗嵌入局部语义失配与全局语义指标。用 GPT-4o 构造 1,050 条合成假说–参考对，隔离各幻觉类型以校验指标正交性；并在真实模型与多域数据上评测。权重经可分性搜索与人工标注验证。

## 实验与结果
合成数据上 t-SNE 显示四类指标可分；WER-only（高 WER 但义近）样本语义分低，而局部/全局语义替换样本 SE 高（表 1 示例）。引言称 Encoder–decoder（如 Whisper）错误更均衡，decoder 向多模态（如 Phi-4）更偏流利、形态/语义更好但音似替换更多。SHALLOW 与 WER 在低错误率时相关强，高 WER 时解耦。正文抽取在语义误差公式段截断，完整跨模型数值表未完整可读。

## 结论
SHALLOW 提供可解释的 ASR 幻觉画像，能在 WER 失效的困难条件下仍区分错误类型，支持按应用需求做模型选型与架构迭代。

## 点评
把“幻觉”从笼统 WER 拆成可操作维度，对医疗/法律转录很有价值。权重与工具链（metaphone、LanguageTool）偏英语表层；全文结果段截断，架构对比与跨域数字需谨慎引用摘要陈述。
