# What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR

- 论文编号：750
- 报告人：Hawau Olamide Toyin
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/toyin26_interspeech.pdf

## 问题
口吃等非典型语音同时存在 verbatim（含重复/拖长）与 intended（去流利性障碍）两种合法转写；多数评测只用单一参考并奖励“删掉障碍”，混淆用例与模型排序。

## 方法
在 FluencyBank Timestamped（3430 条）上对 11 个开源 ASR（自回归 seq2seq/transducer 与 CTC 族）分别报 isWER 与 vWER；对齐 CASA 临床口吃事件分析事件类型影响。假设：自回归更擅 intended，CTC 更贴声学 verbatim。

## 实验与结果
排序不一致：NVIDIA CTC verbatim 最优（vWER 17.20）但 intended 仅第 5；Canary-1B intended 最优（isWER 13.85）。Whisper-large-v3 intended 第 2、verbatim 第 3。同数据 NVIDIA 族内范式差异支持“训练范式偏向转写风格”。延长最易、多音节/不完整音节重复最难；intended 难“去掉”碎片，verbatim 难“保真”重复。

## 结论
非典型 ASR 必须按用例声明参考类型；自回归偏语义 intended，CTC 偏 verbatim。单参考“最佳”可能对临床或听写场景不公平。

## 点评
把评测伦理问题形式化得很清楚，双参考排名翻转是强证据。同训练集内比较增强了因果解释。尚未微调、仅英语口吃；临床标记转写（特殊 token）路线未纳入同一基准。
