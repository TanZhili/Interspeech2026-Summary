# An Approach to Simultaneous Acquisition of Real-Time MRI Video, EEG, and Surface EMG for Articulatory, Brain, and Muscle Activity During Speech Production

- 论文编号：140
- 报告人：Kevin Huang
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lee26b_interspeech.pdf

## 问题
言语产生跨神经计划、肌电与发音运动；既往多模态最多两两组合，缺少 rtMRI+EEG+表面 EMG 同步，且 MRI 梯度、心电与肌电伪迹严重。

## 方法
0.55T 上螺旋 bSSFP rtMRI（约 99 fps）+ 光学麦克风；BrainVision MR 兼容系统采 EEG/EMG/ECG/EOG（5 kHz，光纤同步 MRI 时钟）。面肌三通道 EMG。多阶段去噪：平均模板减梯度伪迹 → BCG/脉冲伪迹 → ICA（含 EMG/EOG 参考）去肌电与眼电。先导：1 名英语男说话人，发声/无声/想象，机内与机外对照。

## 实验与结果
初步结果显示伪迹明显衰减，可同时观察声道运动、面肌与脑电。论文定位为可行性与管线展示，强调对言语神经科学与静默/想象言语 BCI 的潜在价值；代码与数据公开。

## 结论
三模态同步采集在技术上可行；专用伪迹抑制是关键。完整科学分析待管线成熟后展开。

## 点评
贡献主要在采集与去噪工程，填补“脑–肌–声道”同窗空白。单人先导、电极数有限，定量神经科学结论尚早，但对后续开源实验平台意义大。
