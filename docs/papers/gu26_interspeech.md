# Mutual Cancellation between Masking Effects Benefits Speech Intelligibility

- 论文编号：1290
- 报告人：Yixin Gu
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gu26_interspeech.pdf

## 问题
竞争语音带来 informational masking（IM）与 modulation masking（MM），并与 energetic masking（EM）纠缠；既往用全局 SNR 或事后校正难以干净分离。本文在跨语言设置下用高能 glimpse 比例（HEGP）约束 EM，检验语言相似性与调制保留程度如何共同决定可懂度，以及 MM 释放能否抵消 EM 代价。

## 方法
目标为 Harvard 英语句（以 “the” 起首）；竞争语音（CS）为英语同库句或普通话语料拼接摘录。由同一 CS 派生：LPC 阶 50/12/5 的谱–时调制噪声（STM）、Hilbert 包络调制的时间调制噪声（TM）、长时谱平稳噪声（TS）；普通话 TM 用普通话包络乘英语 TS。对每对目标–掩蔽器用自适应调 SNR，使 HEGP=0.3/0.4/0.5（低分=更强 EM），共 2 语言 ×3 EM ×6 掩蔽器=36 条件。25 名正常听力美式英语母语者听 180 句，打字复述目标词，指标 WRR。

## 实验与结果
HEGP↑ → WRR↑；CS 条件 WRR 最低，调制保留减弱时 WRR 渐进上升。0.3/0.4 HEGP 上英/普差异很小；0.5 HEGP 上普通话派生掩蔽器 WRR 56.9%，比英语侧高约 5.6 ppt，且普通话 CS/STM-50 显著优于英语对应条件。相对 CS，高/中 EM 下要到 STM-5 才显著提升；普通话 TM 相对 STM-5 再显著提升，英语 TM 则否。TM vs TS 多数不显著（普通话高 EM 除外）。ANOVA：EM、masker 主效应大，language 小但显著；language×masker 不显著。Glimpse 分析：高能 glimpse 数按设计对齐，非高能/总 glimpse 随调制减弱而减少，解释英语 TM 需更高 SNR 才能达同 HEGP。

## 结论
听者表现是“语言不相似带来的 IM 释放”与“英–英条件下电平线索减弱带来的 IM”之间的相互抵消；降低谱–时/时间调制可释放 MM，甚至在总 glimpse 更少的 TS 上仍可接近 TM，体现 MM 释放对 EM 的抵消。讨论指出 LPC 掩蔽器仍可能可懂，IM 与 MM 难以彻底拆开。正文讨论末尾有抽取截断。

## 点评
用 HEGP 对齐而非固定 SNR，是把“EM 控制”做实的关键设计；跨语言 + 调制梯度让 IM/MM 争论可操作化。脆弱点是 LPC 噪声仍可能残留可懂度、TM/TS 统计差异弱，以及 IM/MM 概念边界作者自己也承认未闭合——结果更适合读作“掩蔽效应相互抵消”的现象证据，而非纯净因果分解。
