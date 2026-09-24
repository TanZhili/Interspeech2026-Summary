# PAN-Mask: Pathology-Aware Neurological Masking with End-to-End Learnable Weights for Neurological Disorder Detection from Speech

- 论文编号：1006
- 报告人：Qi Sun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26b_interspeech.pdf

## 问题
WavLM 等自监督分类沿用内容无关随机掩码，忽略病理语音中稀疏、局部的临床生物标记，易 shortcut 到少数显著帧。

## 方法
PAN-Mask：轻量检测器提取六类可解释声学描述（节律不规则、停顿、音高单调、能量下降、嗓音质量、周期性），可学习注意力聚合为帧级病理显著性；训练时优先掩蔽高显著性段，迫使编码器学分布式表征。检测器与分类器端到端联合优化。六数据集、三病种（AD/PD/抑郁）、五语言，超参固定。

## 实验与结果
相对随机掩码准确率提升 8.31–22.72 个百分点（平均 13.82%）。框架跨病种/语言无需手工重设特征重要性，并提供可解释显著性洞察。

## 结论
病理感知掩码作为任务感知正则，可提升神经疾病语音检测并抑制 shortcut，同时给出临床可解释线索。

## 点评
把“别只盯最显眼的病理片段”写成可微掩码目标，方向新颖。增益幅度大但依赖各数据集基线强弱；显著性是否真正对齐临床标注仍需外部验证。
