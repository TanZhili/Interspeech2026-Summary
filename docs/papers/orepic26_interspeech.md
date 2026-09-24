# SELFIX: An Interactive System for Natural Self-Voice Approximation

- 论文编号：1395
- 报告人：Pavo Orepic
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/orepic26_interspeech.pdf

## 问题
录音自我声音因缺骨导滤波而显「不像自己」；既往多频段均衡搜索空间过大、维度不感知对齐，难收敛到普适滤波器。

## 方法
SELFIX：交互界面用感知动机的低维滑杆（音高 F0、声道长度 VTL、低频倾斜、梯形滤波器等，经 PSOLA 等变换），随机化无标签初始位置。被试反复调到「像自然说话自己」并评匹配度与信心（0–100）。初步研究 N=25（13 男/12 女）。

## 实验与结果
被试调整一致且匹配/信心评分高，支持界面效度。全体倾向增强低频（约 <600 Hz）；男性额外降低音高、增长声道长度。PCA 与性别×滑杆交互显示自我声音近似超出单纯频谱均衡。

## 结论
结构化感知参数可为可扩展个性化自我声音建模提供声学基础。

## 点评
把无引导 EQ 搜索换成说话人身份相关的少数维度，实验设计干净。强在性别差异发现；脆弱点在四参数未必覆盖个体差异全貌，且实验室朗读材料与日常自我暴露条件不同。
