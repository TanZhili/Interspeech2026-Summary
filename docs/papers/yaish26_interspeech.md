# Active Constructive Interference for Speech

- 论文编号：222
- 报告人：Ofir Yaish
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yaish26_interspeech.pdf

## 问题
传统 ANC 只做破坏性干扰消噪，被动语音增强则在麦克风后重建设；二者均未在声学域主动“塑造”语音。作者提出 Active Speech Enhancement（ASE）：同时衰减干扰并放大语音相关分量。

## 方法
ASE-TM：在前馈 ANC 设定下，误差麦作修改麦，使 eh=d+a 跟踪清洁目标 c。网络基于 SEmamba，用 Mamba2 的 TFMamba + 中间多头注意力，输出抵消信号 y 的复谱，经扬声器非线性与次级路径后与主路径叠加。损失含时域/幅值/复谱、防缠绕相位、度量对抗与一致性。任务覆盖加噪（VoiceBank-DEMAND）、去混响、去削波；仿真矩形房间与 SEF 扬声器非线性。

## 实验与结果
Table 1：去噪 PESQ 2.98 / STOI 0.99 / NMSE −21.76（优于 ARN 2.45、THF-FxLMS 2.37）；去混响 PESQ 2.43；去削波（η=0.25）PESQ 3.09。消融显示 Mamba2+损失改动贡献最大，注意力加速收敛。预测未来 500 样点以满足因果时 PESQ 仍约 2.96；约 22.3M 参数。

## 结论
主动建设性干扰可在消噪之外显式增强语音，在三类 ASE 任务上全面超过改编后的 ANC 基线。

## 点评
把 ANC 目标从“eh→0”翻转为“eh→c”，范式清晰。强结果部分来自与被动增强目标更对齐的损失与架构；基线本为消噪设计，在去混响/去削波上吃亏，对比解读需谨慎。仿真房间与固定几何下的实时部署仍待硬件验证。
