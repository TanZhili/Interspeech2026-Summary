# Time-normalized spectrograms reveal segmental differences in English heterographic homophones

- 论文编号：793
- 报告人：Yu-Hsiang Tseng
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26_interspeech.pdf

## 问题
异形同音词常被假定“听起来一样”，但时长已显示与频率相关。段落层面（音段实现）是否也系统性不同、是否受话语语境意义塑造，仍缺大规模声学证据。

## 方法
收集 35 对异形同音词各 200 token（共 **14,000**）：做 **时间归一化频谱图**，并导出 phone logits；用 GPT-2 得上下文嵌入（CE），度量同音对内语义可分性。分析频谱/phone logits 能否区分词型，并回归语义对比、频率、搭配概率等协变量。

## 实验与结果
- 时间归一化频谱已能系统预测同音对内词型；phone logits 显示细微差异（如 *wait* 元音起音慢于 *weight*）。
- CE logits 对 spectral logits 有正向效应：语境语义越可分，语音 token 越易正确分类。
- 时长归一化后，词长效应弱；频率呈 U 形；前后词高概率搭配时 spectral logits 更大（实现更“典型”）。

## 结论
同音词只是近似同音；具体实现受 token 级意义共定。结果更支持形式–意义在 token 层对齐的词库模型（如 Discriminative Lexicon），而非把音段当作纯抽象符号。

## 点评
用时间归一化频谱避开单纯时长解释，把“意义塑形发音”落到可量化的频谱/phone logits，方法干净。强在大样本与 CE 控制；脆弱在 GPT-2 语义代理与英语同音对选取——推广到其他语言需谨慎。
