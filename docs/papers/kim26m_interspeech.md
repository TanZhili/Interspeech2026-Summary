# Physics-Aware Deepfake Detection via Distance–Speech Consistency

- 论文编号：1541
- 报告人：Kyeongrae Kim
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26m_interspeech.pdf

## 问题
音视频 deepfake 检测多依赖唇–语音同步，且面向静态正面说话视频；动态、野外场景下说话人移动、唇部线索退化时可靠性下降。需要与唇同步互补的物理约束。

## 方法
利用真实录音中语音能量随说话人–摄像头距离可预测变化、伪造常破坏该耦合：从视频估计距离，从语音提取距离相关声学量（如 SNR、C50），检验一致性以判真伪；可与唇同步检测器简单集成。在 DF24、AuViRe RealWorld 等野外数据上训练/评测，并构造强动态子集 DF-Dynamic。

## 实验与结果
DF-Dynamic 上 ROC-AUC：SpeechForensics 0.5096、AuViRe 0.5517、本文 0.7449。全文对完整集与消融有更多表；摘要称物理线索在动态场景有效，并与唇同步集成可跨数据集稳定增益。

## 结论
作者认为距离–语音物理一致性可作为动态说话视频的有效伪造线索，补充唇同步范式。

## 点评
把声学物理先验引入 AV 伪造检测，针对“野外动态”痛点明确。距离估计与房间声学假设在剪辑/多麦/强后处理视频上可能失效；与唇同步集成依赖各模态独立错误模式不完全重叠。
