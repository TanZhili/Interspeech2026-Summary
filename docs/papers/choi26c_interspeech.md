# Considerate Listener Modeling for Korean Streaming Backchannel Prediction

- 论文编号：1854
- 报告人：Yong-Seok Choi
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26c_interspeech.pdf

## 问题
流式附和（backchannel）若时机不当会打断说话；仅声学易在“需要回答的停顿”（问题/指令后）上过预测。需零 look-ahead、兼顾停顿邻近与语用合适性。

## 方法
Considerate Listener：块级共享声学编码器 + 停顿检测器对声学做 pause-aware soft scaling；ASR 部分假设经 Q-Former 交叉注意力融合；L_look-ahead=0。引入 Semantic FDR（预测 BC 落在 NOBC-PauseFP 的比例）。韩语咨询语料约 99h，块级 BC 仅 3.6%。

## 实验与结果
相对声学基线 (A) Macro-F1 66.77%：文本融合 (C) 69.14%、完整 (D) 68.93%（约 +2.16pp）。Semantic FDR：5.76%→(D) 3.07%，Semantic FP 相对降 53.8%。完整系统精度最高但召回略降，抑制集中在语用不当停顿。

## 结论
停顿软缩放 + 部分 ASR 文本融合可在零前瞻流式设定下提升 Macro-F1，并显著降低语用不当附和；Semantic FDR 比 Macro-F1 更能反映非打断目标。

## 点评
把“能不能插话”从声学停顿推进到话语行为约束，指标设计贴产品体验。私有咨询语料与人工 NOBC 标注限制复现；双条件联合时略过抑制，需在精度与召回间权衡。
