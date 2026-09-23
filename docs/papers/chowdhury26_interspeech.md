# Predicting Cognitive Load from Speech and Interaction Dynamics in Dyadic Conversations

- 论文编号：3052
- 报告人：Tahiya Chowdhury
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chowdhury26_interspeech.pdf

## 问题
语音认知负荷研究多在受控单任务、离散分类设定下进行，随机划分易高估泛化；双人协作中轮换、重叠等交互动态与连续 NASA-TLX 负荷的关系仍不清楚。

## 方法
基于 AVCAffe 远程协作数据（53 对、最多 9 任务、106 人），按任务切 30s 窗，Silero VAD 过滤弱语音窗。特征分三组：OpenSMILE eGeMAPSv02 静态声学（88 维）、一阶差分时间动态（88 维）、仅用计时的交互特征（说话占比、重叠/静音窗比例、话轮切换等）。以共享 GRU 编码双人序列、均值池化后双回归头预测个体 NASA-TLX（0–21），联合 MSE；对照为任务级聚合特征上的 Random Forest。评估用 Leave-One-Dyad-Out，主指标 CCC，辅以 PCC、RMSE。

## 实验与结果
静态声学 GRU：时间需求 dyad CCC 0.42 最稳；心理需求个体不对称（A 约 0.31，B 约 0.13）；努力/绩效有弱信号；挫折/体力接近无效。GRU 对时间需求优于 RF（约 0.41 vs 0.33），但 Wilcoxon 校正后与 RF 差异不显著。交互特征 alone 将时间需求 CCC 提至 0.51；A+I 使四维负荷均提升（心理 0.22→0.32 等）。置换重要性：时间需求关联重叠与话轮切换；心理需求关联说话时间不平衡。对间 CCC 异质性大（部分 0.6–0.9，亦有负相关）。

## 结论
双人对话语音可对时间/心理等负荷做适度、可跨对泛化的回归；交互动态提供互补信号，但可能混入任务结构效应，且样本量限制了带注意力序列模型收益。

## 点评
把问题从“分类高/低负荷”改成跨对回归，并显式拆开声学 vs 交互，方向对自然协作场景更诚实。最强信号来自 10 维交互特征，说明“测的是负荷还是任务诱发的轮替模式”仍需拆解；小样本 LODO 下 GRU 未显著碾压 RF，模型复杂度应服务于可解释特征而非堆砌。
