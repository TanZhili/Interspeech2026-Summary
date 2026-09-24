# Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition

- 论文编号：1611
- 报告人：Chengxi Deng
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/deng26c_interspeech.pdf

## 问题
老年语音标注贵、伪标签不可靠，且说话人异质性强；直接过滤丢弃低置信样本会伤说话人覆盖，无可靠度排序的增量训练易早期污染并误差累积。

## 方法
为 Whisper 设计轻量 CEM（3 层残差 FFN，拼解码输出与 top-10 logits）估 token/话语置信度。按说话人内置信度降序均分 K 组再跨说话人聚合；从高到低增量：每步用当前模型重标下一子集并与已累积数据合并训练。再把每步微调换成说话人提示 SAT（提示长 4+LoRA），可选测试时适应与说话人自适应重标。骨干 Whisper-medium。

## 实验与结果
DementiaBank Pitt 与 JCCOCC MoCA：默认 10% 说话人有标、其余无标。相对全量伪标签半监督基线，提出方法绝对降 WER/CER 1.45%/2.27%（相对 6.21%/6.98%）。置信过滤优于随机；置信排序增量优于随机划分增量；增量+SAT 进一步提升，低置信子集伪标签质量改善最大（如 Pitt Rank5 WER 63.77→约 55）。

## 结论
置信度课程式增量与说话人自适应伪标可逐步提高老年语音半监督 ASR，并支撑未见说话人的测试时适应。

## 点评
「说话人内排序」避免扔掉整个人的困难话语，比全局 top-k 过滤更适合异质老年群体。课程从易到难抑制早期误差雪崩。依赖说话人 ID 已知，与病历场景匹配，但不适用于完全匿名无说话人聚类的数据。
