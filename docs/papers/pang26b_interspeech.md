# ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition

- 论文编号：3143
- 报告人：Zi Haur Pang
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/pang26b_interspeech.pdf

## 问题
Speech LLM 做多语多模态 SER 时，性别表现差距如何随语言与模态变化尚缺系统基准；多模态融合不保证更公平。

## 方法
在 MELD-ST（英/日/德，人工标注说话人性别）上基准多种 Speech LLM。提出 ERM-MinMaxGAP：LoRA 微调 Qwen2-Audio，主损失为交叉熵 ERM；正则 R=（各语言内男女损失差的最大值）^p（主设 p=2）；λ 按验证集性别差距相对阈值 ε 用投影梯度式自适应升降。评估单模态（仅语音）与多模态（语音+真值转写）。

## 实验与结果
多语设定相对最强基线：单模态 W-F1/ACC 约 +5.5/+9.8，多模态约 +5.0/+3.6；整体性别 AVG 差距分别降约 0.1 与 1.4 量级（摘要称 0.1%/1.4%），多模态下 AVG 再降 0.80。偏差强依赖语言与模型；多模态常提准确率但不稳定缩小性别差。消融：固定大 λ 可压差距但伤 SER；自适应 λ 在性能–公平折中更优；p=2 较 p=1 更利于公平。

## 结论
给出多语多模态 Speech-LLM SER 性别偏差基准，并表明惩罚最差语言内性别损失差可同时提升识别与公平折中。

## 点评
把“最差语言间隙”作为优化目标，避免平均公平掩盖某一语的极端偏差，适合多语部署。性别为人工标注、模态用金标转写，真实 ASR 转写误差下的公平性未测；固定大 λ 的效用–公平权衡表明超参仍关键。
