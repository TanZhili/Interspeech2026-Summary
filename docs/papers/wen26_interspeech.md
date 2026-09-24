# Addressing random spatial translations in measured microphone directional responses by maximizing finite order energy

- 论文编号：149
- 报告人：Xue Wen
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wen26_interspeech.pdf

## 问题
实测麦克风/阵列方向传递函数（DTF）相对参考中心存在未知空间平移；平移在球谐域间重分配能量，破坏“高阶≈更细空间细节”的假设，给有限阶处理带来不确定性。

## 方法
定义有限阶质心（FOC）：在平移类中寻找使阶数 ≤L 的能量比（FOER）最大的平移，从而最小化截断误差。离散球网格上对球谐正交化算能量，并用阶权重正则与分频段调度优化求稳。可推广到 2D 与阵列（最大化各麦最低 FOER）。将参考中心移到 FOC 作校准。

## 实验与结果
S24+、EasyCom 眼镜等：单麦 FOC 靠近物理麦、阵列 FOC 靠近几何中心，并可暴露测量偏置。插值/平滑：FOC 平移后相对误差下降。方向感知 Ambisonic 编码：方向误差 ≤10° 时多数阵列空间相关与 EQ 改善。ITA/3D3A HRTF 上 FOC 分布标准差约 10–30 mm；阵列 FOC 校准可改善 HRTF 延时图矢状对称性。

## 结论
作者认为 FOC 是声学定义的参考中心，可消除测量定位不确定并支撑有限阶下游处理；能力限于平移，其他指向性缺陷需另法。

## 点评
把“找中心”从几何直觉变成可优化的能量准则，对不规则消费级阵列很实用。用例侧重展示行为而非冲榜；高阶目标更平坦、需正则，物理位置与 FOC 的差距何时关键仍依赖场景。
