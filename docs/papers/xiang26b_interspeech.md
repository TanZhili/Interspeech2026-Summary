# Revisiting Delay Compensation via Feature-Level Temporal Accumulation in Continuous Emotion Recognition

- 论文编号：3030
- 报告人：Jian Xiang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiang26b_interspeech.pdf

## 问题
连续情绪识别（CER）标注常滞后于信号；主流做法是对标签做固定时移的 shift-based delay compensation（SDC），需截断边界且对延迟参数敏感。作者认为标注更像在时间窗上累积证据，而非瞬时判断的延迟报告。

## 方法
提出 accumulated delay compensation（ADC）：对冻结 wav2vec2.0 特征各维做因果滑动均值滤波，群延迟 τ=(N−1)/2，不改输入–标签对齐。后端用 Constrained Neural ODE。RECOLA 官方划分；CCC 评测。对比实践级 RA-SDC（训练/评测截断对齐）与公平设定（同扩展序列上 ADC 均值滤波 vs 纯延迟）。

## 实验与结果
实践级：唤醒 ADC 峰值 CCC 0.816（τ=2s）vs RA-SDC 0.808（1.5s）；效价 ADC 0.485（τ=6s，一 seed 无效）或有效最佳 0.484（4.5s）vs RA-SDC 0.473（3s）；均超无补偿基线（0.746/0.385）。唤醒偏好较短积分窗，效价偏好较长窗；ADC 对延迟参数更稳健。

## 结论
特征级时间累积可同时平滑与内生延迟补偿，是比标准时移更优的 CER 延迟处理方式，且维度依赖窗口长度。

## 点评
把延迟补偿从“挪标签”改成“积特征”，物理上对应标注者累积证据，并自然低通。强处是公平对比与唤醒/效价差异分析；脆弱处是仅 RECOLA、短块拼接与常数填充边界，以及效价不稳定 seed。
