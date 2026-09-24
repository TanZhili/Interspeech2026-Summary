# Carrier-Aware Sound Zone Control for Parametric Array Loudspeakers

- 论文编号：2170
- 报告人：Mengtong Li
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/li26da_interspeech.pdf

## 问题
参量阵扬声器（PAL）靠超声载波与边带非线性自解调产生可闻声；既有声区控制（SZC）多只优化边带激励，把载波当固定背景，自由度不足，声学对比度与解调效率受限。

## 方法
提出载波感知 SZC：对称调制结构下分别测量边带条件与载波条件有效传递函数 Gs(q)、Gc(w)，使解调场对边带权重 w 或载波权重 q 近似线性。采用有限阶段交替优化：初始载波全 1 → 测 Gs 优化边带 → 测 Gc 优化载波（映射为共轭）→ 再对齐边带。以 ACC 为验证；仿真用 k-space，实验 24×24 列 PAL（40 kHz 载波）、消声室扫描。

## 实验与结果
相对仅边带 ACC，载波感知在亮区更集中、暗区泄漏更少（仿真与实测一致）。宽带白噪声实验、相同功率约束下，总 AC 由 12.4 dB 升至 23.6 dB（+11.2 dB），亮区总 SPL +7.0 dB。超声场显示载波与边带空间对齐是增益来源。

## 结论
将载波作为主动控制维可显著提升 PAL 声区对比与解调效率，利于紧凑定向空间音频/私密语音渲染。

## 点评
抓住 PAL“解调∝载波×边带”的物理本质，把被忽视的载波纳入 ACC，比继续堆边带自由度更对症。有限交替避免反复重测成本，工程务实；载波优化在单音频点（1 kHz）完成再宽带对齐，宽带最优性仍可能受限。
