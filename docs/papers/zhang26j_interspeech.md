# Improved modeling of vocal fold contacting and de-contacting in a geometric vocal fold model

- 论文编号：753
- 报告人：Tianyi Zhang
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26j_interspeech.pdf

## 问题
几何声带模型常把接触简化为正弦位移在中线截断，忽略部分接触阶段组织形变减速与分离时粘着力导致的初速降低，损害合成自然度。

## 方法
在 Titze 型几何模型上引入生物力学启发的渐进接触/去接触，并保留/改进声门面积脉冲左右偏斜机制；接入发音器官合成器。与无软接触的 2019 参考模型做 A/B 偏好与五分制 MOS（多组预发声参数、合成句）。

## 实验与结果
新模型在 A/B 中获 58.1% 偏好（95% CI [56.0%, 60.2%]）；MOS 均值 3.02 vs 旧模型 2.68。混合效应模型确认 NEW 主效应提升自然度。

## 结论
更真实的接触/去接触动力学可改善几何声源的感知自然度，利于低资源可控发音合成。

## 点评
针对声源周期中「短但关键」的碰撞阶段做机制修补，并用听感实验闭环验证。强在相对 2019 模型的对照清晰；脆弱点在整体 MOS 仍中等，自然度瓶颈可能还在声道/韵律等其它模块。
