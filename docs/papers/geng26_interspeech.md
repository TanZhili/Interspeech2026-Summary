# Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis

- 论文编号：711
- 报告人：Haopeng Geng
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/geng26_interspeech.pdf

## 问题
MDD 需要忠实刻画细粒度声学偏差，但沿用 ASR 的 CTC 会因稀疏后验与延迟发射抹掉短暂错误线索（声学陷阱）；显式规范音素提示或强 LM 又易把预测拉回规范文本（语言学陷阱），且推理依赖提示限制自发场景。

## 方法
提出无提示的 CROTTC-IF：(1) CROTTC——用一维最优传输求单一单调帧–标签对齐（OTTC），并对两路增强视图的帧级后验做对称 KL 一致性正则（CR），损失为 L_CR + η(L_OTTC)；无 blank 主导的稠密对齐。(2) Indirect Fusion（IF）——训练期把规范音素与错误标注作特权信息，经融合网络与双头错误检测教师反传到编码器/解码器；推理丢弃教师，仅用 AM/LM 浅融合搜假设。(3) 另构造 LLM-MDD，用多模态 LLM 与不同提示模板量化显式规范先验的影响。全文自 LLM-MDD 训练细节起抽取被截断。

## 实验与结果
摘要与引言报告：CROTTC-IF 在 L2-ARCTIC 上 F1 71.77%，在 Iqra’Eval2 排行榜 F1 71.70%；无辅助数据与显式规范提示。评测覆盖 L2-ARCTIC、ERJ、speechocean762 与阿拉伯语 Iqra’Eval2。因后半正文截断，更细消融与 LLM 对比数字无法从全文完整核对。

## 结论
作者认为解耦声学建模与显式规范先验、用稠密帧对齐 + 训练期特权知识迁移，可在无提示推理下得到稳健 MDD。边界与完整 LLM 实验结果因抽取截断未能充分呈现。

## 点评
问题诊断清晰：针对 CTC 稀疏/延迟与规范泄漏分别改对齐目标与训练期知识注入，推理仍保持 prompt-free，路线与 CAPT 实际约束契合。抽取文本在 LLM-MDD 一节中断，实验数字与 LLM 分析只能部分采信；实现上也依赖最优传输与多任务权重调参，对低资源标注质量敏感。
