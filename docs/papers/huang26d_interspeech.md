# Before the Turn: Investigating Motion Cues Preceding Speech in Dyadic Interaction

- 论文编号：1243
- 报告人：Ying-Hsuan Huang
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/huang26d_interspeech.pdf

## 问题
计算 turn-taking 多作反应式声学边界检测，滞后于人类意图；已有视觉特征多是离散标签或统计量，未量化全身连续运动学，也未考察不同身体部位是否具有不同的预言语运动起始时间线。

## 方法
在 InterAct 3D 骨架（8.3h、241 二元场景）上定义 Shift/Hold 与有无停顿四类情形；提取部位角速度与运动多样性（FullBody/UpperBody/Hands/Head），说话人 Z-score 归一化，在上下文有界窗口内检测 \(\hat{V}_t>2\) 的最早 onset。用 Transformer 系统变化观察窗 \(W_L\) 与预测超前 \(\tau\in\{0,0.5,1.0,1.5\}\)s，比较各部位对 Shift vs Hold 的预测力。

## 实验与结果
约 30–35% 转换有明显预备动作；远端（手/头）常在发声前 0.5–0.6s 激活，UpperBody 峰值可早至约 2.9s。UpperBody 在 \(W_{0.5}\) 上 F1-Shift 达 76.81%，长窗仍稳；Head 随窗加长因点头等倾听噪声而崩。超前 \(\tau=1.5\) 时 Shift 预测可优于 \(\tau=0\)；Floor-claiming（尤其重叠 Case C）体现约 1.5s 运动多样性累积，Floor-holding 则在发声碰撞点爆发。静默间隙（Case B）头部位有短时协商信号。

## 结论
交际意图在发声前就以异步多模态运动编码：上半身提供最长稳定超前，远端给短窗同步；抢轮与守轮的运动时间线本质不同，支持「主动 turn-taking 协商」视角。

## 点评
把问题从「加视觉特征」转到「量化部位特异的预言语时间学」，证据链（onset 统计→观察窗→超前预测→运动学验证）清晰。强在生物力学可读性；局限是二元、半结构化、被试少，且预测器非端到端部署系统，外推到多人/实时代理需谨慎。
