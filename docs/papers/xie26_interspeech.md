# FakeSound2: A Benchmark for Explainable, Traceable, and Generalizable Deepfake Sound Detection

- 论文编号：1157
- 报告人：Zeyu Xie
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xie26_interspeech.pdf

## 问题
通用音频 deepfake 检测多停在片段级真假二分类，无法回答何时被改、如何被改、来自哪个源，且对未见生成器易崩溃（文中称操纵类型准确率可由 93.1% 掉到 32.4%）。需要面向可解释、可追溯与可泛化的诊断基准，而非只比二分类分数。

## 方法
提出 FakeSound2 基准：覆盖 6 类操纵（Generation、Editing、Inpainting、Separation、Splicing、Addition）与 12 个源，含 clip-wise 与 frame-wise；评测定位（Accidentify、F1segment）、溯源（Accsource）与操纵类型识别（Accmanipulation），并区分 in-domain / out-of-domain。资源公开于项目页。

## 实验与结果
Table 2：域内定位普遍很强（多类 Accidentify/F1 近 100%），但域外操纵类型准确率崩溃（如 Generation 99.40%→4.23%，Editing 87.96%→0.00%，Inpainting 99.75%→46.49%）。结论是现有模型擅定位、弱解释与弱泛化，易记生成器伪迹。

## 结论
作者主张把 FakeSound2 当作诊断工具：稳定追问模型是否理解伪造本质，而非追逐当前源上的排行榜分数。

## 点评
把 DSD 从“判真假”拉到 how/when/where，对取证叙事有价值；域外操纵类型崩盘的诊断结论比单一 SOTA 数字更有信息量。基准本身依赖当前 12 源构造，生成技术迭代后仍需持续扩展。
