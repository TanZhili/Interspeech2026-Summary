# Label Correction Enhanced Dual-Stream Multiple Instance Learning for Weakly-Supervised Depression Detection in Speech

- 论文编号：1716
- 报告人：Xinzhou Xu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/sun26e_interspeech.pdf

## 问题
语音抑郁检测在弱监督下同时面临不准标签（标注/问卷错误）与不精确标签（抑郁线索仅在录音局部）；既往工作少同时处理二者。

## 方法
提出 LC-DMIL：样本级 1D-CNN+Bi-LSTM 骨干上融合似然比翻转与原型余弦相似度校正（权重 γ），得到校正标签；再把样本切为实例袋，双流 MIL（max-rule 找关键实例 + 基于关键实例的 MIL-aggregator）融合输出；样本/实例损失含分类与熵项。输入 80 维 log Mel。

## 实验与结果
DAIC-WOZ（AVEC 2017 划分）：交换 PHQ-8∈[7,12] 的训练标签模拟不准监督。LC-DMIL UAR 0.651、F1 0.642，优于 DepAudioNet、SpeechFormer、SLLC 等（UAR 差异 p<0.005）。γ=0.3 优于 0.7；双流优于单流与 mean/attention 等替代。AVEC 2014 随机翻 3/7 标签时 UAR 0.670，亦优于仅 LC 或仅 MIL。

## 结论
标签校正处理不准监督、双流 MIL 处理不精确监督，二者结合在弱监督语音抑郁检测上有效。

## 点评
把「标错」与「标粗」拆成校正模块与实例袋学习，问题分解清晰。弱监督靠人为翻边沿 PHQ 分数构造，与真实标注噪声分布可能不同；μ、实例数等超参敏感，部署需验证集重调。
