# Exploring Hesitation as a Signal for Spoken Grammatical Error Correction

- 论文编号：1869
- 报告人：Seunghoon Han
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/han26c_interspeech.pdf

## 问题
口语语法纠错（SGEC）常规流水线把不流畅当作噪声先删再做文本 GEC，可能丢掉 L2 学习者因语法不确定而产生的犹豫线索。作者假设犹豫与语法错误共现，应被当作正信号而非噪声。

## 方法
在人工带犹豫标注的转写上：(1) 注入特殊标记——静音停顿 `[SP]`、填充停顿区 `[FP]`/`[/FP]`、重复区 `[REP]`/`[/REP]`；(2) 为每个 token 加犹豫类型嵌入（正常/SP/FP 区内/REP 区内）与 token 嵌入相加。基座 T5-base，输入格式 `gec: <marked transcript>`，在 S&I Corpus 2025 训练域上微调。对比：规则去不流畅（DD）、人工流畅转写（Fluent oracle）。用人工转写而非 ASR，以隔离犹豫信号与识别错误。

## 实验与结果
ERRANT span-based F0.5：Proposed 0.4790，优于 DD 0.4585（+2.05%p）与 Fluent 0.4606（+1.84%p）。犹豫附近（±1 token）误差上相对 Fluent +2.78%p（0.5087 vs 0.4809），远区仅 +1.15%p。按类型：FP 增益最大（相对 Fluent +9.10%p），SP 中等，REP 基线已高、增益小。按 ERRANT：对 U:NOUN 等多余类错误提升明显（如 +11.5%p）。

## 结论
保留并显式编码犹豫信息，比规则去流畅甚至人工流畅转写更能帮助口语 GEC，且增益集中在犹豫附近，支持“犹豫携带纠错线索”。落地需能输出犹豫标注的 ASR；本文用人工转写隔离效应，未在端到端 ASR 噪声下验证。

## 点评
挑战“先清不流畅再纠错”的默认流水线，实验设计干净：超越 Fluent oracle 这一点很有说服力。代价是控制设定与挑战赛 cascade 不可直接比绝对分；FP 上 Fluent 反而更差，也提示人工“清理”可能一并抹掉纠错线索。
