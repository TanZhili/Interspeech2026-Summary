# NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation

- 论文编号：2211
- 报告人：Qinke Ni
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ni26_interspeech.pdf

## 问题
表达 TTS 越来越多纳入非语言发声（NV），但评测缺标准、缺配对真人参考，常只能粗查“有没有事件”，无法量化与真实录音差距。

## 方法
发布 NV-Bench：1651 条多语（中/英）野外话语、配对 GT，按 Batliner 功能分类覆盖 14 类 NV；平衡单标签与相对平衡多标签子集。训多语 NV-ASR（SenseVoice-Small 微调）作自动评委。双维协议：指令对齐（CER/PCER/OCER）与声学保真（SIM、DNSMOS、FAD/FD、主观）。评 Orpheus、CosyVoice 变体及自训 NV-CV3/NV-FlexiVoice。

## 实验与结果
NV-ASR 在标准 ASR 与 NV 集上可靠（如 SMIIP-NV CER 1.29%）。多数模型 PCER 仍高（控制弱）；NV-CV3、NV-FlexiVoice 在对齐与保真上整体更强。客观指标与人类感知相关，可作标准化框架。

## 结论
NV-Bench 把 NV 当作交际行为评测，分离“控不住”与“听不真”；公开测试集与协议支撑可复现对比。

## 点评
配对 GT + 平衡类别 + PCER 是相对现有“有没有笑声”评测的实质进步。依赖 NV-ASR 作裁判，其标签错误会传导；多标签子集仍受长尾共现约束。
