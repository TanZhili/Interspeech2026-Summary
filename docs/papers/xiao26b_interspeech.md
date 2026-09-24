# WSG: Clinically-Informed Weighted Speech Graphs for Dementia Detection

- 论文编号：2266
- 报告人：Yao Xiao
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/xiao26b_interspeech.pdf

## 问题
Speech graph 能刻画词检索结构，但既往节点仅为抽象词，未编码语义、发音切换与 Cookie Theft 的空间 CIU 信息，难对齐临床切换/叙事效率指标。

## 方法
提出 Weighted Speech Graphs（WSG）：仅用目标词（SVF 动物、PVF 以 p 开头真词、CTD 的 CIU）建有向图；边权为语义（ConceptNet Numberbatch）、音系（SoundVectors）、空间（CIU 坐标欧氏距离）与时间间隔的距离/相似度，再按拓扑特征极性选择。特征含 N、E、WC 及加权/未加权 diameter、ASP、density、ATD。用朴素贝叶斯与嵌套交叉验证上的 SFS；开源 PyWSG。

## 实验与结果
CognoMemory（SVF/PVF/CTD）与 ADReSS（CTD）。仅用目标词相对全转写显著提升（如 PVF F1/AUC 0.55/0.56→0.75/0.75）。SFS 常只选 1–2 个特征即可接近全基线特征集；PVF 常选 diameter(phon)（痴呆组均值 2.8 vs HC 5.3）；SVF 多见时间加权直径；CTD 多见空间加权 ASP/ATD 与 WC。ADReSS 上最终子集 F1/AUC 0.73/0.75，与目标词+基线特征相当。

## 结论
临床属性边权使极少特征即可匹配完整未加权特征集，并提供可解释的切换/空间/时间模式；目标词构图是关键前提。

## 点评
把临床切换与 CIU 空间叙事直接写进边权，比纯拓扑更可解释。依赖 ASR（CognoMemory）或词典抽取目标词，抽取误差会扭曲图；特征选择在小样本上折间波动大，最终子集宜视为稳健候选而非唯一真值。
