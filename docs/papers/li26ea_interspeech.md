# U2A-Net: Physically Motivated Ultrasound-to-Audio Neural Modeling for Parametric Array Loudspeakers

- 论文编号：2390
- 报告人：Mengtong Li
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/li26ea_interspeech.pdf

## 问题
参量阵扬声器（PAL）非线性强，A2A 把调制与空中自解调揉成黑盒，复杂度高；U2U 又被强超声载波主导，难精建模可听频段 THD/IMD。

## 方法
提出 U2A 建模：输入为已调超声驱动 \(s_u(t)\)（192 kHz），输出为可听声 \(y_a(t)\)（48 kHz）。多速率 WaveNet：16 残差块 + 可学习 4× 下采样（两层 stride-2 Conv），联合波形与频谱幅度 MSE。在消声室 USBAM PAL（576 阵元，40 kHz）采集约 3 h 语音/音乐/环境声同步数据（7:2:1）。对比同骨干 A2A-Net 与二阶 U2A-Volterra。

## 实验与结果
四级输入幅度下，U2A-Net 平均绝对 THD/IMD 偏差最低（如 level 1.0：THD 0.52%、IMD 1.26%），且文称平均非线性失真建模误差低于 1.62%。大信号时相对 A2A 优势更明显；U2A-VF 因二阶表达力不足，THD/IMD 曲线近零、误差大。线性频响三方法接近，差异主要在非线性自解调。

## 结论
物理动机的 U2A 表述让网络专注自解调，在代表 PAL 上稳定优于 A2A 与低阶 Volterra，适合 PAL 辨识与后续补偿。

## 点评
输入–输出域对齐 Westervelt 物理，比单纯加大 A2A 容量更干净。多速率下采样是必要工程件。当前仅一个 USBAM 原型与轴上 1.8 m，外推到其他调制/离轴/混响环境仍待证。
