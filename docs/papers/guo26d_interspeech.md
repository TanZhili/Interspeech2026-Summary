# Lightweight Convolutional Front-ends for Real-time Framewise Phoneme Recognition in Cochlear Implants

- 论文编号：2689
- 报告人：Yuchu Guo
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/guo26d_interspeech.pdf

## 问题
人工耳蜗端侧需因果、≤约 10 ms 时延的语音处理；音素级 TF 掩蔽增强依赖帧级音素分类，但缺少在 MCU 约束下对轻量卷积前端架构取舍的系统评测。

## 方法
在严格因果设定下，为 LSTM/GRU（及文中提及的 Mamba/注意力变体）加轻量卷积前端：Conv1D-F、Conv1D-T、Conv2D，含标准/膨胀层深 L∈{1,2,4,6,8}。交叉熵训练 2 s 片段。在 STM32F746G 上用 Cube.AI 测 flash/RAM/MAC/时延（可变形卷积、注意力、Mamba 因平台限制未上板）。

## 实验与结果
加卷积前端普遍抬升帧级音素准确率（如 GRU+Conv2D 8L 达 38.94%，无前端 Large GRU 约 34.34%）。1D 结构多数保持亚 10 ms 时延与小内存；Conv2D 深网络工作内存与时延急剧上升（8L 时延约 14 ms、RAM 约 78 kB）。膨胀卷积以可预期方式扩感受野。深度并非越深越好，常在 L=2–4 附近见峰。

## 结论
作者认为因果轻量卷积前端可提升 CI 相关音素分类，1D+膨胀是部署友好折中；并给出 MCU 实测资源表供架构选型。

## 点评
贡献偏工程基准：准确率–时延–内存三元权衡写清楚。音素准确率绝对水平仍不高（约 30–39%），但正文引用此前工作称这一水平已可助掩蔽增强。平台限制使部分先进模块缺部署数据；全文抽取后半略残缺，以 Table 1 与方法描述为主。
