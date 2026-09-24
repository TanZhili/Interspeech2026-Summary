# Evaluation of forced alignment of code-mixed speech: the case of Hindi-English

- 论文编号：2179
- 报告人：Ayushi Pandey
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/pandey26b_interspeech.pdf

## 问题
印地语–英语语码混合的强制对齐面临扩展音素表、拼写（nuqta 常缺）与说话人自由变体；现有工具与单语假设不足，音系分析与边界标注基础薄弱。

## 方法
在 PBCM 语料（约 6941 句、113 说话人）上用 MFA v1.0。实验1：针对 [ph]∼[f]、[Ã]∼[z] 五套词典 bootstrap（无映射、多数基线、映射到本土/擦音代理、最大 bootstrap）。实验2：用去歧义后的词典，比较三种声学训练——整句语码混合、单语印地短语块、孤立英语词——对齐句中英语词，以手工金标中点绝对误差评价。

## 实验与结果
[ph]∼[f]：无映射 F=0.72；多数基线完美；ph→p F=0.97，f→s 很差。金标显示说话人几乎稳定产出 /f/。[Ã]∼[z]：无映射 F=0.16；最大 bootstrap（Ã→c, z→s）最好 F=0.74。实验2：语码混合句训练平均误差 4.15 ms，约为单语印地（38.18 ms）或英语词（37.58 ms）的 1/10；<10 ms 覆盖 87.06% vs 约 42–48%。

## 结论
原则性词典设计（bootstrap）与语码混合句级声学训练对双语对齐均必要；语码混合数据即使词级也常优于更大单语印地训练。

## 点评
把 nuqta 缺失导致的双向变体问题说清楚了，并区分“几乎已稳定的 /f/”与“仍双变体的 Ã/z”。用句级混合数据训声学模型这一结论对下游语音工具很实用。局限是 MFA 版本较旧、手工金标规模有限，新版 MFA 与说话人条件发音概率仍待验证。
