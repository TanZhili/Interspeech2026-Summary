# SuTRA: Structurally-Unified Tokenization with Root Awareness

- 论文编号：291
- 报告人：Vaibhav Rathore
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rathore26_interspeech.pdf

## 问题
BPE 等子词优化压缩却忽略形态；印地语系等富形态语言以 akshara（辅音+matra）为书写原子，频率合并常切断词根与词缀（Morphological Shattering），并导致语义难恢复（Semantic Blindness）。现有形态数据集对印地语系边界标注不足。

## 方法
SuTRA 两阶段：预分词用正字规则把词绑成 akshara 单元，并用金标准词典或字符级 seq2seq 标出禁止跨越的形态边界；训练阶段在 BPE 式合并中用得分 S(a,b)=f(a,b)·Ψ(a,b)^γ_t，其中 Ψ=1−冲突次数/频次，γ_t 从高到低退火（先保词根、后挂词缀）。另构建 Hindi/Marathi/Gujarati 约 56 万词 LLM 核验形态切分金标准（IndicCorp + 规则分解 + Gemini 核验），表面边界保证可拼接还原。

## 实验与结果
形态对齐 Boundary F1：SuTRA 印地 0.586、马拉地 0.617（均最高），古吉拉特 0.584（接近 Unigram）。语义可恢复性：印地 Linear R² 相对 BPE 约 +34%（0.4464 vs 0.3329）。Hi↔Mr 翻译（3 层 Transformer，共享 32k 词表）：Marathi→Hindi chrF2 38.84、COMET 0.6554 最优；反向接近最强基线；摘要称平均 +8.08 chrF2。扰动稳健性上 Jaccard 高、Root-Affected 近零，优于纯统计分词。

## 结论
用轻量形态先验约束频率合并，可降低 Morphological Shattering，使整词语义更易从子词线性恢复，并提升翻译与扰动稳健性，而不显著推高 fertility/词表规模；未来可扩到其他富形态语言及 TTS/ASR。

## 点评
关键不是换更大模型，而是在词汇学习目标里显式惩罚跨词素合并，并保住 akshara 原子性。金标准依赖 LLM 核验，边界质量会传导到合并惩罚；对 Sandhi 强融合与词典外词仍依赖 seq2seq 推断，可能是主要误差源。虽放在 ASR 相关会场，正文实验以文本分词与 MT 为主。
