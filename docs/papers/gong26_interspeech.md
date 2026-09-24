# NCPSZ: A Nonlinear Control Network for Miniature Loudspeakers in Personal Sound Zone Applications

- 论文编号：182
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gong26_interspeech.pdf

## 问题
个人声区（PSZ）线性方法在微型扬声器强非线性失真下失效；辅助扬声器高电平反相消漏易产生谐波，线性滤波器难以复现所需非线性分量。

## 方法
NCPSZ 非对称双网：大容量 ModelNet（约 32.71M）离线拟合扬声器–麦克风非线性；轻量因果 CtrlNet（约 0.18M）实时预补偿。锚点扬声器（主听筒）维持亮区目标，CtrlNet 驱动辅助扬声器抑制暗区非线性泄漏。损失为时频 BZ 保真与 DZ 能量最小化。在半消声室智能手机漏音场景采集（THD 3.2%@250 Hz），LibriSpeech 驱动 >1300 条高电压录音。

## 实验与结果
ModelNet 测试 MSE 约 1.6×10⁻⁹。200–2000 Hz 平均 AC 相对线性 VAST +3.78 dB，相对参数匹配因果 CNN +1.80 dB；亮区 SPL 接近目标，暗区更低。

## 结论
显式可微电声模型 + 锚点策略可在微型扬声器非线性体制下提升漏音抑制，并保持边缘可部署的因果控制。

## 点评
把 PSZ 从线性滤波器优化推进到“可微扬声器模型进环”，切中手机漏音实际。锚点扬声器降低对 BZ 损失的依赖，工程合理；收益相对线性天花板更可信，相对 CNN 的优势则指向 GRU 时序建模。
