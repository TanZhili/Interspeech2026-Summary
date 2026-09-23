# Evaluation of forced alignment of code-mixed speech: the case of Hindi-English

- 论文编号：2179
- 报告人：Ayushi Pandey
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/pandey26b_interspeech.pdf

## 问题
印地–英语语码混合语音的强制对齐面临音位清单扩大、正字法（nuqta 常缺）与说话人变异；现有工具对混合语境下的自由变体与句中插入英语词边界估计不足。

## 方法
在 PBCM 语料上用 MFA v1.0 做两组实验。(1) 词表设计：对 [ph]∼[f]、[Ã]∼[z] 等自由变体比较无映射、多数基线、主导音映射、擦音代理与最大 bootstrapping（如 Ã→c、z→s）。(2) 声学训练数据：分别用句级语码混合全句、单语印地语块、孤立英语词训声学模型，对齐手标英语词音位中点。

## 实验与结果
[ph]∼[f]：多数说话人稳定产出 /f/；多数基线 F=1.0，ph→p 达 0.97，无映射仅 0.72。[Ã]∼[z]：真实产出两端并存，最大 bootstrapping F=0.74 最好。句级语码混合声学模型中点平均误差 4.15 ms，约为单语印地（38.18 ms）与孤立英语（37.58 ms）的 1/10；<10 ms 容差覆盖 87.06% vs 单语约 42–48%。

## 结论
原则性词表 bootstrapping 与句级语码混合训练数据对可靠双语对齐均必不可少；即使词级语码混合数据也优于更大单语印地语料。

## 点评
把正字法“隐形 nuqta”与声学自由变体拆开做词表 vs 声学消融，对低资源强制对齐很实用。局限是 MFA 版本偏旧、读语料可能压低口语变体；[Ã]∼[z] 仍难用单一标签解决，说明混合语需要多发音条目而非简单多数映射。
