# End-Fire Degradation-Robust DOA Estimation for Compact Linear Microphone Arrays

- 论文编号：2156
- 报告人：Zheng Wen
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wen26c_interspeech.pdf

## 问题
紧凑均匀线阵在端射附近 DOA 误差显著增大；既往多作经验现象。本文从远场平面波下 TDOA→方位非线性逆映射的病态性解释该退化，并在不增大孔径、无训练条件下提出缓解方法与真实数据集。

## 方法
理论：τ∝cosθ，|∂θ/∂τ|∝1/|sinθ|，Fisher/CRLB 在端射发散。在 reliability-aware PHAT-β 框架上提出：(1) W-SRP-PHAT——逆方差启发加权的 SRP；(2) GCC-WLS——过采样、物理约束时延搜索，并在余弦域 u=cosθ 做加权最小二乘融合后再一次 arccos，避免反复放大误差。自采数据：4 麦、间距 3.5 cm（孔径 10.5 cm），5×4×3 m 房间，方位 20°–160°（步长 10°），距离 1/2 m，每条件约 100–200 段 1 s 语音；端射区定义 [20°,40°]∪[140°,160°]。对比零样本 SRP-PHAT、SRP-MVDR。

## 实验与结果
1 m：W-SRP-PHAT / GCC-WLS 全向 RMSE 约 2.45°/2.43°，端射 3.18°/3.14°，S-ACC_EF 0.82，Deg. Span 0°；基线 SRP-PHAT 全向 3.31°、端射 4.83°、Span 30°。2 m 条件更难，两提案仍显著优于基线（端射约 4.46°/4.99° vs PHAT 7.71°），退化跨度仍为 0°。误差分布呈向正横侧偏置。

## 结论
端射退化源于病态 TDOA–方位映射；方差抑制加权 SRP 与余弦域融合可在紧凑阵上显著稳住端射精度，并公布配套数据集与代码。

## 点评
用 CRLB 把“端射难”说成可设计的病态逆问题，两条补救分别打在聚合与逆映射上，论证清楚。评测全是训练无关方法，贴合电视等边缘设备；局限是单房间、单阵列几何，且端射定义到 40° 偏宽，外推需谨慎。
