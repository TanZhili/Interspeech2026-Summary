# TSExplorer: An interactive data annotation and exploration tool for time-series data

- 论文编号：3572
- 报告人：Einari Vaaras
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/vaaras26_interspeech.pdf

## 问题
时序数据（语音、视频、生理信号等）常用高维特征，但标注与分析往往顺序浏览或静态汇总，难以在特征空间中看清样本关系、比对不同表征或做增量标注。

## 方法
发布跨平台 GUI 工具 TSExplorer：离线提取高维特征后，在交互式 2D 散点图（t-SNE/PCA/UMAP）中浏览整库；点选样本联动音频/视频/波形/谱图等 widget。支持随机、顺序、farthest-first 采样与队列；可切换多种特征表征；标签用下拉或快捷键修改。布局可定制，widget/2DV/采样策略可扩展。Python + PySide6 + PyQtGraph，播放依赖 VLC。

## 实验与结果
正文以系统设计与资源开销为主：如 10 万×160 维 t-SNE 约 1.8 GB RAM、单核约 8 分钟；10 万语音样本预载音频与多特征约 5.1 GB，按需加载可 <0.4 GB；空闲约 0.3 GB。工具已开源，并引用先前工作 [6] 的描述与评估。

## 结论
提供面向时序数据的通用交互标注与探索环境，覆盖无标/半标/全标工作流及特征空间反馈，便于探索分析、标注与标签精修。

## 点评
把“特征空间导航 + 多视图检视”做成可扩展产品，贴合人机协同标注。本文偏工具介绍，量化用户研究细节主要指向此前论文；大库 2DV 预计算仍是使用门槛。
