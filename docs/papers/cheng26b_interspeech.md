# Active Noise Control With a Gain Constraint for Micro-Loudspeakers

- 论文编号：2202
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/cheng26b_interspeech.pdf

## 问题
微型扬声器低频复现能力弱，固定滤波 ANC 的 Wiener 解在低频增益过高易引起机械过冲；串高通虽限功率却增加群时延、降低降噪上限。

## 方法
在设计固定控制滤波时对频率响施加增益约束：先提 ANC-LF-FRC（仅低频约束）防过冲；因期望响应间断引发 Gibbs、损 NR，再加 ANC-FRC，对目标降噪带内其他频点也加约束。仿真与实测对比无约束 Wiener、高通级联、LF-FRC 与 FRC。

## 实验与结果
LF-FRC 可抑低频过冲但 NR 曲线出现起伏；FRC 在目标带更平滑。Table 1：FRC 在 100–500/500–1000/1000–2000 Hz 训练噪声上平均 NR 约 1.55/13.96/18.55 dB，优于高通与 LF-FRC，接近 Wiener 中高频表现且避免低频过冲。

## 结论
在滤波器预训练阶段施加频响增益约束，可在不增加电子延迟的前提下兼顾微型扬声器保护与有效降噪。

## 点评
把硬件能力直接写进固定滤波设计目标，比事后级联滤波更贴产品 ANC。Gibbs 分析解释了“只压低频不够”，FRC 是务实补丁。
