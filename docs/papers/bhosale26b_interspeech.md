# Dual-Geometry Manifolds for Few-shot RIR Prediction

- 论文编号：2630
- 报告人：Yoshiki Masuyama
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/bhosale26b_interspeech.pdf

## 问题
少样本跨场景 RIR 预测常把参考在静态欧氏潜空间融合，与早期反射树状层级、晚期混响平坦扩散的物理异质性冲突，易抹平早期路径并损害清晰度。

## 方法
用 Gromov \(\delta\)-hyperbolicity 实证局部声学流形由早期高双曲性过渡到晚期近欧氏，且过渡速率随房间体积变化。提出 Janus-RIR：并行双曲（Poincaré 球 + Einstein 中点）与欧氏聚合分支，上下文感知门 \(\alpha(t)\) 按时融合；早段对双曲注意力加熵惩罚。骨干沿用 xRIR 的 ResNet/坐标（及可选深度图）特征。在 AcousticRooms 上 \(K\in\{1,4,8\}\) 评测。

## 实验与结果
Janus-RIR（含 NoVision）在 EDT/\(C_{50}/T_{60}\) 上全面优于 Few-shot RIR 与 xRIR；\(K=8\) 时 NoVision 相对 xRIR \(T_{60}\) 误差约降 26%（10.53%→7.75%），并改善 \(C_{50}\)。Hard 外推距离档误差更稳。消融：纯双曲、双欧氏或仅时间门均变差；潜空间范数轨迹显示小房更快塌缩、大房更久保持双曲结构。

## 结论
按物理阶段切换潜几何可同时改善早期清晰度与晚期混响估计；模型隐式适应环境混合时间。未来拟探索早期时域最优传输插值等。

## 点评
先用 \(\hat\delta\) 度量证明几何演变，再设计门控双流形，论证链条完整。相对“加参数/加视觉”的消融说明收益来自曲率对齐。Griffin-Lim 相位重建与仿真数据仍可能限制听感与实测外推。
