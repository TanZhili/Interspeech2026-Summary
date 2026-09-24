# From Echo to Accuracy: Robust Voice Quality Assessment Using Blind Unsupervised Diffusion-based Dereverberation

- 论文编号：2608
- 报告人：Sven Franz
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/franz26_interspeech.pdf

## 问题
客观嗓音质量指标（如 CPPS）对混响敏感，临床治疗室录音会系统性压低或扭曲病理排序；需不依赖测得 IR 的盲去混响。

## 方法
两库无回声嗓音样本卷积真实治疗室 IR，再用无监督扩散去混响 BUDDy。检验：(H1) 首次去混响对 CPPS；(H2) 混响对 CPPS 水平与排序；(H3) 二次去混响能否恢复水平与排序。

## 实验与结果
低混响录音去混响未引入系统 CPPS 偏置；混响条件下降的 CPPS 经处理后得到补偿。连续言语上嗓音质量排序可重建，CPPS 接近无回声参考水平（跨库一致）。

## 结论
盲扩散去混响可有效缓解房间声学对连续言语客观嗓音评估的扭曲，支持更房间无关的 CPPS 应用。

## 点评
把增强算法目标对准临床声学指标而非听感/ASR，场景贴切。结论主要针对连续言语与所测治疗室 IR；极短元音任务与极端混响外推仍需验证。
