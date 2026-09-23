# How Speaker Normalization Procedures Influence the Computational Modelling of Non-native Vowel Perception: Implications for the L2LP model

- 论文编号：1574
- 报告人：Jooyoung Lee
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26l_interspeech.pdf

## 问题
用神经网络建模非母语元音感知时，说话人归一化几乎是必需的，但既有比较多在单语内做；跨语言场景下既要消说话人差异，又要保留 L1–L2 音系间有意义的声学距离（L2LP 假设分离感知语法）。何种归一化最能复现无英语知识的西班牙语听者对美式英语元音的归类，以及这对 L2LP 的 Full Copying 意味着什么，尚不清楚。

## 方法
用 DIMEx100 墨西哥西班牙语五元音（/i,e,a,o,u/）的 F1–F2 中点训练 MLP（2 输入、两层 128 隐单元、5 输出），在六种输入处理下只改归一化：raw Hz、gender-wise Z、Lobanov、Nearey 1/2、Gerstman。为模拟 L1 听者，把从西班牙语样本估计的归一化参数套到 TIMIT 九个美式英语单元音上，得到 5×9 归类概率矩阵，再与 Escudero & Chládková 的真人归类矩阵比 MAE、RMSE、Pearson r、top-1 类别匹配数（/9）。训练/测样本约 123,884 / 14,091；跨语言模拟用 TIMIT 测集 10,825 token。

## 实验与结果
Lobanov 全面最优：MAE 13.93、RMSE 23.30、r=0.75、匹配 7/9；其次多为 Nearey 1 与 gender-wise Z（各 6 匹配）；Gerstman 最差（MAE 25.60、r=0.16、匹配 3）。矩阵上 Lobanov 最接近真人的块对角模式，且是唯一把英语 /u/ 主要映到西班牙语 /u/ 的方法（其余多映到 /o/）。

## 结论
尽管人们担心 Lobanov 会过归一化、抹掉跨语言差异，它反而最贴合“无目标语知识”听者；作者据此把 Full Copying 延伸到 L1 归一化行为本身，并推测随 L2 发展、需保留跨语言对比时 Nearey 类方法可能更合适。局限：仅 F1–F2、MLP 架构较简。全文末尾结论句有抽取截断。

## 点评
核心贡献是把“归一化方法排行榜”绑到明确的听者状态（L2LP 初始态），而不是追求类别可分性最高的那一种。用西班牙语参数去归一化英语输入，是设计上刻意的 L1 滤波器；脆弱点在于真人基线来自合成元音、模型输入只有两个共振峰，且“过归一化=Full Copying”仍是事后解释，需用不同水平学习者数据验证 Nearey 是否随水平上升更优。
