# Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs

- 论文编号：2406
- 报告人：Philipp Grundhuber
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/grundhuber26_interspeech.pdf

## 问题

声学传送（AT）等分区神经音频编解码用交叉重建等指标评解缠，但解码器可忽略错误分区中的冗余，泄漏检测不到；经典 DCI/MIG 也不适配分区级结构。

## 方法

将预训练 AT 编码器当固定特征提取器，对 speech / acoustic 两分区分别训练相同轻量 MLP 探针：回归 T60、C50、DRR（分频带+宽带），分类说话人 ID。以意图分区与非意图分区性能差 Δ 作解缠度量。数据：DNS5 read speech ⊕ GWAsmall RIR。系统扫描训练任务集、量化级数 N∈{4,8,16}/未量化、声学流时间下采样等配置。

## 实验与结果

AT 模型在说话人上解缠显著（如 N=8 时 Δacc 达 56.8 pp：83.1% vs 26.3%）；声学信息仅部分分离，speech 分区 T60 相关常仍 &gt;0.75。量化放大说话人分离，但声学泄漏不变；声学流下采样对房间参数估计影响小。声学嵌入盲估宽带 T60 RMSE 0.094 s（ρ=0.947），距监督 CRNN-MB（0.082 s）约 0.02 s 内。ScoreQ 等输出质量与解缠不对齐：无解缠的 +Dereverberation 基线也可有不错 ScoreQ。

## 结论

作者认为探测比交叉重建更能暴露分区泄漏；AT 目标迫使说话人信息进 speech 分区，却无对称压力把房间信息推出 speech，故解缠不对称。未来可用对抗/梯度反转等显式去相关。

## 点评

把“解缠是否真发生”从听感/重建质量里拆出来，用物理可解释的房间参数作探针，诊断力强。简单 MLP 测到的是泄漏下界。仅覆盖时不变因素；语言学内容探针与其他编解码架构尚未验，结论对 AT 训练目标结构的依赖很强。
