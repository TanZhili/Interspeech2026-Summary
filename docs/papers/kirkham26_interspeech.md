# PyPhonPlan: Simulating phonetic planning with dynamic neural fields and task dynamics

- 论文编号：1804
- 报告人：Sam Kirkham
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kirkham26_interspeech.pdf

## 问题
任务动力学把发音目标当作固定吸引子，缺少学习、记忆与感知对产出的内在机制；DNF 与任务动力学的整合研究增多，但缺少面向言语社区、把两者直接打通的现代开源工具。

## 方法
开源 Python 工具包 PyPhonPlan：一维动态神经场（输入、墨西哥帽交互核、阈值门控）、Hebbian 记忆场、跨场耦合与可选 latched gate（防止感知耦合误触发产出）；用规划场峰位置作为临界阻尼谐振子的时变目标，求解 tract variable 轨迹。模块化支持多层场、手势输入与可视化。

## 实验与结果
以三层感知–规划–记忆模型仿真简化 shadowing：1 基线 + 10 阴影 + 1 washout。基线峰在响应位置 x=3；阴影期被感知输入拉向 x≈1.56；washout 仍偏基线约 −0.29（x=2.71），记忆痕迹驱动收敛，并体现在 tract variable 轨迹上。作者强调为示意性人工例。

## 结论
提供可复现、可扩展的 DNF+任务动力学规划到产出框架。讨论指出输入定时仍手动、缺少完整 articulator–tract 映射、高维扩展受限；展望接 TADA、状态反馈与说话人–听者耦合。

## 点评
把理论组件工程化，降低发音规划动力学入门成本。示例能展示交互收敛的涌现机制，但定时与 1D 人工参数空间限制定量拟合人类数据的力度；价值主要在工具与可复现实验脚手架。
